from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json,sys,time
R=Path(__file__).resolve().parents[1]; CHECKS=0; T0=time.perf_counter()
def ck(x):
 global CHECKS
 assert x,CHECKS
 CHECKS+=1
def fw(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def char(s,t):return 1-2*((s&t).bit_count()%2)
def spec(v):return [F(a*a,len(v)**2) for a in fw(v)]
@lru_cache(maxsize=30000)
def fac(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
def logadd(a,w,x):
 if not w:return
 for sign,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in fac(n):a[p]=a.get(p,F(0))+sign*e*w
def clean(a):return {p:v for p,v in a.items() if v}
def ent(p):
 a={}
 for x in p:
  if x:logadd(a,-x,x)
 return clean(a)
def kl(p,q):
 a={}
 for x,y in zip(p,q):
  if x:ck(y>0);logadd(a,x,x/y)
 return clean(a)
def linear(*terms):
 a={}
 for w,b in terms:
  for p,x in b.items():a[p]=a.get(p,F(0))+w*x
 return clean(a)
def phi(a,b):
 r={}
 if a:logadd(r,a,(a+b)/a)
 if b:logadd(r,b,(a+b)/b)
 return clean(r)
def bound_sig(c,q):
 n=len(c);a=[F(x,n) for x in fw(c)];b=[x/n for x in fw([c[s]*q[s] for s in range(n)])]
 d=sum(q)/n;r={2:2*d}
 for x,y in zip(a,b):
  if x:r=linear((1,r),(1,phi((x-y)**2,y*y)),(1,{2:-2*y*y}))
 return r,a,b
def influence(v):
 n=(len(v)-1).bit_length()
 return F(sum(v[s]!=v[s^(1<<j)] for s in range(len(v)) for j in range(n)),len(v))
def rank(v):
 piv={}
 for x in v:
  while x:
   b=x.bit_length()-1
   if b in piv:x^=piv[b]
   else:piv[b]=x;break
 return len(piv)
def affine_support(v):
 a=[i for i,x in enumerate(fw(v)) if x]
 return rank([x^a[0] for x in a])
def case(phase,t,L,shift,policy):
 n=1<<t;g=[1-2*((phase>>s)&1) for s in range(8)]
 labels=[sum(((s&m).bit_count()%2)<<j for j,m in enumerate(L)) for s in range(n)]
 c=[char(s,shift)*g[labels[s]] for s in range(n)]
 masks=[(0 if policy==0 else 15 if policy==1 else (7*s+3*(s>>1)+5)&15 if policy==2 else (s^(s>>2)^9)&15) for s in range(n)]
 q=[F(x.bit_count(),4) for x in masks];d=sum(q)/n
 h=[c[s]*(1-2*((masks[s]>>v)&1)) for v in range(4) for s in range(n)]
 G=c*4;parent=G+h
 ph=spec(h);pg=spec(G);pf=spec(parent);mix=[(x+y)/2 for x,y in zip(pg,ph)]
 # Erasure is entropy of sector label conditional on union coordinate.
 B=linear((1,ent(pf)),(-1,ent(mix)))
 key,a,b=bound_sig(c,q);ck(B==clean(key));ck(affine_support(c)<=3)
 ck(influence(parent)==(influence(G)+influence(h))/2+d)
 ck(influence(parent)==sum(x*i.bit_count() for i,x in enumerate(pf)))
 qbar=[sum(q[s] for s in range(n) if labels[s]==y)/F(n,8) for y in range(8)]
 compressed,ag,bg=bound_sig(g,qbar);ck(clean(compressed)==B)
 for u in range(8):
  idx=shift
  for j in range(3):
   if u>>j&1:idx^=L[j]
  ck(a[idx]==ag[u]);ck(b[idx]==bg[u])
 # Keep calibrated singleton masses and a normalized full joint private reference.
 rho=sum(ph[n:]);rh=ph[:n]+[(x+rho/F(3*n))/2 for x in ph[n:]]
 Q=[]
 for z in range(2):
  for u in range(4*n):Q.append(pf[z*4*n+u] if u<n else rh[u]/4)
 ck(sum(rh)==1);ck(sum(Q)==1)
 ck(kl(pf,Q)=={p:x/2 for p,x in kl(ph,rh).items()})
 # Physical restrictions project affine Fourier support.
 for j in range(t):
  for val in range(2):ck(affine_support([c[s] for s in range(n) if (s>>j)&1==val])<=3)
 return len(parent)
def structural():
 v=[1 if s.bit_count()>=2 else -1 for s in range(32)]
 ck(affine_support(v)==5)
 cof=[]
 for j in range(5):
  for val in range(2):
   w=[v[s] for s in range(32) if (s>>j)&1==val];ck(affine_support(w)==4);cof.append(4)
 minors=[]
 for mask in range(1,16):
  left=[j for j in range(5) if mask>>j&1];right=[j for j in range(5) if not mask>>j&1]
  rows=[sum(((a>>k)&1)<<j for k,j in enumerate(left)) for a in range(1<<len(left))]
  cols=[sum(((b>>k)&1)<<j for k,j in enumerate(right)) for b in range(1<<len(right))]
  witness=next(( (a,b,c,d) for a,b in combinations(rows,2) for c,d in combinations(cols,2) if v[a|c]*v[b|d]!=v[a|d]*v[b|c]),None)
  ck(witness is not None);minors.append([mask,witness])
 ln=sum(F(2, (2*k+1)*3**(2*k+1)) for k in range(12));tail=F(2,25*3**25)*F(9,8)
 ck(ln>F(2,3));ck(ln+tail<F(7,10));ck(F(5,4)**3<2);ck(F(5,2)>F(9,4))
 return {'threshold_cofactor_affine_ranks':cof,'bipartition_minor_witnesses':minors,'ln2_interval':[str(ln),str(ln+tail)]}
mode=sys.argv[1];count=0;largest=0
if mode=='base':
 for p in range(256):
  for policy in range(4):largest=max(largest,case(p,3,[1,2,4],0,policy));count+=1;assert time.perf_counter()-T0<55
else:
 for p in [0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23]:
  for t,L in [(4,[3,6,12]),(5,[7,14,28]),(6,[15,22,45])]:
   ck(rank(L)==3);ck(rank(L+[1])==4)
   for shift in (0,1):
    for policy in range(4):largest=max(largest,case(p,t,L,shift,policy));count+=1;assert time.perf_counter()-T0<55
out={'mode':mode,'cases':count,'assertions':CHECKS,'largest_parent_truth_table':largest,'seconds':time.perf_counter()-T0,'structural':structural()}
out['assertions']=CHECKS
(R/'out'/('FIXTURES_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
