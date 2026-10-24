import numpy as np
from explore import data,Hneg
rng=np.random.default_rng(20260915002)
worst=None;low=1e100
for _ in range(10000):
 r=rng.dirichlet([.5,.5,.5])*.25*(1-10**rng.uniform(-9,0))
 q,m,_=data(r);v=np.sqrt(r)
 z=np.r_[r,2*v[1]*v[2],2*v[2]*v[0],2*v[0]*v[1]]
 tr=np.array([1,1,1,0,0,0]);d=tr/4-z;e=tr/4+3*z
 F=2*np.outer(d,d)/q[0]+2*np.outer(e,e)/sum(q[1:])
 val=np.linalg.eigvalsh(Hneg(F,m))[0]
 if val<low:low=val;worst=(r.tolist(),m.tolist(),val)
print('count grouped only worst',worst)
