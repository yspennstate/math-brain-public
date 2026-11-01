"""Second, independent certificate for Prop 6.2 of the T067 q=4 d=2 draft (agent H, 17-18 Oct 2026).

Written from the paper's Table 2 (features) and Appendix A (coefficients) only; no code shared with indep_cover.py.
K * s^3 is built as a bihomogeneous polynomial in (a, u; b, v), u and v homogenising a and b; each case substitutes
the barycentric chart of the ordered simplex (vertices rho(-1,-1,-1,3), rho(-1,-1,1,1), rho(-1,1/3,1/3,1/3), 0),
the cell split z0>=z3 / z3>=z0, and one of 24 permutations for b, then multiplies by (U V)^e and checks every
coefficient of  K s^3 - sum_k gamma_k Sigma_k s^3  is >= 0.  A separate plain-Fraction evaluator of K checks the
polynomial at random rational points.

usage: python cert_b1e.py [selftest | run [e_max] | control NAME]
"""
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction as Fr

import flint

Q = flint.fmpq
RHO = Fr(677, 1000)
U_GRID = Fr(1375940705703331, 30399297484750848)
M_END = 8 * U_GRID
BETA = Fr(1, 10**6)
G24_A = Fr(-44673597587449418976423934191113, 1462309266444848905334068011200160)
G24_SHIFT = Fr(1743, 480965)
G24_B = Fr(-3787526362446847631199691392941357033, 140663915267129350750800004201376990880)
GJ = {0: Fr(32189, 5000), 1: Fr(307513, 304635), 2: Fr(1349531, 958408), 3: Fr(13119169, 971828),
      8: Fr(2046290, 998719), 10: Fr(10803745609, 1218540000), 11: Fr(649352, 585675), 12: Fr(-96567, 5000),
      13: Fr(-33529637, 939631), 14: Fr(-96567, 5000), 15: Fr(1007541, 284861), 16: Fr(2858842, 731359),
      17: Fr(8086351, 894289), 18: Fr(314989, 778090), 19: Fr(-293112, 998719), 20: Fr(390816, 998719),
      21: Fr(2119698, 387547), 22: Fr(-760908, 859123), 23: Fr(-9410, 911487), 29: Fr(-1454253, 671354),
      30: Fr(-1640643, 978656), 31: Fr(-146556, 998719), 32: Fr(-505057, 629438)}
PERMS = list(itertools.permutations(range(4)))
VERT = [[-RHO, -RHO, -RHO, 3 * RHO], [-RHO, -RHO, RHO, RHO], [-RHO, RHO / 3, RHO / 3, RHO / 3], [0, 0, 0, 0]]


def q(x):
    x = Fr(x)
    return Q(x.numerator, x.denominator)


def g_coeffs(shift=G24_SHIFT):
    g = dict(GJ)
    g[24] = G24_A + shift
    return g


# ---------------- symbolic K s^3 as a bihomogeneous polynomial -----------------
CTX = flint.fmpq_mpoly_ctx.get(('a0', 'a1', 'a2', 'a3', 'u', 'b0', 'b1', 'b2', 'b3', 'v'), 'degrevlex')
_g = CTX.gens()
A_, U_, B_, V_ = _g[0:4], _g[4], _g[5:9], _g[9]


class Hm:
    """polynomial numerator with its a-degree and b-degree (value = p / (u^da v^db))."""
    __slots__ = ('p', 'da', 'db')

    def __init__(self, p, da, db):
        self.p, self.da, self.db = p, da, db

    def lift(self, da, db):
        return self.p * U_ ** (da - self.da) * V_ ** (db - self.db)

    def __add__(self, o):
        if not isinstance(o, Hm):
            o = Hm(CTX.from_dict({}) + q(o), 0, 0)
        da, db = max(self.da, o.da), max(self.db, o.db)
        return Hm(self.lift(da, db) + o.lift(da, db), da, db)

    __radd__ = __add__

    def __neg__(self):
        return Hm(-self.p, self.da, self.db)

    def __sub__(self, o):
        return self + (-o)

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if isinstance(o, Hm):
            return Hm(self.p * o.p, self.da + o.da, self.db + o.db)
        return Hm(self.p * q(o), self.da, self.db)

    __rmul__ = __mul__

    def __pow__(self, k):
        return Hm(self.p ** k, self.da * k, self.db * k)


