import matplotlib.pyplot as plt
import pandas as pd
import time

data = pd.read_csv('eeg_data.csv')

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], label='EEG Data', color='b')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title('Live EEG Data Plot')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()

def update_plot(data):
    line.set_xdata(range(len(data)))
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.1)

for i in range(1, len(data)):
    live_data = data.iloc[:i]['value']
    update_plot(live_data)
    time.sleep(0.1)

plt.ioff()
plt.show()
