#!/usr/bin/env python3
from fractions import Fraction as F

samples = [4, 7, 8, 16, 32, 64, 128]
print("P26 independent reexecution of C30 exact audit arithmetic for C31 AF 4.49(ii) Ramanujan cones")
for s in samples:
    d = s*s
    r = s
    x = F(r*(d+2), d+r)
    y = F(2*(d+2), d+r)
    assert 2*x == r*y
    assert x + F(d,2)*y == d+2

    alpha = F(d+1,d+2)
    beta = F(1,d+2)
    lower = alpha*alpha*y*F(r,2) + 2*alpha*beta*x
    closed = F(r*(d+1)*(d+3),(d+2)*(d+r))
    assert lower == closed

    gap_lower = 1 - F(2*s, s*s+1)
    ratio = closed*gap_lower/2
    L = F((s-1)*(s-1)*(s*s+3), 2*(s+1)*(s*s+2))
    assert ratio == L

    delta = L - F(s-3,2)
    delta_closed = F(5*s*s-2*s+9, 2*(s+1)*(s*s+2))
    assert delta == delta_closed
    assert delta > 0

    print(f"s={s}: budget=PASS lower={closed} ratio_L={L} > (s-3)/2={F(s-3,2)} by {delta}")

baseline = F(10786653,2251652)/(F(51,44)*2)
assert baseline == F(2326533,1125826)
print(f"PG(2,49)_ratio_baseline={baseline}")
print("ALL_EXACT_CHECKS_PASS")
