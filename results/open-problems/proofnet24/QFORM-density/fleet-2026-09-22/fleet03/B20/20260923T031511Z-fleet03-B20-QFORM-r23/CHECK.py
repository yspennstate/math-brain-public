import math
import numpy as np

Cstar = 103680.0**(1.0/3.0)
partner = Cstar * 2.0**(7.0/6.0)
rankone = 16.0*math.sqrt(60.0)*2.0**0.25
assert partner < 105.463
assert rankone < 148.0

# Exact threshold algebra used in Corollary 4.1.
assert abs((1.5 - 1.0/(4.0*(2.0/9.0))) - 3.0/8.0) < 1e-14
assert abs((2.0/3.0)*(3.0/8.0) - 1.0/4.0) < 1e-14

def random_check(seed):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=3)
    v /= np.linalg.norm(v)
    lam = rng.uniform(0.05, 0.95)
    D = np.eye(3) - lam*np.outer(v,v)
    vals, vecs = np.linalg.eigh(D)
    Ds = vecs @ np.diag(np.sqrt(vals)) @ vecs.T
    Dis = vecs @ np.diag(1.0/np.sqrt(vals)) @ vecs.T

    E, _ = np.linalg.qr(rng.normal(size=(3,3)))
    e1, es, e0 = E[:,0], E[:,1], E[:,2]
    q = rng.uniform(0.05,0.95)
    T = np.outer(e1,e1) + q*np.outer(es,es)
    S1 = Ds @ T @ Ds
    S2 = D - S1

    W = rng.normal(size=(3,2))
    W -= np.outer(v, v@W)
    W, _ = np.linalg.qr(W)
    W = W[:,:2]

    d1 = np.linalg.det(W.T @ S1 @ W)
    d2 = np.linalg.det(W.T @ S2 @ W)
    x = float(v@e0)**2
    y = float(v@e1)**2
    z = float(v@es)**2
    m = 1.0-d1-d2

    errs = [
        np.linalg.norm(Dis@S1@Dis-T),
        np.linalg.norm(S1+S2-D),
        abs(d1-q*x),
        abs(d2-(1.0-q)*y),
        abs(m-((1.0-q)*x+q*y+z)),
    ]
    return max(errs)

mx = max(random_check(s) for s in range(100))
assert mx < 1e-11

print("partner_bound", partner)
print("rankone_bound", rankone)
print("max_random_normalform_error", mx)
print("QFORM_B20_R23_CHECK_PASS")
