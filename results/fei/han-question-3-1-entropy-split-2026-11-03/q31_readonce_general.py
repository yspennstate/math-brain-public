# T021: general read-once formulas. With siblings of the path child arbitrary, the block recursion depends on them only
# through P = prod of the siblings' means (Parseval: sum_T g_j^(T)^2 = mu_j). Step with arbitrary P in (0,1).
import mpmath as mp
from q31_tree_entropy import Phi
mp.mp.dps = 200
def stepP(st, P):
    c0, I, D = st; mu = (1 - c0) / 2; c0n = -1 + 2 * mu * P
    Dn = P * (D - Phi(c0 ** 2, I ** 2) + Phi(4 * mu ** 2, I ** 2)) - P * P * Phi(4 * mu ** 2, I ** 2) + Phi(c0n ** 2, (I * P) ** 2)
    return (c0n, I * P, Dn)
if __name__ == "__main__":
    for d in ("0.1", "0.01", "0.001"):
        dl = mp.mpf(d); st = (mp.mpf(0), mp.mpf(1), mp.mpf(0)); L = 0; rows = []
        while st[1] > mp.mpf("1e-8"):
            st = stepP(st, 1 - dl); L += 1
            if L % max(1, int(1 / dl)) == 0: rows.append((L, mp.nstr(mp.log(1 / st[1]), 4), mp.nstr(st[0], 4), mp.nstr(st[2] / st[1], 6)))
        print("P = 1 - %s:" % d, rows[:3], "...", rows[-3:])
