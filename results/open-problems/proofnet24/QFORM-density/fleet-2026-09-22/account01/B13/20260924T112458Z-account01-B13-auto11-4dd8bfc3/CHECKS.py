import math
import numpy as np

rng=np.random.default_rng(123)
max_gram_err=0.0
max_leverage_err=0.0
for _ in range(1000):
    n=10
    v=rng.normal(size=n)
    g=rng.normal(size=n)
    B=np.column_stack([v,g])
    G=B.T@B
    if np.linalg.det(G)<1e-10:
        continue
    W2=np.linalg.det(G)
    D=np.outer(v,g)-np.outer(g,v)
    sumD=sum(D[i,j]**2 for i in range(n) for j in range(i+1,n))
    max_gram_err=max(max_gram_err,abs(W2-sumD))
    Ginv=np.linalg.inv(G)
    leverage=np.einsum('ij,jk,ik->i',B,Ginv,B)
    star=np.array([sum(D[i,j]**2 for j in range(n) if j!=i) for i in range(n)])
    max_leverage_err=max(max_leverage_err,float(np.max(np.abs(leverage-star/W2))))

C_A=3*2**(-2/3)*math.e**(2/3)
print('max_gram_wedge_error=',repr(max_gram_err))
print('max_leverage_star_error=',repr(max_leverage_err))
print('C_A=',repr(C_A))
print('(4*C_A)^3=',repr((4*C_A)**3))
print('432*e^2=',repr(432*math.e**2))
print('24^(3/2)=',repr(24**1.5))
print('128*24^3=',128*24**3)
