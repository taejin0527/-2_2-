import csv
from datetime import datetime, timedelta

station = list()
day = list()
bus = list()
time = list()
f1 = open('data1.csv', 'r', encoding='utf-8')
f2 = open('data2(월).csv', 'r', encoding='utf-8')
#f3 = open('data3.csv', 'w', encoding='utf-8', newline='')
f4 = open('out(월).txt', 'w')
#wr = csv.writer(f3)

rdr1 = csv.reader(f1)
rdr2 = csv.reader(f2)

for line in rdr1:
    #if line[1] == 'ENTERED' and line[3] == '1':
     #   station.append(line[7]) #버스가 첫번째 정류장 enter 한 시간
    if line[1] == 'LEFT_LAST':
        station.append(line[7])  #버스가 left_last 한 시간
#station에는 enter, left_last 한 날짜와 시간이 저장되어 있음...
print("here")
for line in rdr2:
    bus.append(line[0])
count = 0
for i in range(len(station)):
    for j in range(len(bus)):
        if station[i][0:10] == bus[j][0:10]:
            time1 = datetime(int(station[i][0:4]), int(station[i][5:7]), int(station[i][8:10]), int(station[i][11:13]),
                             int(station[i][14:16]), int(station[i][17:19]))
            time2 = datetime(int(bus[j][0:4]), int(bus[j][5:7]), int(bus[j][8:10]), int(bus[j][11:13]),
                             int(bus[j][14:16]), int(bus[j][17:19]))
            print(time1)
            print(time2)
            date = time1-time2
            day.append(str(date))
            count = count+1

print(count)
print(len(day))
for i in range(len(day)):
    #print(day[i])
    #wr.writerow(day[i])
    f4.write(day[i])
    f4.write('\n')

f1.close()
f2.close()
#f3.close()
f4.close()
