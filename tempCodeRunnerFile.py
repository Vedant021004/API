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