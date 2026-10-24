from fractions import Fraction

# Run-10 finite route-discovery check for the canonical log-sawtooth gauge.
# At a half-period peak u and the next integer-period trough v=sqrt(2)u,
# g(v)/g(u) <= 2^(3/8).  A peak multiplier H therefore forces an
# actual down-step whenever H > 2^(3/8), equivalently H^8 > 8.

candidates = [Fraction(5, 4), Fraction(4, 3), Fraction(3, 2), Fraction(2, 1)]
print("exact candidate scan for sawtooth height H")
for h in candidates:
    lhs = h ** 8
    ok = lhs > 8
    print(f"H={h}: H^8={lhs}; drop_condition(H^8>8)={ok}")

passing = [h for h in candidates if h ** 8 > 8]
print(f"first_passing={passing[0]}")
print(f"certificate: 4^8={4**8}, 8*3^8={8*(3**8)}, inequality={4**8 > 8*(3**8)}")
assert passing[0] == Fraction(4, 3)
assert 4**8 > 8 * 3**8
print("PASS")
