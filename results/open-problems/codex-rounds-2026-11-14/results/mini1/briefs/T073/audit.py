"""Small exact-arithmetic audit of PROOF.md; Python standard library only."""

import os
import resource

# Fail before the audit if launched without the author's compute constraints.
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))

from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb
import json
from pathlib import Path


def polynomial(e):
    return 2 * e**4 - e**3 - 4 * e + 1


def contraction(e):
    return (2 - 4 * e) * (1 - e**3 / 2)


def decimal(q):
    with localcontext() as ctx:
        ctx.prec = 40
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def record(q):
    return {"exact": str(q), "decimal": decimal(q)}


# p(k) = epsilon + (1/2-epsilon)*g(k).
g = (0, 0, 1, 2, 2)

# Independent update-rule reconstruction: delete one uniformly selected
# neighbor, take the majority of the remaining three, then reverse it with
# probability epsilon. This must reproduce fair ties for four neighbors.
rule_checks = 0
for bits in product((0, 1), repeat=4):
    p_vote = F(sum(sum(bits[i] for i in triple) >= 2
                   for triple in combinations(range(4), 3)), 4)
    assert 2 * p_vote == g[sum(bits)]
    for e in (F(0), F(1, 10), F(2481, 10000), F(1, 2)):
        direct = (e, e, F(1, 2), 1 - e, 1 - e)[sum(bits)]
        independent = e + (1 - 2 * e) * p_vote
        assert direct == independent
        rule_checks += 1


local_pairs = 0
telescoping_orders = 0
minimum_slack = 100
for pair in product(((0, 0), (0, 1), (1, 1)), repeat=4):
    lower = tuple(v[0] for v in pair)
    upper = tuple(v[1] for v in pair)
    disagreement = tuple(u - l for l, u in pair)
    blocked = tuple(any(all(lower[j] == upper[j] == b
                            for j in range(4) if j != i)
                        for b in (0, 1)) for i in range(4))
    lhs = g[sum(upper)] - g[sum(lower)]
    rhs = sum(disagreement[i] * (not blocked[i]) for i in range(4))
    assert 0 <= lhs <= rhs
    minimum_slack = min(minimum_slack, rhs - lhs)
    for order in permutations(range(4)):
        current = list(lower)
        total = 0
        for i in order:
            before = g[sum(current)]
            current[i] = upper[i]
            contribution = g[sum(current)] - before
            assert 0 <= contribution <= disagreement[i]
            if blocked[i]:
                assert contribution == 0
            total += contribution
        assert total == lhs
        telescoping_orders += 1
    local_pairs += 1


# Substitute u = 1-exp(-s): the age integral is integral_0^1 u^3 du.
age_integral_substitution = F(1, 4)
# Independent expansion in exp(-s), integrating each exponential separately.
age_integral_expansion = sum(F((-1)**j * comb(3, j), j + 1)
                             for j in range(4))
# Independent exponential-clock ordering check: y must have the oldest
# last-ring time among the four distinct rate-one clocks.
orders = list(permutations(range(4)))
age_integral_clock_race = F(sum(order[0] == 0 for order in orders), len(orders))
assert age_integral_substitution == age_integral_expansion == age_integral_clock_race
blocking_coefficient = 2 * age_integral_substitution
assert blocking_coefficient == F(1, 2)


endpoint = F(2481, 10000)
# Expanded polynomial versus unexpanded coupling contraction.
endpoint_poly = polynomial(endpoint)
endpoint_factored = contraction(endpoint) - 1
assert endpoint_poly == endpoint_factored < 0
raw_numerator = (2 * 2481**4 - 2481**3 * 10000
                 - 4 * 2481 * 10000**3 + 10000**4)
assert endpoint_poly == F(raw_numerator, 10000**4)

# Decimal grid bracketing, independently of bisection.
grid_lo = F(248076, 1000000)
grid_hi = F(248077, 1000000)
# Check this independently selected decimal grid without changing its endpoints.
assert polynomial(grid_lo) > 0 > polynomial(grid_hi)

lo, hi = F(0), F(1, 2)
for _ in range(50):
    mid = (lo + hi) / 2
    if polynomial(mid) > 0:
        lo = mid
    else:
        hi = mid
assert polynomial(lo) > 0 > polynomial(hi)
assert grid_lo < lo < hi < grid_hi < endpoint < F(1, 4)


result = {
    "status": "all assertions passed",
    "compute": {"nice": os.getpriority(os.PRIO_PROCESS, 0),
                "OMP_NUM_THREADS": os.environ["OMP_NUM_THREADS"],
                "cpu_time_limit_seconds": 30},
    "update_rule_checks": rule_checks,
    "ordered_local_pairs": local_pairs,
    "pair_order_checks": telescoping_orders,
    "minimum_local_slack_in_units_of_half_minus_epsilon": minimum_slack,
    "age_integral_substitution": record(age_integral_substitution),
    "age_integral_expansion": record(age_integral_expansion),
    "age_integral_clock_ordering": record(age_integral_clock_race),
    "blocking_coefficient_before_epsilon_cubed": record(blocking_coefficient),
    "rational_endpoint": record(endpoint),
    "contraction_at_endpoint": record(contraction(endpoint)),
    "polynomial_at_endpoint": record(endpoint_poly),
    "polynomial_raw_numerator_denominator_10_to_16": raw_numerator,
    "root_grid_lower": record(grid_lo),
    "root_grid_upper": record(grid_hi),
    "root_lower": record(lo),
    "root_upper": record(hi),
    "root_bracket_width": record(hi - lo),
    "improvement_from_one_quarter_at_rational_endpoint": record(F(1, 4) - endpoint),
    "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
output = json.dumps(result, indent=2, sort_keys=True) + "\n"
Path(__file__).with_name("audit_output.json").write_text(output)
print(output, end="")
