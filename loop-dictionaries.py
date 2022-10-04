person = {
    "name": "Allen",
    "age": 20,
    "address":"USA"
}

print(person.items())
#for key in person:
   # print(f"key:{key} value:{person[key]}")

for key, value in person.items():
    print(f"key:{key} value:{value}")
