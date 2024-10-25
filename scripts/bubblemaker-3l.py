#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np


# In[67]:


coord=np.genfromtxt('coord.PdFeIr11.3l.80x40')
xyz=coord[:,1:4]
natoms=xyz.shape[0]


# In[68]:


natoms/3


# In[69]:


xyz_layer = np.zeros((int(natoms/3),3))

k=0
for i in range(natoms):
    if xyz[i,2] == 0.5773:
        xyz_layer[k,:] = xyz[i,:]
        k+=1

center_x=np.max(xyz_layer[:,0])/3
center_y=np.max(xyz_layer[:,1])/2
center = [center_x,center_y,0.5773]
dr=xyz_layer-np.asarray(center)
max_nr=max(np.linalg.norm(dr,axis=1))


# In[70]:


max_nr


# In[71]:


with open('restart.PdFeIr11.3l.80x40','r') as f:
    header=[]
    for lines in range(7):
        header.append(f.readline())
    
#    mag = []
#    for lines in range(3):
#        mag.append(np.float64(f.readline().split()[3]))


# In[72]:


oldres=np.genfromtxt('restart.PdFeIr11.3l.80x40')
oldmom=oldres[:,3]
#print(oldmom)


# In[73]:


#Heaviside bubble
moments=[]
radius=0.08
for atom in xyz_layer:
    dr=atom-center
    nr=np.linalg.norm(dr)
    arg=nr/max_nr
    mz=2.0*np.heaviside(arg-radius,0.0)-1.0 #np.exp(-arg*arg/0.01)
    my=dr[1]/nr*(1-mz*mz)
    mx=dr[0]/nr*(1-mz*mz)
    m=np.asarray([mx,my,mz])
    moments.append(m)


# In[74]:


moments=np.concatenate(moments).reshape(int(natoms/3),3)


# In[75]:


with open('start.bubble','w') as f:
    for line in header:
            f.write(line)
    
    k=0
    for i in range(natoms):
        if xyz[i,2] == 0.5773:
            fstring="{iter:8d}{ens:8d}{iatom:8d} {mag:16.8e}{mx:16.8e}{my:16.8e}{mz:16.8e}\n".format(iter=0,ens=1,iatom=i+1,mag=oldmom[i],mx=moments[k,0],my=moments[k,1],mz=moments[k,2])
            k += 1
        else:
            fstring="{iter:8d}{ens:8d}{iatom:8d} {mag:16.8e}{mx:16.8e}{my:16.8e}{mz:16.8e}\n".format(iter=0,ens=1,iatom=i+1,mag=oldmom[i],mx=0,my=0,mz=1)
            
        f.write(fstring)


# In[ ]:




