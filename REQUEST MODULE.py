import requests
import pandas as pd
response = requests.get("https://api.github.com")
# print(response.status_code)
# print(dir(response))
# print(response.text)
# print("hello" , response.json)
# print("hello",response.json())
set = pd.DataFrame(response.json())



import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)


import requests

student = {
    "name": "Vedant",
    "age": 20
}

response = requests.post(
    "https://example.com",
    json=student
)


import requests

my_headers = {
    "User-Agent": "Vedant-App"
}

response = requests.get(
    "https://api.github.com",
    headers=my_headers
)

print(response.status_code)



import requests

headers = {
    "User-Agent": "Vedant-App"
}

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

print(response.json())






import requests

username = input("Enter username: ")

response = requests.get(
    f"https://api.github.com/users/{username}"
)

data = response.json()






import requests

params = {
    "name": "Vedant",
    "course": "Python"
}

response = requests.get(
    "https://httpbin.org/get",
    params=params
)

print(response.json())


import requests

try:
    response = requests.get(
        "https://api.github.com"
    )

    response.raise_for_status()

    print("Success")

except Exception as e:
    print("Error:", e)



import requests
URL = "https://catfact.ninja/fact"
response = requests.get(URL)    
print(response.text)
print(dir(response))
print(response.status_code)
print(response.ok)
print(response.json)
print(response.history)
print(response.raise_for_status)
print(response.connection)
# print(response.cookies.get_dict())
print(response.__sizeof__)
print(response.headers)


import requests
URL = "https://catfact.ninja/fact"

for i in range(10):
    try:
       response = requests.get(URL, timeout = 0.1)    
       print(response.text)
       print(response.status_code)
       break
    except Exception as e:
        print("Timeout error")
else:
    print("All retries are Failled")        