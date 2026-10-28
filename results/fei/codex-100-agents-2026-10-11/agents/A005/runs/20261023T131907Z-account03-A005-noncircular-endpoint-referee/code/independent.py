"""Independent direct-character implementation; imports no campaign helper."""
import itertools
import json
import time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def transform(values):
    return tuple(sum(values[x]*(1-2*((x&s).bit_count()%2)) for x in range(8)) for s in range(8))

def derivative_counts(values):
    return tuple(sum(values[x] != values[x^(1<<i)] for x in range(8)) for i in range(3))

def log_series(x):
    z=(x-1)/(x+1)
    term=z
    total=Q(0)
    for j in range(40):
        total += 2*term/Q(2*j+1)
        term *= z*z
    return total,total+2*term/(81*(1-z*z))

LOG_TWO=log_series(Q(2))

@lru_cache(None)
def log2integer(x):
    exponent=x.bit_length()-1
    a,b=log_series(Q(x,1<<exponent))
    return exponent+a/LOG_TWO[1],exponent+b/LOG_TWO[0]

@lru_cache(None)
def entropy(spectrum):
    lower=upper=Q(6)
    for a in spectrum:
        if a:
            l,u=log2integer(abs(a))
            lower -= Q(a*a,32)*u
            upper -= Q(a*a,32)*l
    return lower,upper

def main():
    start=time.monotonic()
    roots=[tuple(1-2*((mask>>x)&1) for x in range(8)) for mask in range(256)]
    spectra=[transform(f) for f in roots]
    costs=[derivative_counts(f) for f in roots]
    terms=[m for m in range(8) if m.bit_count()<=2]
    assert len(terms)==7
    assertions=cases=0
    for mask in range(128):
        polynomial=[terms[j] for j in range(7) if mask>>j&1]
        q=tuple(1-2*(sum((x&m)==m for m in polynomial)%2) for x in range(8))
        dcq=derivative_counts(q)
        active=[i for i,c in enumerate(dcq) if c]
        r=len(active)
        assert sum(dcq)>=4*r; assertions+=1
        outside=sum(1<<i for i in range(3) if i not in active)
        for j,f in enumerate(roots):
            assert time.monotonic()-start<55,'frozen runtime exceeded'
            product=tuple(f[x]*q[x] for x in range(8))
            s=transform(product)
            dcp=derivative_counts(product)
            delta=Q(sum(v<0 for v in f),8)
            for i in range(3):
                change=Q(dcp[i]-costs[j][i],8)
                assert change>=Q(dcq[i],8)-4*delta if i in active else change==0
                assertions+=1
            for t in range(8):
                if t & outside == t:
                    assert sum(s[z]**2 for z in range(8) if z&outside==t)==sum(spectra[j][z]**2 for z in range(8) if z&outside==t)
                    assertions+=1
            if sorted(abs(a) for a in s)==sorted(abs(a) for a in spectra[j]):
                gain=Q(0)
            else:
                gain=entropy(s)[1]-entropy(spectra[j])[0]
            assert gain<=r; assertions+=1
            influence_change=Q(sum(dcp)-sum(costs[j]),8)
            assert influence_change>=Q(r,2)-4*delta*r; assertions+=1
            gamma=5*(Q(1,2)-4*delta)-1
            assert gain-5*influence_change<=-r*gamma; assertions+=1
            cases+=1
    result=dict(status='PASS',cases=cases,exact_assertions=assertions,seconds=time.monotonic()-start,
                domain='all256 Boolean roots on3 bits times all128 quadratic phases',
                arithmetic='direct integer character sums and physical derivatives; rational log series40 terms',
                independence='no main helper imported; distinct Fourier transform and log implementation',
                limitation='same author independent implementation, not independent-agent proof acceptance')
    (ROOT/'out'/'INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
    lower_log,upper_log=log2integer(127)
    deficit_lower=14-Q(16129,8192)*upper_log-Q(15,64)
    assert deficit_lower>Q(1,256)
    phase_gamma=Q(7,8)-15*Q(1,1<<10000)
    assert phase_gamma>Q(3,4)
    scalar=dict(status='PASS',exact_assertions=2,point8_deficit_lower=str(deficit_lower),
                phase_gamma_lower='3/4',degree=2,K='15/4',k=10000,
                scope='new phase gap and rechecked seed gap; prior full paid-pair scalar certificate consumed, not rerun')
    (ROOT/'out'/'SCALAR.json').write_text(json.dumps(scalar,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(scalar))

if __name__=='__main__':
    main()
