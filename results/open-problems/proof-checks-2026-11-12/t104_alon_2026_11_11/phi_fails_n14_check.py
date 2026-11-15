"""Exact recheck of three statements from the Codex prover's PROOF.md (an agent, 11 Nov 2026).

(a) Phi' < 0 at x = (11, 1 x 11, -11, -11)/sqrt(374), n = 14, while Psi > 0 there.
(b) H_n(y) for y = (s, 1 x s, -s, -s), n = s + 3, equals
        -2 s^2 (s-1)(s+1)^4 (s+3)(s^2 - 11 s + 6)(s^2 + 4 s - 1)        for s = 2..60.
(c) Zero padding. With rho = 2q - 1, B = p^2, t = 2B - rho, C_n = (n-1)(n^2 + (rho-5) n + 6):
        Psi_n = C_n m - ((n-4) t + 2B),
        C_{n+1} - C_n = 3 n^2 + (2 rho - 9) n + 6,
        (n-4) C_{n+1} - (n-3) C_n = 2 h^3 + (15 + rho) h^2 + (31 + 3 rho) h + 12 - 10 rho,   h = n - 5,
    the first on random rational points, the other two on a grid larger than their degrees (so as identities).
    Then: Psi_n(x) >= 0 implies Psi_{n+1}(x, 0) >= 0, tested directly on random points.
Written from the statements with the forms of chain_check.py; no code of the prover is used.
"""
import random
from fractions import Fraction as F

from chain_check import forms


def psi_normalised(n, x):
    """Psi with |x| = 1 enforced by homogeneity: returns Psi_h / T^3 and (q, p^2, m) normalised."""
    T = sum(v * v for v in x); P = sum(v ** 3 for v in x); Q = sum(v ** 4 for v in x)
    m = max(x[i] * x[j] for i in range(len(x)) for j in range(len(x)) if i != j)
    q = Q / (T * T); B = P * P / T ** 3; mm = m / T
    psi = (n - 4) * (2 * q - 1) - 2 * (n - 3) * B + (n - 1) * (n * n - 6 * n + 6 + 2 * n * q) * mm
    return psi, q, B, mm


def main():
    # (a)
    s = 11; n = s + 3
    y = [F(s)] + [F(1)] * s + [F(-s), F(-s)]
    assert sum(y) == 0 and y == sorted(y, reverse=True) and y[0] + y[-1] >= 0
    T, K, m, W, Mh, H, Psi = forms(n, y)
    print(f"(a) n=14: T={T} W={W} m/T={m / T} M/T={Mh / T} H/T^4={H / T ** 4} Psi_h/T^3={Psi / T ** 3}")
    assert T == 374 and H < 0 and Psi > 0 and W > 0
    # Phi' is H at T = 1
    print("    Phi' =", H / T ** 4, "=", float(H / T ** 4), "; Psi =", Psi / T ** 3, "=", float(Psi / T ** 3))
    # (b)
    first_neg = None
    for s in range(2, 61):
        n = s + 3
        y = [F(s)] + [F(1)] * s + [F(-s), F(-s)]
        H = forms(n, y)[5]
        rhs = -2 * s * s * (s - 1) * (s + 1) ** 4 * (s + 3) * (s * s - 11 * s + 6) * (s * s + 4 * s - 1)
        assert H == rhs, s
        if H < 0 and first_neg is None:
            first_neg = n
    print(f"(b) factorisation exact for s = 2..60; first n in this family with H < 0: n = {first_neg}")
    # (c) identities
    def C(n, rho):
        return (n - 1) * (n * n + (rho - 5) * n + 6)
    for n in range(-3, 9):
        for rho in (F(-2), F(-1, 3), F(0), F(5, 7), F(3)):
            assert C(n + 1, rho) - C(n, rho) == 3 * n * n + (2 * rho - 9) * n + 6
            h = n - 5
            assert (n - 4) * C(n + 1, rho) - (n - 3) * C(n, rho) == 2 * h ** 3 + (15 + rho) * h * h + (31 + 3 * rho) * h + 12 - 10 * rho
    rnd = random.Random(14)
    cnt = 0; implied = 0
    for trial in range(6000):
        n = rnd.randint(5, 12)
        x = [F(rnd.randint(-9, 9)) for _ in range(n)]
        if trial % 3 == 0:
            x = [F(rnd.choice([-2, -1, 0, 0, 1, 3])) for _ in range(n)]
        sm = sum(x); x = [v - sm / n for v in x]
        if all(v == 0 for v in x):
            continue
        psi, q, B, mm = psi_normalised(n, x)
        rho = 2 * q - 1; t = 2 * B - rho
        assert psi == C(n, rho) * mm - ((n - 4) * t + 2 * B)
        assert -1 <= rho <= 1 and mm >= 0
        psi1 = psi_normalised(n + 1, x + [F(0)])[0]
        cnt += 1
        if psi >= 0:
            implied += 1
            assert psi1 >= 0, (n, x)
    print(f"(c) identities exact; Psi_n formula exact on {cnt} points; Psi_n >= 0 => Psi_(n+1) >= 0 held on all {implied} points with Psi_n >= 0")


if __name__ == "__main__":
    main()
