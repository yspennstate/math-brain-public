"""Frozen A015-positive-anchor-v1; exact physical truth/Walsh/edge checks."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import argparse, hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
checks = 0

def ck(condition):
    global checks
    checks += 1
    assert condition, checks
    if checks % 1024 == 0:
        assert time.perf_counter()-START < 55, 'frozen runtime exceeded'

def walsh(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    # Physical sign coordinate is +1 for bit1, -1 for bit0.
    return [Q(x*(-1)**mask.bit_count(), len(a)) for mask,x in enumerate(a)]

def physical(table, n):
    return [Q(sum(table[x] != table[x ^ (1 << i)] for x in range(1 << n)), 1 << n)
            for i in range(n)]

def monotone(table, s):
    return all(table[x] <= table[x | (1 << i)] for x in range(1 << s) for i in range(s))

def anchors(table, s):
    allbits = (1 << s)-1
    return [allbits ^ x for x in range(1 << s) if table[x] < 0 and
            all(table[x | (1 << i)] > 0 for i in range(s) if not x & (1 << i))]

# Rational logarithm intervals, with the explicit positive-series remainder.
def seed_ln2():
    t = Q(1,3)
    lo = 2*sum((t**(2*j+1)/Q(2*j+1) for j in range(18)), Q(0))
    return lo, lo+2*t**37/(37*(1-t*t))

LN2 = seed_ln2()

@lru_cache(None)
def log2_interval(v):
    assert v > 0
    k = 0
    while v >= 2:
        v /= 2
        k += 1
    while v < 1:
        v *= 2
        k -= 1
    t = (v-1)/(v+1)
    lo = 2*sum((t**(2*j+1)/Q(2*j+1) for j in range(18)), Q(0))
    hi = lo+2*t**37/(37*(1-t*t))
    return k+lo/LN2[1], k+hi/LN2[0]

def entropy_interval(probs):
    lo = hi = Q(0)
    counts = {}
    for p in probs:
        if p:
            counts[p] = counts.get(p, 0)+1
    for p, count in counts.items():
        a, b = log2_interval(1/p)
        lo += count*p*a
        hi += count*p*b
    return lo, hi

def positive_case(table, s, L):
    aa = anchors(table, s)
    t = len(aa)
    n = s+t*L
    ck(n <= 12)
    eps = Q(1,1 << L)
    bb = [[j for j, anchor in enumerate(aa) if not z & anchor] for z in range(1 << s)]
    av = [eps**len(b) for b in bb]
    q = Q(table.count(-1), 1 << s)
    # Build literal CNF, separately from the b(z) conditional formula.
    truth = []
    for x in range(1 << n):
        z = x & ((1 << s)-1)
        good = all((z & anchor) or ((x >> (s+j*L+l)) & 1)
                   for j, anchor in enumerate(aa) for l in range(L))
        truth.append(1 if good else -1)
    ff = walsh(truth)
    gg = walsh(table)
    mm = walsh([2*a-1 for a in av])
    ck(sum(p*p for p in ff) == 1)
    for S in range(1 << s):
        ck(ff[S] == mm[S])
    # Each physical coefficient, including cross-private-group sets.
    for mask, coeff in enumerate(ff):
        T, S = mask >> s, mask & ((1 << s)-1)
        if T:
            groups = [j for j in range(t) if T & (((1 << L)-1) << (j*L))]
            pred = 2*sum(((-1)**(S.bit_count()-(z & S).bit_count())*av[z]
                          for z in range(1 << s) if all(j in bb[z] for j in groups)), Q(0))/(1 << s)
            ck(coeff == pred)
    infl = physical(truth, n)
    ck(sum(infl) == sum((Q(mask.bit_count())*v*v for mask,v in enumerate(ff)), Q(0)))
    core = sum((sum(abs(av[z]-av[z ^ (1 << i)]) for z in range(1 << s))/Q(1 << s)
                for i in range(s)), Q(0))
    private = 2*L*sum((len(bb[z])*av[z] for z in range(1 << s)), Q(0))/(1 << s)
    ck(sum(infl[:s]) == core)
    ck(sum(infl[s:]) == private)
    ig = sum(physical(table, s))
    ck(private <= 2*L*q*eps)
    ck(abs(core-ig) <= 2*s*q*eps)
    ck(abs(sum(infl)-ig) <= 2*q*(s+L)*eps)
    mass = sum((v*v for mask,v in enumerate(ff) if mask >> s), Q(0))
    ck(mass == 4*sum((a*(1-a) for a in av), Q(0))/(1 << s))
    ck(mass <= 4*q*eps)
    # All private variables genuinely relevant.
    ck(all(v > 0 for v in infl[s:]))
    coarse = [v*v for v in ff[:1 << s]]+[mass]
    tv = (sum(abs(coarse[i]-gg[i]*gg[i]) for i in range(1 << s))+mass)/2
    ck(tv <= 4*eps)
    hf = entropy_interval(v*v for v in ff)
    hp = entropy_interval(coarse)
    # Interval strict tests with exact-zero sector handled explicitly.
    ck(hf[1] >= hp[0])
    ck(hf[0] <= hp[1]+mass*n)
    if L >= 3:
        hg = entropy_interval(v*v for v in gg)
        hb = entropy_interval([4*eps,1-4*eps])
        err = hb[1]+4*eps*s+4*q*eps*n
        ck(hf[1]-hg[0] <= err)
        ck(hg[1]-hf[0] <= err)
    return n

def signed_case(table, s, L):
    false = [z for z,v in enumerate(table) if v < 0]
    n = s+len(false)*L
    ck(n <= 10)
    eps = Q(1,1 << L)
    q = Q(len(false),1 << s)
    truth = []
    for x in range(1 << n):
        z = x & ((1 << s)-1)
        truth.append(1 if all(z != v or ((x >> (s+j*L+l)) & 1)
                            for j,v in enumerate(false) for l in range(L)) else -1)
    ff, gg = walsh(truth), walsh(table)
    for S in range(1 << s):
        ck(ff[S] == (1-eps)*gg[S]+(eps if S == 0 else 0))
    privmass = Q(0)
    for mask,v in enumerate(ff):
        T = mask >> s
        if T:
            groups = sum(bool(T & (((1 << L)-1) << (j*L))) for j in range(len(false)))
            ck(abs(v) == (Q(2,1 << s)*eps if groups == 1 else 0))
            privmass += v*v
    ck(privmass == 4*q*eps*(1-eps))
    ig = sum(physical(table,s))
    ck(sum(physical(truth,n)) == (1-eps)**2*ig+2*q*eps*(s*(1-eps)+L))
    # Exact conditional normalization as rational multiplicative identity:
    # R has uniform atom1/(2^n-1), Z=(2^s-1)/(2^n-1), r=R/Z.
    atom = Q(1,(1 << n)-1)
    Z = Q((1 << s)-1,(1 << n)-1)
    ck(atom/Z == Q(1,(1 << s)-1))

def run(pilot):
    count = signed = 0
    maxn = 0
    for s in range(1, (2 if pilot else 3)+1):
        for code in range(1, (1 << (1 << s))-1):
            table = [1 if code & (1 << x) else -1 for x in range(1 << s)]
            if monotone(table,s):
                for L in ([1,2] if pilot else [1,2,3]):
                    maxn = max(maxn,positive_case(table,s,L))
                    count += 1
    ck(count == (10 if pilot else 69))
    if not pilot:
        for s in range(1,4):
            for code in range(1,(1 << (1 << s))-1):
                table = [1 if code & (1 << x) else -1 for x in range(1 << s)]
                signed_case(table,s,1)
                signed += 1
                if s <= 2:
                    signed_case(table,s,2)
                    signed += 1
        ck(signed == 286)
    scalars = 0
    for s in range(1, (8 if pilot else 64)+1):
        for j in range(0, (3 if pilot else 8)+1):
            delta = Q(1,1 << j)
            A = 0
            while (1 << A) < 8*s/delta:
                A += 1
            L = 2*A
            eps = Q(1,1 << L)
            ck(A >= 3)
            ck(A <= 8*s/delta)
            ck(eps*(s+L)/(1-eps)**2 <= delta)
            ck(eps*(s+L)/(1-eps)**2 <= Q(17,32)*delta/s)
            scalars += 1
    # Positive AND2 core: distinct ratios disprove affine transplantation.
    for L in [1,2,3]:
        eps = Q(1,1 << L)
        m = [2*eps**(2-z.bit_count())-1 for z in range(4)]
        mm, gg = walsh(m), walsh([-1,-1,-1,1])
        ck(mm[1]/gg[1] == 1-eps*eps)
        ck(mm[3]/gg[3] == (1-eps)**2)
        ck(mm[1]/gg[1] != mm[3]/gg[3])
    # Two independent signed false-point groups on neighboring core points.
    eps = Q(1,2)
    ck(2*eps*(1-eps) > abs(eps-eps))
    # Scalar key boundary, separate from formula code.
    for b in range(1,129):
        ck(b <= (1 << (b-1)))
    return {"status":"PASS", "positive_cases":count,"signed_review_cases":signed,
            "scalar_pairs":scalars,"assertions":checks,"max_positive_dimension":maxn,
            "arithmetic":"integer Walsh and physical flips; exact fractions and rational entropy intervals",
            "elapsed_seconds":time.perf_counter()-START,
            "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pilot', action='store_true')
    args = parser.parse_args()
    result = run(args.pilot)
    output = ROOT/'out'/('pilot.json' if args.pilot else 'checks.json')
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
