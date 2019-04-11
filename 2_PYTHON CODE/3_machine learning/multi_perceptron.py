import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import RMSprop

np.random.seed(7)

xy = np.loadtxt('/Users/taejin/Desktop/거리(월요일).csv', delimiter=',', dtype=np.float32, encoding='utf-8-sig')

x_data = np.array(xy[:, 0:-1], dtype=np.float32)
y_data = np.array(xy[:, -1], dtype=np.float32)
y_data = y_data.reshape(12965, 1)

rmsprop = RMSprop(lr=0.0001)

model = Sequential()
model.add(Dense(64, input_dim=2,  activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, input_dim=2))
model.compile(loss='mse', optimizer=rmsprop)
model.summary()

hist = model.fit(x_data, y_data, epochs=20)
print(hist.history.keys())

plt.plot(hist.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

print(model.predict(np.array([59.4, 41]).reshape(1, 2))) #9초
print(model.predict(np.array([105.9, 58]).reshape(1, 2))) #39초
print(model.predict(np.array([495.5, 81]).reshape(1, 2))) #330
print(model.predict(np.array([1023.2, 79]).reshape(1, 2))) #801


"""""
x = np.linspace(20, 100, 50).reshape(50, 1)
y = np.linspace(10, 70, 50).reshape(50, 1)

X = np.concatenate((x, y), axis=1)
Z = np.matmul(X, w) + b


xs = np.array(xy[:, 0], dtype=np.float32)
ys = np.array(xy[:, 1], dtype=np.float32)
zs = np.array(xy[:, -1], dtype=np.float32)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, Z)
#ax.scatter(xs, ys, zs)
ax.set_xlabel('weight')
ax.set_ylabel('speed')
ax.set_zlabel('time')
ax.view_init(15, 15)

plt.show()
"""""