import math

p0 = 6*math.sqrt(3)*math.atanh((math.sqrt(2)-1)/math.sqrt(3))
partner_obstruction = 3*math.sqrt(2)
analytic_upper = 9*(1-1/math.sqrt(2))

assert p0 < analytic_upper < 3 < math.pi < partner_obstruction
assert partner_obstruction - p0 > 1.7

c0 = math.sqrt(3)/2
# Deterministic sanity check of the exact two-sheet pointwise comparison.
# b=sqrt(3)*max_i d_i ranges in [1/sqrt(2),sqrt(2)] for unit d in e^perp.
for ia in range(1, 200):
    a = (c0*c0) * ia/200
    r0 = math.sqrt(a)
    for ib in range(201):
        b = 1/math.sqrt(2) + (math.sqrt(2)-1/math.sqrt(2))*ib/200
        L = c0/(1+b)
        test = r0 + L + b*math.sqrt(L*L + 2*r0*L)
        assert test > c0

print(f"p0={p0:.16f}")
print(f"analytic_upper={analytic_upper:.16f}")
print(f"3sqrt2={partner_obstruction:.16f}")
print(f"gap_to_3sqrt2={partner_obstruction-p0:.16f}")
print("PASS HOUSEHOLDER_GLOBAL_MAX_SANITY")
