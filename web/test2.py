import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#t = np.arange(0, 1.1, .1)
#x = np.sin(3*np.pi*t)
#y = np.cos(2*np.pi*t)

x = np.array([-3,-2,-1,0,1,2,3,2,0])
y = np.array([-5,-2,-1,0,2,3,2,2,0])

tck, u = interpolate.splprep([x, y], s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)
#print(t)
print(u)
plt.figure()
plt.plot(x, y, 'x', out[0], out[1] )
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-10, 10, -10, 10])
plt.title('Spline of parametrically-defined curve')
plt.show()

#np.sin(2*np.pi*unew), np.cos(2*np.pi*unew)