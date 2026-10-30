import itertools, json, sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from time import perf_counter
start=perf_counter(); checks=0; pilot='--pilot' in sys.argv
def ck(b):
 global checks
 assert b
 checks+=1
 if checks%100000==0: assert perf_counter()-start < (55 if pilot else 170)
def fw(v):
 a=list(v); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k): a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return a
def infraw(a): return sum(s.bit_count()*v*v for s,v in enumerate(a))
def edges(v):
 n=(len(v)-1).bit_length()
 return [sum(v[u]!=v[u^(1<<i)] for u in range(len(v)) if not (u>>i&1)) for i in range(n)]
def unate(v):
 n=(len(v)-1).bit_length()
 return all(len({v[u]-v[u^(1<<i)] for u in range(len(v)) if not(u>>i&1)}-{0})<=1 for i in range(n))
def stars(n):
 for parent in itertools.product(range(-1,n),repeat=n):
  if any(j==i or (j>=0 and parent[j]!=-1) for i,j in enumerate(parent)): continue
  yield parent
def inputmap(u,parent):
 y=u
 for j in range(len(parent)):
  for i,c in enumerate(parent):
   if c==j: y^=((u>>i)&1)<<j
 return y
def label(s,parent):
 t=s
 for i,j in enumerate(parent):
  if j>=0: t^=((s>>j)&1)<<i
 return t
base_count=0; unate_counts={}
for n in (1,2,3):
 uc=0
 for table in range(1<<(1<<n)):
  h=[1 if table>>u&1 else -1 for u in range(1<<n)]
  if not unate(h): continue
  uc+=1; a=fw(h); old=infraw(a)
  for j in range(n):
   for i in range(n):
    if i==j: continue
    dj=sum(v*v for s,v in enumerate(a) if s>>j&1)
    dij=sum(v*v for s,v in enumerate(a) if s>>j&1 and s>>i&1)
    both=0
    for u in range(1<<n):
     if u&(1<<i|1<<j): continue
     da=(h[u]-h[u^(1<<j)])//2
     db=(h[u^(1<<i)]-h[u^(1<<i)^(1<<j)])//2
     both+=da*db
    ck(dj-2*dij==both*(1<<(n+2)))
    ck(dj-2*dij>=0)
  for parent in stars(n):
   g=[h[inputmap(u,parent)] for u in range(1<<n)]; b=fw(g)
   for s in range(1<<n): ck(b[label(s,parent)]==a[s])
   ck(infraw(b)>=old)
   ck(infraw(b)==sum(edges(g))*(1<<(n+1)))
   ck(len({label(s,parent) for s in range(1<<n)})==1<<n)
   base_count+=1
 unate_counts[n]=uc

def quad(n,flag):
 terms=[(i,) for i in range(n)]+list(itertools.combinations(range(n),2))
 return [(-1)**((flag&1)^sum(((flag>>(j+1))&1)*int(all(u>>i&1 for i in term)) for j,term in enumerate(terms))) for u in range(1<<n)]
