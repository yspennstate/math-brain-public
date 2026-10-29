import numpy as np
from gen import *
rng=np.random.default_rng(3)
g2=0.5
for m in (2,3,4):
    P=np.eye(m)-1.0/m; one=np.ones(m)
    # build V = W + (r 1^T + 1 r^T)/m + mu 11^T/m^2-ish from W, r, M
    A=rng.standard_normal((m,m)); W=P@(A@A.T)@P
    for rs in (0.0,0.5,1.0):
        u=P@rng.standard_normal(m); r=rs*W@u  # r in range of W
        S=50.0
        V=W+(np.outer(r,one)+np.outer(one,r))/m+S*np.outer(one,one)/m**2
        ev=np.linalg.eigvalsh(V)
        Wd=P@bdrift(V,g2)@P
        print("m",m,"r-scale",rs,"minev %.3f"%ev.min(),"PbP diag",np.round(np.diag(Wd),4), "D=",np.round(np.diag(W)-np.trace(W)/m,3))
