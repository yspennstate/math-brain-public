import math
import numpy as np

eps = 0.01
c = 0.5
b = np.array([0.1, 0.1, 0.1])
u = np.array([math.sqrt(3)/2, 0.5, 0.0])
v = np.array([0.0, 0.0, 1.0])
S = 2*np.outer(u,u) - 2*np.outer(v,v)
A0 = np.block([
    [S + np.outer(b,b)/2, b[:,None]],
    [b[None,:], np.array([[2.0]])],
])
l1 = eps*np.array([1.0,0.0,0.0,0.0])
l2 = eps*np.array([0.0,1.0,0.0,0.0])
C = (np.outer(l1,l2)+np.outer(l2,l1))/c
A6 = np.zeros((6,6))
A6[:4,:4] = A0 + C
A6[:4,4] = l1
A6[4,:4] = l1
A6[:4,5] = l2
A6[5,:4] = l2
A6[4,5] = A6[5,4] = c
base = np.block([
    [A0, np.zeros((4,2))],
    [np.zeros((2,4)), np.array([[0.0,c],[c,0.0]])],
])
print("eig(A0)=", np.linalg.eigvalsh(A0))
print("eig(A6)=", np.linalg.eigvalsh(A6))
print("perturbation_norm=", np.linalg.norm(A6-base,2))
print("A6=")
np.set_printoptions(precision=12, suppress=True)
print(A6)
B_partner = 9.8345318556
print("density_bound=", 1/abs(c) + 4*B_partner)
