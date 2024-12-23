import pandas as pd
import time
import os

eeg_data = pd.read_csv('../data/eeg_data.csv', nrows=10)

def classify_frequency(band_data):
    for i in range(0, len(band_data)):
        frequency = band_data.iloc[i, 1]
        
        if frequency in range(0, 3):
            band = 'delta'
        elif frequency in range(4, 7):
            band = 'theta'
        elif frequency in range(8, 12):
            if frequency in range(8, 10):
                band = 'Lower alpha'
            else:
                band = 'Upper alpha'
        elif frequency in range(13, 30):
            if frequency in range(13, 15):
                band = 'Sensorimotor rhythm'
            elif frequency in range(16, 20):
                band = 'Lower beta'
            else:
                band = 'Higher beta'
        elif frequency in range(33, 100):
            band = 'gamma'
        else:
            band = 'Invalid'
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(band, end="\r")
        
        time_interval = band_data.iloc[1, 0] - band_data.iloc[0, 0]
        time.sleep(time_interval)

classify_frequency(eeg_data)
