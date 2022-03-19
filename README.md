# Coordtrans
Coordinate transformation from the lattice vector basis of reciprocal space to the orthogonal basis of reciprocal space (x, y, z), and vice versa.

b2x.py is change b1, b2, b3 to x, y, z.

x2b.py is change x, y, z to b1, b2, b3.

![1](http://latex.codecogs.com/svg.latex?\vec{X}=\left(\vec{e}_1,\vec{e}_2,...,\vec{e}_n\right)\left(\begin{matrix}x_1\\\\x_2\\\\.\\\\.\\\\x_n\end{matrix}\right)=\left(\vec{e}_a,\vec{e}_b,...,\vec{e}_{sn}\right)\left(\begin{matrix}x_1'\\\\x_2'\\\\.\\\\.\\\\x_n'\end{matrix}\right))

For example (oC32):

![1](http://latex.codecogs.com/svg.latex?\left(\begin{matrix}1&0&0\\\\0&1&0\\\\0&0&1\end{matrix}\right)\left(\begin{matrix}x\\\\y\\\\z\end{matrix}\right)=\left(\begin{matrix}-0.2808&0.4336&0.5\\\\0.2808&-0.4336&0.5\\\\0.2808&0.4336&-0.5\end{matrix}\right)\left(\begin{matrix}a_1\\\\a_2\\\\a_3\end{matrix}\right))

(x, y, z) is the orthogonal basis of reciprocal space; (a_1, a_2, a_3) is the lattice vector basis of reciprocal space.
