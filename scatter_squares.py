import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c = (0, 0, 0.5), edgecolor = 'none', s = 5)
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Greens, edgecolor = 'none', s = 40)

# set chart title and label axes.
plt.title("Squre Numbers", fontsize = 15)
plt.xlabel("Value", fontsize = 8)
plt.ylabel("Square of Value", fontsize = 8)

# Set size of tick labels.
plt.tick_params(axis = 'both', labelsize = 8)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.savefig('scatter_plot.png', bbox_inches = 'tight')
