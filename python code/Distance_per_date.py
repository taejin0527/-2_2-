from math import sin, cos, sqrt, atan2, radians
from datetime import datetime, timedelta

header = []
name = ['월요일.csv', '화요일.csv', '수요일.csv', '목요일.csv', '금요일.csv']
line_counter = 0
value = 13.5
R = 6373.0


data = list()
bus = list()
date = 'a'
count = 0

with open('월요일.csv') as f2:
    line_counter = 0
    count = 0
    while 1:
        data = f2.readline().replace("\n", "")
        if not data:
            break
        if line_counter == 0:
            print("head")
            header = data.split(",")
        else:
            if data.split(",")[0][0:10] != date:  #날짜가 다르다면 line_counter = 1
                line_counter = 1
                count = 0
            if line_counter == 1:  # 날짜가 다르다면 dist에 0을 넣고 date에 현재 날짜를 집어 넣음.
                date = data.split(",")[0][0:10]
                bus.append(0)
                lat1 = radians(float(data.split(",")[1]))
                lon1 = radians(float(data.split(",")[2]))
            else:
                lat2 = radians(float(data.split(",")[1]))
                lon2 = radians(float(data.split(",")[2]))

                print(lat1, lon1)
                print(lat2, lon2)

                d_lon = lon2 - lon1
                d_lat = lat2 - lat1

                a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distance = R * c
                count = count + distance
                bus.append(value-count)
                #count = count + distance
                #print("Result:", distance)
                #print("count:", count)
                lat1 = lat2
                lon1 = lon2
        line_counter = line_counter + 1

f4 = open('거리(월).txt', 'w')
for i in range(len(bus)):
    #print(day[i])
    #wr.writerow(day[i])
    f4.write(str(bus[i]))
    f4.write('\n')

f4.close()
