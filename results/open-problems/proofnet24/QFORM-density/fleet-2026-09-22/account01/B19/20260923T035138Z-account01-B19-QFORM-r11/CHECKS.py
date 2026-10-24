import math
import itertools
import numpy as np
from mpmath import beta, e

# Constants in REPORT.md.
star2 = 1/6 - 1/64
assert abs(star2 - 29/192) < 1e-15
assert 128 * 48**0.25 < 337
hub_sb = 4 * 2**0.25 * (192/29)**0.25
assert hub_sb < 7.631
Delta = (29/384)/8
assert abs(Delta - 29/3072) < 1e-15

def C3(q):
    return (3**(1/6) * float(e)**(2/3) / (4*q**(1/3))
            * float(beta(1/4, 3/(8*q)-1/4))**(2/3))

assert C3(1) * Delta**(-1/6) < 6.490
assert C3(4/3) * Delta**(-1/6) < 12.511

# Algebraic regression for W_i=D_i+O_i and W_i>=||m||^2 when s3(A)>=1.
rng = np.random.default_rng(20260923)
for trial in range(40):
    n = 7
    # Build an exact rank-three symmetric target with |eigenvalues| >= 1.
    Q, _ = np.linalg.qr(rng.normal(size=(n, 3)))
    lam = np.array([1.0 + rng.random(), -(1.0 + rng.random()), 1.0 + rng.random()])
    A = Q @ np.diag(lam) @ Q.T
    i = trial % n
    idx = [j for j in range(n) if j != i]
    m = A[i, idx]
    B = A[np.ix_(idx, idx)]
    W = D = O = 0.0
    for jj, j in enumerate(idx):
        r = B[jj, :]
        W += np.dot(m, m)*np.dot(r, r) - np.dot(m, r)**2
        for aa in range(len(idx)):
            for bb in range(aa+1, len(idx)):
                k, l = idx[aa], idx[bb]
                det = A[i, k]*A[j, l] - A[i, l]*A[j, k]
                if j in (k, l):
                    O += det*det
                else:
                    D += det*det
    assert abs(W-(D+O)) <= 1e-8 * max(1.0, abs(W))
    assert W + 1e-9 >= np.dot(m, m)

# Exhaustive partition regression on small examples: best captured disjoint packet >=D/8.
for trial in range(10):
    n = 7
    X = rng.normal(size=(n,n))
    A = (X+X.T)/2
    i = 0
    res = list(range(1,n))
    terms = []
    D = 0.0
    for j in res:
        cols = [x for x in res if x != j]
        for aa in range(len(cols)):
            for bb in range(aa+1,len(cols)):
                k,l=cols[aa],cols[bb]
                z=(A[i,k]*A[j,l]-A[i,l]*A[j,k])**2
                D += z
                terms.append((j,k,l,z))
    best=0.0
    for bits in itertools.product([0,1], repeat=len(res)):
        J={res[t] for t,b in enumerate(bits) if b==0}
        K={res[t] for t,b in enumerate(bits) if b==1}
        captured=sum(z for j,k,l,z in terms if j in J and k in K and l in K)
        best=max(best,captured)
    assert best + 1e-12 >= D/8

print('star2=', star2)
print('hub_smallball_constant=', hub_sb)
print('Delta2_floor=', Delta)
print('L3_q1=', C3(1)*Delta**(-1/6))
print('L3_q4over3=', C3(4/3)*Delta**(-1/6))
print('QFORM_B19_R11_HEAVY_HUB_COMPOUND_CHECK_PASS')
