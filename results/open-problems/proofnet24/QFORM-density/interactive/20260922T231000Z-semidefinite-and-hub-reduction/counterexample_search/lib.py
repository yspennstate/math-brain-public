"""Exact-conditional density estimators for Q(X) = X^T A X + b^T X + c, X with independent coordinates
having piecewise-constant densities <= 1.  No binning anywhere in E1/E2.

E2 (fibre identity over all coordinates):
   p(s) = sum_i E_{X_-i} sum_{roots D} f_i(X_i + D) |h'_i| / (2 |h'|^2),   h = A x + b/2 (half gradient)
E1 (one hub integrated exactly, everything else sampled):
   Q = a x_h^2 + 2 T x_h + R ;  p(s) = E sum_{roots x} f_h(x) / (2 sqrt(T^2 - a (R - s)))   (a != 0)
                                     = E f_h((s-R)/(2T)) / (2|T|)                          (a == 0)
"""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np


class PWLaw:
    """Piecewise-constant density on disjoint intervals [a_k, b_k) with heights c_k <= 1 (normalised)."""
    def __init__(self, a, b, c=None):
        a = np.atleast_1d(np.asarray(a, float)); b = np.atleast_1d(np.asarray(b, float))
        c = np.ones_like(a) if c is None else np.atleast_1d(np.asarray(c, float))
        o = np.argsort(a)
        self.a, self.b, c = a[o], b[o], c[o]
        assert np.all(self.b > self.a)
        assert np.all(self.a[1:] >= self.b[:-1] - 1e-12), "intervals overlap"
        mass = c * (self.b - self.a)
        tot = mass.sum()
        self.c = c / tot
        self.p = mass / tot
        self.cp = np.cumsum(self.p)
        assert self.c.max() <= 1 + 1e-9, "density exceeds 1"

    def sample(self, n, rng):
        u = rng.random(n)
        k = np.minimum(np.searchsorted(self.cp, u, side='right'), len(self.a) - 1)
        return self.a[k] + (self.b[k] - self.a[k]) * rng.random(n)

    def pdf(self, t):
        t = np.asarray(t, float)
        k = np.searchsorted(self.a, t, side='right') - 1
        kk = np.clip(k, 0, len(self.a) - 1)
        inside = (k >= 0) & (t < self.b[kk])
        return np.where(inside, self.c[kk], 0.0)

    def mean_var(self):
        m = np.sum(self.p * (self.a + self.b) / 2)
        e2 = np.sum(self.p * (self.a**2 + self.a*self.b + self.b**2) / 3)
        return m, e2 - m*m

    def shifted(self, d):
        return PWLaw(self.a + d, self.b + d, self.c)

    def desc(self, k=4):
        return [(round(x, 3), round(y, 3)) for x, y in zip(self.a[:k], self.b[:k])]


def U(center=0.0, width=1.0):
    return PWLaw([center - width/2], [center + width/2])


def comb(positions, total=1.0):
    positions = np.sort(np.asarray(positions, float)); d = total / len(positions)
    return PWLaw(positions - d/2, positions + d/2)


def sample_X(laws, m, rng):
    return np.column_stack([L.sample(m, rng) for L in laws])


def _roots(a, h, cc):
    """Roots D of a D^2 + 2 h D + cc = 0 ; a array (broadcast) ; returns list of (D, ok)."""
    a = np.broadcast_to(a, h.shape)
    lin = np.abs(a) < 1e-15
    disc = h*h - a*cc
    ok = (disc >= 0) & ~lin
    sq = np.sqrt(np.where(ok, disc, 0.0))
    qq = -(h + np.copysign(sq, h))
    with np.errstate(divide='ignore', invalid='ignore'):
        D1 = np.where(ok, qq / np.where(lin, 1.0, a), 0.0)
        D2 = np.where(ok & (qq != 0), cc / np.where(qq == 0, 1.0, qq), 0.0)
        Dl = np.where(lin & (h != 0), -cc / (2*np.where(h == 0, 1.0, h)), 0.0)
    okl = lin & (h != 0)
    return [(np.where(lin, Dl, D1), ok | okl), (D2, ok)]


