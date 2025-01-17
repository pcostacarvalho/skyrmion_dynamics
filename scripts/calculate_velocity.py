import numpy as np

cmass = np.loadtxt('cmass_skynum.PdFeIr11.out')

pos_ini = cmass[0,1:2]
pos_fin = cmass[len(cmass[:,0])-1,1:2]

dist = np.linalg.norm(pos_fin-pos_ini)*0.384
time = (cmass[len(cmass[:,0])-1,0] - cmass[0,0])*1e-3
vel = dist*1e3/time

#print(dist)
#print(time)
print("velocity: ", vel, "m/s")

