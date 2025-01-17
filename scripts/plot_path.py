import numpy as np
import matplotlib.pyplot as plt

cmass = np.loadtxt('cmass_skynum.PdFeIr11.out')
#cmassp = np.loadtxt('cmass-pristine.out')
coord = np.loadtxt('coord.PdFeIr11.80x40')
imp_pos = np.loadtxt('posfile_clus')

nx = 79*0.707
ny = 39*0.707

max_x = np.max(coord[:,1])
max_y = np.max(coord[:,2])

##def cut_cmass(cmass, max_x, max_y):
##    cut_x = []
##    cut_y = []
##    for i in range(len(cmass[:,0])):
##        if (cmass[i,1] < max_x/0.384 and cmass[i,2] < max_y/0.384):
##            cut_x.append(cmass[i,1])
##            cut_y.append(cmass[i,2])
##    return np.column_stack((cut_x, cut_y))
##
##cut = cut_cmass(cmass, max_x, max_y)
##print(cut)

cut = cmass

while (cut[:,1].max() > nx):
    ind = np.where(cut[:,1] == cut[:,1].max())
    cut = cut[:ind[0][0]-1, :]
#    cut = np.delete(cut, ind[0][0], 0)
#    print(len(cut[:,0]))

while (cut[:,2].max() > ny):
    ind = np.where(cut[:,2] == cut[:,2].max())
    cut = cut[:ind[0][0]-1, :]
#   cut = np.delete(cut, ind[0][0], 0)
    print(len(cut[:,0]))

##indexx = np.where(cmass[:,1] == cmass[:,1].max())
##indexy = np.where(cmass[:,2] == cmass[:,2].max())
##
##if (indexx <= indexy):
##    cut = cmass[:indexx[0][0]+1,:]
##else:
##    cut = cmass[:indexy[0][0]+1,:]
##
##cutp = cmassp
##
##
##while (cutp[:,1].max() > nx):
##    ind = np.where(cutp[:,1] == cutp[:,1].max())
##    cutp = cutp[:ind[0][0]-1, :]
###    cutp = np.delete(cutp, ind[0][0], 0)
###    print(len(cutp[:,0]))
##
##while (cutp[:,2].max() > ny):
##    ind = np.where(cutp[:,2] == cutp[:,2].max())
##    cutp = cutp[:ind[0][0]-1, :]
###   cutp = np.delete(cutp, ind[0][0], 0)
##    print(len(cutp[:,0]))
##    
##    indexx = np.where(cmassp[:,1] == cmassp[:,1].max())
##    indexy = np.where(cmassp[:,2] == cmassp[:,2].max())
##
##    if (indexx <= indexy):
##        cut = cut[:indexx[0][0]+1,:]
##    else:
##        cut = cut[:indexy[0][0]+1,:]

pos_ini = cut[0,1:3]
pos_fin = cut[-1,1:3]

dist = np.linalg.norm(pos_fin-pos_ini)*0.384
time = (cut[-1,0] - cut[0,0])*1e-3

velx = (pos_fin[0]-pos_ini[0])*1e3/time
vely = (pos_fin[1]-pos_ini[1])*1e3/time
vel = dist*1e3/time

print(velx, vely, vel, np.sqrt(velx**2 + vely**2))

plt.rcParams.update({'font.size': 18})
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.plot(cut[:,1]*0.384,cut[:,2]*0.384, '-g', label='impurity')
#ax.plot(cutp[:,1]*0.384,cutp[:,2]*0.384, '--g', label='pristine')
ax.plot(imp_pos[0,2]*0.384, imp_pos[0,3]*0.384, 'ko', markersize=10, markerfacecolor='blue')
ax.axhline(y=0, color='black')
ax.axhline(y=max_y*0.384, color='black')
ax.axvline(x=0, color='black')
ax.axvline(x=nx*0.384, color='black')
ax.set_xlabel('x (nm)')
ax.set_ylabel('y (nm)')
ax.set_xlim([-0.5,max_x*0.384+0.5])
ax.set_ylim([-0.5,max_y*0.384+0.5])
plt.legend()
plt.savefig('jsmall.position.pdf')
plt.show()

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.plot(cut[:,0]*1e-3,cut[:,1]*0.384, '-r', label='x')
ax.plot(cut[:,0]*1e-3,cut[:,2]*0.384, '-b', label='y')
#ax.plot(cutp[:,0]*1e-3,cutp[:,1]*0.384, '--r')
#ax.plot(cutp[:,0]*1e-3,cutp[:,2]*0.384, '--b')
ax.axhline(y=imp_pos[0,2]*0.384, color='red', linewidth=0.5)
ax.axhline(y=imp_pos[0,3]*0.384, color='blue', linewidth=0.5)
ax.set_xlabel('time (ps)')
ax.set_ylabel('position (nm)')
#ax.set_xlim([0,max_x])
#ax.set_ylim([0,max_y])
plt.legend()
plt.savefig('jsmall.position.time.pdf')
plt.show()



