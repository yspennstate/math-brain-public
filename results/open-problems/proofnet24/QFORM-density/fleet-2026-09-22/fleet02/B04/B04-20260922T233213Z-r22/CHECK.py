import sympy as sp
import numpy as np
import math

s2 = sp.sqrt(2)
H2 = sp.Matrix([[1,1],[1,-1]])/s2
B = 3*H2
C = sp.Rational(1,5)*H2
D = -sp.Rational(3,20)*H2
u = sp.Matrix([1,1])/s2
qx = sp.Rational(1,20)*u
qy = sp.Rational(1,20)*u
q = sp.Matrix.vstack(qx,qy)
a = sp.Integer(2)

A = sp.zeros(5)
A[0,0] = a
for j in range(4):
    A[0,j+1] = a*q[j]
    A[j+1,0] = a*q[j]
R = sp.zeros(4)
R[:2,:2] = C
R[:2,2:] = B
R[2:,:2] = B.T
R[2:,2:] = D
R += a*q*q.T
A[1:,1:] = R

print("B^T B =", sp.simplify(B.T*B))
print("Dprod =", sp.simplify(abs(B.det())))
eps = sp.Rational(1,5)+sp.Rational(3,20) + sp.sqrt(2)/10 + sp.Rational(1,100)
lower = sp.simplify(2-eps)
print("Weyl perturbation upper bound =", eps, "=", float(sp.N(eps,16)))
print("rigorous s_min lower bound =", lower, "=", float(sp.N(lower,16)))
print("lower bound > 1 =", bool(lower > 1))
A_np = np.array(A.evalf(30).tolist(), dtype=float)
eig = np.linalg.eigvalsh(A_np)
print("eigenvalues (numeric check only) =", [float(f"{x:.15f}") for x in eig])
C2 = 8*math.sqrt(math.e)/(3**0.25)
new_bound = C2/(math.sqrt(2)*(9**0.25))
partner_bound = 5.749943550416816/math.sqrt(6)
print("C_2 =", format(C2,'.15f'))
print("new two-sided contaminated bound =", format(new_bound,'.15f'))
print("partner clean-side companion bound =", format(partner_bound,'.15f'))
