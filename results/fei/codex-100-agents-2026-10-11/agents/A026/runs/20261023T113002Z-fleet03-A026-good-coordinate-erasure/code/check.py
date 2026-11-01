from pathlib import Path
from fractions import Fraction as F
import sys,time,json
import prior as p
e=p.e;R=Path(__file__).resolve().parents[1];MODE=p.MODE;START=time.monotonic()
PH=(F(0),F(1,512),F(1,256));rows=[];fair_guard=[];prefixes=0
def split(Q,c):
 return tuple(Q[c*t] for t in range(len(Q)//c)),tuple(sum(Q[c*t+1:c*t+c]) for t in range(len(Q)//c))
def make(q0,q1,b):
 c=len(b)+1;return tuple(q0[t] if u==0 else q1[t]*b[u-1] for t in range(len(q0)) for u in range(c))
def mix(pi,t):return tuple((1-t)*x+t/F(len(pi)) for x in pi)
def mux(a,g,h):return tuple((g if a[u]==1 else h)[t] for t in range(len(g)) for u in range(len(a)))
def profile(a):
 P=p.spectrum(a);V=1-P[0];assert V
 return tuple(x/V for x in P[1:]),V
def extract(Q,c):
 q0,q1=split(Q,c);t=next((i for i,x in enumerate(q1) if x),None)
 if t is None:return q0,q1,None
 b=tuple(x/q1[t] for x in Q[c*t+1:c*t+c]);p.ck(make(q0,q1,b)==Q,'factorization')
 return q0,q1,b
def structural(a,g,h,Q,j):
 c=len(a);k=j-(c.bit_length()-1);v=mux(a,g,h);P=p.spectrum(v)
 vv=tuple(p.child(v,j,z) for z in (0,1));gg=tuple(p.child(g,k,z) for z in (0,1));hh=tuple(p.child(h,k,z) for z in (0,1))
 D=tuple(F(x-y,2) for x,y in zip(g,h));PD=p.spectrum(D);md=p.marginal(PD,k)
 dd=[p.spectrum(tuple(F(x-y,2) for x,y in zip(gg[z],hh[z]))) for z in (0,1)]
 mp=p.marginal(P,j);mq=p.marginal(Q,j);pp=[p.spectrum(x) for x in vv];ks=[]
 for z in (0,1):
  kz=[]
  for i in range(len(mp)):
   u=i%c;t=i//c
   kval=(dd[z][t]/(2*md[t]) if md[t] else F(1,2)) if u else (pp[z][i]/(2*mp[i]) if mp[i] else F(1,2))
   if mp[i]:p.ck(kval==pp[z][i]/(2*mp[i]),'actual phase agreement')
   kz.append(kval)
  ks.append(kz)
 p.ck(all(x+y==1 for x,y in zip(*ks)))
 joint=[tuple(q*k for q,k in zip(mq,kz)) for kz in ks];rho=tuple(sum(x) for x in joint)
 p.ck(min(rho)>0 and sum(rho)==1)
 qq=tuple(tuple(x/rho[z] for x in joint[z]) for z in (0,1))
 return gg,hh,qq,rho
def walk(a,g,h,Q,b,d):
 global prefixes
 prefixes+=1;c=len(a);pi,V=profile(a);v=mux(a,g,h);P=p.spectrum(v);q0,q1=split(Q,c)
 p.ck(Q==make(q0,q1,b));p.ck(sum(Q)==1)
 PD=p.spectrum(tuple(F(x-y,2) for x,y in zip(g,h)))
 p.ck(all(not qt or PD[t] for t,qt in enumerate(q1)),'D support')
 for phi in PH:
  bt=mix(pi,phi);qt=make(q0,q1,bt)
  p.ck(sum(qt)==1)
  for i,prob in enumerate(P):
   if prob:p.ck(qt[i]/Q[i]==(bt[i%c-1]/b[i%c-1] if i%c else 1))
 if not d:return
 for k in range(d):
  j=c.bit_length()-1+k;gg,hh,qq,rho=structural(a,g,h,Q,j)
  # One altered profile per edge suffices to reject a normalization dependent on shape.
  alt=mix(pi,PH[0]);_,_,qa,ra=structural(a,g,h,make(q0,q1,alt),j)
  p.ck(ra==rho,'structural profile-independent CURRENT rho')
  _,qfair,_=p.physical(v,Q,j)
  for z in (0,1):
   x,y=split(qq[z],c);p.ck(qa[z]==make(x,y,alt))
   xf,yf=split(qfair[z],c)
   if qfair[z]!=make(xf,yf,b) and len(fair_guard)<1:
    fair_guard.append({'a':list(a),'g':list(g),'h':list(h),'b':list(map(str,b)),'Q':list(map(str,Q)),'DATA_index':k,'outcome':z,'fair_rho_changes_shape':True})
   walk(a,gg[z],hh[z],qq[z],b,d-1)
def subtree(a,g,h,Q,d,policy,depth=0):
 c=len(a);pi,V=profile(a);v=mux(a,g,h);P=p.spectrum(v);q0,q1,b=extract(Q,c)
 if b is None:return p.CE(P,Q),{},{}
 phi=PH[-1] if (depth+policy)%2 else PH[1];qn=make(q0,q1,mix(pi,phi))
 charge=p.sub(p.CE(P,qn),p.CE(P,Q));eta=sum(P[i] for i in range(len(P)) if i%c)
 p.eq(charge,e.scale(p.sub(p.KL(pi,mix(pi,phi)),p.KL(pi,b)),eta),'post-control signed reset')
 if not d or (policy==1 and depth>0 and depth%2):return p.CE(P,qn),charge,{}
 k=d-1 if policy==1 else 0;j=c.bit_length()-1+k;gg,hh,qq,rho=structural(a,g,h,qn,j)
 vv=[mux(a,gg[z],hh[z]) for z in (0,1)]
 dh=p.sub(e.entropy(P),p.avg(*(e.entropy(p.spectrum(x)) for x in vv)))
 ref=p.sub(p.CE(P,qn),e.add(dh,p.avg(*(p.CE(p.spectrum(vv[z]),qq[z]) for z in (0,1)))))
 p.nn(ref,'full structural query refund')
 cs=[subtree(a,gg[z],hh[z],qq[z],d-1,policy,depth+1) for z in (0,1)]
 pay=e.add(dh,p.avg(cs[0][0],cs[1][0]));charges=e.add(charge,p.avg(cs[0][1],cs[1][1]));refund=e.add(ref,p.avg(cs[0][2],cs[1][2]))
 p.eq(pay,e.add(p.CE(P,Q),charges,p.neg(refund)))
 return pay,charges,refund
def controller(a,g,h,Q,j,d,policy):
 v=mux(a,g,h);P=p.spectrum(v);vv,qq,rho=p.physical(v,Q,j)
 aa=[p.child(a,j,z) for z in (0,1)];dh=p.sub(e.entropy(P),p.avg(*(e.entropy(p.spectrum(x)) for x in vv)))
 ref=p.sub(p.CE(P,Q),e.add(dh,p.avg(*(p.CE(p.spectrum(vv[z]),qq[z]) for z in (0,1)))))
 p.nn(ref,'actual CURRENT controller rho')
 cs=[subtree(aa[z],g,h,qq[z],d,policy) for z in (0,1)]
 pay=e.add(dh,p.avg(cs[0][0],cs[1][0]));charge=p.avg(cs[0][1],cs[1][1]);refund=e.add(ref,p.avg(cs[0][2],cs[1][2]))
 p.eq(pay,e.add(p.CE(P,Q),charge,p.neg(refund)))
 return pay,charge,refund,rho
def main():
 endpoint=e.add(e.scale(e.lg(F(16807,15606)),F(9,64)),e.scale(e.lg(F(384,383)),F(3,8)))
 p.ck(16807**144*384**384 < 2**17*15606**144*383**384)
 p.nn(p.sub(p.const(F(17,1024)),endpoint));p.ck(F(45,2576)-F(17,1024)==F(143,164864))
 histories=[]
 for m in ([1] if MODE=='pilot' else [1,2]):
  root,kids=p.instance(m);v,Q,W,Z=kids[1];g=tuple(v[8*t+3] for t in range(len(v)//8));h=tuple(v[8*t] for t in range(len(v)//8));q0,q1=p.split(Q);d=m+2
  for theta in p.TH:
   qt=p.make(q0,q1,p.prof(theta))
   for j in (0,1):
    vv,qq,rho=p.physical(v,qt,j)
    for z in (0,1):
     a=p.child(p.AA,j,z);pi,V=profile(a);x,y,b=extract(qq[z],4)
     if z==0:p.ck(b==pi,'dictator carried point')
     else:p.nn(p.KL(pi,b),'point child inherited mismatch')
     qnew=make(x,y,mix(pi,PH[-1]));before=prefixes;walk(a,g,h,qnew,mix(pi,PH[-1]),d)
     rows.append({'m':m,'theta':str(theta),'controller':j,'outcome':z,'prefixes':prefixes-before,'rho':list(map(str,rho))})
  for policy in (range(1) if MODE=='pilot' else range(3)):
   # First paid theta1/8; one actual DATA query; next3/16; controller; repeated post-DATA resets.
   qt=p.make(q0,q1,p.prof(F(1,8)));cfirst=p.sub(p.CE(p.spectrum(v),qt),p.CE(p.spectrum(v),Q))
   gd,hd,qd,_=structural(p.AA,g,h,qt,3);vd=[mux(p.AA,gd[z],hd[z]) for z in (0,1)]
   dh=p.sub(e.entropy(p.spectrum(v)),p.avg(*(e.entropy(p.spectrum(x)) for x in vd)))
   paychildren=[];allcharges=[]
   for z in (0,1):
    x,y=split(qd[z],8);qn=make(x,y,p.prof(F(3,16)));c=p.sub(p.CE(p.spectrum(vd[z]),qn),p.CE(p.spectrum(vd[z]),qd[z]))
    pay,cc,refund,rho=controller(p.AA,gd[z],hd[z],qn,policy%2,d-1,policy)
    paychildren.append(pay);allcharges.append(e.add(c,cc))
   pay=e.add(dh,p.avg(*paychildren));charges=e.add(cfirst,p.avg(*allcharges))
   p.nn(p.sub(endpoint,charges));p.nn(p.sub(e.add(p.CE(p.spectrum(v),Q),endpoint),pay))
   olddh=p.sub(e.entropy(p.spectrum(root[0])),p.avg(*(e.entropy(p.spectrum(x[0])) for x in kids)))
   total=e.add(olddh,p.avg(p.CE(p.spectrum(kids[0][0]),kids[0][1]),pay));reserve=p.sub(p.const(4*(m+F(29,16))-F(1,8)),total)
   lower=3*m-F(15,8)+F(143,329728);p.nn(p.sub(reserve,p.const(lower)))
   histories.append({'m':m,'policy':policy,'original_quota_unused':p.bounds(reserve),'proved_lower':str(lower),'all_signed_resets':p.bounds(charges)})
 p.ck(bool(fair_guard),'fair completion negative guard found')
 out={'status':'PASS','mode':MODE,'assertions':p.count,'controller_children':len(rows),'post_DATA_prefixes':prefixes,'seconds':time.monotonic()-START,'endpoint_interval':p.bounds(endpoint),'rows':rows,'histories':histories,'fair_completion_counterexample':fair_guard}
 (R/'out'/('PILOT.json' if MODE=='pilot' else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','histories','fair_completion_counterexample')}))
if __name__=='__main__':main()
