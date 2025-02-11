import matplotlib.pyplot as plt

plt.figure(figsize = (4,4))
x = [10, 20, 20, 50]
y = ["A", "B", "C", "D"]
z = [0, 0.2, 0, 0]
plt.pie(x, labels = y, explode = z)
plt.show()
