dict = {
    "name": "Nika",
    "age": 16,
    "surname": "Gigani",
    "academy": "GOA",
    "fav-color": "red",
    "year": 1995
}

total_sum = 0

for value in dict.values():
    if isinstance(value, int):
        total_sum += value

print(total_sum)