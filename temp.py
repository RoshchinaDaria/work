import requests
headers = { 'Content-Type': 'application/json'}
data={
  "email": "teвstjhbvj3ц3вhwrbv@mail.com",
  "device_id": "70c9c4e9ad15088c46561c0310ad14c6750f1518",
  "password": "Qwerty123!",
  "product_focus": "extension",
  "source": "stage.irsextension.online"
}
response = requests.post("https://stage.irsextension.online/api/register", headers=headers, json=data)
print(response.json())

trigger = [master]
b = {"a":1}
