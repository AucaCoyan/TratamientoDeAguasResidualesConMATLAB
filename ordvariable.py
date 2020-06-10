#  Chapter 2
import math
import matplotlib.pyplot
import numpy as np

# Time and DQO
So = int(500)
t = np.array([2.6, 5.2, 7.85, 10.51, 13.19, 15.91, 18.7, 21.61, 24.8, 31.16])
DQO = np.array([450, 400, 350, 300, 250.0, 200.0, 150, 100, 50, 1])

# First Plot x, y = (t, DQO)
"""
X = t
Y = DQO
matplotlib.pyplot.scatter(t, DQO)
matplotlib.pyplot.xlabel("Tiempo (h)")
matplotlib.pyplot.ylabel("DQO (mg/l)")
matplotlib.pyplot.title("Datos Experimentales (orden cero, gráfica según ec.(II-2a))")
matplotlib.pyplot.scatter(X, Y)
matplotlib.pyplot.show()
# """

# Second Plot x, y = [t, ln(So/DQO)]   ->  it's done without numpy
"""
X = t
Y = []
for x in DQO:
    Y.append(math.log(So / x))

matplotlib.pyplot.scatter(X, Y)
matplotlib.pyplot.show()
"""

# Third Plot x, y = [t, ln(So/DQO)]
# """
X1 = np.divide(t, (So - DQO))
Y1 = np.log(So / DQO) / (So - DQO)

# """

A = np.polyfit(X1, Y1, 1)
k1 = A[0] # pendiente de A
k2e = A[1]
k2 = -A[1]
recta = X1 * k1  + k2e
# plot the line
matplotlib.pyplot.plot(X1, recta)

# insert custom point
matplotlib.pyplot.text(0.06, 0.0077, "o experimentales")

# Plot
matplotlib.pyplot.scatter(X1, Y1)
matplotlib.pyplot.show()