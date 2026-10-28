from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T015026Z-account03-A057-coherent-restriction-remainder/code/check_nonflat.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('worst_lower=None')[0],ns)
add,entropy,phi,influence,nonneg,walsh,interval=[ns[k] for k in ['add','entropy','phi','influence','nonneg','walsh','interval']]
entropy=lru_cache(maxsize=1024)(entropy);start=time.monotonic();pilot='--pilot' in sys.argv
checks=roots=old_edges=last_edges=proper_edges=positive_old=nontrivial_q=0;lowest_ratio=Q(1)
def ck(b):
 global checks
 assert b;checks+=1
 if time.monotonic()-start>(55 if pilot else 180):raise RuntimeError('frozen runtime')
def restrict(g,i,v):return tuple(g[x] for x in range(len(g)) if x>>i&1==v)
def bval(x,m):return (-1)**sum((x>>i&1)*(x>>(i+1)&1) for i in range(0,m,2))
@lru_cache(maxsize=256)
def physical(m,g,r,sign):
 N=1<<m
 return tuple(sign*g[y]*(-1)**z.bit_count() if x==N-1 else bval(x,m) for z in range(1<<r) for y in range(len(g)) for x in range(N))
@lru_cache(maxsize=256)
def H(m,g,r,sign=1):return entropy(physical(m,g,r,sign))
def packet(m,q):
 N=1<<m;c=Q(1,N);bv=tuple(bval(x,m) if x!=N-1 else 0 for x in range(N));L={}
 for w in walsh(bv):
  a=Q(w*w,N*N);bb=q*c*c
  L=add((1,L),(1,phi(a)),(1,phi(bb)),(-1,phi(a+bb)))
 return L
domains=[(4,k,2,t) for k in ([1] if pilot else range(1,5)) for t in range(16)]
if not pilot:domains +=[(8,2,2,t) for t in [0,6,8,15]]+[(4,2,3,t) for t in [1,23,254]]
for m,k,n,t in domains:
 g=tuple(1 if t>>y&1 else -1 for y in range(1<<n));c=Q(1,1<<m);B=2*m-4*m*c
 vals=physical(m,g,k,1);ck(4*sum(influence(vals,i) for i in range(m))==B);roots+=1
 for i in range(n):
  gc=[restrict(g,i,v) for v in [0,1]]
  old=add((1,H(m,g,k)),(-Q(1,2),H(m,gc[0],k)),(-Q(1,2),H(m,gc[1],k)))
  inner=add((1,entropy(g)),(-Q(1,2),entropy(gc[0])),(-Q(1,2),entropy(gc[1])))
  ck(old==add((c,inner)));ck(nonneg(old));ck(nonneg(add((1,{2:2*c}),(-1,old))))
  old_edges+=1
  if nonneg(add((1,old),(-1,{2:c/1000}))):positive_old+=1
  for h in gc:
   mu=Q(sum(h),len(h));q=mu*mu;nontrivial_q+=q not in [0,1]
   T=add((1,{2:c*(m+Q(9,2))*q}),(c,phi(q)))
   # Retained q log(1/q), with coefficient c, is compared as an exact prime-log expression.
   ck(nonneg(add((1,{2:c*(m+Q(9,2))}),(-1,T))))
   D=add((1,H(m,h,1)),(-Q(1,2),H(m,h,0,1)),(-Q(1,2),H(m,h,0,-1)))
   L=packet(m,q);J=add((1,D),(-1,L))
   ck(nonneg(J));ck(nonneg(add((1,{2:3*c*q}),(-1,J))))
   ck(nonneg(add((1,T),(-1,D))));ck(nonneg(D))
   if not q:ck(D=={})
   ck(nonneg(add((1,{2:B}),(-1,old),(-1,T),(-1,{2:Q(29,32)*B}))))
   last_edges+=1
   for r in range(2,k+1):
    proper=add((1,H(m,h,r)),(-Q(1,2),H(m,h,r-1,1)),(-Q(1,2),H(m,h,r-1,-1)))
    ck(proper=={});proper_edges+=1
for m in range(4,257,4):
 c=Q(1,1<<m);B=2*m-4*m*c
 ck(c*(m+Q(13,2))<=Q(3,32)*B)
 ck(c*(44*m+208)<=6*m)
out={'status':'PASS','pilot':pilot,'roots':roots,'old_core_edges':old_edges,'positive_old_core_edges':positive_old,'last_character_edges':last_edges,'nontrivial_q_edges':nontrivial_q,'proper_character_zero_decrements':proper_edges,'exact_assertions':checks,'seconds':time.monotonic()-start,'scope':'finite exact checks; width/all-m theorem follows from coherent packet proof, not numerical extrapolation'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
