import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(2*x)
tck = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0)

plt.figure()
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-1, 7, -2, 4])

yder = interpolate.splev(xnew, tck, der=1)

plt.plot(xnew, yder, xnew, np.cos(xnew),'--',x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')



plt.show()