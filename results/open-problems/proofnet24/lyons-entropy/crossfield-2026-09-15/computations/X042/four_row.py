import itertools,numpy as np
f=lambda z:(1-z)*np.log(1-z)-z*np.log(z) if 0<z<1 else 0.
def val(U):
 rows=sum(np.dot(r,r)*f(r[2]**2/np.dot(r,r)) for r in U)
 pairs=0
 for i,j in itertools.combinations(range(4),2):
  c=np.cross(U[i],U[j]);t=np.dot(c,c)
  if t>1e-20:pairs+=t*f(c[2]**2/t)
 return (rows+pairs)/2,rows,pairs
rng=np.random.default_rng(12345);best=(1e9,None)
for _ in range(5000):
 O=np.linalg.qr(rng.normal(size=(4,4)))[0];v=val(O[:,:3])[0]
 if v<best[0]:best=v,O
print(best[0]);print(best[1]);print('u',best[1][:,3]);print('w',best[1][:,2]);
