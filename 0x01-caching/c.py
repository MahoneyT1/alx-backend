data = {
    "name": "hary",
    "age": 46,
    "height": 1.67
}

data.pop("name")
first_item = next(iter(data))
print(first_item)