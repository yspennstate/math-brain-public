"""Family (e): convex side of rank three with mixed leverage, semi-Gaussian model.
Y = X0 rho + G in R^3, X0 one coordinate (law f0, default uniform[-1/2,1/2]), G ~ N(0, sig^2 (I - rho rho^T)) (the spread
coordinates), Q = Y^T diag(lam) Y + b.Y + c0 X0.  Given X0 = x, Q is a noncentral generalised chi-square in 3 Gaussian
dimensions; its density is computed EXACTLY by a surface integral (sphere for definite, hyperboloid sheets otherwise),
then averaged over x by Gauss-Legendre.  Best response for X0: top measure-one set of g0(x) = p(s | X0 = x)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from scipy.optimize import minimize

SIG = np.sqrt(1/12)
_ct, _cw = np.polynomial.legendre.leggauss(40)
NPHI = 72
_phi = (np.arange(NPHI) + 0.5)*2*np.pi/NPHI
_et, _ew = np.polynomial.legendre.leggauss(40)


def gcs_density(svals, theta, m, q):
    """density at svals of sum_k theta_k (Z_k + m_k)^2 + q, Z iid N(0,1), all theta_k != 0 (3 of them)."""
    svals = np.atleast_1d(svals)
    th = np.asarray(theta, float); m = np.asarray(m, float)
    pos = th > 0
    out = np.zeros(len(svals))
    sq = np.sqrt(np.abs(th))
    norm = 1/np.prod(sq)/(2*np.pi)**1.5
    npos = int(pos.sum())
    # orient so that the 'odd' sign is last: npos = 3 or 0 definite; npos = 2 -> (+,+,-); npos = 1 -> (-,-,+) = -(+,+,-)
    if npos in (0, 1):
        return _flip(svals, th, m, q)
    order = np.argsort(~pos, kind='stable')          # positives first
    th = th[order]; m = m[order]; sq = sq[order]
    for i, s in enumerate(svals):
        d = s - q
        if npos == 3:
            if d <= 0: continue
            r = np.sqrt(d)
            ct = _ct[:, None]; st = np.sqrt(1 - ct*ct)
            om = np.stack([st*np.cos(_phi)[None, :], st*np.sin(_phi)[None, :], np.broadcast_to(ct, (len(_ct), NPHI))])
            W = r*om
            expo = -0.5*sum((W[k]/sq[k] - m[k])**2 for k in range(3))
            integ = np.exp(expo)
            val = (integ*_cw[:, None]).sum()*(2*np.pi/NPHI)
            out[i] = 0.5*r*norm*val
        else:                                          # (+,+,-): W1^2 + W2^2 - W3^2 = d
            r = np.sqrt(abs(d))
            if d < 0:                                  # two sheets: W = (r sinh e cos f, r sinh e sin f, +- r cosh e)
                emax = np.arccosh(max(1.0, (12 + abs(m[2]))*sq[2]/max(r, 1e-12))) + 0.5
                e = (_et + 1)/2*emax; we = _ew/2*emax
                tot = 0.0
                for sgn in (1, -1):
                    W1 = r*np.sinh(e)[:, None]*np.cos(_phi)[None, :]; W2 = r*np.sinh(e)[:, None]*np.sin(_phi)[None, :]
                    W3 = sgn*r*np.cosh(e)[:, None]*np.ones((1, NPHI))
                    expo = -0.5*((W1/sq[0] - m[0])**2 + (W2/sq[1] - m[1])**2 + (W3/sq[2] - m[2])**2)
                    tot += (np.exp(expo)*np.sinh(e)[:, None]*we[:, None]).sum()*(2*np.pi/NPHI)
                out[i] = 0.5*r*norm*tot
            else:                                      # one sheet: W = (r cosh e cos f, r cosh e sin f, r sinh e)
                emax = np.arcsinh((12 + abs(m[2]))*sq[2]/max(r, 1e-12)) + 0.5
                e = _et*emax; we = _ew*emax
                W1 = r*np.cosh(e)[:, None]*np.cos(_phi)[None, :]; W2 = r*np.cosh(e)[:, None]*np.sin(_phi)[None, :]
                W3 = r*np.sinh(e)[:, None]*np.ones((1, NPHI))
                expo = -0.5*((W1/sq[0] - m[0])**2 + (W2/sq[1] - m[1])**2 + (W3/sq[2] - m[2])**2)
                out[i] = 0.5*r*norm*(np.exp(expo)*np.cosh(e)[:, None]*we[:, None]).sum()*(2*np.pi/NPHI)
    return out


def _flip(svals, th, m, q):
    # Q = sum th (Z+m)^2 + q ; -Q = sum (-th)(Z+m)^2 - q ; p_Q(s) = p_{-Q}(-s)
    return gcs_density(-np.atleast_1d(svals), -th, m, -q)


def cond_params(x, rho, lam, b, c0, sig=SIG):
    """Given X0 = x: Q = Z^T M Z + 2 g.Z + qq with Z ~ N(0, I3); return (theta, mvec, q) of the diagonal form."""
    rho = np.asarray(rho, float); L = np.diag(lam)
    SG = sig*sig*(np.eye(3) - np.outer(rho, rho))
    ev, EV = np.linalg.eigh(SG); S = EV @ np.diag(np.sqrt(np.maximum(ev, 0))) @ EV.T
    M = S @ L @ S
    g = S @ (L @ (x*rho) + b/2)
    qq = x*x*rho @ L @ rho + x*(b @ rho) + c0*x
    th, U = np.linalg.eigh(M)
    gp = U.T @ g
    mvec = gp/th
    return th, mvec, qq - np.sum(gp*gp/th)


def density(svals, rho, lam, b, c0, f0=None, nx=32):
    """p_Q(s), X0 ~ f0 given as list of intervals [(a,b), ...] with density 1 (default [(-.5,.5)])."""
    f0 = [(-0.5, 0.5)] if f0 is None else f0
    svals = np.atleast_1d(svals); out = np.zeros(len(svals))
    gx, gw = np.polynomial.legendre.leggauss(nx)
    for (a, bb) in f0:
        xs = (gx + 1)/2*(bb - a) + a; ws = gw/2*(bb - a)
        for x, wt in zip(xs, ws):
            th, mv, q = cond_params(x, rho, lam, b, c0)
            out += wt*gcs_density(svals, th, mv, q)
    return out


def g0(x, s, rho, lam, b, c0):
    th, mv, q = cond_params(x, rho, lam, b, c0)
    return gcs_density([s], th, mv, q)[0]


if __name__ == "__main__":
    t0 = time.time()
    # checks: rho = 0 -> fully Gaussian; (1,1,-1) at s -> 0-: 3 sqrt 2 = 4.2426 ; (1,1,1) max = 12*0.2420 = 2.904
    print("Gauss (1,1,-1) p(-1e-3), p(-0.05):", density([-1e-3, -0.05], [0, 0, 0], [1, 1, -1], np.zeros(3), 0.0, nx=4), flush=True)
    print("Gauss (1,1,-1) one-sheet p(1e-3):", density([1e-3], [0, 0, 0], [1, 1, -1], np.zeros(3), 0.0, nx=4), flush=True)
    ss = np.linspace(0.02, 0.4, 20)
    pv = density(ss, [0, 0, 0], [1, 1, 1], np.zeros(3), 0.0, nx=4)
    print("Gauss (1,1,1) max:", pv.max(), "at", ss[np.argmax(pv)], " (exact 12*0.24197=2.9037 at s=1/12)", flush=True)
    # mixed leverage example: rho = (1,0,0)*0.9 definite
    pv = density(ss, [0.9, 0, 0], [1, 1, 1], np.zeros(3), 0.0)
    print("rho=(.9,0,0) definite max:", pv.max(), "at", ss[np.argmax(pv)], " t", time.time()-t0, flush=True)
