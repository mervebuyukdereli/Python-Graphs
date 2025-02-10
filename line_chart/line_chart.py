import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0, 100, 11)  # (başlangıç, bitiş, eleman sayısı)
dizi2 = dizi1 ** 2  # dizi1'in karesi alınıyor

plt.plot(dizi1, dizi2, "b*-")  

plt.title("Quadratic Function")  # Grafik başlığı
plt.xlabel("X Values")  # X ekseni etiketi
plt.ylabel("Y Values (X^2)")  # Y ekseni etiketi
plt.grid(True)  # Izgara ekleme
plt.show()  # Grafiği göster
