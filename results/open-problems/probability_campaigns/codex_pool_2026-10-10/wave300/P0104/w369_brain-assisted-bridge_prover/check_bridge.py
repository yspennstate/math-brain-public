"""Small exact checks and analytic-counterexample measurements; not a proof audit."""
from fractions import Fraction as Q
from pathlib import Path
import json
import math
import time

ROOT=Path(__file__).resolve().parent
started=time.monotonic()
checks=[]

def distribution(atoms):
    assert sum(w for x,w in atoms)==1 and all(w>0 for x,w in atoms)
    mean=sum(x*w for x,w in atoms)
    variance=sum(w*(x-mean)**2 for x,w in atoms)
    fourth=sum(w*(x-mean)**4 for x,w in atoms)
    return mean,variance,fourth

def intervals(atoms):
    points=sorted(set(x for x,w in atoms))
    return [(b-a,sum(w for x,w in atoms if a<=x<=b))
            for a in points for b in points if a<=b]

examples=[[(Q(-1),Q(1,2)),(Q(1),Q(1,2))],
          [(Q(0),Q(1,100)),(Q(1),Q(99,100))],
          [(Q(0),Q(1,10)),(Q(2),Q(7,10)),(Q(3),Q(1,5))],
          [(Q(-10),Q(1,20)),(Q(-1),Q(9,20)),(Q(1),Q(9,20)),(Q(10),Q(1,20))]]
for j,atoms in enumerate(examples):
    mean,var,fourth=distribution(atoms)
    kurtosis=fourth/var**2
    p=1/(32*kurtosis)
    width=min(length for length,mass in intervals(atoms) if mass>=1-p)
    assert var<=width**2 and p*width**2<=4*var
    checks.append({'name':f'L2-exact-{j}','pass':True,'variance':str(var),
                   'kurtosis':str(kurtosis),'p':str(p),'width':str(width)})
    for length in [Q(1,2),Q(1)]:
        # A maximizing interval can start at an atom: shifting its left end to
        # its first atom retains all captured atoms and does not increase length.
        maxmass=max(sum(w for x,w in atoms if a<=x<=a+length) for a,w in atoms)
        epsilon=1-maxmass
        assert var>=epsilon*length**2/4
    checks.append({'name':f'L0-exact-{j}','pass':True})

p,q,a,b=Q(1,10),Q(1,5),Q(0),Q(3)
middle=(p*a+q*b)/(p+q)
mean,var,fourth=distribution([(a,p),(middle,1-p-q),(b,q)])
assert var==p*q/(p+q)*(b-a)**2
checks.append({'name':'L1-sharp-equality','pass':True,'variance':str(var)})

joint=[(Q(1),Q(-1),Q(1,3)),(Q(1),Q(2),Q(1,6)),
       (Q(-1),Q(1),Q(1,3)),(Q(-1),Q(-2),Q(1,6))]
assert all(sum(w*d for m,d,w in joint if m==sign)==0 for sign in [Q(-1),Q(1)])
cubic=sum(w*m*d**3 for m,d,w in joint)
fourth=sum(w*(m+d)**4 for m,d,w in joint)
without_cubic=sum(w*(m**4+6*m**2*d**2+d**4) for m,d,w in joint)
assert cubic==2 and fourth==27 and without_cubic==19
checks.append({'name':'L5-cubic-term-cannot-be-discarded','pass':True,
               'actual_fourth':str(fourth),'without_cubic':str(without_cubic)})

measurements=[]
for t in [3,6,12,24,48,96,192]:
    n=math.exp(t)
    prob=math.exp(-t/6)
    base=math.exp(t/3)
    spike=math.sqrt(n*t)
    scale=math.sqrt(n/t)
    var=(1-prob)*base**2+prob*spike**2
    fourth=(1-prob)*base**4+prob*spike**4
    assert spike<n and base<n
    assert base/scale<2 and spike/scale>=base/scale
    # On each constant-survival interval, probability*exp(lambda/6) is
    # largest at its right endpoint; these are all possible extrema.
    tail_ratio=max(math.exp((base/scale)/6),prob*math.exp(t/6))
    assert tail_ratio<=math.exp(1/3)*(1+1e-12)
    measurements.append({'log_n':t,'total_variation_to_sign':prob,
                         'kolmogorov_distance_to_sign':prob/2,
                         'variance_over_n_two_thirds':var/base**2,
                         'finite_n_variance_exponent':math.log(var)/(2*t),
                         'standardized_fourth_moment':fourth/var**2,
                         'max_tail_ratio':tail_ratio})
checks.append({'name':'L4-seven-scale-formulas-and-tail-endpoints','pass':True})
seconds=time.monotonic()-started
assert seconds<30
result={'command':'python -X utf8 ~/brain_workers/w369/check_bridge.py',
        'seconds':seconds,'checks_passed':len(checks),'checks_failed':0,
        'checks':checks,'counterexample_measurements':measurements,
        'analytical_limits':{'weak_limit':'symmetric sign','variance_exponent':'5/12',
                             'claimed_KPZ_variance_exponent':'1/3',
                             'standardized_fourth_moment':'asymptotic to n^(1/6)'},
        'scope':'Supporting finite calculations only; no FPP simulation, no proof certification.'}
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
