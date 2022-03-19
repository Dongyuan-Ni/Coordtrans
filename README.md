# Coordtrans
Coordinate transformation from b to x, and vice versa.

b2x.py is change b_1, b_2, b_3 to x, y, z.

x2b.py is change x, y, z to b_1, b_2, b_3.

Input files: kpts.dat or kpts_xyz.dat

Theory:

![1](http://latex.codecogs.com/svg.latex?\vec{X}=\left(\vec{e}_1,\vec{e}_2,...,\vec{e}_n\right)\left(\begin{matrix}x_1\\\\x_2\\\\.\\\\.\\\\x_n\end{matrix}\right)=\left(\vec{e}_a,\vec{e}_b,...,\vec{e}_{sn}\right)\left(\begin{matrix}x_1'\\\\x_2'\\\\.\\\\.\\\\x_n'\end{matrix}\right))

For example (oC32):

![1](http://latex.codecogs.com/svg.latex?\left(\begin{matrix}1&0&0\\\\0&1&0\\\\0&0&1\end{matrix}\right)\left(\begin{matrix}x\\\\y\\\\z\end{matrix}\right)=\left(\begin{matrix}1&0&0\\\\0&1&0\\\\0&0&1\end{matrix}\right)\left(\begin{matrix}-0.2808&0.4336&0.5\\\\0.2808&-0.4336&0.5\\\\0.2808&0.4336&-0.5\end{matrix}\right)\left(\begin{matrix}a_1\\\\a_2\\\\a_3\end{matrix}\right))

(e_1, e_2, e_3) is (b_1, b_2, b_3).

(e_a, e_b, e_c) is (Brillouin zone basis).
