"""Standalone exact checker for one gate at one rational product bias.

Given a +-1 table (entry x = G(x), bit i of x = 1 iff input i is TRUE), rational biases p_i = Pr[input i true], and a
stored potential (npz with nodes xs, values G, cap C; Gamma(z) = s*Gnum(log2(1/s)) + c z(1-z), s = min(z,1-z), Gnum the
piecewise-linear interpolant of the stored doubles, read as exact binary rationals), it computes

    w_T = Ghat_mu(T)^2 = R_T^2 * prod_{i in T} p_i(1-p_i)           exactly (R_T from the matrix [[1-p,p],[1,-1]]),
    It_i, p_out, W = sum It_i/4 - p_out(1-p_out)                     exactly,
    Htilde = sum w_T log2(1/w_T), h(V_i), Gamma(p_i), Gamma(p_out)    in rational intervals,

and returns an interval for D = sum_i It_i (Gamma(p_i) + h(V_i))/V_i - Htilde - Gamma(p_out) and for c = -D/W.
Logarithms: ln r = e ln 2 + 2 atanh(z), z = (m-1)/(m+1), r = m 2^e with m in [2/3, 4/3), series with the explicit tail
bound 2|z|^(2N+1)/((2N+1)(1-z^2)); ln 2 = 2 atanh(1/3) likewise.  Partial sums are rounded outward to multiples of
2^-PREC.  No floating-point value decides any inequality."""
from fractions import Fraction as Fr
import math, bisect
import numpy as np

PREC = 400
NTERMS = 90
_ONE = 1 << PREC


