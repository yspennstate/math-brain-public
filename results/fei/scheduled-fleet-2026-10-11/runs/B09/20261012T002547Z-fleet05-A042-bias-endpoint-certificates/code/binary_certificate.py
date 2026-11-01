from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import defaultdict
import json,time
root=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def check(v):
 global checks
 assert v
 checks+=1
def table(mask,n):
 return {x:F(1 if mask>>sum(v<<i for i,v in enumerate(x))&1 else -1) for x in product((0,1),repeat=n)}
def essential(T,n):
 return all(any(T[x]!=T[tuple(v^(i==j) for j,v in enumerate(x))] for x in T) for i in range(n))
def spectrum(T,p):
 n=len(p); P={}; W={}
 for s in range(1<<n):
  moment=F(0); den=F(1); w=F(1)
  for i in range(n):
   if s>>i&1: den*=p[i]*(1-p[i]); w*=4*p[i]*(1-p[i])
  for x in T:
   a=F(1)
   for i in range(n):
    a*=p[i] if x[i] else 1-p[i]
    if s>>i&1: a*=x[i]-p[i]
   moment+=T[x]*a
  P[s]=moment*moment/den; W[s]=w
 check(sum(P.values())==1)
 return P,W
def factors(n):
 d=2; out={}
 while d*d<=n:
  while n%d==0: out[d]=out.get(d,0)+1; n//=d
  d+=1 if d==2 else 2
 if n>1: out[n]=out.get(n,0)+1
 return out
def term(out,c,x):
 if not c:return
 assert x>0
 for prime,power in factors(x.numerator).items(): out[prime]+=c*power
 for prime,power in factors(x.denominator).items(): out[prime]-=c*power
def expr(P,W):
 E=defaultdict(F)
 for s in P:
  if s and P[s]:term(E,P[s],W[s]/P[s])
 return {p:c for p,c in E.items() if c}
def same(A,B):check({k:v for k,v in A.items() if v}=={k:v for k,v in B.items() if v})
def delta(P):return sum((s.bit_count()-1)*P[s] for s in P if s)
def influence(P):return sum(s.bit_count()*P[s] for s in P)
binary=[table(mask,2) for mask in range(16)]
essential_masks=[i for i,T in enumerate(binary) if essential(T,2)]
check(len(essential_masks)==10)
grid=[F(1,1024),F(1,17),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(16,17),F(1023,1024)]
binary_cases=0; class_counts={'corner':0,'parity':0,'nonessential':0}
for mask,T in enumerate(binary):
 count=sum(v==1 for v in T.values())
 kind='corner' if count in (1,3) else 'parity' if mask in essential_masks else 'nonessential'
 class_counts[kind]+=1
 for p,q in product(grid,repeat=2):
  P,W=spectrum(T,[p,q]); D=delta(P); E=expr(P,W); expect=defaultdict(F)
  if kind=='corner':
   exceptional=next(x for x in T if T[x]==(1 if count==1 else -1))
   u=p if exceptional[0] else 1-p; v=q if exceptional[1] else 1-q
   check(D==4*u*(1-u)*v*(1-v))
   term(expect,2*D,F(2))
   term(expect,2*D*u/(1-u),1/u);term(expect,2*D*v/(1-v),1/v)
  elif kind=='parity':
   vp=4*p*(1-p);vq=4*q*(1-q)
   check(D==vp*vq)
   if vp!=1:term(expect,D*(1-vp)/vp,1/(1-vp))
   if vq!=1:term(expect,D*(1-vq)/vq,1/(1-vq))
  else:check(D==0)
  same(E,expect);binary_cases+=1

