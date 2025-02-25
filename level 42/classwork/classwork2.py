dict = {
    "name": "Nika",
    "age": 16,
    "surname": "Gigani",
    "academy": "GOA",
    "fav-color": "black",
}

print(dict.keys())
print(dict.values())
print(dict.items())

for key, value in dict.items():
    print(f"{key} is {value}")