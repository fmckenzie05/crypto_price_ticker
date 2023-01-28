import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
  "start": "1",
  "limit": "1",
  "convert": "USD"
}
headers = {
  "Accepts": "application/json",
  "X-CMC_Pro_API_Key": "bf720a9a-811e-4dff-9fb8-5635f7416a23"
}

response = requests.get(url, params=parameters, headers=headers)

data = response.json()

print(data)