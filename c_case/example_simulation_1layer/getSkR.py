import numpy as np

# Read coordinates and calculate area of paralellogram 
coord=np.genfromtxt('coord.PdFeIr11.80x40')
xmax=np.max(coord[:,1])
ymax=np.max(coord[:,2])
Area = xmax * ymax
#print('b=',xmax,'   h=',ymax,',   Total area=',Area)

# Read moments and calculate no. spins up and down.
moms=np.genfromtxt('restart.PdFeIr11.out')
nup=moms[moms[:,6]>=0].shape[0]
ndw=moms[moms[:,6]<0].shape[0]
ntot=nup+ndw
#print('N_up=', nup,',   N_dw=', ndw)

# Calculate skyrmion radius in two ways:
# Either from the number of spins up/dw or the area of the spins up/dw.
skA = Area * ndw / np.float64(ntot)
skR = np.sqrt(skA/np.pi)
skN = np.sqrt(ndw/np.pi)
#print('Skyrmion area=',skA,',   Skyrmion radius=',skR)

print('Skyrmion radius (areas)=',np.rint(skR*100)/100.0,2*np.rint(skR*100)/100.0)
print('Skyrmion radius (atoms)=',np.rint(skN*100)/100.0,2*np.rint(skN*100)/100.0)
print('Skyrmion radius (average)=',np.rint(0.5*(skR+skN)*100)/100.0,np.rint(1.0*(skR+skN)*100)/100.0)

