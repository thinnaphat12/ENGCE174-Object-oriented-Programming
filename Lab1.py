#หน้า25
squares = [x**2 for x in range(10)]
print(squares)

square_dict = {x: x**2 for x in range(5)}
print(square_dict)

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

#หน้า26
square = lambda x: x**2
print(square(5))

#หน้า27
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next(fib))

#หน้า28
numbers = [1, 2, 3, 4, 5]

print("First elememt:", numbers[0])
print("Last elememt:", numbers[-1])

print("Sliced elememts:", numbers[2:4])

numbers.append(6)
print("After append:", numbers)

numbers.remove(3)
print("After removeal:", numbers)

#หน้า29
even_numbers = [x for x in range(10) if x % 2 == 0]
squares = [num**2 for num in even_numbers]
print("Squares of even numberes:", squares)

#หน้า30
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New york", "Los Angeles", "Chicago"]

for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} year old and lives in {city}")

#หน้า31
coordinates = (3, 5)

x, y = coordinates
print("x-coordinate:", x)
print("y-coordinate:", y)

location = {(3, 5): "home", (10, 20): "Office"}
print("Location at (3, 5):", location[(3, 5)])

#หน้า32
from collections import namedtuple

Point = namedtuple('Poinnt', ['x', 'y'])

p1 = Point(3, 5)
p2 = Point(-1, 2)

print("Coodinates of p1:", p1.x, p1.y)
 
#หน้า33
coordinates = (3, 5)

#หน้า34
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print("Name:", person['name'])

person['age'] = 31
print("Updated age:", person['age'])

for key, value in person.items():
        print(f"{key}: {value}")

#หน้า35
numbers = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in numbers}
print("Dictinoary of squares:", square_dict)

#หน้า36
person = {'name': 'Alice', 'age' : 30}

city = person.get('city', 'Unknown')
print("City:", city)

#หน้า37
cities = {
    'New York' : [32, 25,30, 28, 35],
    'Los Angeles': [75 ]
}