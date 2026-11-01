#!/usr/bin/env python3
"""
I0067 exact/symbolic self-check for the B2 high-frequency sideband test.

This does NOT certify the source endpoint theorem. It verifies the explicit
first stochastic Picard variance formula used to test a possible variable-
transport endpoint obstruction.

Model on T^3:
  du = nu Delta u dt + P[(b.grad)u] dW,
  b(x) = sigma cos(x_2) e_1,
  u0_N(x) = A e_3 exp(i N x_1).

At first stochastic Picard order, b.grad sends the input to frequencies
(N,+/-1,0), and P leaves the e_3 polarization unchanged.
"""
import sympy as sp

N, nu, sigma, A, s, t = sp.symbols(
    "N nu sigma A s t", positive=True
)

# Each cosine sideband has noise amplitude sigma*A*N/2.
amp2 = sigma**2 * A**2 * N**2 / 4

# Heat damping of output frequency |(N,+/-1,0)|^2=N^2+1
after = sp.exp(-2*nu*(N**2+1)*(t-s))
before = sp.exp(-2*nu*N**2*s)
integrand = after * before
variance = sp.simplify(amp2 * sp.integrate(integrand, (s, 0, t)))
expected = sp.simplify(
    sigma**2*A**2*N**2/(8*nu)
    * sp.exp(-2*nu*(N**2+1)*t)
    * (sp.exp(2*nu*t)-1)
)
assert sp.simplify(variance - expected) == 0

# Critical parabolic time t=N^{-2}; with unit input amplitude.
Vcrit = sp.simplify(expected.subs({t: 1/N**2, A: 1}))
critical_limit = sp.simplify(sp.limit(Vcrit, N, sp.oo))
assert critical_limit == sigma**2*sp.exp(-2*nu)/4

# With order-minus-one normalization A=N, divide output variance by
# output frequency squared N^2+1. This is the squared Fourier-scale
# proxy for a -1 homogeneous norm. It remains finite and nonzero.
Vnorm = sp.simplify(
    expected.subs({t: 1/N**2, A: N}) / (N**2+1)
)
norm_limit = sp.simplify(sp.limit(Vnorm, N, sp.oo))
assert norm_limit == sigma**2*sp.exp(-2*nu)/4

print("status=PASS")
print("sideband_variance=", expected)
print("critical_time_unit_amplitude_limit=", critical_limit)
print("critical_minus_one_normalized_limit=", norm_limit)
print("interpretation=first stochastic Picard sideband is critical, not supercritical")
print("source_endpoint_certified=False")
