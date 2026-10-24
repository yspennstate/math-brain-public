import math
import random
import numpy as np

C_E3 = 8.4530212255281768747049
assert 64*C_E3 < 541
assert (2.0**-16)**2/16 == 2.0**-36

# Random numerical regression for the r=1 signature peel.
# If p eigenvalues of A are >=1 and q are <=-1, then D=diag(A_LL,A_JJ)
# must have p-1 eigenvalues >=1-s2(W) and q-1 <=-(1-s2(W)).
def check_once(nL, nJ):
    X = np.random.randn(nL+nJ, nL+nJ)
    A = (X + X.T)/2
    B = A[:nL,:nL]
    C = A[nL:,nL:]
    W = A[:nL,nL:]
    sv = np.linalg.svd(W, compute_uv=False)
    s2 = sv[1] if len(sv) > 1 else 0.0
    ev = np.linalg.eigvalsh(A)[::-1]
    p = int(np.sum(ev >= 1.0-1e-12))
    q = int(np.sum(ev <= -1.0+1e-12))
    D = np.block([[B, np.zeros((nL,nJ))],
                  [np.zeros((nJ,nL)), C]])
    de = np.linalg.eigvalsh(D)[::-1]
    if p >= 2:
        assert de[p-2] >= 1.0-s2-1e-9
    if q >= 2:
        assert de[-(q-1)] <= -(1.0-s2)+1e-9

random.seed(20260924)
np.random.seed(20260924)
for _ in range(1000):
    check_once(random.randint(2,6), random.randint(2,6))

# Sharp examples in the report.
A_cross = np.block([[np.zeros((2,2)), np.eye(2)],
                    [np.eye(2), np.zeros((2,2))]])
assert np.allclose(np.linalg.eigvalsh(A_cross), [-1,-1,1,1])

s=1.7
A_side=np.zeros((4,4))
A_side[0,0]=1
A_side[1,1]=1
A_side[2,3]=A_side[3,2]=s
assert np.allclose(np.linalg.eigvalsh(A_side), [-s,1,1,s])

print('E3_tail_threshold=', 2.0**-36)
print('E3_density_bound=', 64*C_E3)
print('random_signature_peel_checks=1000 PASS')
print('sharp_examples=PASS')
