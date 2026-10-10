import json
from pathlib import Path

# Specify the path to the JSON file using pathlib
path = Path("data.json")
# print(type(path))
file_load = json.loads(path.read_text())
# print(type(file_load))
print("\n")
# print(file_load.keys())
for var_loc in file_load["labs"]:
    # print(var_loc.keys())
    if var_loc["location"] == "USA":
        print("Name: ", var_loc["name"],"Contact: ", var_loc["contact"])
