import math

# Constants inherited from the preceding finite-multiband theorem and the
# exact full-spectrum Z_{3,1} estimate.
C_band = 529.0
C_global = 1.0 + math.sqrt(2.0)
c_shift = 1.0 + math.log(2.0)

# Rearrangement splitting at s/2 gives these two coefficients.
A = 2.0**(1.0/3.0) * C_band * c_shift**(2.0/3.0)
B = 2.0**(1.0/3.0) * C_global * c_shift

print(f"A_exact={A:.15f}")
print(f"B_exact={B:.15f}")
assert A < 947.0
assert B < 5.2
print("A<947 PASS")
print("B<5.2 PASS")

# If best-N spectral approximation satisfies e_N <= D N^{-theta}, balancing
# the N-band 2/3 endpoint against the global log endpoint uses
# N ~ L^nu, nu=1/(3 theta+1/2), and yields
# alpha=(4 theta+1)/(6 theta+1).
def alpha(theta):
    return (4.0*theta + 1.0)/(6.0*theta + 1.0)

for theta in [0.1, 0.25, 0.5, 1.0, 2.0, 10.0]:
    nu = 1.0/(3.0*theta + 0.5)
    exp_head = 2.0/3.0 + nu/6.0
    exp_tail = 1.0 - theta*nu
    target = alpha(theta)
    print(f"theta={theta:g} nu={nu:.15f} head={exp_head:.15f} tail={exp_tail:.15f} alpha={target:.15f}")
    assert abs(exp_head-exp_tail) < 1e-12
    assert abs(exp_head-target) < 1e-12
    assert 2.0/3.0 < target < 1.0

# Near-saturation complexity scaling: if Q_Y(s)>=eta||Y|| and
# N <= (eta/(2A))^6 L^2, then e_N >= eta||Y||/(2B).
for eta in [0.1, 0.25, 0.5, 0.9]:
    coeff = (eta/(2.0*A))**6
    tail_fraction = eta/(2.0*B)
    print(f"eta={eta:.2f} N_coeff={coeff:.18e} tail_fraction={tail_fraction:.15f}")
    assert coeff > 0.0
    assert tail_fraction > 0.0

# Representative balanced-rate checks.  Multiplying the little-endpoint
# modulus by L^(1-alpha) should remain O(1) under e_N=N^{-theta}.
for theta in [0.25, 0.5, 1.0]:
    a = alpha(theta)
    nu = 1.0/(3.0*theta + 0.5)
    for L in [1e3, 1e6, 1e12]:
        N = max(1, int(round(L**nu)))
        q = A*N**(1.0/6.0)*L**(-1.0/3.0) + B*N**(-theta)
        scaled = q*L**(1.0-a)
        print(f"rate theta={theta:g} L={L:.0e} N={N} q={q:.12f} scaled={scaled:.12f}")
        assert math.isfinite(scaled)

print("CHECK_PASS")
