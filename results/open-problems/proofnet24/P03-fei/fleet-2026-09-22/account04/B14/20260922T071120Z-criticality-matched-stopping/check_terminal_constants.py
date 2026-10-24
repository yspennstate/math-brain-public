import math


def h2(p):
    if p in (0.0, 1.0):
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def sigma(K):
    lo, hi = 0.0, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if h2(m) > K * m:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def delta(K):
    return math.log2(1 + 2 ** (-K)) / K


Ks = [3.0, 4.0, 5.0, 6.521851214, 6.521851214 - 2 / math.log(2)]
for K in Ks:
    s = sigma(K)
    q = 1 / (1 + 2 ** K)
    d = delta(K)
    direct = h2(q) / K - q
    print(
        f"K={K:.15f} sigma={s:.15f} delta={d:.15f} "
        f"direct={direct:.15f} err={abs(d-direct):.3e}"
    )
