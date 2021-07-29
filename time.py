import time

print(time.ctime(0))#since time bagn for the computer 
print(time.time())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
time_object = time.gmtime()

time.string= "20 April, 2020"
time.strptime(time_string,"%d %B, %Y")

local_time = time.strftime("%B %d %Y %H %M %S", time_object)
print(local_time)
