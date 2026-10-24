#!/usr/bin/env python3
"""Independent high-precision reconstruction of the B05 bent-defect prefix ledger.

This is deliberately independent of the author's binary64 checker.  Walsh
coefficients are obtained from exact integer FWHTs; only the final logarithms
are evaluated numerically (Decimal, 100 decimal digits).
"""

from itertools import product
from decimal import Decimal as D, getcontext

getcontext().prec = 100
LN2 = D(2).ln()


def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectral_entropy(values):
    w = fwht(values)
    N = D(len(values))
    ans = D(0)
    for z in w:
        if z:
            q = (D(z) / N) ** 2
            ans -= q * q.ln() / LN2
    return ans


def h2(t):
    if t == 0 or t == 1:
        return D(0)
    return -t * t.ln() / LN2 - (1 - t) * (1 - t).ln() / LN2


def jphase(t):
    return 1 - h2(D("0.5") + (t * (1 - t)).sqrt())


def packet_parts(a, v):
    q = a * a + v * v
    if q == 0:
        return D(0), D(0)
    t = v * v / q
    return q * h2(t), q * jphase(t)


def bent_values(k, m, next_u=None, flip=False):
    """Truth table after u_1=...=u_m=0; optionally fix u_{m+1}."""
    h = k // 2
    free_u = list(range(m, h))
    if next_u is not None:
        free_u = free_u[1:]
    coords = [("u", j) for j in free_u] + [("v", j) for j in range(h)]
    out = []
    for bits in product((0, 1), repeat=len(coords)):
        u = [0] * h
        v = [0] * h
        if next_u is not None:
            u[m] = next_u
        for bit, (kind, j) in zip(bits, coords):
            (u if kind == "u" else v)[j] = bit
        val = -1 if sum(u[j] * v[j] for j in range(h)) % 2 else 1
        if flip and not any(u) and not any(v):
            val *= -1
        out.append(val)
    return out


def selector_values(k, m, next_u=None):
    g = bent_values(k, m, next_u, False)
    gp = bent_values(k, m, next_u, True)
    return g + gp  # y=0 block, then y=1 block; coordinate order is immaterial


def delta_selector(k, m):
    s = selector_values(k, m)
    g = bent_values(k, m, None, False)
    gp = bent_values(k, m, None, True)
    return spectral_entropy(s) - (spectral_entropy(g) + spectral_entropy(gp)) / 2


def formula(k, m):
    delta = D(2) ** (-k)
    rho = delta.sqrt()
    c = D(2) ** m * rho
    ps = []
    qs = []
    for sig in (1, -1):
        den = (sig - rho) ** 2 + rho ** 2
        t = rho ** 2 / den
        ps.append(den * h2(t))
        qs.append(den * jphase(t))
    AL, BL = (ps[0] + ps[1]) / 2, (ps[0] - ps[1]) / 2
    AQ, BQ = (qs[0] + qs[1]) / 2, (qs[0] - qs[1]) / 2
    L = AL - 2 * delta + c * (BL + 2 * rho)
    Q = AQ - 2 * delta + c * (BQ + 2 * rho)
    return L, Q, AL, AQ


def direct_parts(k, m):
    g = bent_values(k, m, None, False)
    gp = bent_values(k, m, None, True)
    wg, wgp = fwht(g), fwht(gp)
    N = D(len(g))
    L = Q = D(0)
    for x, y in zip(wg, wgp):
        a = (D(x) + y) / (2 * N)
        v = (D(x) - y) / (2 * N)
        l, q = packet_parts(a, v)
        L += l
        Q += q
    return L, Q


def main():
    tol = D("1e-75")
    rows = 0
    min_l_credit = D("Infinity")
    min_q_credit = D("Infinity")
    max_err = D(0)
    for k in (2, 4, 6, 8, 10):
        h = k // 2
        for m in range(h + 1):
            ld, qd = direct_parts(k, m)
            lf, qf, AL, AQ = formula(k, m)
            err = max(abs(ld - lf), abs(qd - qf), abs(delta_selector(k, m) - (lf + qf)))
            max_err = max(max_err, err)
            assert err < tol, (k, m, err)
            if m < h:
                lnext, qnext, _, _ = formula(k, m + 1)
                gl = lf - lnext / 2
                gq = qf - qnext / 2
                min_l_credit = min(min_l_credit, gl)
                min_q_credit = min(min_q_credit, gq)
                assert abs(gl - (AL - 2 * D(2) ** (-k)) / 2) < tol
                assert abs(gq - (AQ - 2 * D(2) ** (-k)) / 2) < tol
                assert gl >= 0 and gq >= 0

                # Independently verify the two-coordinate order-swap identity.
                parent_data = spectral_entropy(selector_values(k, m)) - (
                    spectral_entropy(selector_values(k, m, 0))
                    + spectral_entropy(selector_values(k, m, 1))
                ) / 2
                g = bent_values(k, m, None, False)
                gp = bent_values(k, m, None, True)
                child_data = D(0)
                for flip, vals in ((False, g), (True, gp)):
                    child_data += spectral_entropy(vals) - (
                        spectral_entropy(bent_values(k, m, 0, flip))
                        + spectral_entropy(bent_values(k, m, 1, flip))
                    ) / 2
                child_data /= 2
                swap_credit = parent_data - child_data
                assert abs(swap_credit - (gl + gq)) < tol, (k, m, swap_credit, gl + gq)
                rows += 1

    # Independent high-precision asymptotic spot checks (closed form only).
    for k in range(2, 202, 2):
        h = k // 2
        vals = [formula(k, m) for m in range(h + 1)]
        for m in range(h):
            gl = vals[m][0] - vals[m + 1][0] / 2
            gq = vals[m][1] - vals[m + 1][1] / 2
            assert gl >= 0 and gq >= 0

    print("status=PASS")
    print("truth_table_rows_checked=%d" % rows)
    print("closed_form_k_even_checked=2..200")
    print("decimal_digits=100")
    print("max_truth_table_formula_error=%s" % format(max_err, ".6E"))
    print("min_L_prefix_credit=%s" % format(min_l_credit, ".20E"))
    print("min_Q_prefix_credit=%s" % format(min_q_credit, ".20E"))
    print("scope=finite reconstruction plus high-precision checks; analytic all-k proof is in REPORT.md")


if __name__ == "__main__":
    main()
