# n = 0 contraction ratio over two-point mixtures of four-preimage weight vectors q on the 3-simplex,
# subject to the entropy constraint E H(q) >= h0 = log 4 - 2c (c = log 9/8).
# Ratio R = E[(Au)^2] / E[sum_i p_i u_i^2] with the hand-derived n = 0 formulas.
import numpy as np, math, sys
from scipy.optimize import minimize
c = math.log(9/8); h0 = math.log(4) - 2*c
def H(q):
    q = np.clip(q, 1e-300, 1); return float(-(q*np.log(q)).sum())
def num(q):
    q0,q1,q2,q3 = q; return (q0+q2-q1-q3)**2
def den(q):
    q0,q1,q2,q3 = q
    a = q0+q1+q3; b = q1+q2; d = q0+q2+q3
    t = 0.0
    if a > 0: t += 0.5*(q0-q1-q3)**2/a
    if b > 0: t += 0.5*(q1-q2)**2/b
    if d > 0: t += 0.5*(q0+q2-q3)**2/d
    return t
def softmax(z):
    z = z - z.max(); e = np.exp(z); return e/e.sum()
def unpack(x):
    q = softmax(x[:4]); qq = softmax(x[4:8]); pi = 1/(1+math.exp(-max(-60.0, min(60.0, x[8])))); return q, qq, pi
def ratio(x):
    q, qq, pi = unpack(x)
    n = pi*num(q) + (1-pi)*num(qq); d = pi*den(q) + (1-pi)*den(qq)
    return n/d if d > 1e-12 else 0.0
def ent(x):
    q, qq, pi = unpack(x); return pi*H(q) + (1-pi)*H(qq)
def obj(x, lam=50.0):
    return -ratio(x) + lam*max(0.0, h0 - ent(x))**2 * 100
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
best = (-1, None)
for trial in range(150):
    x0 = rng.normal(size=9)*3
    r = minimize(obj, x0, method="Nelder-Mead", options=dict(maxiter=4000, xatol=1e-9, fatol=1e-12))
    x = r.x
    if ent(x) >= h0 - 1e-4 and ratio(x) > best[0]:
        best = (ratio(x), x.copy())
R, x = best
if x is None: raise SystemExit('no feasible two-point mixture found within tolerance')
q, qq, pi = unpack(x)
print(f"h0 = {h0:.6f}  (log4 - 2c)")
print(f"max ratio over two-point mixtures = {R:.6f}   entropy = {ent(x):.6f}")
print(f"pi = {pi:.4f}  q = {np.round(q,4)}  H = {H(q):.4f}  R(q) = {num(q)/max(den(q),1e-12):.4f}")
print(f"        q' = {np.round(qq,4)}  H = {H(qq):.4f}  R(q') = {num(qq)/max(den(qq),1e-12):.4f}")
# also: deterministic (one-point) maximum under H(q) >= h0
best1 = (-1, None)
for trial in range(150):
    x0 = rng.normal(size=4)*3
    f = lambda z: -(num(softmax(z))/max(den(softmax(z)),1e-12)) + 5000*max(0.0, h0 - H(softmax(z)))**2
    r = minimize(f, x0, method="Nelder-Mead", options=dict(maxiter=4000, xatol=1e-9, fatol=1e-12))
    q1 = softmax(r.x)
    if H(q1) >= h0 - 1e-4:
        v = num(q1)/max(den(q1),1e-12)
        if v > best1[0]: best1 = (v, q1)
print(f"one-point max ratio under H(q) >= h0: {best1[0]:.6f}  at q = {np.round(best1[1],4)}")
