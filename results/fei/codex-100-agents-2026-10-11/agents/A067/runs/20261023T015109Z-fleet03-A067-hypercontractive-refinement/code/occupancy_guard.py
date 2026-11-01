from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x;assert time.monotonic()-start<55
def sp(v):
 return [F(sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(len(v)))**2,len(v)**2) for s in range(len(v))]
def rest(v,j,b):return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2)]
def marg(q,j):return [a+b for a,b in zip(rest(q,j,0),rest(q,j,1))]
def ln(x):
 z=(x-1)/(x+1);a=sum((2*z**(2*k+1)/(2*k+1) for k in range(30)),F(0))
 return a,a+2*z**61/(61*(1-z*z))
ln2=ln(F(2))
def lg(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln(x);return k+a/ln2[1],k+b/ln2[0]
def ce(p,q):
 lo=hi=F(0)
 for a,b in zip(p,q):
  if a:
   l,u=lg(1/b);lo+=a*l;hi+=a*u
 return lo,hi
v=[]
for x in range(32):
 b=(-1)**(((x&3)==3)+(((x>>2)&3)==3));v.append(b-2*(x==0))
q=marg(sp(v),0);v=rest(v,0,0);p=sp(v);cp=ce(p,q);out=[]
for j,name in [(0,'exposed_Y2'),(3,'w'),(1,'intact_Y3')]:
 qr=marg(q,j);pr=marg(p,j);mismatch=[]
 for x in range(len(p)):
  row=(x&((1<<j)-1))|((x>>(j+1))<<j)
  if p[x]*qr[row]!=q[x]*pr[row]:mismatch.append(x)
 v0,v1=rest(v,j,0),rest(v,j,1);p0,p1=sp(v0),sp(v1)
 ck(set(v0)=={-1,1});ck(set(v1)=={-1,1});ck(sum(qr)==1);ck(all(x>0 for x in qr))
 inf=F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
 c0,c1=ce(p0,qr),ce(p1,qr)
 e=(cp[0]-(c0[1]+c1[1])/2-2*inf,cp[1]-(c0[0]+c1[0])/2-2*inf)
 if name.startswith('intact'):ck(not mismatch);ck(e[1]<0)
 else:ck(bool(mismatch));ck(e[0]>0)
 out.append({'query':name,'mismatching_pairs':len(mismatch)//2,'physical_influence':str(inf),'signed_debit_lower':str(e[0]),'signed_debit_upper':str(e[1]),'approx':float(sum(e)/2)})
(R/'out/OCCUPANCY_GUARD.json').write_text(json.dumps({'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'rows':out},indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','checks':checks,'rows':[{k:v for k,v in x.items() if k not in ('signed_debit_lower','signed_debit_upper')} for x in out]}))
