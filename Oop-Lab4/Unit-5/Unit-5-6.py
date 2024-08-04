# Page 20
# Given a list of number, remove all occurrences of a specific number and calculate the sum of remaining number.

numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]
remove_num = 3

while remove_num in numbers:
    numbers.remove(remove_num)

print("Numbers after removeal:", numbers)
print("Sum of remaining numbers:", sum(numbers))