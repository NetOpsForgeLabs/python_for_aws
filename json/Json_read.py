import json

path = r"C:\\Users\\rajatx\\Downloads\\ip-ranges.json"

with open(path, "r") as file:
    data = json.load(file)
    # print(data.keys()) #checking the data keys
    # print(type(data)) #checking the type of data
    for service_name in data["prefixes"]:
        if service_name["service"] == "ROUTE53_HEALTHCHECKS" and service_name["region"] == "us-west-2":
            print(service_name["ip_prefix"])