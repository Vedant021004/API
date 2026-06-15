import config
import requests

URL = config.users()
print(URL)


headers = {
    "Authorization": "Bearer 25a9f1cfc8ebc5671f3f2e4ab2789da334ca22acd74b4d6b8f36b62e18a1ffa2"
}

name = input("please enter your name : ")
email = input("please enter your email : ")
status = input("please enter your status : ")
gender = input("please enter your gender : ")

data = dict()
data['name'] = name
data['email'] = email
data['status'] = status
data['gender'] = gender

post = requests.post(URL,headers = headers, data = data)
print(post)
print(post.status_code)
print(post.json())