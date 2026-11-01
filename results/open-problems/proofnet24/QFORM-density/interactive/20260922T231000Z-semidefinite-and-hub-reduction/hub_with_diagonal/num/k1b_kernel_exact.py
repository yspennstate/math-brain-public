try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Exact check of Lemma 2.2: J_a(t,sigma) = sup_{0<=f<=1, int f<=1} int f(x) 1{|ax+t|<1} |sigma - a x^2 - 2xt|^{-1/2} dx
#   = int_0^inf min(1, m(lam)) dlam,  m(lam) = |{x : |phi(x)| < lam^-2, |a x + t| < 1}|  (exact, explicit).
# With y = x + t/a:  |phi| < eps  <=>  y^2 in ((Delta - |a| eps)/a^2, (Delta + |a| eps)/a^2),  slab <=> |y| < 1/|a|.
import numpy as np
rng = np.random.default_rng(7)

def m_of_eps(eps, a, Delta):
    A = (Delta - abs(a)*eps)/a**2; B = (Delta + abs(a)*eps)/a**2
    cap = 1.0/abs(a)
    up = np.minimum(np.sqrt(np.maximum(B, 0.0)), cap); dn = np.minimum(np.sqrt(np.maximum(A, 0.0)), cap)
    return 2*np.maximum(up - dn, 0.0)

def J(a, Delta):
    lam = np.geomspace(1e-8, 1e12, 400001)
    mm = np.minimum(1.0, m_of_eps(lam**-2.0, a, Delta))
    # trapezoid in lam
    return np.trapezoid(mm, lam) if hasattr(np, 'trapezoid') else np.trapz(mm, lam)

worst = 0.0; worst_rec = None; worst2 = 0.0
for trial in range(3000):
    a = rng.choice([-1,1])*10**rng.uniform(-4, 0)
    Delta = rng.choice([-1,1])*10**rng.uniform(-9, 2)
    v = J(a, Delta)
    r = v/(9.05*abs(Delta)**-0.25)
    if r > worst:
        worst, worst_rec = r, (a, Delta, v)
    # also the sharper two-regime form
    if abs(Delta) >= a*a/16:
        b2 = 4*abs(Delta)**-0.25
    else:
        b2 = abs(a)**-0.5*(4 + 2*np.sqrt(2) + np.sqrt(2)*np.log(a*a/(8*abs(Delta))))
    worst2 = max(worst2, v/b2)
print("J_a depends on (a, Delta) only (t enters through Delta).", flush=True)
print("worst J/(9.05|Delta|^-1/4) =", round(worst, 4), "at a, Delta, J =", worst_rec, flush=True)
print("worst J/(two-regime bound) =", round(worst2, 4), flush=True)
# a = 0 limit comparison: J -> 2|t|^{-1/2}?  (Delta = t^2)
for t in [0.1, 0.5, 1.0]:
    for a in [1e-4, 1e-2]:
        print("t", t, "a", a, "J", round(J(a, t*t), 4), " 2|t|^-1/2 =", round(2*t**-0.5, 4), flush=True)
