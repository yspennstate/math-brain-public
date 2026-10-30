import json,time,sys
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv
spec={'helper_version':'A019-zero-row-repair-v1','family':'actual private queries with two balanced Boolean children; exact/uniform supplied child references, independently chosen; same nonlinear mask reference and absent-query zero-row convention','domain':'pilot dimension2; full dimensions2,3, every balanced-child query and four ordered supplied-reference choices','case_count':32 if pilot else 464,'symmetry':'none','arithmetic':'exact prime-log identities and proved rational logarithm intervals','memory_estimate_MB':100,'maximum_runtime_seconds':60}
(R/'out'/('REPAIR_PILOT_SPEC.json' if pilot else 'REPAIR_SPEC.json')).write_text(json.dumps(spec,indent=2))
source=(R/'code/check_exposure.py').read_text();defs=source[source.index('def ck(x):'):source.index("transport={'positive'")]
ns={'Q':Q,'lru_cache':lru_cache,'checks':0};exec(defs,ns)
sp=ns['spectrum'];ce=ns['ce'];add=ns['add'];gate=ns['gate'];nn=ns['nonnegative'];ck=ns['ck'];start=time.monotonic();cases=0
for n in ([2] if pilot else [2,3]):
 N=1<<n
 for mask in range(1<<N):
  h=tuple(1-2*((mask>>v)&1) for v in range(N));ph=sp(h)
  for query in range(n):
   children=[tuple(h[(u&((1<<query)-1))|(((u>>query)<<1|b)<<query)] for u in range(N//2)) for b in (0,1)]
   if any(sum(t) for t in children):continue
   pcs=[sp(t) for t in children]
   for kinds in ((0,0),(0,1),(1,0),(1,1)):
    cases+=1;assert time.monotonic()-start<60
    qs=[pcs[b] if not kinds[b] else tuple(Q(1,N//2) for _ in range(N//2)) for b in (0,1)]
    qh=[Q(0)]*N
    for u in range(N//2):
     j=(u&((1<<query)-1))|((u>>query)<<(query+1));row=ph[j]+ph[j|(1<<query)];qrow=(qs[0][u]+qs[1][u])/2
     for b in (0,1):qh[j|(b<<query)]=qrow*(ph[j|(b<<query)]/row if row else int(b==0))
    root=gate(h,tuple(qh),1);ch=[gate(children[b],qs[b],1) for b in (0,1)]
    ck(qh[0]==(qs[0][0]+qs[1][0])/2)
    deltaD=add((Q(1,2),ch[0][1]),(Q(1,2),ch[1][1]),(-1,root[1]))
    ck(nn(add((-1,deltaD))))
    dh=add((1,ce(ph,ph)),(-Q(1,2),ce(pcs[0],pcs[0])),(-Q(1,2),ce(pcs[1],pcs[1])))
    dcf=add((1,root[0]),(-Q(1,2),ch[0][0]),(-Q(1,2),ch[1][0]))
    ck(nn(add((Q(1,2),dh),(-1,dcf))))
result={'status':'PASS','cases':cases,'checks':ns['checks'],'seconds':time.monotonic()-start,'conclusion':'two balanced children plus absent-query zero-row lift imply no positive net activation reference surcharge beyond one-half inherited core entropy decrement','full_fei':'OPEN'}
(R/'out'/('REPAIR_PILOT_CHECK.json' if pilot else 'REPAIR_CHECK.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result))
