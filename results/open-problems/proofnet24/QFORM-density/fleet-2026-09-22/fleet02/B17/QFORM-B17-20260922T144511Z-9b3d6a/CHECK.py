import cmath
import math


def sinc(x):
    return 1.0 if x == 0.0 else math.sin(x) / x


alpha = 1.0
b = 1.0
C = 3.0 * math.sqrt(2.0)

# Exact limiting zero-saddle series; omitted weighted contribution is at most
# the omitted Poisson probability because exp(-3 b^2 k^2) <= 1.
K = 12
p = math.exp(-alpha)
poisson_partial = 0.0
saddle_factor = 0.0
for k in range(K + 1):
    if k > 0:
        p *= alpha / k
    poisson_partial += p
    saddle_factor += p * math.exp(-3.0 * b * b * k * k)
poisson_tail_bound = 1.0 - poisson_partial

# One rare interval: exact full-row Lindeberg contribution.
m = 100
lindeberg = alpha * b * b + alpha**3 / (12.0 * m**3)

# Numerical sanity check of the exact one-bank characteristic function.
def psi_m(t, m, alpha, b):
    w0 = 1.0 - alpha / m
    return (
        w0 * sinc(t * w0 / (2.0 * math.sqrt(m)))
        + (alpha / m)
        * cmath.exp(1j * t * b)
        * sinc(t * alpha / (2.0 * m * math.sqrt(m)))
    )


t = 1.0
m_cf = 10000
cf_finite = psi_m(t, m_cf, alpha, b) ** m_cf
cf_limit = cmath.exp(-t * t / 24.0 + alpha * (cmath.exp(1j * t * b) - 1.0))
cf_error = abs(cf_finite - cf_limit)

print(f"C_3sqrt2 = {C:.16f}")
print(f"alpha=b=1 zero-saddle factor (K={K}) = {saddle_factor:.16f}")
print(f"omitted contribution <= Poisson tail = {poisson_tail_bound:.3e}")
print(f"limiting p_Q(0), truncated = {C * saddle_factor:.16f}")
print(f"finite-m Lindeberg contribution at m={m} = {lindeberg:.16f}")
print(f"Lindeberg limit alpha*b^2 = {alpha*b*b:.16f}")
print(f"cf finite m={m_cf} = {cf_finite}")
print(f"cf limit = {cf_limit}")
print(f"cf error = {cf_error:.6e}")

assert 0.0 < saddle_factor < 1.0
assert poisson_tail_bound < 1.0e-9
assert C * saddle_factor + C * poisson_tail_bound < C
assert abs(lindeberg - alpha * b * b) < 1.0e-6
assert cf_error < 1.0e-4
print("PASS")
