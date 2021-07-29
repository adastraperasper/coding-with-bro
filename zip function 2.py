# zip (*iterables)= aggregate elements fron two or more iterables
#  (list, tuples,sets, etc )
# creates a zip object with paired elements stored in tuples for each element

usernames = ["dude", "bro", "mister"]
passwords =["password","abc123","guest"]
users= dict(zip(usernames, passwords))
print(type(users))

for key,value in users.items():
    print(key + " :" +value)
