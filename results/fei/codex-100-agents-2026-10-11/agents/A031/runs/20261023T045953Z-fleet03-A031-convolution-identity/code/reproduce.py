from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];count=0;cache={};start=time.monotonic()
def ck(x):
 global count
 assert x
 count+=1
def lg(x):
 if x in cache:return cache[x]
 k=x.numerator.bit_length()-x.denominator.bit_length();z=x/F(2)**k
 if z<1:z*=2;k-=1
 def series(z):
  t=(z-1)/(z+1);u=t;s=F(0)
  for j in range(24):s+=u/(2*j+1);u*=t*t
  return 2*s,2*s+2*u/(49*(1-t*t))
 a,b=series(z);c,d=series(F(2));cache[x]=(k+a/d,k+b/c);return cache[x]
def logs(terms):
 lo=hi=F(0)
 for w,x in terms:
  if not w:continue
  a,b=lg(x)
  if w<0:a,b=b,a
  lo+=w*a;hi+=w*b
 return lo,hi
def add(*xs):return tuple(sum(x[j] for x in xs) for j in [0,1])
def scale(x,c):return tuple(c*z for z in (x if c>=0 else x[::-1]))
def sub(x,y):return add(x,scale(y,-1))
def av(xs):return scale(add(*xs),F(1,len(xs)))
def zero(x):ck(x[0]<=0<=x[1])
def overlap(x,y):ck(max(x[0],F(y[0]))<=min(x[1],F(y[1])))
def marg(p,mask):
 out={}
 for s,v in p.items():out[s&~mask]=out.get(s&~mask,F(0))+v
 return out
