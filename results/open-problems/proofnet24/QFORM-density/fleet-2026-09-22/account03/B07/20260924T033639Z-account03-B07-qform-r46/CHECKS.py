from fractions import Fraction
import math
import random

SEED = 2026092407
random.seed(SEED)

# Exact rational checks of the rank-one level-set parameterization.
triples = [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29)]
exact_trials = 0
for aa, bb, cc in triples:
    for swap in (False, True):
        if swap:
            u1, u2 = Fraction(bb,cc), Fraction(aa,cc)
        else:
            u1, u2 = Fraction(aa,cc), Fraction(bb,cc)
        v1, v2 = -u2, u1
        lam = Fraction(7,3)
        s = Fraction(2,5)
        t = Fraction(-11,7)
        C = Fraction(-5,8)
        q0 = Fraction(13,9)
        c1, c2 = s*u1+t*v1, s*u2+t*v2
        for y in [Fraction(-3,2), Fraction(-1,3), Fraction(0), Fraction(2,7), Fraction(5,4)]:
            z = (q0-C-lam*y*y-2*s*y)/(2*t)
            x1, x2 = u1*y+v1*z, u2*y+v2*z
            uy = u1*x1+u2*x2
            q = lam*uy*uy + 2*c1*x1 + 2*c2*x2 + C
            assert q == q0
            exact_trials += 1
        assert max(v1*v1, v2*v2) >= Fraction(1,2)
        chosen = -v1*lam/(2*t) if v1*v1 >= v2*v2 else -v2*lam/(2*t)
        assert chosen*chosen >= lam*lam/(8*t*t)

# Floating regression over arbitrary orientations and signs. This is not proof evidence.
max_rel_error = 0.0
min_lead_ratio = float('inf')
float_trials = 5000
for _ in range(float_trials):
    th = random.random()*2*math.pi
    u1, u2 = math.cos(th), math.sin(th)
    v1, v2 = -u2, u1
    lam = random.choice((-1.0,1.0))*10**random.uniform(-2,2)
    t = random.choice((-1.0,1.0))*10**random.uniform(-2,2)
    s = random.uniform(-3,3)
    C = random.uniform(-3,3)
    q0 = random.uniform(-3,3)
    y = random.uniform(-4,4)
    z = (q0-C-lam*y*y-2*s*y)/(2*t)
    x1, x2 = u1*y+v1*z, u2*y+v2*z
    c1, c2 = s*u1+t*v1, s*u2+t*v2
    uy = u1*x1+u2*x2
    q = lam*uy*uy + 2*c1*x1 + 2*c2*x2 + C
    max_rel_error = max(max_rel_error, abs(q-q0)/(1+abs(q0)))
    if abs(v1) >= abs(v2):
        lead = abs(-v1*lam/(2*t))
    else:
        lead = abs(-v2*lam/(2*t))
    lower = abs(lam)/(2*math.sqrt(2)*abs(t))
    min_lead_ratio = min(min_lead_ratio, lead/lower)

# Propagated exact constants in the r40 application.
delta = 2**-10
pair_constant = 4*math.sqrt(2)
pair_density = pair_constant/math.sqrt(delta)
residual_energy = (1/512)/(delta**2)
partner_density = 2*math.sqrt(18*math.pi)/(3/256)
assert abs(residual_energy-2048) < 1e-12
assert pair_density < 181.02
assert partner_density < 1283.394
assert min_lead_ratio >= 1-1e-12
assert max_rel_error < 1e-7

print(f"seed={SEED}")
print(f"exact_levelset_trials={exact_trials}")
print(f"float_levelset_trials={float_trials}")
print(f"max_relative_levelset_error={max_rel_error:.3e}")
print(f"min_quadratic_lead_ratio_to_bound={min_lead_ratio:.12f}")
print(f"pair_receiver_constant_4sqrt2={pair_constant:.15f}")
print(f"delta=2^-10={delta:.15f}")
print(f"pair_density_if_|lambda|S>=delta={pair_density:.15f}")
print(f"residual_harmonic_star_energy_lower_bound={residual_energy:.15f}")
print(f"partner_r0_density_constant={partner_density:.15f}")
print("STATUS=PASS")