def fibre_density(A, laws, svals, N=100000, b=None, c=0.0, rng=None, chunk=None, coords=None):
    """E2. Returns (mean, se) arrays over svals.  coords: restrict the partition of unity to a subset
    (then the estimator is for the SAME density only if the weights over coords sum to one, i.e. we use
    |grad_coords Q|^2 in the denominator)."""
    rng = np.random.default_rng(1) if rng is None else rng
    A = np.asarray(A, float); n = A.shape[0]
    b = np.zeros(n) if b is None else np.asarray(b, float)
    svals = np.atleast_1d(np.asarray(svals, float)); S = len(svals)
    dA = np.diag(A).copy(); A2 = A @ A; dA2 = np.diag(A2).copy()
    idx = np.arange(n) if coords is None else np.asarray(coords)
    gd = {}
    for jj, i in enumerate(idx):
        gd.setdefault(id(laws[i]), (laws[i], []))[1].append(jj)
    groups = [(L, np.array(cols)) for L, cols in gd.values()]
    if chunk is None:
        chunk = max(1000, min(50000, int(4e6 // max(n, 1))))
    tot = np.zeros(S); tot2 = np.zeros(S); done = 0
    while done < N:
        m = min(chunk, N - done)
        X = sample_X(laws, m, rng)
        H = X @ A + b/2                      # half gradient (A symmetric)
        Qv = np.einsum('ij,ij->i', X, X @ A) + X @ b + c
        if coords is None:
            AH = H @ A
            g2 = np.einsum('ij,ij->i', H, H)
        else:
            Hs = H[:, idx]
            AH = Hs @ A[np.ix_(idx, idx)]    # sum_{k in S} A_ki h_k for i in S
            g2 = np.einsum('ij,ij->i', Hs, Hs)
        Hi = H[:, idx]; ai = dA[idx]; a2i = dA2[idx] if coords is None else (A[np.ix_(idx, idx)]**2).sum(0)
        est = np.zeros((m, S))
        for si, s in enumerate(svals):
            cc = (Qv - s)[:, None]
            for D, ok in _roots(ai[None, :], Hi, np.broadcast_to(cc, Hi.shape)):
                t = X[:, idx] + D
                f = np.zeros_like(t)
                for L, cols in groups:
                    f[:, cols] = L.pdf(t[:, cols])
                f *= ok
                hi = Hi + D*ai[None, :]
                G2 = g2[:, None] + 2*D*AH + D*D*a2i[None, :]
                with np.errstate(divide='ignore', invalid='ignore'):
                    w = np.where(f > 0, f*np.abs(hi)/(2*G2), 0.0)
                est[:, si] += w.sum(1)
        tot += est.sum(0); tot2 += (est**2).sum(0); done += m
    mean = tot/N; var = tot2/N - mean**2
    return mean, np.sqrt(np.maximum(var, 0)/N)


def hub_TR(A, X, h, b=None, c=0.0):
    """For hub index h: T = A[h,-h].X' + b_h/2, R = X'^T M X' + b'.X' + c, and a = A[h,h]."""
    n = A.shape[0]; b = np.zeros(n) if b is None else b
    rest = np.array([j for j in range(n) if j != h])
    Xp = X[:, rest] if X.shape[1] == n else X
    M = A[np.ix_(rest, rest)]
    MX = Xp @ M
    T = Xp @ A[h, rest] + b[h]/2
    R = np.einsum('ij,ij->i', Xp, MX) + Xp @ b[rest] + c
    return A[h, h], T, R, Xp, MX, rest


def hub_cond_values(a, T, R, svals, fh):
    """E1 summand for each sample (rows) and each s (columns)."""
    svals = np.atleast_1d(svals)
    Tm = T[:, None]; Rm = R[:, None]; sm = svals[None, :]
    if abs(a) < 1e-15:
        with np.errstate(divide='ignore', invalid='ignore'):
            x = (sm - Rm) / (2*Tm)
            v = np.where(Tm != 0, fh.pdf(x) / (2*np.abs(Tm)), 0.0)
        return v
    disc = Tm*Tm - a*(Rm - sm)
    ok = disc > 0
    sq = np.sqrt(np.where(ok, disc, 0.0))
    x1 = (-Tm + sq)/a; x2 = (-Tm - sq)/a
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.where(ok, (fh.pdf(x1) + fh.pdf(x2)) / (2*np.where(ok, sq, 1.0)), 0.0)
    return v


def hub_density(A, laws, h, svals, N=200000, b=None, c=0.0, rng=None, chunk=None, return_samples=False):
    """E1 for hub h. Returns mean, se over svals."""
    rng = np.random.default_rng(2) if rng is None else rng
    A = np.asarray(A, float); n = A.shape[0]
    svals = np.atleast_1d(np.asarray(svals, float)); S = len(svals)
    if chunk is None:
        chunk = max(2000, min(100000, int(2e7 // max(n*n, S*50, 1))))
    tot = np.zeros(S); tot2 = np.zeros(S); done = 0
    rest_laws = [laws[j] for j in range(n) if j != h]
    while done < N:
        m = min(chunk, N - done)
        Xp = sample_X(rest_laws, m, rng)
        a, T, R, _, _, _ = hub_TR(A, Xp, h, b, c)
        v = hub_cond_values(a, T, R, svals, laws[h])
        tot += v.sum(0); tot2 += (v**2).sum(0); done += m
    mean = tot/N; var = tot2/N - mean**2
    return mean, np.sqrt(np.maximum(var, 0)/N)


def hist_density(A, laws, svals, widths, N=2000000, b=None, c=0.0, rng=None, chunk=200000):
    rng = np.random.default_rng(7) if rng is None else rng
    A = np.asarray(A, float); n = A.shape[0]; b = np.zeros(n) if b is None else b
    svals = np.atleast_1d(svals); widths = np.atleast_1d(widths)
    cnt = np.zeros((len(svals), len(widths))); done = 0
    while done < N:
        m = min(chunk, N - done)
        X = sample_X(laws, m, rng)
        Qv = np.einsum('ij,ij->i', X, X @ A) + X @ b + c
        for i, s in enumerate(svals):
            d = np.abs(Qv - s)
            for k, w in enumerate(widths):
                cnt[i, k] += np.count_nonzero(d < w/2)
        done += m
    p = cnt / N
    return p / widths[None, :], np.sqrt(p*(1-p)/N) / widths[None, :]


def top_set_law(g, edges, maxint=12):
    """Best response: indicator of the top measure-one superlevel set of g (on bins)."""
    bw = edges[1] - edges[0]; k = int(round(1.0/bw))
    order = np.argsort(-g); mask = np.zeros(len(g), bool); mask[order[:k]] = True
    act = np.nonzero(mask)[0]
    a = []; bb = []; start = act[0]; prev = act[0]
    for cidx in act[1:]:
        if cidx != prev + 1:
            a.append(edges[start]); bb.append(edges[prev+1]); start = cidx
        prev = cidx
    a.append(edges[start]); bb.append(edges[prev+1])
    return PWLaw(a, bb)


def smooth(g, w=1):
    if w <= 0:
        return g
    ker = np.ones(2*w+1)/(2*w+1)
    return np.convolve(g, ker, mode='same')


def spread_unit(n, rng, orth=()):
    v = rng.standard_normal(n)
    for u in orth:
        v -= (v @ u) * u
    return v / np.linalg.norm(v)


class GaussLaw:
    """Gaussian coordinate (used for the spread-leaf limit Y = B^T X', Y ~ N(mu, sigma^2))."""
    def __init__(self, sigma=np.sqrt(1/12), mu=0.0):
        self.s = float(sigma); self.m = float(mu)
        self.c = np.array([1/(self.s*np.sqrt(2*np.pi))])
    def sample(self, n, rng):
        return self.m + self.s*rng.standard_normal(n)
    def pdf(self, t):
        z = (np.asarray(t, float) - self.m)/self.s
        return np.exp(-0.5*z*z)/(self.s*np.sqrt(2*np.pi))


def mu3(A):
    ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
    return ev[2] if len(ev) >= 3 else 0.0


class FixedSampler:
    """Common random numbers: pre-drawn uniforms per coordinate so that re-evaluations with changed
    parameters (not laws) reuse the same X."""
    def __init__(self, laws, N, seed):
        rng = np.random.default_rng(seed)
        self.X = sample_X(laws, N, rng)


def fibre_density_v(A, laws, svals, N=100000, b=None, c=0.0, rng=None, X=None, elem=2_000_000):
    """E2 vectorised over (samples, coordinates, s).  If X is given (common random numbers) it is used
    instead of sampling (N ignored)."""
    rng = np.random.default_rng(1) if rng is None else rng
    A = np.asarray(A, float); n = A.shape[0]
    b = np.zeros(n) if b is None else np.asarray(b, float)
    svals = np.atleast_1d(np.asarray(svals, float)); S = len(svals)
    dA = np.diag(A).copy(); a2 = (A*A).sum(0)
    gd = {}
    for i in range(n):
        gd.setdefault(id(laws[i]), (laws[i], []))[1].append(i)
    groups = [(L, np.array(cols)) for L, cols in gd.values()]
    m_chunk = max(200, int(elem // max(n*S, 1)))
    Ntot = N if X is None else X.shape[0]
    tot = np.zeros(S); tot2 = np.zeros(S); done = 0
    lin = (np.abs(dA) < 1e-15)[None, :, None]
    aa = np.where(lin, 1.0, dA[None, :, None])
    sv = svals[None, None, :]
    while done < Ntot:
        m = min(m_chunk, Ntot - done)
        Xc = sample_X(laws, m, rng) if X is None else X[done:done+m]
        H = Xc @ A + b/2
        Qv = np.einsum('ij,ij->i', Xc, H + b/2) + c   # x^T A x + b.x + c = x.(Ax + b) + c ... fixed below
        Qv = np.einsum('ij,ij->i', Xc, Xc @ A) + Xc @ b + c
        AH = H @ A; g2 = np.einsum('ij,ij->i', H, H)
        h = H[:, :, None]; cc = Qv[:, None, None] - sv
        disc = h*h - dA[None, :, None]*cc
        okq = (disc >= 0) & ~lin
        sq = np.sqrt(np.where(okq, disc, 0.0))
        qq = -(h + np.copysign(sq, h))
        with np.errstate(divide='ignore', invalid='ignore'):
            D1 = np.where(lin, np.where(h != 0, -cc/(2*np.where(h == 0, 1.0, h)), 0.0), qq/aa)
            ok1 = np.where(lin, h != 0, okq)
            D2 = np.where(okq & (qq != 0), cc/np.where(qq == 0, 1.0, qq), 0.0)
        est = np.zeros((m, S))
        for D, ok in ((D1, ok1), (D2, okq)):
            D = np.where(ok, D, 0.0)
            t = Xc[:, :, None] + D
            f = np.empty_like(t)
            for L, cols in groups:
                f[:, cols, :] = L.pdf(t[:, cols, :])
            f *= ok
            hi = h + D*dA[None, :, None]
            G2 = g2[:, None, None] + 2*D*AH[:, :, None] + D*D*a2[None, :, None]
            with np.errstate(divide='ignore', invalid='ignore'):
                w = np.where(f > 0, f*np.abs(hi)/(2*G2), 0.0)
            est += w.sum(1)
        tot += est.sum(0); tot2 += (est**2).sum(0); done += m
    mean = tot/Ntot; var = tot2/Ntot - mean**2
    return mean, np.sqrt(np.maximum(var, 0)/Ntot)


def hub_window_values(a, T, R, svals, fh, delta):
    """Exact conditional P(|a x^2 + 2 T x + R - s| <= delta) for x ~ fh (PWLaw), per sample and s  -> (m, S).
    Divided by 2 delta this is an unbiased estimator of the window-averaged density (no spikes: <= 1/(2 delta))."""
    svals = np.atleast_1d(svals)
    Tm = T[:, None]; Rm = R[:, None]; sm = svals[None, :]
    out = np.zeros((len(T), len(svals)))
    if abs(a) < 1e-15:
        with np.errstate(divide='ignore', invalid='ignore'):
            e1 = (sm - Rm - delta)/(2*Tm); e2 = (sm - Rm + delta)/(2*Tm)
        lo = np.minimum(e1, e2); hi = np.maximum(e1, e2)
        zero = (Tm == 0)
        for ak, bk, ck in zip(fh.a, fh.b, fh.c):
            ov = np.clip(np.minimum(hi, bk) - np.maximum(lo, ak), 0, None)
            out += ck*np.where(zero, (np.abs(sm - Rm) <= delta)*(bk - ak), ov)
        return out
    # general a: set {x : s-delta <= q(x) <= s+delta}, q = a x^2 + 2 T x + R.  Work with sign(a) q.
    sg = np.sign(a); aa = abs(a)
    def roots(level):              # roots of aa x^2 + 2 sg T x + sg (R - level) = 0
        disc = Tm*Tm - aa*sg*(Rm - level)
        ok = disc >= 0
        sq = np.sqrt(np.where(ok, disc, 0.0))
        return (-sg*Tm - sq)/aa, (-sg*Tm + sq)/aa, ok
    up = sm + delta if sg > 0 else sm - delta     # the level where sg*q <= sg*up (the outer interval)
    dn = sm - delta if sg > 0 else sm + delta
    o1, o2, oko = roots(up)       # sg q <= sg up   <=> x in [o1, o2]
    i1, i2, oki = roots(dn)       # sg q <  sg dn   <=> x in (i1, i2)
    for ak, bk, ck in zip(fh.a, fh.b, fh.c):
        outer = np.clip(np.minimum(o2, bk) - np.maximum(o1, ak), 0, None)*oko
        inner = np.clip(np.minimum(i2, bk) - np.maximum(i1, ak), 0, None)*oki
        out += ck*(outer - inner)
    return out
