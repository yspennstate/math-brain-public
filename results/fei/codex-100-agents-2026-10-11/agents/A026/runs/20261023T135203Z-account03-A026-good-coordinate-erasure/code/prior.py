from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,time,json
import exact_helper as e
R=Path(__file__).resolve().parents[1];MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full');START=time.monotonic();count=nodes=edges=transactions=0
TH=(F(0),F(1,8),F(3,16));AA=tuple(-1 if u<3 else 1 for u in range(8))
PI=tuple(p/(1-e.stats(AA)[0][0]) for p in e.stats(AA)[0][1:])
def ck(v,msg=''):
 global count
 assert v,(count,msg);count+=1
 if time.monotonic()-START>(55 if MODE=='pilot' else 240):raise TimeoutError('frozen cap')
def neg(v):return e.scale(v,-1)
def sub(a,b):return e.add(a,neg(b))
def avg(a,b):return e.scale(e.add(a,b),F(1,2))
def const(x):return {2:F(x)} if x else {}
def eq(a,b,msg=''):ck(not sub(a,b),msg)
def nn(a,msg=''):ck(e.enclosure(a)[0]>=0,(msg,e.enclosure(a)))
def enc(a):return {str(p):str(c) for p,c in a.items()}
def bounds(a):return list(map(str,e.enclosure(a)))
def CE(P,Q):return e.add(*(e.scale(e.lg(q),-p) for p,q in zip(P,Q) if p))
def KL(P,Q):return sub(CE(P,Q),e.entropy(P))
@lru_cache(None)
def spectrum(v):
 n=len(v);return tuple(F(x*x,n*n) for x in e.walsh(v))
