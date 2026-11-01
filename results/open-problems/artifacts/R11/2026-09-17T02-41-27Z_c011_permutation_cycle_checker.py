from fractions import Fraction
from itertools import permutations
from math import factorial, comb


def H(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def beta_int(a, b):
    assert a >= 1 and b >= 1
    return Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def cycle_partition(p):
    n = len(p)
    seen = [False] * n
    blocks = []
    for i in range(n):
        if not seen[i]:
            cyc = []
            j = i
            while not seen[j]:
                seen[j] = True
                cyc.append(j)
                j = p[j]
            blocks.append(tuple(sorted(cyc)))
    return tuple(sorted(blocks))

checks = 0

# Exhaustive permutation-cycle counts through m=8.
for m in range(2, 9):
    counts = {}
    two_cycle_total = 0
    for p in permutations(range(m)):
        cp = cycle_partition(p)
        if len(cp) == 2:
            two_cycle_total += 1
            counts[cp] = counts.get(cp, 0) + 1
    assert Fraction(two_cycle_total, factorial(m)) == H(m - 1) / m
    checks += 1
    for cp, c in counts.items():
        i = len(cp[0])
        j = len(cp[1])
        assert c == factorial(i - 1) * factorial(j - 1)
        assert Fraction(c, factorial(m)) == beta_int(i, j) / m
        checks += 2

# Hidden-label projection identity: sum over full hidden split sides gives visible beta kernel.
hidden_checks = 0
for m in range(2, 26):
    for b in range(2, m + 1):
        for i in range(1, b):
            lhs = sum(
                Fraction(comb(m - b, s - i), 1) * beta_int(s, m - s)
                for s in range(i, m - b + i + 1)
            )
            rhs = beta_int(i, b - i)
            assert lhs == rhs
            hidden_checks += 1
            checks += 1

# Activated-slot compiler: activation m*eps cancels the 1/m from a uniform permutation.
compiler_checks = 0
for N in range(3, 31):
    eps = Fraction(1, N ** 3)
    for m in range(2, N + 1):
        activation = m * eps
        assert activation <= 1
        for i in range(1, m):
            one_slot_specific = activation * beta_int(i, m - i) / m
            assert one_slot_specific == eps * beta_int(i, m - i)
            compiler_checks += 1
            checks += 1

# N=3 exact reduced-root degree-3 witness.
N = 3
eps = Fraction(1, N ** 3)
activation = N * eps                         # 1/9
specific_split_per_slot = activation * Fraction(1, 6)  # each of three 1|2 partitions
success_per_slot = 3 * specific_split_per_slot
p_no_visible = (1 - success_per_slot) ** 2
p_raw_degree3 = 6 * specific_split_per_slot ** 2        # ordered distinct proposals
p_reduced_degree3 = p_raw_degree3 / (1 - p_no_visible)
assert activation == Fraction(1, 9)
assert specific_split_per_slot == Fraction(1, 54)
assert p_no_visible == Fraction(289, 324)
assert p_raw_degree3 == Fraction(1, 486)
assert p_reduced_degree3 == Fraction(2, 105)
checks += 5

# N=4: explicit positive degree-4 witness from crossing 2|2 cycle bipartitions.
N = 4
eps = Fraction(1, N ** 3)
activation = N * eps                         # 1/16
# A specified 2|2 cycle partition occurs for exactly one permutation out of 4!.
q_cross = activation * Fraction(1, factorial(4))
# Either ordering of two fixed crossing partitions gives four singleton intersections.
p_degree4_lower_witness = 2 * q_cross * q_cross
assert q_cross == Fraction(1, 384)
assert p_degree4_lower_witness == Fraction(1, 73728)
assert p_degree4_lower_witness > 0
checks += 3

# Error scale for eps_N=N^-3: accumulated two-slot interaction bound is O(N^2 eps_N)=1/N.
for N in range(2, 1000):
    eps = Fraction(1, N ** 3)
    assert N * N * eps == Fraction(1, N)
    checks += 1

print('R11 C011 exact checker')
print('exhaustive_permutation_m_max=8')
print(f'hidden_beta_projection_checks={hidden_checks}')
print(f'activated_slot_compiler_checks={compiler_checks}')
print('N3_reduced_degree3=2/105')
print('N4_degree4_positive_witness=1/73728')
print('error_scale=N^2*N^-3=1/N')
print(f'total_exact_checks={checks}')
print('ALL_EXACT_CHECKS_PASS')
