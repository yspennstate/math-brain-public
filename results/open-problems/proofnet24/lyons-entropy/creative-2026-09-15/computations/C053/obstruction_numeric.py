exec(open('computations/C053/degree2_numeric.py').read().split("print('e1vec'")[0])
from fractions import Fraction
N=masks.sum(axis=1);h=N-p@N;v=p@(h*h)
for i,j in edges:
 idx=(masks[:,i]+2*masks[:,j]).astype(int);w=np.bincount(idx,weights=p,minlength=4);ph=np.bincount(idx,weights=p*h,minlength=4);rho=(ph**2/w).sum()/v
 T=(w[1]+w[2])/(2*np.sqrt(w[0]*w[3]));print((i,j),'T=',T,'D=',2*(1+T),'rho=',rho)
a=np.array([2,3,1,3]);print('diag1 witness',a@(np.linalg.inv(S)-C)@a)
