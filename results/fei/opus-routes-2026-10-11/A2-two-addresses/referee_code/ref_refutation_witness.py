"""Rigorous primal witnesses for A2-R-even-weights (scenario B, even rows kept by weight only).
By weak duality, mu + sum_T sup_rows w (v - mu) >= sum_T w_T v_T for any feasible choice with sum w_T = 1, so a
feasible point with positive value proves that the single-multiplier bound is positive for EVERY mu.
Each witness: exact rational weights (sum exactly 1, each in [lo, 1 - 3 lo]), values in mpmath intervals."""
from fractions import Fraction
from math import gcd
from mpmath import iv, mpf
import ref_refutations as RR
iv.dps = 40
L2 = iv.log(2)
def log2(x): return iv.log(x) / L2
C = iv.mpf(16) / 3 - iv.mpf(3) / 2 * log2(iv.mpf(3))
DEL = 2 - C / 2
KAP = C / 2 - 1
def h(t):
    t = iv.mpf(t); return -(t * log2(t) + (1 - t) * log2(1 - t))
def G(p, q):
    S = p * p + q * q
    return KAP * (log2(iv.mpf(S)) - 2) + C * iv.mpf(q * q) / S - h(iv.mpf(q * q) / S)
ts = [0, 1, 1, 2]
for rho, e_odd in [(3, True), (4, True), (5, True), (6, False)]:
    mu, val, nodd, lo, hi, odd = RR.scenarioB_even_weights(rho, e_odd)
    pv, choice = RR.primal_witness_B(rho, e_odd, odd)
    # rebuild the odd options with their exact data (N, nu', pairs) in the same enumeration order
    emin = 1 if e_odd else 2
    NMAX = 2 ** (rho + 2) - 3 * emin
    prs = []
    p = 3
    while (p * p + 1) // 2 <= NMAX:
        for q in range(1, p, 2):
            if gcd(p, q) == 1 and (p * p + q * q) // 2 <= NMAX:
                prs.append((p, q))
        p += 2
    exact = []
    def rec(start, prodn, chosen, u):
        nu = 1
        while prodn * nu * nu <= NMAX:
            exact.append((prodn * nu * nu, nu, list(chosen)))
            nu += 2
        if u == rho:
            return
        for k in range(start, len(prs)):
            pp, qq = prs[k]
            nn = (pp * pp + qq * qq) // 2
            if prodn * nn <= NMAX:
                chosen.append((pp, qq)); rec(k, prodn * nn, chosen, u + 1); chosen.pop()
    if e_odd:
        rec(0, 1, [], 0)
    assert len(exact) == len(odd)
    loF = Fraction(emin, 2 ** (rho + 2)); hiF = 1 - 3 * loF
    # weights: odd rows exact; even rows: recompute the float optimum then rationalise and fix the sum
    fixed = Fraction(0); free = []
    for s, ch in enumerate(choice):
        if ch[0] == "odd":
            fixed += Fraction(exact[ch[1]][0], 2 ** (rho + 2))
        else:
            free.append(s)
    rem = 1 - fixed
    import math
    Cf = float(C.mid); Df = float(DEL.mid)
    def wsum(lam):
        return sum(min(max(2.0 ** (-(Cf * ts[s] + lam) / Df - 1 / math.log(2)), float(loF)), float(hiF)) for s in free)
    la, lb = -100.0, 100.0
    for _ in range(200):
        mid = (la + lb) / 2
        if wsum(mid) > float(rem): la = mid
        else: lb = mid
    wf = {s: min(max(2.0 ** (-(Cf * ts[s] + la) / Df - 1 / math.log(2)), float(loF)), float(hiF)) for s in free}
    wq = {s: Fraction(wf[s]).limit_denominator(10 ** 9) for s in free}
    # clamp to the box and put the rounding residue on the largest free weight
    for s in free:
        wq[s] = min(max(wq[s], loF), hiF)
    big = max(free, key=lambda s: wq[s])
    wq[big] += rem - sum(wq.values())
    assert loF <= wq[big] <= hiF
    total = iv.mpf(0)
    wsumF = fixed + sum(wq.values())
    assert wsumF == 1
    desc = []
    for s, ch in enumerate(choice):
        if ch[0] == "odd":
            N, nu, pr = exact[ch[1]]
            w = iv.mpf(N) / 2 ** (rho + 2)
            L = rho + 2 - log2(iv.mpf(N))
            v = DEL * L + 2 * KAP * (1 - log2(iv.mpf(nu)))
            for (pp, qq) in pr:
                v -= G(pp, qq)
            v -= C * ts[s]
            total += w * v
            desc.append(f"T{s}: odd row N={N} nu'={nu} pairs={pr} w={Fraction(N, 2**(rho+2))}")
        else:
            wF = wq[s]
            w = iv.mpf(wF.numerator) / wF.denominator
            total += w * (DEL * log2(1 / w) - C * ts[s])
            desc.append(f"T{s}: even row (weight only) w={float(wF):.6f}")
    print(f"rho={rho} e {'odd' if e_odd else 'even'}: primal witness value in [{float(total.a):+.6f}, {float(total.b):+.6f}]",
          "POSITIVE" if total.a > 0 else "NOT CERTIFIED")
    for d in desc:
        print("   ", d)
