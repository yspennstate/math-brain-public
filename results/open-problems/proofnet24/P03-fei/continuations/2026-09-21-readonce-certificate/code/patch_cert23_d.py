"""patch: region-3 width attribution from the forms actually used (case a / case b direct forms, T4 direct)"""
p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
start = s.index("def phi3_over_u_lower(cert, Xp, Yp):")
end = s.index("def verify_region3(")
new = '''def phi3_over_u_lower(cert, Xp, Yp):
    """lower bound of Phi/u on the cell x' in Xp, y' in Yp (u = 2^-x' <= v = 2^-y'); returns (lo, wx, wy) where wx, wy
    are the widths attributable to the x' and y' axes through the enclosures actually used"""
    n = len(Xp.lo)
    u = exp2neg(Xp); v = exp2neg(Yp); ellu = ell_iv(u); ellv = ell_iv(v)
    w = u + v - u * v                                    # w = 1 - pq
    ulo = np.maximum(u.lo, 1e-300)
    P1 = cert.Ghat_range(Xp) / (1 - u)
    res_a = np.full(n, np.inf); res_b = np.full(n, np.inf)
    wax = np.zeros(n); way = np.zeros(n); wbx = np.zeros(n); wby = np.zeros(n)
    # case (a): w <= 1/2 -> G(pq) = Lambda(w); valid on the part of the cell where w <= 1/2
    a_mask = w.lo <= 0.5
    if a_mask.any():
        sel = a_mask
        va = Iv(v.lo[sel], v.hi[sel]); wa = Iv(w.lo[sel], np.minimum(w.hi[sel], 0.5)); ua = Iv(u.lo[sel], u.hi[sel])
        Zr = Iv(va.lo, wa.hi)
        P2_mv = -(1 - va) * Lambda_prime_range(cert, Zr)
        Lv = Lambda_range(cert, va); Lw = Lambda_range(cert, wa)
        P2_dir = (Lv - Lw) / ua
        use_dir = P2_dir.lo >= P2_mv.lo
        res_a[sel] = np.maximum(P2_mv.lo, P2_dir.lo)
        # widths of the used form: direct -> Lambda(v) width (y), Lambda(w) width (half x, half y), |P2| du/u (x);
        # mean value -> (1-v) Lambda' width over [v, w]: shrinks with v only through the z-range, attribute to y
        dx = np.where(use_dir, 0.5 * Lw.width() / ulo[sel] + np.abs(P2_dir.lo) * ua.width() / ulo[sel], np.abs(P2_mv.lo) * 0.0)
        dy = np.where(use_dir, (Lv.width() + 0.5 * Lw.width()) / ulo[sel], P2_mv.width())
        wax[sel] = dx; way[sel] = dy
    # case (b): w >= 1/2 -> G(pq) = G_hat(L(pq)), L(pq) = 1 + [u ell(u)/ln2 - log1p(m)/ln2], m = 1 - 2v = -expm1((1-y') ln2)
    b_mask = w.hi >= 0.5
    if b_mask.any():
        sel = b_mask
        ub = Iv(u.lo[sel], u.hi[sel]); vb = Iv(v.lo[sel], v.hi[sel]); Yb = Iv(Yp.lo[sel], Yp.hi[sel])
        mlo = paddn(-np.expm1((1 - Yb.lo) * np.log(2.0))); mhi = padup(-np.expm1((1 - Yb.hi) * np.log(2.0)))
        m = Iv(np.maximum(mlo, 0.0), np.maximum(mhi, 0.0))
        l1pm = Iv(paddn(np.log1p(m.lo)), padup(np.log1p(m.hi)))
        Lpq_m1 = (ub * ell_iv(ub) - l1pm) / LN2
        Lpq_m1 = Iv(np.maximum(Lpq_m1.lo, 0.0), np.maximum(Lpq_m1.hi, 0.0))
        half_minus_v = m / 2
        Z1 = Iv(vb.lo, np.full_like(vb.lo, 0.5))
        lam1 = Lambda_prime_range(cert, Z1)
        X1 = Iv(np.ones_like(ub.lo), UP(1 + Lpq_m1.hi))
        gp1 = Ghat_prime_range(cert, X1)
        P2_mv = -(half_minus_v / ub) * lam1 - (Lpq_m1 / ub) * gp1
        Lv = Lambda_range(cert, vb); GL = cert.Ghat_range(1 + Lpq_m1)
        P2_dir = (Lv - GL) / ub
        use_dir = P2_dir.lo >= P2_mv.lo
        res_b[sel] = np.maximum(P2_mv.lo, P2_dir.lo)
        dx = np.where(use_dir, 0.5 * GL.width() / ulo[sel] + np.abs(P2_dir.lo) * ub.width() / ulo[sel], 0.5 * P2_mv.width())
        dy = np.where(use_dir, (Lv.width() + 0.5 * GL.width()) / ulo[sel], 0.5 * P2_mv.width())
        wbx[sel] = dx; wby[sel] = dy
    P2_lo = np.minimum(res_a, res_b)
    # the case whose bound is the binding one contributes its widths
    use_a = res_a <= res_b
    wPx = np.where(use_a, wax, wbx); wPy = np.where(use_a, way, wby)
    # P3 = E/u
    T1 = 8 * (1 - u) * v * ellu / LN2
    T2 = 8 * (1 - v) * v * ellv / LN2
    T3 = 8 * v
    Zw = Iv(v.lo, np.minimum(w.hi, 0.75))
    T4_mv = (1 - v) * psit_prime_iv(Zw)                              # [Psit(w) - Psit(v)]/u = (1-v) Psit'(xi)
    T4_dir = (psit_iv(w) - psit_iv(v)) / u
    T4_hi = np.minimum(T4_mv.hi, T4_dir.hi)
    T4_w = np.minimum(T4_mv.width(), T4_dir.width())
    T5 = psit_over_z_iv(u)                                           # Psit(u)/u
    P3_hi = T1.hi + T2.hi + T3.hi + T4_hi - T5.lo
    wx = P1.width() + T1.width() + T5.width() + wPx + 0.5 * T4_w
    wy = T2.width() + T3.width() + wPy + 0.5 * T4_w
    return P1.lo + P2_lo - P3_hi, wx, wy

'''
s = s[:start] + new + s[end:]
open(p, "w", encoding="utf-8", newline="").write(s)
import py_compile; py_compile.compile(p, doraise=True); print("phi3 attribution rewritten, compiles")
