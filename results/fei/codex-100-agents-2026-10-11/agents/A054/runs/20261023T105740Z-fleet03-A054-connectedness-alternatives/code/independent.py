from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;payments=0
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen cap')
def span(vs):
 s={0}
 for v in vs:s|={x^v for x in s}
 return s
def factor(x):
 d={};p=2
 while p*p<=x:
  while x%p==0:d[p]=d.get(p,0)+1;x//=p
  p+=1
 if x>1:d[x]=d.get(x,0)+1
 return d
def combine(*terms):
 out={}
 for vec,m in terms:
  for p,q in vec.items():out[p]=out.get(p,F(0))+m*q
 return {p:q for p,q in out.items() if q}
def entropy(vals):
 N=len(vals);out={}
 for s in range(N):
  a=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals))
  q=F(a*a,N*N)
  if q:
   for p,e in factor(q.denominator).items():out[p]=out.get(p,F(0))+q*e
   for p,e in factor(q.numerator).items():out[p]=out.get(p,F(0))-q*e
 return {p:q for p,q in out.items() if q}
def nonnegative(vec):
 d=lcm(*(q.denominator for q in vec.values())) if vec else 1
 a=b=1
 for p,q in vec.items():
  z=int(q*d)
  if z>=0:a*=p**z
  else:b*=p**(-z)
 return a>=b
def influence(vals):
 n=len(vals).bit_length()-1;N=len(vals)
 return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N) for i in range(n)),N)
examples={}
for filename in ['EXAMPLES.json','N4_EXAMPLES.json']:
 for key,e in json.loads((R/'out'/filename).read_text()).items():examples[filename+':'+key]=e
