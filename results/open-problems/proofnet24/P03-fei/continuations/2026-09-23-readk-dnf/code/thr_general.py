# Thresholds T_{t,r} under NON-identical product measures: exact (50 digits) ratios
#  r2 = (W ln(1/W) - sum_i J_i ln+(4 v_i / W)) / J      (J-credit inequality)
#  fp = LHS+ / J  (nats),  fb = LHS+/(I - V) in bits
import mpmath as mp, random, sys, math
from isoper3 import biased_P
mp.mp.dps = 50
def run(r, t, q):
    f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q)
    sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    V = mp.fsum(P[1:]); W = mp.fsum(P[A] for A in range(1, 1 << r) if bin(A).count('1') >= 2)
    I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r))
    J = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r) if bin(A).count('1') >= 2)
    Inf = [mp.fsum(P[A] for A in range(1 << r) if A >> i & 1) for i in range(r)]
    Ji = [Inf[i] - P[1 << i] for i in range(r)]
    lhs = mp.fsum(P[A] * mp.log(mp.fprod(sig2[i] for i in range(r) if A >> i & 1) / P[A]) for A in range(1, 1 << r) if P[A] > 0)
    out = {}
    if W > 0 and J > 0:
        cred = mp.fsum(Ji[i] * max(0, mp.log(4 * (Ji[i] / sig2[i]) / W)) for i in range(r) if Ji[i] > 0)
        out['r2'] = float((W * mp.log(1 / W) - cred) / J)
        out['fp'] = float(lhs / J)
    if I > V: out['fb'] = float(lhs / (I - V) / mp.log(2))
    out['fI'] = float(lhs / I)
    return out
rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); rmax = int(sys.argv[3])
best = {}
for trial in range(T):
    r = rng.randint(2, rmax); t = rng.randint(1, r)
    q = []
    for _ in range(r):
        u = rng.random()
        q.append(10 ** -rng.uniform(0, 14) if u < 0.35 else (1 - 10 ** -rng.uniform(0, 14) if u < 0.7 else rng.uniform(0.02, 0.98)))
    q = [min(max(v, 1e-15), 1 - 1e-15) for v in q]
    o = run(r, t, q)
    for k, v in o.items():
        if k not in best or v > best[k][0]:
            best[k] = (v, r, t, ['%.3g' % x for x in q])
    if trial % 300 == 0: print(trial, {k: round(v[0], 3) for k, v in best.items()}, flush=True)
for k, v in best.items(): print('WORST', k, v)
