import math
from collections import defaultdict


def conv_dist(pi, n):
    d = {0: 1.0}
    for _ in range(n):
        nd = defaultdict(float)
        for s, ps in d.items():
            for k, pk in pi.items():
                nd[s + k] += ps * pk
        d = dict(nd)
    return d


def check(pi, n, m):
    nu = sum(k * p for k, p in pi.items())
    lam = m / n
    pn = conv_dist(pi, n)
    pn1 = conv_dist(pi, n - 1)
    p = pn.get(m, 0.0)
    if p <= 0 or nu <= 0:
        raise ValueError("need positive conditioning atom and mean")

    b = -math.log(p)
    c = sum(v for s, v in pn1.items() if s <= m)
    qbar = {k: (k * pk / nu if k > 0 else 0.0) for k, pk in pi.items()}

    R = {}
    for k in range(m + 1):
        rv = pn1.get(m - k, 0.0) / c
        if rv > 0:
            R[k] = rv

    mu = {}
    for k, pk in pi.items():
        if 0 < k <= m:
            v = (k * pk * pn1.get(m - k, 0.0)) / (lam * p)
            if v > 0:
                mu[k] = v

    D = 0.0
    H = 0.0
    for k, muk in mu.items():
        D += muk * math.log(muk / R[k])
        H += muk * (-math.log(qbar[k]))

    normalizer_term = math.log(lam / (nu * c))
    rhs = D + H + normalizer_term
    Z = lam * p / (nu * c)
    tilt_errors = [abs(muk - qbar[k] * R[k] / Z) for k, muk in mu.items()]

    return {
        "nu": nu,
        "lambda": lam,
        "p_cond": p,
        "b": b,
        "c": c,
        "mu_sum": sum(mu.values()),
        "R_sum": sum(R.values()),
        "D": D,
        "Hq": H,
        "normalizer_term": normalizer_term,
        "split_error": abs(b - rhs),
        "tilt_max_error": max(tilt_errors) if tilt_errors else 0.0,
    }


tests = [
    ({0: 0.45, 1: 0.25, 2: 0.18, 4: 0.12}, 6, 8),
    ({0: 0.55, 1: 0.20, 3: 0.15, 7: 0.10}, 7, 10),
    ({0: 0.40, 1: 0.30, 2: 0.10, 5: 0.12, 9: 0.08}, 8, 12),
]

for i, (pi, n, m) in enumerate(tests, 1):
    out = check(pi, n, m)
    print(f"case {i}: n={n} m={m}")
    for key, value in out.items():
        print(f"  {key}={value:.16g}")
    print()
