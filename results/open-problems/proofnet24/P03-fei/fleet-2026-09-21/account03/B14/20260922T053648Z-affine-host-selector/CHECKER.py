from fractions import Fraction
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext

# Source host edges and their physical pivot directions.
PAIRS = [(78,79),(113,121),(228,484),(170,186),(149,151),
         (338,466),(284,316),(291,295),(393,457)]
PIVOTS = [0,3,8,4,1,7,5,2,6]

assert sorted(PIVOTS) == list(range(9))
assert len({x for e in PAIRS for x in e}) == 18
for (u,v), r in zip(PAIRS, PIVOTS):
    assert (u ^ v) == (1 << r)

# Exact affine split-count distribution.  A query a.x+c splits host j iff a_rj=1.
hist = Counter()
for a in range(1, 1 << 9):
    split = sum((a >> r) & 1 for r in PIVOTS)
    hist[split] += 1
assert hist == Counter({1:9,2:36,3:84,4:126,5:126,6:84,7:36,8:9,9:1})

# Exact physical decision-tree DP: maximize number of original host edges reached
# intact as terminal one-dimensional subcubes.
FULL_MASK = (1 << 9) - 1

def consistent(vertex, fixed_mask, fixed_values):
    return ((vertex ^ fixed_values) & fixed_mask) == 0

def intact_edge_terminal(fixed_mask, fixed_values):
    # A state is exactly an original host edge when 8 bits are fixed and both
    # edge endpoints remain.  Its pivot bit must be the only free bit.
    if fixed_mask.bit_count() != 8:
        return None
    free = next(i for i in range(9) if not ((fixed_mask >> i) & 1))
    for j, ((u,v), r) in enumerate(zip(PAIRS, PIVOTS)):
        if r == free and consistent(u,fixed_mask,fixed_values) and consistent(v,fixed_mask,fixed_values):
            return j
    return None

@lru_cache(None)
def best(fixed_mask, fixed_values):
    term = intact_edge_terminal(fixed_mask, fixed_values)
    if term is not None:
        return 1
    free_bits = [i for i in range(9) if not ((fixed_mask >> i) & 1)]
    if not free_bits:
        return 0
    ans = 0
    for i in free_bits:
        m2 = fixed_mask | (1 << i)
        v0 = fixed_values & ~(1 << i)
        v1 = fixed_values | (1 << i)
        ans = max(ans, best(m2,v0) + best(m2,v1))
    return ans

root_best = best(0,0)
assert root_best == 8
first_scores = {}
for i in range(9):
    first_scores[i] = best(1<<i,0) + best(1<<i,1)
assert set(first_scores.values()) == {8}

# Find which host-edge terminal labels can be preserved after root x0 by an
# optimal continuation.  A set-valued companion recursion chooses one optimum.
@lru_cache(None)
def best_set(fixed_mask, fixed_values):
    term = intact_edge_terminal(fixed_mask, fixed_values)
    if term is not None:
        return frozenset([term])
    free_bits = [i for i in range(9) if not ((fixed_mask >> i) & 1)]
    if not free_bits:
        return frozenset()
    bestS = frozenset()
    for i in free_bits:
        m2 = fixed_mask | (1 << i)
        S = best_set(m2, fixed_values & ~(1<<i)) | best_set(m2, fixed_values | (1<<i))
        if len(S) > len(bestS):
            bestS = S
    return bestS

preserved_after_x0 = best_set(1,0) | best_set(1,1)
assert preserved_after_x0 == frozenset(range(1,9))

# Exact uniform weights and Poincare arithmetic.
q = Fraction(2, 512)  # one host edge
assert 8*q == Fraction(1,32)
assert 2*Fraction(1,512) + 8*q + Fraction(247,256) == 1

b = Fraction(1,256)
omega = b*(1-b)/4
scaled_omega = q*omega
assert omega == Fraction(255,262144)
assert scaled_omega == Fraction(255,67108864)

a_star = Fraction(2682048,10_000_000)
lift_contribution = a_star * scaled_omega

getcontext().prec = 70
Mplus = Decimal('6.52185121301287772365150440023918196647146413881')
Cstar = Decimal('6.5218512')
required = Decimal(266) * (Mplus-Cstar)

assert required == Decimal('0.00000346142547449130017046362240308140946092346')

print('PASS')
print('affine_split_histogram', dict(sorted(hist.items())))
print('optimal_intact_edges', root_best)
print('every_physical_first_query_score', first_scores)
print('preserved_after_x0', sorted(preserved_after_x0))
print('uniform_intact_terminal_mass', Fraction(1,32))
print('uniform_split_endpoint_mass_each', Fraction(1,512))
print('uniform_constant_terminal_mass', Fraction(247,256))
print('omega_source', omega)
print('scaled_omega', scaled_omega)
print('stable_quadratic_split_contribution', Decimal(lift_contribution.numerator)/Decimal(lift_contribution.denominator))
print('threat_corridor_sufficient_delta', required)
