# list comprehension = a way ti create a new list with less syntax
#                   can mimic certain lambda functions, easier to read
# list = [expression for item in iterable if]

students = [100,90,80,70,60,50,40,30,20,10,0]

#passed_students = list(filter(lambda x : x >= 60, students))

passed_students = [i for i in students if i >= 60]

passed_students =[i if i >= 60 else "Failed" for i in students]
print(passed_students)
 
