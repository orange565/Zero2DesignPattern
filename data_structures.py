list1 = [3, 5, 2, ]
list2 = [6, 9, 1, 2, 4]

a = [(x,y) for x in list1 for y in list2]

print(a)

fruits = ["Elma","Muz","Kiraz"]
print(fruits[0])
fruits[1] = "Uzum"
fruits.append("Karpuz")
fruits.remove("Elma")
print(fruits)
fruits.pop()
print(fruits)
fruits.append("Armut")
print(fruits)

point = {3,5}
x,y = point
print(x)
print(y)

student = {
    "name" : "Alice",
    "age" : 22,
    "courses": ["Math","History"]
}

print(student["name"])
student["age"]=23
student["courses"].append("Science")

print(student)

students = [{
    "name" : "Alice",
    "age" : 22,
    "courses": ["Math","History"]
},{
    "name" : "Robert",
    "age" : 23,
    "courses": ["Math","History"]
},{
    "name" : "John",
    "age" : 24,
    "courses": ["Math","History"]
}]

print(students[1]["name"])
students[1]["age"]=23
students[1]["courses"].append("Science")

print(students[1])
print("------")
print(students[1:3])

numbers = [1,2,3,4,5]
squad_numbers = [x**3 for x in numbers]
print(squad_numbers)
even_squad_numbers = [x**3 for x in numbers if (x**3)%2 == 0]
print(even_squad_numbers)