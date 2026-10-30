import math
import numpy as np


def C_r(r):
    alpha = (r - 1.0) / r
    theta = r / (2.0 * r - 1.0)
    return ((1.0 + alpha) / (math.pi * alpha)) * (
        (alpha * math.pi / 2.0)
        * (2.0 / (r - 1.0)) ** (1.0 / r)
        * (2.0 * math.pi) ** alpha
        * 2.0 ** (alpha + 0.5)
    ) ** theta


def scale_exponent(q):
    r = q / (q - 1.0)
    return -r / (2.0 * r - 1.0) + q * (r - 1.0) / (2.0 * r - 1.0)


assert abs(C_r(2.0) - 3.0) < 1e-12
for q in (2.0, 3.0, 4.0):
    assert abs(scale_exponent(q)) < 1e-12

A = np.array([
    [0,0,1,0,1,0],
    [0,0,0,1,0,1],
    [1,0,1,0,0,0],
    [0,1,0,0,0,0],
    [1,0,0,0,0,1],
    [0,1,0,0,1,0],
], dtype=float)
vals = np.linalg.eigvalsh(A)
assert np.sum(np.abs(vals) >= 1.0 - 1e-12) == 4
coeff = np.poly(A)
expected = np.array([1,-1,-5,4,6,-3,-1], dtype=float)
assert np.max(np.abs(coeff - expected)) < 1e-10

print('C_2 =', C_r(2.0))
for q in (2.0, 3.0, 4.0):
    r = q / (q - 1.0)
    print(f'q={q:g}, r={r:.12g}, exponent={scale_exponent(q):.3e}, C_r={C_r(r):.15f}')
print('stress eigenvalues =', ', '.join(f'{x:.10f}' for x in vals))
print('number |lambda|>=1 =', int(np.sum(np.abs(vals) >= 1.0 - 1e-12)))
print('max characteristic-polynomial coefficient error =', float(np.max(np.abs(coeff-expected))))
print('STATUS=PASS')