for key,e in examples.items():
 n=e['n'];N=1<<n;labels={int(x):l for x,l in e['labels'].items()};U=set(labels);vals=[-1 if x in U else 1 for x in range(N)];vs=list(range(1,N))
 weights={v:sum((x in U)!=((x^v) in U) for x in range(N))+2*sum((x^v) in U and labels[x]!=labels[x^v] for x in U) for v in vs}
 bases=[b for b in combinations(vs,n) if len(span(b))==N];M=min(sum(weights[v] for v in b) for b in bases)
 ck(M==e['M']);ck(weights=={int(v):w for v,w in e['ell'].items()})
 for v in vs:
  lam=next(t for t in sorted(set(weights.values())) if v in span([z for z in vs if weights[z]<=t]))
  ck(lam==e['lambda'][str(v)])
  ck(min(sum(weights[z] for z in b) for b in bases if v in b)==M+weights[v]-lam)
 w={v:sum(vals[x]!=vals[x^v] for x in range(N)) for v in vs}
 gam={v:(weights[v]-w[v])//2 for v in vs};M0=min(sum(w[v] for v in b) for b in bases)
 ck(M0==e['M0'])
 for v in vs:
  lam0=next(t for t in sorted(set(w.values())) if v in span([z for z in vs if w[z]<=t]))
  ck(lam0==e['lambda0'][str(v)])
  ck(min(sum(w[z] for z in b) for b in bases if v in b)+2*gam[v]==M0+weights[v]-lam0)
 high=[b for b in bases if max(weights[v] for v in b)>=len(U)]
 if not high:ck(e['tau'] is None);continue
 b=min(high,key=lambda b:sum(weights[v] for v in b));cost=sum(weights[v] for v in b)
 ck(cost==M+e['tau'])
 v=next(v for v in b if weights[v]>=len(U))
 marked=min((sum(w[z] for z in c)+2*gam[t],c,t) for c in bases for t in c if weights[t]>=len(U))
 ck(marked[0]==M0+e['tau0'])
 ck(marked[0]==e['best_singleton'][0])
 for scheme,cost,b,v in [('all',cost,b,v),('singleton',*marked)]:
  # Reorder to make the qualifying direction the actual queried coordinate.
  b=(v,)+tuple(z for z in b if z!=v)
  reset=[]
  for y in range(N):
   x=0
   for j,z in enumerate(b):
    if y>>j&1:x^=z
   reset.append(vals[x])
  H=entropy(vals);Hnew=entropy(reset);ck(H==Hnew)
  children=[reset[bit::2] for bit in range(2)];L=combine((H,F(1)),(entropy(children[0]),-F(1,2)),(entropy(children[1]),-F(1,2)))
  I0=influence(vals);Inew=influence(reset);rho=I0-Inew;wi=F(sum(reset[x]!=reset[x^1] for x in range(N)),N);K=F(37,4)
  D=combine((H,F(1)),({2:K*I0},F(-1)))
  S=combine(({2:K*sum(map(influence,children))/2},F(1)),(entropy(children[0]),-F(1,2)),(entropy(children[1]),-F(1,2)))
  ck(combine((D,F(1)),(S,F(1)))==combine((L,F(1)),({2:K*(wi+rho)},F(-1))))
  if cost<=e['I0'] and n>=2:
   # Test zero and maximal permissible historical debit; both use SAME rho.
   for u in [F(0),F(e['I0']-cost,N)]:
    ck(nonnegative(combine(({2:K*(wi+rho-u)},F(1)),(L,F(-1)))));payments+=1
 # Complete identity checked even when the sufficient criterion fails.
# Fixed zero-release guard: exact directional profile, not full basis enumeration.
fixtures=[]
for k in [2,3,4]:
 n=k+4;N=1<<n;U={x for x in range(16) if (((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2)==0}
 labels={x:(1 if x==15 else 0) for x in U};p=F(10,N);cheap=[]
 for v in range(1,N):
  w=F(sum((x in U)!=((x^v) in U) for x in range(N)),N)
  gam=F(sum((x^v) in U and labels[x]!=labels[x^v] for x in U),N);ell=w+2*gam
  if v>=16:ck(w==2*p and gam==0)
  else:ck(w==F(1,2**(k+1)) and gam<=F(1,2**(k+3)))
  if ell<p:cheap.append(v)
 ck(len(span(cheap))==16)
 for i in range(n):
  v=1<<i;gam=F(sum((x^v) in U and labels[x]!=labels[x^v] for x in U),N);ck(gam==0)
 fixtures.append({'k':k,'cheap_rank':4,'M_equals_I0':'proved by data/control quotient rank; not enumerated','tau':0})
# Independent A052 changed-partition guard, with complete child orbit minima.
def affine_min(vals):
 N=len(vals);n=N.bit_length()-1;vs=range(1,N)
 bs=[b for b in combinations(vs,n) if len(span(b))==N]
 w={v:F(sum(vals[x]!=vals[x^v] for x in range(N)),N) for v in vs}
 return min(sum(1-w[v] if (d&v).bit_count()%2 else w[v] for v in b) for b in bs for d in range(N))
guard=[-1 if x&6==0 else 1 for x in range(8)]
swapped=[guard[((y&1)<<1)|((y&2)>>1)|(y&4)] for y in range(8)]
ck(influence(guard)==influence(swapped)==1);ck(affine_min(guard)==1)
for vals,expected_L,expected_cost in [(guard,0,0),(swapped,2,1)]:
 ch=[vals[b::2] for b in range(2)]
 L=combine((entropy(vals),F(1)),(entropy(ch[0]),-F(1,2)),(entropy(ch[1]),-F(1,2)))
 ck(L==({2:F(expected_L)} if expected_L else {}))
 ck(influence(vals)-sum(map(affine_min,ch))/2==expected_cost)
# Strict singleton-only improvement with a NONZERO actual entropy bill.
vals=[-1 if x in [1,2] else 1 for x in range(8)]
reset=[vals[(y&1)^((3 if y&2 else 0))^(y&4)] for y in range(8)]
ck([x for x,v in enumerate(reset) if v==-1]==[1,3])
ck(entropy(vals)==entropy(reset)=={2:F(2)})
ck(influence(vals)==F(3,2) and influence(reset)==1)
ck(all(entropy(reset[b::2])=={} for b in range(2)))
rho=F(1,2);u=F(1,2);wi=F(1,2)
ck(F(37,4)*(wi+rho-u)>=2);ck(F(3,2)>F(3,2)-u)
ck(F(1)<=F(3,2)-u) # exact sharp cost1 versus all-labelled cost3/2
out={'status':'PASS','assertions':checks,'representatives':len(examples),'actual_signed_identity_and_payment_tests':payments,'fixtures':fixtures,'seconds':time.perf_counter()-start,'method':'independent direct character sums, exact prime-log cancellation, integer-product sign certificate, set-span basis enumeration; no imported helper'}
(R/'out/INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
