import common as c
from fractions import Fraction as F
from math import factorial
import json,time
def rank(p,order):
 v={}
 for s,w in enumerate(p):
  if not w:continue
  for r,j in enumerate(order,1):
   if s>>j&1:v=c.add(v,c.logv(r),w)
  v=c.add(v,c.logv(factorial(s.bit_count())),-w)
 return c.scale(v,F(6,5))
def rare(p,n):
 return sum((w*n*s.bit_count() for s,w in enumerate(p) if 120*s.bit_count()<11*n),F(0))
cases=0
for n in [1,2,3]:
 for mask in range(1<<(1<<n)):
  table=[1 if mask>>x&1 else -1 for x in range(1<<n)]
  p=[a*a for a in c.fwht(table)];N=sum(x==1 for x in table)
  old=rank(p,list(range(n)));qo=rare(p,n)
  for i in range(n):
   children=[];lp={};counts=[]
   for bit in [0,1]:
    t=[table[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1))]
    q=[a*a for a in c.fwht(t)];children.append(q);nc=sum(x==1 for x in t);counts.append(nc)
    if nc:lp=c.add(lp,c.logv(nc),(1-q[0])/2)
   av=c.scale(c.add(rank(children[0],list(range(n-1))),rank(children[1],list(range(n-1)))),F(1,2))
   delta={}
   for s,w in enumerate(p):
    if s>>i&1:delta=c.add(delta,c.logv(s.bit_count()),w)
   ii=sum(w for s,w in enumerate(p) if s>>i&1)
   delta=c.add(delta,c.logv(i+1),-ii)
   for j in range(i+1,n):
    ij=sum(w for s,w in enumerate(p) if s>>j&1)
    delta=c.add(delta,c.logv(F(j,j+1)),ij)
   c.check(c.add(av,old,F(-1))==c.scale(delta,F(6,5)))
   qr=sum((w*(n-1)*(s.bit_count()-((s>>i)&1)) for s,w in enumerate(p) if 120*(s.bit_count()-((s>>i)&1))<11*(n-1)),F(0))-qo
   c.check((rare(children[0],n-1)+rare(children[1],n-1))/2-qo==qr)
   parent=c.scale(c.logv(N),1-p[0]) if N else {}
   diff=c.add(parent,lp,F(-1));c.check(not diff or c.enclose(diff)[0]>=0)
   c.check(sum(counts)==N)
   residual=[F(0)]*(1<<(n-1))
   for s,w in enumerate(p):residual[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=w
   c.check(residual==[(a+b)/2 for a,b in zip(*children)])
   cases+=1
result={'helper':'A013-general-reset-v1','status':'PASS','physical_query_cases':cases,'exact_assertions':c.checks,'elapsed_seconds':time.perf_counter()-c.start,'failures':0}
(c.RUN/'out/GENERAL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
