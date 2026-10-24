"""Constants for the logarithmic union theorem (unions of regular functions, overlap k).
H/I <= h 2.886 + vacuum 1.443 + (1+a) log k + beta + 2 log 3 + log(ea/(a-1)) + 1 + log(2e) + E_nu G
E_nu G <= int_0^inf min(1, kB e^{-u ln2/(4a)} + k g(u/2)) du
g(v) = sup_{b >= v} phi_{l(b)}(2^{1-b}) [b > beta], l(b) = ceil(b/beta) - 2, phi_0(x) = x, phi_l(x) = x(2e ln(1/x)/l)^l."""
import numpy as np, math
LN2 = math.log(2); B = 3 * math.sqrt(3 / math.pi)
def phi_b(l, b):
    # phi_l(2^{1-b}) computed in log space
    lx = (1 - b) * LN2
    if l == 0:
        return math.exp(lx)
    return math.exp(lx + l * math.log(2 * math.e * (-lx) / l))
def envelope(beta, bmax=4000.0, step=0.01):
    bs = np.arange(0.0, bmax, step)
    val = np.zeros_like(bs)
    for i, b in enumerate(bs):
        if b <= beta: continue
        l = math.ceil(b / beta) - 2
        val[i] = phi_b(l, b)
    env = np.maximum.accumulate(val[::-1])[::-1]
    return bs, env
def EG(k, a, beta, env_cache={}):
    key = beta
    if key not in env_cache: env_cache[key] = envelope(beta)
    bs, env = env_cache[key]
    us = np.arange(0.0, 6000.0, 0.02)
    gv = np.interp(us / 2, bs, env, right=0.0)
    integrand = np.minimum(1.0, k * B * np.exp(-us * LN2 / (4 * a)) + k * gv)
    return float(np.trapezoid(integrand, us))
def CF(k, a, beta):
    return 2.886 + 1.443 + (1 + a) * math.log2(k) + beta + 2 * math.log2(3) + math.log2(math.e * a / (a - 1)) + 1 + math.log2(2 * math.e) + EG(k, a, beta)
ks = [1, 2, 3, 4, 5, 8, 10, 16, 32, 100, 1000, 10**4, 10**6]
grid_a = [1.2, 1.44, 1.7, 2.0, 2.5]; grid_b = [5, 6, 8, 10, 12, 16, 20]
best = {}
for k in ks:
    best[k] = min((CF(k, a, b), a, b) for a in grid_a for b in grid_b)
    print(f"k={k:8d}: union FEI constant {best[k][0]:8.2f} (a={best[k][1]}, beta={best[k][2]})  old {3.9 + 21.2 * k:10.1f}", flush=True)
# fixed parameters for a clean statement
for a, b in [(1.44, 10), (2.0, 10), (2.0, 12), (1.7, 12)]:
    vals = [CF(k, a, b) for k in ks]
    lk = np.log2(np.array(ks, float))
    for A0 in (60, 70, 80):
        Bc = max((v - A0) / l for v, l in zip(vals, lk) if l > 0)
        ok1 = vals[0] <= A0
        print(f"a={a} beta={b}: C(k) <= {A0} + {Bc:.2f} log2 k (k=1 ok: {ok1}, C(1)={vals[0]:.1f})")
