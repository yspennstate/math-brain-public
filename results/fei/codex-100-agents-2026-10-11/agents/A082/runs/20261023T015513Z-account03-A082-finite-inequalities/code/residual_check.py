from pathlib import Path
import exact as E
from exact import F
import json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();cases=positive=0
u=(F(1,3),)*3;v=(F(1,6),F(1,3),F(1,2))
for code in range(16):
 f=tuple(-1 if code>>x&1 else 1 for x in range(4));P=E.spectrum(f);q=P[0]
 pc=tuple(x/(1-q) for x in P[1:]) if q<1 else u
 for profile in (u,v,pc):
  for oldvac in [F(k,4) for k in range(5)]:
   if (q and oldvac==0) or (q<1 and oldvac==1):continue
   Q=(oldvac,)+tuple((1-oldvac)*x for x in profile)
   for targetprofile in (u,v):
    fresh=(q,)+tuple((1-q)*x for x in targetprofile)
    binary={}
    if q:binary=E.add(binary,E.scale(E.logform(q/oldvac),q))
    if q<1:binary=E.add(binary,E.scale(E.logform((1-q)/(1-oldvac)),1-q))
    term=E.scale(E.sub(E.ce(pc,targetprofile),E.ce(pc,profile)),1-q) if q<1 else {}
    delta=E.sub(E.ce(P,fresh),E.ce(P,Q));rhs=E.add(E.scale(binary,-1),term)
    E.ck(not E.sub(delta,rhs));cases+=1
    if E.interval(delta)[0]>0:positive+=1
out=dict(status='PASS',cases=cases,positive_full_reset_costs=positive,assertions=E.ASSERTIONS,elapsed_seconds=time.perf_counter()-start,conclusion='Only changing the nonempty conditional profile can create new positive conversion after final vacuum calibration')
(ROOT/'out/RESIDUAL_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
