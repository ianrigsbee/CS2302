#Ian Rigsbee
#Professor: Olec Fuentes
#CS2302 - lab1
#date of last modification 2/8/19
#purpose: to hone our skills in recursion by using shapes and plotting.
#and to also make us think in python rather than java

import matplotlib.pyplot as plt
import numpy as np



#for the method i decided to use p and change its values for each corner
#so for p[0][1] and p[1][1] I would make a new array from those two points
#and add or subtract. only problem was getting the newsize of the square 
def draw_squares(ax,n,p,originalsize):
    if n>0:
        
        #new distance 
        newsize = originalsize/3
        
        #four arrays that plot the new squares on the corners of the original square and the recursive squares 
        q = np.array([[p[0,0]-newsize,p[0,1]-newsize],[p[0,0]-newsize,p[0,1]+newsize],[p[0,0]+newsize,p[0,1]+newsize],
                      [p[0,0]+newsize,p[0,1]-newsize],[p[0,0]-newsize,p[0,1]-newsize]])
        
        s = np.array([[p[1,0]-newsize,p[1,1]-newsize],[p[1,0]-newsize,p[1,1]+newsize],[p[1,0]+newsize,p[1,1]+newsize],
                      [p[1,0]+newsize,p[1,1]-newsize],[p[1,0]-newsize,p[1,1]-newsize]])
        
        o = np.array([[p[2,0]-newsize,p[2,1]-newsize],[p[2,0]-newsize,p[2,1]+newsize],[p[2,0]+newsize,p[2,1]+newsize],
                      [p[2,0]+newsize,p[2,1]-newsize],[p[2,0]-newsize,p[2,1]-newsize]])
    
        l = np.array([[p[3,0]-newsize,p[3,1]-newsize],[p[3,0]-newsize,p[3,1]+newsize],[p[3,0]+newsize,p[3,1]+newsize],
                      [p[3,0]+newsize,p[3,1]-newsize],[p[3,0]-newsize,p[3,1]-newsize]])
        
        
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,newsize)
        draw_squares(ax,n-1,s,newsize)
        draw_squares(ax,n-1,o,newsize)
        draw_squares(ax,n-1,l,newsize)
    
        
        
plt.close("all") 
orig_size = 100
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')



