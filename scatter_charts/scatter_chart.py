import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(15,10)*100
y = np.random.rand(15,10)*100

x2 = np.random.rand(15,10)*50
y2= np.random.rand(15,10)*50

fig, ax = plt.subplots(1,1, figsize=(5,4))
plt.scatter(x,y, color = "black", alpha = 0.5)
plt.scatter(x2, y2, color = "red")
plt.xlabel("Yatay Eksen", size = 15)
plt.ylabel("Düşey Eksen", size = 15)
plt.title("Grafiğin Başlığı", size = 18)
fig.text(0.65, 0.55,
	 """

	 Bu bölümde grafik ile ilgili
	 açıklamalar, ek bilgiler ve
	 yorumlar yer alacaktır.
""", fontfamily = "serif", fontsize = 15)
plt.legend(labels = ["Siyah", "Kırmızı"])
plt.show()
