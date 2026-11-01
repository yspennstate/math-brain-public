"""Independent check of Proposition 6.3 (K >= 0) of the T067 q=4 draft, built from kfeat.py (Table 2 + App. A).

For each of the 192 cells (24 perms x 2 z-cells x 2 w-cells... the paper's 24 x 4 x 2: perms x cell pair x m is
not how it counts, so we count perms x z-cell x w-cell = 96 and treat m in {0, M} inside each) we build
    G = K P^5 Q^5 S^3 (UV)^e  -  gamma * Sigma_1 P^5 Q^5 S^3 (UV)^e
as an exact polynomial in the 8 cell variables and test that every coefficient is >= 0.
A quantity x with value poly / (P^da Q^db) is carried as Hq(poly, da, db).
usage: python cert.py [cell_index ...]   (no args: all cells, 4 workers)
"""
import sys, json, time, random
from fractions import Fraction as F
from itertools import permutations
import flint
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else '.')
import kfeat

NAMES = ('z0', 'z1', 'z2', 'z3', 'w0', 'w1', 'w2', 'w3')
CTX = flint.fmpq_mpoly_ctx.get(NAMES, 'degrevlex')
GENS = CTX.gens()
PERMS = list(permutations(range(4)))
VTX = [[-2031000, -2031000, -2031000, 6093000], [-2031000, -2031000, 2031000, 2031000],
       [-2031000, 677000, 677000, 677000], [0, 0, 0, 0]]          # 3e6 * vertices


def q(x):
    return flint.fmpq(x.numerator, x.denominator) if isinstance(x, F) else flint.fmpq(x)


class Ctx:
    def __init__(self, P, Q):
        self.P, self.Q = P, Q
        self.Pp, self.Qp = {0: CTX.from_dict({}) + 1}, {0: CTX.from_dict({}) + 1}

    def pp(self, k):
        if k not in self.Pp:
            self.Pp[k] = self.pp(k - 1) * self.P
        return self.Pp[k]

    def qp(self, k):
        if k not in self.Qp:
            self.Qp[k] = self.qp(k - 1) * self.Q
        return self.Qp[k]


class Hq:
    __slots__ = ('p', 'da', 'db', 'c')

    def __init__(self, p, da, db, c):
        self.p, self.da, self.db, self.c = p, da, db, c

    def lift(self, da, db):
        return self.p * self.c.pp(da - self.da) * self.c.qp(db - self.db)

    def __add__(self, o):
        if not isinstance(o, Hq):
            o = Hq(CTX.from_dict({}) + q(F(o)), 0, 0, self.c)
        da, db = max(self.da, o.da), max(self.db, o.db)
        return Hq(self.lift(da, db) + o.lift(da, db), da, db, self.c)

    __radd__ = __add__

    def __neg__(self):
        return Hq(-self.p, self.da, self.db, self.c)

    def __sub__(self, o):
        return self + (-o if isinstance(o, Hq) else -F(o))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if isinstance(o, Hq):
            return Hq(self.p * o.p, self.da + o.da, self.db + o.db, self.c)
        return Hq(self.p * q(F(o)), self.da, self.db, self.c)

    __rmul__ = __mul__

    def __truediv__(self, o):          # division by a rational scalar only
        return Hq(self.p * q(1 / F(o)), self.da, self.db, self.c)

    def __pow__(self, k):
        r = self
        for _ in range(k - 1):
            r = r * self
        return r


def cell_vars(tz, tw):
    z, w = list(GENS[:4]), list(GENS[4:])
    Z = [z[0] + z[3], z[1], z[2], z[3]] if tz == 0 else [z[0], z[1], z[2], z[3] + z[0]]
    W = [w[0] + w[3], w[1], w[2], w[3]] if tw == 0 else [w[0], w[1], w[2], w[3] + w[0]]
    return Z, W


def lin(Z):
    return [sum((Z[j] * VTX[j][i] for j in range(3)), CTX.from_dict({})) for i in range(4)]


def cells():
    return [(pi, tz, tw) for pi in range(24) for tz in (0, 1) for tw in (0, 1)]


