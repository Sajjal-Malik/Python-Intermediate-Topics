import json

car = {"brand": "Ford", "model": "Mustang", "year": 1964, "new": True, "colors": ["red", "white", "blue"]}

carJSOn = json.dumps(car, indent=2)
# carJSOn = json.dumps(cars, indent=2, sort_keys=True)

print(carJSOn) 
print(type(carJSOn))


# with open('car.json', 'w') as file:
#     json.dump(car, file, indent=2)



with open('car.json', 'r') as file:
    reading = file.read()
    print(reading)





car = json.loads(carJSOn)
print(car)
print(type(car))


with open('car.json', 'r') as file:
    car = json.load(file)
    print(car)