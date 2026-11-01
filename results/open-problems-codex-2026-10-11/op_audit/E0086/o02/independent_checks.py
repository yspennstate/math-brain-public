from pathlib import Path
from collections import Counter
import itertools, math, json
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
ROOT=Path(__file__).resolve().parent
steps=((1,0),(-1,0),(0,1),(0,-1))
report={}
# Exhaustive walk enumeration independently implemented (seven steps).
n=7; total=4**n
hs=[(1,0),(2,0),(1,1)]
aval=[1,4-8/math.pi,4/math.pi]
maxima={h:Counter() for h in hs}; killed={h:Counter() for h in hs}
for seq in itertools.product(steps,repeat=n):
 path=[(0,0)]
 for dx,dy in seq:
  x,y=path[-1];path.append((x+dx,y+dy))
 visits=Counter(path); visited=set(path)
 for h in hs:
  eligible=[v for (x,y),v in visits.items() if (x+h[0],y+h[1]) not in visited]
  maxima[h][max(eligible,default=0)]+=1
  first=next((j for j,x in enumerate(path) if x==h),len(path))
  killed[h][sum(x==(0,0) for x in path[:first])]+=1
 assert max(v for (x,y),v in visits.items() if (x+8,y) not in visited)==max(visits.values())
tailchecks=[]
for h,a in zip(hs,aval):
 p=1-1/(2*a)
 for k in range(1,n+3):
  q=sum(v for value,v in maxima[h].items() if value>=k)/total
  qk=sum(v for value,v in killed[h].items() if value>=k)/total
  assert q<=(n+1)*p**(k-1)+1e-14
  assert qk<=p**(k-1)+1e-14
 tailchecks.append({'h':h,'maximum_counts':dict(maxima[h]),'killed_counts':dict(killed[h])})
report['exhaustive']={'steps':n,'paths':total,'offsets':tailchecks,'checks':'all k=1..9; far-offset equality for every path'}
# Independently solve finite killed chains and compare the Schur formula.
greens=[]
for R in [6,11,17]:
 sites=[(x,y) for x in range(-R,R+1) for y in range(-R,R+1) if x*x+y*y<=R*R]
 ix={z:i for i,z in enumerate(sites)}; A=lil_matrix((len(sites),len(sites)))
 for z,i in ix.items():
  A[i,i]=1
  for dx,dy in steps:
   w=(z[0]+dx,z[1]+dy)
   if w in ix:A[i,ix[w]]=-.25
 A=A.tocsr(); o=ix[(0,0)]; e=np.zeros(len(sites));e[o]=1; col=spsolve(A,e)
 for h in [(1,0),(2,1),(4,0)]:
  j=ix[h];eh=np.zeros(len(sites));eh[j]=1; ch=spsolve(A,eh)
  schur=col[o]-ch[o]*col[j]/ch[j]
  mask=np.arange(len(sites))!=j
  direct=spsolve(A[mask][:,mask],e[mask])[list(np.arange(len(sites))[mask]).index(o)]
  err=abs(schur-direct);assert err<1e-11;assert abs(ch[o]-col[j])<1e-11
  greens.append({'R':R,'h':h,'states':len(sites),'schur':float(schur),'direct':float(direct),'error':float(err)})
report['green']=greens
# Scan membership at its actual assigned time; contained-disc geometry.
geometry=[]
for alpha in [.26,.375,.49]:
 for N in [512,8192,131072]:
  r=N**alpha; lower=(2*N)**alpha; bound=math.ceil(2*r)
  offsets=[(x,y) for x in range(-bound,bound+1) for y in range(-bound,bound+1) if lower**2<x*x+y*y<=4*r*r]
  fits=len(offsets)<=N
  if fits:
   for i,(x,y) in enumerate(offsets):
    t=N+i;assert t**(2*alpha)<x*x+y*y<=4*t**(2*alpha)
  L=2**alpha;c=(L+2)/2;d=(2-L)/4; q=math.floor(c*r)
  inside=[]
  for x in range(math.floor(q-d*r),math.ceil(q+d*r)+1):
   for y in range(-math.ceil(d*r),math.ceil(d*r)+1):
    if (x-q)**2+y*y<=(d*r)**2:inside.append((x,y))
  aset=set(offsets);assert set(inside)<=aset
  geometry.append({'alpha':alpha,'N':N,'offset_count':len(offsets),'fits':fits,'contained_disc_sites':len(inside),'g_pi':4*alpha*(1-alpha)})
report['geometry']=geometry
# Finite scan implication for several independent seeded walks.
alpha=.375;N=8192;r=N**alpha;lo=(2*N)**alpha;bound=math.ceil(2*r)
offsets=[(x,y) for x in range(-bound,bound+1) for y in range(-bound,bound+1) if lo**2<x*x+y*y<=4*r*r]
assert len(offsets)<=N
witness=[]
for seed in [4,19,53,101,991]:
 rng=np.random.default_rng(seed); path=[(0,0)]
 for j in rng.integers(0,4,size=2*N):
  dx,dy=steps[j];x,y=path[-1];path.append((x+dx,y+dy))
 v=Counter(path[:N+1]);favorite=max(v,key=v.get);full=set(path)
 for i,(dx,dy) in enumerate(offsets):
  hole=(favorite[0]+dx,favorite[1]+dy)
  if hole not in full:break
 else:raise AssertionError('no finite hole for sample')
 t=N+i;prefix=Counter(path[:t+1]);assert hole not in prefix;assert prefix[favorite]>=v[favorite]
 witness.append({'seed':seed,'time':t,'start_max':v[favorite],'witness_local_time':prefix[favorite]})
report['witness']=witness
# Algebraic leading coefficient and margins at the concrete parameter.
alpha=3/8;s=.51
b=(2/math.pi)*(s-(s-alpha)**2/s)
assert abs(b-(2/math.pi)*(2*alpha-alpha*alpha/s))<1e-15
assert 4*alpha*(1-alpha)==15/16
report['constants']={'alpha':alpha,'g':4*alpha*(1-alpha)/math.pi,'global':1/math.pi,'b_s_at_0.51':b}
(ROOT/'independent_checks.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'paths':total,'green_max_error':max(x['error'] for x in greens),'geometry':geometry,'witness':witness,'constants':report['constants']},indent=2))
