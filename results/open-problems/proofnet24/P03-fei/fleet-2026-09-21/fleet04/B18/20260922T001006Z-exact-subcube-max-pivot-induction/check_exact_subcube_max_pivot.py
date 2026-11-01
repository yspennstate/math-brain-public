#!/usr/bin/env python3
from fractions import Fraction
from math import log2

TOL = 1e-10

def pc(x):
    return x.bit_count()

def walsh(vals, n):
    N = 1 << n
    out = []
    for S in range(N):
        z = sum(v * (-1 if pc(S & x) & 1 else 1) for x, v in enumerate(vals))
        out.append(Fraction(z, N))
    return out

def entropy_influence(vals, n):
    H = I = 0.0
    for S, a in enumerate(walsh(vals, n)):
        p = float(a * a)
        if p:
            H -= p * log2(p)
            I += pc(S) * p
    return H, I

def influences(vals, n):
    N = 1 << n
    return [
        sum(vals[x] != vals[x ^ (1 << i)] for x in range(N)) / N
        for i in range(n)
    ]

def gauge(vals, n, T):
    return [
        v * (-1 if pc(x & T) & 1 else 1)
        for x, v in enumerate(vals)
    ]

def h2(p):
    if p == 0.0 or p == 1.0:
        return 0.0
    return -p * log2(p) - (1 - p) * log2(1 - p)

def detect_subcube(supp, m):
    if not supp or len(supp) & (len(supp) - 1):
        return None
    fixed, aval = [], {}
    for j in range(m):
        bits = {(s >> j) & 1 for s in supp}
        if len(bits) == 1:
            fixed.append(j)
            aval[j] = next(iter(bits))
    if len(supp) != 1 << (m - len(fixed)):
        return None
    exp = {
        s for s in range(1 << m)
        if all(((s >> j) & 1) == aval[j] for j in fixed)
    }
    return (fixed, aval) if exp == set(supp) else None

def canonical_data(vals, n, pivot, others, fixed, aval):
    F = [others[j] for j in fixed]
    Z = [i for i in range(n) if i != pivot and i not in F]
    tau, sigma = [], []

    def point(s, y, zmask):
        x = (s << pivot)
        for i, b in y.items():
            if b:
                x |= 1 << i
        for a, i in enumerate(Z):
            if (zmask >> a) & 1:
                x |= 1 << i
        return x

    ya = {others[j]: aval[j] for j in fixed}
    for zmask in range(1 << len(Z)):
        v0 = vals[point(0, ya, zmask)]
        v1 = vals[point(1, ya, zmask)]
        if v1 != -v0:
            return None
        sigma.append(v0)

        yout = dict(ya)
        yout[F[0]] ^= 1
        tv = vals[point(0, yout, zmask)]
        for ymask in range(1 << len(F)):
            y = {F[a]: (ymask >> a) & 1 for a in range(len(F))}
            if all(y[F[a]] == ya[F[a]] for a in range(len(F))):
                continue
            for s in (0, 1):
                if vals[point(s, y, zmask)] != tv:
                    return None
        tau.append(tv)
    return F, Z, tau, sigma

def control_entropy(r):
    q = 2.0 ** (-r)
    Hy0 = h2(q) + q * log2((1 - q) / q)
    return h2(q) + (1 - q) * Hy0 + q * r

candidate_pivots = 0
representation_failures = 0
formula_failures = 0
bound_failures = 0
max_control_ratio = 0.0

for n in range(1, 5):
    N = 1 << n
    # quotient by global sign: f(0)=+1
    for mask in range(1 << (N - 1)):
        vals = [1] + [
            -1 if (mask >> (i - 1)) & 1 else 1
            for i in range(1, N)
        ]
        raw_p = influences(vals, n)
        folded = [min(p, 1 - p) for p in raw_p]

        for pivot in range(n):
            if folded[pivot] == 0 or folded[pivot] + TOL < max(folded):
                continue

            # Median-character center all coordinates. Centering the pivot,
            # if needed, complements its pivotality event; centering other
            # coordinates leaves that event unchanged.
            T = sum((1 << i) for i, p in enumerate(raw_p) if p > 0.5)
            g = gauge(vals, n, T)
            pg = influences(g, n)
            others = [i for i in range(n) if i != pivot]

            supp = []
            for m in range(1 << (n - 1)):
                x = sum(
                    ((m >> a) & 1) << i
                    for a, i in enumerate(others)
                )
                if g[x] != g[x | (1 << pivot)]:
                    supp.append(m)

            det = detect_subcube(supp, n - 1)
            if det is None:
                continue
            fixed, aval = det
            r = len(fixed)
            if r == 0:
                continue
            q = len(supp) / (1 << (n - 1))
            if abs(q - folded[pivot]) > TOL:
                representation_failures += 1
                continue

            # Maximum folded influence gives the average-control condition.
            F = [others[j] for j in fixed]
            if sum(pg[k] for k in F) > r * q + TOL:
                representation_failures += 1
                continue

            candidate_pivots += 1
            data = canonical_data(g, n, pivot, others, fixed, aval)
            if data is None:
                representation_failures += 1
                continue

            _, Z, tau, sigma = data
            H, I = entropy_influence(g, n)
            Ht, It = entropy_influence(tau, len(Z))
            Hs, Is = entropy_influence(sigma, len(Z))
            C = control_entropy(r)
            Hf = C + (1 - q) * Ht + q * Hs
            If = (r + 1) * q + (1 - q) * It + q * Is

            if abs(H - Hf) > TOL or abs(I - If) > TOL:
                formula_failures += 1
            ratio = C / ((r + 1) * q)
            max_control_ratio = max(max_control_ratio, ratio)
            if C > 4 * (r + 1) * q + TOL:
                bound_failures += 1

# Independent scalar scan, far beyond the exhaustive dimensions.
for r in range(1, 257):
    q = 2.0 ** (-r)
    C = control_entropy(r)
    if C > 4 * (r + 1) * q + 1e-12:
        bound_failures += 1

print("PASS" if not (representation_failures or formula_failures or bound_failures) else "FAIL")
print(f"candidate_exact_subcube_max_pivots={candidate_pivots}")
print(f"representation_failures={representation_failures}")
print(f"formula_failures={formula_failures}")
print(f"control_bound_failures={bound_failures}")
print(f"max_exhaustive_control_entropy_ratio={max_control_ratio:.12f}")
print("scalar_scan_r=1..256")
