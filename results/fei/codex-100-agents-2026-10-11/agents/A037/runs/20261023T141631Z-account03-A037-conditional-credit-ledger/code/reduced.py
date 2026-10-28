from fractions import Fraction as F
from pathlib import Path
import json,time
import exact as E
R=Path(__file__).resolve().parents[1]
def local(w,mu,beta):
 d=F(1,2**w);alpha=1-beta;n=2**(w-1);v=4*d*(1-d);B=[];P=[];Y=[[],[]]
 for typ,count in [(0,1),(1,1),(2,n-2)]:
  if not count:continue
  for U in [0,1]:
   mass=mu*mu if U==0 else 1-mu*mu
   for c in [1,-1]:
    yy=[]
    for y,a in [(0,F(1)),(1,1-4*d)]:
     if typ==0 and U==0:z=(1+c*a*mu)**2/4
     else:z=(a*a if typ==0 else (16*d*d if y else 0))*mass/4
     yy.append(z*count)
    p=sum(yy)/2
    b=p-alpha*d*d*mass if typ==0 else beta*p+(alpha*v*mass/4 if typ==1 else 0)
    P.append(p);B.append(b)
    for y in [0,1]:Y[y].append(yy[y])
 assert sum(P)==sum(B)==sum(Y[0])==sum(Y[1])==1
 outs=[sum((b*yy/(2*p) if p else 0 for p,b,yy in zip(P,B,Y[y])),F(0)) for y in [0,1]]
 assert sum(outs)==1
 dp=E.kl(P,[E.iv(x) for x in B]);out=E.kl([F(1,2)]*2,[E.iv(x) for x in outs])
 if w==2:new=E.iv(0)
 else:
  pp=[(1-4*d)**2,16*d*d,(n-2)*16*d*d];qq=[pp[0],beta*pp[1]+alpha*(1-pp[0]),beta*pp[2]]
  new=E.scale(F(1,4),E.kl(pp,[E.iv(x) for x in qq]))
 sigma=E.add(E.sub(new,dp),out)
 return sigma,outs,dp,new,P,B,Y
if __name__=='__main__':
 start=time.perf_counter();rows=[]
 for w in range(2,13):
  for j in range(9):
   for beta in [F(5,6),F(4,5)]:
    s,o,d,k,*_=local(w,F(j,8),beta)
    rows.append({'w':w,'mu':str(F(j,8)),'beta':str(beta),'sigma':E.enc(s),'outcomes':list(map(str,o))})
    assert time.perf_counter()-start<55
 receipt={'status':'PASS','cases':len(rows),'strict_positive':sum(F(x['sigma'][0])>0 for x in rows),'strict_negative':sum(F(x['sigma'][1])<0 for x in rows),'unresolved_zero':sum(F(x['sigma'][0])<=0<=F(x['sigma'][1]) for x in rows),'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'rows':rows}
 (R/'out/REDUCED.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in receipt.items() if k!='rows'}))
 print('POSITIVE',next((x for x in rows if F(x['sigma'][0])>0),None))
