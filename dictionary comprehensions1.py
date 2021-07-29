# dictionary comprehension = create dictionaries using an expresion
#           can replace for loops and certain lambda functions
#
#dictionary = {key: expression for(key,value) in iterable}

#

#cities_in_C = {key :round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print (cities_in_C)



_______________________________________________________________________

#weather = {"New York":"snowing", "Boston":"sunny","los angeles":"sunny","Chicago":"cloudy"}


#sunny_weather ={key: value for (key,value) in weather.items() if value =="sunny"}
#print (sunny_weather)

____________________________________________

#cities = {'New York': 32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}

#desc_cities = {key:("Warm" if value >= 40 else "Cold") for(key,value) in cities.items()}

__________________________________________________________________
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "Warm"

    else:
        return "Cold"



cities = {'New York': 32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
desc_cities = {key: check_temp(value) for(key,value) in cities.items()}
print(desc_cities)
