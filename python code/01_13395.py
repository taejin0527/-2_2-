import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csv 파일 읽기
# 속성 이름 = ['get_date', 'lat', 'lng', 'speed', 'line_no']
data = pd.read_csv("/Users/taejin/Desktop/201801.csv", names=['get_date', 'lat', 'lng', 'speed', 'line_no'])

###
# Data configure

# print("#####data#######")
# print(data[data['get_date'] < '2018.01.02 00:00:00'])
# print(data.loc[ (data['get_date']>'2018.01.02 00:00:00')&(data['get_date']<'2018.01.03 00:00:00'), :])
# print(data.loc[ (data['get_date']>'2018.01.03 00:00:00')&(data['get_date']<'2018.01.04 00:00:00'), :])
# print(data.tail())
# print(data.describe())
# print(data.shape)
###

# c_bin = data.loc[(data['get_date']<'2018.01.02 00:00:00'), ['lat', 'lng']]
# print(np.array(c_bin, dtype="float").shape[0])

lat = data.loc[(data['get_date']<'2018.01.02 00:00:00'), 'lat']
lng = data.loc[(data['get_date']<'2018.01.02 00:00:00'), 'lng']
x1 = np.array(lat, dtype="float")
y1 = np.array(lng, dtype="float")
lat = data.loc[(data['get_date']>'2018.01.02 00:00:00')&(data['get_date']<'2018.01.03 00:00:00'), 'lat']
lng = data.loc[(data['get_date']>'2018.01.02 00:00:00')&(data['get_date']<'2018.01.03 00:00:00'), 'lng']
x2 = np.array(lat, dtype="float")
y2 = np.array(lng, dtype="float")
lat = data.loc[(data['get_date']>'2018.01.03 00:00:00')&(data['get_date']<'2018.01.04 00:00:00'), 'lat']
lng = data.loc[(data['get_date']>'2018.01.03 00:00:00')&(data['get_date']<'2018.01.04 00:00:00'), 'lng']
x3 = np.array(lat, dtype="float")
y3 = np.array(lng, dtype="float")
lat = data.loc[(data['get_date']>'2018.01.04 00:00:00')&(data['get_date']<'2018.01.05 00:00:00'), 'lat']
lng = data.loc[(data['get_date']>'2018.01.04 00:00:00')&(data['get_date']<'2018.01.05 00:00:00'), 'lng']
x4 = np.array(lat, dtype="float")
y4 = np.array(lng, dtype="float")
lat = data.loc[(data['get_date']>'2018.01.05 00:00:00')&(data['get_date']<'2018.01.06 00:00:00'), 'lat']
lng = data.loc[(data['get_date']>'2018.01.05 00:00:00')&(data['get_date']<'2018.01.06 00:00:00'), 'lng']
x5 = np.array(lat, dtype="float")
y5 = np.array(lng, dtype="float")
lat = data.loc[(data['get_date']>'2018.01.06 00:00:00')&(data['get_date']<'2018.01.07 00:00:00'), 'lat']
lng = data.loc[(data['get_date']>'2018.01.06 00:00:00')&(data['get_date']<'2018.01.07 00:00:00'), 'lng']
x6 = np.array(lat, dtype="float")
y6 = np.array(lng, dtype="float")

# list11 = [float(x) for x in x1]
# list12 = [float(y) for y in y1]
# print(x1)
# print(y1)

# plt.figure()
# plt.scatter(list1, list2)
# plt.show()

###
# draw scatter graph

f, axarr = plt.subplots(3, 2, figsize=(15,20))
f.suptitle('BUS 13395 route')
axarr[0, 0].scatter(x1, y1)
axarr[0, 0].set_title('Day 1')
axarr[0, 1].scatter(x2, y2)
axarr[0, 1].set_title('Day 2')
axarr[1, 0].scatter(x3, y3)
axarr[1, 0].set_title('Day 3')
axarr[1, 1].scatter(x4, y4)
axarr[1, 1].set_title('Day 4')
axarr[2, 0].scatter(x3, y3)
axarr[2, 0].set_title('Day 5')
axarr[2, 1].scatter(x4, y4)
axarr[2, 1].set_title('Day 6')
plt.show()
