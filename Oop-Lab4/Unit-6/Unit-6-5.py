# Page 15
# Example 4 : Set operation and methods

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.add(5)
set2.discard(6)

print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set2 a superset of set1?", set2.issuperset(set1))

