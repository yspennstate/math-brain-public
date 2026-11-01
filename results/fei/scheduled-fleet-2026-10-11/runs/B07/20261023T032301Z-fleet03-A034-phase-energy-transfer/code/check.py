from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time
RUN=Path(__file__).resolve().parents[1]; START=time.monotonic(); checks=0
def need(test,label):
 global checks
 checks+=1
 if not test:raise AssertionError(label)
 if checks%2048==0 and time.monotonic()-START>55:raise TimeoutError('frozen55s cap')
def walsh(v):
 a=list(v);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for i in range(j,j+s):a[i],a[i+s]=a[i]+a[i+s],a[i]-a[i+s]
  s*=2
 return a
def degree(bits):
 a=list(bits)
 for i in range(len(a).bit_length()-1):
  for x in range(len(a)):
   if x>>i&1:a[x]^=a[x^(1<<i)]
 return max([x.bit_count() for x,v in enumerate(a) if v]+[0])
def energy(v,n):return Q(sum((v[x]-v[x^(1<<i)])**2 for x in range(1<<n) for i in range(n)),4*(1<<n))
@lru_cache(None)
def log2_interval(t):
 t=Q(t);e=0
 while t<1:t*=2;e-=1
 while t>=2:t/=2;e+=1
 def ln(z):
  z=(z-1)/(z+1);s=sum(2*z**(2*j+1)/(2*j+1) for j in range(18));r=2*z**37/(37*(1-z*z));return s,s+r
 a,b=ln(t);c,d=ln(Q(2));return e+a/d,e+b/c
@lru_cache(None)
def ent_atom(p):
 if p==0:return Q(0),Q(0)
 a,b=log2_interval(1/p);return p*a,p*b
def entropy(ps):
 e=[ent_atom(p) for p in ps];return sum(t[0] for t in e),sum(t[1] for t in e)
def affine_cells(n):
 N=1<<n;spaces=[]
 for mask in range(1<<(N-1)):
  V={0}|{i for i in range(1,N) if mask>>(i-1)&1}
  if all(x^y in V for x in V for y in V):spaces.append(V)
 found={}
 for V in spaces:
  for a in range(N):
   C=frozenset(a^v for v in V);found[C]=sum(1<<x for x in C)
 return sorted(found.items(),key=lambda z:z[1])
def basis(V):
 out=[];span={0}
 for x in sorted(V):
  if x not in span:out.append(x);span|={y^x for y in tuple(span)}
 return out
def sxor(it):
 a=0
 for x in it:a^=x
 return a
partition_summary=[]
for n in range(4):
 N=1<<n;cells=affine_cells(n);full=(1<<N)-1;parts=[]
 def recurse(left,part):
  if not left:parts.append(tuple(part));return
  if len(part)==4:return
  first=(left&-left).bit_length()-1
  for C,m in cells:
   if m>>first&1 and m&left==m:recurse(left^m,part+[C])
 recurse(full,[]);basis_count=0
 for part in parts:
  dims=[len(C).bit_length()-1 for C in part]
  need(max(n-d for d in dims)<=3,'complete-cover codimension')
  profile=sorted(Q(len(C),N) for C in part)
  allowed=[[Q(1)],[Q(1,2)]*2,[Q(1,4),Q(1,4),Q(1,2)],[Q(1,4)]*4,[Q(1,8),Q(1,8),Q(1,4),Q(1,2)]]
  need(profile in allowed,'all dyadic mass profiles')
  for C in part:
   off=min(C);V={x^off for x in C};b=basis(V);d=len(b)
   mon=[0]+[1<<i for i in range(d)]+[(1<<i)|(1<<j) for i in range(d) for j in range(i)]
   for m in mon:
    bits=[0]*N
    for z in range(1<<d):
     x=off^sxor(b[i] for i in range(d) if z>>i&1);bits[x]=int(z&m==m)
    need(degree(bits)<=n-d+2,'every interpolation generator degree')
    need(degree(bits)<=5,'all quadratic phase combinations by linearity')
    basis_count+=1
 partition_summary.append({'nY':n,'partitions_up_to4':len(parts),'phase_basis_generators':basis_count})

# Every finite physical projection of an affine frequency plane has equal power-of-two fibers.
label_cases=0
for nx in range(5):
 for A in range(1<<nx):
  for B in range(1<<nx):
   for mask in range(1<<nx):
    labels=[((A if t&1 else 0)^(B if t&2 else 0))&mask for t in range(4)]
    counts=[labels.count(x) for x in set(labels)]
    need(len(set(labels)) in (1,2,4) and len(set(counts))==1,'projection fibers1/2/4')
    label_cases+=1

