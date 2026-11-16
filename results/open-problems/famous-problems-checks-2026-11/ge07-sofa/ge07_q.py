# GE07 moving sofa: the upper bound Q of Baek (arXiv 2411.19826, Definitions 8.1.3, 8.1.4, 8.2.2) on a
# discrete model: convex bodies are polygons whose edge normals lie on one fixed angular grid, so that
# Minkowski combinations are linear in the vector of support values and Q is an exact quadratic form.
# Tests: Q(G) = |G|; area <= Q <= Q(G) on a family of caps; concavity along segments; sign of the
# directional derivative at Gerver's sofa. Floating point; nothing here is a proof.
import math, sys
import numpy as np

def out(*a):
    print(*a, flush=True)

PI2 = math.pi/2
phi = 0.039177364790083641
theta = 0.681301509382724894
a1, a2 = 1.210322422072688751, -0.25
b1, b2 = -0.527624598026784624, 0.920258385160637622
c1, c2 = 0.626045522848465867, -0.944750803946430751
d1, d2 = 1.313022761424232933, -0.525382670414554437
e1, e2 = 1.210322422072688751, 0.25
KAP = np.array([(-0.210322422072688751, 0.25), (-0.919179292771593322, 0.472406619750805465),
                (-0.613763229430251668, 0.889626479003221860), (-0.308347166088910014, 0.472406619750805465),
                (-1.017204036787814585, 0.25)])
TB = [0.0, phi, theta, PI2 - theta, PI2 - phi, PI2]

def xG(t):
    t = np.asarray(t, dtype=float)
    c = np.cos(t); s = np.sin(t)
    w = [(a1*c + a2*s - 1, -a2*c + a1*s - 0.5),
         (-t*t/4 + b1*t + b2, t/2 - b1 - 1),
         (c1 - t, c2 + t),
         (-t/2 + d1 - 1, -t*t/4 + d1*t + d2),
         (e1*c + e2*s - 0.5, -e2*c + e1*s - 1)]
    j = np.zeros(t.shape, dtype=int)
    for k in range(1, 5):
        j[t >= TB[k]] = k
    res = np.zeros((2,) + t.shape)
    for k in range(5):
        m = (j == k)
        res[0][m] = c[m]*w[k][0][m] - s[m]*w[k][1][m] + KAP[k, 0]
        res[1][m] = s[m]*w[k][0][m] + c[m]*w[k][1][m] + KAP[k, 1]
    return res

def xE(a, b, e=0.0):          # semi-ellipse-like rotation paths; a = b = 2/pi is Hammersley's sofa
    return lambda t: np.array([a*(np.cos(2*np.asarray(t)) - 1), b*np.sin(2*np.asarray(t)) + e*np.sin(4*np.asarray(t))])

def mix(x1, x2, lam):
    return lambda t: (1 - lam)*x1(t) + lam*x2(t)

# ---- the grid --------------------------------------------------------------------------------
def make_base(n):
    parts = []
    for k in range(5):
        m = max(8, int(round(n*(TB[k+1] - TB[k])/PI2)))
        parts.append(np.linspace(TB[k], TB[k+1], m + 1)[:-1])
    return np.concatenate(parts + [np.array([PI2])])

class Grid:
    def __init__(self, n):
        self.base = make_base(n)
        self.M = len(self.base)
        m = self.M - 1
        self.m = m
        self.ang = np.concatenate([self.base[:-1] + q*PI2 for q in range(4)])
        self.N = len(self.ang)
        self.cu = np.cos(self.ang); self.su = np.sin(self.ang)
        self.iR = int(np.argmin(np.abs(self.base - phi)))
        self.iL = int(np.argmin(np.abs(self.base - (PI2 - phi))))
        assert abs(self.base[self.iR] - phi) < 1e-14 and abs(self.base[self.iL] - (PI2 - phi)) < 1e-14
        d = np.roll(self.ang, -1) - self.ang
        d[-1] += 2*math.pi
        self.sind = np.sin(d)

    def verts(self, h):       # p_i = intersection of support lines i and i+1
        hn = np.roll(h, -1); cn = np.roll(self.cu, -1); sn = np.roll(self.su, -1)
        px = (h*sn - hn*self.su)/self.sind
        py = (-h*cn + hn*self.cu)/self.sind
        return px, py

    def ell(self, h):         # signed edge lengths
        px, py = self.verts(h)
        dx = px - np.roll(px, 1); dy = py - np.roll(py, 1)
        return -dx*self.su + dy*self.cu

    def support(self, poly):
        res = np.full(self.N, -1e300)
        for i0 in range(0, self.N, 512):
            sl = slice(i0, i0 + 512)
            res[sl] = (np.outer(self.cu[sl], poly[:, 0]) + np.outer(self.su[sl], poly[:, 1])).max(axis=1)
        return res

