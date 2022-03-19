import numpy as np
from numpy.linalg import *

#从x,y,z变到b1,b2,b3

with open('kpts_xyz.dat', 'r') as f:
    data = f.readlines()
kpts_xyz = []
for i in range(len(data)):
    kpts_xyz.append([float(j) for j in data[i].split()])
kpts_xyz = np.array(kpts_xyz)

# A is the high-symmetry points: X, Y, Z's coordinates in BZ with respect to the basis (b1, b2, b3)
A = np.array(
    [[-0.2808, 0.2808, 0.2808],
     [0.4336, -0.4336, 0.4336],
     [0.5, 0.5, -0.5]]
)
B = A.T
out = B.dot(kpts_xyz.T)

np.savetxt('kpts.dat', out.T, fmt='%10.6f')

