"""Arithmetic relaxation of K2: rows are replaced by abstract 'row types' carrying only the data that
Lemmas 3-5 constrain, and H/I is maximised over admissible combinations of four types with exact total weight 1.

Row type: f fair coordinates, u <= UMAX unfair coordinates (p,q) (coprime, p>q>=1, p<=PMAX), integer nu' >= 1,
class in {odd, evenhalf, ternary}; r = f+u <= RMAX.
  weight w = nu'^2 prod(p^2+q^2) / 4^(r+1)   (Lemma 3b), must be <= 1
  odd class: nu' odd, all p,q odd                     (Lemma 3d)
  even classes: nu' even, 2 v2(nu') >= e_c (+2 if ternary), e_c = #{unfair with p^2+q^2 odd}
     (integrality: 4 w 2^r = sum (2phi)^2 is an integer, and divisible by 4 for {0,+-1}-valued rows)
  a = L + H(q) = 2 - 2 log2 nu' + 2 f + sum Ft(p,q);   b = I(q) >= f/2 + sum m  (small side, D1 empty)
Scenario A: all rows ternary, any positions may be absent, sum w = 1.
Scenario B: all rows half-valued, all four present, rho = |R_cap| >= 0; with e = |E_* base|:
   e odd : odd rows have r = rho, even-half rows r >= rho+1, every w >= 2^-(rho+2)
   e even: no odd rows, even-half rows r >= rho, every w >= 2^-(rho+1)
Maximise sum w a / sum w (|T| + b) by Dinkelbach; exact weight arithmetic with a common denominator."""
import numpy as np, math, itertools, sys, json
from math import gcd

RMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
UMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3
PMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 9
NUMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 64

def h(t):
    return 0.0 if t <= 0 or t >= 1 else -t * math.log2(t) - (1 - t) * math.log2(1 - t)
def Ft(p, q):
    s = p * p + q * q
    return 2 - math.log2(s) + h(q * q / s)
def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

PAIRS = [(p, q) for p in range(2, PMAX + 1) for q in range(1, p) if gcd(p, q) == 1]
DEN = 4 ** (RMAX + 1)

def types():
    out = []  # (cls, r, wnum (over DEN), a, b)
    for u in range(UMAX + 1):
        for combo in itertools.combinations_with_replacement(PAIRS, u):
            prodS = 1
            for p, q in combo:
                prodS *= p * p + q * q
            allodd = all(p % 2 and q % 2 for p, q in combo)
            ec = sum(1 for p, q in combo if (p * p + q * q) % 2)
            sF = sum(Ft(p, q) for p, q in combo)
            sm = sum(q * q / (p * p + q * q) for p, q in combo)
            for f in range(RMAX - u + 1):
                r = f + u
                for nu in range(1, NUMAX + 1):
                    num = nu * nu * prodS * (2 ** f)      # weight = num / 4^(r+1)
                    if num > 4 ** (r + 1):
                        break
                    wnum = num * 4 ** (RMAX - r)          # over DEN
                    a = 2 - 2 * math.log2(nu) + 2 * f + sF
                    b = f / 2 + sm
                    if nu % 2 == 1:
                        if allodd:
                            out.append(("odd", r, wnum, a, b))
                    else:
                        if 2 * v2(nu) >= ec:
                            out.append(("evenhalf", r, wnum, a, b))
                        if 2 * v2(nu) >= ec + 2:
                            out.append(("ternary", r, wnum, a, b))
    return out

def best_by_weight(lst, lam, t):
    """lst of (wnum, a, b) -> dict wnum -> (best value, a, b) for position with |T| = t"""
    d = {}
    for wnum, a, b in lst:
        w = wnum / DEN
        v = w * (a - lam * (t + b))
        if wnum not in d or v > d[wnum][0]:
            d[wnum] = (v, a, b)
    return d

def pair_table(d1, d2, allow_absent1, allow_absent2):
    W1 = list(d1.keys()); W2 = list(d2.keys())
    if allow_absent1: W1 = W1 + [0]
    if allow_absent2: W2 = W2 + [0]
    v1 = np.array([d1[w][0] if w else 0.0 for w in W1]); v2_ = np.array([d2[w][0] if w else 0.0 for w in W2])
    A1 = np.array(W1, dtype=np.int64); A2 = np.array(W2, dtype=np.int64)
    S = (A1[:, None] + A2[None, :]).ravel(); V = (v1[:, None] + v2_[None, :]).ravel()
    I1 = np.repeat(np.arange(len(W1)), len(W2)); I2 = np.tile(np.arange(len(W2)), len(W1))
    ok = S <= DEN
    S, V, I1, I2 = S[ok], V[ok], I1[ok], I2[ok]
    order = np.lexsort((-V, S))
    S, V, I1, I2 = S[order], V[order], I1[order], I2[order]
    first = np.ones(len(S), dtype=bool); first[1:] = S[1:] != S[:-1]
    return S[first], V[first], I1[first], I2[first], W1, W2

