# sort() method = used with lists
# sort() function = used with iterables
# does not work with tupples ()

students = [("john","F",50),
            ("mary","E",50),
            ("bob","D",50),
            ("joe","C",36),
            ("mellissa","B",21),
            ("jack","A",30)]






age = lambda ages:ages[2]
# students.sort(key= age)
sorted_students = sorted(students, key = age)

for i in students:
    print (i)



