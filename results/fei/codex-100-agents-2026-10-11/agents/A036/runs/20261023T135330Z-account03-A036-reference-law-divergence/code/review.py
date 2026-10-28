from pathlib import Path
from fractions import Fraction as F
from math import comb
import exact as E
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
 assert time.perf_counter()-start<55
def KL(p,q):return E.kl(p,[E.iv(v) for v in q])
def ref(p,s):
 q=[F(5,6)*x for x in p];q[0]=p[0];q[s]+=F(1,6)*(1-p[0]);ck(sum(q)==1)
 return q
def step(t,q,i):
 p=E.law(t);ts=[E.restrict(t,i,y) for y in [0,1]];ps=[E.law(v) for v in ts]
 ids=[j for j in range(len(p)) if not j>>i&1]
 pb=[p[j]+p[j|(1<<i)] for j in ids];qb=[q[j]+q[j|(1<<i)] for j in ids]
 ck(pb==[(a+b)/2 for a,b in zip(*ps)])
 ks=[[v/(2*w) if w else F(1,2) for v,w in zip(pp,pb)] for pp in ps]
 out=[sum((v*w for v,w in zip(qb,k)),F(0)) for k in ks];ck(sum(out)==1 and min(out)>0)
 qs=[[v*w/o for v,w in zip(qb,k)] for k,o in zip(ks,out)]
 for pp,qq in zip(ps,qs):ck(sum(qq)==1 and all(not v or w>0 for v,w in zip(pp,qq)))
 O=E.scale(F(-1,2),E.logpoint(4*out[0]*out[1]));er=E.sub(KL(p,q),KL(pb,qb))
 meanK=E.scale(F(1,2),E.total(KL(pp,qq) for pp,qq in zip(ps,qs)))
 ck(E.overlaps(KL(p,q),E.add(meanK,E.add(O,er))))
 return ts,qs,out,O,er
def core(k,m,r):
 t=[]
 for x in range(1<<(k+m)):
  z=x&((1<<k)-1);y=x>>k;v=1-2*(z&1)
  if z in (2,3):v=-v
  if z==0 and y.bit_count()%3==r:v=-v
  t.append(v)
 return t
def A(m,r):return F(sum((-1)**w*comb(m,w) for w in range(m+1) if w%3==r),1<<m)
def rho(m,r):return F(sum(comb(m,w) for w in range(m+1) if w%3==r),1<<m)
def run(k,m,r):
 t=core(k,m,r);p=E.law(t);q=ref(p,len(p)-1);d=F(1,1<<k)
 ft=E.fwht(t);ck(F(ft[0],len(t))==-2*d*rho(m,r));ck(F(ft[-1],len(t))==-2*d*A(m,r));ck(p[-1]>0)
 ck(all(bool(a)==bool(b) for a,b in zip(p,q)))
 ts,qs,out,O,er=step(t,q,k)
 den=A(m-1,r)**2+A(m-1,(r-1)%3)**2
 bias=(A(m-1,r)**2-A(m-1,(r-1)%3)**2)/den
 mu=F(ft[0],len(t));nu=F(ft[1<<k],len(t));d0=2*mu*nu/(mu*mu+nu*nu) if mu or nu else F(0)
 eta=F(1,6)*(mu*mu*d0+(1-mu*mu)*bias);ck(2*out[0]-1==eta)
 if bias:ck(abs(bias)>=F(3,5) and (k<4 or abs(eta)>F(1,12)))
 old=[];fresh=[];release=E.add(O,er)
 for child,qq in zip(ts,qs):
  ls,rs,oo,o,e=step(child,qq,k);release=E.add(release,E.scale(F(1,2),E.add(o,e)))
  for v,rr in zip(ls,rs):
   pp=E.law(v);ff=ref(pp,len(pp)-1)
   ck(pp[-1]>0);ck(all(bool(a)==bool(b) for a,b in zip(pp,rr)))
   ck(all(bool(a)==bool(b) for a,b in zip(pp,ff)))
   old.append(KL(pp,rr));fresh.append(KL(pp,ff))
 sigma=E.scale(F(1,4),E.total(E.sub(a,b) for a,b in zip(fresh,old)))
 telescope=E.add(E.sub(E.scale(F(1,4),E.total(fresh)),KL(p,q)),release)
 ck(E.overlaps(sigma,telescope))
 return {'k':k,'m':m,'r':r,'eta':str(eta),'sigma':E.enc(sigma),'release':E.enc(release)}
def main():
 pilot='--pilot' in sys.argv
 domain=[(3,2,r) for r in range(3)] if pilot else [(k,m,r) for k in [3,4] for m in [2,4,6] for r in range(3)]
 results=[run(*x) for x in domain]
 # Infinite bridge checked independently using integer binomial phase counts.
 for m in range(1,43):
  for r in range(3):ck(A(m+6,r)==-F(27,64)*A(m,r))
 for m in range(2,44,2):
  ck(all(A(m,r) for r in range(3)))
  biases=[(A(m-1,r)**2-A(m-1,(r-1)%3)**2)/(A(m-1,r)**2+A(m-1,(r-1)%3)**2) for r in range(3)]
  ck(sum(bool(x) for x in biases)==2);ck(all(not x or abs(x)>=F(3,5) for x in biases))
 n=65536;bound=F(n-4,4608)-F(1,15);ck(bound==F(9059,640));ck(bound-8==F(3939,640))
 for rr in range(3,15):
  T=2**rr;l=2*(rr+1);ck(T*F(3939,640)>4*(l+1))
 receipt={'status':'PASS','cases':len(results),'assertions':checks,'interval_assertions':E.checks,'seconds':time.perf_counter()-start,'results':results,'large_bill_lower':str(bound),'large_deficit_lower':str(bound-8)}
 (R/'out'/('REVIEW_PILOT.json' if pilot else 'REVIEW_CHECK.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in receipt.items() if k!='results'}))
if __name__=='__main__':main()
