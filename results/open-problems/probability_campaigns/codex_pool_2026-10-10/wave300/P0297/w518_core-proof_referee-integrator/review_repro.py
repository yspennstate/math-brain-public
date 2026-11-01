"""Independent finite two-route response check; no stochastic simulation."""
import math

def simpson(f, lo, hi, n=20000):
    assert n % 2 == 0
    h = (hi - lo) / n
    return h / 3 * (f(lo) + f(hi) + 4 * sum(f(lo + (2*k+1)*h) for k in range(n//2)) + 2 * sum(f(lo + 2*k*h) for k in range(1, n//2)))

xi = 0.7
phi = lambda z: math.exp(-z*z/4) / math.sqrt(4*math.pi)  # N(0,2)
target = -1/math.sqrt(math.pi)
for beta in (2.0, 10.0, 50.0, 250.0):
    direct = simpson(lambda z: -z*math.tanh(beta*xi*z/2)*phi(z)/2, -12, 12)
    switch = simpson(lambda z: 0.5*(1-math.tanh(beta*xi*z/2)**2)*phi(z), -12, 12)
    corrected = -beta*xi*switch
    print(f"beta={beta:g} direct={direct:.12f} corrected={corrected:.12f} ibp_error={abs(direct-corrected):.3g} limit_error={abs(direct-target):.6g}")
    assert abs(direct-corrected) < 1e-7
assert abs(direct-target) < 2e-5

# Snowflake covariance countermodel: H^d scales by lambda^d under metric scaling.
for p in (1.0, 0.8, 0.5):
    gamma = 1.2
    xi_p = gamma*p/2
    dimension = 2/p
    assert abs(xi_p*dimension-gamma) < 1e-12
    print(f"snowflake p={p:g} dimension={dimension:g} xi={xi_p:g} xi*d={xi_p*dimension:g}")

gamma = math.sqrt(8/3)
d_known = 4.0
xi_known = gamma/d_known
Q_known = 2/gamma + gamma/2
old_identity = 2*Q_known/xi_known
correct_identity = gamma/xi_known
print(f"Brownian anchor: old 2Q/xi={old_identity:.12g}; correct gamma/xi={correct_identity:.12g}; proved d={d_known:g}")
assert abs(old_identity-10) < 1e-12
assert abs(correct_identity-d_known) < 1e-12
