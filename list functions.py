lucky_numbers = [4,8, 15, 22, 33, 22, 24,12, 18, 44, 76]
friends =["bob", 'jim', 'karen', 'melissa',"quebec", "quebec"]
friends.append("ana")
friends.insert(1, "Kelly")
friends.remove("quebec")
friends.pop()
print(friends.index("melissa"))
print(friends.count("quebec"))


friends2 = friends.copy()
print(friends)
