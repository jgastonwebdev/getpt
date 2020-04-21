import populartimes # https://github.com/m-wrzr/populartimes
#import googlemaps
import json
from datetime import datetime
import sys
#from pytz import timezone



api_key = 'AIzaSyBxSQjyY8sx2ubPotvlNN1u_X-Qt5ycvmg'

place_id = "ChIJq6qqqq64yIkRbu4kO2vTskM"

pt = populartimes.get_id(api_key, place_id)


today = datetime.now()

dayofweek = int(today.strftime("%w"))

ptdata = pt['populartimes'][dayofweek]['data']



results = ptdata
notzero = []
for x in results:
    if x > 0:
        notzero.append(x)


notzero.sort()

if results.index(notzero[0]) == 0:
    print('12 AM')

if results.index(notzero[0]) == 1:
    print('1 AM')

if results.index(notzero[0]) == 2:
    print('2 AM')

if results.index(notzero[0]) == 3:
    print('3 AM')

if results.index(notzero[0]) == 4:
    print('4 AM')

if results.index(notzero[0]) == 5:
    print('5 AM')

if results.index(notzero[0]) == 6:
    print('6 AM')

if results.index(notzero[0]) == 7:
    print('7 AM')

if results.index(notzero[0]) == 8:
    print('8 AM')

if results.index(notzero[0]) == 9:
    print('9 AM')

if results.index(notzero[0]) == 10:
    print('10 AM')

if results.index(notzero[0]) == 11:
    print('11 AM')

if results.index(notzero[0]) == 12:
    print('12 PM')

if results.index(notzero[0]) == 13:
    print('1 PM')

if results.index(notzero[0]) == 14:
    print('2 PM')

if results.index(notzero[0]) == 15:
    print('3 PM')

if results.index(notzero[0]) == 16:
    print('4 PM')

if results.index(notzero[0]) == 17:
    print('5 PM')

if results.index(notzero[0]) == 18:
    print('6 PM')

if results.index(notzero[0]) == 19:
    print('7 PM')

if results.index(notzero[0]) == 20:
    print('8 PM')

if results.index(notzero[0]) == 21:
    print('9 PM')

if results.index(notzero[0]) == 22:
    print('10 PM')

if results.index(notzero[0]) == 23:
    print('11 PM')


