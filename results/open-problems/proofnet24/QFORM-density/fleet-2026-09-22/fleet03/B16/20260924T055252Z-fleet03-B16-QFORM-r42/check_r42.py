import math

# Exact collar arithmetic from r41.
rho2 = 63/64 - 1/4032
assert abs(rho2 - 62/63) < 1e-15

# New hard-collar Fourier constant.
Cstar = math.sqrt(math.pi) * (63/31)**0.25
assert 2.11626 < Cstar < 2.11627

# Designated-partner strict-target compression eigenvalues.
for eta in [0.0, 0.25, 1.0, 4.0, 16.0, -0.25, -1.0, -16.0]:
    d = math.sqrt(9 + 4*eta*eta)
    eig = [2.0, (1+d)/2, (1-d)/2]
    assert sum(x >= 1 for x in eig) >= 2
    assert sum(x <= -1 for x in eig) >= 1

# Elementary numerical sanity check of the exact Plancherel identity in the
# special case H~Unif[-1/2,1/2], a=0. Then F_t(z)=sin(t z)/(t z) and
# integral_R |F_t(z)|^2 dz = pi/|t|. Truncate only for a regression check;
# the proof in REPORT.md is exact and does not use this computation.
t = 3.0
L = 500.0
N = 400_000
step = 2*L/N
acc = 0.0
for k in range(N+1):
    z = -L + k*step
    y = 1.0 if z == 0.0 else math.sin(t*z)/(t*z)
    weight = 0.5 if k in (0, N) else 1.0
    acc += weight*y*y
numerical = acc*step
exact = math.pi/abs(t)
assert abs(numerical-exact) < 3e-4

print(f"Cstar={Cstar:.15f}")
print(f"rho2_endpoint={rho2:.15f}")
print(f"sinc2_numerical={numerical:.15f}")
print(f"sinc2_exact={exact:.15f}")
print(f"sinc2_abs_error={abs(numerical-exact):.15g}")
print("STATUS=PASS")
