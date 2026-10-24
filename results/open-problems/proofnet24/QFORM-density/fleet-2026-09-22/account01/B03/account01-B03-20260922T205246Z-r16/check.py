import math
import random
import numpy as np

C = 4 * 2**(7/8)
assert abs(C - 7.33603234563737) < 1e-12

# Algebraic constant collapse in Section 6:
# min_R 6 G R^(1/3)+1/(2R) = 4 sqrt(2) G^(3/4).
for _ in range(1000):
    G = 10**random.uniform(-6, 6)
    R = (1/(4*G))**(3/4)
    lhs = 6*G*R**(1/3) + 1/(2*R)
    rhs = 4*math.sqrt(2)*G**(3/4)
    assert abs(lhs-rhs) <= 1e-10*max(1, abs(rhs))

# Spectral scaling check for random zero-diagonal symmetric triples.
for _ in range(10000):
    vals = [10**random.uniform(-4,4)*random.choice((-1,1)) for _ in range(3)]
    b,c,d = vals
    B = np.array([[0.0,b,c],[b,0.0,d],[c,d,0.0]])
    sv = np.linalg.svd(B, compute_uv=False)
    s = sv.min()
    M = max(abs(b),abs(c),abs(d))
    assert abs(np.linalg.det(B) - 2*b*c*d) <= 1e-8*max(1,abs(2*b*c*d))
    assert abs(b*c*d) + 1e-12*max(1,abs(b*c*d)) >= s**3/2
    assert M + 1e-12*max(1,M) >= s/math.sqrt(2)

print('QFORM_B03_ZERO_DIAGONAL_TRIPLE_PASS')
