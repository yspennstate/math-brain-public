"""Recompute the two REFUTED proof shortcuts (A2-R-lagr1, A2-R-even-weights) with my own code.

(1) A2-R-lagr1, scenario A (E_* empty, every row {0,+-1}-valued): single-multiplier bound
      B(mu) = mu + M_0(mu) + 2 M_1(mu) + M_2(mu),  M_t(mu) = max(0, sup_rows w (e_t - mu)),
    rows = 'ternary' types: f fair coords, unfair coprime pairs (p,q), nu' even with 2 v2(nu') >= e_c + 2,
    w = nu'^2 prod(p^2+q^2) / 4^(r+1) <= 1, e_t = 2 - 2 log2 nu' + 2 f + sum Ft - c (t + f/2 + sum m).
    min over mu of B is computed exactly for a finite menu (B is convex and piecewise linear in mu, so its minimum
    is at a breakpoint; all breakpoints are enumerated).  A positive minimum on a sub-menu is positive on every
    larger menu.  Rigour: the sub-menu 'fair only' (u = 0, nu' = 2) is re-checked with intervals.

(2) A2-R-even-weights, scenario B: odd rows exact (e odd), even rows replaced by their weight only:
      value <= w (delta log2(1/w) - c t - mu) for w in [lo, 1 - 3 lo];
    the minimum over mu of B is computed for rho = 1..12, e odd and even.  A positive value is witnessed rigorously
    by a primal point (four row options with weights summing to 1 and positive total), by weak duality."""
import math, itertools, json, sys
from math import gcd
from mpmath import iv, mpf

C = 16 / 3 - 1.5 * math.log2(3)
DEL = 2 - C / 2
KAP = C / 2 - 1


def h(t):
    return 0.0 if t <= 0 or t >= 1 else -t * math.log2(t) - (1 - t) * math.log2(1 - t)


def Ft(p, q):
    s = p * p + q * q
    return 2 - math.log2(s) + h(q * q / s)


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def min_convex_pwl(lines_by_t, mult, absent):
    """lines_by_t[t] = list of (slope, intercept) meaning w*(e - mu) = -w mu + w e. B(mu) = mu + sum mult_t max(lines).
    Exact minimum of a convex piecewise-linear function: evaluate at all pairwise breakpoints of each M_t and at
    breakpoints between consecutive optimal segments (done here by evaluating B at every candidate kink)."""
    cands = set()
    for t, L in lines_by_t.items():
        Ls = list(L) + ([(0.0, 0.0)] if absent else [])
        # kinks of max of lines are among intersections of pairs; too many pairs -> use upper envelope
        Ls.sort()
        hull = []
        for (a, b) in Ls:   # slopes ascending: build upper envelope
            if hull and hull[-1][0] == a:
                if hull[-1][1] >= b:
                    continue
                hull.pop()
            while len(hull) >= 2:
                (a1, b1), (a2, b2) = hull[-2], hull[-1]
                # remove middle if intersection(1,3) is left of intersection(1,2)
                if (b - b1) * (a2 - a1) >= (b2 - b1) * (a - a1):
                    hull.pop()
                else:
                    break
            hull.append((a, b))
        for (a1, b1), (a2, b2) in zip(hull, hull[1:]):
            cands.add((b1 - b2) / (a2 - a1))
        lines_by_t[t] = hull
    def B(mu):
        tot = mu
        for t, Ls in lines_by_t.items():
            tot += mult[t] * max(a * mu + b for a, b in Ls)
        return tot
    best = min((B(mu), mu) for mu in cands) if cands else (B(0.0), 0.0)
    return best


def scenarioA(RMAX, UMAX, PMAX, NUMAX):
    pairs = [(p, q) for p in range(2, PMAX + 1) for q in range(1, p) if gcd(p, q) == 1]
    rows = []
    for u in range(UMAX + 1):
        for combo in itertools.combinations_with_replacement(pairs, u):
            prodS = 1
            for p, q in combo:
                prodS *= p * p + q * q
            ec = sum(1 for p, q in combo if (p * p + q * q) % 2)
            sF = sum(Ft(p, q) for p, q in combo)
            sm = sum(q * q / (p * p + q * q) for p, q in combo)
            for f in range(RMAX - u + 1):
                r = f + u
                for nu in range(2, NUMAX + 1, 2):
                    if 2 * v2(nu) < ec + 2:
                        continue
                    num = nu * nu * prodS * 2 ** f
                    if num > 4 ** (r + 1):
                        break
                    w = num / 4 ** (r + 1)
                    a = 2 - 2 * math.log2(nu) + 2 * f + sF
                    b = f / 2 + sm
                    rows.append((w, a, b))
    lines = {t: [(-w, w * (a - C * (t + b))) for (w, a, b) in rows] for t in (0, 1, 2)}
    return min_convex_pwl(lines, {0: 1, 1: 2, 2: 1}, True), len(rows)


