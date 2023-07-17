import json

data = """
[
{
"id": "001",
"name": "Chuck",
"x" : "2"
},
{
"id": "009",
"name": "Dora",
"x" : "7"
}
]
"""

info = json.loads(data)

print("User Count:", len(info))

for item in info:
    print("Name:", item["name"])
    print("Id:", item["id"])
    print("Atrr:", item["x"])
