#หน้า25
squares = [x**2 for x in range(10)]
print(squares)

square_dict = {x: x**2 for x in range(5)}
print(square_dict)

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)