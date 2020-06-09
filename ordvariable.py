#  Chapter 2
import math
import matplotlib.pyplot
import numpy

# Time and DQO
So = int(500)
t = [2.6, 5.2, 7.85, 10.51, 13.19, 15.91, 18.7, 21.61, 24.8, 31.16]
DQO = [int(450), int(400), int(350), int(300.0), int(250.0), int(200.0), int(150.0), int(100.0), int(50.0), int(1.0)]

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
"""

# Second Plot x, y = [t, ln(So/DQO)]
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
A = []
# A is a vector equal to (So - DQO)
for x in DQO:
    A.append(So - x)

X1 = numpy.divide(t, A)
print(X1)

# https://numpy.org/doc/stable/reference/routines.math.html

Y = []
for x in DQO:
    Y.append(math.log(So / x))
Y1 = []




print(Y1)

# matplotlib.pyplot.scatter(X1, Y1)
# matplotlib.pyplot.show()
# """