import numpy as np
from explore import data

for scale in [.15,.3,.45]:
  for cos in [.1,.4,.7,.9,.97]:
    V=np.array([[1,0],[cos,np.sqrt(1-cos*cos)],[cos,-np.sqrt(1-cos*cos)]])
    K0=scale*V@V.T
    if np.linalg.eigvalsh(K0)[-1]>=.99: continue
    for eps in [1e-5,1e-8,1e-11,1e-14]:
      K=K0+eps*np.eye(3)
      dd=data(K)
      if dd is None: continue
      p,c,tau,m,e,cm,d=dd
      if cm<0: print(scale,cos,eps,'compare',cm,'tau',tau,'c',c,'m',m)
