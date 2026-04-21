from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

import time
start_time = time.time()

# Чтение файла
filename = "23.wav"
fs, data = wavfile.read(filename)  # частота дискретизации

# Преобразование в моно канал
if len(data.shape) > 1: data = data[:, 0]

# Ввод с клавиатуры
N = int(input("Количество отсчётов: "))
N = min(N, len(data))  # защита от превышения длины

samples = data[:N]

# График отсчётов
plt.figure(figsize=(10, 5))
plt.plot(range(N), samples, '-o')
plt.title("Дискретные отсчёты сигнала")
plt.xlabel("Отсчёт")
plt.ylabel("Амплитуда")
plt.grid()
plt.show()

# Осциллограмма
timeO = np.arange(len(data)) / fs

plt.figure(figsize=(10, 5))
plt.plot(timeO, data)
plt.title("Осциллограмма")
plt.xlabel("Время, сек")
plt.ylabel("Амплитуда")
plt.grid()
plt.show()

# Мнимая часть ДПФ
fft_vals = np.fft.fft(data)
fft_imag = np.imag(fft_vals)

freqs = np.fft.fftfreq(len(data), d=1/fs)

plt.figure(figsize=(10, 5))
plt.plot(freqs, fft_imag)
plt.title("Мнимая часть ДПФ")
plt.xlabel("Частота, Гц")
plt.ylabel("Im")
plt.grid()
plt.show()

# Гистограмма
plt.figure(figsize=(10, 5))
plt.hist(data, bins=50)
plt.title("Гистограмма")
plt.xlabel("Амплитуда")
plt.ylabel("Отсчёт")
plt.grid()
plt.show()










# Проверка того, читаете ли Вы код студента до конца
print (time.time() - start_time, "seconds")