"""Interval certificate for the numerical constants of route L2.

Every constant here has the form  K = sup_{L >= 0} F(L),  L = ln(1/eps),  F(L) = sum_{j in J(L)} t(rho_j(L), L), where
  t(r, L) = r (1 + ln(1/r) + L) / ln 2        (so eps * t(rho, L) = psi(rho * eps), psi(x) = x log2(e/x)),
  rho_j(L) >= d_{j,i} / eps_i is an upper bound that is non-increasing in L:
    j = 0       rho = e^{-L}                                          (|fhat(i)| <= eps_i)
    j = 1, ent  rho = min(1, 2 e^{-L} (L + ln 2))                     (level-1 inequality for {0,+-1} functions)
    j >= 1, bon rho = min(1, exp(-L (1 - 2/q) + j ln(q - 1)))  any q >= 2   (Bonami), q = q*(L, j) in closed form.
t is increasing in r on (0, 1] (dt/dr = (ln(1/r) + L)/ln 2 >= 0) and in L.  Hence on a cell [La, Lb):
  t(rho_j(L), L) <= t(rbar_j, Lb),  rbar_j = min(1, bound_j(Lleft)),  Lleft = La, or j/c for a term that enters
  inside the cell (localized sums, J(L) = {0..floor(c L)}).
The cell bounds are first searched in float64 with bisection down to the target, then every final cell is
re-evaluated in mpmath interval arithmetic (outward rounding) and only the upper endpoints are used.
Tails L >= Lmax use one fixed q and a closed form that is decreasing in L past an explicit point.
Constants: b_2^ent (ent branch alone), b_2 (ent and bon), b_k for k = 3..10 (bon), C(c) for c = 0.2, 0.3, 0.4, 0.45.
Usage: python certify_constants.py OUTJSON [names...]
"""
import os, sys, json, math, time
from fractions import Fraction

