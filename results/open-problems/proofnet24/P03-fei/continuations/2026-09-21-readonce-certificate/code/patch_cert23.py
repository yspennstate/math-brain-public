"""one-off patch: Iv broadcasting, width-attributed directional splitting, region-1 bound with widths"""
import re
p = "fei_cert.py"; s = open(p, encoding="utf-8", newline="").read()
old = '''    def __init__(self, lo, hi=None):
        lo = np.asarray(lo, dtype=float)
        self.lo = lo; self.hi = lo if hi is None else np.asarray(hi, dtype=float)
'''
assert old in s
new = '''    def __init__(self, lo, hi=None):
        lo = np.asarray(lo, dtype=float)
        if hi is None:
            self.lo = lo; self.hi = lo
        else:
            hi = np.asarray(hi, dtype=float)
            if lo.shape != hi.shape:
                lo, hi = np.broadcast_arrays(lo, hi); lo = np.array(lo); hi = np.array(hi)
            self.lo = lo; self.hi = hi
'''
s = s.replace(old, new); open(p, "w", encoding="utf-8", newline="").write(s); print("Iv broadcast fix written")

p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
old = '''    Gg = psit_over_z_iv(v)                                                             # Psi(1-v)/v
    return A_lo + B.lo + Cc.lo + D.lo + Ee.lo + F_lo + Gg.lo
'''
assert old in s
new = '''    Gg = psit_over_z_iv(v)                                                             # Psi(1-v)/v
    lo = A_lo + B.lo + Cc.lo + D.lo + Ee.lo + F_lo + Gg.lo
    gp = Ghat_prime_range(cert, Xl); smax = np.maximum(np.abs(gp.lo), np.abs(gp.hi))
    wx = 2 * cert.Ghat_range(X).width() / v.lo + Cc.width() + p.width() * np.abs(psi_prime_iv(Z).lo)
    wy = B.width() + D.width() + Gg.width() + smax * lam.width() / v.lo
    return lo, wx, wy
'''
s = s.replace(old, new)
old = '''    P3_hi = T1.hi + T2.hi + T3.hi + T4_hi - T5.lo
    return P1.lo + P2_lo - P3_hi
'''
assert old in s
new = '''    P3_hi = T1.hi + T2.hi + T3.hi + T4_hi - T5.lo
    wx = P1.width() + T1.width() + T5.width() + cert.Ghat_range(Xp).width()
    wy = T2.width() + T3.width() + 2 * cert.Ghat_range(Yp).width() + (1 - v.lo) * psit_prime_iv(Zw).width()
    return P1.lo + P2_lo - P3_hi, wx, wy
'''
s = s.replace(old, new)
old_start = s.index("def _adaptive(bound_fn, x0, x1, y0, y1, max_depth, name, chunk=1500000):")
old_end = s.index("def _adaptive1d(")
new = '''def _adaptive(bound_fn, x0, x1, y0, y1, max_depth, name, chunk=1000000):
    """bound_fn returns (lower bound, width attributable to x, width attributable to y); a failing cell is split in two
    along the axis with the larger attributed width"""
    t0 = time.time()
    for depth in range(max_depth + 1):
        lo = np.empty(len(x0)); wx = np.empty(len(x0)); wy = np.empty(len(x0))
        for s in range(0, len(x0), chunk):
            e = min(len(x0), s + chunk)
            lo[s:e], wx[s:e], wy[s:e] = bound_fn(Iv(x0[s:e], x1[s:e]), Iv(y0[s:e], y1[s:e]))
        bad = lo < 0; nb = int(bad.sum())
        print("  %s depth %2d: %9d cells, %8d failing, min lower bound %+.3e  (%.0f s)" % (name, depth, len(x0), nb, lo.min(), time.time() - t0), flush=True)
        if nb == 0:
            return True
        if depth == max_depth:
            j = int(np.argmin(lo))
            print("  FAILED: worst cell [%.6f, %.6f] x [%.6f, %.6f] bound %.3e" % (x0[j], x1[j], y0[j], y1[j], lo[j]))
            return False
        bx0, bx1, by0, by1 = x0[bad], x1[bad], y0[bad], y1[bad]
        sx = wx[bad] >= wy[bad]
        xm = (bx0 + bx1) / 2; ym = (by0 + by1) / 2
        nx0 = np.concatenate([bx0[sx], xm[sx], bx0[~sx], bx0[~sx]]); nx1 = np.concatenate([xm[sx], bx1[sx], bx1[~sx], bx1[~sx]])
        ny0 = np.concatenate([by0[sx], by0[sx], by0[~sx], ym[~sx]]); ny1 = np.concatenate([by1[sx], by1[sx], ym[~sx], by1[~sx]])
        x0, x1, y0, y1 = nx0, nx1, ny0, ny1
    return False

def phi1_lower(cert, X, Y):
    """region 1 bound with width attribution (same bound as fei_cert.verify_region1)"""
    GX = cert.Ghat_range(X); GY = cert.Ghat_range(Y); GS = cert.Ghat_range(X + Y); E = E_iv(X, Y)
    lo = GX.lo + GY.lo - GS.hi - E.hi
    return lo, GX.width() + 0.5 * GS.width() + 0.5 * E.width(), GY.width() + 0.5 * GS.width() + 0.5 * E.width()

def verify_region1_dir(cert, max_depth=30):
    xs = cert.xs; n = len(xs) - 1
    I, Kk = np.triu_indices(n)
    return _adaptive(lambda X, Y: phi1_lower(cert, X, Y), xs[I], xs[I + 1], xs[Kk], xs[Kk + 1], max_depth, "region 1")

'''
s = s[:old_start] + new + s[old_end:]
s = s.replace('    if which in ("all", "R1"): results["R1"] = verify_region1(cert, max_depth)', '    if which in ("all", "R1"): results["R1"] = verify_region1_dir(cert, max_depth)')
open(p, "w", encoding="utf-8", newline="").write(s); print("fei_cert23 patched")
import py_compile; py_compile.compile("fei_cert.py", doraise=True); py_compile.compile("fei_cert23.py", doraise=True); print("both compile")
