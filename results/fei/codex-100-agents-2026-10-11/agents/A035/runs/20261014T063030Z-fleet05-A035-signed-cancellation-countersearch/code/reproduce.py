from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,time
import kernel as k
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();k.CAP=50
def chars(t):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
parent=[]
for x in range(128):
 y=x&3;xx=(x>>2)&15;z=(x>>6)&1;p=(y.bit_count()%2)^(y==1)
 parent.append(k.bent(y,2)*k.bent(xx,4)*(-1 if p and xx==0 and z else 1))
children=[k.restrict(parent,2,v) for v in (0,1)];spectra=[chars(t) for t in [parent]+children];pa,a0,a1=spectra
assert all(a0[s]==(pa[(s&3)|((s&~3)<<1)]+pa[((s&3)|((s&~3)<<1))^4])//2 for s in range(64))
assert all(a1[s]==(pa[(s&3)|((s&~3)<<1)]-pa[((s&3)|((s&~3)<<1))^4])//2 for s in range(64))
d=Q(1,64);d0=Q(1,32);assert all(a1[s]==0 for s in range(64) if s&32)
assert [a0[s] for s in (0,32,4,36)]==[14,2,-2,2]
mu={};r0={};r1={};rbar={};coarse=defaultdict(lambda:[Q(0),Q(0)]);full=(Q(0),Q(0))
bc=chars([k.bent(y,2) for y in range(4)]);cm=chars([k.bent(y,2) if (y.bit_count()%2)^(y==1) else 0 for y in range(4)])
for s in range(32):
 u=Q(a0[s+32]**2,4096)/d0;rr=Q(a0[s]**2+a0[s+32]**2,4096)
 mu[s]=u;r0[s]=rr;r1[s]=Q(a1[s]**2+a1[s+32]**2,4096);rbar[s]=(rr+r1[s])/2
 l=Q(cm[s&3],bc[s&3]);eps=k.bent((s>>3)&3,2);lab=(str(l),eps)
 coarse[lab][0]+=u;coarse[lab][1]+=rr
 full=k.add(full,k.mul(k.ratlog(u/rr),u))
small=(Q(0),Q(0))
for u,r in coarse.values():small=k.add(small,k.mul(k.ratlog(u/r),u))
loss=k.sub(full,small);assert loss[0]>0
assert sum(mu.values())==sum(r0.values())==sum(r1.values())==sum(rbar.values())==1
assert mu[0]/r0[0]==Q(16,25) and mu[4]/r0[4]==16
assert rbar[0]==Q(25,1024) and r0[0]==Q(25,512)
assert rbar[4]==Q(33,1024) and r0[4]==Q(1,512)
def oriented(a,N,i):
 result=(Q(0),Q(0))
 for s in range(N):
  if s&(1<<i):continue
  b=a[s^(1<<i)]**2;rr=a[s]**2+b
  if b:result=k.add(result,k.mul(k.ratlog(Q(rr,b)),Q(b,N*N)))
 return result
prices=[oriented(pa,128,6),oriented(a0,64,5),oriented(a1,64,5)]
reset=(Q(0),Q(0));Db=(Q(0),Q(0))
for s,u in mu.items():
 reset=k.add(reset,k.mul(k.ratlog(rbar[s]/r0[s]),u));Db=k.add(Db,k.mul(k.ratlog(u/rbar[s]),u))
Dp=k.sub(k.ratlog(1/d),k.mul(prices[0],1/d));lost=k.sub(Dp,Db);physical=k.add((Q(1),Q(1)),reset)
drift=k.sub(k.mul(prices[1],Q(1,2)),prices[0]);pred=k.mul(k.sub(lost,physical),d)
assert pred[0]<=drift[1] and pred[1]>=drift[0]
out=dict(helper_version='A035-private-direct-v1',runtime_seconds=time.perf_counter()-start,truth_tables=3,all_direct_characters=256,active_child_signed_Walsh=[14,2,-2,2],old_trace_shared_fiber=dict(core_ratio='1/2',queried_bent_sign='+1',different_private_mate_sectors=[0,1],likelihoods=['16/25','16']),old_trace_lost_KL=k.emit(loss),incoming_reference_example={'mate_sector0':{'rbar':'25/1024','r_actual':'25/512'},'mate_sector1':{'rbar':'33/1024','r_actual':'1/512'}},active_child_d='1/32',inactive_child_d='0',physical_reference_only_branch_mass='1/2',parent_Lambda=k.emit(prices[0]),child_Lambda=[k.emit(p) for p in prices[1:]],parent_collapse_KL=k.emit(lost),physical_child_KL=k.emit(physical),signed_reset=k.emit(reset),Lambda_drift=k.emit(drift),status='PASS')
(ROOT/'out'/'reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
