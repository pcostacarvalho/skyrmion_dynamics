import numpy as np
import math

mom= np.loadtxt("moments.fe.layer", comments="#", dtype=float)

mom_clus = open('momfile_clus', 'w')

mx = 0
my = 0
mz = 1

for i in range(len(mom)):
    ind = 1
    print('{:3d}'.format(i+1) + '{:3d}'.format(ind) + '{:12.6f}'.format(mom[i]) + '{:12.6f}'.format(mx) + '{:12.6f}'.format(my) + '{:12.6f}'.format(mz), file = mom_clus)
    
mom_clus.close()



