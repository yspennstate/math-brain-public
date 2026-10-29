import numpy as np, sys
from gen import *
rng = np.random.default_rng(0)
def P_(m): return np.eye(m)-1.0/m
# F1 = tr W
F1=lambda V: np.trace(P_(V.shape[0])@V)
G1=lambda V: P_(V.shape[0])
H1=lambda V,E: 0.0
# F2 = det V
F2=lambda V: np.linalg.det(V)
G2=lambda V: np.linalg.det(V)*np.linalg.inv(V)
def H2(V,E):
    Vi=np.linalg.inv(V); d=np.linalg.det(V)
    return d*(np.trace(Vi@E)**2 - np.trace(Vi@E@Vi@E))
def sample(m):
    kind=rng.integers(5)
    A=rng.standard_normal((m,m))
    if kind==0: V=A@A.T+0.05*np.eye(m)
    elif kind==1: V=np.eye(m)+rng.uniform(0,0.9)*np.ones((m,m))  # ray
    elif kind==2: u=rng.standard_normal(m); V=np.eye(m)*rng.uniform(1e-3,1)+np.outer(u,u)*rng.uniform(1,50)
    elif kind==3: V=np.diag(rng.uniform(0.01,10,m))
    else: V=rng.uniform(0.01,1)*np.eye(m)+rng.uniform(1,100)*np.ones((m,m))+0.3*(A@A.T)*rng.uniform(0,1)
    return V
for g2 in (0.3,0.6,0.9,1.0):
  for m in (2,3,4,6):
    for name,F,G,H in (("trW",F1,G1,H1),("det",F2,G2,H2)):
        worst=1e9; wV=None
        for _ in range(3000):
            V=sample(m); R2=np.sum(V*V)
            dl,qv=gen_log(F,G,H,V,g2)
            r=dl/R2
            if r<worst: worst=r; wV=V
        print("g2 %.1f m %d %-4s min drift(log F)/|V|^2 = %+.4f"%(g2,m,name,worst), flush=True)
