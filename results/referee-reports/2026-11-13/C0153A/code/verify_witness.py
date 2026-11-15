"""Exact arithmetic checks of the literature counterexample; no MCMC."""
from fractions import Fraction as F
import json
import math
import os
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)

q, d = 3, 3
w = F(17, 6)
p = w / (1 + w)
nu = (F(9, 17), F(4, 17), F(4, 17))
nu_free = (F(1, 3),) * 3

def bp(message):
    weights = tuple((1 + w * x) ** (d - 1) for x in message)
    return tuple(x / sum(weights) for x in weights)

def pressure_exponential_squared(message):
    vertex = sum((1 + w * x) ** d for x in message)
    edge = 1 + w * sum(x*x for x in message)
    return vertex**2 / edge**d

assert bp(nu) == nu and bp(nu_free) == nu_free
S = sum(x*x for x in nu)
rho_wired = w*S / (1+w*S)
rho_free = w / (q+w)
# Independently sum the Edwards-Sokal joint weights over all color pairs.
joint_Z = sum(nu[i]*nu[j]*(1+w if i == j else 1)
              for i in range(q) for j in range(q))
rho_by_color_pairs = sum(p*(1+w)*nu[i]**2 for i in range(q))/joint_Z
assert rho_wired == rho_by_color_pairs == F(113, 215)
assert rho_free == F(17, 35)
pressure_ratio = pressure_exponential_squared(nu_free)/pressure_exponential_squared(nu)
assert pressure_ratio == F(14749, 14739) > 1
assert rho_wired-rho_free == F(12, 301)
# Second pressure check using direct floating-point logarithms.
def phi(message):
    return (math.log(sum((1+float(w*x))**d for x in message))
            - d/2 * math.log(1+float(w)*sum(float(x)**2 for x in message)))
gap = phi(nu_free)-phi(nu)
assert gap > 0 and abs(gap-0.5*math.log(float(pressure_ratio))) < 2e-15
# Check maximal fixed point by monotone iteration from the wired boundary.
ratio = float(1+w)**2  # one iteration from infinity
for _ in range(10000):
    ratio = (((1+float(w))*ratio+q-1)/(ratio+float(w)+q-1))**(d-1)
assert abs(ratio-2.25) < 1e-10

result = {
    'kind': 'exact algebra and small numerical audit, not simulation evidence',
    'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'd': d, 'q': q, 'w': str(w), 'p': str(p),
    'wired_message': [str(x) for x in nu],
    'free_edge_density': str(rho_free),
    'wired_edge_density': str(rho_wired),
    'density_gap': str(rho_wired-rho_free),
    'exp_twice_free_minus_wired_pressure': str(pressure_ratio),
    'pressure_gap_decimal': gap,
    'wired_bp_ratio_after_10000_iterations': ratio,
    'p_uniqueness_decimal': 2*math.sqrt(2)/(1+2*math.sqrt(2)),
    'p_order_disorder_decimal': 1-1/(1+2**(1/3)+2**(2/3)),
}
root = Path(__file__).resolve().parents[1]
(root/'data').mkdir(exist_ok=True)
out = root/'data'/'witness_verification.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
