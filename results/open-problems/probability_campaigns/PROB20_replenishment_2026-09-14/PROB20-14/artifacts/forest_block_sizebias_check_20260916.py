from fractions import Fraction

# Exact finite-support critical test law: E[xi]=1.
PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
R = 0.5
QEXP = 1.5


def conv_dist(base, n):
    dist = {0: Fraction(1)}
    for _ in range(n):
        nxt = {}
        for a, pa in dist.items():
            for x, px in base.items():
                nxt[a + x] = nxt.get(a + x, Fraction(0)) + pa * px
        dist = nxt
    return dist


CONV = {n: conv_dist(PI, n) for n in range(31)}


def conditioned_block_sum(m, b):
    target = m - b
    den = CONV[m].get(target, Fraction(0))
    if den == 0:
        return None
    out = {}
    for c, pc in CONV[b].items():
        rem = CONV[m - b].get(target - c, Fraction(0))
        if rem:
            out[c] = pc * rem / den
    return out


def forest_first_generation(m, b):
    target = m - b
    denprob = CONV[m].get(target, Fraction(0))
    if denprob == 0:
        return None
    nu_mb = Fraction(b, m) * denprob  # forest Dwass
    out = {}
    for c, pc in CONV[b].items():
        if c == 0:
            continue
        remprob = CONV[m - b].get((m - b) - c, Fraction(0))
        if remprob:
            nu_child = Fraction(c, m - b) * remprob
            out[c] = pc * nu_child / nu_mb
    return out


identity_checks = 0
tail_checks = 0
max_lhs_rhs_ratio = 0.0

for m in range(2, 26):
    for b in range(1, m):
        q_block = conditioned_block_sum(m, b)
        eta = forest_first_generation(m, b)
        if q_block is None or eta is None:
            continue

        assert sum(eta.values()) == 1

        # Proposition 3.1: eta(c) = m c/[b(m-b)] Q(X_b=c).
        for c, eta_c in eta.items():
            rhs = Fraction(m * c, b * (m - b)) * q_block.get(c, Fraction(0))
            assert eta_c == rhs
            identity_checks += 1

        # Normalization consequence E_Q X_b = b(m-b)/m.
        mean_block = sum(Fraction(c) * p for c, p in q_block.items())
        assert mean_block == Fraction(b * (m - b), m)

        # Check the relative-jump inequality (5.4) for several M values.
        if b <= m / 2:
            den = CONV[m][m - b]
            for M in (1, 4, 9, 16):
                lhs = sum(
                    float(p) * (c ** R)
                    for c, p in eta.items()
                    if c ** R > M * (1 + b ** R)
                )
                K = 0.5 * (M ** (1 / R))
                coordinate_tail = 0.0
                for d, pd in PI.items():
                    rem = CONV[m - 1].get(m - b - d, Fraction(0))
                    if rem and d > K:
                        coordinate_tail += float(pd * rem / den) * (d ** QEXP)
                rhs = (2 ** (QEXP + 1)) * (1 + b ** R) * coordinate_tail
                assert lhs <= rhs + 1e-12
                tail_checks += 1
                if rhs > 0:
                    max_lhs_rhs_ratio = max(max_lhs_rhs_ratio, lhs / rhs)
        else:
            # For b>m/2 and M>=1 the relative-jump event is deterministically empty.
            for c in eta:
                assert c <= m - b < b

print(f"IDENTITY_CHECKS={identity_checks}")
print(f"TAIL_CHECKS={tail_checks}")
print(f"MAX_LHS_RHS_RATIO={max_lhs_rhs_ratio:.16f}")
print("ALL_ASSERTIONS_PASSED")
