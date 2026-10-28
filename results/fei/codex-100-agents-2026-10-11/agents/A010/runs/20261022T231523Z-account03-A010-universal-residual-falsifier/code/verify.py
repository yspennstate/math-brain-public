from pathlib import Path
from fractions import Fraction as F
from math import comb,prod
from itertools import product
import json,time
B=Path(__file__).resolve().parents[1];O=B/'out';start=time.monotonic();checks=0;events=0;labels=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
data=json.loads((O/'SMALL_TRACES.json').read_text(encoding='utf-8'))
for row in data:
 a,b,k=row['a'],row['b'],row['k'];n=a+b;lam=F(1,b)
 E=[(i,a+j) for i in range(a) for j in range(b) if not(i==j and i<k)]
 D=(1+lam/4)**len(E)-1
 for tr in row['traces']:
  A=tr['A'];z=tr['single_trace'];owned={int(i):s for i,s in z['owned'].items()};children={int(i):v for i,v in z['children'].items()};roots=z['roots']
  ck(sum(owned.values())==A);ck(all(not(owned[i]&owned[j]) for i in owned for j in owned if i<j))
  # Independent normalized Bernoulli law retains all absent gates.
  raw=prod((lam/4)/(1+lam/4) if i in roots else 1/(1+lam/4) for i in range(len(E)))
  raw/=1-(1+lam/4)**(-len(E));ck(raw==prod(lam/4 for i in roots)/D)
  queue=roots[:];seen=set();union=0
  while queue:
   i=queue.pop(0);ck(i not in seen);seen.add(i);S=owned[i];s=S.bit_count();ck(S&sum(1<<v for v in E[i])==S);union|=S
   raw/=s*(s+1)*comb(2,s)
   c=len(children[i]);raw/=F((c+1)*(c+2)*comb(s+c-1,c))
   ck(children[i]==sorted(children[i]))
   for v,j in children[i]:
    ck(S>>v&1 and v in E[j]);raw*=lam;queue.append(j)
  ck(union==A and seen==set(owned));ck(raw*D>=(lam/72)**A.bit_count())
  events+=1
  U=A&((1<<a)-1);V=A>>a
  if U and V:ck(raw*D==F(tr['numerator']))
  else:
   vertices=[i for i in range(n) if A>>i&1];choices=[[j for j,e in enumerate(E) if i in e] for i in vertices];total=F(0)
   for assigned in product(*choices):
    ck(len(set(assigned))==len(assigned));total+=(lam/32)**len(assigned);labels+=1
   ck(total==F(tr['numerator']))
  # Direct character summation, not FWHT or a helper import.
  coeff=F(sum((1 if any(x>>i&1 and x>>j&1 for i,j in E) else -1)*(-1 if (x&A).bit_count()%2 else 1) for x in range(1<<n)),1<<n)
  r=sum(((U>>i)^(V>>i))&1 for i in range(k))
  ck(coeff==-2*((F(1,2**a) if not V else 0)+(F(1,2**b) if not U else 0)+F(k-1-2*r,2**n)))
 ck(time.monotonic()-start<55)
cuts=0
for w in range(1,4):
 for subset in range(1,(1<<(1<<w))-1):
  boundary=sum(1 for x in range(1<<w) for j in range(w) if x<(x^(1<<j)) and ((subset>>x)^(subset>>(x^(1<<j))))&1)
  ck(boundary>=w);cuts+=1
result={'status':'PASS','helper':'A010-independent-replay-v1','functions':len(data),'events':events,'one_sided_label_choices':labels,'cube_subsets':cuts,'assertions':checks,'seconds':time.monotonic()-start,'imports_author_helpers':False}
(O/'VERIFY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
