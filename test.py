import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

# print(data)
arr = pd.DataFrame(data)
print(arr['name'])