def _rd(q):   # round a Fraction down to the 2^-PREC grid
    return Fr((q.numerator * _ONE) // q.denominator, _ONE)


def _ru(q):
    return Fr(-((-q.numerator * _ONE) // q.denominator), _ONE)


def _atanh2_pos(z, upper):
    """bound for 2 atanh(z), 0 <= z <= 1/3: every positive term rounded in one direction (the power as well)"""
    if z == 0:
        return Fr(0)
    rnd = _ru if upper else _rd
    s = Fr(0); zp = rnd(z); z2 = rnd(z * z)
    for j in range(NTERMS):
        s = rnd(s + rnd(2 * zp / (2 * j + 1)))
        zp = rnd(zp * z2)
    if upper:
        tail = 2 * z ** (2 * NTERMS + 1) / ((2 * NTERMS + 1) * (1 - z * z))
        s = _ru(s + _ru(tail))
    return s


def _atanh2(z):
    """interval for 2 atanh(z), |z| <= 1/3 (atanh is odd and increasing; z is first enclosed on the 2^-PREC grid)"""
    assert abs(z) <= Fr(1, 3)
    if z >= 0:
        lo, hi = _rd(z), _ru(z)
        return _atanh2_pos(lo, False), _atanh2_pos(min(hi, Fr(1, 3)), True)
    lo, hi = _rd(-z), _ru(-z)
    return -_atanh2_pos(min(hi, Fr(1, 3)), True), -_atanh2_pos(lo, False)


LN2 = _atanh2(Fr(1, 3))          # ln 2 = 2 atanh(1/3)


def ln_iv(r):
    r = Fr(r)
    assert r > 0
    e = r.numerator.bit_length() - r.denominator.bit_length()
    m = r / Fr(2) ** e
    while m >= Fr(4, 3):
        m /= 2; e += 1
    while m < Fr(2, 3):
        m *= 2; e -= 1
    lo, hi = _atanh2((m - 1) / (m + 1))
    if e >= 0:
        return lo + e * LN2[0], hi + e * LN2[1]
    return lo + e * LN2[1], hi + e * LN2[0]


def log2_iv(r):
    lo, hi = ln_iv(r)
    a = [lo / LN2[0], lo / LN2[1], hi / LN2[0], hi / LN2[1]]
    return min(a), max(a)


def xlogx_iv(w):
    """interval for w log2(1/w), w in (0,1] rational; 0 for w = 0"""
    w = Fr(w)
    if w == 0 or w == 1:
        return Fr(0), Fr(0)
    lo, hi = log2_iv(1 / w)
    return w * lo, w * hi


def h_iv(v):
    v = Fr(v)
    a = xlogx_iv(v); b = xlogx_iv(1 - v)
    return a[0] + b[0], a[1] + b[1]


class ExactPot:
    def __init__(self, npz, c=Fr(0)):
        d = np.load(npz)
        self.xs = [Fr(float(x)) for x in d["xs"]]
        self.G = [Fr(float(x)) for x in d["G"]]
        self.K = self.xs[-1]
        self.c = Fr(c)
        self.xs_f = [float(x) for x in d["xs"]]

    def gnum_iv(self, xlo, xhi):
        """range of the piecewise-linear interpolant over [xlo, xhi] (inside [1, K])"""
        assert self.xs[0] <= xlo and xhi <= self.K, "x outside the node range"
        def val(x):
            j = bisect.bisect_right(self.xs, x) - 1
            j = min(max(j, 0), len(self.xs) - 2)
            x0, x1 = self.xs[j], self.xs[j + 1]
            return self.G[j] + (self.G[j + 1] - self.G[j]) * (x - x0) / (x1 - x0)
        pts = [val(xlo), val(xhi)]
        j0 = bisect.bisect_right(self.xs, xlo); j1 = bisect.bisect_left(self.xs, xhi)
        for j in range(j0, j1):
            pts.append(self.G[j])
        return min(pts), max(pts)

    def gamma_iv(self, z):
        z = Fr(z)
        s = min(z, 1 - z)
        if s == Fr(1, 2):
            g = self.G[0] if self.xs[0] == 1 else None
            assert g is not None
            base = (s * g, s * g)
        else:
            xlo, xhi = log2_iv(1 / s)
            glo, ghi = self.gnum_iv(max(xlo, self.xs[0]), xhi)
            base = (s * glo, s * ghi)
        m = self.c * z * (1 - z)
        return base[0] + m, base[1] + m


def exact_spectrum(table, ps):
    """table: list of +-1 ints; ps: list of Fractions.  Returns dict T -> w_T (exact)"""
    k = len(ps); n = 1 << k
    A = [Fr(int(v)) for v in table]
    for i in range(k):
        p = ps[i]; step = 1 << i
        B = list(A)
        for x in range(n):
            if (x >> i) & 1:
                continue
            a0 = A[x]; a1 = A[x | step]
            B[x] = (1 - p) * a0 + p * a1          # even part
            B[x | step] = a0 - a1                 # odd part, sqrt(p(1-p)) factored out
        A = B
    w = {}
    for T in range(n):
        if A[T] == 0:
            continue
        f = A[T] * A[T]
        for i in range(k):
            if (T >> i) & 1:
                f *= ps[i] * (1 - ps[i])
        w[T] = f
    return w


def check(table, ps, npz, c=Fr(0), verbose=True):
    ps = [Fr(p) for p in ps]
    k = len(ps)
    pot = ExactPot(npz, c)
    w = exact_spectrum(table, ps)
    tot = sum(w.values())
    assert tot == 1, "Parseval fails"
    mean = None
    # p_out from the empty coefficient: Ghat(empty) = E G = 1 - 2 p_out
    A0 = sum(Fr(int(v)) * _prob(x, ps) for x, v in enumerate(table))
    p_out = (1 - A0) / 2
    It = [sum(wt for T, wt in w.items() if (T >> i) & 1) for i in range(k)]
    W = sum(It) / 4 - p_out * (1 - p_out)
    Hlo = Fr(0); Hhi = Fr(0)
    for wt in w.values():
        a, b = xlogx_iv(wt); Hlo += a; Hhi += b
    Rlo = Fr(0); Rhi = Fr(0)
    for i in range(k):
        V = 4 * ps[i] * (1 - ps[i])
        g = pot.gamma_iv(ps[i]); hv = h_iv(V)
        r = It[i] / V
        Rlo += r * (g[0] + hv[0]); Rhi += r * (g[1] + hv[1])
    go = pot.gamma_iv(p_out)
    Dlo = Rlo - Hhi - go[1]
    Dhi = Rhi - Hlo - go[0]
    out = dict(p_out=p_out, W=W, It=It, D=(Dlo, Dhi), c=(-Dhi / W, -Dlo / W), Gamma_out=go,
               Htilde=(Hlo, Hhi), nnz=len(w))
    if verbose:
        print("  p_out = %s = %.15f ; W = %s = %.15f" % (p_out, float(p_out), W, float(W)))
        print("  It_i = %s" % ", ".join("%.12f" % float(x) for x in It))
        print("  Htilde in [%.18f, %.18f]" % (float(Hlo), float(Hhi)))
        print("  Gamma(p_out) in [%.18f, %.18f]" % (float(go[0]), float(go[1])))
        print("  D in [%.18e, %.18e]   (width %.2e)" % (float(Dlo), float(Dhi), float(Dhi - Dlo)))
        print("  c = -D/W in [%.15e, %.15e]" % (float(out["c"][0]), float(out["c"][1])))
    return out


def _prob(x, ps):
    pr = Fr(1)
    for i, p in enumerate(ps):
        pr *= p if (x >> i) & 1 else (1 - p)
    return pr


if __name__ == "__main__":
    # self-test of the logarithm against math.log at a few points
    for r in (Fr(3, 7), Fr(10**20 + 3, 7), Fr(1, 10**30), Fr(5, 4)):
        lo, hi = ln_iv(r)
        print("ln %s in [%.17g, %.17g]  math %.17g  width %.1e" % (r if r.denominator < 10**6 else "big", float(lo), float(hi),
              math.log(float(r)) if float(r) > 0 else float('nan'), float(hi - lo)))
