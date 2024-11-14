import numpy as np
import matplotlib.pyplot as plt

# Data contoh: Waktu belajar (x) dalam jam dan nilai yang diperoleh (y)
waktu_belajar = np.array([1, 2, 3, 4, 5, 6, 7, 8])
nilai = np.array([55, 60, 62, 70, 65, 78, 85, 88])

# Menghitung koefisien regresi linear
n = len(waktu_belajar)
mean_x = np.mean(waktu_belajar)
mean_y = np.mean(nilai)

# Menghitung nilai b (slope) dan a (intercept)
b = np.sum((waktu_belajar - mean_x) * (nilai - mean_y)) / np.sum((waktu_belajar - mean_x)**2)
a = mean_y - b * mean_x

# Membuat fungsi garis regresi
def garis_regresi(x):
    return a + b * x

# Plot scatter data
plt.scatter(waktu_belajar, nilai, color='blue', label='Data Asli')
plt.plot(waktu_belajar, garis_regresi(waktu_belajar), color='red', label=f'Garis Regresi: y = {a:.2f} + {b:.2f}x')

# Menambahkan label dan judul
plt.xlabel('Waktu Belajar (jam)')
plt.ylabel('Nilai')
plt.title('Regresi Linear antara Waktu Belajar dan Nilai')
plt.legend()
plt.grid(True)
plt.show()