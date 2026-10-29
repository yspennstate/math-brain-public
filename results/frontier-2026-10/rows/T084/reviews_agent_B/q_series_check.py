"""The swap Hall condition (swap_classes*.py, shift 1) is equivalent to: for every lam-power, N/(1-q)^2 = N/u^2 expanded as a power
series in q has nonnegative coefficients, i.e. the second partial sums of N's q-coefficients are >= 0. Check it on K_n directly from
the exact numerators (kn_poly_adjacent / kn_poly_disjoint), n = 3..14, a path independent of the swap code."""
import json, sys
import sympy as sp
import kn_poly_adjacent as A, kn_poly_disjoint as D
lam, u = sp.symbols("lam u"); q = sp.symbols("q")
for n in range(3, int(sys.argv[1]) + 1):
    for name, mod in (("adj", A), ("dis", D)):
        if name == "dis" and n < 4: continue
        N = mod.numerator(n).as_expr()
        P = sp.Poly(sp.expand(N.subs(u, 1 - q)), lam, q)
        coef = {}
        for (a, b), c in P.terms(): coef.setdefault(a, {})[b] = int(c)
        neg = 0; ex = None
        for a, row in coef.items():
            top = max(row); s1 = s2 = 0
            for b in range(top + 1):
                s1 += row.get(b, 0); s2 += s1
                if s2 < 0: neg += 1; ex = ex or (a, b, s2)
        print(json.dumps({"n": n, "pair": name, "lam_powers": len(coef), "negative_second_partial_sums": neg, "example": ex}), flush=True)
