# BUS 13395
import tensorflow as tf
import pandas as pd
import numpy as np
tf.set_random_seed(777)  # for reproducibility

data = pd.read_csv("/Users/taejin/Desktop/13395_mon.csv", names=['get_date', 'lat', 'lng', 'speed', 'line_no', 'y',
                                                                 'dist'])

d_data_r = data.loc[1:, 'dist']
d_data = np.array(d_data_r, dtype="float")
print(d_data_r.head())
s_data_r = data.loc[1:, 'speed']
print(s_data_r.head())
s_data = np.array(s_data_r, dtype="float")

y_data_r = data.loc[1:, 'y']
y_data = np.array(y_data_r, dtype="float")
print(y_data_r.head())

# 입력값을 받기 위한 플레이스홀더 정의
d = tf.placeholder(tf.float32)                  # 거리
#s = tf.placeholder(tf.float32, shape=[None])                  # 속도
#t = tf.placeholder(tf.float32, shape=[None])                  # 교통량
#r = tf.placeholder(tf.float32, shape=[None])                  # 강수량
# 출력값을 받기 위한 플레이스홀더 정의
Y = tf.placeholder(tf.float32)                                # 예측 시간

# 변수들 설정, 소프트맥스 회귀 모델 정의
w1 = tf.Variable(tf.random_normal([1]), name='distance')
print(w1)
"""
w2 = tf.Variable(tf.random_normal([1]), name='speed')
w3 = tf.Variable(tf.random_normal([1]), name='traffic')
w4 = tf.Variable(tf.random_normal([1]), name='rain')
"""
b = tf.Variable(tf.random_normal([1]), name='bias')
print(b)

hypothesis = w1*d + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize. Need a very small learning rate for this data set
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(1000001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={d: d_data, Y: y_data})
    if step % 50000 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
