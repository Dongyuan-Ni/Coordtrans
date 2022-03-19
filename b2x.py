import numpy as np
from numpy.linalg import *

#从b1,b2,b3变到x,y,z

with open('kpts.dat', 'r') as f:
    data = f.readlines()
kpts = []
for i in range(len(data)):
    kpts.append([float(j) for j in data[i].split()])
kpts = np.array(kpts)

# A is the high-symmetry points: X, Y, Z's coordinates in BZ with respect to the basis (b1, b2, b3)
A = np.array(
    [[-0.2808, 0.2808, 0.2808],
     [0.4336, -0.4336, 0.4336],
     [0.5, 0.5, -0.5]]
)
B = A.T
out = inv(B).dot(kpts.T)

np.savetxt('kpts_xyz.dat', out.T, fmt='%10.6f')

