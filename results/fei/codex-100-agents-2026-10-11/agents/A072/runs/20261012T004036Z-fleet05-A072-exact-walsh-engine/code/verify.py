import hashlib,json,sys,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT))
from EXACT_WALSH_INTERFACE import VERSION,uniform_entropy_certificate,sign,add,BASE

def dump(name,x):
    (ROOT/name).write_text(json.dumps(x,indent=2,default=str)+'\n',encoding='utf-8')

def table(n,mask):return tuple(1-2*((mask>>x)&1) for x in range(1<<n))

def run(pilot):
    start=time.perf_counter()
    if pilot:
        results=[{'mask':m,**uniform_entropy_certificate(table(2,m))} for m in range(16)]
        dump('out/pilot_records.json',results)
        summary={'mode':'pilot','functions':16,'coordinates':32,'failures':0,'runtime_seconds':time.perf_counter()-start}
        assert summary['runtime_seconds']<55
        dump('out/pilot.json',summary);print(json.dumps(summary));return
    Kstar={2:F(4),5:F(5,2),3:F(-9,2)};results=[]
    for n,mask,cutoff in [(5,4194372,F(539,200)),(6,1103806792023,F(368,125))]:
        c=uniform_entropy_certificate(table(n,mask))
        ratios=[r['B_over_influence_prime_log'] for r in c['coordinates']]
        assert all(x is not None for x in ratios)
        m=0
        for j in range(1,n):
            if sign(add((1,ratios[j]),(-1,ratios[m])))['sign']<0:m=j
        comparisons=[sign(add((1,r),(-1,ratios[m]))) for r in ratios]
        assert all(s['sign']>=0 for s in comparisons)
        minimum_coordinates=[j for j,s in enumerate(comparisons) if s['sign']==0]
        strict_cutoff=sign(add((1,ratios[m]),(-cutoff,{2:F(1)})))
        strict_Kstar=sign(add((1,ratios[m]),(-1,Kstar)))
        assert strict_cutoff['sign']==strict_Kstar['sign']==1
        result={'n':n,'negative_bit_mask':mask,'negative_assignments':[x for x in range(1<<n) if mask>>x&1],
                'minimum_coordinates':minimum_coordinates,'minimum_prime_log':ratios[m],
                'minimum_comparisons':comparisons,'rational_lower_cutoff':cutoff,
                'strict_cutoff_certificate':strict_cutoff,'strict_Kstar_certificate':strict_Kstar,
                'certificate':c}
        dump(f'out/witness_n{n}.json',result);results.append(result)
        if time.perf_counter()-start>55:raise RuntimeError('Frozen runtime cap')
    growth=sign(add((1,results[1]['minimum_prime_log']),(-1,results[0]['minimum_prime_log'])))
    assert growth['sign']==1
    dump('out/comparison.json',growth)
    summary={'engine_version':VERSION,'functions':2,'coordinates':11,
             'physical_children':22,'failures':0,'exact_minima_certified':2,
             'entropy_decrement_identities_checked':11,'integer_bit_cap':8000000,
             'minimum_coordinates':[r['minimum_coordinates'] for r in results],
             'minimum_prime_log':[r['minimum_prime_log'] for r in results],
             'runtime_seconds':time.perf_counter()-start,
             'baseline_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest()}
    dump('ENGINE_CERTIFICATE.json',summary);print(json.dumps(summary,default=str))

if __name__=='__main__':run('--pilot' in sys.argv)