def build(m, shift=G24_SHIFT):
    """returns (K s^3, [Sigma_k s^3]) as Hm, at the scalar m."""
    a = [Hm(x, 1, 0) for x in A_]
    b = [Hm(x, 0, 1) for x in B_]
    S = lambda xs: sum(xs[1:], xs[0])
    A = S([x * x for x in a]); B = S([y * y for y in b])
    c = S([a[i] * b[i] for i in range(4)])
    ta = S([x ** 3 for x in a]); tb = S([y ** 3 for y in b])
    sa = S([x ** 4 for x in a]); sb = S([y ** 4 for y in b])
    p = lambda i, j: S([a[k] ** i * b[k] ** j if i and j else (a[k] ** i if i else b[k] ** j) for k in range(4)])
    s = 1 + c * Fr(1, 4)
    H = [a[k] + b[k] + a[k] * b[k] - c * Fr(1, 4) for k in range(4)]
    N = S([h * h for h in H]); J = S([h ** 3 for h in H])
    s2 = s * s; s3 = s2 * s
    p21, p12, p22 = p(2, 1), p(1, 2), p(2, 2)
    ell = p21 + p12
    kap = c * ell - (B * ta + A * tb) * Fr(1, 3)
    p31s = p(3, 1) + p(1, 3)
    g = g_coeffs(shift)
    phi = {
        0: m * (J * s - (ta + tb) * s3),
        1: (A * B * (A + B)) * s3 - m * (N * N - (A * A + B * B) * s3),
        2: (A + B) * (c * c - A * B * Fr(1, 3)) * s3,
        3: m * (c * c - A * B * Fr(1, 3)) * s3,
        8: (c ** 3 - ta * tb * Fr(2, 3)) * s3,
        10: m * c * (A + B) * s3,
        11: c * ta * tb * s3,
        12: m * ell * s3,
        13: m * (p22 - A * B * Fr(1, 4)) * s3,
        14: m * p31s * s3,
        15: m * c * (ta + tb) * s3,
        16: m * ell * (A + B) * s3,
        17: m * kap * s3,
        18: m * (p(3, 2) + p(2, 3) - (B * ta + A * tb) * Fr(1, 4)) * s3,
        19: (c * p22 - ta * tb * Fr(1, 3)) * s3,
        20: (p(3, 3) - ta * tb * Fr(1, 4)) * s3,
        21: (p(4, 2) + p(2, 4) - (B * sa + A * sb) * Fr(1, 4)) * s3,
        22: m * c * (A * A + B * B) * s3,
        23: (24 * c ** 4 - S([S([a[i] * b[pi[i]] for i in range(4)]) ** 4 for pi in PERMS])) * s3,
        24: (A * B * (A + B) - m * (A * A + B * B)) * s3,
        29: (c * p31s - (B * sa + A * sb) * Fr(1, 3)) * s3,
        30: (p21 * p21 + p12 * p12 - (B * sa + A * sb - A * B * (A + B) * Fr(1, 4)) * Fr(1, 3)) * s3,
        31: (p21 * p12 - ta * tb * Fr(1, 3)) * s3,
        32: (A + B) * (p22 - A * B * Fr(1, 4)) * s3,
    }
    K = ta * tb * Fr(2, 3) * s3 - N * c * c * s2 - m * BETA * A * B * s3
    for j, ph in phi.items():
        if g.get(j, 0):
            K = K + ph * g[j]
    sig = [(A * B * (A + B) - 2 * ta * tb) * s3, (A + B) * (A * B - c * c) * s3,
           m * (A * B - c * c) * s3 if m else None, (A * B * (A + B) + 2 * ta * tb) * s3]
    return K, sig


