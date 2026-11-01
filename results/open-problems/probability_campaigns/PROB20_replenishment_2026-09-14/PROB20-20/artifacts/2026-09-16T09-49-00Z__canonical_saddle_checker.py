#!/usr/bin/env python3
"""
PROB20-20 finite bookkeeping checker for the moving-tilt / capped-canonical
identities. This is not evidence for the universal asymptotic conjecture.

Checks on several finite toy laws:
  * exact capped exponential-tilt coefficient identity;
  * KL = Legendre-cost identity;
  * theta > s in examples chosen to mimic the asymptotic regime;
  * monotonic truncated log-mean bound at s;
  * exact band first-moment decomposition;
  * exact saddle-separation inequality
        (theta-s) U >= log(L B(theta)/B'(s));
  * band probability and variance elementary inequalities.
"""
import math
from collections import defaultdict

def bisect_mean(fn, target):
    lo, hi = 0.0, 1.0
    while fn(hi) < target:
        hi *= 2.0
        if hi > 100:
            raise RuntimeError("failed to bracket")
    for _ in range(220):
        mid = 0.5*(lo+hi)
        if fn(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)

def conv_prob(prob, n, m):
    dp = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for s,p in dp.items():
            for k,pk in prob.items():
                if s+k <= m:
                    nxt[s+k] += p*pk
        dp = nxt
    return dp.get(m, 0.0)

def run_case(name, prob, L, U, n, m, mu):
    tail = sum(p for k,p in prob.items() if k > L)
    def M(t):
        return tail + sum(p*math.exp(t*k) for k,p in prob.items() if k <= L)
    def Mp(t):
        return sum(k*p*math.exp(t*k) for k,p in prob.items() if k <= L)
    theta = bisect_mean(lambda t: Mp(t)/M(t), mu)

    def F(t):
        return sum(p*math.exp(t*k) for k,p in prob.items() if k <= U)
    def Fp(t):
        return sum(k*p*math.exp(t*k) for k,p in prob.items() if k <= U)
    lam = m/n
    s = bisect_mean(lambda t: Fp(t)/F(t), lam)

    def B(t):
        return sum(p*math.exp(t*k) for k,p in prob.items() if L < k <= U)
    def Bp(t):
        return sum(k*p*math.exp(t*k) for k,p in prob.items() if L < k <= U)

    fs = F(s)
    can = {k:p*math.exp(s*k)/fs for k,p in prob.items() if k <= U}
    exact = conv_prob({k:p for k,p in prob.items() if k <= U}, n, m)
    tilted_local = conv_prob(can, n, m)
    rhs = math.exp(-s*m)*(fs**n)*tilted_local

    I = lam*s - math.log(fs)
    KL = sum(pk*math.log(pk/prob[k]) for k,pk in can.items() if pk > 0)

    low_log_mean_s = Mp(s)/M(s)
    band_decomp_error = abs(Bp(s) - (lam*fs - Mp(s)))
    separation_slack = (theta-s)*U - math.log((L*B(theta))/Bp(s))

    pband = B(s)/fs
    band_first_can = Bp(s)/fs
    var = sum((k-lam)**2*pk for k,pk in can.items())

    assert theta > s
    assert low_log_mean_s <= mu + 1e-12
    assert abs(exact-rhs) < 1e-12
    assert abs(I-KL) < 1e-12
    assert band_decomp_error < 1e-12
    assert separation_slack > -1e-12
    assert pband + 1e-12 >= band_first_can/U
    assert pband <= band_first_can/L + 1e-12
    assert var + lam*lam + 1e-12 >= L*band_first_can

    return {
        "name": name,
        "theta": theta,
        "s": s,
        "exact_tilt_error": abs(exact-rhs),
        "kl_error": abs(I-KL),
        "low_mean_margin": mu-low_log_mean_s,
        "band_decomp_error": band_decomp_error,
        "separation_slack": separation_slack,
        "pband": pband,
        "band_first_can": band_first_can,
        "variance": var,
    }

CASES = [
    ("toy-A", {0:.45,1:.35,4:.12,9:.08}, 4, 9, 8, 20, 1.25),
    ("toy-B", {0:.50,1:.25,3:.15,8:.07,14:.03}, 3, 14, 10, 25, 0.90),
    ("toy-C", {0:.55,1:.20,5:.15,12:.07,20:.03}, 5, 20, 12, 36, 1.10),
]

results = [run_case(*c) for c in CASES]
for r in results:
    print(r["name"])
    for k,v in r.items():
        if k != "name":
            print(f"  {k}: {v:.15g}")
print("PASS")
