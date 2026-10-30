import math
import itertools
import numpy as np

def stress_matrix(m, eps):
    assert m % 2 == 0 and m >= 4
    n = m + 3
    A = np.zeros((n, n), dtype=float)
    h, y1, y2 = 0, 1, 2
    Z0 = 3
    A[h,h] = 1.0
    A[h,y1] = A[y1,h] = 1.0
    A[y1,y1] = 1.0 - eps
    c = 2.0 * math.sqrt(2.0/m)
    for j in range(m//2):
        z = Z0+j
        A[y1,z] = A[z,y1] = c
    for j in range(m//2, m):
        z = Z0+j
        A[y2,z] = A[z,y2] = c
    return A

def schur_after_h(A):
    a = A[0,0]
    v = A[1:,0]
    return A[1:,1:] - np.outer(v,v)/a

generic_r2_constant = 8.0
one_side_literal_r2_constant = 8.0 * 2.0**(-0.25)
assert abs(one_side_literal_r2_constant - 2.0**(11/4)) < 1e-14

print("QFORM-SCALARPIVOT-GROUPED-RANK2-HALFRIESZ checker")
print("generic r=2 half-Riesz coefficient:", generic_r2_constant)
print("one-side-literal r=2 coefficient:", one_side_literal_r2_constant)

for m in (4, 16, 64, 256):
    for eps in (1.0, 0.1, 1e-3, 1e-8):
        A = stress_matrix(m, eps)
        pair = A[np.ix_([0,1],[0,1])]
        assert abs(np.linalg.det(pair) + eps) < 2e-12

        S = schur_after_h(A)
        # Remaining coordinates are y1,y2,z_1,...,z_m.
        C = S[np.ix_([0,1], list(range(2,m+2)))]
        sv = np.linalg.svd(C, compute_uv=False)
        assert len(sv) == 2
        Delta = float(sv[0]*sv[1])
        assert abs(Delta - 4.0) < 2e-12

        eig = np.linalg.eigvalsh(A)
        assert int(np.sum(np.abs(eig) >= 1.0-1e-10)) >= 3

        minors = [
            abs(np.linalg.det(C[:,[i,j]]))
            for i,j in itertools.combinations(range(m),2)
        ]
        max_minor = max(minors)
        assert abs(max_minor - 8.0/m) < 2e-12

    grouped_bound = one_side_literal_r2_constant * 4.0**(-0.25)
    local_bound = (8.0/math.sqrt(2.0)) * (8.0/m)**(-0.25)
    print(
        f"m={m:3d}: Delta2=4, max physical 2x2 det={8/m:.12g}, "
        f"grouped density bound={grouped_bound:.12g}, "
        f"single-physical-pair bound={local_bound:.12g}"
    )

# Active five-dimensional compression used to display representative spectra.
def active(eps):
    return np.array([
        [1.,1.,0.,0.,0.],
        [1.,1.-eps,0.,2.,0.],
        [0.,0.,0.,0.,2.],
        [0.,2.,0.,0.,0.],
        [0.,0.,2.,0.,0.]
    ])
for eps in (1.0, 0.1, 1e-3, 1e-8):
    vals = np.linalg.eigvalsh(active(eps))
    assert np.sum(np.abs(vals)>=1-1e-12) >= 3
    print("eps=", eps, "active spectrum=", np.array2string(vals, precision=10))

# Designated fleet04/B09 application.
K = np.diag([5.0,3.0,1.0])
Astar = np.block([[np.zeros((3,3)),K],[K,np.zeros((3,3))]])
spec = np.linalg.eigvalsh(Astar)
assert np.allclose(spec, [-5.,-3.,-1.,1.,3.,5.])
partner_bound = 3.0 * 15.0**(-1.0/3.0)
print("partner spectrum:", spec)
print("partner density bound 3*15^(-1/3):", partner_bound)

print("ALL ASSERTIONS PASSED")
