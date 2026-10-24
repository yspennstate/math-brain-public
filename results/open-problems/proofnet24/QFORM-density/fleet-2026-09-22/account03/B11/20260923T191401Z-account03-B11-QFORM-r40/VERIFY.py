import math

# Constants from the punctured-collar top-two lemma.
g0 = 17/288
beta0 = (34/111)*g0
kappa_star = beta0*g0
assert abs(kappa_star - 0.0010672564926037147) < 1e-15

# Exact mixed L1_w(L2_v) formula for the fragmented Sidon construction.
def mixed_norm(N: int) -> float:
    ell = 1/N
    J = (4/3)*2**(-1/4)*ell**1.5
    return J*(N + math.sqrt(2)*N*(N-1)/2)

lead = (4/3)*2**(-3/4)
assert abs(lead - 0.7928047433351473) < 1e-15

vals = [(N, mixed_norm(N), mixed_norm(N)/math.sqrt(N)) for N in (2,4,10,100,1000)]
for N, val, ratio in vals:
    print(N, f"{val:.12f}", f"{ratio:.12f}")

# Divergence check and asymptotic ratio.
assert mixed_norm(1000) > mixed_norm(100) > mixed_norm(10)
assert abs(mixed_norm(1000)/math.sqrt(1000) - lead) < 5e-4

# Designated partner gate.
partner_bound = 2048*math.sqrt(2/7)
assert partner_bound < 1094.703
print("kappa_star", f"{kappa_star:.15f}")
print("lead", f"{lead:.15f}")
print("partner_bound", f"{partner_bound:.12f}")
print("QFORM_B11_R40_MIXED_SLICE_CHECK_PASS")
