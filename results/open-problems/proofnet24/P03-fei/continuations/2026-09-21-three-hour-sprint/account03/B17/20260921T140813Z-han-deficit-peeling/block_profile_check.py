from __future__ import annotations
from fractions import Fraction
from itertools import combinations
from math import log2, log
from decimal import Decimal, getcontext

C_EXT = 6.521845710923046575
C_TEST = 7.0


def h2f(p: Fraction) -> float:
    if p == 0 or p == 1:
        return 0.0
    x = float(p)
    return -x * log2(x) - (1 - x) * log2(1 - x)


def fwht_int(vals):
    a = list(map(int, vals))
    h = 1
    n = len(a)
    while h < n:
        for s in range(0, n, 2 * h):
            for j in range(s, s + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(vals):
    N = len(vals)
    w = fwht_int(vals)
    return [Fraction(x * x, N * N) for x in w]


def entropy(ps):
    out = 0.0
    for p in ps:
        if p:
            x = float(p)
            out -= x * log2(x)
    return out


def stats(vals, n):
    ps = spectrum(vals)
    H = entropy(ps)
    inf = []
    for i in range(n):
        inf.append(sum(p for m, p in enumerate(ps) if (m >> i) & 1))
    return H, inf


def restrict(vals, n, R, out):
    R = tuple(R)
    outpos = [i for i in range(n) if i not in R]
    z = []
    for a in range(1 << len(R)):
        x = 0
        for k, i in enumerate(R):
            if (a >> k) & 1:
                x |= 1 << i
        for k, i in enumerate(outpos):
            if (out >> k) & 1:
                x |= 1 << i
        z.append(vals[x])
    return z


def credit_rhs(vals, n, r, C):
    H, _ = stats(vals, n)
    tot = 0.0
    count = 0
    for R in combinations(range(n), r):
        for y in range(1 << (n - r)):
            face = restrict(vals, n, R, y)
            Hf, ps = stats(face, r)
            credit = max(0.0, sum(C * float(p) - h2f(p) for p in ps))
            tot += Hf + credit
            count += 1
    rhs = (n / r) * (tot / count)
    return H, rhs, rhs - H


def onepoint(n):
    a = [1] * (1 << n)
    a[0] = -1
    return a


def bent_pairs(n):
    assert n % 2 == 0
    ans = []
    for x in range(1 << n):
        q = 0
        for i in range(0, n, 2):
            q ^= ((x >> i) & 1) & ((x >> (i + 1)) & 1)
        ans.append(-1 if q else 1)
    return ans


def majority(n):
    return [1 if x.bit_count() >= (n + 1) // 2 else -1 for x in range(1 << n)]


def tribes2(s):
    n = 2 * s
    ans = []
    for x in range(1 << n):
        ok = True
        for a in range(s):
            if (((x >> (2 * a)) & 1) | ((x >> (2 * a + 1)) & 1)) == 0:
                ok = False
                break
        ans.append(1 if ok else -1)
    return ans


getcontext().prec = 80
LN2 = Decimal(2).ln()


def dlog2(x):
    return x.ln() / LN2


def dphi(x):
    return Decimal(0) if x == 0 else -x * dlog2(x)


def onepoint_H_D(n):
    a = Decimal(2) ** Decimal(1 - n)
    return dphi((1 - a) ** 2) + (Decimal(2) ** n - 1) * dphi(a * a)


def onepoint_profile(n, r):
    a = Decimal(2) ** Decimal(1 - n)
    b = Decimal(2) ** Decimal(2 - n - r)
    heavy = Decimal(1) - (Decimal(2) ** r - 1) * b
    Hp = dphi(heavy) + (Decimal(2) ** r - 1) * dphi(b)
    F = (Decimal(2) ** Decimal(r - n)) * onepoint_H_D(r)
    J = Hp - F
    H = onepoint_H_D(n)
    I = Decimal(n) * a
    D = Decimal(n) / Decimal(r) * Hp - H
    return [
        H / I,
        Hp / I,
        F / I,
        J / I,
        D / I,
        (Decimal(n) / Decimal(r)) * J / I,
        (Decimal(n) / Decimal(r)) * Hp / I,
    ]


def pstar(C_minus_c):
    lo = 1e-12
    hi = 0.5
    for _ in range(100):
        m = (lo + hi) / 2
        h = -m * log2(m) - (1 - m) * log2(1 - m)
        if h / m > C_minus_c:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


if __name__ == "__main__":
    cinf = 2 / log(2)
    c2 = 8 - 2.5 * log2(5)
    print("constants", f"Cinf={cinf:.15f}", f"C2={c2:.15f}")
    print(
        "thresholds",
        f"pstar_ext_CminusCinf={pstar(C_EXT - cinf):.15f}",
        f"pstar_ext_CminusC2={pstar(C_EXT - c2):.15f}",
        f"pstar_7_CminusCinf={pstar(C_TEST - cinf):.15f}",
    )
    print("onepoint_profile columns=H/I,Hproj/I,F/I,J/I,D/I,(n/r)J/I,(n/r)Hproj/I")
    for n, r in [(16, 2), (32, 16), (64, 2), (64, 32), (64, 63), (128, 64)]:
        xs = onepoint_profile(n, r)
        print("onepoint", n, r, *[f"{float(x):.9f}" for x in xs])
    print(
        "bent_obstruction: for n=2m and R choosing one endpoint from r distinct quadratic pairs, "
        "D_r=0, F_R=0, J_R=r, H/I=2 exactly"
    )
    tests = [
        ("onepoint4", 4, onepoint(4)),
        ("onepoint6", 6, onepoint(6)),
        ("bent4", 4, bent_pairs(4)),
        ("bent6", 6, bent_pairs(6)),
        ("majority5", 5, majority(5)),
        ("tribes2x3", 6, tribes2(3)),
        ("tribes2x4", 8, tribes2(4)),
    ]
    for C in (C_EXT, C_TEST):
        print("restriction_credit_target", f"C={C:.15f}")
        for name, n, vals in tests:
            for r in sorted(set((max(1, n // 2), n - 1))):
                H, rhs, gap = credit_rhs(vals, n, r, C)
                print(name, n, r, f"H={H:.12f}", f"rhs={rhs:.12f}", f"gap={gap:.12f}")
