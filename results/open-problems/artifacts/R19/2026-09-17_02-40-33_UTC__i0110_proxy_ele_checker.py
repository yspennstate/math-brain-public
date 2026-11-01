from fractions import Fraction


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def centered_defect(r, pi):
    m = sum(r)
    return sum((ri - m * pii) ** 2 / pii for ri, pii in zip(r, pi))


# Exact rational toy instances exercising BOTH trimming sets in the proof:
# B = relative proxy-error states, C = tiny stationary-mass states.
for N in [16, 32, 64, 128]:
    tiny = Fraction(1, N**3)
    rest = (1 - tiny) / Fraction(N - 1, 1)
    pi = [tiny] + [rest] * (N - 1)

    # Move O(1/N) proxy mass between two ordinary states. TV(q,pi)->0,
    # but those two states violate a fixed relative-error threshold.
    delta = Fraction(1, 2 * N)
    q = pi.copy()
    q[1] -= delta
    q[2] += delta
    assert q[1] >= 0

    eps = Fraction(1, N)
    zeta = Fraction(1, N)
    s = [(1 - zeta) * x for x in q]

    # Fixed finite thresholds only for this self-check.
    a = Fraction(1, 4)
    b = Fraction(1, 4)
    B = {j for j, (qi, pii) in enumerate(zip(q, pi)) if abs(qi - pii) > a * pii}
    C = {j for j, pii in enumerate(pi) if pii < b / Fraction(N, 1)}
    G = [j for j in range(N) if j not in B and j not in C]

    # Pointwise proxy domination assumed by the bridge lemma.
    assert sum(pi) == 1
    assert sum(q) == 1
    assert sum(s) == 1 - zeta
    for si, qi in zip(s, q):
        assert si <= (1 + eps) * qi + eps / Fraction(N, 1)

    delta_tv = tv(q, pi)
    piB = sum(pi[j] for j in B)
    qB = sum(q[j] for j in B)
    sB = sum(s[j] for j in B)
    piC = sum(pi[j] for j in C)
    qC = sum(q[j] for j in C)
    sC = sum(s[j] for j in C)

    # Exact trimming estimates from the proof.
    assert piB <= 2 * delta_tv / a
    assert qB <= piB + 2 * delta_tv
    assert sB <= (1 + eps) * qB + eps * Fraction(len(B), N)
    assert piC <= b
    assert qC <= piC + 2 * delta_tv
    assert sC <= (1 + eps) * qC + eps * Fraction(len(C), N)

    r = [s[j] if j in G else Fraction(0, 1) for j in range(N)]
    m = sum(r)
    c = (1 + eps) * (1 + a) + eps / b - 1
    for j in G:
        assert r[j] <= (1 + c) * pi[j]

    D = centered_defect(r, pi)
    bound = c + (1 - m)
    assert D <= bound

    print(
        f"N={N} TV={delta_tv} B={sorted(B)} C={sorted(C)} "
        f"m={m} D={D} bound={bound}"
    )

# Pure exact algebra behind the last step of the general proof.
pi = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
f = [Fraction(0, 1), Fraction(6, 5), Fraction(9, 10)]
c = Fraction(1, 5)
m = sum(p * x for p, x in zip(pi, f))
D = sum(p * (x - m) ** 2 for p, x in zip(pi, f))
assert D == sum(p * x * x for p, x in zip(pi, f)) - m * m
assert D <= m * (1 + c - m) <= c + (1 - m)
print(
    "algebraic_bound_exact:",
    "m=", m,
    "D=", D,
    "sharp_upper=", m * (1 + c - m),
    "coarse_upper=", c + (1 - m),
)
print("ALL_EXACT_CHECKS_PASS")