def build(cell, g24_override=None):
    """returns dict of polynomials: G at m=0 and m=M (without (UV)^e), Sigma1 term, phi24 term, and U V."""
    pi, tz, tw = cell
    Z, W = cell_vars(tz, tw)
    U, V = sum(Z, CTX.from_dict({})), sum(W, CTX.from_dict({}))
    c = Ctx(U * 3000000, V * 3000000)
    al, be = lin(Z), lin(W)
    perm = PERMS[pi]
    a = [Hq(al[i], 1, 0, c) for i in range(4)]
    b = [Hq(be[perm[i]], 0, 1, c) for i in range(4)]
    return c, a, b, U, V


def k_parts(c, a, b, g24):
    """K s^3 as Hq, split into the m-free part and the coefficient of m; also phi24's two parts and Sigma1."""
    G = dict(kfeat.G); G[24] = g24
    pw = lambda i, j: sum((a[k] ** i * b[k] ** j if i and j else (a[k] ** i if i else b[k] ** j)
                           for k in range(4)), Hq(CTX.from_dict({}), 0, 0, c))
    A, B = pw(2, 0), pw(0, 2); ta, tb = pw(3, 0), pw(0, 3); sa, sb = pw(4, 0), pw(0, 4)
    cc = pw(1, 1); p21, p12, p22 = pw(2, 1), pw(1, 2), pw(2, 2)
    p31s = pw(3, 1) + pw(1, 3); p32, p23, p33 = pw(3, 2), pw(2, 3), pw(3, 3)
    p42, p24 = pw(4, 2), pw(2, 4); ell = p21 + p12
    kap = cc * ell - (B * ta + A * tb) / 3
    H = [a[i] + b[i] + a[i] * b[i] - cc / 4 for i in range(4)]
    N = H[0] * H[0] + H[1] * H[1] + H[2] * H[2] + H[3] * H[3]
    J = H[0] ** 3 + H[1] ** 3 + H[2] ** 3 + H[3] ** 3
    sym4 = None
    for p in PERMS:
        t = a[0] * b[p[0]] + a[1] * b[p[1]] + a[2] * b[p[2]] + a[3] * b[p[3]]
        t2 = t * t
        sym4 = t2 * t2 if sym4 is None else sym4 + t2 * t2
    cc2 = cc * cc
    AB = A * B
    # m-free polynomial part
    P0 = (F(2, 3) * ta * tb + G[1] * AB * (A + B) + G[2] * (A + B) * (cc2 - AB / 3)
          + G[8] * (cc2 * cc - F(2, 3) * ta * tb) + G[11] * cc * ta * tb + G[19] * (cc * p22 - ta * tb / 3)
          + G[20] * (p33 - ta * tb / 4) + G[21] * (p42 + p24 - (B * sa + A * sb) / 4)
          + G[23] * (24 * cc2 * cc2 - sym4) + G[24] * AB * (A + B)
          + G[29] * (cc * p31s - (B * sa + A * sb) / 3)
          + G[30] * (p21 * p21 + p12 * p12 - (B * sa + A * sb - AB * (A + B) / 4) / 3)
          + G[31] * (p21 * p12 - ta * tb / 3) + G[32] * (A + B) * (p22 - AB / 4))
    A2B2 = A * A + B * B
    # coefficient of m in the polynomial part
    P1 = (-kfeat.BETA * AB + G[1] * A2B2 - G[0] * (ta + tb) + G[3] * (cc2 - AB / 3) + G[10] * cc * (A + B)
          + G[12] * ell + G[13] * (p22 - AB / 4) + G[14] * p31s + G[15] * cc * (ta + tb) + G[16] * ell * (A + B)
          + G[17] * kap + G[18] * (p32 + p23 - (B * ta + A * tb) / 4) + G[22] * cc * A2B2 - G[24] * A2B2)
    s = 1 + cc / 4
    s2 = s * s; s3 = s2 * s
    K0s3 = P0 * s3 - N * cc2 * s2
    K1s3 = P1 * s3 + G[0] * J * s - G[1] * N * N
    phi24_0 = AB * (A + B) * s3
    phi24_1 = -1 * A2B2 * s3
    Sig1 = AB * (A + B) - 2 * ta * tb
    return K0s3, K1s3, phi24_0, phi24_1, Sig1