def clip(P, nx, ny, c):       # keep {p : <p, n> <= c}; P convex, counterclockwise
    d = P[:, 0]*nx + P[:, 1]*ny - c
    ins = d <= 0
    if ins.all():
        return P
    if not ins.any():
        return P[:0]
    Pn = np.roll(P, -1, axis=0); dn = np.roll(d, -1); insn = np.roll(ins, -1)
    cr = ins != insn
    den = np.where(cr, d - dn, 1.0)
    tt = np.where(cr, d/den, 0.0)
    I = P + tt[:, None]*(Pn - P)
    arr = np.stack([P, I], axis=1)
    msk = np.stack([ins, cr], axis=1)
    return arr[msk]

def triple(G, xfun):
    """support vectors (hK, hB, hD) of the cap with rotation path xfun and of B_K, D_K (Definition 8.1.4)"""
    m = G.m
    t = G.base
    x = xfun(t)
    hu = x[0]*np.cos(t) + x[1]*np.sin(t) + 1          # h_K(t)
    hv = -x[0]*np.sin(t) + x[1]*np.cos(t) + 1         # h_K(t + pi/2)
    assert abs(hu[-1] - hv[0]) < 1e-12, "path must start at the origin and end on the x-axis"
    hup = np.concatenate([hu[:-1], hv])               # angles base[:-1], base + pi/2 : 2m+1 values on [0, pi]
    aup = np.concatenate([t[:-1], t + PI2])
    ca = np.cos(aup); sa = np.sin(aup)
    sd = np.sin(np.diff(aup))
    px = (hup[:-1]*sa[1:] - hup[1:]*sa[:-1])/sd
    py = (-hup[:-1]*ca[1:] + hup[1:]*ca[:-1])/sd
    poly = np.concatenate([[[hup[0], 0.0]], np.stack([px, py], axis=1), [[-hup[-1], 0.0]]])
    e = np.roll(poly, -1, axis=0) - poly
    en = np.roll(e, -1, axis=0)
    convex_defect = float((e[:, 0]*en[:, 1] - e[:, 1]*en[:, 0]).min())
    hK = G.support(poly)
    B = poly
    for k in range(G.iR, G.M):
        B = clip(B, -math.cos(t[k]), -math.sin(t[k]), 1 - hu[k])
    D = poly
    for k in range(0, G.iL + 1):
        D = clip(D, math.sin(t[k]), -math.cos(t[k]), 1 - hv[k])
    hB = G.support(B); hD = G.support(D)
    # injectivity on the grid: x' . u < 0 and x' . v > 0 in the interior
    dx = np.gradient(x[0], t); dy = np.gradient(x[1], t)
    xu = dx*np.cos(t) + dy*np.sin(t); xv = -dx*np.sin(t) + dy*np.cos(t)
    inj = float(max(xu[3:-3].max(), (-xv[3:-3]).max()))   # negative means the condition holds on the grid
    info = dict(convex_defect=convex_defect, inj=inj, areaK=0.5*float(np.sum(hK*G.ell(hK))),
                eqR=1 - hu[G.iR] - hB[2*m + G.iR], eqBottomB=hB[3*m], eqL=1 - hv[G.iL] - hD[3*m + G.iL], eqBottomD=hD[3*m],
                minellB=float(G.ell(hB).min()), minellD=float(G.ell(hD).min()), minellK=float(G.ell(hK).min()))
    return (hK, hB, hD), info

def Q(G, P):
    hK, hB, hD = P
    m = G.m; iR = G.iR; iL = G.iL
    t = G.base
    lK = G.ell(hK); lB = G.ell(hB); lD = G.ell(hD)
    areaK = 0.5*np.sum(hK*lK)
    i0, i1 = 3*m + 1, 3*m + iL
    JdD = 0.5*np.sum(hD[i0:i1]*lD[i0:i1])
    pDx, pDy = G.verts(hD)
    YD = (pDx[3*m + iL - 1], pDy[3*m + iL - 1])
    xKx = (hK[:m+1] - 1)*np.cos(t) - (hK[m:2*m+1] - 1)*np.sin(t)
    xKy = (hK[:m+1] - 1)*np.sin(t) + (hK[m:2*m+1] - 1)*np.cos(t)
    Jx = 0.5*np.sum(xKx[iR:iL]*xKy[iR+1:iL+1] - xKx[iR+1:iL+1]*xKy[iR:iL])
    pBx, pBy = G.verts(hB)
    XB = (pBx[2*m + iR], pBy[2*m + iR])
    j0, j1 = 2*m + iR + 1, 3*m
    JbB = 0.5*np.sum(hB[j0:j1]*lB[j0:j1])
    J1 = 0.5*(YD[0]*xKy[iL] - xKx[iL]*YD[1])
    J2 = 0.5*(xKx[iR]*XB[1] - XB[0]*xKy[iR])
    return float(areaK + JdD + J1 - Jx + J2 + JbB)

