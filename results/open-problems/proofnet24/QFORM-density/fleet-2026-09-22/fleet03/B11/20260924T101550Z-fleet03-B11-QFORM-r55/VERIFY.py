import math, random
import numpy as np

SEED = 20260924
N = 50000
rng = random.Random(SEED)

c1 = 12 * (5/8)**(1/3)
c2 = (64 * 26 * 2 * math.sqrt(2))**(1/3) * 5**(1/6)
cdep = 4 * 22**0.75
max_norm_err = 0.0
max_disc_err = 0.0
max_det_err = 0.0
min_gate1 = float('inf')
min_gate2 = float('inf')
checks = 0

for _ in range(N):
    a = rng.uniform(-7, 7)
    b = rng.uniform(-7, 7)
    t = rng.uniform(-7, 7)
    D = t*t - a*b
    if D <= 1e-8:
        continue
    s = math.sqrt(D)
    aa, bb, tt = a/s, b/s, t/s
    max_norm_err = max(max_norm_err, abs(tt*tt-aa*bb-1))

    if abs(aa*bb) <= tt*tt/4 + 1e-14:
        min_gate1 = min(min_gate1, abs(tt))
        x = rng.uniform(-3, 3)
        if abs(bb) > 1e-12:
            lim = abs(tt*x)/(2*abs(bb))
            y = rng.uniform(-lim, lim)
        else:
            y = rng.uniform(-3, 3)
        assert 2*abs(tt*x+bb*y) + 1e-10 >= abs(tt*x)

        y = rng.uniform(-3, 3)
        if abs(bb) > 1e-12 and abs(y) > 1e-12:
            xmax = 2*abs(bb*y)/max(abs(tt), 1e-12)
            x = rng.uniform(-0.99*xmax, 0.99*xmax)
            assert 2*abs(aa*x+tt*y) + 1e-9 >= abs(tt*y)
    else:
        min_gate2 = min(min_gate2, max(abs(aa), abs(bb)))
        x = rng.uniform(-4, 4)
        y = rng.uniform(-4, 4)
        z = aa*x*x + 2*tt*x*y + bb*y*y
        disc = (2*tt*x)**2 - 4*bb*(aa*x*x-z)
        max_disc_err = max(max_disc_err, abs(disc - 4*(x*x+bb*z)))

    lam = rng.choice([-1,1]) * 10**rng.uniform(-2,2)
    r = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    C = np.array([[aa,tt],[tt,bb]])
    B = np.block([[C, r[:,None]], [r[None,:], np.array([[lam]])]])
    S = C - np.outer(r,r)/lam
    max_det_err = max(max_det_err, abs(np.linalg.det(B)-lam*np.linalg.det(S)))
    checks += 1

assert c1 < 11
assert c2 < 22
assert min_gate1 >= 2/math.sqrt(5) - 1e-8
assert min_gate2 >= 1/math.sqrt(5) - 1e-8

print(f"checks={checks}")
print(f"case1_constant={c1:.15f}")
print(f"case2_constant={c2:.15f}")
print(f"dependent_square_coefficient={cdep:.15f}")
print(f"max_normalization_error={max_norm_err:.3e}")
print(f"max_discriminant_identity_error={max_disc_err:.3e}")
print(f"max_schur_det_error={max_det_err:.3e}")
print(f"min_case1_abs_t={min_gate1:.15f}; threshold={2/math.sqrt(5):.15f}")
print(f"min_case2_max_diag={min_gate2:.15f}; threshold={1/math.sqrt(5):.15f}")
print("QFORM_B11_R55_INDEFINITE_PAIR_L3_CHECK_PASS")
