import matplotlib.pyplot as plt
categories=["math","science","english","history","geography"]
scores=[88,92,80,75,85]

plt.bar(categories,scores, color = "yellow")
plt.xlabel("subjects")
plt.ylabel("scores")
plt.title("exam scores by subjects")

plt.grid()
plt.show()
