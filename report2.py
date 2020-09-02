import requests
import time

start = time.time()

report = requests.get("http://localhost:21212/report").json()

print('{:<2} {:<20}                  {:<10}           {:<10}     {}'.format('ID:', 'Name:', 'Num Loc:', 'Avg value:','Categories:'))

for r in report:
    #print({}      ).format(str(r[0]) + "\t\t\t" + str(r[1]) + "\t\t\t\t" + str(r[2]) + "\t\t\t" + str(r[3]) + "\t\t\t" + str(r[4]))
    print('{:<1}   {:<20}                   {:<10}          {:<10}     {}'.format(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4])))

end = time.time()

time = end - start
final_time = round(time,2)

print("")
print("Program time is: " + str(final_time) +" seconds")