#Ian Rigsbee
#Professor: Olec Fuentes
#CS2302 - lab1
#date of last modification 2/8/19
#purpose: to hone our skills in recursion by using shapes and plotting.
#and to also make us think in python rather than java

import matplotlib.pyplot as plt
import numpy as np




# tried making it like squares where I can just change up some of the values to better fit 
#the upside down V for the tree but i got stuck. i created the distance but whenever used it just
#makes the graph look out of place. 
def drawbst(n,p,ax):
    if n>0:
         ax.plot(p[:,0],p[:,1],color='k')
         
         #distance = (p[2,0]-p[1,0])/2
         
         # add and subtract values to get the children 
         leftchild = np.array([[p[0,0]-1,p[0,1]-1],[p[1,0]-1,p[1,1]-1],[p[2,0]-1,p[2,1]-1]])
         
         rightchild = np.array([[p[0,0]+1,p[0,1]-1],[p[1,0]+1,p[1,1]-1],[p[2,0]+1,p[2,1]-1]])
         
         drawbst(n-1,leftchild,ax)
         drawbst(n-1,rightchild,ax)
         
         



plt.close("all") 
fig, ax = plt.subplots()
origin = np.array([[-1,-1],[0,0],[1,-1]]) #upside down V for tree origin
drawbst(3,origin,ax)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('BST.png')