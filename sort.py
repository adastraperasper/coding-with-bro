# sort() method = used with lists
# sort() function = used with iterables
# does not work with tupples ()
students = ["Squid", "Sandt", "Patrick","Gina","Joe","Chair" ]
#students.sort(reverse= True)
sorted_students = sorted (students, reverse= True)

for i in students:
    print(i)
