import csv
import json

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

#with open("myfiles/students.json","w") as json_file:
#    json.dump(students[0],json_file)

with open("myfiles/students.json","r") as json_file:
    new_student = json.load(json_file)

print(new_student['courses'])


#with open("myfiles/first.csv","w") as csv_file:
#    csv_writer = csv.writer(csv_file)
#
#    csv_writer.writerow(['2','4','6'])
#    csv_writer.writerow(['5','7','12'])
#    csv_writer.writerow(['8','10','18'])

#with open("myfiles/first.csv","r") as csv_file:
#    csv_reader= csv.reader(csv_file)
#
#    for row in csv_reader:
#        print(row)


""" file = open("myfiles/first.txt","a+")

file.write("Hello NTT")
str_value = file.read()
file.close()


#print(str_value) """

#file = open("myfiles/first.csv","r+")
#file.write("a,b,c\n")
#file.write("1,2,3")
#file.close()