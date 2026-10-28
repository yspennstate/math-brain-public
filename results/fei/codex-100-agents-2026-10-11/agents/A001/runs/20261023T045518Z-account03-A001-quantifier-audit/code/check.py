from helpers import *
import helpers

def CE(p,q):
 ck(len(p)==len(q) and sum(p)==sum(q)==1)
 ck(all(b>0 for a,b in zip(p,q) if a))
 return add(*[(-a,log(b)) for a,b in zip(p,q) if a])
def marginal(p,j):return tuple(p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2))
def query(v,Q,j):
 p=spectrum(v);ch=[transport(v,j,s) for s in (0,1)];pc=[spectrum(c) for c in ch];m=marginal(p,j);r=marginal(Q,j);B=erase(v,j)
 ck(tuple((a+b)/2 for a,b in zip(*pc))==m)
 rho=add((1,CE(p,Q)),(-1,entropy(p)),(-1,CE(m,r)),(1,entropy(m)))
 ck(not rho or interval(rho)[0]>=0)
 ck(add((1,B),*[(F(1,2),CE(t,r)) for t in pc])==add((1,CE(p,Q)),(-1,rho)))
 return ch,pc,r,B,rho
MAJ=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
def actual(k,r,ctrl=MAJ):
 return tuple(ctrl[x] if y==0 else (1 if y&((1<<k)-1)==0 else -1) for y in range(1<<r) for x in range(len(ctrl)))
def source(k,r,z,ctrl=MAJ,edited=True):
 s=F(1,1<<k);t=F(1,1<<r);mu=1-2*s;nc=len(ctrl);pg=spectrum(tuple(-1 if y&((1<<k)-1)==0 else 1 for y in range(1<<r)))
 V=tuple(mu*mu if T==0 else (1-mu*mu)/((1<<r)-1) for T in range(1<<r));R=tuple((1-z)*a+z*b for a,b in zip(pg,V));ck(sum(R)==1)
 if not edited:return tuple(R[T] if S==0 else F(0) for T in range(1<<r) for S in range(nc))
 psi=tuple(F(1-c,2) for c in ctrl);pp=sum(psi)/nc;e=2*pp*t;ck(0<=e<=s)
 ph=amplitudes(psi);gh=amplitudes(tuple(-1 if y&((1<<k)-1)==0 else 1 for y in range(1<<r)))
 p=tuple((gh[T]*(S==0)+2*t*ph[S])**2 for T in range(1<<r) for S in range(nc));ck(p==tuple(spectrum(actual(k,r,ctrl))))
 q=tuple(sum(p[T*nc:(T+1)*nc]) for T in range(1<<r));ck(q==tuple(a*a+2*e*a+2*e*t for a in gh))
 rp=tuple((1-e/s)*a+(e/s)*mu*(T==0)+2*e*t for T,a in enumerate(R));ck(sum(rp)==1 and min(rp)>0 and min(q)>=0)
 if z==0:ck(rp==q)
 Q=tuple((rp[T]*p[T*nc+S]/q[T] if q[T] else rp[T]*(S==0)) for T in range(1<<r) for S in range(nc));ck(sum(Q)==1)
 return Q

def rec(d):
 lo,hi=interval(d)
 return {'prime_log':enc(d),'interval':[str(lo),str(hi)],'millionth_enclosure':[(lo*10**6).__floor__(),(hi*10**6).__ceil__()]}
start=time.perf_counter();v=actual(3,6);p=spectrum(v)
ch,pc,m,B0,r0=query(v,p,6);on,off=ch;Qon=source(3,5,F(1));Qfar=source(3,5,F(1),edited=False)
rows=[];histories=[(a,d,h) for a in range(3) for d in (5,6) for h in range(3)]
# d indices are encoder-low after active removal, r4 dummy indices5,6.
if '--pilot' in sys.argv:histories=histories[:1]
for active,dummy,h in histories:
 ac,pa,ra,B1,r1=query(on,Qon,3+active);ck(tuple(ac[0])==actual(2,4));Qa=source(2,4,F(1))
 cc,pcs,rc,B2,r2=query(ac[0],Qa,dummy);ck(tuple(cc[0])==actual(2,3));Qc=source(2,3,F(1));Qsibling=source(2,3,F(1),edited=False)
 base=add((1,B0),(F(1,2),B1),(F(1,4),B2),(F(1,8),CE(pcs[0],Qc)),(F(1,8),CE(pcs[1],Qsibling)),(F(1,2),CE(pc[1],Qfar)))
 baseM=add((1,const(3)),(-1,base));ck(F(248210,10**6)<interval(baseM)[0]<interval(baseM)[1]<F(248211,10**6))
 daughters,pd,rd,B3,r3=query(cc[0],Qc,h)
 controls=[tuple(restrict(MAJ,h,s)) for s in (0,1)];ck([sum(F(1-c,2) for c in ctrl)/len(ctrl) for ctrl in controls]==[F(1,4),F(3,4)])
 for u,w in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(1),F(1))]:
  Q=[source(2,3,z,ctrl) for z,ctrl in zip((u,w),controls)]
  ck(all(tuple(spectrum(a))==tuple(spectrum(actual(2,3,c))) for a,c in zip(daughters,controls)))
  Z=[add((1,CE(t,q)),(-1,CE(t,rd))) for t,q in zip(pd,Q)]
  bill=add((1,base),(F(-1,8),r3),*[(F(1,16),z) for z in Z]);margin=add((1,const(3)),(-1,bill))
  direct=add((1,B0),(F(1,2),B1),(F(1,4),B2),(F(1,8),B3),*[(F(1,16),CE(t,q)) for t,q in zip(pd,Q)],(F(1,8),CE(pcs[1],Qsibling)),(F(1,2),CE(pc[1],Qfar)))
  ck(bill==direct);ck(interval(margin)[0]>0)
  changed=[any(a/(1-rd[0])!=b/(1-q[0]) for a,b in zip(rd[1:],q[1:])) for q in Q]
  rows.append({'active':active,'dummy_index':dummy,'encoder':h,'parameters':[str(u),str(w)],'margin':rec(margin),'weighted_KL_refund':rec(add((F(1,8),r3))),'weighted_signed_resets':[rec(add((F(1,16),z))) for z in Z],'nonempty_profile_changes':changed})
  ck(time.perf_counter()-start<55)
out={'status':'PASS','exact_assertions':helpers.count,'rows':rows,'base_margin':rec(baseM),'elapsed_seconds':time.perf_counter()-start}
(RUN/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8',newline='')
print(json.dumps({'status':out['status'],'exact_assertions':helpers.count,'rows':len(rows),'elapsed_seconds':out['elapsed_seconds'],'maximal_margin':rows[-1]['margin']['millionth_enclosure']}))
