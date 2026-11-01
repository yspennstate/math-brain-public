from explore import vals
import numpy as np
rng=np.random.default_rng(971)
worst=[];pw=[]
for i in range(10000):
 x,y=sorted(1/(1+np.exp(-rng.uniform(-9,9,2))));l=1/(1+np.exp(-rng.uniform(-9,9)))
 if min(abs(x-l),abs(y-l))<1e-7:continue
 p,J=vals(x,l);r,K=vals(y,l)
 if min(np.linalg.eigvalsh(J))<1e-12 or min(np.linalg.eigvalsh(K))<1e-12:continue
 c=np.clip(0,r[0],p[0]);v=p-c;w=r-c
 a=v@np.linalg.solve(J,v);b=w@np.linalg.solve(K,w)
 worst.append((max(a,b),x,y,l,c))
 pw.append((p@np.linalg.solve(J,p),x,l))
print('raw',sorted(pw,reverse=True)[:5]);print('clipped',sorted(worst,reverse=True)[:10])
