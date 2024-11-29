import numpy as np
import matplotlib.pyplot as plt
import math

jfile = np.loadtxt('jij.#NAME', comments="#")
dm = np.loadtxt('dij.#NAME', comments="#")

### find rotation matrix that rotates vector vi to vf ---> z perpendicular to the surface
##
##vi = np.array([1,1,1])/np.sqrt(3)
##vf = np.array([0,0,1])
##
##cross = np.cross(vi,vf)
##
##s = np.linalg.norm(cross)
##
##c = np.dot(vi,vf)
##
##matrix = np.array([[0,-cross[2],cross[1]], [cross[2],0,-cross[0]], [-cross[1],cross[0],0]])
##
##matrix_2 = np.matmul(matrix,matrix)
##
##I = np.array([[1,0,0],[0,1,0],[0,0,1]])
##
##
##R1 = I + matrix + matrix_2*(1-c)/s**2 

# reference: https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d

#print(R1)

#print(np.matmul(R1,vi))

### find rotation matrix that rotates vi to vf - align the direction between two NN in x [100]

vi = np.array([0.683012701892219,0.183012701892219,0])/0.707106781186548 
vf = np.array([1,0,0])

#print(vi)

cross = np.cross(vi,vf)

s = np.linalg.norm(cross)

c = np.dot(vi,vf)

matrix = np.array([[0,-cross[2],cross[1]], [cross[2],0,-cross[0]], [-cross[1],cross[0],0]])

matrix_2 = np.matmul(matrix,matrix)

I = np.array([[1,0,0],[0,1,0],[0,0,1]])


R2 = I + matrix + matrix_2*(1-c)/s**2 

#print(R2)

#print(np.matmul(R2,vi))


jfile_rot = np.empty([len(jfile),7])

for i in range(0,len(jfile)):
    rotation_1 = np.matmul(R2,jfile[i,2:5])
#    jfile_rot[i,2], jfile_rot[i,3], jfile_rot[i,4]  = math.floor(rotation_1[0]*10000)/10000, math.floor(rotation_1[1]*10000)/10000, math.floor(rotation_1[2]*10000)/10000
    jfile_rot[i,2], jfile_rot[i,3], jfile_rot[i,4]  = rotation_1[0], rotation_1[1], rotation_1[2]
    jfile_rot[i,0]=jfile[i,0]
    jfile_rot[i,1]=jfile[i,1]
    jfile_rot[i,5]=jfile[i,5]
    jfile_rot[i,6]=jfile[i,6]

np.savetxt('jij.#NAME.rot',jfile_rot,fmt='%3i %3i%12.6f%12.6f%12.6f%12.6f%12.6f')


dm_rot = np.empty([len(dm),9])


delta=0.000001



for i in range(0,len(dm)):
    rotation_2 = np.matmul(R2,dm[i,2:5])
    dm_rot[i,2], dm_rot[i,3], dm_rot[i,4]  = rotation_2[0], rotation_2[1], rotation_2[2]

    if np.linalg.norm(dm[i,5:8]) < delta:
        dm_rot[i,5], dm_rot[i,6], dm_rot[i,7]  = dm[i,5], dm[i,6], dm[i,7]
        dm_rot[i,0]=dm[i,0]
        dm_rot[i,1]=dm[i,1]
        dm_rot[i,7]=dm[i,7]
        dm_rot[i,8]=dm[i,8]
        continue
    
    rotation_3 = np.matmul(R2,dm[i,5:8]/np.linalg.norm(dm[i,5:8]))
    dm_rot[i,5], dm_rot[i,6], dm_rot[i,7]  = (rotation_3[0])*np.linalg.norm(dm[i,5:8]), (rotation_3[1])*np.linalg.norm(dm[i,5:8]), (rotation_3[2])*np.linalg.norm(dm[i,5:8])
    
    dm_rot[i,0]=dm[i,0]
    dm_rot[i,1]=dm[i,1]
    dm_rot[i,7]=dm[i,7]
    dm_rot[i,8]=dm[i,8]

f = open('check.#NAME.out', 'w')

print('dm.old         dm.rot', file=f)
for i in range(0,len(dm)):
    print ('%9.6f' %np.linalg.norm(dm[i,5:8]), '%9.6f' %np.linalg.norm(dm_rot[i,5:8]), file=f)
    
f.close()

np.savetxt('dij.#NAME.rot',dm_rot,fmt='%3i %3i%12.6f%12.6f%12.6f%12.6f%12.6f%12.6f%12.6f')
