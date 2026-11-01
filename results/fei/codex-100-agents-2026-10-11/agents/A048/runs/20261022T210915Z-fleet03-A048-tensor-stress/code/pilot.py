import json, math, time
from pathlib import Path

base=Path(__file__).resolve().parents[1]
spec={'helper_version':'A048-canonical-gap-pilot-v1','family':'product of m disjoint width-r Boolean point-defect signs in F_h','domain':[[3,5],[2,4],[2,3],[3,4]],'case_count':4,'symmetry':'equal coordinate marginals grouped exactly, no seed exclusion','arithmetic':'binary64 discovery only; not a certificate','memory_estimate_MB':20,'maximum_runtime_seconds':60}
(base/'out'/'PILOT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
def ent(p): return -p*math.log2(p)-(1-p)*math.log2(1-p) if 0<p<1 else 0.
def run(m,r):
    delta=2.**(-r); t=(1-(1-2*delta)**m)/2; p0=(1-t)**2/4; v=1-p0
    ds=[.5,.5,t/2]+[delta/2]*(m*r); rs=[d/v for d in ds]
    def phi(c):
        prod=1.; value=0.
        for a in rs: value+=a*prod; prod*=1-c*a
        return value
    lo,hi=0.,1.
    for _ in range(60):
        c=(lo+hi)/2
        if phi(c)>1:lo=c
        else:hi=c
    c=(lo+hi)/2
    ce=ent(p0)+v*(math.log2(c)+sum(-a*math.log2(c*a)-(1-a)*math.log2(1-c*a) for a in rs))
    g=sum(ent(d) for d in ds)-2
    return {'m':m,'r':r,'c':c,'G':g,'CE':ce,'CE_minus_2':ce-2,'gain':2+g-ce}
start=time.monotonic(); rows=[run(*x) for x in spec['domain']]
result={'status':'DISCOVERY_ONLY','rows':rows,'runtime_seconds':time.monotonic()-start}
(base/'out'/'PILOT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
