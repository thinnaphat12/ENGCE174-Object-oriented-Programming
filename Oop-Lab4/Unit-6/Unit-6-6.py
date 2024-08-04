# Page 16
# Example 5 : Using sets for unique operations

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

unique_elements = set(list1).union(set(list2)).difference(set(list3))
print("Unique elements:", unique_elements)