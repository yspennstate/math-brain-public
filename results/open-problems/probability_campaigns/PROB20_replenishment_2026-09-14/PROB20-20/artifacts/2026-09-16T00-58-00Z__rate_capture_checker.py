import math
from collections import defaultdict


def exact_hit_prob(q, U, r, x):
    """Exact P(exists s<=r: partial sum>=x and all increments through hit <=U)."""
    alive = {0: 1.0}
    hit = 0.0
    for _ in range(r):
        nxt = defaultdict(float)
        for z, pz in alive.items():
            for k, pk in q.items():
                if k > U:
                    continue
                zz = z + k
                if zz >= x:
                    hit += pz * pk
                else:
                    nxt[zz] += pz * pk
        alive = dict(nxt)
    return hit


def rate_envelope(q, U):
    return min(-math.log(pk) / k for k, pk in q.items() if 1 <= k <= U and pk > 0)


def rate_bound(q, U, r, x):
    a = rate_envelope(q, U)
    d = r / x
    if a <= d:
        return a, 1.0, "trivial a<=r/x"
    log_upper = math.log(r) - a*x + r + r*math.log(x/r)
    return a, min(1.0, math.exp(log_upper)), log_upper


def check_case(name, q, U, r, x):
    assert abs(sum(q.values()) - 1.0) < 1e-12
    p = exact_hit_prob(q, U, r, x)
    a, ub, meta = rate_bound(q, U, r, x)
    ok = p <= ub + 1e-12
    return dict(name=name, p=p, upper=ub, a=a, U=U, r=r, x=x, ok=ok, meta=meta)


cases = [
    ("geometric_like_A", {1:.5,2:.25,3:.125,4:.0625,5:.03125,6:.015625,7:.0078125,8:.0078125}, 6, 2, 12),
    ("geometric_like_B", {1:.5,2:.25,3:.125,4:.0625,5:.03125,6:.015625,7:.0078125,8:.0078125}, 8, 2, 12),
    ("irregular_A", {1:.70,3:.15,7:.08,15:.05,30:.02}, 15, 3, 31),
    ("flat_dyadic", {1:.2,2:.2,4:.2,8:.2,16:.2}, 16, 3, 24),
]

results = [check_case(*c) for c in cases]

binom_checks = []
for h, p0, A in [(10, .2, 12), (20, .15, 20), (25, .1, 30)]:
    r = math.ceil(A*h)
    tail = 0.0
    for j in range(h):
        tail += math.comb(r,j)*(p0**j)*((1-p0)**(r-j))
    mu = r*p0
    delta = 1 - h/mu
    ch = math.exp(-mu*delta*delta/2) if 0 < delta < 1 else 1.0
    binom_checks.append((h,p0,A,r,tail,ch,tail <= ch + 1e-12))

print("RATE_ENVELOPE_CHECKS")
for x in results:
    print(x)
print("all_rate_bounds_pass =", all(x["ok"] for x in results))

print("\nBINOMIAL_CAPTURE_CHECKS")
for row in binom_checks:
    print(row)
print("all_binomial_bounds_pass =", all(row[-1] for row in binom_checks))
