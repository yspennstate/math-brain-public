import itertools, math, json, random, collections
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
out={}
# Exact rational finite-disc computation, independently constructed.
def solve(A,b):
 A=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
 for k in range(len(A)):
  i=next(i for i in range(k,len(A)) if A[i][k]); A[k],A[i]=A[i],A[k]
  v=A[k][k]; A[k]=[z/v for z in A[k]]
  for i in range(len(A)):
   if i!=k and A[i][k]:
    v=A[i][k]; A[i]=[x-v*y for x,y in zip(A[i],A[k])]
 return [row[-1] for row in A]
steps=[(1,0),(-1,0),(0,1),(0,-1)]
pts=[(x,y) for x in range(-2,3) for y in range(-2,3) if x*x+y*y<=4]; idx={p:i for i,p in enumerate(pts)}
A=[[F(i==j) for j in range(len(pts))] for i in range(len(pts))]
for p,i in idx.items():
 for d in steps:
  z=(p[0]+d[0],p[1]+d[1])
  if z in idx: A[i][idx[z]]-=F(1,4)
o=idx[(0,0)]; G0=solve(A,[int(i==o) for i in range(len(pts))]); exact=[]
for h in [(1,0),(1,1),(2,0)]:
 k=idx[h]; Gh=solve(A,[int(i==k) for i in range(len(pts))]); keep=[i for i in range(len(pts)) if i!=k]
 B=solve([[A[i][j] for j in keep] for i in keep],[int(i==o) for i in keep])[keep.index(o)]
 formula=G0[o]-Gh[o]**2/Gh[k]; assert B==formula
 exact.append({'h':h,'G00':str(G0[o]),'B':str(B),'formula':str(formula)})
out['exact_green_radius_2']=exact
# Independent sparse solves, altered radii and traps from claimant's checks.
sparse=[]
for R in [4,9,17]:
 pts=[(x,y) for x in range(-R,R+1) for y in range(-R,R+1) if x*x+y*y<=R*R]; idx={p:i for i,p in enumerate(pts)}; o=idx[(0,0)]
 A=lil_matrix((len(pts),len(pts)))
 for p,i in idx.items():
  A[i,i]=1
  for d in steps:
   z=(p[0]+d[0],p[1]+d[1])
   if z in idx: A[i,idx[z]]=-.25
 A=A.tocsr(); e=np.zeros(len(pts));e[o]=1; G0=spsolve(A,e)
 for h in [(1,1),(2,1),(3,0)]:
  k=idx[h]; e=np.zeros(len(pts));e[k]=1; Gh=spsolve(A,e)
  keep=np.array([i for i in range(len(pts)) if i!=k]);e=np.zeros(len(keep));e[list(keep).index(o)]=1
  B=spsolve(A[keep][:,keep],e)[list(keep).index(o)]; formula=G0[o]-Gh[o]**2/Gh[k]
  err=abs(B-formula);assert err<1e-11
  sparse.append({'R':R,'h':h,'error':err})
out['sparse_green']=sparse
# Enumerate every eight-step path once; exact counts, theoretical comparisons.
hs=[(1,0),(1,1),(2,0)]; aval=[1,4/math.pi,4-8/math.pi]; counts={h:[0]*10 for h in hs}; killed={h:[0]*10 for h in hs}
for seq in itertools.product(range(4),repeat=8):
 path=[(0,0)];x=y=0
 for i in seq:
  dx,dy=steps[i];x+=dx;y+=dy;path.append((x,y))
 loc=collections.Counter(path); visited=set(path)
 for h in hs:
  M=max([v for (x,y),v in loc.items() if (x+h[0],y+h[1]) not in visited],default=0)
  end=path.index(h) if h in path else len(path); Nh=sum(z==(0,0) for z in path[:end])
  for k in range(1,10): counts[h][k]+=M>=k; killed[h][k]+=Nh>=k
 assert all((x+9,y) not in visited for x,y in visited)
for h,a in zip(hs,aval):
 for k in range(1,10):
  p=(1-1/(2*a))**(k-1)
  assert counts[h][k]/4**8<=9*p+1e-13
  assert killed[h][k]/4**8<=p+1e-13
out['enumeration']={'paths':4**8,'boundary_tail_counts':{str(h):v for h,v in counts.items()},'killed_tail_counts':{str(h):v for h,v in killed.items()},'all_passed':True}
# Exact integer tests of annular schedule, alpha=p/q.
scans=[]
for p,q in [(3,10),(3,8),(9,20)]:
 for N in [512,4096,16384]:
  b=math.ceil(2*N**(p/q)); ann=[(x,y) for x in range(-b,b+1) for y in range(-b,b+1) if (x*x+y*y)**q>(2*N)**(2*p) and (x*x+y*y)**q<=4**q*N**(2*p)]
  fits=len(ann)<=N
  if fits:
   for i,(x,y) in enumerate(ann):
    n=N+i; norm=x*x+y*y
    assert norm**q>n**(2*p) and norm**q<=4**q*n**(2*p)
  scans.append({'alpha':f'{p}/{q}','N':N,'offsets':len(ann),'fits':fits})
  if (p,q,N)==(3,8,4096): schedule=ann
out['integer_scan_tests']=scans
# Direct prefix calculation at the deterministic scan time for a final-time hole.
witnesses=[]; N=4096
for seed in range(10):
 rng=random.Random(87000+seed);path=[(0,0)];x=y=0
 for j in range(2*N):
  dx,dy=rng.choice(steps);x+=dx;y+=dy;path.append((x,y))
 loc=collections.Counter(path[:N+1]); fav=max(loc,key=loc.get); full=set(path)
 i=next(i for i,h in enumerate(schedule) if (fav[0]+h[0],fav[1]+h[1]) not in full);n=N+i;h=schedule[i]
 prefix=collections.Counter(path[:n+1]); assert (fav[0]+h[0],fav[1]+h[1]) not in prefix; assert prefix[fav]>=loc[fav]
 witnesses.append({'seed':seed,'scan_time':n,'favorite_visits_at_N':loc[fav],'visits_at_scan':prefix[fav]})
out['scan_path_implication']=witnesses
# Algebra of leading coefficient, strict gap, and chosen summable exponents.
coeff=[]
for alpha in [.251,.3,.375,.49]:
 g=4*alpha*(1-alpha)/math.pi; assert g<1/math.pi
 c=(g+1/math.pi)/2;s=.5
 while True:
  s+=.00001;b=2/math.pi*(2*alpha-alpha**2/s)
  if b<c: break
 A=2*s/math.pi;D=2*(s-alpha)/math.pi;assert abs(A-D*D/A-b)<1e-12
 coeff.append({'alpha':alpha,'g':g,'s':s,'b':b,'c':c,'tail_exponent':1-c/b})
out['coefficients']=coeff
Path('independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({'exact_green':exact,'sparse_max_error':max(v['error'] for v in sparse),'enumerated_paths':4**8,'scan_cases':len(scans),'walk_checks':len(witnesses),'all_passed':True},indent=2))
