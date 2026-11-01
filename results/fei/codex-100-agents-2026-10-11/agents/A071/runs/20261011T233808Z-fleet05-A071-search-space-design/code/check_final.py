import json,itertools,hashlib,time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from sparse_search import exact_min,encode,ratios,vector,SCALE

ROOT=Path(__file__).resolve().parents[1]

def fwht(mask):
    a=[1-2*((mask>>x)&1) for x in range(32)]
    for h in (1,2,4,8,16):
        for first in range(0,32,2*h):
            for j in range(first,first+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
    return a

def orbit(mask):
    points=[x for x in range(32) if mask>>x&1];out=set()
    for perm in itertools.permutations(range(5)):
        image=[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in points]
        for t in range(32):out.add(sum(1<<(x^t) for x in image))
    return out

def describe(mask):
    w=fwht(mask);assert sum(x*x for x in w)==1024
    cs=[x//2 for x in w];r=ratios(cs,True)
    coords=[]
    for row in r:
        i=row['i'];edge=sum(((mask>>x)^(mask>>(x^(1<<i))))&1 for x in range(32) if not(x>>i&1))
        assert F(row['L'],256)==F(edge,16)
        coords.append({'i':i,'edge_count':edge,'influence':str(F(edge,16)),'ratio_interval_scaled':[str(F(row['lo'],row['L'])),str(F(row['hi'],row['L']))],'prime_log_ratio':{str(p):str(v) for p,v in vector(row['packets'],row['L'])}})
    # Inverse physical truth table checked separately from sparse moment formula.
    for x in range(32):
        inv=sum(w[s]*(1 if (s&x).bit_count()%2==0 else -1) for s in range(32))
        assert inv==32*(1-2*((mask>>x)&1))
    best=exact_min(cs);best.update({'negative_mask':mask,'A':[x for x in range(32) if mask>>x&1]})
    return {'mask':mask,'walsh':w,'coordinate_ratios':coords,'minimum':encode(best)},best

def run():
    start=time.perf_counter();sparse=json.loads((ROOT/'out/search.json').read_text());full=json.loads((ROOT/'out/full_census.json').read_text())
    assert full['complete'] and full['counts']['raw']==1<<31
    seed_record,seed=describe(sparse['global_best']['negative_mask'])
    certs=[];violations=[];equal=[]
    for mask in full['candidate_masks']:
        if time.perf_counter()-start>55:raise RuntimeError('Frozen 55-second cap')
        rec,b=describe(mask)
        if b['vector']==seed['vector']:equal.append(mask);rec['verdict']='EXACT_EQUAL_PRIME_LOG_FORM'
        elif b['hi']*seed['L']<seed['lo']*b['L']:rec['verdict']='STRICT_BELOW_SEED'
        elif b['lo']*seed['L']>seed['hi']*b['L']:violations.append(mask);rec['verdict']='STRICT_ABOVE_SEED'
        else:raise ArithmeticError('Nonidentical expressions have overlapping intervals')
        certs.append(rec)
        (ROOT/'out/candidate_certificates.json').write_text(json.dumps(certs,indent=2),encoding='utf-8')
    assert not violations,'Full E*(5) exceeds sparse seed; preserve witnesses, change target'
    # Every retained maximizing candidate lies in the seed's cube-isometry orbit.
    seedorbit=orbit(seed_record['mask']);assert all(mask in seedorbit for mask in equal)
    sparse_orbits={}
    for k,ties in sparse['ties_by_k'].items():
        if time.perf_counter()-start>55:raise RuntimeError('Frozen 55-second cap')
        seeds=[];uncovered={sum(1<<x for x in A) for A in ties}
        while uncovered:
            m=min(uncovered);o=orbit(m);covered=uncovered&o;seeds.append({'seed_mask':m,'full_translation_permutation_orbit_size':len(o),'anchored_ties_covered':len(covered)});uncovered-=covered
        sparse_orbits[k]=seeds
    counts=full['counts'];assert counts['strict_upper_passes']+counts['candidates']==counts['entropy_evaluated']
    result={'full_E5_certificate_complete':True,'seed':seed_record,'equality_candidate_masks':equal,'candidate_count':len(certs),'all_candidates_certified':True,'strict_above_seed':violations,'extremizer_negative_support_orbit_size':len(seedorbit),'extremizer_truth_tables_including_output_complement':2*len(seedorbit),'sparse_maximum_orbits':sparse_orbits,'runtime_seconds':time.perf_counter()-start,'universal_fei':'OPEN','next_obstruction':'Dimension six lead witness has min erasure ratio >368/125, so E5 is not a dimension-independent constant'}
    (ROOT/'out/final_certificate.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('seed','sparse_maximum_orbits')},indent=2))

if __name__=='__main__':run()
