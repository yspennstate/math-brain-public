import math

tau = 1/128
q = math.sqrt(tau + tau*tau)
delta = tau + q
mu = 1 - delta
lev = 2*q*q/(mu*mu)
density_constant = 4/mu

print(f"tau={tau:.17g}")
print(f"q={q:.15f}")
print(f"delta={delta:.15f}")
print(f"mu={mu:.15f}")
print(f"leverage_upper={lev:.15f}")
print(f"leverage_gate={lev <= 0.5}")
print(f"density_constant={density_constant:.15f}")
assert mu > 0
assert lev < 0.5
assert density_constant < 4.428

# Exact radical identity used in the report.
assert abs(q - math.sqrt(129)/128) < 1e-15
assert abs(mu - (127-math.sqrt(129))/128) < 1e-15