# All16 actual quadratic phases on two bits, including constants.
phase=[quad(2,i) for i in range(16)]; pa=[fw(x) for x in phase]
h=[1 if u.bit_count()<2 else -1 for u in range(8)]; a=fw(h)
rank=[2 if f&8 else 0 for f in range(16)]
for f in range(16):
 nonzero=[b*b for b in pa[f] if b]
 ck(len(nonzero)==1<<rank[f])
 ck(all(v==16//(1<<rank[f]) for v in nonzero))
 ck(rank[f]*16<=2*infraw(pa[f]))
# Complete MAJ3 rank reference in original subset order: all positive atoms.
reference={1:F(27,49),2:F(27,196),4:F(3,49),7:F(1,4)}
ck(sum(reference.values())==1)
ck(F(27,49)*F(27,196)*F(3,49)*F(1,4)>F(1,4096))
# Hence base Gamma=-1/4 log2(product)<3 without floating logs.
control_count=0
tuples=itertools.product(range(16),repeat=3)
if pilot: tuples=itertools.islice(tuples,16)
for flags in tuples:
 af=[]
 for s in range(8):
  f=0
  for i in range(3):
   if s>>i&1:f^=flags[i]
  af.append(f)
 for parent in stars(3):
  g=[]
  for z in range(4):
   flips=sum((phase[flags[i]][z]==-1)<<i for i in range(3))
   for x in range(8):g.append(h[inputmap(x,parent)^flips])
  b=fw(g)
  for s in range(8):
   for t in range(4): ck(b[label(s,parent)|(t<<3)]==a[s]*pa[af[s]][t])
  ix=sum((s&7).bit_count()*v*v for s,v in enumerate(b))
  iz=sum((s>>3).bit_count()*v*v for s,v in enumerate(b))
  ck(ix==1536) # I_x=3/2, denominator 4^5=1024.
  ck(sum(edges(g)[:3])*64==ix)
  ck(sum(edges(g)[3:])*64==iz)
  ranknum=sum(a[s]*a[s]*rank[af[s]] for s in range(8))
  ck(ranknum*16<=2*iz)
  # Fiber counts and exact packet reference normalize; every positive coefficient covered.
  ck(sum(reference[s]*len([t for t in range(4) if pa[af[s]][t]])/ (1<<rank[af[s]]) for s in reference)==1)
  control_count+=1

@lru_cache(None)
def lninterval(v):
 # Positive rational, reduce to [1,2). Avoid negative-shift or float powers.
 v=F(v); k=0
 while v>=2:v/=2;k+=1
 while v<1:v*=2;k-=1
 t=(v-1)/(v+1)
 lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 hi=lo+2*t**41/(41*(1-t*t))
 if k:
  l2,u2=lninterval(F(2))
  # lninterval(2) would recurse: handled below by the primitive.
 return lo,hi,k
def primitive(v):
 t=(F(v)-1)/(F(v)+1)
 lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return lo,lo+2*t**41/(41*(1-t*t))
l2,u2=primitive(2)
@lru_cache(None)
def loginterval(v):
 y=F(v); k=0
 while y>=2:y/=2;k+=1
 while y<1:y*=2;k-=1
 l,u=primitive(y)
 den=1<<72
 low=F(k)+l/u2; high=F(k)+u/l2
 return F((low*den).numerator//(low*den).denominator,den),F(-((-high*den).numerator//(-high*den).denominator),den)
def add(a,b,scale=F(1)):
 c=dict(a)
 for p,v in b.items():
  c[p]=c.get(p,F(0))+scale*v
  if not c[p]:del c[p]
 return c
@lru_cache(None)
def entropy_expr(squares):
 den=sum(squares); expr={1:F((den-1).bit_length())}
 ck(den&(den-1)==0)
 for v in squares:
  if not v:continue
  m=v;p=2
  while p*p<=m:
   power=0
   while m%p==0:m//=p;power+=1
   if power:expr=add(expr,{1 if p==2 else p:F(power)},-F(v,den))
   p+=1
  if m>1:expr=add(expr,{1 if m==2 else m:F(1)},-F(v,den))
 return expr
def ent(a):return entropy_expr(tuple(sorted(v*v for v in a)))
def lower(expr):
 s=expr.get(1,F(0))
 for p,v in expr.items():
  if p==1:continue
  l,u=loginterval(p);s+=v*(l if v>=0 else u)
 return s
kappa={1:F(12),3:F(-9,2)}
cstar={1:F(16,3),3:F(-3,2)}
ck(lower(add(kappa,{1:F(-24,5)}))>0)
ck(lower(add({1:F(39,8)},kappa,-1))>0)
ck(3**5<2**8 and 3**12>2**19 and 5**10>2**23)
mux_count=0; selector_equalities=0; sharp_equalities=0
domains=list(range(3 if pilot else 4))
for n in domains+[4]:
 if n==4:
  # Eight frozen phase choices, including the two disjoint rank-two factors.
  pairs=list(itertools.combinations(range(n),2))
  def flag(terms):
   out=0
   for term in terms:
    if len(term)==0:out^=1
    elif len(term)==1:out^=1<<(1+term[0])
    else:out^=1<<(1+n+pairs.index(tuple(term)))
   return out
  choices=[flag(x) for x in [[],[()],[(0,)],[(0,1)],[(2,3)],[(0,1),(2,3)],[(0,1),(1,2)],[(0,),(1,2),(2,3)]]]
 else: choices=list(range(1<<(1+n+n*(n-1)//2)))
 phases=[quad(n,f) for f in choices]; spectra=[fw(g) for g in phases]
 for ai,g0 in enumerate(phases):
  a0=spectra[ai]; H0=ent(a0); I0=F(infraw(a0),1<<(2*n))
  for bi,g1 in enumerate(phases):
   a1=spectra[bi]; H1=ent(a1); I1=F(infraw(a1),1<<(2*n))
   g=g0+g1; b=fw(g)
   for s in range(1<<n):
    ck(b[s]==a0[s]+a1[s]);ck(b[s|(1<<n)]==a0[s]-a1[s])
   d=F(sum(x!=y for x,y in zip(g0,g1)),1<<n)
   I=F(infraw(b),1<<(2*n+2))
   ck(I==(I0+I1)/2+d)
   ck(I==F(sum(edges(g)),1<<n))
   L=add(ent(b),add(H0,H1),-F(1,2))
   margin=add({p:d*v for p,v in kappa.items()},L,-1)
   if not margin:selector_equalities+=1
   ck(lower(margin)>=0)
   whole=add({p:I*v for p,v in cstar.items()},ent(b),-1)
   if not whole and I:sharp_equalities+=1
   ck(lower(whole)>=0)
   mux_count+=1

result=dict(status='PASS',pilot=pilot,helper_version=1,unate_counts=unate_counts,base_star_cases=base_count,controlled_cases=control_count,mux_cases=mux_count,selector_exact_equalities=selector_equalities,nonconstant_sharp_whole_equalities=sharp_equalities,exact_assertions=checks,runtime_seconds=perf_counter()-start,arithmetic='Integer truth tables/FWHT and edges; exact entropy expressions; proved 20-term rational logarithm intervals rounded outward to 2^72',universal_bridge='Tagged parity-star rank reference proved; untagged unequal-support collision remains open')
path=Path(__file__).resolve().parents[1]/'out'/('pilot.json' if pilot else 'validation.json')
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

