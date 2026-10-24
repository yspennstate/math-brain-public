"""Test the closed-form slack Gamma_lex(p) = C I(l_p) - H(l_p), l_p the lexicographic function of measure p, against
the read-once functional inequality

   (A)  Gamma(pq) <= q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q)

which, with Gamma = Gamma_lex, says: slack(l_{pq}) <= slack(AND(l_p, l_q)), i.e. among read-once formulas of measure
pq the lexicographic one minimises C I - H after one more AND gate. Equality along the extremal structure is
expected when C = beta(1/2) = 6.4547837 (Hod). Reports the minimum of D(p,q) = slack(AND(l_p,l_q)) - slack(l_pq)
over a grid, where it is attained, and how the minimum moves with C.
"""
import sys, math, time
import numpy as np
sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
from fei_chain import chain_state
from fei_comp_search import lex_pattern
from fei_readonce_gamma import Ht_and, h2

_cache = {}
def lexHI(p, digits=80):
    key = round(p, 15)
    if key not in _cache:
        a, H, I = chain_state(lex_pattern(p, digits))
        _cache[key] = (H, I)
    return _cache[key]

def slack_lex(p, C):
    H, I = lexHI(p)
    return C * I - H

def slack_and(p, q, C):
    Hp, Ip = lexHI(p); Hq, Iq = lexHI(q)
    Vp = 4 * p * (1 - p); Vq = 4 * q * (1 - q)
    I = q * Ip + p * Iq
    H = q * (Hp - float(h2(np.array([Vp]))[0])) + p * (Hq - float(h2(np.array([Vq]))[0])) + float(Ht_and(np.array([p]), np.array([q]))[0])
    return C * I - H, I, H

def scan(C, n=400, lo=0.005, hi=0.995):
    grid = np.linspace(lo, hi, n)
    worst = (np.inf, None); rows = []
    t0 = time.time()
    for p in grid:
        for q in grid:
            if q < p:
                continue
            s_and, I_and, H_and = slack_and(p, q, C)
            D = s_and - slack_lex(p * q, C)
            if D < worst[0]:
                worst = (D, (p, q, p * q, s_and, slack_lex(p * q, C)))
    return worst, time.time() - t0

if __name__ == "__main__":
    Phi = (math.sqrt(5) - 1) / 2
    C0 = 6.4547837
    # sanity: dyadic points equal the AND_k slack
    for k in (1, 2, 3, 4):
        p = 2.0 ** -k; H, I = lexHI(p)
        print("l_{1/2^%d}: I %.6f H %.6f slack %.6f" % (k, I, H, C0 * I - H))
    print("nonnegativity: min over p of slack_lex(p) =", min(slack_lex(p, C0) for p in np.linspace(0.001, 0.999, 999)))
    for C in (6.30, 6.40, 6.44, 6.45, C0, 6.46, 6.50):
        (D, where), dt = scan(C, n=160)
        print("C=%.7f: min D = %+.6f at p=%.4f q=%.4f (pq=%.4f)  slack_and %.5f slack_lex %.5f  (%.0f s)" % (C, D, where[0], where[1], where[2], where[3], where[4], dt), flush=True)
    (D, where), dt = scan(C0, n=500)
    print("fine scan at C0: min D = %+.7f at p=%.5f q=%.5f (pq=%.5f) (%.0f s)" % (D, where[0], where[1], where[2], dt))
    # where is it tight? list the pairs with D < 1e-3
    grid = np.linspace(0.005, 0.995, 300); tight = []
    for p in grid:
        for q in grid:
            if q < p: continue
            Dv = slack_and(p, q, C0)[0] - slack_lex(p * q, C0)
            if Dv < 2e-3:
                tight.append((round(Dv, 5), round(p, 4), round(q, 4)))
    tight.sort()
    print("near-tight pairs (D < 2e-3):", tight[:15])
