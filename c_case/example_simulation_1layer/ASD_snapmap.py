#!/usr/bin/env python

# coding: utf-8

# In[1]:


#!/usr/bin/env python
# This import registers the 3D projection, but is otherwise unused.
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glob 
from scipy.interpolate import griddata


# load restart file
momfile=glob.glob("restart.PdFeIr11.out")[0]
mom=np.loadtxt(momfile,usecols = (4,5,6),comments='#')
M = 1    #mensemble
nx = 80
ny = 40
size = nx*ny
c_matrix = np.empty(shape=(M,size))

for i in range(M):
    ini = size*i
    fin = ini+size
    c_matrix[i,:] = mom[ini:fin,2]


coordfile=glob.glob("coord.PdFeIr11.80x40")[0]
coord=np.loadtxt(coordfile,usecols = (1,2,3),comments='#')

# define x,y coordinates
x=coord[:,0]
y=coord[:,1]

#if i < 10: name='00'+str(i)
#if i >= 10 and i < 100: name='0'+str(i)
#if i>=100 and i <1000: name=str(i)

for i in range(M):
    plotname='snapmap-out.png'
    font = {'family' : 'sans',
        'weight' : 'normal',
        'size'   : 18}
    plt.rc('font', **font)
    fig,ax=plt.subplots(1,1,figsize=(8,6))
    c = c_matrix[i,:]
    plt.tripcolor(x*0.384,y*0.384,c,vmin=-1, vmax=1,cmap=cm.coolwarm, shading='gouraud')
    plt.colorbar
    plt.xlabel('$r_x$ (nm)')
    plt.ylabel('$r_y$ (nm)')
    ax.set_aspect('equal', 'box')
    #plt.xlim(0,265)
    #plt.ylim(0,265)
    plt.title('$M_z$ for NX={:4d}, NY={:4d}'.format(nx,ny))
    fig.tight_layout()
    plt.savefig(plotname)
    













