import requests
import config

print(config.users())
response = requests.get(config.users())
print(response.json())
