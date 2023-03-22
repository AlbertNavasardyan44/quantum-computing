import numpy as np
import matplotlib.pyplot as plt

x_data1 =np.arange (-5,5,0.1)
y_data1 =[]
for x in x_data1:

     y=x*x

     y_data1.append(y)

plt.plot(x_data1, y_data1)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
