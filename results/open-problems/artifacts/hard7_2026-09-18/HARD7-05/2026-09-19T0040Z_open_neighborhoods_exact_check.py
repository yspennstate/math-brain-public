#!/usr/bin/env python3
"""Exact finite arithmetic self-check for HARD7-05 run 5.

This does NOT certify the analytic all-lag openness theorem. It checks the
rational endpoint data used in its small- and large-lag transversality:
  q(H)=4H/3,
  a(H)=(1-H^2)/2  (source quadratic coefficient),
  b_m(H)=q(H)^2(1-m)/(2m)  (reference quadratic coefficient),
  theta_ref=(3/8)*(q/m)*m=H/2,
  q(H)-H=H/3.
"""
from fractions import Fraction as F

anchors = [
    ("quarter", F(1,4), F(1,10), F(1,32)),
    ("third",   F(1,3), F(1,6),  F(4,81)),
]

for name, H, m, expected_margin in anchors:
    q = F(4,3) * H
    c = q / m
    a = (1 - H*H) / 2
    b = q*q * (1-m) / (2*m)
    margin = b - a
    theta_ref = F(3,8) * c * m
    tail_margin = q - H

    assert margin == expected_margin
    assert margin > 0
    assert theta_ref == H/2
    assert tail_margin == H/3
    assert tail_margin > 0

    # g_m(H)=((16-7m)/(18m))*H^2 - 1/2.
    g_closed = (F(16,1)-7*m) * H*H / (18*m) - F(1,2)
    assert g_closed == margin

    print(f"{name}: H={H}, m={m}, q={q}, c={c}")
    print(f"  source_quadratic_a={a}")
    print(f"  reference_quadratic_b={b}")
    print(f"  local_margin_b_minus_a={margin}")
    print(f"  reference_exponent={theta_ref}")
    print(f"  tail_rate_margin_q_minus_H={tail_margin}")

print("ALL_EXACT_CHECKS_PASS")
