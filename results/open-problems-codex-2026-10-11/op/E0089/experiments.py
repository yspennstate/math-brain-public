from pathlib import Path
import json,math,itertools
import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm,binom
from scipy.integrate import quad
n=8
E={(i,j) for i in range(4) for j in range(4,8)}
H=(E-{(0,4),(1,5)})|{(0,1),(4,5)}
def closure(edges,mask):
 adj=[sum(1<<w for a,b in edges for v,w in [(a,b),(b,a)] if v==i) for i in range(n)]
 for _ in range(n):
  m=mask
  for i in range(n):
   if (mask&adj[i]).bit_count()>=2:m|=1<<i
  if m==mask:break
  mask=m
 return mask
results=[]
for name,edges in [('G',E),('H',H)]:
 fs=np.array([int(closure(edges,m)==255) for m in range(256)])
 counts=np.array([m.bit_count() for m in range(256)])
 g=[float(fs[counts==j].mean()) for j in range(9)]
 def weights(p):return p**counts*(1-p)**(8-counts)
 p=brentq(lambda p: weights(p)@fs-.5,1e-5,.99999)
 q=weights(p);eps=.5
 joint=0.
 for x in range(256):
  if not fs[x]:continue
  for y in range(256):
   if not fs[y]:continue
   trans=1.
   for i in range(8):
    a=(x>>i)&1;b=(y>>i)&1
    trans*= ((1-eps)+eps*p if a else eps*p) if b else (eps*(1-p) if a else 1-eps*p)
   joint+=q[x]*trans
 phis={str(K):float((q*fs)[counts>8*p+K*math.sqrt(8)].sum()/q[counts>8*p+K*math.sqrt(8)].sum()) for K in [0,.25,.5]}
 results.append(dict(graph=name,edges=sorted(edges),profile=g,median=p,correlation=4*joint-1,phi=phis,closure_seed_17=closure(edges,17)))
assert all(closure(E,m|51)==closure(H,m|51) for m in range(256))
assert all(sum(i in e for e in E)==4 and sum(i in e for e in H)==4 for i in range(8))
assert all(closure(E,m)<=255 for m in range(256))
gauss=[]
rho=.5
for B in [1,2,4,16,64,256,1024,1000000]:
 u=-math.expm1(-math.log(2)/B);t=norm.isf(u)
 v=quad(lambda x:norm.pdf(x)*norm.sf((t-rho*x)/math.sqrt(1-rho*rho)),t,np.inf,epsabs=1e-14)[0]
 c=math.exp(B*math.log1p(-2*u+v))
 gauss.append(dict(B=B,t=t,joint_block_tail=v,limiting_correlation=4*c-1))
out=dict(finite=results,forced_endpoint_check='all 256 masks passed',gaussian=gauss)
Path('experiments.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
