from http import HTTPStatus

from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from .models import Drink
from .serializers import DrinkSerializer

@api_view(["GET", "POST"])
def drink_list(request,format=None):
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({'drinks':serializer.data},)

    if request.method == "POST":
        # get the json data from the request
        serializer = DrinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


# this is required for rest framework to render the view that lets you post data
@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request,id,format=None):
    """
    :param request:
    :param id: the pk passed from the url
    :return:
    """
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        return Response(status=HTTP_204_NO_CONTENT)