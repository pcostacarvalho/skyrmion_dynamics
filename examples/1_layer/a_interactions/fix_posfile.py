import numpy as np
import math

pos_old= np.loadtxt("posfile_example", comments="#", dtype=str)
pos_org = np.loadtxt("cluster-fe-layer", comments="#", dtype=str)

porg = np.asarray(pos_org[:,1:], dtype=float)
pold = np.asarray(pos_old[:,1:], dtype=float)

center = 10

diff = []
for i in range(len(pold)):
    diff.append(pold[i,:] - pold[center-1,:])

diff = np.asarray(diff, dtype=float)
#print(diff)


pos_new = np.empty([len(pos_old),3])

k = []
for i in range(len(diff)):
    teste = diff[i,:]
#    print(teste)
    for j in range(len(porg)):
#        print(porg[j,:])
        if math.isclose(teste[0],porg[j,0]) == True and math.isclose(teste[1],porg[j,1]) == True and math.isclose(teste[2],porg[j,2]) == True:
            k.append(j)
            pos_new[j,:] = pold[i,:]


pos_clus_xyz = open('posfile_clus.xyz', 'w')

pos_clus = open('posfile_clus', 'w')

print(str(len(pos_new)) + '\n', file = pos_clus_xyz)

for i in range(len(pos_new)):
    element=pos_old[k[i],0]
    print('{}'.format(element) + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_new[i]), file = pos_clus_xyz)
    print('{:3d}'.format(i+1) + '{:3d}'.format(i+1) + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_new[i]), file = pos_clus)
    
pos_clus_xyz.close()
pos_clus.close()



            
            
    
