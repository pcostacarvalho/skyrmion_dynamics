#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


coord=np.genfromtxt('coord.PdFeIr11.80x40')
xyz=coord[:,1:4]
natoms=xyz.shape[0]


# In[3]:


center_x=np.max(xyz[:,0])/3
center_y=np.max(xyz[:,1])/2
center = [center_x,center_y,0]
dr=xyz-np.asarray(center)
max_nr=max(np.linalg.norm(dr,axis=1))


# In[4]:


with open('restart.PdFeIr11.80x40','r') as f:
    header=[]
    for lines in range(7):
        header.append(f.readline())
    mag=np.float64(f.readline().split()[3])


# In[5]:


oldres=np.genfromtxt('restart.PdFeIr11.80x40')
oldmom=oldres[:,3]


# In[6]:


##Cosine bubble
#moments=[]
#for atom in xyz:
#    dr=atom-center
#    nr=np.linalg.norm(dr)
#    arg=nr/max_nr
#    mz=np.cos(np.pi*arg)
#    my=dr[0]/nr*np.sin(np.pi*arg)
#    mx=dr[1]/nr*np.sin(np.pi*arg)
#    m=np.asarray([mx,my,mz]).T
#    moments.append(m)


# In[7]:


##Exponent bubble
#moments=[]
#broadening=0.01
#for atom in xyz:
#    dr=atom-center
#    nr=np.linalg.norm(dr)
#    arg=nr/max_nr
#    mz=np.exp(-arg*arg/broadening)
#    my=dr[1]/nr*(1-mz*mz)
#    mx=dr[0]/nr*(1-mz*mz)
#    m=np.asarray([mx,my,mz])
#    moments.append(m)


# In[8]:


#Heaviside bubble
moments=[]
radius=0.08
for atom in xyz:
    dr=atom-center
    nr=np.linalg.norm(dr)
    arg=nr/max_nr
    mz=2.0*np.heaviside(arg-radius,0.0)-1.0 #np.exp(-arg*arg/0.01)
    my=dr[1]/nr*(1-mz*mz)
    mx=dr[0]/nr*(1-mz*mz)
    m=np.asarray([mx,my,mz])
    moments.append(m)


# In[9]:


moments=np.concatenate(moments).reshape(natoms,3)


# In[10]:


with open('start.bubble','w') as f:
    for line in header:
            f.write(line)
    for i,m in enumerate(moments):
        fstring="{iter:8d}{ens:8d}{iatom:8d} {mag:16.8e}{mx:16.8e}{my:16.8e}{mz:16.8e}\n".format(iter=0,ens=1,iatom=i+1,mag=oldmom[i],mx=m[0],my=m[1],mz=m[2])
        f.write(fstring)


# In[ ]:




