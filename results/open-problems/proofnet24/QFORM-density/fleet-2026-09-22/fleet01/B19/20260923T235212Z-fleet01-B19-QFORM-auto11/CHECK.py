import itertools
import math
import numpy as np


def incident_minor_mass(C, b):
    n = len(b)
    total = 0.0
    overlap = [0.0, 0.0, 0.0]
    for R in itertools.combinations(range(n), 2):
        for T in itertools.combinations(range(n), 3):
            M = np.vstack([b[list(T)], C[np.ix_(R, T)]])
            z = float(np.linalg.det(M)) ** 2
            total += z
            overlap[len(set(R).intersection(T))] += z
    return total, overlap


def incident_spectral_mass(C, b):
    lam, U = np.linalg.eigh(C)
    out = 0.0
    for r in range(len(lam)):
        for s in range(r + 1, len(lam)):
            br = float(U[:, r] @ b)
            bs = float(U[:, s] @ b)
            out += lam[r] ** 2 * lam[s] ** 2 * (float(b @ b) - br ** 2 - bs ** 2)
    return out


def exact_rank2_factor(C, b, U, D, tau, w):
    n = len(b)
    lhs = 0.0
    rhs = 0.0
    W = np.column_stack([w, U])
    for R in itertools.combinations(range(n), 2):
        for T in itertools.combinations(range(n), 3):
            M = np.vstack([b[list(T)], C[np.ix_(R, T)]])
            d = float(np.linalg.det(M))
            f = tau * float(np.linalg.det(U[list(R), :])) * float(np.linalg.det(D)) * float(np.linalg.det(W[list(T), :]))
            lhs += d * d
            rhs += f * f
            if abs(d * d - f * f) > 1e-8 * max(1.0, d * d, f * f):
                raise AssertionError((R, T, d * d, f * f))
    return lhs, rhs


def main():
    rng = np.random.default_rng(20260923)
    worst = 0.0
    for n in (4, 5, 6, 7):
        for _ in range(40):
            G = rng.normal(size=(n, n))
            C = (G + G.T) / 2
            b = rng.normal(size=n)
            a, _ = incident_minor_mass(C, b)
            s = incident_spectral_mass(C, b)
            err = abs(a - s) / max(1.0, abs(s))
            worst = max(worst, err)
            assert err < 1e-10

    # Exact-rank-two factorization test.
    worst2 = 0.0
    for n in (5, 7, 9):
        for _ in range(40):
            Q, _ = np.linalg.qr(rng.normal(size=(n, 3)))
            w = Q[:, 0]
            U = Q[:, 1:3]
            D = np.diag([2.3, -1.7])
            tau = 1.2
            beta = np.array([5.0, -3.0])
            b = tau * w + U @ beta
            C = U @ D @ U.T
            x, y = exact_rank2_factor(C, b, U, D, tau, w)
            err = abs(x - y) / max(1.0, abs(y))
            worst2 = max(worst2, err)
            assert err < 1e-10

    C12 = 3 * 2 ** (7 / 6) * math.e ** (1 / 3)
    Cdis = C12 * (3125 / 54) ** (1 / 6)
    lowtail = Cdis * (96 / (47 * math.sqrt(47))) ** (1 / 3)
    Gamma_min = 103823 / 9216
    currency_min = Gamma_min / 566
    exact_rank2 = C12 * (6250 / 207) ** (1 / 6) * (48 / (47 * math.sqrt(47))) ** (1 / 3)

    print('worst spectral/minor identity relative error:', worst)
    print('worst exact-rank2 factorization relative error:', worst2)
    print('C12 =', C12)
    print('Cdis =', Cdis)
    print('low-tail diffuse deletion density constant =', lowtail)
    print('Gamma_min/L^6 =', Gamma_min)
    print('overlap currency minimum/L^6 =', currency_min)
    print('exact-rank2 diffuse endpoint constant =', exact_rank2)


if __name__ == '__main__':
    main()
