import matplotlib.pyplot as plt

# Read the points from the file
x_values = []
y_values = []

with open("points.dat", "r") as file:
    for line in file:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)

# Plot the points
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Solution curve of the given differential equation", color="b")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