# Independent finite composition reconstruction: transform complete four-bit table.
# Children are masks AND=8, OR=14, XOR=6 in the bit-index convention above.
composition_cases=0
for outer_mask in essential_masks:
 G=binary[outer_mask]
 for left_mask,right_mask in product((8,14,6),repeat=2):
  children=[binary[left_mask],binary[right_mask]]
  for p in ([F(1,3),F(2,5),F(1,4),F(3,7)],[F(1,2)]*4):
   inner=[spectrum(children[i],p[2*i:2*i+2]) for i in (0,1)]
   means=[]
   for i in (0,1):
    mean=F(0)
    for x,val in children[i].items():
     mass=F(1)
     for j in (0,1): mass*=p[2*i+j] if x[j] else 1-p[2*i+j]
     if val==1:mean+=mass
    means.append(mean)
   OP,OW=spectrum(G,means);OE=expr(OP,OW)
   composed={x:G[tuple(int(children[i][x[2*i:2*i+2]]==1) for i in (0,1))] for x in product((0,1),repeat=4)}
   P,W=spectrum(composed,p); target=defaultdict(F,OE); targetD=delta(OP); targetI=F(0)
   for i in (0,1):
    V=4*means[i]*(1-means[i]); weight=sum(OP[s] for s in OP if s>>i&1)/V
    for prime,c in expr(*inner[i]).items():target[prime]+=weight*c
    targetD+=weight*delta(inner[i][0]);targetI+=weight*influence(inner[i][0])
   same(expr(P,W),target);check(delta(P)==targetD);check(influence(P)==targetI)
   composition_cases+=1

constant_cases=0
for outer_mask in essential_masks:
 G=binary[outer_mask]
 for position,value in product((0,1),(0,1)):
  other=1-position
  child=table(6,2);p=[F(1,3),F(2,5)]
  composed={x:G[tuple(value if i==position else int(child[x]==1) for i in (0,1))] for x in child}
  P,W=spectrum(composed,p)
  # A restricted binary essential gate is constant or a signed unary literal.
  if G[(value,value)]==G[tuple(value if i==position else 1-value for i in (0,1))]:
   check(P[0]==1 and delta(P)==0 and not expr(P,W))
  else:
   CP,CW=spectrum(child,p);check(P==CP);same(expr(P,W),expr(CP,CW))
  constant_cases+=1

def ln(x,N=32):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(v):
  z=(v-1)/(v+1);lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
  return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
 a,b=series(x);l,u=series(F(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def divide(A,B):
 corners=[a/b for a in A for b in B];return min(corners),max(corners)
def outward(A):
 scale=10**12;return [str(F((A[0]*scale).__floor__(),scale)),str(F((A[1]*scale).__ceil__(),scale))]
ln2=ln(F(2))
Ccorner=(2+4/ln2[1],2+4/ln2[0]);Cxor=(2/ln2[1],2/ln2[0])
paths=[]
for t in (F(1,4),F(1,16),F(1,256)):
 e,d=t,t*t
 def A(x):
  if x==0:return F(0),F(0)
  if x==1:return F(1),F(1)
  l,u=ln(1/x);return x*l/(1-x),x*u/(1-x)
 a,b=A(1-e),A(1-d)
 ratio=divide((2*(a[0]+b[0]),2*(a[1]+b[1])),ln2);ratio=(ratio[0]+2,ratio[1]+2)
 va=4*e*(1-e);vb=4*d*(1-d);a,b=A(1-va),A(1-vb)
 xor=divide((a[0]+b[0],a[1]+b[1]),ln2)
 paths.append({'t':str(t),'corner_pq':[str(1-e),str(1-d)],'corner_ratio_bits':outward(ratio),'xor_pq':[str(e),str(d)],'xor_ratio_bits':outward(xor)})
out={'helper_version':'A042-binary-v1','assertions_passed':checks,'binary_cases':binary_cases,'essential_masks':essential_masks,'classification_counts':class_counts,'composition_cases':composition_cases,'constant_contractions':constant_cases,'C_corner_rational_enclosure':outward(Ccorner),'C_xor_rational_enclosure':outward(Cxor),'unequal_rate_paths':paths,'runtime_seconds':time.monotonic()-start,'continuum_supremum_proof':'REPORT.md; finite fixtures check identities, not continuum coverage'}
(root/'out/CHECK_OUTPUT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
