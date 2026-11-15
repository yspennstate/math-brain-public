"""Where the ratio E_x/Inf_x of tilde f_k under bias P comes from (see forced_exact.py for the formulas).
For each class (i, j) the weight is w = Bin(m, 1-P)(i) Bin(m, 1-P)(j) and the class term is
Phi(A^2, D^2)/D^2 with A, D the class coefficients. Prints, for each k, the mass of classes with
log2(A^2/D^2) >= c*m for c in CS, and the share of the ratio from classes with A^2 >= D^2.
Usage: python forced_profile.py k [t]
"""
import sys
from fractions import Fraction
from math import comb, log2
from forced_exact import bias, pmul, ppow, flog

CS = (0.0, 0.1, 0.2, 0.3, 0.4)


def profile(k, P):
    m = (k - 1) // 2
    u, w = P.numerator, P.denominator
    X, Y = [w - u, u], [u, w - u]
    Xp = [ppow(X, e) for e in range(m + 1)]
    Yp = [ppow(Y, e) for e in range(m + 2)]
    Zp = [ppow([-1, 1], e) for e in range(2 * m + 1)]
    q = 1 - P
    mass = {c: 0.0 for c in CS}
    total = big = 0.0
    zeros = 0
    for i in range(m + 1):
        for j in range(m + 1):
            poly = pmul(pmul(Xp[m - i], Yp[m - j + 1]), Zp[i + j])
            maj = Fraction(sum(poly[m + 1:]), w ** (2 * m - i - j + 1))
            d = (-1) ** j * P ** (2 * m - i - j)
            a = (1 if i == j == 0 else 0) - 2 * (maj - (1 - P) * d) - d
            wt = float(comb(m, i) * comb(m, j) * q ** (i + j) * P ** (2 * m - i - j))
            a2, d2 = a * a, d * d
            tot = a2 + d2
            term = flog(tot / d2) + (float(a2 / d2) * flog(tot / a2) if a2 else 0.0)
            total += wt * term
            if a2 == 0:
                zeros += 1
                continue
            lr = flog(a2 / d2)
            if a2 >= d2:
                big += wt * term
            for c in CS:
                if lr >= c * m:
                    mass[c] += wt
    return total, big, mass, zeros


if __name__ == "__main__":
    k = int(sys.argv[1])
    t = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    tot, big, mass, zeros = profile(k, bias(t))
    m = (k - 1) // 2
    print(f"k={k} m={m} t={t} ratio={tot:.6f} share(A2>=D2)={big / tot:.4f} zero classes={zeros}")
    print("  mass of classes with log2(A^2/D^2) >= c m: " + "  ".join(f"c={c}: {mass[c]:.4f}" for c in CS))
