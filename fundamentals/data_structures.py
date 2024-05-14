"""
    Difference between List, Tuple, Set and Dictionary
    List - square braces
    Tuple - rounded braces
    Set - The set keyword or curly braces
    Dictionary - curly braces: made up of key-value pairs

"""

list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8]
list1[0] = "PC"
print(list1, type(list1))

tuple1 = ("Computer", "Printer", "TV", "Camera", 89, 30.8)
print(tuple1, type(tuple1))

set1 = set(["Computer", "Printer", "TV", "Camera", 89, 30.8])
set2 = {"Computer", "Printer", "TV", "Camera", 89, 30.8}
print(set1, type(set1))
print(set2, type(set2))

dict1 = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}
print(dict1, type(dict1))