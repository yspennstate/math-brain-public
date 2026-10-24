import itertools,numpy as np
rng=np.random.default_rng(142)
f=lambda z:(1-z)*np.log(1-z) - z*np.log(z) if 0<z<1 else 0.
for n in [3,4,5,6,8,12]:
 mn=(1e9,None)
 for _ in range(800):
  U=np.linalg.qr(rng.normal(size=(n,3)))[0];V=U[:,:2];w=U[:,2]
  rows=sum(np.dot(r,r)*f(r[2]**2/np.dot(r,r)) for r in U)
  pairs=0
  for i,j in itertools.combinations(range(n),2):
   cross=np.cross(U[i],U[j]);t=np.dot(cross,cross)
   if t>0:pairs+=t*f(cross[2]**2/t)
  val=(rows+pairs)/2
  if val<mn[0]:mn=val,(rows,pairs)
 print(n,mn)
