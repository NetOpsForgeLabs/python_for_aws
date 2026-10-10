import json

text = '{"ip": "10.1.1.1"}'
print(type(text))

data = json.loads(text)
print(type(data))  
