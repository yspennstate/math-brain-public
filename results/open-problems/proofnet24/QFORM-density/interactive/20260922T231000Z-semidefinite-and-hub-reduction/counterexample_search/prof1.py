import time, numpy as np
from lib import *
k=3; laws=[U()]+[GaussLaw()]*k
A=np.zeros((4,4)); A[0,1]=A[1,0]=1; A[2,2]=1
t0=time.time()
m,se=fibre_density(A,laws,np.linspace(-0.3,0.3,61),N=20000)
print("E2 N=2e4 S=61:",time.time()-t0, m.max(), flush=True)
t0=time.time()
m,se=fibre_density(A,laws,[0.0],N=20000)
print("E2 N=2e4 S=1:",time.time()-t0, flush=True)
