import math

# Exact formulas proved in REPORT.md; numerically evaluate them.
g43 = math.gamma(4.0/3.0)
for m in [2, 4, 10, 32, 100]:
    log_one_block = -(1.0/3.0)*math.log(m) + math.lgamma(m+1.0) + math.lgamma(4.0/3.0) - math.lgamma(m+1.0/3.0)
    one_block = math.exp(log_one_block)
    triple = one_block**3
    gautschi_lower = g43**3 * m
    assert triple > gautschi_lower
    print(m, f"moment={triple:.12f}", f"lower={gautschi_lower:.12f}")

partner_constant = 4.0*math.sqrt(math.pi)
ridge_constant = 288.0*math.sqrt(3.0*math.e)/13.0
assert ridge_constant < 64.0
print(f"partner_4sqrtpi={partner_constant:.15f}")
print(f"ridge_constant={ridge_constant:.15f}")
print("STATUS=PASS")