try:  # BelowNormal priority
    import ctypes
    from ctypes import wintypes
    _k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _k32.GetCurrentProcess.restype = wintypes.HANDLE
    _k32.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    _k32.SetPriorityClass.restype = wintypes.BOOL
    _k32.SetPriorityClass(_k32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

from mpmath import iv, mpf

iv.prec = 80
LN2 = math.log(2.0)
IV_LN2 = iv.log(2)


# ----------------------------------------------------------------- rho bounds (float and interval)
def qstar(L, j):
    """minimiser over q >= 2 of -L(1-2/q) + j ln(q-1); None when the minimum value is >= 0 (bound capped at 1)."""
    if L < 2 * j:
        return None
    x = ((L - j) + math.sqrt(L * (L - 2 * j))) / j
    return 1.0 + x


def rho_float(L, j, branches):
    if j == 0:
        return math.exp(-L)
    r = 1.0
    if "bon" in branches:
        q = qstar(L, j)
        if q is not None:
            lr = -L * (1 - 2 / q) + j * math.log(q - 1)
            r = min(r, math.exp(min(0.0, lr)))
    if j == 1 and "ent" in branches and L >= 1.0:
        r = min(r, 2 * math.exp(-L) * (L + LN2))
    return r


def rho_iv_upper(L, j, branches):
    """rigorous upper bound (an mpf) for the rho bound at the point L (a float or an mpf, taken exactly)."""
    Li = iv.mpf(L)
    one = mpf(1)
    if j == 0:
        return min(one, iv.exp(-Li).b)
    r = one
    if "bon" in branches:
        q = qstar(float(L), j)
        if q is not None:
            qi = iv.mpf(q)
            lr = -Li * (1 - 2 / qi) + j * iv.log(qi - 1)
            r = min(r, iv.exp(lr).b)
    if j == 1 and "ent" in branches and L >= 1.0:
        r = min(r, (2 * iv.exp(-Li) * (Li + IV_LN2)).b)
    return r


def t_float(r, L):
    if r <= 0.0:
        return 0.0
    return (r * (1 - math.log(r) + L)) / LN2 if r < 1 else (1 + L) / LN2   # -log r: 1/r overflows for denormal r


def t_iv_upper(r, L):
    """rigorous upper endpoint (an mpf) of t(r, L) for r in (0, 1] (mpf, exact) and a float L."""
    ri, Li = iv.mpf(r), iv.mpf(L)
    if r >= 1:
        v = (1 + Li) / IV_LN2
    else:
        v = ri * (1 + iv.log(1 / ri) + Li) / IV_LN2
    return v.b


# ----------------------------------------------------------------- cell bounds
def jrange(La, Lb, spec):
    """(base, extra): base terms present for every L in [La, Lb); extra terms j enter at L = j/c inside the cell."""
    if spec["kind"] == "level":
        return [spec["j"]], []
    c = spec["c"]
    base_top = math.floor(Fraction(La) * c)
    top = math.ceil(Fraction(Lb) * c) - 1          # max floor(cL) over L < Lb
    return list(range(0, base_top + 1)), list(range(base_top + 1, top + 1))


def enter_point_lower(j, c):
    """an mpf <= j/c (rigorous)."""
    v = iv.mpf(j * c.denominator) / iv.mpf(c.numerator)
    return v.a


def cell_float(La, Lb, spec):
    base, extra = jrange(La, Lb, spec)
    br = spec["branches"]
    s = 0.0
    for j in base:
        s += t_float(rho_float(La, j, br), Lb)
    for j in extra:
        s += t_float(rho_float(max(La, float(j / spec["c"])), j, br), Lb)
    return s


def cell_iv(La, Lb, spec):
    """rigorous upper bound (an mpf) for sup of F over [La, Lb)."""
    base, extra = jrange(La, Lb, spec)
    br = spec["branches"]
    s = iv.mpf(0)
    for j in base:
        s += iv.mpf(t_iv_upper(rho_iv_upper(La, j, br), Lb))
    for j in extra:
        e = enter_point_lower(j, spec["c"])
        Lleft = e if e > La else mpf(La)
        s += iv.mpf(t_iv_upper(rho_iv_upper(Lleft, j, br), Lb))
    return s.b


def F_point(L, spec):
    """float value of the majorant at a point (a lower estimate of the sup when maximised over a grid)."""
    br = spec["branches"]
    if spec["kind"] == "level":
        js = [spec["j"]]
    else:
        js = range(0, math.floor(Fraction(L) * spec["c"]) + 1)
    return sum(t_float(rho_float(L, j, br), L) for j in js)


# ----------------------------------------------------------------- tails
def tail_bound(spec, Lmax):
    """rigorous bound on sup_{L >= Lmax} F(L), with the conditions it needs checked; returns (value, note)."""
    if spec["kind"] == "level" and spec["branches"] == ("ent",):
        assert Lmax >= 3
        L = iv.mpf(Lmax)
        v = 2 * iv.exp(-L) * (L + IV_LN2) * (1 + 2 * L) / IV_LN2
        return v.b, "rho<=2e^-L(L+ln2), ln(1/rho)<=L, 2e^-L(L+ln2)(1+2L) decreasing for L>=2"
    if spec["kind"] == "level":
        j = spec["j"]
        q = 4.0
        sig = 1 - 2 / q
        assert Lmax >= 1 / sig
        L = iv.mpf(Lmax)
        Cq = iv.mpf(q - 1) ** j
        R = Cq * iv.exp(-sig * L)
        assert R.b <= 1
        v = R * (1 + (1 + sig) * L) / IV_LN2
        return v.b, "q=4: rho<=3^j e^{-L/2}; C e^{-sL}(1+(1+s)L) decreasing for L>=1/s-1/(1+s)"
    c = spec["c"]
    cf = float(c)
    x = ((1 - cf) + math.sqrt(1 - 2 * cf)) / cf
    q = 1 + x
    qi = iv.mpf(q)
    s = (1 - 2 / qi) - iv.mpf(c.numerator) / c.denominator * iv.log(qi - 1)
    assert s.a > 0 and q - 1 >= 1
    assert Lmax >= 2 / s.a
    L = iv.mpf(Lmax)
    R = iv.exp(-s * L)
    v = (iv.mpf(c.numerator) / c.denominator * L + 1) * R * (1 + (1 + s) * L) / IV_LN2
    return v.b, f"q={q:.6f}, s={float(s.a):.6f}: every term rho_j<=e^(-sL) for j<=cL; (cL+1)e^(-sL)(1+(1+s)L)/ln2 decreasing for L>=2/s"


# ----------------------------------------------------------------- driver
def initial_cells(Lmax, Lgeo, ratio1, Lcoarse, ratio2):
    pts = [i * 0.01 for i in range(int(round(Lgeo / 0.01)) + 1)]
    L = pts[-1]
    while L < Lmax:
        L = min(Lmax, L * (ratio1 if L < Lcoarse else ratio2))
        pts.append(L)
    return list(zip(pts[:-1], pts[1:]))


def certify(name, spec, Lmax, target, Lcoarse, max_rounds=60):
    t0 = time.time()
    cells = initial_cells(Lmax, 10.0, 1.002, Lcoarse, 1.02)
    # grid lower estimate of sup F (float)
    best = (0.0, 0.0)
    for (a, b) in cells:
        for L in (a, 0.5 * (a + b)):
            v = F_point(L, spec)
            if v > best[0]:
                best = (v, L)
    if spec["kind"] == "loc":  # the sup sits at an entry point j/c (right limit); evaluate there
        c = spec["c"]
        for j in range(0, math.floor(Fraction(Lmax) * c) + 1):
            L = float(Fraction(j) / c)
            L = math.nextafter(L, math.inf) if Fraction(L) * c < j else L
            if L <= Lmax:
                v = F_point(L, spec)
                if v > best[0]:
                    best = (v, L)
    # local refinement around the 30 best grid cells (the grid alone can sit 1e-4 below a smooth maximum)
    scored = sorted(((max(F_point(a, spec), F_point(0.5 * (a + b), spec)), a, b) for (a, b) in cells), reverse=True)[:30]
    for (_, a, b) in scored:
        w = b - a
        lo, hi = max(0.0, a - 2 * w), b + 2 * w
        for t in range(2001):
            L = lo + (hi - lo) * t / 2000
            v = F_point(L, spec)
            if v > best[0]:
                best = (v, L)
    if target is None:
        target = math.ceil((best[0] + 2e-5) * 1e4) / 1e4
    final = []
    work = cells
    rounds = 0
    while work and rounds < max_rounds:
        if len(work) > 400000:
            raise RuntimeError(f"{name}: {len(work)} cells above target {target} at round {rounds}; the target is below the sup")
        nxt = []
        for (a, b) in work:
            u = cell_float(a, b, spec)
            if u <= target * (1 - 1e-9):
                final.append((a, b, u))
            else:
                m = 0.5 * (a + b)
                if not (a < m < b):
                    raise RuntimeError(f"{name}: cannot split cell [{a},{b}] (u={u} > target {target})")
                nxt += [(a, m), (m, b)]
        work = nxt
        rounds += 1
    if work:
        raise RuntimeError(f"{name}: {len(work)} cells still above target {target} after {rounds} rounds")
    tf = time.time()
    T_low = iv.mpf(repr(target)).a          # the decimal target, rounded down
    worst_iv = mpf(0)
    worst_cell = None
    n_over = 0
    for (a, b, u) in final:
        w = cell_iv(a, b, spec)
        if w > T_low:
            n_over += 1
        if w > worst_iv:
            worst_iv, worst_cell = w, (a, b, u)
    tail, tail_note = tail_bound(spec, Lmax)
    ok = (n_over == 0) and (tail <= T_low)
    worst_iv = float(worst_iv)
    tail = float(tail)
    res = dict(name=name, spec={k: (str(v) if isinstance(v, Fraction) else v) for k, v in spec.items()},
               certified_upper_bound=target, ok=bool(ok), grid_lower_estimate=best[0], grid_argmax_L=best[1],
               grid_argmax_eps=math.exp(-best[1]), cells=len(final), refinement_rounds=rounds,
               worst_cell_interval_upper=worst_iv, worst_cell=worst_cell, Lmax=Lmax, tail_bound=tail, tail_note=tail_note,
               seconds_float=tf - t0, seconds_interval=time.time() - tf)
    print(f"{name:10s} ok={ok} certified<= {target}  grid {best[0]:.6f} at L={best[1]:.4f}  cells {len(final)}  "
          f"worst iv {worst_iv:.6f}  tail {tail:.2e}  ({time.time() - t0:.0f}s)", flush=True)
    return res


SPECS = {
    "b2_ent": (dict(kind="level", j=1, branches=("ent",)), 60.0, None, 60.0),
    "b2": (dict(kind="level", j=1, branches=("ent", "bon")), 60.0, None, 60.0),
}
for k in range(3, 11):
    SPECS[f"b{k}"] = (dict(kind="level", j=k - 1, branches=("bon",)), max(60.0, 2 * (k - 1) * math.log(3) + 60), None, 100.0)
for c, Lmax, Lc in ((Fraction(1, 5), 100.0, 50.0), (Fraction(3, 10), 250.0, 60.0), (Fraction(2, 5), 800.0, 100.0),
                    (Fraction(9, 20), 2500.0, 250.0)):
    SPECS[f"C({float(c)})"] = (dict(kind="loc", c=c, branches=("ent", "bon")), Lmax, None, Lc)


def main():
    out_path = sys.argv[1]
    names = sys.argv[2:] or list(SPECS)
    res = {}
    if os.path.exists(out_path):
        try:
            res = json.load(open(out_path, encoding="utf-8"))
        except Exception:
            res = {}
    for nm in names:
        spec, Lmax, target, Lc = SPECS[nm]
        res[nm] = certify(nm, spec, Lmax, target, Lc)
        json.dump(res, open(out_path, "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
