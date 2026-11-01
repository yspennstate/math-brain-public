from fractions import Fraction
from math import sqrt, e

# Exact near-null star arithmetic.
assert Fraction(7,9) - Fraction(1,16) == Fraction(103,144)
assert sqrt(103)/12 > 0.8457

# Exact diffuse partition constants.
assert Fraction(1,4) / 10 == Fraction(1,40)
assert Fraction(1,40) / 16 == Fraction(1,640)
assert e*sqrt(640) < 68.768

# Full-matrix pair constant used in the paid local-atom branch.
Cpair = 3*(400**(1/3))*(((Fraction(3,16)**2)*Fraction(1,4))**(-Fraction(1,6)))
assert float(Cpair) < 49

# Regression of the Pluecker degree and partition-expectation identities
# on deterministic Parseval frames. This is diagnostic only.
import random
import numpy as np

rng = random.Random(119)
for m in (4, 5, 8, 13):
    G = np.array([[rng.uniform(-1,1) for _ in range(2)] for __ in range(m)], dtype=float)
    # Whiten to a Parseval frame.
    S = G.T @ G
    vals, vecs = np.linalg.eigh(S)
    V = G @ (vecs @ np.diag(vals**-0.5) @ vecs.T)
    gram = V.T @ V
    assert np.max(np.abs(gram-np.eye(2))) < 1e-10
    h = np.sum(V*V, axis=1)
    W = np.zeros((m,m))
    for i in range(m):
        for j in range(i+1,m):
            W[i,j] = W[j,i] = np.linalg.det(np.stack([V[i],V[j]]))**2
    assert abs(np.sum(np.triu(W,1))-1) < 1e-10
    assert np.max(np.abs(np.sum(W,axis=1)-h)) < 1e-10
    D = 0.0
    for i in range(m):
        for j in range(i+1,m):
            for k in range(m):
                for l in range(k+1,m):
                    if len({i,j,k,l}) == 4:
                        D += W[i,j]*W[k,l]
    D2 = 1 - np.sum(h*h) + np.sum(np.triu(W,1)**2)
    assert abs(D-D2) < 1e-9

print('QFORM_B19_R19_TWO_BANK_STAR_CHECK_PASS')
print('pair_constant=', float(Cpair))
print('two_bank_density_cap=', e*sqrt(640))
