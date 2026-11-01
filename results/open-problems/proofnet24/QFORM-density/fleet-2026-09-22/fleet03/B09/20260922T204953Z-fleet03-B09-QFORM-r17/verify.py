import math
import numpy as np

C_an = 1.5 * 10.0 ** (2.0 / 3.0)
C_peer = C_an * (math.e * math.sqrt(2.0)) ** (2.0 / 3.0)
C_lpp2 = C_an * (2.0 * math.sqrt(2.0)) ** (2.0 / 3.0)

assert abs(C_an - 6.962383250419168) < 1e-12
assert C_peer < 17.086
assert C_lpp2 < 13.925

# Verify the optimization min_{r>0} A/r + B sqrt(r).
for A, B in [(1.0, 1.0), (2.3, 0.7), (0.2, 4.0)]:
    r = (2.0 * A / B) ** (2.0 / 3.0)
    lhs = A / r + B * math.sqrt(r)
    rhs = 3.0 * 2.0 ** (-2.0 / 3.0) * A ** (1.0 / 3.0) * B ** (2.0 / 3.0)
    assert abs(lhs - rhs) < 1e-12

# Target-valid diffuse family: A = uv^T + vu^T + ww^T,
# with u on bank I and orthonormal v,w on bank J.
for m in [2, 4, 8, 20, 50]:
    assert m % 2 == 0
    u = np.ones(m) / math.sqrt(m)
    v = np.ones(m) / math.sqrt(m)
    w = np.concatenate((np.ones(m // 2), -np.ones(m // 2))) / math.sqrt(m)
    assert abs(float(v @ w)) < 1e-12

    A = np.zeros((2 * m, 2 * m))
    A[:m, m:] = np.outer(u, v)
    A[m:, :m] = np.outer(v, u)
    A[m:, m:] = np.outer(w, w)

    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-9]
    assert len(nz) == 3
    assert np.max(np.abs(np.sort(nz) - np.array([-1.0, 1.0, 1.0]))) < 1e-10
    assert np.max(np.abs(A)) <= 1.0 / m + 1e-12

print(f"analytic_constant={C_an:.15f}")
print(f"peer_BL_constant={C_peer:.15f}")
print(f"optional_LPP2_constant={C_lpp2:.15f}")
print("optimization_identity=PASS")
print("diffuse_family_spectrum_and_entry_scale=PASS")
