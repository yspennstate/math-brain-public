"""Family (e) near the cone and away from it: one or two heavy coordinates + Gaussian rest, (1,1,-1) and (1,1,1).
Conditioning on the heavy coordinates (Gauss-Legendre), exact surface integrals for the Gaussian part."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, time
from famE_semi import gcs_density, SIG

t0 = time.time()


def cond_params_k(xs, rhos, lam, b):
    """heavy coordinates x (k,), rows rhos (k,3); G ~ N(0, sig^2 (I - sum rho rho^T))."""
    L = np.diag(lam); P = sum(np.outer(r, r) for r in rhos)
    SG = SIG**2*(np.eye(3) - P)
    ev, EV = np.linalg.eigh(SG); S = EV @ np.diag(np.sqrt(np.maximum(ev, 0))) @ EV.T
    y0 = sum(x*r for x, r in zip(xs, rhos))
    M = S @ L @ S; g = S @ (L @ y0 + b/2); qq = y0 @ L @ y0 + b @ y0
    th, U = np.linalg.eigh(M); gp = U.T @ g
    return th, gp/th, qq - np.sum(gp*gp/th)


def density_k(svals, rhos, lam, b=np.zeros(3), nx=20):
    gx, gw = np.polynomial.legendre.leggauss(nx); xs = gx/2; ws = gw/2
    out = np.zeros(len(svals)); k = len(rhos)
    if k == 1:
        for x, wt in zip(xs, ws):
            th, mv, q = cond_params_k([x], rhos, lam, b); out += wt*gcs_density(svals, th, mv, q)
    else:
        for x0, w0 in zip(xs, ws):
            for x1, w1 in zip(xs, ws):
                th, mv, q = cond_params_k([x0, x1], rhos, lam, b); out += w0*w1*gcs_density(svals, th, mv, q)
    return out


sneg = -np.array([1e-4, 3e-3, 1e-2, 3e-2, 1e-1, 2e-1]); spos = np.array([1e-4, 1e-2, 5e-2])
print("s values:", list(sneg), list(spos), flush=True)
for lamv, name in (([1, 1, -1], '(1,1,-1)'), ([1, 1, 1], '(1,1,1)')):
    lam = np.array(lamv, float)
    sv = np.concatenate([sneg, spos]) if lamv[2] < 0 else np.array([0.02, 0.05, 0.08, 0.12, 0.2, 0.3])
    print(f"{name} Gaussian  : {np.round(density_k(sv, [np.zeros(3)], lam, nx=2), 4)}", flush=True)
    for axis in (0, 2):
        for lev in (0.1, 0.3, 0.6, 0.9):
            rho = np.zeros(3); rho[axis] = np.sqrt(lev)
            print(f"{name} one heavy, lev {lev} on axis {axis}: {np.round(density_k(sv, [rho], lam), 4)}  t={time.time()-t0:.0f}", flush=True)
    # two heavy coordinates forming a pair sum along one axis: rows (r/sqrt2) e_axis each
    for axis in (0, 2):
        for lev in (0.5, 0.9):
            r = np.zeros(3); r[axis] = np.sqrt(lev/2)
            print(f"{name} pair-sum heavy (X0+X1) lev {lev} on axis {axis}: {np.round(density_k(sv, [r, r.copy()], lam, nx=14), 4)}  t={time.time()-t0:.0f}", flush=True)
    # two heavy coordinates on two different axes (pair of heavy directions)
    r0 = np.zeros(3); r0[0] = np.sqrt(0.6); r1 = np.zeros(3); r1[2] = np.sqrt(0.6)
    print(f"{name} heavy on axes 0 and 2 (lev .6 each): {np.round(density_k(sv, [r0, r1], lam, nx=14), 4)}  t={time.time()-t0:.0f}", flush=True)
