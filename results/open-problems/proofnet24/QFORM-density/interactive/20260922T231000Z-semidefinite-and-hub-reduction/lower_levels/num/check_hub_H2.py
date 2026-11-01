try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(3)

# X_h uniform on a union of intervals (lefts), each of length ell; total mass 1.
def interval_len_where(a, l, r, s, u, lefts, ell):
    # measure of {x in union : |a x^2 + 2 l x + r - s| <= u}, vectorized over samples (l, r arrays)
    # solve a x^2 + 2 l x + (r - s) = +-u; set where g in [s-u, s+u] is union of <= 2 intervals
    tot = np.zeros_like(l)
    def roots(cst):
        # roots of a x^2 + 2 l x + cst = 0
        if a == 0:
            with np.errstate(divide='ignore', invalid='ignore'):
                x = -cst/(2*l)
            return x, x, np.ones_like(l, dtype=bool)
        disc = l*l - a*cst
        ok = disc >= 0
        sq = np.sqrt(np.where(ok, disc, 0.0))
        x1 = (-l - sq)/a; x2 = (-l + sq)/a
        return np.minimum(x1, x2), np.maximum(x1, x2), ok
    lo_c = r - s - u   # g - (s+u) ... careful: g <= s+u  <=> a x^2+2lx + (r-s-u) <= 0
    hi_c = r - s + u   # g >= s-u  <=> a x^2+2lx + (r-s+u) >= 0
    for L0 in lefts:
        A0, B0 = L0, L0 + ell
        # sample the set via exact interval arithmetic: G(x) = g(x)-s; want -u <= G <= u
        # For a != 0: {G <= u} is interval [p1,p2] (a>0) or complement (a<0); {G >= -u} is complement of (q1,q2) (a>0)
        p1, p2, okp = roots(lo_c)
        q1, q2, okq = roots(hi_c)
        if a > 0:
            # {G<=u} = [p1,p2] if okp else empty ; {G>=-u} = R \ (q1,q2) if okq else R
            left = np.clip(np.minimum(np.where(okq, q1, p2), p2), A0, B0) - np.clip(p1, A0, B0)
            right = np.clip(p2, A0, B0) - np.clip(np.maximum(np.where(okq, q2, p1), p1), A0, B0)
            left = np.where(okq, np.maximum(left, 0), 0.0); right = np.where(okq, np.maximum(right, 0), 0.0)
            full = np.where(okp & ~okq, np.maximum(np.clip(p2, A0, B0) - np.clip(p1, A0, B0), 0), 0.0)
            tot += np.where(okp, left + right + full, 0.0)
        elif a < 0:
            # mirror: G(x) = -(|a| x^2 - 2 l x ...) ; use symmetry by negating: -G in [-u,u]
            raise NotImplementedError
        else:
            # affine: G = 2 l x + (r - s); interval of x of length u/|l| around (s-r)/(2l)
            c0 = (s - r)/(2*l); hw = u/(2*np.abs(l))
            tot += np.maximum(np.clip(c0 + hw, A0, B0) - np.clip(c0 - hw, A0, B0), 0)
    return tot

def H2_quantity(a, sampler, s, lefts, ell, N=40000):
    l, r = sampler(N)
    us = np.logspace(-9, 0, 91)
    P = np.array([interval_len_where(a, l, r, s, u, lefts, ell).mean() for u in us])
    # E[|Z|^{-1/2}; |Z|<=1] = P(|Z|<=1) + (1/2) int_0^1 u^{-3/2} P(u) du ; integrate on log grid, tail below 1e-9 bounded by P ~ Cu log
    integrand = 0.5*us**(-1.5)*P*us   # d(log u)
    val = P[-1] + np.trapezoid(integrand, np.log(us))
    return val, P

m = 60
w = np.ones(m)/np.sqrt(m)
def make_sampler(kind, a, theta=0.0, eps=0.0, W=None):
    def sampler(N):
        Xp = rng.uniform(-0.5, 0.5, size=(N, m))
        L = Xp @ w
        if kind == "pure":
            R = np.zeros(N)
        elif kind == "theta":
            R = theta*L*L
        elif kind == "dense":
            R = eps*np.einsum('ni,ij,nj->n', Xp, W, Xp)
        elif kind == "theta+dense":
            R = theta*L*L + eps*np.einsum('ni,ij,nj->n', Xp, W, Xp)
        return L, R
    return sampler

Wm = rng.normal(size=(m, m)); Wm = (Wm + Wm.T)/np.sqrt(2*m)
laws = {"uniform": ([-0.5], 1.0), "spread3": ([-0.5, 7.0, 40.0], 1.0/3)}
for lawname, (lefts, ell) in laws.items():
    print(f"X_h law: {lawname}", flush=True)
    for (kind, a, theta, eps) in [("pure", 0.0, 0, 0), ("pure", 0.01, 0, 0), ("pure", 0.1, 0, 0),
                                  ("theta", 0.01, 25.0, 0), ("theta", 0.01, 50.0, 0), ("theta", 0.01, 90.0, 0),
                                  ("dense", 0.01, 0, 1.0), ("dense", 0.05, 0, 3.0), ("theta+dense", 0.02, 20.0, 1.0)]:
        smp = make_sampler(kind, a, theta, eps, Wm)
        best = 0.0; bests = None
        for s in np.linspace(-3, 3, 25):
            v, _ = H2_quantity(a, smp, s, lefts, ell, N=20000)
            if v > best: best, bests = v, s
        # N-norm (hub theorem quantity) for this family: N = w w^T - a*M'
        if kind == "pure": Mp = np.zeros((m, m))
        elif kind == "theta": Mp = theta*np.outer(w, w)
        elif kind == "dense": Mp = eps*Wm
        else: Mp = theta*np.outer(w, w) + eps*Wm
        N_ = np.outer(w, w) - a*Mp
        No = N_ - np.diag(np.diag(N_))
        print(f"  {kind:12s} a={a:<5} theta={theta:<5} eps={eps:<4}  sup_s H2' ~ {best:.3f} at s={bests:.2f}   ||N_off|| = {np.linalg.norm(No,2):.3f}  1 - a*theta = {1-a*theta:.2f}", flush=True)
