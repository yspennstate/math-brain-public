#!/usr/bin/env python3
"""ProofNet24 P17 M41 arithmetic certificate.

This script evaluates only the explicit constants in the analytic theorem
P17-M41-RATIONAL-MAGNETIC-BLOCH-GRID-37.  It is not an eigenvalue
certificate and does not claim a magnetic spectral gap.

For rational source frequencies theta_i=p_i/Q_i and magnetic flux b=p/q,
a Landau-gauge period cell has dimensions
    P1=lcm(Q1,q),  P2=Q2,
while the gauge with the magnetic phase in the other direction has
    P1=Q1, P2=lcm(Q2,q).
The smaller of the two cells may be used.

For a uniform N-point angular grid in all four residual parameters
(alpha1,alpha2,beta1,beta2), the theorem gives

  epsilon_grid <= C/N,
  C = 4*pi*r*A*(1/Q1+1/Q2)
      + 2*pi*A*(1/P1+1/P2),
  A = exp(-(1-2*r)).

The historical Figure-4.3.3 rational pair is Q1=153,Q2=148, r=0.4.
At b=1/153 the Landau-gauge magnetic period is already 153, so the
finite Bloch matrices remain 153*148=22644 dimensional.
"""
from math import exp, gcd, pi


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def constants(Q1: int, Q2: int, q: int, r: float):
    A = exp(-(1.0 - 2.0*r))
    landau = (lcm(Q1, q), Q2)
    swapped = (Q1, lcm(Q2, q))
    cell = min((landau, swapped), key=lambda p: p[0]*p[1])
    P1, P2 = cell
    hull_coeff = 4*pi*r*A*(1/Q1 + 1/Q2)
    bloch_coeff = 2*pi*A*(1/P1 + 1/P2)
    return {
        "A": A,
        "landau_cell": landau,
        "swapped_cell": swapped,
        "chosen_cell": cell,
        "matrix_dimension": P1*P2,
        "hull_equal_grid_coefficient": hull_coeff,
        "bloch_equal_grid_coefficient": bloch_coeff,
        "all_four_equal_grid_coefficient": hull_coeff+bloch_coeff,
    }


def main():
    d = constants(153, 148, 153, 0.4)
    for k, v in d.items():
        print(f"{k} = {v}")
    assert d["chosen_cell"] == (153, 148)
    assert d["matrix_dimension"] == 22644
    assert abs(d["hull_equal_grid_coefficient"] - 0.054704658135346126) < 1e-15
    assert abs(d["bloch_equal_grid_coefficient"] - 0.06838082266918266) < 1e-15
    assert abs(d["all_four_equal_grid_coefficient"] - 0.12308548080452879) < 1e-15


if __name__ == "__main__":
    main()