def solve(menus, lam, absent_ok):
    """menus: dict t-position -> list (wnum,a,b) for positions 0, 1, 2(=second |T|=1), 3(|T|=2)"""
    tpos = {0: 0, 1: 1, 2: 1, 3: 2}
    d = {k: best_by_weight(menus[k], lam, tpos[k]) for k in range(4)}
    if any(len(d[k]) == 0 for k in range(4)) and not absent_ok:
        return -1e18, None
    SA, VA, IA1, IA2, WA1, WA2 = pair_table(d[0], d[1], absent_ok, absent_ok)
    SB, VB, IB1, IB2, WB1, WB2 = pair_table(d[2], d[3], absent_ok, absent_ok)
    need = DEN - SA
    pos = np.searchsorted(SB, need)
    pos = np.minimum(pos, len(SB) - 1)
    hit = SB[pos] == need
    if not hit.any():
        return -1e18, None
    tot = VA[hit] + VB[pos[hit]]
    j = int(np.argmax(tot))
    ia = np.nonzero(hit)[0][j]; ib = pos[hit][j]
    pick = (WA1[IA1[ia]], WA2[IA2[ia]], WB1[IB1[ib]], WB2[IB2[ib]])
    return float(tot[j]), pick, d

def ratio_of(pick, d):
    tpos = [0, 1, 1, 2]
    Hs = 0.0; Is = 0.0
    for k, wnum in enumerate(pick):
        if wnum == 0:
            continue
        v, a, b = d[k][wnum]
        w = wnum / DEN
        Hs += w * a; Is += w * (tpos[k] + b)
    return Hs / Is, Hs, Is

def scenario_menus(T):
    """yield (label, menus, absent_ok)"""
    tern = [(wn, a, b) for c, r, wn, a, b in T if c == "ternary"]
    yield ("A ternary", {k: tern for k in range(4)}, True)
    for rho in range(0, RMAX + 1):
        lo_odd = DEN // 4 ** (rho + 1) * 2 ** rho     # 2^-(rho+2) * DEN
        odd = [(wn, a, b) for c, r, wn, a, b in T if c == "odd" and r == rho and wn >= lo_odd]
        evh = [(wn, a, b) for c, r, wn, a, b in T if c == "evenhalf" and r >= rho + 1 and wn >= lo_odd]
        menu = odd + evh
        if odd:
            yield (f"B rho={rho} e odd", {k: menu for k in range(4)}, False)
        lo_even = 2 * lo_odd
        evh2 = [(wn, a, b) for c, r, wn, a, b in T if c == "evenhalf" and r >= rho and wn >= lo_even]
        if rho >= 1 and evh2:
            yield (f"B rho={rho} e even", {k: evh2 for k in range(4)}, False)

def main():
    T = types()
    print("row types:", len(T), {c: sum(1 for t in T if t[0] == c) for c in ("odd", "evenhalf", "ternary")}, flush=True)
    results = []
    for label, menus, absent_ok in scenario_menus(T):
        lam = 2.0
        best = None
        for it in range(30):
            res = solve(menus, lam, absent_ok)
            if res[1] is None:
                break
            val, pick, d = res
            rt, Hs, Is = ratio_of(pick, d)
            best = (rt, Hs, Is, [int(x) for x in pick], [d[k][pick[k]][1:] if pick[k] else None for k in range(4)])
            if rt <= lam + 1e-12:
                break
            lam = rt
        if best:
            print(label, "sup ratio", round(best[0], 6), "weights/DEN", best[3], "rows(a,b)", best[4], flush=True)
            results.append((label, best))
    results.sort(key=lambda t: -t[1][0])
    print("OVERALL best:", results[0][0], results[0][1][:3])
    with open("../data/relax_R%d_U%d_P%d.json" % (RMAX, UMAX, PMAX), "w", encoding="utf-8") as fh:
        json.dump([(l, b[:4]) for l, b in results], fh, indent=1)

if __name__ == "__main__":
    main()
