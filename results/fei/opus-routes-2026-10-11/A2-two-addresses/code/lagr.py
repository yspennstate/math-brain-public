"""Lagrangian certificate for the arithmetic relaxation at c = c*.
Since sum_T w_T = 1,  Phi := sum_T w_T e_T = mu + sum_T w_T (e_T - mu) <= mu + sum_T M_T(mu),
M_T(mu) = sup over admissible single rows at position T of w (e_T - mu)   (0 allowed if the row may be absent).
e_T = 2 - 2 log2 nu' + delta f + sum_unf (Ft - c m) - c |T|,  delta = 2 - c/2.
For each scenario we minimise B(mu) = mu + M_0 + 2 M_1 + M_2 over mu (convex in mu).
B <= 0 for every scenario certifies (within the parameter bounds) that the relaxation sup is <= c*."""
import numpy as np, math, sys
sys.path.insert(0, ".")
import relax as RX

C = 16 / 3 - 1.5 * math.log2(3)

def main():
    T = RX.types()
    DEN = RX.DEN
    def menu_rows(cls_pred):
        return [(wn / DEN, a, b) for c, r, wn, a, b in T if cls_pred(c, r, wn)]
    scen = []
    tern = menu_rows(lambda c, r, wn: c == "ternary")
    scen.append(("A ternary", tern, True))
    for rho in range(0, RX.RMAX + 1):
        lo = 2.0 ** (-rho - 2)
        m_odd = menu_rows(lambda c, r, wn, rho=rho, lo=lo: (c == "odd" and r == rho and wn / DEN >= lo - 1e-15) or
                          (c == "evenhalf" and r >= rho + 1 and wn / DEN >= lo - 1e-15))
        if any(True for c, r, wn, a, b in T if c == "odd" and r == rho):
            scen.append((f"B rho={rho} e odd", m_odd, False))
        if rho >= 1:
            lo2 = 2.0 ** (-rho - 1)
            m_even = menu_rows(lambda c, r, wn, rho=rho, lo2=lo2: c == "evenhalf" and r >= rho and wn / DEN >= lo2 - 1e-15)
            scen.append((f"B rho={rho} e even", m_even, False))
    worst = -1e9
    for label, menu, absent in scen:
        W = np.array([x[0] for x in menu]); A = np.array([x[1] for x in menu]); Bv = np.array([x[2] for x in menu])
        e = {t: A - C * (t + Bv) for t in (0, 1, 2)}
        def Bmu(mu):
            tot = mu
            for t, mult in ((0, 1), (1, 2), (2, 1)):
                v = W * (e[t] - mu)
                mx = v.max() if len(v) else -1e18
                if absent:
                    mx = max(mx, 0.0)
                tot += mult * mx
            return tot
        # convex minimisation by ternary search on a bracket, then grid polish
        lo, hi = -10.0, 10.0
        for _ in range(200):
            m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
            if Bmu(m1) <= Bmu(m2): hi = m2
            else: lo = m1
        mu = (lo + hi) / 2
        val = Bmu(mu)
        worst = max(worst, val)
        print(f"{label:22s} best mu {mu:+.5f}  bound B(mu) = {val:+.6f}", flush=True)
    print("worst scenario bound:", worst, "(<= 0 certifies the relaxation at c* within the bounds)")

if __name__ == "__main__":
    main()
