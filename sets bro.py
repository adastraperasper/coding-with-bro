#set = collection which is unordered, unindexed. no duplicate values

utensils ={"fork", "spoon", "knife", "spoon" }
dishes ={"bowl", "plate","cup", "knife"}


utensils.add("napkin")
utensils.remove("fork")

dishes.update(utensils)

dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dishes:
    print(x)
