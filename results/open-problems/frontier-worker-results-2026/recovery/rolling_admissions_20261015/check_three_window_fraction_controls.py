from pathlib import Path
from fractions import Fraction as F
from itertools import product
from datetime import datetime
import hashlib,json
H=Path(__file__).resolve().parent;states=list(product([1,2],repeat=3));ids={x:i for i,x in enumerate(states)};n=8;L=[[F(0) for j in range(n)] for i in range(n)];reward=[];events=[]
for i,(a,b,c) in enumerate(states):
 terms=[]
 if a==1:terms.append((26,(2,b,c)))
 if b==1:terms.append((26+max(a-b,0),(a,2,c)))
 if c==1:terms.append((26+max(b-c,0),(a,b,2)))
 terms.append((c,(b,c,1)));events.append(terms);reward.append(F(c))
 for rate,child in terms:L[i][ids[child]]+=rate;L[i][i]-=rate
def solve(mat,y):
 a=[list(row)+[val] for row,val in zip(mat,y)];N=len(y)
 for j in range(N):
  pivot=next(k for k in range(j,N) if a[k][j]);a[j],a[pivot]=a[pivot],a[j];z=a[j][j];a[j]=[x/z for x in a[j]]
  for k in range(N):
   if k!=j:
    z=a[k][j];a[k]=[x-z*y for x,y in zip(a[k],a[j])]
 return [row[-1] for row in a]
mat=[list(row) for row in zip(*L)];mat[-1]=[F(1)]*n;pi=solve(mat,[F(0)]*(n-1)+[F(1)]);assert min(pi)>0
stationary=1/sum(p*r for p,r in zip(pi,reward))
sub=[[-L[i][j] for j in range(1,n)] for i in range(1,n)]
times=[F(0)]+solve(sub,[F(1)]*7);adv=[F(0)]+solve(sub,reward[1:]);total=sum(rate for rate,_ in events[0])
T=F(1,total)+sum(F(rate,total)*times[ids[child]] for rate,child in events[0])
A=F(1,total)+sum(F(rate,total)*adv[ids[child]] for rate,child in events[0]);assert T/A==stationary
wrong=T/(A-F(1,total));assert wrong!=stationary
r=json.loads((H/'T170_THREE_COMPRESSED_d14_C2_RECEIPT.json').read_bytes());bound=F(r['axis']);assert 0<=bound-stationary<F(1,10**7)
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS independent8-state exact generator/stationary/first-cycle controls','time':str(T),'advance':str(A),'ratio':str(T/A),'certified_C2_bias_upper':str(bound),'omitted_self_ratio':str(wrong),'cap1_ratio':'1','checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(H/'T170_THREE_FRACTION_CONTROL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
