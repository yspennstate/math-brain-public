import ast, hashlib, itertools, json, math, sys, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from EXACT_WALSH_INTERFACE import uniform_certificate,biased_certificate,restrict,VERSION
A071=Path(r'~\brain_workers\FEI100_20261011\agents\A071\runs\20261011T214639Z-fleet05-A071-search-space-design')

def dump(path,data):
    path.write_text(json.dumps(data,indent=2,default=str),encoding='utf-8')

def load_spectrum():
    # Only the old spectrum function; do not run the original search/logarithms.
    src=(A071/'code/search.py').read_text(encoding='utf-8')
    node=next(t for t in ast.parse(src).body if isinstance(t,ast.FunctionDef) and t.name=='spectrum')
    env={'math':math,'F':F}
    exec(compile(ast.Module(body=[node],type_ignores=[]),'A071-spectrum','exec'),env)
    return env['spectrum'],hashlib.sha256(src.encode()).hexdigest()

@lru_cache(None)
def cert(table,p):
    c=biased_certificate(table,p)
    if all((q*8).denominator==1 for q in p):
        assert tuple(c['spectrum'])==legacy(table,tuple(int(q*8) for q in p))
    return c

legacy,legacy_sha=load_spectrum()

def run(pilot=False):
    start=time.perf_counter(); limit=55 if pilot else 120
    uniform=[]
    for n in range(4):
        for code in range(1<<(1<<n)):
            table=tuple(1-2*((code>>x)&1) for x in range(1<<n))
            c=uniform_certificate(table)
            uniform.append({'code':code,**c})
    dump(ROOT/'out'/('pilot_uniform.json' if pilot else 'uniform.json'),uniform)
    biases=[(4,4,4)] if pilot else list(itertools.product((1,2,4),repeat=3))
    cases=parents=children=mixture_entries=0
    path=ROOT/'out'/('pilot_grid.jsonl' if pilot else 'grid.jsonl')
    with path.open('w',encoding='utf-8') as out:
        for ms in biases:
            p=tuple(F(m,8) for m in ms)
            for code in range(128):
                table=tuple(1 if x==0 or not code>>(x-1)&1 else -1 for x in range(8))
                parent=cert(table,p); parents+=1
                for mask in range(1,7):
                    A=[i for i in range(3) if mask>>i&1]
                    B=[i for i in range(3) if not mask>>i&1]
                    q=[sum((parent['spectrum'][s] for s in range(8)
                        if sum(((s>>i)&1)<<j for j,i in enumerate(B))==t),F(0))
                        for t in range(1<<len(B))]
                    mixture=[F(0)]*len(q); average_I=[F(0)]*len(B)
                    for z in range(1<<len(A)):
                        ct,cp=restrict(table,p,mask,z); ch=cert(ct,cp); children+=1
                        w=math.prod(p[i] if z>>j&1 else 1-p[i] for j,i in enumerate(A))
                        for t in range(len(q)): mixture[t]+=w*ch['spectrum'][t]
                        for j in range(len(B)): average_I[j]+=w*ch['spectral_influences'][j]
                    assert mixture==q
                    assert average_I==[parent['spectral_influences'][i] for i in B]
                    cases+=1; mixture_entries+=len(q)
                out.write(json.dumps({'code':code,'bias_numerators_over_8':ms,**parent},default=str)+'\n')
                if time.perf_counter()-start>limit: raise RuntimeError('Frozen runtime cap')
    # Persist named controls, including the minimum-positive A071 witness.
    witnesses=[]
    for name,table,ms,mask in [
        ('AND-calibration',tuple(-1 if x&3==3 else 1 for x in range(8)),(1,2,4),1),
        ('A071-minimum-positive',tuple(-1 if x==3 else 1 for x in range(8)),(1,1,4),4)]:
        c=cert(table,tuple(F(m,8) for m in ms))
        records=[]
        for z in range(1<<mask.bit_count()):
            ct,cp=restrict(table,c['biases'],mask,z)
            records.append({'z':z,'table':ct,**cert(ct,cp)})
        witnesses.append({'name':name,'table':table,'block_mask':mask,'children':records,**c})
    dump(ROOT/'out'/('pilot_witnesses.json' if pilot else 'witnesses.json'),witnesses)
    result={'engine_version':VERSION,'mode':'pilot' if pilot else 'full',
        'uniform_tables_n_0_through_3':len(uniform),'biased_parent_cases':parents,
        'physical_block_cases':cases,'physical_child_occurrences':children,
        'mixture_entries':mixture_entries,'distinct_biased_tables_checked':cert.cache_info().currsize,
        'A071_exact_spectrum_matches':cert.cache_info().currsize,
        'failures':0,'entropy_comparisons':0,'runtime_seconds':time.perf_counter()-start,
        'legacy_spectrum_source_sha256':legacy_sha,'independent_entropy_review':'NOT_PERFORMED'}
    dump(ROOT/('ENGINE_CERTIFICATE.json' if not pilot else 'out/pilot.json'),result)
    print(json.dumps(result))

if __name__=='__main__': run('--pilot' in sys.argv)
