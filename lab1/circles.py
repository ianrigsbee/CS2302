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
    z = center[0]+rad*np.sin(t)
    c = center[1]+rad*np.cos(t)
    return z,c


#this method takes x and y instead of center but will be turning those two points
#into a center to use the circle() function. the method makes 5 smaller circles within
#the original circle. one in the middle,to the left,right,up and down. the cirlces will have their
#x and y coordinates either added or subtracted with radius *2/3 simply because having 
#1/3 will move the cirlces closer to the middle point which i dont want
def draw_circles(ax,n,x,y,radius,w):
    if n>0:
        
        #created center for use of circle()
        center = [x,y]
        z,c = circle(center,radius)
        ax.plot(z,c,color='k')
        
        #adding and subtracting to shift the circles within the original circle
        draw_circles(ax,n-1,x,y,radius/3,w)
        draw_circles(ax,n-1,x+radius*2/3,y,radius/3,w)
        draw_circles(ax,n-1,x,y+radius*2/3,radius/3,w)
        draw_circles(ax,n-1,x-radius*2/3,y,radius/3,w)
        draw_circles(ax,n-1,x,y-radius*2/3,radius/3,w)
        


plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, 100,0, 100,.9)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')
