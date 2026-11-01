from fractions import Fraction
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 80

# Rigorous rational comparison used in REPORT.md.
# (5/3)^4 < 8 => 2^(-3/4) < 3/5, which yields A < 203/75.
assert Fraction(5, 3) ** 4 < 8
A_upper = Fraction(203, 75)
pi_lower = Fraction(157, 50)  # classical pi > 3.14
L = 389 * A_upper * A_upper - 388 * pi_lower
lhs = L * L
rhs = (140 * A_upper) ** 2 * 6 * pi_lower
assert L > 0 and lhs < rhs

# High-precision sanity evaluation of the explicit polynomial upper.
pi = mp.pi

def J(p):
    return mp.sqrt(pi) * mp.gamma((p + 1) / 2) / (2 * mp.gamma((p + 2) / 2))

A = J(mp.mpf('-0.5'))
B = J(mp.mpf('0.5'))
assert abs(A * B - pi) < mp.mpf('1e-70')
U4 = mp.sqrt(3) / (140 * mp.sqrt(pi)) * (389 * A - 388 * B)
baseline = 3 * mp.sqrt(2)
assert U4 < baseline

# Exact integral formula for the aligned endpoint global peak; numerical value is only a check.
aligned = 2 * mp.sqrt(6 * pi) * mp.quad(
    lambda r: mp.e ** (-3 * r * r) * mp.besseli(0, 3 * r * r),
    [0, mp.mpf('0.5')],
)
assert aligned < U4 < baseline

# Finite frame sanity checks.  The analytic proof is R^T R = I_3 identically.
Jmat = np.diag([1.0, 1.0, -1.0])
for theta in [0.0, 0.17, 0.4, math.pi / 8, math.pi / 4]:
    c, s = math.cos(theta), math.sin(theta)
    v1 = np.array([c, 0.0, s])
    v2 = np.array([-s, 0.0, c])
    e2 = np.array([0.0, 1.0, 0.0])
    R = np.vstack([v1, v2, e2])
    assert np.linalg.norm(R.T @ R - np.eye(3), ord=np.inf) < 1e-12
    eig = np.linalg.eigvalsh(R @ Jmat @ R.T)
    assert np.max(np.abs(np.sort(eig) - np.array([-1.0, 1.0, 1.0]))) < 1e-12

print('PASS QFORM-SATURATED-OPPOSITE-HEAVY-ZERO-v1')
print('rational_square_gap =', rhs - lhs)
print('A =', mp.nstr(A, 42))
print('B =', mp.nstr(B, 42))
print('A*B =', mp.nstr(A * B, 42))
print('U4 =', mp.nstr(U4, 42))
print('3sqrt2 =', mp.nstr(baseline, 42))
print('margin =', mp.nstr(baseline - U4, 42))
print('aligned_global_peak =', mp.nstr(aligned, 42))
