import csv
from datetime import datetime, timedelta

header = []
name = ['9월.csv', '10월.csv', '11월.csv']
line_counter = 0

bus2 = []
bus3 = []
bus4 = []
bus5 = []
bus6 = []

for i in range(3):
    with open(name[i]) as f2:
        line_counter = 0
        while 1:
            data = f2.readline().replace("\n", "")
            #print(data)
            #print(data)
            if not data:
                break
            if line_counter == 0:
                print("here")
                header = data.split(",")
            else:   # 1부터 7까지 일요일, 월요일 ... 토요일 순서
                if datetime(int(data.split(",")[0][0:4]), int(data.split(",")[0][5:7]), int(data.split(",")[0][8:10]),
                            int(data.split(",")[0][11:13]), int(data.split(",")[0][14:16]),
                            int(data.split(",")[0][17:19])).weekday() == 0:
                    print("here")
                    bus2.append(data.split(","))
                elif datetime(int(data.split(",")[0][0:4]), int(data.split(",")[0][5:7]), int(data.split(",")[0][8:10]),
                              int(data.split(",")[0][11:13]), int(data.split(",")[0][14:16]),
                              int(data.split(",")[0][17:19])).weekday() == 1:
                    bus3.append(data.split(","))
                elif datetime(int(data.split(",")[0][0:4]), int(data.split(",")[0][5:7]), int(data.split(",")[0][8:10]),
                              int(data.split(",")[0][11:13]), int(data.split(",")[0][14:16]),
                              int(data.split(",")[0][17:19])).weekday() == 2:
                    bus4.append(data.split(","))
                elif datetime(int(data.split(",")[0][0:4]), int(data.split(",")[0][5:7]), int(data.split(",")[0][8:10]),
                              int(data.split(",")[0][11:13]), int(data.split(",")[0][14:16]),
                              int(data.split(",")[0][17:19])).weekday() == 3:
                    bus5.append(data.split(","))
                elif datetime(int(data.split(",")[0][0:4]), int(data.split(",")[0][5:7]), int(data.split(",")[0][8:10]),
                              int(data.split(",")[0][11:13]), int(data.split(",")[0][14:16]),
                              int(data.split(",")[0][17:19])).weekday() == 4:
                    bus6.append(data.split(","))
            line_counter = line_counter + 1

#print(header)
#print(bus2)
#print(bus3)
#print(bus4)
#print(bus5)
#print(bus6)

bus = [bus2, bus3, bus4, bus5, bus6]
print(bus[0])
name2 = ['월요일.csv', '화요일.csv', '수요일.csv', '목요일.csv', '금요일.csv']
for i in range(5):
    with open(name2[i], 'w') as f3:
        f3.write(",".join(header)+'\n')
        for j in bus[i]:
            f3.write(",".join(j)+'\n')

