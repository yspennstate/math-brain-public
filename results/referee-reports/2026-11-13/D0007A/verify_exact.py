"""Exact identities for Proposition 9 and the power-density lower bound.

The earlier reservoir audit is retained independently at
sources/prior_check_general.py; execute it directly for its 1000 trials.
"""
from fractions import Fraction as Q
import json
import math
from pathlib import Path


def main():
    n, k, delta, theta, distance = Q(19), Q(9), Q(1, 10), Q(19, 20), Q(9, 20)
    shift = theta*k*(k+1)*delta/n
    assert shift == distance
    assert -distance-n*delta/2 == Q(-7, 5)
    assert -distance+n*delta/2 == Q(1, 2)
    assert Q(-7, 5)+delta < 0 < Q(1, 2)-delta
    for p in [Q(9, 19), Q(10, 19)]:
        top_mean = theta*(1-p)*delta/2
        bottom_mean = -theta*p*delta/2
        assert p*top_mean+(1-p)*bottom_mean == 0
    for odd_n in range(3, 18, 2):
        assert odd_n*Q(1, 40) < distance
    # Integral_0^a (a-x)^2 * 5*x^4 dx, a=1/6.
    a = Q(1, 6)
    lower = 5*(a*a*a**5/5-2*a*a**6/6+a**7/7)
    assert lower == a**7/21 == Q(1, 5878656)
    beta_minimum = Q(105)*Q(3, 4)**2*Q(1, 4)**4
    assert beta_minimum == Q(945, 4096)
    beta_q = beta_minimum/2
    assert 216*beta_q < 25 <= 217*beta_q
    record = dict(two_band_shift=str(shift), theta=str(theta),
                  power4_n5_variance_lower=str(lower),
                  power4_n5_rms_lower=math.sqrt(float(lower)),
                  beta_3_5_uniform_piece_bound=217,
                  assertions="exact rational checks passed")
    Path("data").mkdir(exist_ok=True)
    Path("data/additional_exact_checks.json").write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
