from exact import *
import exact as E
spec={'helper':'A028-data-release-drift-v1','family':'all controllers dimensions0..2 and ordered Boolean branch pairs sharing one or two data bits',
'domain':'data dimension1 and2; every physical first data coordinate; no automatic escalation',
'case_count':11616,'symmetry':'none','arithmetic':'integer/Fraction/prime-log/rational atanh24',
'memory_estimate_MB':100,'maximum_runtime_seconds':55,'claim_tested':'Delta H_F - weighted Delta H_G,H <=2p(1-p)Inf_i(GH); terminate on first exact counterexample'}
(ROOT/'out'/'DRIFT_PROBE_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
def sl(t,j,v):return tuple(t[x] for x in range(len(t)) if ((x>>j)&1)==v)
cases=0;witness=None
for na,code,a in tables(2):
 p=F(a.count(-1),len(a))
 for nd in [1,2]:
  core=[t for n,c,t in tables(nd) if n==nd]
  for g in core:
   for h in core:
    f=tuple(h[x] if val==-1 else g[x] for val in a for x in range(1<<nd))
    for j in range(nd):
     df=add(stats(f)[2],scale(add(stats(sl(f,j,0))[2],stats(sl(f,j,1))[2]),F(-1,2)))
     dg=add(stats(g)[2],scale(add(stats(sl(g,j,0))[2],stats(sl(g,j,1))[2]),F(-1,2)))
     dh=add(stats(h)[2],scale(add(stats(sl(h,j,0))[2],stats(sl(h,j,1))[2]),F(-1,2)))
     prod=tuple(x*y for x,y in zip(g,h));release=2*p*(1-p)*edges(prod,[j])
     excess=add(df,scale(dg,-(1-p)),scale(dh,-p),{2:-release})
     cases+=1
     if excess and enclosure(excess)[0]>0:
      witness={'controller':list(a),'G':list(g),'H':list(h),'data_coordinate':j,'p':str(p),
       'release':str(release),'excess_prime_log':{str(q):str(v) for q,v in excess.items()},
       'excess_interval':[str(x) for x in enclosure(excess)],'cases_before_witness':cases}
      break
     if time.monotonic()-START>55:raise RuntimeError('frozen cutoff')
    if witness:break
   if witness:break
  if witness:break
 if witness:break
out={'status':'REFUTED' if witness else 'NO_COUNTEREXAMPLE_IN_FROZEN_DOMAIN','cases_executed':cases,'witness':witness,
 'compute_seconds':time.monotonic()-START,'arithmetic':spec['arithmetic'],
 'scope':'Only release-alone DATA residual claim tested; arbitrary-controller whole-block theorem unchanged'}
(ROOT/'out'/'drift_probe.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
