import itertools
import math
import numpy as np


def build(m, delta):
    n = 3*m + 1
    up = np.zeros(n); um = np.zeros(n); v = np.zeros(n); h = np.zeros(n)
    up[:m] = 1/math.sqrt(m)
    um[m:2*m] = 1/math.sqrt(m)
    v[2*m:3*m] = 1/math.sqrt(m)
    h[-1] = 1
    A = (np.outer(up, up) - np.outer(um, um)
         + (1-delta)*np.outer(v, v)
         + math.sqrt(delta)*(np.outer(h, v)+np.outer(v, h)))
    return A


def count_large(B, tol=1e-9):
    return int(np.sum(np.abs(np.linalg.eigvalsh(B)) >= 1-tol))


for m, delta in [(3, .5), (10, .1), (32, 2**-12)]:
    A = build(m, delta)
    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-10]
    assert np.allclose(nz, [-1, -delta, 1, 1], atol=1e-9)
    assert count_large(A) == 3
    for i in range(A.shape[0]):
        B = np.delete(np.delete(A, i, axis=0), i, axis=1)
        assert count_large(B) <= 2

    md = float(np.max(np.abs(np.diag(A))))
    m2 = 0.0
    m3 = 0.0
    for I in itertools.combinations(range(A.shape[0]), 2):
        m2 = max(m2, abs(np.linalg.det(A[np.ix_(I,I)])))
    for I in itertools.combinations(range(A.shape[0]), 3):
        m3 = max(m3, abs(np.linalg.det(A[np.ix_(I,I)])))
    assert md <= 1/m + 1e-12
    assert m2 <= max(1/m**2, delta/m) + 1e-12
    assert m3 <= max((1-delta)/m**3, delta/m**2) + 1e-12

    # Base/collar identity for H={hub}.
    D = A[:-1,:-1]
    s = np.linalg.svd(D, compute_uv=False)
    assert abs(s[2] - (1-delta)) < 1e-9
    collar = np.linalg.norm(A[-1,:-1])
    assert abs(collar**2 - delta) < 1e-9
    assert abs((1-s[2]) - collar**2) < 1e-9

print('F_bound_delta_half=', 12*2**(1/3))
print('surplus_bound_alpha_2^-20=', 1+3*math.sqrt(2**-20 + 2**-40))
print('QFORM_B19_PRINCIPALMINIMAL_THRESHOLD_TRANSFER_CHECK_PASS')
