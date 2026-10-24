from fractions import Fraction
from math import comb, factorial, gcd


def fall(a, r):
    z = 1
    for t in range(r):
        z *= a - t
    return z


def ceil_log2(n):
    assert n >= 1
    return (n - 1).bit_length()


def K(N):
    return min(N, max(2, N.bit_length() - 1))


def constraint_upper(N):
    k = K(N)
    return (2 * N) ** (k + 2)


def exact_constraint_count(N):
    k = K(N)
    return (N - 1) * sum(comb(N, b) * (2 ** b) for b in range(1, k + 1))


def params(N):
    C = constraint_upper(N)
    L = 2 + ceil_log2(2 * C)
    M = N ** 6 * L + 1
    return C, L, M


def hprob(N, s, i, j):
    den = fall(N, i + j)
    return Fraction(
        fall(s, i) * fall(N - s, j) + fall(s, j) * fall(N - s, i),
        den,
    )


def beta(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))


def harmonic(n):
    return sum(Fraction(1, r) for r in range(1, n + 1))


checks = 0
lines = []
for N in range(3, 41):
    k = K(N)
    C, L, M = params(N)
    D = exact_constraint_count(N)

    # Number of all phase/cylinder constraints is bounded by C_N.
    assert D <= C
    checks += 1

    # L_N is chosen so 2^(L_N-2) >= 2 C_N.
    assert (1 << (L - 2)) >= 2 * C
    checks += 1

    # Hoeffding + union bound is strictly < 1 because
    # 2 C exp(-2 M/N^6) < 2 C 2^(-2L) < 1.
    assert 2 * C < (1 << (2 * L))
    checks += 1

    # M_N = 1 mod N, which forces nonuniform singleton occupation counts
    # at phase s=1 for every deterministic M_N-multiset.
    assert M % N == 1 and gcd(M, N) == 1
    checks += 2

    eps = Fraction(1, N ** 3)

    # Every good family must use singleton {1} at phase s=1 because its
    # target frequency 1/N is farther than eps from 0.
    assert Fraction(1, N) - eps > 0
    checks += 1

    # Harmonic weight normalization and generator-error envelope.
    wsum = sum(Fraction(N, 2 * s * (N - s)) for s in range(1, N))
    assert wsum == harmonic(N - 1)
    checks += 1
    assert 2 * eps * wsum <= Fraction(2, N ** 2)
    checks += 1

    # Exact hypergeometric beta-kernel identity on a finite core.
    for i in range(1, min(5, N)):
        for j in range(1, min(5, N - i + 1)):
            if i + j <= N:
                q = sum(
                    Fraction(N, 2 * s * (N - s)) * hprob(N, s, i, j)
                    for s in range(1, N)
                )
                assert q == beta(i, j)
                checks += 1

    lines.append(
        f"N={N} K={k} C={C} L={L} M={M} D={D} gcd(M,N)={gcd(M,N)}"
    )

for N in range(3, 41):
    _, _, M = params(N)
    assert M % N == 1
    checks += 1

print(f"EXACT_CHECKS={checks}")
print("DESIGN_EXISTENCE_CERTIFICATE: for each N, the union-bound upper envelope is strictly < 1")
print("M_MOD_N_CERTIFICATE: M_N == 1 (mod N), so phase-s=1 empirical singleton counts cannot be label-uniform")
print("GENERATOR_CERTIFICATE: exact hypergeometric beta identity verified on all tested finite cores")
print("ERROR_CERTIFICATE: 2 eps_N H_{N-1} <= 2/N^2")
print("PARAMETER_SAMPLES:")
for line in lines[:5] + lines[-3:]:
    print(line)
print("ALL_EXACT_CHECKS_PASS")
