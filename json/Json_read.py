
# Import the JSON module to work with JSON data
import json

# Specify the path to the downloaded AWS IP ranges JSON file
path = r"C:\Users\rajatx\Downloads\ip-ranges.json" # Keep your system file path

# Open the JSON file in read mode
with open(path, "r", encoding="utf-8") as file:

    # Parse the JSON file into a Python dictionary
    data = json.load(file)

    # Display the top-level keys in the JSON data
    # print(data.keys())

    # Check the data type of the parsed JSON
    # print(type(data))

    # Iterate through each entry in the AWS IPv4 prefixes list
    for service_name in data["prefixes"]:

        # Filter IP ranges by AWS service and Region
        if service_name["service"] == "ROUTE53_HEALTHCHECKS" and service_name["region"] == "us-west-2":

            # Display the matching IPv4 CIDR range
            print(service_name["ip_prefix"])
