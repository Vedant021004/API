import json

text = '{"name":"Vedant","age":20}'

data = json.loads(text)

print(data)
print(type(data))

# 

import json

person = {
    "name": "Vedant",
    "age": 20
}

json_data = json.dumps(person)

print(json_data)
print(type(json_data))


data = {
    "name": "Vedant",
    "age": 20
}

print(data["name"])

# nested jason
import json
data = {
    "name" : "vedant",
    "age" : 21,
    "love" : {
            "name": "riddhikapil",
            "marry": "soon"
        }   
}
print(data['age'])
print(data['love']["name"])


# json array
import json
array = {
    "name" : "vedantriddhik",
    "love" : "mwaah",
    "skills" : 
    [
        
        "mmm",
        "missi"

    ]
}
new = json.dumps(array)
print(array['name'])
print(array["skills"][1])
print(new)



# 
import json

with open("data.json") as file:
    data = json.load(file)

print(data["name"])

# 

import json

data = {
    "name": "Vedant",
    "love": "riddhi"
}

with open("data.json", "w") as file:
    json.dump(data, file)



import json

json_data = '{"name":"Vedant"}'

data = json.loads(json_data)

print(data["name"])    


import json

data = {
    "name": "Vedant"
}

json_data = json.dumps(data)

print(json_data)