def ins(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
@lru_cache(None)
def child(v,j,b):return tuple(v[ins(x,j,b)] for x in range(len(v)//2))
def marginal(Q,j):return tuple(Q[ins(x,j,0)]+Q[ins(x,j,1)] for x in range(len(Q)//2))
def physical(v,Q,j):
 P=spectrum(v);mp=marginal(P,j);mq=marginal(Q,j)
 vv=tuple(child(v,j,b) for b in (0,1));pp=tuple(spectrum(x) for x in vv)
 ck(all(2*x==y+z for x,y,z in zip(mp,*pp)))
 ks=tuple(tuple(p/(2*z) if z else F(1,2) for p,z in zip(ps,mp)) for ps in pp)
 joint=tuple(tuple(q*k for q,k in zip(mq,kb)) for kb in ks)
 rho=tuple(sum(x) for x in joint);ck(sum(rho)==1 and min(rho)>0)
 qs=tuple(tuple(x/rho[b] for x in joint[b]) for b in (0,1))
 return vv,qs,rho
def prof(theta):return tuple((1-theta)*p+theta/F(7) for p in PI)
DP={t:KL(PI,prof(t)) for t in TH+(F(1,4),)}
def make(q0,q1,b):return tuple(q0[t] if u==0 else q1[t]*b[u-1] for t in range(len(q0)) for u in range(8))
def split(Q):return tuple(Q[8*t] for t in range(len(Q)//8)),tuple(sum(Q[8*t+1:8*t+8]) for t in range(len(Q)//8))
def eta(P):return sum(p for i,p in enumerate(P) if i%8)
def source_profile(a,g,h,rg,rh):
 p=F(3,8);pg=spectrum(g);ph=spectrum(h)
 q=tuple((1-p)*x+p*y for x,y in zip(pg,ph));r=tuple((1-p)*x+p*y for x,y in zip(rg,rh))
 v=tuple((g if a[u]==1 else h)[x] for x in range(len(g)) for u in range(8));P=spectrum(v)
 ck(all(sum(P[8*t:8*t+8])==q[t] for t in range(len(q))))
 Q=tuple(r[t]*(P[8*t+u]/q[t] if q[t] else F(u==0)) for t in range(len(q)) for u in range(8))
 W=e.add(e.scale(KL(pg,rg),1-p),e.scale(KL(ph,rh),p));D=KL(q,r);Z=sub(W,D)
 eq(KL(P,Q),D,'prescribed conditional profile');nn(Z,'source-label slack')
 return v,Q,W,Z
def instance(m):
 g=tuple((-1 if (x&7)==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 h=tuple((-1 if (x&7).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(len(g)))
 rr=(F(1,len(g)),)*len(g);root=source_profile(AA,g,h,rr,rr)
 vg,rg,rhog=physical(g,rr,0);vh,rh,rhoh=physical(h,rr,0)
 kids=tuple(source_profile(AA,vg[b],vh[b],rg[b],rh[b]) for b in (0,1))
 M=1<<(m+2);beta=F(40*M,55*M-36);char=((1<<m)-1)<<2
 ck(rhog[1]==F(5*M-12,10*M) and rhoh[1]==F(1,2))
 ck(rg[1][char]==F(8,5*M-12) and rh[1][char]==F(1,M))
 for t,qt in enumerate(tuple(F(5,8)*x+F(3,8)*y for x,y in zip(spectrum(vg[1]),spectrum(vh[1])))):
  if not qt:continue
  true=F(5,8)*spectrum(vg[1])[t]/qt
  ref=F(5,8)*rg[1][t]/(F(5,8)*rg[1][t]+F(3,8)*rh[1][t])
  ck((true==F(20,23) and ref==beta and qt==F(23,32)) if t==char else true==ref)
 Zformula=e.scale(KL((F(20,23),F(3,23)),(beta,1-beta)),F(23,32))
 eq(kids[1][3],Zformula,'actual posterior slack')
 ck(eta(spectrum(kids[1][0]))==F(45,64));ck(len(set(vg[1]))==len(set(vh[1]))==2)
 ck(e.edges(root[0],range(m+6))==m+F(29,16))
 return root,kids
def walk(v,Q,d):
 global nodes,edges,transactions
 nodes+=1;P=spectrum(v);q0,q1=split(Q)
 ck(make(q0,q1,PI)==Q);ck(sum(Q)==1)
 for t in range(len(q0)):
  z=sum(P[8*t+1:8*t+8]);ck(all(P[8*t+u]==z*PI[u-1] for u in range(1,8)))
 qs={t:make(q0,q1,prof(t)) for t in TH}
 for t,q in qs.items():ck(sum(q)==1 and all(not p or z>0 for p,z in zip(P,q)))
 for t in TH:
  for s in TH:
   transactions+=1
   for i,p in enumerate(P):
    if p:ck(qs[s][i]/qs[t][i]==(prof(s)[i%8-1]/prof(t)[i%8-1] if i%8 else 1))
 if not d:return
 for k in range(d):
  j=3+k;vv,base,rho=physical(v,Q,j);ck(eta(P)==sum(eta(spectrum(x)) for x in vv)/2)
  for t in TH:
   _,cc,rr=physical(v,qs[t],j);ck(rr==rho)
   for b in (0,1):
    qx,qy=split(base[b]);ck(cc[b]==make(qx,qy,prof(t)))
  for b in (0,1):edges+=1;walk(vv[b],base[b],d-1)
def policy(v,Q,theta,d,depth,history,which):
 P=spectrum(v);targets=[F(1,8)] if depth==0 else ([F(3,16)] if which==0 else [F(0),F(3,16)] if which==2 else [F(3,16) if sum(history)%2 else F(1,8)])
 original=Q;reset={};rcount=0
 for t in targets:
  a,b=split(Q);qn=make(a,b,prof(t));C=sub(CE(P,qn),CE(P,Q));eq(C,e.scale(sub(DP[t],DP[theta]),eta(P)))
  reset=e.add(reset,C);theta=t;Q=qn;rcount+=1
 stop=not d or (which==1 and depth>=2 and sum(history)%2==0)
 if stop:
  return {'payment':CE(P,Q),'reset':reset,'potential':e.scale(DP[theta],eta(P)),'nodes':0,'resets':rcount,'leaves':1,'refund':{}}
 j=3+(d-1 if which==1 and sum(history)%2 else 0);vv,qq,_=physical(v,Q,j)
 hh=e.entropy(P);dh=sub(hh,avg(*(e.entropy(spectrum(x)) for x in vv)))
 refund=sub(CE(P,Q),e.add(dh,avg(*(CE(spectrum(x),q) for x,q in zip(vv,qq)))));nn(dh);nn(refund)
 cs=[policy(vv[b],qq[b],theta,d-1,depth+1,history+(b,),which) for b in (0,1)]
 pay=e.add(dh,avg(*(x['payment'] for x in cs)));resets=e.add(reset,avg(*(x['reset'] for x in cs)))
 pot=avg(*(x['potential'] for x in cs));ref=e.add(refund,avg(*(x['refund'] for x in cs)))
 eq(pay,e.add(CE(P,original),resets,neg(ref)),'complete current-reference history')
 return {'payment':pay,'reset':resets,'potential':pot,'nodes':1+sum(x['nodes'] for x in cs),'resets':rcount+sum(x['resets'] for x in cs),'leaves':sum(x['leaves'] for x in cs),'refund':ref}
def main():
 rows=[];hist=[]
 ck(sorted(PI)==[F(1,15)]*6+[F(3,5)])
 endpoint=e.scale(DP[F(3,16)],F(45,64));eq(endpoint,e.scale(e.lg(F(16807,15606)),F(9,64)))
 ck(16807**9<2*15606**9);nn(sub(const(F(1,64)),endpoint));ck(F(45,2576)-F(1,64)==F(19,10304))
 for m in ([1] if MODE=='pilot' else [1,2]):
  root,kids=instance(m);v,Q,W,Z=kids[1];nn(sub(Z,const(F(45,2576))))
  d=m+2;N=len(Q)//8
  refs={'inherited':Q}
  if MODE=='full':
   refs['flat-block']=make((F(1,2*N),)*N,(F(1,2*N),)*N,PI)
   refs['off-support-biased']=make(tuple(F(i+1,N*(N+1)) for i in range(N)),tuple(F(N-i,N*(N+1)) for i in range(N)),PI)
  for name,q in refs.items():
   before=(nodes,edges,transactions);walk(v,q,d)
   rows.append({'m':m,'reference':name,'prefixes':nodes-before[0],'edges':edges-before[1],'transactions':transactions-before[2]})
   (R/'out/CHECKPOINT.json').write_text(json.dumps({'status':'PARTIAL','completed_roots':len(rows),'rows':rows},indent=2)+'\n',encoding='utf-8',newline='\n')
  for w in (range(1) if MODE=='pilot' else range(3)):
   ans=policy(v,Q,F(0),d,0,(),w);eq(ans['reset'],ans['potential'],'signed potential telescope from original profile')
   nn(sub(endpoint,ans['reset']));nn(sub(e.add(CE(spectrum(v),Q),endpoint),ans['payment']))
   P0=spectrum(root[0]);dh=sub(e.entropy(P0),avg(*(e.entropy(spectrum(x[0])) for x in kids)))
   payment=e.add(dh,avg(CE(spectrum(kids[0][0]),kids[0][1]),ans['payment']))
   U=4*(m+F(29,16));reserve=sub(const(U-F(1,8)),payment);lower=3*m-F(15,8)+F(19,20608)
   nn(sub(reserve,const(lower)))
   hist.append({'m':m,'policy':w,'data_query_nodes':ans['nodes'],'resets':ans['resets'],'leaves':ans['leaves'],'signed_reset':enc(ans['reset']),'signed_reset_interval':bounds(ans['reset']),'full_payment':enc(payment),'unused_original_quota_interval':bounds(reserve),'proved_lower_bound':str(lower)})
  e.factors.cache_clear();e.cached_enclosure.cache_clear()
 out={'status':'PASS','mode':MODE,'roots':len(rows),'prefixes':nodes,'query_edges':edges,'profile_transactions':transactions,'assertions':count,'seconds':time.monotonic()-START,'rows':rows,'histories':hist,'integer_certificate':{'left':str(16807**9),'right':str(2*15606**9),'strict':True},'endpoint_cost_interval':bounds(endpoint)}
 (R/'out'/('PILOT.json' if MODE=='pilot' else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','histories','integer_certificate')}))
if __name__=='__main__':main()
