#!/usr/bin/env python3
import itertools, math

C = 6.521851214


def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    N = len(a)
    return [x/N for x in a]


def find_c(r):
    mu = sum(r)
    if mu <= 1.0 + 1e-13:
        return None
    def g(c):
        prod = 1.0
        for x in r:
            prod *= 1.0-c*x
        return 1.0-c-prod
    lo, hi = 1e-14, 1.0
    for _ in range(120):
        mid = (lo+hi)/2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def qlaw(r):
    n = len(r)
    mu = sum(r)
    q = [0.0]*(1 << n)
    if mu <= 1.0 + 1e-13:
        for i, x in enumerate(r):
            q[1 << i] = x
        return q, None
    c = find_c(r)
    t = [c*x for x in r]
    for S in range(1, 1 << n):
        z = 1.0
        for i in range(n):
            z *= t[i] if (S >> i) & 1 else (1.0-t[i])
        q[S] = z/c
    return q, c


def entropy(p):
    return -sum(x*math.log2(x) for x in p if x > 0)


def kl(p, q):
    z = 0.0
    for x, y in zip(p, q):
        if x > 1e-15:
            if y <= 1e-15:
                return float("inf")
            z += x*math.log2(x/y)
    return z


def coarse_kl(p, q, n, degree):
    keep = [S for S in range(1, 1 << n) if S.bit_count() <= degree]
    pp = [p[S] for S in keep]
    qq = [q[S] for S in keep]
    pp.append(1.0-sum(pp))
    qq.append(1.0-sum(qq))
    return kl(pp, qq)


for n in range(1, 5):
    N = 1 << n
    total = 0
    max_id_err = 0.0
    min_comp_gap = float("inf")
    min_single_gap = float("inf")
    misses_single = 0
    misses_low2 = 0
    min_single_res = float("inf")
    min_low2_res = float("inf")
    first_single_miss = None

    for neg in itertools.combinations(range(N), N//2):
        vals = [1.0]*N
        for j in neg:
            vals[j] = -1.0

        a = fwht(vals)
        p = [x*x for x in a]
        r = [sum(p[S] for S in range(1 << n) if (S >> i) & 1)
             for i in range(n)]
        mu = sum(r)
        H = entropy(p)
        q, c = qlaw(r)
        Hmax = entropy(q)
        K = Hmax-H

        if c is None:
            comp = 0.0
        else:
            t = [c*x for x in r]
            prod = 1.0
            for x in t:
                prod *= x*(1.0-x)
            comp = prod/(c*c*math.log(2.0))

        direct = kl(p, q)
        max_id_err = max(max_id_err, abs(K-direct))
        sing = coarse_kl(p, q, n, 1)
        low2 = coarse_kl(p, q, n, 2)
        min_comp_gap = min(min_comp_gap, K-comp)
        min_single_gap = min(min_single_gap, K-sing)

        Rbase = C*(mu-1.0)-Hmax
        rs = Rbase+max(comp, sing)
        r2 = Rbase+max(comp, low2)
        min_single_res = min(min_single_res, rs)
        min_low2_res = min(min_low2_res, r2)

        if rs < -1e-10:
            misses_single += 1
            if first_single_miss is None:
                first_single_miss = (neg, mu, H, Hmax, K, comp, sing, rs)
        if r2 < -1e-10:
            misses_low2 += 1
        total += 1

    print(
        f"n={n} balanced={total} max_identity_error={max_id_err:.3e} "
        f"min_K_minus_comp={min_comp_gap:.12g} "
        f"min_K_minus_single={min_single_gap:.12g} "
        f"single_bound_misses={misses_single} "
        f"min_single_residual={min_single_res:.12g} "
        f"low2_bound_misses={misses_low2} "
        f"min_low2_residual={min_low2_res:.12g}"
    )
    if first_single_miss is not None:
        neg, mu, H, Hmax, K, comp, sing, rs = first_single_miss
        print(
            " first_single_miss",
            "negative_vertices="+str(neg),
            f"I={mu:.12g}", f"H={H:.12g}", f"Hmax={Hmax:.12g}",
            f"Kocc={K:.12g}", f"comp={comp:.12g}",
            f"singleKL={sing:.12g}", f"bound_residual={rs:.12g}"
        )

print("PASS")
