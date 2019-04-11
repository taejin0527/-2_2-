import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csv 파일 읽기
# 속성 이름 = ['line_no', 'inout_type', 'seq', 'stop_name', 'x', 'y', 'get_date']
#             버스 번호,    출발/도착,     순서,    정거장 이름,  lng, lat,     시간
data = pd.read_csv("/Users/taejin/Desktop/13395_stop_raw.csv", names=['line_no', 'inout_type', 'seq', 'stop_name', 'x', 'y', 'get_date'])

data2 = pd.read_csv("/Users/taejin/Desktop/201801.csv", names=['get_date', 'lat', 'lng', 'speed', 'line_no'])

# print(data.head(10))

lat = data.loc[(data['get_date']>'2018.01.02 00:00:00')&(data['get_date']<'2018.01.03 00:00:00'), 'y']
lng = data.loc[(data['get_date']>'2018.01.02 00:00:00')&(data['get_date']<'2018.01.03 00:00:00'), 'x']
x1 = np.array(lat, dtype="float")
y1 = np.array(lng, dtype="float")

lat = data2.loc[(data2['get_date']>'2018.01.02 00:00:00')&(data2['get_date']<'2018.01.03 00:00:00'), 'lat']
lng = data2.loc[(data2['get_date']>'2018.01.02 00:00:00')&(data2['get_date']<'2018.01.03 00:00:00'), 'lng']
x2 = np.array(lat, dtype="float")
y2 = np.array(lng, dtype="float")

print(x1, y1)

plt.figure(figsize=(20,20))
plt.scatter(y1, x1, color='r')
plt.plot(y2, x2)
plt.show()