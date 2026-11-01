# check: the drift of r = P V 1 contains +(g2 S/(2 m^2 tau0^2)) W D  (S = 1^T V 1), i.e. the mean token pushes r along +WD
import numpy as np
from gen import bdrift
rng=np.random.default_rng(5); g2=0.5
for m in (3,4):
    P=np.eye(m)-1.0/m; one=np.ones(m)
    A=rng.standard_normal((m,m)); W=P@(A@A.T)@P; D=np.diag(W)-np.trace(W)/m
    for S in (10.0,100.0,1000.0):
        r=np.zeros(m)
        V=W+(np.outer(r,one)+np.outer(one,r))/m+S*np.outer(one,one)/m**2
        V=V+1e-9*np.eye(m)
        br=P@bdrift(V,g2)@one
        pred=g2*(S/m**2+np.trace(W)/m)/(2*m)*(W@D) + g2*(0)  # r=0: (1/2m)(D (1^T V D) + WD (v^T 1)) with v^T1 = trV
        print(m,S,np.round(br,4),np.round(pred,4))
