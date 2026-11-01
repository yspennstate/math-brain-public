from fractions import Fraction as F
from pathlib import Path
import json,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(p):
 global checks
 checks+=1
 assert p,checks
def root(x,y):
 D=(1+x/4)*(1+y/4)-1
 return x/(4*D),y/(4*D),x*y/(16*D)
def verify(p,q,r):
 x,y=4*r/q,4*r/p
 det=(p-4*r)*(q-4*r)-16*r*r
 ck(det==p*q-4*r*(p+q))
 ck((x+y<=1)==(det>=0))
 ck(root(x,y)==(p,q,r))
 if det>=0:
  ck(p>=4*r and q>=4*r and r<=F(1,17))
  for t in [F(0),F(1,4),F(1,2),F(1),F(2),F(4)]:
   ck(t*t*p+q-4*(t+1)**2*r>=0)
 return x,y,det
for i in range(1,16):
 for j in range(1,17-i):
  x,y=F(i,16),F(j,16);p,q,r=root(x,y)
  xx,yy,det=verify(p,q,r);ck((xx,yy)==(x,y) and det>=0)
count=0;feasible=0
for i in range(1,17):
 for j in range(1,18-i):
  p,q,r=F(i,18),F(j,18),F(18-i-j,18);x,y,det=verify(p,q,r)
  count+=1;feasible+=det>=0
p,q,r=F(2,3),F(5,18),F(1,18);x,y,det=verify(p,q,r);t=F(1,2)
cut=t*t*p+q-4*(t+1)**2*r
ck(p+q+r==1 and 0<r<F(1,17) and p>4*r and q>4*r)
ck(x==F(4,5) and y==F(1,3) and det==F(-2,81) and cut==F(-1,18))
result={'status':'PASS','helper':'A010-pair-cone-v1','packing_pairs':120,'probability_vectors':count,'feasible_vectors':feasible,'assertions':checks,'seconds':time.monotonic()-start,'falsifier':{'p':[str(p),str(q),str(r)],'lambda':[str(x),str(y)],'determinant':str(det),'cut_t':str(t),'cut_value':str(cut)}}
ck(result['seconds']<20)
(B/'out/PAIR.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
