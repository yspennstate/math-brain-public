import numpy as np

def calc(r):
 r=np.array(r,float); T=r.sum(); q0=(1-4*T)/8
 q=q0+T-r
 m=np.log(q[[1,2,0]]*q[[2,0,1]]/(q0*q))
 d=m.prod(); R=m@r; U=(r/m).sum()
 V=(1/m**2).sum()/4-2*sum(r[k]/(m[i]*m[j]) for i,j,k in ((0,1,2),(1,2,0),(2,0,1)))
 b=2*d*U/(d+64*R*R)
 f=d*V-4*d*d*U*U/(d+64*R*R)
 return f,m,b

rng=np.random.default_rng(11011)
best=(-1,None)
for j in range(200000):
 if j%2:
  r=np.exp(rng.uniform(-20,10,3)); r=r/r.sum()
 else:
  r=rng.dirichlet([1,1,1])
 t=1-np.exp(rng.uniform(-30,0)) if j%3 else rng.random()
 r*=t/4
 f,m,b=calc(r)
 if f>best[0]: best=(f,(r.tolist(),m.tolist(),b))
 if f>1.001:
  print('FAIL',f,r,m,b); break
else: print('PASS')
print('BEST',best)
