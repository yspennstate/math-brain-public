"""Independent butterfly Walsh reconstruction of sharp ghost prepayment."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T034945Z-fleet03-A079-correlated-auxiliaries/code'
sys.path.insert(0,str(OLD));import check as c
def walsh(v):
 w=list(v);step=1
 while step<len(w):
  for lo in range(0,len(w),2*step):
   for j in range(lo,lo+step):
    x,y=w[j],w[j+step];w[j]=x+y;w[j+step]=x-y
  step*=2
 return tuple(F(x,len(w)) for x in w)
def prob(v):return tuple(x*x for x in walsh(v))
a,b=c.rows((-1,)*4);A,B=walsh(a),walsh(b);beta=sum(x*x for x in B)
def reference(r):return tuple(A[u]**2 if t==0 else B[u]**2*r[t] for t in range(len(r)) for u in range(16))
start=time.monotonic();records=[]
h=tuple((-1)**x.bit_count() for x in range(8))
for rho in (F(0),F(1,128),F(1,64),F(1,32),F(1,2)):
 for lam in (F(0),rho/2,rho,F(1,64)):
  for s in (1,-1):
   if time.monotonic()-start>30:raise TimeoutError('frozen30s')
   r=tuple((1-rho)*(t==7)+rho*(t==1) for t in range(8));q=reference(r)
   v=tuple(x+s*y*z for z in h for x,y in zip(a,b));p=prob(v)
   surcharge=c.add((1,c.ce(p,q)),(-1,c.ent(p)))
   c.ok(surcharge==c.add((beta,c.log(1/(1-rho)))))
   c.ok(sum(q)==1);c.ok(c.erasure(p,4)=={});c.ok(sum(v for t,v in enumerate(p) if t>>4&1)==beta)
   rnew=(F(0),lam,F(0),1-lam);qnew=reference(rnew);terminals=[];cost=[]
   for bit in (0,1):
    vv=tuple(z for j,z in enumerate(v) if (j>>4)&1==bit);pp=prob(vv)
    c.ok(all(z in (-1,1) for z in vv));c.ok(sum(qnew)==1)
    terminals.append(dict(truth=vv,spectrum=pp,complete_reference=qnew));cost.append(c.ce(pp,qnew))
   c.ok(terminals[0]['spectrum']==terminals[1]['spectrum'])
   inc=c.add((F(1,2),cost[0]),(F(1,2),cost[1]),(-1,c.ce(p,q)))
   c.ok(inc==c.add((beta,c.log((1-rho)/(1-lam)))))
   records.append(dict(rho=rho,lambda_=lam,source_injection_cost=surcharge,increment=inc,source_reference=r,complete_incoming_reference=q,both_full_terminals=terminals))
out=dict(status='PASS',transactions=len(records),assertions=c.checks,seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),method='independent butterfly FWHT and exact prime-log identities; both full physical child truths',records=records)
(ROOT/'out/independent.json').write_text(json.dumps(c.dump(out),indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
