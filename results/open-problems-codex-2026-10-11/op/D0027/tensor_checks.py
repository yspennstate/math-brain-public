from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
start=time.monotonic();I=[[F(1),F(0)],[F(0),F(1)]]
def pair(a,b):return [[a,b],[a,b]]
def matrices(q,a,b,kind):
 p=1-q
 if kind=='C':
  den=a-b
  if not den:return None
  A=[[-b*(1-a)/den,-(1-a)*(1-b)/den],[a*b/den,a*(1-b)/den]]
  # B from direct rational two-by-two conjugation, rather than theorem formula.
  T=[[a,1-a],[b,1-b]]
 else:
  if not a:return None
  T=[[a,-a],[b,1-b]]
  A=pair(b,1-b)
 H=[[-p,p],[q,-q]];det=T[0][0]*T[1][1]-T[0][1]*T[1][0]
 inv=[[T[1][1]/det,-T[0][1]/det],[-T[1][0]/det,T[0][0]/det]]
 def mm(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
 N=[[F(0),F(0)],[F(0),F(1)]]
 assert mm(mm(inv,N),T)==A
 B=mm(mm(inv,H),T)
 states=list(product([0,1],repeat=3))
 K=[]
 for i,s,k in states:
  K.append([(B[s][t] if i==j and k==l else F(0))-A[i][j]*B[s][t]*A[k][l] for j,t,l in states])
 assert all(sum(row)==0 for row in K)
 return A,B,K
qs=[F(1,5),F(1,2),F(4,5)];grid=sorted(set([F(-2),F(-1),F(-4,5),F(-1,2),F(-1,5),F(0),F(1,5),F(1,2),F(4,5),F(1),F(3,2),F(2)]))
cases=0;positive=[]
for q in qs:
 for kind,a,b in product(['C','V'],grid,grid):
  z=matrices(q,a,b,kind)
  if z is None:continue
  K=z[2];ok=all(K[i][j]>=0 for i in range(8) for j in range(8) if i!=j)
  expected=(kind=='C' and (a,b) in [(F(1),F(0)),(F(0),F(1))]) or (kind=='V' and (a,b) in [(1-q,1-q),(-(1-q),q)])
  assert ok==expected,(q,kind,a,b)
  cases+=1
  if ok:positive.append([str(q),kind,str(a),str(b)])
# Check full five-cycle sums; negative local rates are allowed to cancel here.
def cycle(K,n=5):
 states=list(product([0,1],repeat=n));idx={x:i for i,x in enumerate(states)};ss=list(product([0,1],repeat=3));si={x:i for i,x in enumerate(ss)}
 G=[[F(0) for _ in states] for _ in states]
 for row,x in enumerate(states):
  for c in range(n):
   sites=[(c-1)%n,c,(c+1)%n];old=tuple(x[z] for z in sites)
   for tri in ss:
    y=list(x)
    for z,val in zip(sites,tri):y[z]=val
    G[row][idx[tuple(y)]]+=K[si[old]][si[tri]]
 return states,G
parity_cases=0;negative_witnesses=[]
for q in qs:
 for r in [F(-3),F(-2),F(-1),F(-1,2),F(1,2),F(1),F(2),F(3)]:
  # T*1=healthy indicator; T*(1,-1)=constant r.
  a=r/2;b=(1+r)/2;A,B,K=matrices(q,a,b,'V');states,G=cycle(K)
  assert all(sum(row)==0 for row in G)
  chi=[F((-1)**sum(x)) for x in states]
  assert all(sum(g*v for g,v in zip(row,chi))==0 for row in G)
  bad=[(i,j,G[i][j]) for i in range(32) for j in range(32) if i!=j and G[i][j]<0]
  assert bad
  negative_witnesses.append({'q':str(q),'r':str(r),'row':list(states[bad[0][0]]),'col':list(states[bad[0][1]]),'rate':str(bad[0][2])})
  parity_cases+=1
for n in range(5,10):
 triples=[frozenset([(c-1)%n,c,(c+1)%n]) for c in range(n)]
 assert len(set(triples))==n
result={'status':'PASS','local_grid_cases':cases,'positive_cases':positive,'global_parity_cases':parity_cases,'global_negative_witnesses':negative_witnesses,'unique_triples_cycles':list(range(5,10)),'arithmetic':'exact fractions','elapsed_seconds':time.monotonic()-start}
Path('tensor_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print({k:v for k,v in result.items() if k!='global_negative_witnesses'},flush=True)
