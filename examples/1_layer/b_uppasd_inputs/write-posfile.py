#!/usr/bin/env python
# coding: utf-8

# In[1]:


#adapted from write-inputs-cluster (Ivan)
import numpy as np
import sys

### Read j data ###
dataj_imp = np.loadtxt('jij.fe.layer.rot')

dataj_imp_vec = dataj_imp[:,2:5]

### Definitions ####
size_x = int(sys.argv[1])  # size of the spin lattice
size_y = int(sys.argv[2])
va = [0.707000,0.000000,0] ## primitive vector 1 of the lattice
vb = [0.353500,0.612300,0] ## primitive vector 2 of the lattice
pos_imp = 1 # position (site number) of the impurity on jfile.imp

NAME=str(size_x)+'x'+str(size_y)


maxn = 0
for i in range(len(va)):
    if int(str(va[i])[::-1].find('.')) >= maxn:
        maxn = int(str(va[i])[::-1].find('.'))
    if int(str(vb[i])[::-1].find('.')) >= maxn:
        maxn = int(str(vb[i])[::-1].find('.'))

index_imp = list(map(int, list(set(dataj_imp.transpose()[0]))))
#print(index_imp)
index_imp.remove(pos_imp)
#print(index_imp, maxn)


atom = 0 ; positions = [] ; center = 0


#value between 0 and 1 to specify the position of the cluster inside the lattice
fx = float(sys.argv[3])
fy = float(sys.argv[4])

mean_x = round(size_x*fx)
mean_y = round(size_y*fy)
for i in range(size_x):
    for j in range(size_y):
        atom += 1
        p = (np.multiply(va,i)+np.multiply(vb,j))
        positions.append(p.tolist())
        if i == mean_x and j == mean_y:
            center = atom
positions = np.round(positions, decimals=maxn).tolist()


interactions_center = list(np.where(dataj_imp[:,0]==pos_imp)[0])
dataj_imp_vec_center = dataj_imp[interactions_center,2:5]
#print(dataj_imp_vec_center)
sites_imp_old = list(map(int, list(dataj_imp[interactions_center,1])))
#print(sites_imp_old)
#print(dataj_imp_vec_center)


interactions_center = list(np.where(dataj_imp[:,0]==pos_imp)[0]) 
dataj_imp_vec_center = dataj_imp[interactions_center,2:5]                    #impurities positions
sites_imp_old = list(map(int, list(dataj_imp[interactions_center,1])))       #number of the impurities
j_center_dist = dataj_imp[interactions_center,5:7]                           #interactions from the impurities

sites_imp = []
positions_imp = [] ; all_sites_imp = []

### central atom with other impurities
all_sites_imp.append(center)

for i in range(len(dataj_imp_vec_center)):
    pos_now = np.add(positions[center-1],dataj_imp_vec_center[i])
#    print(pos_now)
    pos_now = np.round(pos_now, decimals=maxn)
#    print(positions)
    ind = int(positions.index(list(pos_now)))+1
    sites_imp.append(ind)
    all_sites_imp.append(ind)
#    print(all_sites_imp)
    positions_imp.append(pos_now)

all_sites_imp = list(set(all_sites_imp))
#print(len(all_sites_imp))


### write a *.xyz file with 'Fe' format as the impurities and 'Nb' as the pristine
print('writing file .xyz and posfile_clus...', end='')
system_file = open('system_'+NAME+'.xyz', 'w')
posclus = open('posfile_clus_'+NAME, 'w')

print(str(len(positions)) + '\n', file = system_file)
count = 1
for i in range(len(positions)):
    atom_now = (i + 1)
    pos_now = positions[atom_now-1]
    pos_now = np.round(pos_now, decimals=maxn)
    if not atom_now in all_sites_imp:
        print("Fe" + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file = system_file)
    else:
        print("Nb " + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file = system_file)
        print('%3s%3s' %(count, count)  + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file = posclus)
        count += 1

system_file.close()
posclus.close()

print('[ok]')