# ---------------- plain-Fraction evaluator of K (second coding of Table 2) -----------------
def K_direct(a, b, m, shift=G24_SHIFT):
    g = g_coeffs(shift)
    dot = lambda x, y: sum(i * j for i, j in zip(x, y))
    A, B, c = dot(a, a), dot(b, b), dot(a, b)
    ta, tb = sum(x ** 3 for x in a), sum(x ** 3 for x in b)
    sa, sb = sum(x ** 4 for x in a), sum(x ** 4 for x in b)
    P = lambda i, j: sum(a[k] ** i * b[k] ** j for k in range(4))
    s = 1 + c / 4
    H = [a[k] + b[k] + a[k] * b[k] - c / 4 for k in range(4)]
    N, J = sum(h * h for h in H), sum(h ** 3 for h in H)
    F3, F4 = J / s ** 2, N ** 2 / s ** 3
    ell = P(2, 1) + P(1, 2); kap = c * ell - (B * ta + A * tb) / 3; p31 = P(3, 1) + P(1, 3)
    ph = {0: m * (F3 - ta - tb), 1: A * B * (A + B) - m * (F4 - A * A - B * B), 2: (A + B) * (c * c - A * B / 3),
          3: m * (c * c - A * B / 3), 4: kap, 5: c * (A + B), 6: c * (A * A + B * B), 7: B * P(2, 1) + A * P(1, 2),
          8: c ** 3 - Fr(2, 3) * ta * tb, 9: c * A * B, 10: m * c * (A + B), 11: c * ta * tb, 12: m * ell,
          13: m * (P(2, 2) - A * B / 4), 14: m * p31, 15: m * c * (ta + tb), 16: m * ell * (A + B), 17: m * kap,
          18: m * (P(3, 2) + P(2, 3) - (B * ta + A * tb) / 4), 19: c * P(2, 2) - ta * tb / 3, 20: P(3, 3) - ta * tb / 4,
          21: P(4, 2) + P(2, 4) - (B * sa + A * sb) / 4, 22: m * c * (A * A + B * B),
          23: 24 * c ** 4 - sum(dot(a, [b[pi[i]] for i in range(4)]) ** 4 for pi in PERMS),
          24: A * B * (A + B) - m * (A * A + B * B), 25: B * ta + A * tb - m * (ta + tb), 26: m * (A - m) * (B - m),
          27: (A + B) * (A - m) * (B - m), 28: m * m * (A + B - 2 * m), 29: c * p31 - (B * sa + A * sb) / 3,
          30: P(2, 1) ** 2 + P(1, 2) ** 2 - (B * sa + A * sb - A * B * (A + B) / 4) / 3, 31: P(2, 1) * P(1, 2) - ta * tb / 3,
          32: (A + B) * (P(2, 2) - A * B / 4)}
    return Fr(2, 3) * ta * tb - N * c * c / s - BETA * m * A * B + sum(g.get(j, 0) * ph[j] for j in ph)


# ---------------- cases -----------------
ZCTX = flint.fmpq_mpoly_ctx.get(('z0', 'z1', 'z2', 'z3', 'w0', 'w1', 'w2', 'w3'), 'degrevlex')
_z = ZCTX.gens()


def chart(xs, cell):
    x0, x1, x2, x3 = xs
    if cell == 0:
        x0 = x0 + x3      # z0 >= z3
    else:
        x3 = x3 + x0      # z3 >= z0
    lam = [x0, x1, x2, x3]
    coords = [sum((lam[k] * q(VERT[k][i]) for k in range(3)), ZCTX.from_dict({})) for i in range(4)]
    return coords, x0 + x1 + x2 + x3


def substitution(pi, ca, cb):
    al, U = chart(_z[0:4], ca)
    be, V = chart(_z[4:8], cb)
    bb = [be[pi[i]] for i in range(4)]   # b sorted by pi
    return al + [U] + bb + [V], U, V


def point(lam, cell):
    lam = list(lam)
    if cell == 0:
        lam[0] += lam[3]
    else:
        lam[3] += lam[0]
    tot = sum(lam)
    return [sum(lam[k] * VERT[k][i] for k in range(4)) / tot for i in range(4)], lam, tot


def certify(Kh, sig, pi, ca, cb, e_max, gammas):
    subs, U, V = substitution(pi, ca, cb)
    D = (Kh.da, Kh.db)
    Kp = Kh.lift(*D).compose(*subs, ctx=ZCTX)
    Sp = [None if s_ is None else s_.lift(*D).compose(*subs, ctx=ZCTX) for s_ in sig]
    UV = U * V
    for gam in gammas:
        P0 = Kp
        for k, gk in enumerate(gam):
            if gk:
                P0 = P0 - Sp[k] * q(gk)
        P = P0
        for e in range(e_max + 1):
            if e:
                P = P * UV
            cs = P.coeffs()
            neg = sum(1 for x in cs if x < 0)
            if neg == 0:
                return dict(ok=True, e=e, deg=D[0] + e, gamma=[str(x) for x in gam], nterms=len(cs))
    return dict(ok=False, e=e_max, neg=neg, gamma=[str(x) for x in gammas[-1]])


