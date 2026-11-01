import math,json,time
from fractions import Fraction as Q
from pathlib import Path
start=time.monotonic();run=Path(__file__).resolve().parents[1]
(run/'out').mkdir(exist_ok=True)
def walsh(v):
 a=list(v);step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
  step*=2
 return [Q(x,len(a)) for x in a]
def ell(a,b):
 u=float(a*a);v=float(b*b);s=u+v
 return sum(x*math.log2(s/x) for x in [u,v] if x)
found=[]
for sign in [-1,1]:
 b=[sign*(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16)]
 for point in range(16):
  c=b.copy();c[point]*=-1
  p,q=walsh(b),walsh(c)
  a=[(x+y)/2 for x,y in zip(p,q)];beta=[(x-y)/2 for x,y in zip(p,q)]
  B=sum(ell(x,y) for x,y in zip(a,beta));d=Q(1,16)
  rows=[]
  for j in range(1,33):
   r=Q(j,32)
   R=ell(1-r+r*a[0],r*beta[0])+float(r*(1-r))*ell(1-a[0],beta[0])-float(r)*ell(a[0],beta[0])
   rows.append((str(r),(float(r)*B+R)/float(r*d)))
  if min(x[1] for x in rows)<4<max(x[1] for x in rows):found.append({'sign':sign,'point':point,'mean':str(a[0]),'B_over_d':B/float(d),'rows':rows})
out={'status':'DISCOVERY_ONLY','crossings':found,'runtime_seconds':time.monotonic()-start}
(run/'out/DISCOVERY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out)[:10000])
