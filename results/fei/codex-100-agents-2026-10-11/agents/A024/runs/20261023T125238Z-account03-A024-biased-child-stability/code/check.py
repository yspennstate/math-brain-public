from pathlib import Path
import sys,time,json,hashlib
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261023T105459Z-account03-A024-biased-child-stability/code/check_flat.py'
exec(compile(old.read_text(encoding='utf-8').split('fixtures=')[0],str(old),'exec'))
run=R;start=time.monotonic();checks=0
pilot='--pilot' in sys.argv;cap=55 if pilot else 240
branches=Counter();cases=closures=0

def union(n,p,A,B):return truth(n,p,A|B)
def active(v):
 for m in anf(v):
  if m:return (m&-m).bit_length()-1
 return 0
def choose(n,p,A,B):
 v=union(n,p,A,B)
 if len(set(v))==1:return 0,'constant',Q(0)
 if not any(m.bit_count()==2 for m in p):return active(v),'affine',None
 k=codim(n,A);l=codim(n,B)
 k=999 if k is None else k;l=999 if l is None else l
 if k>l:A,B,k,l=B,A,l,k
 if k>=4:
  m=next(m for m in p if m.bit_count()==2)
  return (m&-m).bit_length()-1,'sparse',Q(1,4)
 if l>=4:
  g=truth(n,p,A)
  return (active(v),'difference',None) if len(set(g))==1 else (active(g),'one_low',Q(1,8))
 C=A&B;t=codim(n,C)
 if t is not None and t<=3:return active(v),'intersection_low',Q(1,4)
 g=truth(n,p,A^B)
 return (active(v),'intersection_only',None) if len(set(g))==1 else (active(g),'two_low',Q(1,8))

@lru_cache(maxsize=4096)
def audit(v,i):
 w=fwht(v);N=len(v);a=sum(abs(w[s]) for s in range(N) if not s>>i&1)
 d=Q(sum(w[s]**2 for s in range(N) if s>>i&1),N*N)
 cross=Q(sum(abs(w[s]*w[s^(1<<i)]) for s in range(N) if not s>>i&1),N*N)
 le(cross,d*Q(a,N))
 le(sign(add(erasure(v,i),const(-2*cross))),0)
 for s in range(N):
  if s>>i&1:le(Q(abs(w[s]),N),d)
 return d,Q(sum(map(abs,w)),N)

def one(n,p,A,B,close):
 global cases,closures
 v=union(n,p,A,B);i,branch,lower=choose(n,p,A,B);branches[branch]+=1
 if n:
  d,norm=audit(v,i)
  if branch=='affine' and d:
   ws=fwht(v);le(Q(sum(abs(ws[t]) for t in range(len(v)) if not t>>i&1),len(v)),5)
  le(sign(add(erasure(v,i),const(-10*d))),0)
  if lower is not None:le(lower,d)
  elif branch!='constant':le(norm,{'affine':7,'difference':5,'intersection_only':3}[branch])
  if close:
   fs=set(flats(n-1))
   for j in range(n):
    for bit in (0,1):
     c=child(n,p,A,j,bit);cc=child(n,p,B,j,bit)
     eq(c[:2],cc[:2]);eq(c[2] in fs,True);eq(cc[2] in fs,True)
     eq(union(c[0],c[1],c[2],cc[2]),restrict(v,j,bit));closures+=1
 cases+=1
 if cases%256==0 and time.monotonic()-start>cap:raise TimeoutError('frozen cap')

for n in range(3 if pilot else 4):
 fs=flats(n);mons=[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)]
 for code in range(1<<len(mons)):
  p=tuple(m for j,m in enumerate(mons) if code>>j&1)
  for ia,A in enumerate(fs):
   for B in fs[ia:]:one(n,p,A,B,True)

# Fixed higher-dimensional cases exercise every substantive branch, no search.
def flatmask(n,eqs):
 return sum(1<<x for x in range(1<<n) if all((x&m).bit_count()%2==b for m,b in eqs))
fixtures=[]
for n,p,ea,eb in [
 (8,(3,12,48,192),[(1,0),(2,0),(4,0),(8,0)],[(16,0),(32,0),(64,0),(128,0)]),
 (7,(3,12,48),[(1,0),(2,0),(4,0)],[(8,0),(16,0),(32,0),(64,0)]),
 (4,(3,12),[(1,0),(2,0),(4,0)],[(2,0),(4,0),(8,0)]),
 (6,(0,1,2,3),[(1,0),(2,0)],[(4,0),(8,0),(16,0),(32,0)]),
 (4,(),[(3,1),(5,0)],[(6,1),(9,0)])]:
 A=flatmask(n,ea);B=flatmask(n,eb);fixtures.append((n,p,A,B));one(n,p,A,B,False)

histories=0
@lru_cache(maxsize=1024)
def repair(n,p,A,B):
 v=union(n,p,A,B)
 if len(set(v))==1:return Q(0),{}
 i,_,_=choose(n,p,A,B);v0,v1,d,q,Bi=split(v,i)
 le(sign(add(Bi,const(-10*d))),0)
 zs=[]
 for bit in (0,1):
  c=child(n,p,A,i,bit);cc=child(n,p,B,i,bit)
  eq(union(c[0],c[1],c[2],cc[2]),(v0,v1)[bit])
  zs.append(repair(c[0],c[1],c[2],cc[2]))
 It=d+(zs[0][0]+zs[1][0])/2
 Ht=add(stats(v)[2],sc(add(stats(v0)[2],stats(v1)[2]),-Q(1,2)),sc(add(zs[0][1],zs[1][1]),Q(1,2)))
 eq(It,stats(v)[1]);eq(Ht,stats(v)[2]);return It,Ht
for n,p,A,B in fixtures:
 v=union(n,p,A,B)
 for i in range(n):
  zs=[]
  for bit in (0,1):
   c=child(n,p,A,i,bit);cc=child(n,p,B,i,bit)
   zs.append(repair(c[0],c[1],c[2],cc[2]))
  v0,v1,d,q,Bi=split(v,i)
  eq(stats(v)[1],d+(zs[0][0]+zs[1][0])/2)
  eq(stats(v)[2],add(stats(v)[2],sc(add(stats(v0)[2],stats(v1)[2]),-Q(1,2)),sc(add(zs[0][1],zs[1][1]),Q(1,2))))
  histories+=1
out=dict(status='PASS',descriptions=cases,physical_restrictions=closures,branches=dict(branches),mixed_prefixes=histories,exact_assertions=checks,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inherited_helper_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),formal_certificate=False,independent_review='PENDING')
save('PILOT.json' if pilot else 'VALIDATION.json',out);print(json.dumps(out))
