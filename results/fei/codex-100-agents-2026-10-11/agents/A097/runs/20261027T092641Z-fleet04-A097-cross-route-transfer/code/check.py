import json, math, sys, time
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
COUNT = 0

def ck(ok):
    global COUNT
    COUNT += 1
    assert ok, COUNT
    if time.monotonic() - START > 55:
        raise RuntimeError('frozen 55 second limit exceeded; INCOMPLETE')

def walsh(values):
    a = list(values)
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2*step):
            for z in range(step):
                x, y = a[j+z], a[j+z+step]
                a[j+z], a[j+z+step] = x+y, x-y
        step *= 2
    return [F(x, len(a)) for x in a]

def spectrum(v):
    return [x*x for x in walsh(v)]

def compress(s, i):
    return (s & ((1 << i)-1)) | ((s >> (i+1)) << i)

def project(p, i):
    out = [F(0)]*(len(p)//2)
    for s, x in enumerate(p):
        out[compress(s, i)] += x
    return out

def restrict(v, i, b):
    return [x for s, x in enumerate(v) if (s >> i) & 1 == b]

def influence(p):
    return sum((x*s.bit_count() for s, x in enumerate(p)), F(0))

def factors(n):
    out = Counter()
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out

def addlog(out, x, c):
    if not c or x == 1:
        return
    for p, k in factors(x.numerator).items():
        out[p] += c*k
    for p, k in factors(x.denominator).items():
        out[p] -= c*k

def ce(p, q):
    out = defaultdict(F)
    for x, y in zip(p, q):
        if x:
            ck(y > 0)
            addlog(out, y, -x)
    return {k: v for k, v in out.items() if v}

def combine(*terms):
    out = defaultdict(F)
    for scale, term in terms:
        for p, c in term.items():
            out[p] += scale*c
    return {k: v for k, v in out.items() if v}

def entropy(p):
    return ce(p, p)

def div(p, q):
    return combine((1, ce(p, q)), (-1, entropy(p)))

@lru_cache(None)
def ln_bounds(x):
    # Exact rational atanh expansion, geometric tail; normalize to [1,2).
    x = F(x)
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    z = (x-1)/(x+1)
    z2 = z*z
    t = z
    s = F(0)
    for j in range(24):
        s += 2*t/(2*j+1)
        t *= z2
    rem = 2*t/(49*(1-z2))
    if k:
        # ln 2 uses the same expansion without recursive normalization.
        zz = F(1, 3)
        tt = zz
        ss = F(0)
        for j in range(24):
            ss += 2*tt/(2*j+1)
            tt /= 9
        rr = 2*tt/(49*(1-F(1, 9)))
        return (s+k*ss, s+rem+k*(ss+rr)) if k > 0 else (s+k*(ss+rr), s+rem+k*ss)
    return s, s+rem

def lower_upper_natural(logs):
    lo = hi = F(0)
    for p, c in logs.items():
        a, b = ln_bounds(F(p))
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    return lo, hi

def census(maxn):
    roots = edges = 0
    for n in range(maxn+1):
        M = 1 << n
        for table in range(1 << M):
            roots += 1
            v = [1 if (table >> s) & 1 else -1 for s in range(M)]
            p = spectrum(v)
            ck(sum(p) == 1)
            for i in range(n):
                children = [spectrum(restrict(v, i, b)) for b in [0, 1]]
                pp = project(p, i)
                ck(pp == [(x+y)/2 for x, y in zip(*children)])
                infi = sum((x for s, x in enumerate(p) if s >> i & 1), F(0))
                ck(influence(p) == infi + sum(map(influence, children))/2)
                jj = combine((F(1, 2), div(children[0], pp)), (F(1, 2), div(children[1], pp)))
                lo, hi = lower_upper_natural(jj)
                ck(not jj or (lo >= 0 and hi <= 2*infi))
                for q in [p, [(x+F(1, M))/2 for x in p]]:
                    edges += 1
                    qp = project(q, i)
                    d = div(p, q)
                    dp = div(pp, qp)
                    loss = combine((1, d), (-1, dp))
                    avg = combine((F(1, 2), div(children[0], qp)), (F(1, 2), div(children[1], qp)))
                    ck(combine((1, avg), (-1, d), (-1, jj), (1, loss)) == {})
                    B = combine((1, entropy(p)), (-1, entropy(pp)))
                    avgce = combine((F(1, 2), ce(children[0], qp)), (F(1, 2), ce(children[1], qp)))
                    ck(combine((1, avgce), (-1, ce(p, q)), (1, B), (1, loss)) == {})
    return roots, edges

def family(ns):
    profiles = 0
    records = []
    for n in ns:
        M = 1 << n
        # Actual truth table; n=10 is still only 1024 entries.
        values = []
        for x in range(M):
            val = 1
            for j in range(0, n, 2):
                if not (x >> j & 1) and not (x >> (j+1) & 1):
                    val = -val
            values.append(val)
        p = spectrum(values)
        ck(p == [F(1, M)]*M)
        ck(influence(p) == F(n, 2))
        for k in range(2, n):
            profiles += 1
            m = n * (1 << (n-k+1))
            N = 1 << m
            eps = F(1, N)
            tail = 1 << k
            weights = [N]*M
            for V in range(1 << k):
                weights[tail | V] += (N-1) * (-1 if V.bit_count() & 1 else 1)
            ck(all(x > 0 for x in weights))
            ck(sum(weights) == M*N)
            ck(weights[0] == N)
            # Superset zeta transform checks EVERY inclusion marginal.
            zeta = list(weights)
            for i in range(n):
                for U in range(M):
                    if not U >> i & 1:
                        zeta[U] += zeta[U | (1 << i)]
            for U in range(M):
                if U.bit_count() < k:
                    ck(zeta[U] == (M >> U.bit_count()) * N)
            counts = Counter(weights)
            ck(counts[1] == counts[2*N-1] == 1 << (k-1))
            ck(counts[N] == M-(1 << k))
            q = [F(w, M*N) for w in weights]
            for i in range(k):
                ck(project(q, i) == project(p, i))
                ck(sum((x for s, x in enumerate(p) if s >> i & 1), F(0)) == F(1, 2))
            a = F(1 << (k-1), M)
            ck(a*m == n)
            ck(0 < eps < 1 and 1 < 2-eps < 2)
            # Grouped exact log monomials: D=-a log eps-a log(2-eps).
            # The two occupied likelihoods and their multiplicities suffice.
            ck(F(counts[1], M) == F(counts[2*N-1], M) == a)
            if k == n-1:
                ck(a == F(1, 4) and m == 4*n)
            # Distinct moment outside the declared range: perturbation is real.
            ck(zeta[(1 << k)-1] != (M >> k)*N)
            records.append({'n': n, 'k': k, 'epsilon_exponent': m,
                            'loss_lower': str(F(n)-a), 'loss_upper': n,
                            'CE_rate_strict_upper': 4,
                            'matched_marginal_order': k-1})
    return profiles, records

def calibration():
    cases = 0
    # Finite rational log-affine fixtures: u/q is constant on two cells.
    # p != u is allowed while the constraints p0 and p1+p2 match.
    for den in [4, 8, 16]:
        for a in range(1, den):
            q = [F(1, 4)]*4
            # Affine constraints fix first and last cells to their true values.
            u = [F(a, 2*den), F(1, 4), F(1, 4), F(den-a, 2*den)]
            for b in range(1, den):
                p = [u[0], F(b, 2*den), F(den-b, 2*den), u[3]]
                ck(sum(p) == sum(u) == 1)
                ck(combine((1, div(p, q)), (-1, div(p, u)), (-1, div(u, q))) == {})
                # Full scalar mass penalty cancels at s=1/2.
                ck(combine((1, ce(p, [x/2 for x in q])), (-1, ce(p, [x/2 for x in u])), (-1, div(u, q))) == {})
                cases += 1
    # Derivative erratum t factor: t=3/4, a=1/4, z=1/3.
    t, a, z = F(3, 4), F(1, 4), F(1, 3)
    ck(-a/z+(t-a)/(t-z) == t*(z-a)/(z*(t-z)) == F(9, 20))
    return cases

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'main'
    roots, edges = census(2 if mode == 'pilot' else 3)
    profiles, records = family([4] if mode == 'pilot' else [4, 6, 8, 10])
    cal = calibration()
    result = {'status': 'PASS', 'mode': mode, 'roots': roots, 'query_reference_cases': edges,
              'family_profiles': profiles, 'calibration_fixtures': cal,
              'exact_assertions': COUNT, 'seconds': time.monotonic()-START,
              'records': records, 'arithmetic': 'integers/Fraction, exact formal prime logs, rigorous natural-log intervals'}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/f'CHECK_{mode}.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}))
