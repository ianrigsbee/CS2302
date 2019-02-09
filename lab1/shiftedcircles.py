#Ian Rigsbee
#Professor: Olec Fuentes
#CS2302 - lab1
#date of last modification 2/8/19
#purpose: to hone our skills in recursion by using shapes and plotting.
#and to also make us think in python rather than java

import matplotlib.pyplot as plt
import numpy as np
import math 



def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


#simply adding the radius to x or y will shift it in a certain direction
#adding radius to x will make the circle center shift to the left
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #shifts to the left or right. doing same thing to y shifts it up or down
        ax.plot(x+radius,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
        

      

plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 30, [100,0], 100,.9)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('shiftedcircles.png')

        
        
#draw circle (axis=suck my momma)



