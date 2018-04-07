import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def find_radius(dx1,dy1,dx2,dy2):
    radiji = []
    for x in range(len(dx1)): #calculate radius of curvature using an equation from: https://en.wikipedia.org/wiki/Curvature#Local_expressions
        ulomek_gor = (dx1[x]**2 + dy1[x]**2)**1.5
        ulomek_dol = abs(dx1[x]*dy2[x] - dy1[x]*dx2[x])
        radiji.append(ulomek_gor/ulomek_dol)
    return radiji

x = np.linspace(0,100,1000)
y = np.square(x) #generates x,y pairs to interpolate

tck, u= interpolate.splprep([x,y], s=0.1) #interpolate, tck returns coefficients defining the curve, u represents f(u) = new_x and g(u) = new y
new_u = np.linspace(u.min(), u.max(), 3000) #get a few more numbers u
x2,y2 = interpolate.splev(new_u, tck, der=0) #generate a bunch more x and y pairs with the function we got with interpolation
dx1, dy1 = interpolate.splev(new_u,tck, der=1) #calculate 1st order derivative
dx2, dy2 = interpolate.splev(new_u,tck, der=2) #calculate 2nd order derivative

r = find_radius(dx1,dy1,dx2,dy2)

print(r)

plt.plot(x, y, 'o', x2, y2) #plot calculated points
plt.show()



