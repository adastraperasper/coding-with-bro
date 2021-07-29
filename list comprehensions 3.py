# list comprehension = a way ti create a new list with less syntax
#                   can mimic certain lambda functions, easier to read
# list = [expression for item in iterable ]


squares =[] # create an empty list
for i in range (1,11): # create a for loop
    squares.append(i*i) #define what each loop iteration should do

print (squares)    


squares = [i * i for i in range(1,11)]
print(squares)