def to_G(c, h):
    # G = 64 P^8 Q^8 (K s^3)
    return 64 * h.p * c.pp(8 - h.da) * c.qp(8 - h.db)


def check_cell(idx, spot=True):
    t0 = time.time()
    cell = cells()[idx]
    c, a, b, U, V = build(cell)
    K0, K1, f0, f1, S1 = k_parts(c, a, b, kfeat.G[24])
    G0, G1 = to_G(c, K0), to_G(c, K1)
    D0, D1 = to_G(c, f0), to_G(c, f1)
    S = c.P * c.Q * 4 + sum((a[i] * b[i] for i in range(4)), Hq(CTX.from_dict({}), 0, 0, c)).lift(1, 1)
    Sig = S1.p * c.pp(5 - S1.da) * c.qp(5 - S1.db) * S ** 3
    Mq = q(kfeat.MBIG)
    out = {'cell': idx, 'perm': PERMS[cell[0]], 'tz': cell[1], 'tw': cell[2]}
    if spot:   # compare G with direct rational K at a random interior point, both m
        rnd = random.Random(1000 + idx)
        vals = [F(rnd.randint(1, 50)) for _ in range(8)]
        Zv = [vals[0] + vals[3], vals[1], vals[2], vals[3]] if cell[1] == 0 else [vals[0], vals[1], vals[2], vals[3] + vals[0]]
        Wv = [vals[4] + vals[7], vals[5], vals[6], vals[7]] if cell[2] == 0 else [vals[4], vals[5], vals[6], vals[7] + vals[4]]
        Uv, Vv = sum(Zv), sum(Wv)
        av = [sum(Zv[j] * VTX[j][i] for j in range(3)) / (3000000 * Uv) for i in range(4)]
        bs = [sum(Wv[j] * VTX[j][i] for j in range(3)) / (3000000 * Vv) for i in range(4)]
        bv = [bs[PERMS[cell[0]][i]] for i in range(4)]
        Pv, Qv = 3000000 * Uv, 3000000 * Vv
        Sv = 4 * Pv * Qv * (1 + sum(x * y for x, y in zip(av, bv)) / 4)
        fv = [q(x) for x in vals]
        for mm, Gp in ((F(0), G0), (kfeat.MBIG, G0 + G1 * Mq)):
            direct = kfeat.K(av, bv, mm) * Pv ** 5 * Qv ** 5 * Sv ** 3
            got = Gp(*fv)
            assert F(int(got.p), int(got.q)) == direct, ('spot mismatch', idx, mm)
        out['spot'] = 'ok'
    UV = U * V
    dg = q(F(-1, 10) - kfeat.G24_SHIFT)
    out['m'] = {}
    for mm in (0, 1):
        Gp = G0 if mm == 0 else G0 + G1 * Mq
        Dp = D0 if mm == 0 else D0 + D1 * Mq
        tried, win = {}, None
        for gam in (F(0), F(1, 3)):
            for e in (1, 2):
                mn = min(((Gp - Sig * q(gam)) * UV ** e).coeffs())
                tried[f'{gam}|{e}'] = float(mn)
                if mn >= 0:
                    win = (gam, e); break
            if win:
                break
        r = {'pass': win is not None, 'gamma': str(win[0]) if win else None, 'e': win[1] if win else None,
             'tried': tried}
        if win:   # controls: g24 shift -> -1/10 at the winning (gamma, e); gamma -> 0 at e=1,2 is in 'tried'
            r['ctrl_g24_min'] = float(min(((Gp + Dp * dg - Sig * q(win[0])) * UV ** win[1]).coeffs()))
        out['m'][mm] = r
    out['secs'] = round(time.time() - t0, 1)
    return out


if __name__ == '__main__':
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    idxs = [int(x) for x in sys.argv[1:]] or list(range(len(cells())))
    if len(idxs) <= 2:
        for i in idxs:
            print(json.dumps(check_cell(i)), flush=True)
    else:
        from multiprocessing import Pool
        with Pool(4) as pool:
            for r in pool.imap_unordered(check_cell, idxs):
                print(json.dumps(r), flush=True)
