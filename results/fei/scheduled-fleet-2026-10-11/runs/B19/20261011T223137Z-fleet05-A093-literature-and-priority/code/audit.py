from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
CTX = Path(r'~\brain_workers\FEI100_20261011\context')
REPORTS = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPP = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Frozen before any finite validation; this is a fixed census, not a numerical search.
save('out/FROZEN_SPEC.json',{
    'helper_version':'A093 rational-product-Fourier v1',
    'actual_Boolean_family':'All sixteen sign truth tables on two physical bits',
    'parameter_domain':'Each input probability in {1/8,1/2,7/8}',
    'case_count':432,'symmetry':'none',
    'arithmetic':'fractions.Fraction only; no logarithmic sign claim',
    'memory_estimate_MB':20,'maximum_runtime_seconds':60,
    'purpose':'Independently verify biased Parseval and physical-child marginal identity for all three nonempty blocks'})

t0=time.perf_counter()
inputs=[REPORTS/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
inputs += [SUPP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
inputs += list((SUPP/'sources').glob('*'))
inputs += list((REPORTS/'runs').rglob('*'))
inputs += list(CTX.glob('*.txt'))+list(CTX.glob('*.pdf'))
inputs += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
inventory=[]
for p in inputs:
    if p.is_file():
        data=p.read_bytes()
        inventory.append({'path':str(p),'bytes':len(data),'sha256':sha(data)})
        if p.suffix=='.json': json.loads(data.decode('utf-8-sig'))
save('out/SOURCE_INVENTORY.json',inventory)

def law(f,p):
    n=len(p); masses={}
    for sm in range(1<<n):
        moment=Q(0); norm=Q(1)
        for i in range(n):
            if sm>>i&1: norm*=p[i]*(1-p[i])
        for x in product((0,1),repeat=n):
            w=Q(1); v=Q(1)
            for i in range(n):
                w*=p[i] if x[i] else 1-p[i]
                if sm>>i&1: v*=x[i]-p[i]
            moment+=w*f[x]*v
        masses[sm]=moment*moment/norm
    return masses

checks=0; cases=0
for table in product((-1,1),repeat=4):
    f=dict(zip(product((0,1),repeat=2),table))
    for p in product((Q(1,8),Q(1,2),Q(7,8)),repeat=2):
        parent=law(f,p)
        assert sum(parent.values())==1; checks+=1
        for mask in (1,2,3):
            a=[i for i in range(2) if mask>>i&1]
            b=[i for i in range(2) if not mask>>i&1]
            marginal={s:Q(0) for s in range(1<<len(b))}
            mixture=marginal.copy()
            for s,val in parent.items():
                key=sum(((s>>i)&1)<<j for j,i in enumerate(b))
                marginal[key]+=val
            for z in product((0,1),repeat=len(a)):
                w=Q(1)
                for j,i in enumerate(a): w*=p[i] if z[j] else 1-p[i]
                child={}
                for y in product((0,1),repeat=len(b)):
                    x=[0,0]
                    for j,i in enumerate(a): x[i]=z[j]
                    for j,i in enumerate(b): x[i]=y[j]
                    child[y]=f[tuple(x)]
                cp=law(child,tuple(p[i] for i in b))
                assert sum(cp.values())==1; checks+=1
                for s,val in cp.items(): mixture[s]+=w*val
            assert marginal==mixture; checks+=1; cases+=1
andlaw=law({(0,0):1,(0,1):1,(1,0):1,(1,1):-1},(Q(1,8),Q(1,4)))
assert list(andlaw.values())==[Q(225,256),Q(7,256),Q(3,256),Q(21,256)]; checks+=1
save('out/VALIDATION.json',{'cases':cases,'exact_assertions':checks,'arithmetic':'Fraction','seconds':time.perf_counter()-t0,'verdict':'PASS','AND_masses':[str(v) for v in andlaw.values()],'does_not_certify':'No entropy inequality is inferred from finite rational checks; all-dimensional bound is reconstructed analytically in REPORT.md.'})
print(json.dumps({'cases':cases,'exact_assertions':checks,'verdict':'PASS'}))
