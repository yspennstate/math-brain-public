#!/usr/bin/env python3
"""Self-checks for PROB20-19 all-ranks quintic top-five proof.

This is reproducible self-review evidence, not independent verification.
It checks exact symbolic reductions and a deterministic random-projection bank.
"""

import math
import numpy as np
import sympy as sp


def symbolic_checks():
    r, W, mu, nu, xi = sp.symbols("r W mu nu xi", positive=True)
    R = r + 8

    G_over_W = (
        28*r**2 - 10*r + 36
        + 9*(10*mu-r+2)*W
        + (10*r**2 - 160*r - 732)*mu
        - (114*r + 444)*nu
        + 468*xi
    )
    lhs = sp.expand(G_over_W + 96*R*mu - sp.Rational(104, 2025)*R**3)
    rhs = sp.expand(
        28*r**2 - 10*r + 36 - sp.Rational(104, 2025)*R**3
        + 9*(10*mu-r+2)*W
        + (10*r**2 - 64*r + 36)*mu
        - (114*r + 444)*nu
        + 468*xi
    )
    assert sp.simplify(lhs-rhs) == 0

    t = sp.symbols("t", real=True)
    assert sp.factor(
        468*t**3 - 900*t**2 - 60*t + sp.Rational(6405, 13)*t
    ) == sp.Rational(9, 13)*t*(26*t-25)**2

    # Rank-four constrained polynomial.
    mu4 = (1+t**2)/2
    W4 = t**2
    P_direct = sp.simplify(
        444 - sp.Rational(6405, 13)*mu4
        + 9*(10*mu4-2)*W4
        - sp.Rational(16*12**3, 135*30)
        + (-2160*12*t**2 + 32400*t**3)/30
    )
    P_report = (
        87750*t**4 + 2106000*t**3 - 2112525*t**2 + 372113
    ) / 1950
    assert sp.simplify(P_direct-P_report) == 0
    assert sp.factor(sp.diff(P_report, t)) == (
        sp.Rational(3, 13)*t*(780*t**2 + 14040*t - 9389)
    )

    q = 780*t**2 + 14040*t - 9389
    num = sp.Poly(87750*t**4 + 2106000*t**3 - 2112525*t**2 + 372113, t)
    rem = sp.rem(num, sp.Poly(q, t)).as_expr()
    assert sp.factor(rem) == (
        20377375200*t - 13147540463
    ) / 104

    a = sp.Rational(13147540463, 20377375200)
    b = sp.Rational(1291, 2000)
    assert b-a == sp.Rational(30276143, 101886876000)
    assert sp.factor(q.subs(t, b)) == -sp.Rational(235441, 200000)

    # Finite-rank one-variable reductions.
    m = sp.symbols("m", real=True)
    expected = {
        5: (
            (-911250*m**2 + 10125*m + 887287)/2025,
            (-1174500*m + 1160662)/2025,
            (364500*m**2 - 1466100*m + 1215337)/2025,
        ),
        6: (
            (-1093500*m**2 + 218700*m + 1269824)/2025,
            (-1312200*m + 1707224)/2025,
            (364500*m**2 - 1640250*m + 1780124)/2025,
        ),
        7: (
            (-1890*m**2 + 747*m + 2549)/3,
            None,
            (540*m**2 - 2628*m + 3629)/3,
        ),
        8: (
            (-1458000*m**2 + 866700*m + 2238916)/2025,
            None,
            (364500*m**2 - 1867050*m + 3223066)/2025,
        ),
    }
    for rr in range(5, 9):
        RR = rr + 8
        C = sp.Rational(28*rr**2 - 10*rr + 36) - sp.Rational(104, 2025)*RR**3
        B = 10*rr**2 - 178*rr + 60
        cW = 9*(10*m-rr+2)
        upper = sp.expand(C + B*m + cW*rr*(1-m))
        zero = sp.expand(C + B*m)
        lower = sp.expand(C + B*m + cW*(2*m-1))
        eu, ez, el = expected[rr]
        assert sp.simplify(upper-eu) == 0
        if ez is not None:
            assert sp.simplify(zero-ez) == 0
        assert sp.simplify(lower-el) == 0


