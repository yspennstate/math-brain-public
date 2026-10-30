import json,sys,time
from fractions import Fraction as Q
from pathlib import Path
sys.dont_write_bytecode=True
import check as c
def interval(form):
    lo=hi=Q(0)
    for p,a in form.items():
        l,h=c.logint(p)
        lo+=a*(l if a>0 else h)/c.SCALE
        hi+=a*(h if a>0 else l)/c.SCALE
    return lo,hi
start=time.perf_counter();records=[]
seed=sum(1<<x for x in c.SEED_POINTS)
for kind,mask in [('seed',seed),('seed-complement',seed^((1<<64)-1)),('point',1),('point-complement',((1<<64)-1)^1)]:
    core=c.e.uniform_entropy_certificate(c.truth(mask));rows=core['coordinates']
    assert all(r['influence']==rows[0]['influence'] for r in rows)
    assert all(r['B_over_influence_prime_log']==rows[0]['B_over_influence_prime_log'] for r in rows)
    M=mask.bit_count();d=abs(core['walsh'][1])//2
    R,q=c.reserve(M,d);B=interval(rows[0]['B_prime_log']);I=rows[0]['influence']
    Ecore=(B[0]/I,B[1]/I);EF=(Ecore[0]+R[0]/(q*I),Ecore[1]+R[1]/(q*I))
    if kind=='seed':assert Q(323,100)<EF[0] and EF[1]<Q(324,100)
    if kind.startswith('point'):assert Ecore[0]>Q(9,4) and EF[1]<Q(9,4) and R[1]<0
    if kind=='seed-complement':assert EF[1]<Q(8,3)
    records.append({'kind':kind,'mask':str(mask),'minority_negative_count':M,'q':q,
        'core_influence':I,'composed_influence':q*I,'core_erasure_prime_log':rows[0]['B_prime_log'],
        'E_core_bounds':Ecore,'reserve_bounds':R,'E_composed_bounds':EF,
        'all36_coordinates_equal_by_physical_transitivity':True})
    c.dump('out/fixtures.json',records)
result={'fixtures':4,'failures':0,'seed_composition_E_strictly_above':'323/100',
        'both_point_orientations_fail_K':'9/4','runtime_seconds':time.perf_counter()-start}
assert result['runtime_seconds']<55
c.dump('out/fixture_summary.json',result)
print(json.dumps(result))
