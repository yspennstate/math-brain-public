from fractions import Fraction
from itertools import product

p = Fraction(1, 8)
eps = Fraction(1, 8)


def covariance_for_pattern(pattern):
    am, a0, ap, bm, b0, bp = pattern
    probs = (p, 1 - 2*p, p)
    av = (am, a0, ap)
    bv = (bm, b0, bp)
    ea = sum(q*a for q, a in zip(probs, av))
    eb = sum(q*b for q, b in zip(probs, bv))
    eab = sum(q*a*b for q, a, b in zip(probs, av, bv))
    return eab - ea*eb


valid = []
for pattern in product((0, 1), repeat=6):
    am, a0, ap, bm, b0, bp = pattern
    if not (am >= a0 >= ap and bm >= b0 >= bp):
        continue
    rx, sx = am-a0, a0-ap
    rz, sz = bm-b0, b0-bp
    # Lemma-2.3-style one-discrepancy constraint at distinct x,z:
    # a single adjacent addition cannot change both target hole indicators.
    if rx*rz != 0 or sx*sz != 0:
        continue
    valid.append(pattern)
    lhs = covariance_for_pattern(pattern)
    rhs = p*p*(rx*sz + sx*rz)
    assert lhs == rhs, (pattern, lhs, rhs)

assert len(valid) == 14

# Exact mixture diagnostic: with probability eps the first addition changes x
# and the second changes z; otherwise neither target changes. Each realized
# nested pattern obeys monotonicity and same-step mutual exclusion, but after
# mixing the positive covariance is first-order in p*eps rather than p^2*eps.
cross = (1, 0, 0, 1, 1, 0)
no_change = (1, 1, 1, 1, 1, 1)
weights = (eps, 1-eps)
patterns = (cross, no_change)
probs = (p, 1-2*p, p)

ea = eb = eab = Fraction(0)
for w, pattern in zip(weights, patterns):
    am, a0, ap, bm, b0, bp = pattern
    for q, a, b in zip(probs, (am, a0, ap), (bm, b0, bp)):
        ea += w*q*a
        eb += w*q*b
        eab += w*q*a*b
cov = eab - ea*eb
assert cov == Fraction(57, 4096)

# Verify the total-covariance / cross-switch formula for this mixture.
def moments(pattern):
    am, a0, ap, bm, b0, bp = pattern
    return (am-a0, a0-ap, bm-b0, b0-bp)

rho_x = rho_z = sigma_x = sigma_z = chi = Fraction(0)
for w, pattern in zip(weights, patterns):
    rx, sx, rz, sz = moments(pattern)
    rho_x += w*rx
    sigma_x += w*sx
    rho_z += w*rz
    sigma_z += w*sz
    chi += w*(rx*sz + sx*rz)
ux = (1-p)*rho_x + p*sigma_x
uz = (1-p)*rho_z + p*sigma_z
formula = p*chi - ux*uz
assert formula == cov
assert chi == eps
assert cov > p*p*eps
assert cov < p*eps

print(f"valid deterministic nested patterns: {len(valid)}")
print("deterministic identity: Cov_eta = p^2 (R_x S_z + S_x R_z): PASS")
print(f"mixture p={p}, eps={eps}")
print(f"rho_x={rho_x}, sigma_x={sigma_x}, rho_z={rho_z}, sigma_z={sigma_z}, chi={chi}")
print(f"mixture covariance = {cov} = {float(cov):.12f}")
print(f"p^2 eps = {p*p*eps}; p eps = {p*eps}")
print("total-covariance cross-switch formula: PASS")
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
