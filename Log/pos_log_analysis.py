import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path = 'pos_log.txt'

df = pd.read_csv(file_path, sep=" ", header=None)

time = df[0]
rotation_angles = df.iloc[:, 1:4]
position = df.iloc[:, 4:7] 
velocity = df.iloc[:, 10:13]
bias_gyro = df.iloc[:, 13:16]
bias_acc = df.iloc[:, 16:19]
gravity = df.iloc[:, 22:25] 

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(position[4], position[5], position[6], label='Position')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.legend()
plt.title("3D Position Plot")
plt.show()

fig, axs = plt.subplots(5, 1, figsize=(15, 20), sharex=True)

axs[0].plot(time, rotation_angles.values)
axs[0].set_ylabel('Rotation Angles')
axs[0].legend(['X', 'Y', 'Z'], loc='upper right')

axs[1].plot(time, velocity.values)
axs[1].set_ylabel('Velocity')
axs[1].legend(['X', 'Y', 'Z'], loc='upper right')

axs[2].plot(time, bias_gyro.values)
axs[2].set_ylabel('Gyroscope Bias')
axs[2].legend(['X', 'Y', 'Z'], loc='upper right')

axs[3].plot(time, bias_acc.values)
axs[3].set_ylabel('Accelerometer Bias')
axs[3].legend(['X', 'Y', 'Z'], loc='upper right')

axs[4].plot(time, gravity.values)
axs[4].set_ylabel('Gravity')
axs[4].legend(['X', 'Y', 'Z'], loc='upper right')

plt.suptitle('Time Series Plots')
plt.show()