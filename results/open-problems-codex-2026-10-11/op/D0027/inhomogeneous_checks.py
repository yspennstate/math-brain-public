from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
start=time.monotonic();states=list(product([0,1],repeat=5));idx={x:i for i,x in enumerate(states)};triples=list(product([0,1],repeat=3));I=[[F(1),F(0)],[F(0),F(1)]]
patterns=[[F(1),F(-1),F(2),F(-2),F(1,2)],[F(2,3),F(-3,2),F(3),F(1,3),F(-4)],[F(1),F(1),F(1),F(1),F(1)]]
results=[]
for q,kind,rs in product([F(1,5),F(1,2),F(4,5)],['C','V'],patterns):
 p=1-q;As=[];Bs=[];Ts=[]
 for r in rs:
  if kind=='C':
   A=[[(1+r)/(2*r),(1-r)/(2*r)],[-(1+r)/(2*r),(r-1)/(2*r)]]
   u=(1-r*p)/2;v=(1+r*p)/2;B=[[-u,u],[v,-v]]
   T=[[F(1,2),F(1,2)],[(1+r)/2,(1-r)/2]]
  else:
   b=(1+r)/2;A=[[b,1-b],[b,1-b]];c0=(-1+p/r)/2;c1=(-1-p/r)/2;B=[[c0,c0],[c1,c1]]
   T=[[r/2,-r/2],[(1+r)/2,(1-r)/2]]
  As.append(A);Bs.append(B);Ts.append(T)
 G=[[F(0) for _ in states] for _ in states]
 for row,x in enumerate(states):
  for c in range(5):
   left=(c-1)%5;right=(c+1)%5;i,s,k=x[left],x[c],x[right]
   for j,t,l in triples:
    rate=(Bs[c][s][t] if i==j and k==l else F(0))-As[left][i][j]*Bs[c][s][t]*As[right][k][l]
    y=list(x);y[left]=j;y[c]=t;y[right]=l;G[row][idx[tuple(y)]]+=rate
 assert all(sum(row)==0 for row in G)
 chi=[(-1)**sum(x) for x in states]
 assert all(sum(v*z for v,z in zip(row,chi))==0 for row in G)
 bad=[(i,j,G[i][j]) for i in range(32) for j in range(32) if i!=j and G[i][j]<0]
 odd=[(i,j,G[i][j]) for i in range(32) for j in range(32) if (sum(states[i])-sum(states[j]))%2 and G[i][j]!=0]
 assert bad and odd
 checked_similarity=False
 if q==F(1,2) and rs==patterns[0]:
  S=[[F(1) for _ in states] for _ in states]
  for i,x in enumerate(states):
   for j,y in enumerate(states):
    for z in range(5):S[i][j]*=Ts[z][x[z]][y[z]]
  L=[[F(0) for _ in states] for _ in states]
  for i,x in enumerate(states):
   for c in range(5):
    if x[(c-1)%5]==0 or x[(c+1)%5]==0:
     y=list(x);y[c]=1-y[c];rate=p if x[c]==0 else q;L[i][idx[tuple(y)]]+=rate;L[i][i]-=rate
  for i in range(32):
   for j in range(32):
    assert sum(L[i][k]*S[k][j] for k in range(32))==sum(S[i][k]*G[k][j] for k in range(32))
  checked_similarity=True
 results.append({'q':str(q),'branch':kind,'r':[str(r) for r in rs],'negative_rate':str(bad[0][2]),'odd_rate':str(odd[0][2]),'full_similarity_checked':checked_similarity})
Path('inhomogeneous_checks.json').write_text(json.dumps({'status':'PASS','cases':results,'elapsed_seconds':time.monotonic()-start},indent=2),encoding='utf8');print('inhomogeneous PASS',len(results),'full similarity checks',sum(x['full_similarity_checked'] for x in results),flush=True)
