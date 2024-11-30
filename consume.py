import requests
print("Testing")

request = requests.get(" http://127.0.0.1:8000/drinks/")
print(request.json())