def eval_check(Kh, m, pi, ca, cb, rng, n=3, shift=G24_SHIFT):
    subs, U, V = substitution(pi, ca, cb)
    D = (Kh.da, Kh.db)
    Kp = Kh.lift(*D).compose(*subs, ctx=ZCTX)
    for _ in range(n):
        lz = [Fr(rng.randint(0, 40), rng.randint(1, 9)) for _ in range(4)]
        lw = [Fr(rng.randint(0, 40), rng.randint(1, 9)) for _ in range(4)]
        if not any(lz) or not any(lw):
            continue
        a, lz2, Uz = point(lz, ca)
        bs, lw2, Vw = point(lw, cb)
        b = [bs[pi[i]] for i in range(4)]
        s = 1 + sum(x * y for x, y in zip(a, b)) / 4
        want = K_direct(a, b, m, shift) * s ** 3 * Uz ** D[0] * Vw ** D[1]
        got = Kp(*[q(x) for x in lz + lw])
        if Fr(int(got.p), int(got.q)) != want:
            return False
    return True


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'selftest'
    assert G24_A + G24_SHIFT == G24_B, 'Appendix A g24 representations disagree'
    rng = random.Random(20261018)
    t0 = time.time()
    if mode == 'selftest':
        for m in (Fr(0), M_END):
            Kh, sig = build(m)
            print('m', float(m), 'bidegree', Kh.da, Kh.db, 'terms', len(Kh.p.coeffs()), round(time.time() - t0, 1), 's', flush=True)
            for pi, ca, cb in [(PERMS[0], 0, 0), (PERMS[7], 1, 0), (PERMS[23], 1, 1)]:
                print(' eval', pi, ca, cb, eval_check(Kh, m, pi, ca, cb, rng), flush=True)
        return
    if mode == 'run':
        e_max = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        done = set()
        if os.path.exists('cert_b1e_results.jsonl'):
            for l in open('cert_b1e_results.jsonl', encoding='utf-8'):
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get('ok') and o.get('ev'):
                    done.add((o['m'], tuple(o['pi']), o['ca'], o['cb']))
        out = open('cert_b1e_results.jsonl', 'a', encoding='utf-8')
        gam_list = [(0, 0, 0, 0), (Fr(1, 3), 0, 0, 0), (Fr(1, 2), 0, 0, 0), (0, Fr(1, 4), 0, 0)]
        fails = 0
        for m in (Fr(0), M_END):
            Kh, sig = build(m)
            gl = [g for g in gam_list if not (m == 0 and g[2])]
            for pi in PERMS:
                for ca in (0, 1):
                    for cb in (0, 1):
                        if (str(m), tuple(pi), ca, cb) in done:
                            continue
                        r = certify(Kh, sig, pi, ca, cb, e_max, gl)
                        r.update(m=str(m), pi=list(pi), ca=ca, cb=cb, ev=eval_check(Kh, m, pi, ca, cb, rng, n=1),
                                 t=round(time.time() - t0, 1))
                        fails += (not r['ok']) or (not r['ev'])
                        out.write(json.dumps(r) + '\n'); out.flush()
                        print(json.dumps(r), flush=True)
        print('RUN DONE fails', fails, flush=True)
        return
    if mode == 'control':
        name = sys.argv[2]
        shift = Fr(-1, 10) if name == 'shift' else G24_SHIFT
        Kh, sig = build(M_END if name != 'shift0' else Fr(0), shift)
        tot = 0
        for pi in PERMS:
            for ca in (0, 1):
                for cb in (0, 1):
                    r = certify(Kh, sig, pi, ca, cb, int(sys.argv[3]) if len(sys.argv) > 3 else 1, [(0, 0, 0, 0)])
                    tot += not r['ok']
        print('CONTROL', name, 'cases failing', tot, 'of 96', flush=True)


if __name__ == '__main__':
    main()
