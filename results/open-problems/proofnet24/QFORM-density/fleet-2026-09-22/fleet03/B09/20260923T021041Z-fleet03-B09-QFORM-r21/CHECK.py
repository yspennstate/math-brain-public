import math
import numpy as np


def Cbase(r):
    beta=(2*r-3)/4
    Dconst=(math.pi**(r/2+1/4))*2**(3/4)*(6/(2*r-3))**(3/4)
    return ((beta+1)/(math.pi*beta))*((beta/2)*Dconst)**(1/(beta+1))

for r in range(2,7):
    print(r, Cbase(r), math.sqrt(math.e)*Cbase(r))

# target-valid aligned two-sided model, r=3, delta=1/32.
delta=1/32
A=np.zeros((7,7))
# order x,u1,u2,u3,z1,z2,z3; coefficients are quadratic-matrix entries.
for i,j,w in [(0,2,delta),(0,4,1),(1,4,1),(2,5,1),(3,6,1)]:
    A[i,j]=A[j,i]=w
print('eigs', np.linalg.eigvalsh(A))
print('stress_bound_general_peer', math.sqrt(math.e)*Cbase(3)*delta**(-1/7))
print('tau_pair_delta2', delta**2, 'tau_1_128', 1/128)
