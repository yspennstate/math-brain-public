from pathlib import Path
from fractions import Fraction as F
import sys,time,json
import check as s
p=s.p;e=s.e;R=s.R;start=time.monotonic();mode=p.MODE;nodes=resets=controls=datas=0
def physical(a,g,h,Q,j):
 c=len(a);r=c.bit_length()-1
 if j>=r:return s.structural(a,g,h,Q,j)
 v=s.mux(a,g,h);P=p.spectrum(v);mp=p.marginal(P,j);mq=p.marginal(Q,j)
 aa=[p.child(a,j,z) for z in (0,1)];pa=p.spectrum(a);ma=p.marginal(pa,j);pp=[p.spectrum(p.child(v,j,z)) for z in (0,1)];ac=[p.spectrum(x) for x in aa];newc=c//2
 joint=[]
 for z in (0,1):
  q=[]
  for i in range(len(mp)):
   u=i%newc
   kval=(ac[z][u]/(2*ma[u]) if ma[u] else F(1,2)) if u else (pp[z][i]/(2*mp[i]) if mp[i] else F(1,2))
   if mp[i]:p.ck(kval==pp[z][i]/(2*mp[i]),'controller structural true-phase agreement')
   q.append(mq[i]*kval)
  joint.append(tuple(q))
 rho=tuple(sum(q) for q in joint);p.ck(sum(rho)==1 and min(rho)>0)
 qq=tuple(tuple(x/rho[z] for x in joint[z]) for z in (0,1))
 for z in (0,1):
  if newc>1:
   q0,q1,b=s.extract(qq[z],newc)
   if b is not None:p.ck(s.make(q0,q1,b)==qq[z])
 return aa,qq,rho
def run(a,g,h,Q,policy,depth=0,path=()):
 global nodes,resets,controls,datas
 nodes+=1;c=len(a);r=c.bit_length()-1;d=len(g).bit_length()-1;v=s.mux(a,g,h);P=p.spectrum(v);original=Q;charge={}
 if c>1:
  pa=p.spectrum(a);V=1-pa[0];pi=tuple(x/V for x in pa[1:]) if V else (F(1,c-1),)*(c-1)
  phi=(F(1,8) if depth==0 else F(3,16) if (depth+sum(path))%2 else F(0)) if r==3 else (F(0),F(1,4096),F(1,2048))[(depth+policy)%3]
  b=s.mix(pi,phi);x,y=s.split(Q,c);Q=s.make(x,y,b);charge=p.sub(p.CE(P,Q),p.CE(P,original));resets+=1
 n=r+d
 if not n or (policy==5 and depth>2 and sum(path)%3==1):return p.CE(P,Q),charge,{}
 if not r:j=0
 elif not d:j=(depth+policy)%r
 elif policy==0:j=0 if depth%2 else r
 elif policy==1:j=r if depth%2 else r-1
 elif policy==2:j=r+d-1 if r==3 else 0
 elif policy==3:j=r-1 if r==3 else r+d-1
 elif policy==4:j=(sum(path)+depth)%n
 else:j=0 if sum(path)%2 else r+d-1
 if j<r:
  aa,qq,rho=physical(a,g,h,Q,j);gg=[g,g];hh=[h,h];controls+=1
 else:
  gg,hh,qq,rho=physical(a,g,h,Q,j);aa=[a,a];datas+=1
 vv=[s.mux(aa[z],gg[z],hh[z]) for z in (0,1)];dh=p.sub(e.entropy(P),p.avg(*(e.entropy(p.spectrum(x)) for x in vv)))
 refund=p.sub(p.CE(P,Q),e.add(dh,p.avg(*(p.CE(p.spectrum(vv[z]),qq[z]) for z in (0,1)))))
 p.nn(refund,'complete two-sided structural query refund')
 cs=[run(aa[z],gg[z],hh[z],qq[z],policy,depth+1,path+(z,)) for z in (0,1)]
 pay=e.add(dh,p.avg(cs[0][0],cs[1][0]));charges=e.add(charge,p.avg(cs[0][1],cs[1][1]));refunds=e.add(refund,p.avg(cs[0][2],cs[1][2]))
 p.eq(pay,e.add(p.CE(P,original),charges,p.neg(refunds)))
 return pay,charges,refunds
def main():
 endpoint=e.add(e.scale(e.lg(F(16807,15606)),F(9,64)),e.scale(e.lg(F(2048,2047)),F(3,2)))
 p.ck(16807**144*2048**1536 < 2**17*15606**144*2047**1536)
 p.nn(p.sub(p.const(F(17,1024)),endpoint));rows=[]
 for m in ([1] if mode=='pilot' else [1,2]):
  root,kids=p.instance(m);v,Q,W,Z=kids[1];g=tuple(v[8*t+3] for t in range(len(v)//8));h=tuple(v[8*t] for t in range(len(v)//8))
  for policy in (range(1) if mode=='pilot' else range(6)):
   before=(nodes,resets,controls,datas);pay,charges,refund=run(p.AA,g,h,Q,policy)
   p.nn(p.sub(endpoint,charges));p.nn(p.sub(e.add(p.CE(p.spectrum(v),Q),endpoint),pay))
   dh=p.sub(e.entropy(p.spectrum(root[0])),p.avg(*(e.entropy(p.spectrum(x[0])) for x in kids)))
   total=e.add(dh,p.avg(p.CE(p.spectrum(kids[0][0]),kids[0][1]),pay));reserve=p.sub(p.const(4*(m+F(29,16))-F(1,8)),total)
   lower=3*m-F(15,8)+F(143,329728);p.nn(p.sub(reserve,p.const(lower)))
   rows.append({'m':m,'policy':policy,'nodes':nodes-before[0],'resets':resets-before[1],'controller_nodes':controls-before[2],'DATA_nodes':datas-before[3],'signed_charge_interval':p.bounds(charges),'original_quota_reserve_interval':p.bounds(reserve)})
 out={'status':'PASS','mode':mode,'assertions':p.count,'nodes':nodes,'resets':resets,'controller_nodes':controls,'DATA_nodes':datas,'histories':len(rows),'seconds':time.monotonic()-start,'endpoint_interval':p.bounds(endpoint),'rows':rows}
 (R/'out'/('MIXED_PILOT.json' if mode=='pilot' else 'MIXED_VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