def cell(y):return 0 if not y&1 else (1 if not y&2 else (2 if not y&4 else 3))
fixtures=[]
for nx,J0,A,B in [(2,0,1,2),(3,3,5,6)]:
 ny=5;n=nx+ny
 values=[]
 for v in range(1<<n):
  x=v&((1<<nx)-1);y=v>>nx;t=cell(y)
  label=J0^(A if t&1 else 0)^(B if t&2 else 0)
  phase=(int(t==3)*((y>>3)&1)*((y>>4)&1))^((label&x).bit_count()%2)
  values.append(1-2*phase)
 rank_counts={0:0,1:0,2:0};states=0;min_slack=None
 for pattern in itertools.product((-1,0,1),repeat=n):
  free=[i for i,b in enumerate(pattern) if b==-1];fx=sum(i<nx for i in free);fy=len(free)-fx
  fixed=sum(b<<i for i,b in enumerate(pattern) if b!=-1)
  vals=[values[fixed|sum(((z>>j)&1)<<i for j,i in enumerate(free))] for z in range(1<<len(free))]
  M=len(vals);raw=walsh(vals);probs=[Q(w*w,M*M) for w in raw]
  need(sum(probs)==1,'actual Boolean Parseval')
  iy=Q(sum(vals[z]!=vals[z^(1<<i)] for z in range(M) for i in range(fx,len(free))),M)
  iy_fourier=sum((s>>fx).bit_count()*p for s,p in enumerate(probs))
  need(iy==iy_fourier,'physical versus spectral Y influence')
  projectedA=sum(((A>>i)&1)<<j for j,i in enumerate(free[:fx]));projectedB=sum(((B>>i)&1)<<j for j,i in enumerate(free[:fx]))
  r=0 if not(projectedA or projectedB) else (1 if projectedA==projectedB or not(projectedA and projectedB) else 2)
  rank_counts[r]+=1
  rate={0:Q(11,2),1:Q(24),2:Q(4)}[r]
  hlo,hhi=entropy(probs)
  need(hhi<=rate*iy,'full terminal rank-dependent price')
  wm=[sum(probs[s] for s in range(M) if s&((1<<fx)-1)==j) for j in range(1<<fx)]
  xlo,xhi=entropy(wm)
  need(hhi-xlo<=rate*iy,'FULL conditional spectrum retained')
  need(hhi<=24*iy,'SAME rate24 on every restriction')
  if r==0:
   bits=[(1-vals[z<<fx])//2 for z in range(1<<fy)]
   need(degree(bits)<=5,'rank-zero physical phase degree')
  states+=1
 fixtures.append({'nX':nx,'nY':ny,'J0':J0,'A':A,'B':B,'states':states,'rank_counts':rank_counts})

lines=[(0,1),(2,4),(3,7),(5,6)]
dirs=[a^b for a,b in lines];pieces=[[int(x in C) for x in range(8)] for C in lines]
e0=sum(energy(v,3) for v in pieces);summed=[sum(v[x] for v in pieces) for x in range(8)]
need(len(set(dirs))==4,'negative control has no parallel pair')
need(summed==[1]*8 and energy(summed,3)==0 and e0>0,'four-component energy helper REFUTED')
five=[int(x==31) for x in range(32)];six=[int(x==63) for x in range(64)]
need(degree(five)==5,'degree5 admitted boundary')
need(degree(six)==6,'degree6 excluded factor')
pd=[1-2*int(x==7) for x in range(8)];need(degree([(1-x)//2 for x in pd])==3,'point defect scope guard')
h16=entropy([Q(1,16),Q(15,16)])
need(16*h16[1]<Q(11,2),'rational kappa4<11/2')
out={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-START,'partition_summary':partition_summary,'label_projection_cases':label_cases,'fixtures':fixtures,'counterexample':{'lines':lines,'directions':dirs,'component_energy':str(e0),'sum_energy':'0','scope':'refutes positive comparison to all component energies, not FEI'},'kappa4_interval':[str(16*t) for t in h16],'formal_status':'not Lean-certified','scope':'exact finite domains plus all-dimensional analytic proof in PROOF.md'}
(RUN/'out').mkdir(exist_ok=True);(RUN/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','runtime_seconds','partition_summary','label_projection_cases','fixtures','counterexample']}))
