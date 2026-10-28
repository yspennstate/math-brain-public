from pathlib import Path
from fractions import Fraction as F
import json,time
RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
def series(y):
 z=(y-1)/(y+1)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return lo,lo+2*z**41/(41*(1-z*z))
L2,U2=series(F(2))
def logbounds(x):
 if x<1:
  a,b=logbounds(1/x);return -b,-a
 k=0
 while x>=2:x/=2;k+=1
 a,b=series(x);return a+k*L2,b+k*U2
start=time.perf_counter();fibers=0;gates=0
for n in [1,2,3]:
 N=2**n
 for truth in range(2**N):
  for R in range(1,N):
   inside=[i for i in range(n) if R>>i&1];outside=[i for i in range(n) if not R>>i&1];w=len(inside)
   for pattern in range(2**w):
    def point(u,z):
     return sum(((u>>j)&1)<<i for j,i in enumerate(inside))+sum(((z>>j)&1)<<i for j,i in enumerate(outside))
    if not all(truth>>point(pattern,z)&1 for z in range(2**len(outside))):continue
    gates+=1
    all_false=0;all_boundary=0
    for z in range(2**len(outside)):
     bad={u for u in range(2**w) if not truth>>point(u,z)&1}
     boundary=sum((u in bad)!=(u^(1<<j) in bad) for u in range(2**w) for j in range(w) if not u>>j&1)
     ck(len(bad)<2**w)
     ck(not bad or boundary>=w)
     ck(boundary*(2**w-1)>=w*len(bad))
     all_false+=len(bad);all_boundary+=boundary;fibers+=1
    ck(all_boundary*(2**w-1)>=w*all_false)
for w in range(1,129):
 q=1-F(1,2**w);I=F(w,2**(w-1));a=(1-F(1,2**w))/w
 ck(F(1,2**w)==a*I/(2*q))
 ck((1-F(1,2**(w+1)))/(w+1)<=a)
ck(3**5<2**8 and L2>F(2,3))
ck(F(33,5)+F(9,4)+F(9,8)==F(399,40)<10)
normalizers=[]
for m in range(1,9):
 q=F(3,4)**m;I=m*F(3,4)**(m-1);v=4*q*(1-q);D=F(5,4)**m-1;S=F(m,4)
 ck(S==F(3,8)*I/(2*q))
 lo,hi=logbounds(D)
 ck(v*hi<=F(3,4)*(1-q)*I)
 normalizers.append(dict(m=m,D=str(D),sign='negative' if D<1 else 'positive' if D>1 else 'zero'))
# Hypotheses that cannot be dropped: build each physical fixture.
def physical(n,fn):
 values=[fn(x) for x in range(2**n)]
 q=F(values.count(-1),2**n)
 influences=[F(sum(values[x]!=values[x^(1<<i)] for x in range(2**n)),2**n) for i in range(n)]
 return q,influences,values
q,inf,values=physical(2,lambda x:1 if x&2 else -1)
ck(any(values[x]==-1 for x in range(4) if x&1))
ck(inf[0]<2*q) # alleged width-one gate x_1 does not imply f=x_2
q,inf,_=physical(1,lambda x:1 if x&1 else -1)
ck(8*F(1,2)>sum(inf)/(4*q)) # lambda=8 violates the packing row
q,inf,_=physical(2,lambda x:1 if x==3 else -1)
ck(F(1)>F(3,8)*sum(inf)/(2*q)) # AND2 with false rarity pi=1
result=dict(status='PASS',functions=276,implicants=gates,fibers=fibers,exact_assertions=checks,normalizers=normalizers,elapsed_seconds=time.perf_counter()-start)
(RUN/'out/VERIFY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
