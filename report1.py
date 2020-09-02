import requests
import time
areas = requests.get("http://localhost:21212/areas").json()

start = time.time()

print('{:<2} {:<20}                  {:<10}          {:<10}     {}'.format('ID:', 'Name:', 'Num Loc:', 'Avg value:', 'Categories:'))
for area in areas:
        num_locations = requests.get("http://localhost:21212/area/" + str(area[0]) + "/number_locations").json()
        if num_locations is None:
            num_locations = 0
        else:
            num_locations = int(num_locations)

        avg_value = requests.get("http://localhost:21212/area/" + str(area[0]) + "/average_measurement").json()

        if avg_value is None:
            avg_value = "-----"
        else:
            avg_value = round(avg_value, 2)

        categories = requests.get("http://localhost:21212/area/" + str(area[0]) + "/categories").json()

        cat_string = ""
        for category in categories:
            cat_string += category['name'] + ", "
       # print(str(area[0]) + "\t" + str(area[1]) + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(num_locations) + "\t\t\t\t\t\t\t\t" + str(avg_value) + "\t\t\t\t" + cat_string[:-2])
        print('{:<1}   {:<20}                   {:<10}          {:<10}     {}'.format(str(area[0]), str(area[1]), str(num_locations), str(avg_value), cat_string[:-2]))





end = time.time()
time = end - start
final_time = round(time, 2)
print("")
print("Program time: " + str(final_time) + " seconds")