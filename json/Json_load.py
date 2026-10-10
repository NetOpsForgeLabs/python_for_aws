import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
# print(data.keys())
print("\n")
print("name: ",data["name"])  
print("contact: ",data["contact"])  
print("\n")
