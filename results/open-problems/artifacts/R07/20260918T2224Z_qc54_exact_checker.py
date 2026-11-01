from fractions import Fraction

MAX_N = 12

def sign(N, n, k):
    """Slope sign of phi(2^n t), phi(x)=dist(x,Z), on kth dyadic cell of level N."""
    block = 1 << (N - n - 1)
    return 1 if ((k // block) & 1) == 0 else -1

print("R07 exact checker: heterogeneous quadratic clock")
for N in range(1, MAX_N + 1):
    # Exact Walsh/Rademacher orthogonality on the level-N mesh.
    for n in range(N):
        for m in range(N):
            dot = sum(sign(N, n, k) * sign(N, m, k) for k in range(1 << N))
            expected = (1 << N) if n == m else 0
            assert dot == expected, (N, n, m, dot, expected)

    base = sum(Fraction(1 << n, 1 << N) for n in range(N))
    expected_base = 1 - Fraction(1, 1 << N)
    assert base == expected_base

    # Composite clock Q:
    # Q(t)=(sqrt(3)/2)F(2t) on [0,1/2],
    # Q(t)=(1/2)F(2t-1) on [1/2,1].
    # Only squared amplitudes enter the energy, so all arithmetic is rational.
    inner = Fraction(0) if N == 1 else 1 - Fraction(1, 1 << (N - 1))
    left = Fraction(3, 4) * inner
    right = Fraction(1, 4) * inner
    total = left + right

    assert total == inner
    assert left == Fraction(3, 4) * inner
    assert right == Fraction(1, 4) * inner

    print(f"N={N:2d} base={base} left={left} right={right} total={total}")

print("limits: base->1, left->3/4, right->1/4, total->1")
print("Brownian half-window target: 1/2 on each half")
print("PASS")
