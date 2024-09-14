import requests

def test_api(endpoint, data):
  response = requests.post(endpoint, data=data)
  return response.json()


endpoint = "https://stage.virtualcaresystems.org"
data = {"input1": "value1", "input2": "value2"}

response = test_api(endpoint, data)
print(response) 
