import matplotlib.pyplot as plt

liste1 = [10,20,50,100]
liste2 = [5,8,9,50]
liste3 = ["A", "B", "C", "D"]

fig, ax = plt.subplots(1,1,figsize = (8,5))
plt.bar(liste3, liste1, color = "blue")
plt.bar(liste3, liste2, color= "orange")
plt.title("Başlık", size = 18)
plt.xlabel("Düşey", size = 15)
plt.ylabel("Yatay", size = 15)
plt.legend(labels = ["Mavi", "Turuncu"])
fig.text(0.7,0.4,

	 """
	 Bu bölümde grafik ile 
	 ilgili açıklamalar, ek 
         bilgiler, tahminler,
	 yorumlar vs. yer alabilir.
	 
	 """, fontsize = 15)
plt.show()
