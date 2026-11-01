import math

# Constants inherited from the proved r38 near-coloop exact-graph geometry.
beta0 = (17.0 / 288.0) * (34.0 / 111.0)
kappa0 = (34.0 / 111.0) * (17.0 / 288.0) ** 1.5

# Series in (3.13).  For j >= N, concavity gives the tangent-line bound
# sqrt(A+B*j) <= sqrt(A+B*N) + B(j-N)/(2 sqrt(A+B*N)).
A = 4.0 + 2.0 * math.sqrt(2.0) * math.pi
B = 4.0 * math.sqrt(2.0) * math.pi * math.log(2.0)
r = 2.0 ** (-0.5)
N = 40
partial = sum((r ** j) * math.sqrt(A + B * j) for j in range(N))
fN = math.sqrt(A + B * N)
slope = B / (2.0 * fN)
tail = (r ** N) * (fN / (1.0 - r) + slope * r / (1.0 - r) ** 2)
S_upper = partial + tail

exact_null_constant = (
    math.sqrt(2.0) / (math.pi * beta0)
    + math.sqrt(2.0) / math.sqrt(kappa0) * S_upper
)
partner_constant = 2048.0 * math.sqrt(2.0 / 7.0)

print(f"beta0={beta0:.15f}")
print(f"kappa0={kappa0:.15f}")
print(f"S_upper_N40={S_upper:.15f}")
print(f"exact_null_constant={exact_null_constant:.12f}")
print(f"partner_constant={partner_constant:.12f}")

assert beta0 > 0.01808
assert kappa0 > 0.0043927
assert S_upper < 20.759
assert exact_null_constant < 468.0
assert partner_constant < 1094.703

print("QFORM_B11_R39_INTERNAL_BILINEAR_DYADIC_CHECK_PASS")
