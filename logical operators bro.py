# logical operators (and, or, not ) = used to check 2 or more conditionds are true

temp = int(input("What is teh temperature outside ?:"))

if not (temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("Go outside")

elif not (temp < 0 or temp >30):
    print("Temp is bad today")
    print("Stay inside")