def area_columns(xfun, NT, NX):
    tt = (np.arange(NT) + 0.5)*(PI2/NT)
    xx = xfun(tt)
    Xmin = float(xfun(np.array([PI2]))[0][0]) - 1.0
    X = np.linspace(Xmin, 1.0, NX)
    ct = np.cos(tt); st = np.sin(tt)
    lower = np.zeros(NX); upper = np.ones(NX)
    for i0 in range(0, NX, 100):
        dxx = X[i0:i0+100][:, None] - xx[0][None, :]
        U1 = xx[1][None, :] + (1 - ct[None, :]*dxx)/st[None, :]
        U2 = xx[1][None, :] + (1 + st[None, :]*dxx)/ct[None, :]
        Lw = xx[1][None, :] + np.minimum(-(ct/st)[None, :]*dxx, (st/ct)[None, :]*dxx)
        upper[i0:i0+100] = np.minimum(1.0, np.minimum(U1.min(axis=1), U2.min(axis=1)))
        lower[i0:i0+100] = np.maximum(0.0, Lw.max(axis=1))
    w = np.maximum(upper - lower, 0)
    return float(np.sum((w[1:] + w[:-1])*np.diff(X))/2), float((upper - lower)[1:-1].min())

def sofa_area(xfun):
    a1_, _ = area_columns(xfun, 10000, 3001)
    a2_, wmin = area_columns(xfun, 20000, 6001)
    return 2*a2_ - a1_, wmin      # the error is first order in the angular step

def comb(P1, P2, lam):
    return tuple((1 - lam)*u + lam*v for u, v in zip(P1, P2))

# ---- the family of caps -----------------------------------------------------------------------
rng = np.random.default_rng(7)
fam = [("Gerver", xG)]
for r in (0.50, 0.58, 2/math.pi, 0.70):
    fam.append(("semicircle r=%.4f" % r, xE(r, r)))
for (a, b, e) in ((0.60, 0.66, 0.0), (0.66, 0.60, 0.0), (0.62, 0.62, 0.02), (0.62, 0.62, -0.02), (0.58, 0.68, 0.015)):
    fam.append(("ellipse a=%.2f b=%.2f e=%+.3f" % (a, b, e), xE(a, b, e)))
for lam in (0.05, 0.2, 0.5, 0.8):
    fam.append(("mix Gerver/Hammersley lam=%.2f" % lam, mix(xG, xE(2/math.pi, 2/math.pi), lam)))
for lam in (0.03, 0.1, 0.3):
    fam.append(("mix Gerver/ellipse(0.60,0.66) lam=%.2f" % lam, mix(xG, xE(0.60, 0.66), lam)))
    fam.append(("mix Gerver/ellipse(0.62,0.62,+0.02) lam=%.2f" % lam, mix(xG, xE(0.62, 0.62, 0.02), lam)))
for lam in (-0.05, -0.02, -0.01):     # past Gerver's sofa, away from the other cap; kept only if still a valid cap
    fam.append(("extrapolate Gerver/Hammersley lam=%.2f" % lam, mix(xG, xE(2/math.pi, 2/math.pi), lam)))
    fam.append(("extrapolate Gerver/ellipse(0.60,0.66) lam=%.2f" % lam, mix(xG, xE(0.60, 0.66), lam)))

