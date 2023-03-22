fruits = ["apple", "banana", "grape", "orange"]
empty_fruits = []
other_fruits = list()

print(fruits)
print(fruits[2])
print(fruits[-1])

fruits[2] = "mango"
print(fruits)

fruits_length = len(fruits)
print(fruits_length)

fruits.append("Pear")
print(fruits)

fruits.pop()
print(fruits)

fruits.insert(1, "Kiwi")
print(fruits)