def scenarioA_fair_rigorous(F):
    """fair-only menu, nu' = 2, f = 0..F: w = 2^-f, e_t = delta f - c t. Rigorous lower bound of min_mu B on a grid
    with the Lipschitz constant of B (slope in [-3, 1]); returns the certified lower bound of min B."""
    iv.dps = 40
    Ci = iv.mpf(16) / 3 - iv.mpf(3) / 2 * iv.log(3) / iv.log(2)
    Di = 2 - Ci / 2
    def B(mu):
        mu = iv.mpf(mu)
        tot = mu
        for t, mlt in ((0, 1), (1, 2), (2, 1)):
            best = iv.mpf(0)
            bl = mpf(0)
            for f in range(F + 1):
                v = iv.mpf(2) ** (-f) * (Di * f - Ci * t - mu)
                if v.a > bl:   # lower endpoint is a valid lower bound of the max
                    bl = v.a
            tot += mlt * iv.mpf(bl)
        return tot.a     # rigorous lower bound of B(mu)
    # B(mu) >= mu always (M >= 0); so only mu in [-M, 0.05] matters when B < 0.05 is sought; for mu < -delta*F...
    # for mu <= -1: M_0 >= -mu (f = 0 term) so B >= M_1, M_2 terms >= 0 and B >= 2 M_1(mu) >= 2 * 2^-F (delta F - c - mu)
    lo, hi, step = -1.0, 0.03, 1e-4
    worst = mpf(10)
    k = 0
    mu = lo
    while mu <= hi:
        b = B(mu)
        if b < worst:
            worst = b
        mu += step
        k += 1
    # Lipschitz: B(mu') >= B(mu) - 3 |mu - mu'| ; grid spacing step -> loss <= 3 step / 2
    return float(worst) - 3 * step / 2, k


def scenarioB_even_weights(rho, e_odd):
    emin = 1 if e_odd else 2
    lo = emin * 2.0 ** (-rho - 2)
    hi = 1 - 3 * lo
    NMAX = 2 ** (rho + 2) - 3 * emin
    odd = []
    if e_odd:
        prs = []
        p = 3
        while (p * p + 1) // 2 <= NMAX:
            for q in range(1, p, 2):
                if gcd(p, q) == 1 and (p * p + q * q) // 2 <= NMAX:
                    prs.append((p, q))
            p += 2
        def Gp(p, q):
            S = p * p + q * q
            return KAP * (math.log2(S) - 2) + C * q * q / S - h(q * q / S)
        def rec(start, prodn, g, u):
            nu = 1
            while prodn * nu * nu <= NMAX:
                N = prodn * nu * nu
                w = N * 2.0 ** (-rho - 2)
                L = rho + 2 - math.log2(N)
                odd.append((w, DEL * L + 2 * KAP * (1 - math.log2(nu)) - g))
                nu += 2
            if u == rho:
                return
            for k in range(start, len(prs)):
                pp, qq = prs[k]
                nn = (pp * pp + qq * qq) // 2
                if prodn * nn <= NMAX:
                    rec(k, prodn * nn, g + Gp(pp, qq), u + 1)
        rec(0, 1, 0.0, 0)
    def M(t, mu):
        f = lambda w: w * (DEL * math.log2(1 / w) - C * t - mu)
        ws = 2.0 ** (-(C * t + mu) / DEL - 1 / math.log(2))
        best = max(f(lo), f(hi), f(min(max(ws, lo), hi)))
        for (w, base) in odd:
            best = max(best, w * (base - C * t - mu))
        return best
    def B(mu):
        return mu + M(0, mu) + 2 * M(1, mu) + M(2, mu)
    a, b = -20.0, 20.0
    for _ in range(200):
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        if B(m1) <= B(m2):
            b = m2
        else:
            a = m1
    mu = (a + b) / 2
    return mu, B(mu), len(odd), lo, hi, odd