for n in ([int(a) for a in sys.argv[1:]] or [800, 1600]):
    G = Grid(n)
    out("=== grid: %d base angles, %d normals" % (G.M, G.N))
    Ps = []; Qs = []; names = []
    for name, xf in fam:
        P, info = triple(G, xf)
        valid = (info['convex_defect'] > -1e-9 and info['minellK'] > -1e-9 and info['inj'] < 0 and info['areaK'] >= 2.2)
        q = Q(G, P)
        if n == 800 or name == "Gerver":
            A, wmin = sofa_area(xf)
        else:
            A, wmin = float('nan'), float('nan')
        out("%-48s valid=%s |K|=%.5f inj=%+.3f  area=%.7f  Q=%.7f  Q-area=%+.2e  thinnest=%.3f  eq(3),(5): %.1e %.1e %.1e %.1e"
            % (name, valid, info['areaK'], info['inj'], A, q, q - A, wmin, info['eqR'], info['eqBottomB'], info['eqL'], info['eqBottomD']))
        if not valid:
            out("    not a cap of the family: convexity defect of the support polygon %.2e, shortest edge of K %.2e" % (info['convex_defect'], info['minellK']))
        if valid:
            Ps.append(P); Qs.append(q); names.append(name)
    QG = Qs[0]
    out("Q(Gerver) = %.9f   (|G| = 2.219531669)" % QG)
    out("largest Q over the valid family other than Gerver: %.9f (%s)" % (max(Qs[1:]), names[1 + int(np.argmax(Qs[1:]))]))
    # shrunk B, D: cut an extra sliver from B_G and D_G, keeping the equalities (3) and (5)
    hK, hB, hD = Ps[0]
    m = G.m
    extra = []
    for s_, eps in ((0.5, 0.01), (0.9, 0.02), (1.3, 0.01)):
        # rebuild the polygons of B_G and D_G from the support vectors, clip once more
        px, py = G.verts(hB); polyB = np.stack([px, py], axis=1)
        k = int(np.argmin(np.abs(G.base - s_)))
        tk = G.base[k]
        cB = hB[2*m + k] - eps
        B2 = clip(polyB, -math.cos(tk), -math.sin(tk), cB)
        hB2 = G.support(B2)
        px, py = G.verts(hD); polyD = np.stack([px, py], axis=1)
        k2 = int(np.argmin(np.abs(G.base - (PI2 - s_))))
        t2 = G.base[k2]
        D2 = clip(polyD, math.sin(t2), -math.cos(t2), hD[3*m + k2] - eps)
        hD2 = G.support(D2)
        ok = (abs(hB2[2*m + G.iR] - hB[2*m + G.iR]) < 1e-12 and abs(hB2[3*m]) < 1e-12
              and abs(hD2[3*m + G.iL] - hD[3*m + G.iL]) < 1e-12 and abs(hD2[3*m]) < 1e-12)
        P2 = (hK, hB2, hD2)
        q2 = Q(G, P2)
        out("shrunk feet at angle %.1f by %.2f: in L (touching conditions kept): %s   Q = %.7f  (Q - Q(G) = %+.2e)" % (s_, eps, ok, q2, q2 - QG))
        if ok:
            extra.append(P2)
    allP = Ps + extra
    # directional derivative at Gerver and second-order coefficient towards every other point
    worst_b = -1e9; worst_c = -1e9
    for i in range(1, len(allP)):
        q1 = Q(G, allP[i]); qh = Q(G, comb(allP[0], allP[i], 0.5))
        c_ = 2*(QG + q1 - 2*qh); b_ = q1 - QG - c_
        nm = names[i] if i < len(names) else "shrunk feet %d" % (i - len(names) + 1)
        out("  from Gerver towards %-46s DQ = %+.3e   second-order coefficient = %+.3e" % (nm, b_, c_))
        worst_b = max(worst_b, b_); worst_c = max(worst_c, c_)
    out("largest directional derivative at Gerver: %+.3e ; largest second-order coefficient from Gerver: %+.3e" % (worst_b, worst_c))
    worst = -1e9; cnt = 0; arg = None
    for i in range(len(allP)):
        for j in range(i + 1, len(allP)):
            c_ = 2*(Q(G, allP[i]) + Q(G, allP[j]) - 2*Q(G, comb(allP[i], allP[j], 0.5)))
            cnt += 1
            if c_ > worst:
                worst = c_; arg = (i, j)
    out("concavity on %d segments between points of L: largest second-order coefficient %+.3e (pair %s)" % (cnt, worst, arg))
    # exact quadraticity of the discrete Q along one segment
    lam = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    vals = np.array([Q(G, comb(allP[0], allP[3], l)) for l in lam])
    coef = np.polyfit(lam[[0, 2, 4]], vals[[0, 2, 4]], 2)
    out("quadratic along Gerver -> Hammersley: residual at lam = 0.25, 0.75: %.1e" % np.abs(np.polyval(coef, lam[[1, 3]]) - vals[[1, 3]]).max())
out("done")