def random_projection(p, r, seed):
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q[:, :r]


def invariants(Q):
    P = Q @ Q.T
    d = np.diag(P)
    q2 = P**2
    S = {k: float(np.sum(d**k)) for k in range(2, 6)}
    A = B = L = M = 0.0
    p = len(d)
    for i in range(p):
        for j in range(i+1, p):
            q = q2[i, j]
            a, b = d[i], d[j]
            s = a+b
            A += a*b*q
            B += q*q
            L += a*b*s*q
            M += s*q*q
    r = Q.shape[1]
    W = r-S[2]
    return d, S, A, B, L, M, W


def exact_numerator(Q):
    r = Q.shape[1]
    R = r+8
    d, S, A, B, L, M, W = invariants(Q)
    T = math.prod(r+2*j for j in range(5))
    N = (
        T - 135*R*S[2]**2 + 1350*S[2]*S[3]
        - 150*(r+6)*R*S[3] + 1710*R*S[4] - 7020*S[5]
        - 2160*R*A - 720*R*B + 16200*L + 10800*M
    )
    Ncoord = r*(r-1)*(r-2)*(r-3)*(r+26)
    return N, Ncoord, (d, S, A, B, L, M, W)


def rank4_scalar_certificate(mu):
    mustar = 289/450
    if mu <= mustar:
        if mu <= 1/5:
            wsel = 4*(1-mu)
        elif mu <= 1/2:
            wsel = 0.0
        else:
            wsel = 2*mu-1
        return 26644/75 - (6405/13)*mu + 9*(10*mu-2)*wsel
    t = math.sqrt(2*mu-1)
    return (
        87750*t**4 + 2106000*t**3 - 2112525*t**2 + 372113
    ) / 1950


def finite_rank_scalar_certificate(r, mu):
    R = r+8
    C = 28*r*r - 10*r + 36 - 104*R**3/2025
    B = 10*r*r - 178*r + 60
    coeff = 9*(10*mu-r+2)
    if coeff < 0:
        wsel = r*(1-mu)
    else:
        wsel = max(0.0, 2*mu-1)
    return C+B*mu+coeff*wsel


def random_bank():
    minimum_gap = {r: float("inf") for r in range(4, 9)}
    minimum_cert = {r: float("inf") for r in range(4, 9)}
    cases = 0
    for r in range(4, 9):
        for seed in range(400):
            p = r+1+(seed % 8)
            Q = random_projection(p, r, 700000*r+seed)
            N, Nc, data = exact_numerator(Q)
            d, S, A, B, L, M, W = data
            gap = N-Nc
            minimum_gap[r] = min(minimum_gap[r], gap)
            assert gap > -1e-7

            if W > 1e-12:
                Qsum = W/2
                assert L + 1e-10 >= 2*A**1.5/math.sqrt(Qsum)
                assert M + 1e-10 >= 2*B**1.5/math.sqrt(Qsum)
                rho = d*(1-d)/W
                mu = float(np.sum(rho*d))
                assert W + 1e-9 >= 2*mu-1
                assert W <= r*(1-mu) + 1e-9

                if r == 4:
                    cert = rank4_scalar_certificate(mu)
                else:
                    cert = finite_rank_scalar_certificate(r, mu)
                minimum_cert[r] = min(minimum_cert[r], cert)
                assert cert > 0
                # The analytic proof gives gap/(15W) >= certificate.
                assert gap/(15*W) + 1e-6 >= cert
            cases += 1
    return cases, minimum_gap, minimum_cert


if __name__ == "__main__":
    symbolic_checks()
    cases, minimum_gap, minimum_cert = random_bank()
    print("PROB20-19 quintic top-five all-ranks checker")
    print("symbolic checks: PASS")
    print("projection cases:", cases)
    print("minimum exact numerator gap by rank:")
    for r in range(4, 9):
        print(f"  r={r}: {minimum_gap[r]:.12g}")
    print("minimum analytic scalar certificate by rank:")
    for r in range(4, 9):
        print(f"  r={r}: {minimum_cert[r]:.12g}")
    print("random bank: PASS")
