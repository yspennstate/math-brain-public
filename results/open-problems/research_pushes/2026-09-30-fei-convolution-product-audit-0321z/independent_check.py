#!/usr/bin/env python3
"""Independent audit checks, with direct Walsh sums and rational log bounds.

This does not establish any unproved FEI inequality. All accepted comparisons
use integers/Fractions; decimal text is descriptive only.
"""
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parent

def walsh_direct(values):
    return [sum(v * (-1 if (s & x).bit_count() % 2 else 1)
                for x, v in enumerate(values)) for s in range(len(values))]

@lru_cache(None)
def log_two_interval(value):
    x = F(value)
    assert x > 0
    if x < 1:
        a, b = log_two_interval(1 / x)
        return -b, -a
    exponent = 0
    while x >= 2:
        x /= 2
        exponent += 1
    if x == 1:
        return F(exponent), F(exponent)
    def natural_series(y):
        z = (y - 1) / (y + 1)
        partial = sum((2 * z ** (2*j+1) / (2*j+1) for j in range(64)), F(0))
        tail = 2 * z ** 129 / (129 * (1-z*z))
        return partial, partial+tail
    a, b = natural_series(x)
    c, d = natural_series(F(2))
    return F(exponent)+a/d, F(exponent)+b/c

def entropy_interval(weights):
    low = high = F(0)
    for weight, count in Counter(weights).items():
        if not weight:
            continue
        a, b = log_two_interval(1/weight)
        low += count*weight*a
        high += count*weight*b
    return low, high

def entropy_walsh(w):
    return entropy_interval([F(v*v, len(w)**2) for v in w])

def minus(a, b):
    return a[0]-b[1], a[1]-b[0]

def plus(a, b):
    return a[0]+b[0], a[1]+b[1]

def summary(interval):
    return {'rational_lower':str(interval[0]), 'rational_upper':str(interval[1]),
            'decimal_summary':[float(x) for x in interval]}

def direct_influence(values):
    n = (len(values)-1).bit_length()
    return [F(sum(values[x] != values[x^(1<<i)] for x in range(len(values))), len(values))
            for i in range(n)]

def main():
    witness = json.loads((ROOT/'product/witness.json').read_text())
    N = 1 << witness['n']
    negative = set(witness['negative_f'])
    f = [-1 if x in negative else 1 for x in range(N)]
    g = [-1]+[1]*(N-1)
    h = [x*y for x,y in zip(f,g)]
    wf, wg, wh = map(walsh_direct, (f,g,h))
    assert Counter(wf) == {-6:48, -2:60, 26:16, 30:4}
    assert Counter(wg) == {-2:127, 126:1}
    assert Counter(wh) == {-8:48, -4:60, 24:16, 28:4}
    for row in (wf,wg,wh):
        assert sum(x*x for x in row) == N*N
    ef, eg, eh = map(entropy_walsh, (wf,wg,wh))
    gap = minus(eh,plus(ef,eg))
    assert gap[0] > F('0.1630852002095')
    out = {'status':'PASS', 'full_FEI':'OPEN', 'seven_bit_gap':summary(gap)}

    # Reconstruct the physical/spectral joint law directly, without FWHT.
    joint = []
    mean_entropy = (F(0),F(0))
    average_influence = [F(0)]*7
    for z in range(N):
        hz = [f[x]*g[x^z] for x in range(N)]
        wz = walsh_direct(hz)
        joint.append([F(v*v,N**3) for v in wz])
        a,b = entropy_walsh(wz)
        mean_entropy = (mean_entropy[0]+a/N,mean_entropy[1]+b/N)
        average_influence = [a+b/N for a,b in zip(average_influence,direct_influence(hz))]
    assert all(sum(row)==F(1,N) for row in joint)
    q = [sum(row[u] for row in joint) for u in range(N)]
    independent_xor = [F(sum(wf[s]**2*wg[s^u]**2 for s in range(N)),N**4) for u in range(N)]
    assert q == independent_xor
    entropy_q = entropy_interval(q)
    residual = minus(plus(ef,eg),mean_entropy)
    hidden = minus(plus(ef,eg),entropy_q)
    information = minus(entropy_q,mean_entropy)
    ledger_error = minus(residual,plus(hidden,information))
    assert ledger_error[0] <= 0 <= ledger_error[1]
    assert information[0]>0 and hidden[0]>information[1]
    ai,bi = direct_influence(f),direct_influence(g)
    assert average_influence == [a+b-2*a*b for a,b in zip(ai,bi)]
    out['averaged_joint_law'] = {'translations':N,'marginal_entries':N,
        'mean_entropy':summary(mean_entropy), 'H_S_given_U':summary(hidden),
        'I_U_Z':summary(information), 'entropy_deficit':summary(residual),
        'influence_identity':'exact Fraction equality on every coordinate'}

    # Direct sum certificates for the two rare clauses in dimension eleven.
    m = 6
    p = F(1,2**(m-1))
    M = 1 << (2*m-1)
    amask = (1<<m)-1
    bmask = 1|(((1<<(m-1))-1)<<m)
    ff = [-1 if x&amask==0 else 1 for x in range(M)]
    gg = [-1 if x&bmask==0 else 1 for x in range(M)]
    hh = [a*b for a,b in zip(ff,gg)]
    wff,whh = walsh_direct(ff),walsh_direct(hh)
    predicted = Counter()
    for coefficient,count in [(1-2*p+2*p*p,1),(-2*p*(1-p),1),
            (-p*(1-2*p),4*(1/p-1)),(2*p*p,2*(1/p-1)**2)]:
        predicted[coefficient] += int(count)
    assert Counter(F(w,M) for w in whh) == predicted
    clause_gap = minus(entropy_walsh(whh),plus(entropy_walsh(wff),entropy_walsh(wff)))
    assert clause_gap[0] > F('0.00239650700679')
    assert sum(direct_influence(ff))+sum(direct_influence(gg))-sum(direct_influence(hh))==2*p*p
    out['eleven_bit_recovered_clause_gap'] = summary(clause_gap)
    out['eleven_bit_actual_pivotal_deficit'] = str(2*p*p)

    # All physical flip points, not only the origin, in dimensions 2 and 3.
    surgery_count=0
    for n in (2,3):
        size=1<<n
        for table in range(1<<size):
            values=[-1 if table>>x&1 else 1 for x in range(size)]
            w=walsh_direct(values)
            if all(w):
                continue
            assert all(v%4==0 for v in w)
            for x0 in range(size):
                mutated=values[:]
                mutated[x0]*=-1
                new=walsh_direct(mutated)
                for s,(a,b) in enumerate(zip(w,new)):
                    chi=-1 if (s&x0).bit_count()%2 else 1
                    assert b==a-2*values[x0]*chi and b!=0
                    assert a*b>0 if a else b==-2*values[x0]*chi
                surgery_count+=1
    out['all_point_surgery_cases_n2_n3'] = surgery_count
    out['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('averaged_joint_law','seven_bit_gap','eleven_bit_recovered_clause_gap')},indent=2))
    print('n7 gap:',gap[0] > F('0.1630852002095'))
    print('n11 gap:',clause_gap[0] > F('0.00239650700679'))

if __name__=='__main__':
    main()
