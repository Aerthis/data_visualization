import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 3)

# set chart title and label axes.
plt.title("Squre Numbers", fontsize = 15)
plt.xlabel("Value", fontsize = 8)
plt.ylabel("Square of Value", fontsize = 8)

# Set size of tick labels.
plt.tick_params(axis = 'both', labelsize = 8)


plt.show()

plt.scatter(2, 4)

plt.show()
