#หน้า30
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New york", "Los Angeles", "Chicago"]

for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} year old and lives in {city}")