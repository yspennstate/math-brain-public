# T021: is the per-level gain of the general read-once recursion bounded by (1 - P) I (a + 2 ln(1/I)) with a finite a?
# If so, r_L <= sum_l (I_l - I_{l+1})(a + 2 ln 1/I_l) <= int_0^1 (a + 2 ln 1/x) dx = a + 2 for every read-once formula.
# State space of a monotone (unate) path function: |c0| < 1, 0 < I <= 1 - |c0| (I = pivotal probability <= 2 min(p, 1-p)).
# gain(c0, I, P) = r' - r = stepP((c0, I, 0), P)[2] / (I P). Score A = gain / ((1 - P) I) - 2 ln(1/I).
import random, mpmath as mp
from q31_readonce_general import stepP
mp.mp.dps = 90
def score(c0, I, P):
    c0, I, P = mp.mpf(c0), mp.mpf(I), mp.mpf(P)
    g = stepP((c0, I, mp.mpf(0)), P)[2] / (I * P)
    return g / ((1 - P) * I) - 2 * mp.log(1 / I), g
random.seed(11); best = (-mp.inf, None); rows = []
def sample():
    I = 10 ** -random.uniform(0, 25)
    s = random.random()
    c0 = (1 - I) * (2 * random.random() - 1) if s < 0.5 else (random.choice([-1, 1]) * (1 - I) * (1 - 10 ** -random.uniform(0, 12)) if s < 0.75 else random.choice([-1, 1]) * 10 ** -random.uniform(0, 25))
    P = 1 - 10 ** -random.uniform(0, 12) if random.random() < 0.6 else random.random()
    return c0, I, P
for i in range(40000):
    c0, I, P = sample()
    if not (0 < P < 1) or abs(c0) + I > 1: continue
    A, g = score(c0, I, P)
    if A > best[0]: best = (A, (c0, I, P))
print("random scan, 40000 states: max A = %s at c0=%.6g I=%.6g P=%.12g" % (mp.nstr(best[0], 10), *best[1]))
# local refinement from the best few: coordinate search in (atanh-ish c0, log I, log(1-P))
def refine(x):
    c0, I, P = x; step = [0.5, 0.5, 0.5]; A = score(c0, I, P)[0]
    for it in range(300):
        improved = False
        for k in range(3):
            for sgn in (1, -1):
                y = [c0, I, P]
                if k == 0: y[0] = max(-1 + 1e-30, min(1 - 1e-30, c0 + sgn * step[0] * (1 - abs(c0) - I + 1e-30)))
                if k == 1: y[1] = I * 10 ** (sgn * step[1])
                if k == 2: y[2] = 1 - (1 - P) * 10 ** (sgn * step[2])
                if not (0 < y[2] < 1) or not (0 < y[1]) or abs(y[0]) + y[1] > 1: continue
                B = score(*y)[0]
                if B > A: A, (c0, I, P), improved = B, y, True
        if not improved: step = [s / 2 for s in step]
        if max(step) < 1e-4: break
    return A, (c0, I, P)
A, x = refine(best[1])
print("refined: max A = %s at c0=%.10g I=%.6g 1-P=%.6g" % (mp.nstr(A, 12), x[0], x[1], 1 - x[2]))
# the sup of A along the constant-P near-1 orbit (where the continuum value pi^2/2 comes from)
st = (mp.mpf(0), mp.mpf(1), mp.mpf(0)); d = mp.mpf("0.001"); worstorbit = -mp.inf
while st[1] > mp.mpf("1e-10"):
    worstorbit = max(worstorbit, score(st[0], st[1], 1 - d)[0]); st = stepP(st, 1 - d)
print("along P = 1 - 0.001 orbit: max A = %s" % mp.nstr(worstorbit, 10))
print("if A <= a everywhere, then sup_read-once D_k/I_k <= a + 2 =", mp.nstr(A + 2, 10))
