"""Bernstein form in u of N/u (adjacent or disjoint pair, K_n): N/u = sum_j C(d,j) b_j(lam) u^j (1-u)^(d-j), b_j = sum_{k<=j} C(j,k)/C(d,k) a_k(lam).
All b_j with nonnegative lam-coefficients proves N > 0 for every q in (0,1), lam > 0 on that K_n. Optional degree elevation E."""
import sys, json
from fractions import Fraction
from math import comb
import kn_poly_adjacent, kn_poly_disjoint


def bern(n, elev=0, pair="adj"):
    N = (kn_poly_adjacent if pair == "adj" else kn_poly_disjoint).numerator(n)
    a = {}
    for (i, j), c in N.terms():
        a.setdefault(j - 1, {})[i] = a.get(j - 1, {}).get(i, 0) + int(c)   # divide by u
    d = max(a) + elev
    out = []
    for j in range(d + 1):
        bj = {}
        for k in range(0, j + 1):
            if k not in a: continue
            f = Fraction(comb(j, k), comb(d, k))
            for i, c in a[k].items():
                bj[i] = bj.get(i, 0) + f * c
        out.append(bj)
    return d, out


if __name__ == "__main__":
    elev = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    pair = sys.argv[4] if len(sys.argv) > 4 else "adj"
    for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        d, B = bern(n, elev, pair)
        neg = [(j, i, float(c)) for j, bj in enumerate(B) for i, c in bj.items() if c < 0]
        print(json.dumps({"n": n, "pair": pair, "deg_u": d, "elev": elev, "n_negative": len(neg), "sample": neg[:5]}), flush=True)