def primal_witness_B(rho, e_odd, odd):
    """search a primal point: each of the 4 rows is either an odd option (fixed w) or an even option with free w;
    weights in [lo, hi] summing to 1; value sum w (ebar - c t). Returns the best value found (float) and the point."""
    emin = 1 if e_odd else 2
    lo = emin * 2.0 ** (-rho - 2)
    hi = 1 - 3 * lo
    ts = [0, 1, 1, 2]
    best = (-1e9, None)
    # even rows only (free weights): maximise sum w (delta L - c t) with w in [lo, hi], sum = 1 -> water-filling
    opts = [("even", None)] + [("odd", k) for k in range(len(odd))]
    # restrict: row 0 any option, rows 1,2,12 even or one of the 5 heaviest-value odd options
    for c0 in opts:
        for c1 in [("even", None)] + [("odd", k) for k in range(len(odd))]:
            fixed = 0.0
            val = 0.0
            free = []
            choice = [c0, c1, c1, ("even", None)]
            ok = True
            for s, ch in enumerate(choice):
                if ch[0] == "odd":
                    w, base = odd[ch[1]]
                    fixed += w
                    val += w * (base - C * ts[s])
                else:
                    free.append(s)
            rem = 1 - fixed
            if rem < len(free) * lo - 1e-15 or rem > len(free) * hi + 1e-15 or (not free and abs(rem) > 1e-12):
                continue
            if free:
                # maximise sum_{s in free} w_s (delta log2(1/w_s) - c t_s) s.t. sum = rem, lo <= w_s <= hi:
                # KKT: w_s = clip(2^{-(c t_s + lam)/delta - 1/ln2}); bisection on lam
                def wsum(lam):
                    return sum(min(max(2.0 ** (-(C * ts[s] + lam) / DEL - 1 / math.log(2)), lo), hi) for s in free)
                la, lb_ = -100.0, 100.0
                for _ in range(200):
                    mid = (la + lb_) / 2
                    if wsum(mid) > rem:
                        la = mid
                    else:
                        lb_ = mid
                lam = (la + lb_) / 2
                ws = {s: min(max(2.0 ** (-(C * ts[s] + lam) / DEL - 1 / math.log(2)), lo), hi) for s in free}
                tot = sum(ws.values())
                # rescale tiny mismatch onto an interior variable
                for s in free:
                    if lo < ws[s] < hi:
                        ws[s] += rem - tot
                        break
                for s in free:
                    w = ws[s]
                    val += w * (DEL * math.log2(1 / w) - C * ts[s])
            if val > best[0]:
                best = (val, choice)
    return best


if __name__ == "__main__":
    out = {}
    print("(1) scenario A single-multiplier bound (exact min over mu of the piecewise-linear convex B):")
    for (R, U, P, NU) in [(6, 0, 2, 8), (10, 0, 2, 64), (10, 2, 7, 64), (10, 3, 9, 64)]:
        (val, mu), nrows = scenarioA(R, U, P, NU)
        print(f"  menu RMAX={R} UMAX={U} PMAX={P} NUMAX={NU}: {nrows} row types; min_mu B = {val:+.6f} at mu = {mu:+.5f}",
              flush=True)
        out[f"A_R{R}_U{U}_P{P}_NU{NU}"] = dict(rows=nrows, minB=val, mu=mu)
    lbB, k = scenarioA_fair_rigorous(14)
    print(f"  rigorous: fair-only menu (nu'=2, f<=14): min_mu B >= {lbB:+.6f} (grid of {k} points, Lipschitz 3)")
    out["A_fair_rigorous_lower_bound"] = lbB
    print("(2) scenario B, even rows kept by weight only:")
    for rho in range(1, 13):
        for e_odd in (True, False):
            mu, val, nodd, lo, hi, odd = scenarioB_even_weights(rho, e_odd)
            line = f"  rho={rho:2d} e {'odd ' if e_odd else 'even'}: min_mu B ~ {val:+.6f} (mu {mu:+.4f}, odd options {nodd})"
            if val > 0 and rho <= 6:
                pv, pt = primal_witness_B(rho, e_odd, odd)
                line += f"; primal witness value {pv:+.6f}"
                out[f"B_rho{rho}_{'odd' if e_odd else 'even'}_primal"] = pv
            print(line, flush=True)
            out[f"B_rho{rho}_{'odd' if e_odd else 'even'}"] = val
    gibbs = 2 * DEL * math.log2(1 + 2 ** (-C / DEL))
    print("  Gibbs gap 2 delta log2(1 + 2^{-c/delta}) =", gibbs)
    out["gibbs_gap"] = gibbs
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "ref_refutations.json", "w", encoding="utf-8"), indent=1)
