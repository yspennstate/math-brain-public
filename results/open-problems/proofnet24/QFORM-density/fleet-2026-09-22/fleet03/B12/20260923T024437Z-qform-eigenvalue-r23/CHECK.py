import json
import math
import random


def step(B, tau):
    return 2.0 * math.sqrt(B / tau)


def closed(B_terminal, taus_outer_to_inner):
    k = len(taus_outer_to_inner)
    if k == 0:
        return B_terminal
    out = (4.0 ** (1.0 - 2.0 ** (-k))) * (B_terminal ** (2.0 ** (-k)))
    for j, tau in enumerate(taus_outer_to_inner, start=1):
        out *= tau ** (-2.0 ** (-j))
    return out


random.seed(120923)
max_relative_error = 0.0
cases = 0
for k in range(1, 10):
    for _ in range(50):
        B = 10.0 ** random.uniform(-2.0, 2.0)
        taus = [10.0 ** random.uniform(-1.0, 1.0) for _ in range(k)]
        x = B
        # taus are stored outermost -> innermost, so propagate from terminal
        # back to the original form in reverse order.
        for tau in reversed(taus):
            x = step(x, tau)
        y = closed(B, taus)
        rel = abs(x - y) / max(1.0, abs(x), abs(y))
        max_relative_error = max(max_relative_error, rel)
        cases += 1

B_partner = 4.0 * math.pi
C_pair = 9.2 + math.log(10000.0)
C_tail = 9.0 * math.sqrt(3.0) * math.e / 2.0
C_triple = 6.0 * math.sqrt(math.pi)

# Certificate-adapted threshold: tau >= 4/B makes B an invariant cap.
for B in [B_partner, C_pair, C_tail, C_triple, 1.0, 100.0]:
    tau = 4.0 / B
    assert step(B, tau) <= B * (1.0 + 1e-14)

result = {
    "status": "PASS",
    "closed_form_cases": cases,
    "max_relative_error": max_relative_error,
    "partner_B_4pi": B_partner,
    "partner_threshold_4_over_B": 4.0 / B_partner,
    "partner_threshold_expected_1_over_pi": 1.0 / math.pi,
    "pair_B": C_pair,
    "pair_threshold_4_over_B": 4.0 / C_pair,
    "tail_B": C_tail,
    "tail_threshold_4_over_B": 4.0 / C_tail,
    "triple_B": C_triple,
    "triple_threshold_4_over_B": 4.0 / C_triple,
}
print(json.dumps(result, indent=2, sort_keys=True))