def fair(p,i):return {s|b:v/2 for s,v in marg(p,1<<i).items() for b in [0,1<<i]}
def ce(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 return logs([(-v,q[s]) for s,v in p.items() if v])
def H(p):return logs([(-v,v) for v in p.values() if v])
def B(p,i):
 q=marg(p,1<<i);return logs([(v,q[s&~(1<<i)]/v) for s,v in p.items() if v])
def Mrow(p,i):
 q=marg(p,1<<i);return logs([(v,q[s&~(1<<i)]/v) for s,v in p.items() if v and s>>i&1])
def cmi(p,i,j):
 a=marg(p,1<<i);b=marg(p,1<<j);q=marg(p,(1<<i)|(1<<j))
 return logs([(v,v*q[s&~((1<<i)|(1<<j))]/(a[s&~(1<<i)]*b[s&~(1<<j)])) for s,v in p.items() if v])
def normalize_h(h):return tuple(sorted(h))
@lru_cache(None)
def spectrum(L,h):
 hd=dict(h);n=2*L+4;free=[i for i in range(n) if i not in hd]
 es=[13,(((1<<L)-1)<<4)|3,(((1<<L)-1)<<(L+4))|6];vals=[]
 for v in range(1<<len(free)):
  word=sum(b<<i for i,b in h)|sum(((v>>j)&1)<<i for j,i in enumerate(free))
  vals.append(1 if all(word&e for e in es) else -1)
 step=1
 while step<len(vals):
  for s in range(0,len(vals),2*step):
   for j in range(s,s+step):u,v=vals[j],vals[j+step];vals[j],vals[j+step]=u+v,u-v
  step*=2
 ar={sum(((s>>j)&1)<<i for j,i in enumerate(free)):F(v,len(vals)) for s,v in enumerate(vals)}
 p={s:v*v for s,v in ar.items()};ck(sum(p.values())==1);return ar,p
def child(L,h,i,u):return spectrum(L,normalize_h(h+((i,u),)))
def marker(L,h):
 a,p=spectrum(L,h);old=ce(p,fair(p,0));ps=[child(L,h,0,u)[1] for u in [0,1]]
 fresh=av([ce(v,fair(v,2)) for v in ps]);incoming=marg(p,1);inherited=av([ce(v,incoming) for v in ps]);ba=B(p,0)
 net=sub(add(ba,fresh),old);rho=sub((F(1),F(1)),ba);delta=sub(fresh,inherited)
 zero(sub(net,sub(delta,rho)))
 ja=sub(H(marg(p,1)),av([H(v) for v in ps]));zero(sub(net,sub(sub(ba,ja),av([B(v,2) for v in ps]))))
 if dict(h).get(3)==dict(h).get(1)==1:
  ck(ba==(F(0),F(0)));ck(fresh==(F(1),F(1)))
 return add(ba,fresh),net
@lru_cache(None)
def envelope(L,h):
 ck(time.monotonic()-start<55)
 a,p=spectrum(L,h);stop,_=marker(L,h);choices=[stop]
 for i in range(4,2*L+4):
  if i in dict(h):continue
  ps=[child(L,h,i,u)[1] for u in [0,1]]
  old=ce(p,fair(p,0));fresh=av([ce(v,fair(v,0)) for v in ps]);net=sub(add(B(p,i),fresh),old)
  jminus=sub(H(marg(p,(1<<i)|1)),av([H(marg(v,1)) for v in ps]))
  zero(add(net,cmi(p,i,0),jminus))
  # Verify exact signed collapse independently on ALL retained labels.
  for u in [0,1]:
   ac,pc=child(L,h,i,u)
   for S,v in ac.items():ck(v==a[S]+(-1)**u*a[S|(1<<i)])
  children=[envelope(L,normalize_h(h+((i,u),))) for u in [0,1]]
  choices.append(add(B(p,i),av(children)))
 return tuple(max(x[j] for x in choices) for j in [0,1])
main=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));rows=[]
peerroot=Path('agents/A035/runs/20261023T041335Z-fleet03-A035-signed-cancellation-countersearch')
peer=json.loads((peerroot/'out/CHECK.json').read_text(encoding='utf-8'))
for L in [1,2]:
 ar,p=spectrum(L,());I=sum(v for S,v in p.items() for i in [3]+list(range(4,2*L+4)) if S>>i&1)
 M=add(*(Mrow(p,i) for i in range(2*L+4)));bb=[];old=[];env=[];canonical=[];private=[];front=[]
 for s in [0,1]:
  ps=child(L,(),3,s)[1];bb.append(B(ps,1))
  for b in [0,1]:
   h=normalize_h(((3,s),(1,b)));parent=spectrum(L,h)[1];old.append(ce(parent,fair(parent,0)));env.append(envelope(L,h));private.append(B(parent,4));zb=[]
   for y in [0,1]:
    hy=normalize_h(h+((4,y),));py=spectrum(L,hy)[1];zb.append(B(py,L+4))
    for z in [0,1]:
     hz=normalize_h(hy+((L+4,z),));canonical.append(marker(L,hz)[0]);pz=spectrum(L,hz)[1];front.append(ce(pz,fair(pz,0)))
   private.append(av(zb))
 D=add(M,B(p,3),av(bb));bill2=add(D,av(old));bill5=add(D,scale(add(*private),F(1,4)),av(canonical));allbill=add(D,av(env))
 ck(sub((17*I,17*I),bill2)[0]>F(7,8));ck(sub((17*I,17*I),allbill)[0]>F(1,8))
 row=next(z for z in main['cases'] if z['L']==L);overlap(bill2,row['second_reset_bill']);overlap(bill5,row['marker_exposure_bill'])
 fourth=add(D,scale(add(*private),F(1,4)),av(front));peerrow=next(z for z in peer['cases'] if z['L']==L);overlap(fourth,peerrow['fourth_bill'])
 rows.append({'L':L,'all_adaptive_policies_enclosed':True,'all_policy_original_spare_lower':str(17*I-allbill[1]),'canonical_bill':[str(v) for v in bill5]})
h=normalize_h(((3,1),(1,0),(4,1)));p=spectrum(2,h)[1];Q=fair(p,2);pc=[child(2,h,6,u)[1] for u in [0,1]];new=av([ce(v,fair(v,0)) for v in pc]);inc=av([ce(v,marg(Q,64)) for v in pc]);rho=cmi(p,6,2);delta=sub(new,inc);net=sub(add(B(p,6),new),ce(p,Q));zero(sub(net,sub(delta,rho)));ck(net[0]>F(1,10))
put=lambda x:[str(z) for z in x]
review={'claim_id':'A035-CLOSED-REFERENCE-CYCLE-ASYMMETRIC-RESET','version':1,'verdict':'HOLDS_AT_STATED_INHERITED_BANK_SCOPE_NO_REPAIR','endpoint_L':[1,2],'positive_witness':{'L':2,'x':1,'b':0,'y':1,'net':put(net),'Delta':put(delta),'rho':put(rho),'threshold':'net>1/10'},'scope':'Generic fixed-marker identity and endpoint telescoping analytically reconstructed; full fourth bills independently overlap at L1,2; positive local Boolean witness independently reconstructed; no new full-chain source admission review'}
(R/'out/REVIEW_A035.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
out={'checks':count,'seconds':time.monotonic()-start,'private_histories':envelope.cache_info().currsize,'records':rows,'method':'independent truth-table FWHT, rational logs, certified Bellman upper envelopes for all adaptive policies'}
(R/'out/REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
