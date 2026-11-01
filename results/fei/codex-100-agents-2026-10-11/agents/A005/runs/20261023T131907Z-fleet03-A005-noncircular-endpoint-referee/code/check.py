"""Frozen exact phase-normal-form validation; no floating acceptance."""
import argparse
import itertools
import json
import time
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def walsh(f):
    a = list(f)
    s = 1
    while s < len(a):
        for j in range(0, len(a), 2*s):
            for k in range(j, j+s):
                x, y = a[k], a[k+s]
                a[k], a[k+s] = x+y, x-y
        s *= 2
    return tuple(a)

def infs(f, n):
    return tuple(F(sum(f[x] != f[x ^ (1<<i)] for x in range(1<<n)), 1<<n) for i in range(n))

def ln_interval(a):
    z = (a-1)/(a+1)
    acc = F(0)
    for j in range(32):
        acc += 2*z**(2*j+1)/(2*j+1)
    return acc, acc+2*z**65/(65*(1-z*z))

LN2 = ln_interval(F(2))

@lru_cache(None)
def log_interval(w):
    e = w.bit_length()-1
    lo, hi = ln_interval(F(w, 1<<e))
    return F(e)+lo/LN2[1], F(e)+hi/LN2[0]

def histogram(w):
    return tuple(sorted(Counter(abs(x) for x in w if x).items()))

@lru_cache(None)
def entropy_interval(hist, n):
    lo = hi = F(2*n)
    for w, count in hist:
        a, b = log_interval(w)
        coefficient = F(2*count*w*w, 1<<(2*n))
        lo -= coefficient*b
        hi -= coefficient*a
    return lo, hi

def entropy_difference(wnew, wold, n):
    a, b = histogram(wnew), histogram(wold)
    if a == b:
        return F(0), F(0)
    alo, ahi = entropy_interval(a, n)
    blo, bhi = entropy_interval(b, n)
    return alo-bhi, ahi-blo

def monomials(n, degree):
    return tuple(mask for mask in range(1<<n) if mask.bit_count() <= degree)

def phase(n, terms, mask):
    selected = [terms[j] for j in range(len(terms)) if mask >> j & 1]
    return tuple(1-2*(sum((x & m) == m for m in selected) % 2) for x in range(1<<n))

def validate(mode):
    start = time.monotonic()
    if mode == 'pilot':
        n, degree, roots = 4, 2, [0]
        masks = [0,1,2,3,7,15,31,127,511,1023,2047]
    elif mode == 'quadratic':
        n, degree, roots = 4, 2, range(16)
        masks = range(2048)
    else:
        n, degree, roots = 5, 3, range(32)
        masks = sorted(set(range(256)) | {1<<j for j in range(26)} | {(1<<26)-1})
        assert len(masks) == 275
    terms = monomials(n, degree)
    checks = cases = 0
    K = F(16 if mode == 'cubic' else 8)
    gamma = K*(F(1, 1<<(degree-1))-F(4,1<<n))-1
    assert gamma > 0
    for mask in masks:
        q = phase(n, terms, mask)
        iq = infs(q,n)
        support = sum((1<<j) for j in range(n) if iq[j])
        r = support.bit_count()
        assert sum(iq) >= F(r,1<<(degree-1)); checks += 1
        for point in roots:
            assert time.monotonic()-start < 55, 'frozen runtime exceeded'
            f = tuple(-1 if x == point else 1 for x in range(1<<n))
            prod = tuple(a*b for a,b in zip(q,f))
            wf, wp = walsh(f), walsh(prod)
            if0, ip = infs(f,n), infs(prod,n)
            delta = F(1,1<<n)
            for i in range(n):
                if support >> i & 1:
                    assert ip[i]-if0[i] >= iq[i]-4*delta
                else:
                    assert ip[i] == if0[i]
                checks += 1
            outside = ((1<<n)-1) ^ support
            old, new = Counter(), Counter()
            for s in range(1<<n):
                old[s & outside] += wf[s]*wf[s]
                new[s & outside] += wp[s]*wp[s]
            assert old == new; checks += 1
            lo, hi = entropy_difference(wp, wf, n)
            assert hi <= r; checks += 1
            assert sum(ip)-sum(if0) >= F(r,1<<(degree-1))-4*delta*r; checks += 1
            assert hi-K*(sum(ip)-sum(if0)) <= -r*gamma; checks += 1
            cases += 1
    result = dict(status='PASS', mode=mode, dimension=n, degree=degree, K=str(K),
                  gamma=str(gamma), cases=cases, phases=len(masks),
                  exact_assertions=checks, seconds=time.monotonic()-start,
                  arithmetic='integer Walsh and physical edges; Fraction atanh log enclosures,32 terms',
                  scope='finite validation of analytic inequalities, not enumeration of general cubic orbit')
    (BASE/'out'/f'{mode.upper()}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode',choices=['pilot','quadratic','cubic'])
    validate(parser.parse_args().mode)
