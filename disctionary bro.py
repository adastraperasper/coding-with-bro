#dictionary = a changeble, unordered collection of u nique key:value pairs
#             fast becaus eit is using hashing

capitals={'usa':'Washinton DC', 'india':"beijing", "china":"beijing", "Russia":"moscow"}


capitals.update({'Germany':"berlin"})

capitals.update({'india':'taj mahal'})

capitals.pop('china')



print(capitals['Russia'])

print(capitals.get("poland"))

print(capitals.keys())

print(capitals.values())

for key,value in capitals.items():
    print (key, value)


    
