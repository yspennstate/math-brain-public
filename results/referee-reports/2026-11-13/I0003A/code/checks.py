#!/usr/bin/env python3
"""Independent finite checks of the identities used in REPORT.md."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10: os.setpriority(os.PRIO_PROCESS,0,10)
import json, math, random, resource, time
from collections import defaultdict
from pathlib import Path
import numpy as np
start=time.monotonic()
rng=random.Random(3003)

def primitive(signs,R):
    s={0:0}
    for k in range(1,R+1): s[k]=s[k-1]+signs[k]
    for k in range(0,-R,-1): s[k-1]=s[k]-signs[k]
    return s

algebra=[]
for trial in range(100):
    R=6
    e={k:rng.choice((-1,1)) for k in range(-R,R+1)}
    f={k:rng.choice((-1,1)) for k in range(-R,R+1)}
    ss=primitive(e,R);tt=primitive(f,R)
    u={(x,y):rng.randrange(-4,5) for x in range(-3,4) for y in range(-3,4)}
    v={(x,y):rng.randrange(-4,5) for x in range(-3,4) for y in range(-3,4)}
    U=lambda x,y:u.get((x,y),0);V=lambda x,y:v.get((x,y),0)
    lhs2=sum(a*(e[y]*(V(x+1,y)-V(x-1,y))+f[x]*(V(x,y+1)-V(x,y-1))) for (x,y),a in u.items())
    rhs2=0; wint=0;eint=0
    for x in range(-5,5):
        for y in range(-5,5):
            us=[U(x,y),U(x+1,y),U(x+1,y+1),U(x,y+1)]
            vs=[V(x,y),V(x+1,y),V(x+1,y+1),V(x,y+1)]
            b=sum(us[i]*vs[(i+1)%4]-us[(i+1)%4]*vs[i] for i in range(4))
            b2=(us[0]-us[2])*(vs[1]-vs[3])-(us[1]-us[3])*(vs[0]-vs[2])
            assert b==b2
            h2=ss[y]-tt[x]
            rhs2+=h2*b
            wint+=h2*h2*sum((us[i]-us[(i+1)%4])**2 for i in range(4))
            eint+=(V(x+1,y)-V(x,y))**2+(V(x,y+1)-V(x,y))**2
    assert lhs2==rhs2,(lhs2,rhs2)
    assert lhs2**2<=8*wint*eint
    algebra.append({'trial':trial,'pairing_twice':lhs2,'face_sum_twice':rhs2})
Path('data/algebra_checks.json').write_text(json.dumps(algebra,indent=2)+'\n')

# Separate matrix verification: six-by-six torus, rate 1 along each outgoing edge.
Lsize=6;n=Lsize**2
es=[1,1,1,-1,-1,-1];fs=[1,1,-1,1,-1,-1]
L=np.zeros((n,n))
for x in range(Lsize):
 for y in range(Lsize):
  i=x*Lsize+y;L[i,i]=-2
  L[i,((x+es[y])%Lsize)*Lsize+y]+=1
  L[i,x*Lsize+(y+fs[x])%Lsize]+=1
S=(L+L.T)/2;A=(L-L.T)/2
matrix=[]
for lam in (1.0,0.1,0.01):
 H=lam*np.eye(n)-S
 inv=np.linalg.inv(H-A)
 K=H-np.einsum("ij,jk->ik",A,np.linalg.solve(H,A),optimize=False)
 err=float(np.max(np.abs((inv+inv.T)/2-np.linalg.inv(K))))
 assert err<1e-9,err
 matrix.append({'lambda':lam,'symmetric_resolvent_max_error':err})
Path('data/resolvent_checks.json').write_text(json.dumps(matrix,indent=2)+'\n')

# Exact unwrapped transfer. Each integer counts equally likely H/V coin words.
cases={
 'alternating':([1,-1],[1,-1]),
 'period4_vs_alternating':([1,1,-1,-1],[1,-1]),
 'period4_vs_period6':([1,1,-1,-1],[1,1,1,-1,-1,-1]),
 'nonzero_mean':([1,1,-1],[1,-1])}
rows=['case,n,return_count,denominator,probability,partial_green']
exact={}
for name,(ee,ff) in cases.items():
 d={(0,0):1};ps=[];green=0.0
 for step in range(129):
  count=d.get((0,0),0);p=count/(1<<step);green+=p;ps.append(p)
  rows.append(f'{name},{step},{count},{1<<step},{p:.17g},{green:.17g}')
  assert sum(d.values())==1<<step
  if step==128:break
  nd=defaultdict(int)
  for (x,y),c in d.items():
   nd[x+ee[y%len(ee)],y]+=c
   nd[x,y+ff[x%len(ff)]]+=c
  d=nd
 exact[name]=ps
 # Brute-force coin words, independent of transfer recursion.
 for steps in range(13):
  returns=0
  for word in range(1<<steps):
   x=y=0
   for j in range(steps):
    if (word>>j)&1:x+=ee[y%len(ee)]
    else:y+=ff[x%len(ff)]
   returns+=(x==0 and y==0)
  assert returns/(1<<steps)==ps[steps]
 # Dense convolution on torus, circumference > 2*32 and multiple of both periods.
 period=math.lcm(len(ee),len(ff));sz=period*math.ceil(67/period)
 grid=np.zeros((sz,sz));grid[0,0]=1.0
 for step in range(33):
  assert abs(grid[0,0]-ps[step])<1e-14
  nxt=np.zeros_like(grid)
  for y in range(sz):nxt[:,y]+=0.5*np.roll(grid[:,y],ee[y%len(ee)])
  for x in range(sz):nxt[x,:]+=0.5*np.roll(grid[x,:],ff[x%len(ff)])
  grid=nxt
Path('data/exact_returns.csv').write_text('\n'.join(rows)+'\n')

# Exhaust all field pairs with periods <= 6 and zero sum in each direction.
# This checks the finite-state invariant measure used in the periodic proof.
from itertools import product
periodic_count=0
for p in (2,4,6):
 for q in (2,4,6):
  for ee in product((-1,1),repeat=p):
   if sum(ee):continue
   for ff in product((-1,1),repeat=q):
    if sum(ff):continue
    indegree=[0]*(p*q)
    for x in range(q):
     for y in range(p):
      indegree[((x+ee[y])%q)*p+y]+=1
      indegree[x*p+(y+ff[x])%p]+=1
    assert set(indegree)=={2}
    periodic_count+=1
summary={'status':'all checks passed','face_identity_trials':100,'matrix_checks':matrix,
'exact_transfer_horizon':128,'brute_force_horizon':12,'dense_convolution_horizon':32,
'periodic_zero_mean_fields_checked':periodic_count,
'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1,
'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('data/check_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
