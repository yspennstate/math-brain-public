"""Reviewer extension of T240 C6: certify the plateau family on a real eta interval by subdivision.
Reuses worker U's interval engine (iv_exact, iv_scm) unchanged; the per-cell test is the same as certify_plateau.py.
Usage: python widen_eta.py ETA_LO ETA_HI WIDTH OUT.jsonl
"""
import sys, json, time
from fractions import Fraction
from iv_exact import I, S, pi
from iv_scm import variables, full_driver, symmetric_driver, determinant
from certify_plateau import invert_rational

def mid(v): return Fraction(v.lo + v.hi, 2 * S)

def newton(x, eta):
    """Float-quality Newton on point intervals (diagnostic only; the certificate is the cell test)."""
    for _ in range(30):
        f = symmetric_driver([I.of(v) for v in x], I.of(eta))
        F = [mid(r.v) for r in f]
        J = [[mid(d) for d in r.d] for r in f]
        A = invert_rational(J)
        step = [sum(A[i][l] * F[l] for l in range(3)) for i in range(3)]
        x = [Fraction(float(x[i] - step[i])).limit_denominator(10 ** 18) for i in range(3)]
        if max(abs(float(s)) for s in step) < 1e-16:
            break
    return x

def cell(eta_lo, eta_hi, center, radius):
    c = [I.of(v) for v in center]
    eta0 = I(I.of(eta_lo).lo, I.of(eta_hi).hi)
    f00 = symmetric_driver(c, eta0)
    a00 = invert_rational([[mid(v) for v in row.d] for row in f00])
    spread = max(sum((I.of(a00[i][l]) * f00[l].v).maxabs() for l in range(3)) for i in range(3))
    rad = max(3 * spread, I.of(radius).hi)
    box = [I(v.lo - rad, v.hi + rad) for v in c]
    eta = I(I.of(eta_lo).lo, I.of(eta_hi).hi)
    f0 = symmetric_driver(c, eta)
    fb = symmetric_driver(box, eta)
    jac = [list(row.d) for row in fb]
    a_rat = invert_rational([[mid(v) for v in row] for row in jac])
    if determinant(a_rat) == 0: return 'singular', None
    A = [[I.of(v) for v in row] for row in a_rat]
    M = [[I.of(int(i == j)) - sum(A[i][l] * jac[l][j] for l in range(3)) for j in range(3)] for i in range(3)]
    image = [c[i] - sum(A[i][l] * f0[l].v for l in range(3)) + sum(M[i][j] * (box[j] - c[j]) for j in range(3)) for i in range(3)]
    if not all(b.lo < x.lo and x.hi < b.hi for b, x in zip(box, image)): return 'krawczyk', None
    if not max(sum(v.maxabs() for v in row) for row in M) < S: return 'contraction', None
    q, cc, r = box
    if not all(v.positive() for v in [q - cc, q + cc - 4 * r.square()]): return 'physical', None
    a1 = -sum(jac[i][i] for i in range(3))
    a2 = sum(jac[i][i] * jac[j][j] - jac[i][j] * jac[j][i] for i in range(3) for j in range(i + 1, 3))
    a3 = -determinant(jac)
    if not all(v.positive() for v in [a1, a2, a3, a1 * a2 - a3]): return 'hurwitz', None
    j7 = [list(row.d) for row in full_driver(variables([q, cc, q, r, r, r, r]), eta)]
    V = [[1, 0], [0, 0], [-1, 0], [0, 1], [0, 1], [0, -1], [0, -1]]
    W = [[Fraction(1, 2), 0, Fraction(-1, 2), 0, 0, 0, 0], [0, 0, 0, Fraction(1, 4), Fraction(1, 4), Fraction(-1, 4), Fraction(-1, 4)]]
    j2 = [[sum(I.of(W[a][i]) * j7[i][j] * V[j][b] for i in range(7) for j in range(7)) for b in range(2)] for a in range(2)]
    if not ((j2[0][0] + j2[1][1]).negative() and determinant(j2).positive()): return 'odd2', None
    mu = 2 / pi()
    As = mu / (1 + 2 * q).sqrt(); Ac = mu / ((1 + q).square() - cc.square()).sqrt()
    T = mu / (2 * (1 + q) - r.square()).sqrt()
    beta = (q * As + cc * Ac - 2 * r * T) / (1 + q)
    Tp = mu * r / ((2 * (1 + q) - r.square()) * (2 * (1 + q) - r.square()).sqrt())
    common = eta * (Tp + beta - As - Ac); lam = eta * (Tp + beta - As + Ac)
    if not (common.negative() and lam.positive()): return 'teacher_odd', None
    return 'pass', [rad / S, float(mid(lam)) - (lam.hi - lam.lo) / (2 * S), (lam.hi) / S, float(min((q - cc).lo, (q + cc - 4 * r.square()).lo)) / S]

def run(lo, hi, width, out):
    lo, hi, width = Fraction(lo), Fraction(hi), Fraction(width)
    x = [Fraction('0.36771969907760643'), Fraction('0.32538554792403124'), Fraction('0.4143941508524791')]
    x = newton(x, Fraction(1, 2))
    # continue the root from 1/2 to lo first if lo < 1/2 (direction of travel: upward from lo)
    e = Fraction(1, 2)
    while e > lo:
        e = max(lo, e - Fraction(1, 100)); x = newton(x, e)
    stack = []
    a = lo
    with open(out, 'a') as fh:
        while a < hi:
            w = min(width, hi - a)
            ok = False
            while not ok:
                b = a + w
                m = (a + b) / 2
                xm = newton(x, m)
                xa = newton(xm, a); xb = newton(xm, b)
                drift = max(abs(float(xa[i] - xm[i])) for i in range(3)) + max(abs(float(xb[i] - xm[i])) for i in range(3))
                radius = Fraction(max(2 * drift, 1e-9)).limit_denominator(10 ** 15)
                why, info = cell(a, b, xm, radius)
                rec = {'eta_lo': str(a), 'eta_hi': str(b), 'radius_floor': float(radius), 'result': why, 'info': info,
                       'center': [float(v) for v in xm], 't': time.strftime('%H:%M:%S')}
                fh.write(json.dumps(rec) + '\n'); fh.flush()
                if why == 'pass':
                    ok = True; x = xb; a = b
                else:
                    w = w / 2
                    if w < Fraction(1, 10 ** 7):
                        fh.write(json.dumps({'stop': 'width underflow', 'at': str(a)}) + '\n'); return
    print('covered', str(lo), str(hi))

if __name__ == '__main__':
    import os
    if os.name == 'nt':
        import ctypes
        k = ctypes.WinDLL('kernel32'); k.GetCurrentProcess.restype = ctypes.c_void_p
        k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]; k.SetPriorityClass(k.GetCurrentProcess(), 0x4000)
    run(*sys.argv[1:4], sys.argv[4])
