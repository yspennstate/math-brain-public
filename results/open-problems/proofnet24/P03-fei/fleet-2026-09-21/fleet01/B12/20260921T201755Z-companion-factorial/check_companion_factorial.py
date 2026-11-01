from fractions import Fraction
import itertools
import json
import math


def fwht_int(values):
    h = list(map(int, values))
    step = 1
    while step < len(h):
        for base in range(0, len(h), 2 * step):
            for j in range(base, base + step):
                x, y = h[j], h[j + step]
                h[j], h[j + step] = x + y, x - y
        step *= 2
    return h


def analyze(values):
    N = len(values)
    n = N.bit_length() - 1
    assert 1 << n == N
    W = fwht_int(values)
    p = [Fraction(w * w, N * N) for w in W]
    assert sum(p, Fraction()) == 1

    I = sum((Fraction(mask.bit_count()) * p[mask] for mask in range(N)), Fraction())
    V = 1 - p[0]
    p_i = [Fraction() for _ in range(n)]
    u = [Fraction() for _ in range(n)]
    r = [[Fraction() for _ in range(n)] for _ in range(n)]

    for mask, mass in enumerate(p):
        k = mask.bit_count()
        if k == 0 or mass == 0:
            continue
        inds = [i for i in range(n) if (mask >> i) & 1]
        for i in inds:
            p_i[i] += mass
            u[i] += mass / k
        for i in inds:
            for j in inds:
                if i != j:
                    r[i][j] += mass / k

    # Exact companion-flow identities.
    assert sum(u, Fraction()) == V
    assert sum((r[i][j] for i in range(n) for j in range(n) if i != j), Fraction()) == I - V
    for i in range(n):
        assert u[i] + sum((r[i][j] for j in range(n) if j != i), Fraction()) == p_i[i]
        for j in range(n):
            assert r[i][j] == r[j][i]

    # Exact insertion-edge law from the uniform-prefix construction.
    v = [Fraction() for _ in range(N)]
    for A in range(N):
        a = A.bit_count()
        for B in range(N):
            if A & ~B == 0 and p[B]:
                v[A] += p[B] / math.comb(B.bit_count(), a)

    joint = {}
    for A in range(N):
        a = A.bit_count()
        for i in range(n):
            if not ((A >> i) & 1):
                w = v[A | (1 << i)] / (a + 1)
                if w:
                    joint[(i, A)] = w / I
    assert sum(joint.values(), Fraction()) == 1

    Lm = [Fraction() for _ in range(n)]
    Pm = [Fraction() for _ in range(N)]
    for (i, A), mass in joint.items():
        Lm[i] += mass
        Pm[A] += mass
    assert Lm == [x / I for x in p_i]

    Dseq = 0.0
    for (i, A), mass in joint.items():
        x = float(mass)
        Dseq += float(I) * x * math.log2(x / float(Lm[i] * Pm[A]))

    # Companion variable: null if P is empty, otherwise a uniformly selected member of P.
    # Its exact joint law with L must be u_i/I on null and r_ij/I off diagonal.
    comp = {}
    for (i, A), mass in joint.items():
        a = A.bit_count()
        if a == 0:
            comp[(i, -1)] = comp.get((i, -1), Fraction()) + mass
        else:
            for j in range(n):
                if (A >> j) & 1:
                    comp[(i, j)] = comp.get((i, j), Fraction()) + mass / a
    for i in range(n):
        assert comp.get((i, -1), Fraction()) == u[i] / I
        for j in range(n):
            if i != j:
                assert comp.get((i, j), Fraction()) == r[i][j] / I

    Cm = {-1: V / I}
    for j in range(n):
        Cm[j] = (p_i[j] - u[j]) / I

    Dcomp = 0.0
    for (i, c), mass in comp.items():
        x = float(mass)
        Dcomp += float(I) * x * math.log2(x / float(Lm[i] * Cm[c]))
    assert Dcomp <= Dseq + 1e-12

    elogfac = sum(
        float(mass) * math.log2(math.factorial(mask.bit_count()))
        for mask, mass in enumerate(p)
        if mask.bit_count() >= 2 and mass
    )

    q2 = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            q = sum(
                (p[mask] for mask in range(N) if ((mask >> i) & 1) and ((mask >> j) & 1)),
                Fraction(),
            )
            q2 += float(q * q)

    pair_lower = 2.0 * q2 / float(I)
    assert elogfac + 1e-12 >= float(I - V)
    assert float(I - V) + 1e-12 >= pair_lower

    H = -sum(float(mass) * math.log2(float(mass)) for mass in p if mass)
    return {
        "n": n,
        "H": H,
        "I": float(I),
        "V": float(V),
        "I_minus_V": float(I - V),
        "E_log2_K_factorial": elogfac,
        "D_seq": Dseq,
        "D_companion": Dcomp,
        "pair_q2_factorial_lower": pair_lower,
    }


def parity(n):
    return [1 if x.bit_count() % 2 == 0 else -1 for x in range(1 << n)]


def majority(n):
    assert n % 2 == 1
    return [1 if x.bit_count() > n // 2 else -1 for x in range(1 << n)]


def one_point(n):
    return [-1 if x == 0 else 1 for x in range(1 << n)]


def selector_two_parities(m):
    n = 2 * m + 1
    out = []
    for x in range(1 << n):
        z = (x >> (2 * m)) & 1
        inds = range(m) if z == 0 else range(m, 2 * m)
        bit = sum((x >> i) & 1 for i in inds) & 1
        out.append(1 if bit == 0 else -1)
    return out


def main():
    cases = {
        "parity_8": parity(8),
        "majority_7": majority(7),
        "one_point_7": one_point(7),
        "selector_two_parities_m3": selector_two_parities(3),
    }
    result = {name: analyze(values) for name, values in cases.items()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
