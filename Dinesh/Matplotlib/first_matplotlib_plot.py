import matplotlib.pyplot as plt

x_values = [1,1.5,2,2.5,3,3.5,4,4.5,5]
y_values = [3,3,4,4,6,6,4,4,3]
plt.plot(x_values, y_values)
plt.xlabel("x axis values")
plt.ylabel("y axis values")
plt.title("my First matplotlib plot")
plt.show()
plt.plot(x_values, y_values,colour="green",marker="o")
plt.show()
plt.grid()
plt.show()