import numpy as np
#import matplotlib.pyplot as plt
from scipy import interpolate
from math import sqrt

smoothing = 10
z = 10   #offset
'''
x = np.array([148, 146, 143, 140, 139, 138, 142, 146, 159, 167, 178, 183, 189, 194, 198, 204, 207, 212, 223, 234, 244, 252, 256, 265, 268, 268, 261, 257, 254, 249, 245, 238, 234, 231, 225, 212, 190, 167, 151, 127, 115, 102, 93, 87, 80, 76, 75, 76, 77, 78, 79, 82, 88, 93, 97, 104, 111, 119, 126, 131, 140, 145, 150, 154])
y = np.array([107, 111, 116, 123, 134, 150, 160, 170, 185, 191, 197, 200, 205, 206, 208, 210, 210, 210, 208, 203, 197, 192, 188, 171, 154, 143, 123, 109, 102, 94, 86, 75, 71, 67, 64, 59, 54, 51, 57, 76, 89, 102, 111, 119, 133, 145, 160, 169, 173, 176, 178, 180, 184, 186, 188, 190, 192, 194, 196, 198, 200, 201, 202, 204])
'''

x_not_np_array = [148, 146, 143, 140, 139, 138, 142, 146, 159, 167, 178, 183, 189, 194, 198, 204, 207, 212, 223, 234, 244, 252, 256, 265, 268, 268, 261, 257, 254, 249, 245, 238, 234, 231, 225, 212, 190, 167, 151, 127, 115, 102, 93, 87, 80, 76, 75, 76, 77, 78, 79, 82, 88, 93, 97, 104, 111, 119, 126, 131, 140, 145, 150, 154, 200]
y_not_np_array = [107, 111, 116, 123, 134, 150, 160, 170, 185, 191, 197, 200, 205, 206, 208, 210, 210, 210, 208, 203, 197, 192, 188, 171, 154, 143, 123, 109, 102, 94, 86, 75, 71, 67, 64, 59, 54, 51, 57, 76, 89, 102, 111, 119, 133, 145, 160, 169, 173, 176, 178, 180, 184, 186, 188, 190, 192, 194, 196, 198, 200, 201, 202, 204, 250]

x = np.array(x_not_np_array)  #ta dva arraya gresta naprej v interpolacijo
y = np.array(y_not_np_array)

x2 = []  #arraya točk enega offseta
y2 = []

x3 = [] #arraya točk drugega offseta
y3 = []

dist1 = []
dist2 = []

tck, u = interpolate.splprep([x, y], s=smoothing)
unew = np.arange(0, 1.01, 0.001)
out = interpolate.splev(unew, tck)  #out[0] in out[1] vsebujeta arraye z x-i in y-i 


def zracunaj_offset(X1,Y1,X2,Y2):
    dx = (Y2-Y1)/sqrt((X2-X1)**2+(Y2-Y1)**2) * z
    dy = (X2-X1)/sqrt((X2-X1)**2+(Y2-Y1)**2) * z

    x2.append((X2+X1)/2+dx)
    x3.append((X2+X1)/2-dx)

    y2.append((Y2+Y1)/2-dy)
    y3.append((Y2+Y1)/2+dy)

    return


def zracunaj_razdalje1(X1,Y1,X2,Y2):
    dist1.append(sqrt((X2-X1)**2+(Y2-Y1)**2))
def zracunaj_razdalje2(X1,Y1,X2,Y2):
    dist2.append(sqrt((X2-X1)**2+(Y2-Y1)**2))


not_a_np_array_of_interpoleted_Ys = out[1].tolist()

for i in range(len(not_a_np_array_of_interpoleted_Ys)-1):
    #"neki(x_not_np_array[i],y_not_np_array[i],x_not_np_array[i+1],y_not_np_array[i+1])
    zracunaj_offset(out[0][i],out[1][i],out[0][i+1],out[1][i+1])


for j in range(len(x2)-1):
    zracunaj_razdalje1(x2[j],y2[j],x2[j+1],y2[j+1])
    zracunaj_razdalje2(x3[j],y3[j],x3[j+1],y3[j+1])
    
#print(dist1)

#Xs_for_the_x_axis_on_the_graph = np.linspace(0, 10, num=len(x2)-1, endpoint=True)

#plt.figure()
#plt.plot( out[0], out[1], x2, y2, x3, y3 )
#plt.plot(Xs_for_the_x_axis_on_the_graph,dist1, Xs_for_the_x_axis_on_the_graph,dist2)
#plt.plot(Xs_for_the_x_axis_on_the_graph, not_a_np_array_of_interpoleted_Ys)
#plt.axis([0, 10, 0, 2])
#plt.legend(['hitrost enega motorja', 'hirost drugega motorja', 'offset 2'])
#plt.legend(['offse 1', 'input', 'offset 2'])
#plt.axis([0, 300, 0, 300])
#plt.title('YAY, dela :-)')
#plt.show()

'''
plt.figure()
#plt.plot( out[0], out[1], x2, y2, x3, y3 )
plt.plot(out[0], out[1], x2, y2, x3, y3, x, y ,'X')
#plt.plot(Xs_for_the_x_axis_on_the_graph, not_a_np_array_of_interpoleted_Ys)
plt.legend(['offse 1', 'input', 'offset 2'])
plt.axis([0, 300, 0, 300])
plt.title('YAY, dela :-)')
plt.show()
'''
