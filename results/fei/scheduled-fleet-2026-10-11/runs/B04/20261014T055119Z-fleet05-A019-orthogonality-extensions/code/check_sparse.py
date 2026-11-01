import json,time,sys
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv
spec={'helper_version':'A019-sparse-refund-v1','family':'essential rare private query of h0=chi_u, h1=chi_u*(-1)^1_(v=0); both child core references one-half actual spectrum plus one-half empty point; parent actual query conditional lift; fixed nonlinear mask','domain':'pilot k1; full k=1..8, at most13 physical bits; additional analytic identities hold for every k>=1','case_count':1 if pilot else 8,'symmetry':'none','arithmetic':'actual Boolean spectra and exact Fraction prime-log CE identities; interval bounds for point-phase core certificates','memory_estimate_MB':100,'maximum_runtime_seconds':60}
(R/'out'/('SPARSE_PILOT_SPEC.json' if pilot else 'SPARSE_SPEC.json')).write_text(json.dumps(spec,indent=2))
source=(R/'code/check_exposure.py').read_text();defs=source[source.index('def ck(x):'):source.index("transport={'positive'")]
ns={'Q':Q,'lru_cache':lru_cache,'checks':0};exec(defs,ns)
fw=ns['fw'];sp=ns['spectrum'];ce=ns['ce'];add=ns['add'];gate=ns['gate'];nn=ns['nonnegative'];ck=ns['ck'];start=time.monotonic();out=[]
debt={2:Q(1,2),3:Q(1),17:-Q(1,2)} # one-half log2(18/17)
def I(p):return sum(Q(i.bit_count())*v for i,v in enumerate(p))
for k in ([1] if pilot else range(1,9)):
 assert time.monotonic()-start<60
 N=1<<(k+1);h0=tuple(1-2*(v&1) for v in range(N));h1=tuple(h0[v]*(-1 if v>>1==0 else 1) for v in range(N))
 children=[h0,h1];pcs=[sp(t) for t in children]
 qs=[tuple((p+int(i==0))/2 for i,p in enumerate(pc)) for pc in pcs]
 h=tuple(children[b][v] for v in range(N) for b in (0,1));ph=sp(h);qh=[]
 for u in range(N):
  row=ph[2*u]+ph[2*u+1];qrow=(qs[0][u]+qs[1][u])/2
  qh.extend((qrow*ph[2*u]/row,qrow*ph[2*u+1]/row) if row else (qrow/2,qrow/2))
 root=gate(h,tuple(qh),1);ch=[gate(children[b],qs[b],1) for b in (0,1)]
 ck(sum(h)==0);ck(all(sum(t)==0 for t in children));ck(all(abs(sum(t))<len(t) for t in children))
 ck(Q(sum(a!=b for a,b in zip(*children)),N)==Q(1,1<<k))
 ck(all(add((1,ch[b][2]),(-1,ce(pcs[b],pcs[b])))=={2:Q(1)} for b in (0,1)))
 ck(add((1,root[2]),(-1,ce(ph,ph)))=={2:Q(1)})
 ck(add((Q(1,2),ch[0][1]),(Q(1,2),ch[1][1]),(-1,root[1]))==debt)
 ck(add((1,root[0]),(-Q(1,2),ch[0][0]),(-Q(1,2),ch[1][0]),(-Q(1,2),root[2]),(Q(1,4),ch[0][2]),(Q(1,4),ch[1][2]))==debt)
 for cc,pp in [(root[2],ph)]+[(ch[b][2],pcs[b]) for b in (0,1)]:
  ck(nn(add((4*I(pp),{2:Q(1)}),(-1,cc))))
 out.append({'k':k,'core_query_disagreement':str(Q(1,1<<k)),'net_debt':'1/2 log2(18/17)','core_KL_refund':'0','both_children_nonconstant':True,'complete_core_rate4':True})
 (R/'out/SPARSE_PARTIAL.json').write_text(json.dumps(out,indent=2))
result={'status':'PASS','cases':len(out),'checks':ns['checks'],'seconds':time.monotonic()-start,'family':out,'all_dimension_bridge':'proved analytically in REPORT; constant net debt with disagreement2^-k and complete rate4 core certificates','full_fei':'OPEN'}
(R/'out'/('SPARSE_PILOT_CHECK.json' if pilot else 'SPARSE_CHECK.json')).write_text(json.dumps(result,indent=2));print(json.dumps({p:v for p,v in result.items() if p!='family'}))
