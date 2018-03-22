from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, num=11, endpoint=True)
#y = np.cos(-x**2/9.0)
#x = [1,2,3]
y1=[0,0,5,10,15,10,4,6,9,9,9]
y = np.array(y1)

#print(x)
#print(y)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=100, endpoint=True)
y2 = f2(xnew)
plt.plot(x, y, 'o', xnew, y2, '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
#print(f2(xnew))
print (f2)
plt.show()
