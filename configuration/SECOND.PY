import requests
import config
import pandas as pd

print(config.users())
response = requests.get(config.users())
data = response.json()
print(type(data))

arr = pd.DataFrame(data)
print(arr)