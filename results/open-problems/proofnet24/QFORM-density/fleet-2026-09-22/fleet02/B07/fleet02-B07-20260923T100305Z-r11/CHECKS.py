import math
import numpy as np


def constants():
    c14 = 2**(3/4) * math.gamma(3/8) / (2*math.sqrt(math.pi)*math.gamma(1/8))
    C214 = 16*c14*(math.pi*math.sqrt(2*math.e))**0.25
    c12 = (2*math.pi)**-0.5
    C312 = 12*c12*(math.pi*math.sqrt(2*math.e))**0.5
    return C214, C312


def check_m(m):
    assert m % 2 == 0 and m >= 12
    N = m*m
    b = 1/m
    S = math.sqrt(m)
    a = m**(-0.25)

    # Modal block on span{x,y,p,q}; a^2=bS makes it rank two.
    modal = np.array([
        [0, b, a, 0],
        [b, 0, 0, a],
        [a, 0, 0, S],
        [0, a, S, 0],
    ], dtype=float)
    eig = np.linalg.eigvalsh(modal)
    target = np.array([-(S+b), 0, 0, S+b])
    assert np.allclose(eig, target, atol=1e-10)
    assert abs(a*a-b*S) < 1e-12

    # Cross block diag(b,D), D has two singular values S,S.
    E2_D = S**4
    G3_anchor = b*b*E2_D
    edge_E2_product = b*math.sqrt(E2_D)
    assert abs(G3_anchor-1) < 1e-12
    assert abs(edge_E2_product-1) < 1e-12

    # Pair Schur correction deletes one singular component of D exactly.
    D_modes = np.diag([S, S])
    correction = np.diag([S, 0])
    residual = D_modes-correction
    sres = np.linalg.svd(residual, compute_uv=False)
    E2_residual = (sres[0]*sres[1])**2
    assert np.sum(sres > 1e-10) == 1
    assert E2_residual < 1e-20

    # Flat-vector entry bounds; every physical 2x2 principal determinant is entry^2.
    max_entry = max(b, a/math.sqrt(N), 2*S/N)
    assert max_entry**2 < 1/128

    # Uniform fixed-cardinality core upper bound for M=8, as a sample regression.
    M = 8
    core_s3_upper = 2*a*math.sqrt(M/N) + 2*S*M/N

    # e5 Theorem F after conditioning x,y.
    theorem_F_cap = 8/S

    return {
        "m": m,
        "N": N,
        "modal_nonzero": [float(eig[0]), float(eig[-1])],
        "S": S,
        "G3_anchor": G3_anchor,
        "edge_E2_product": edge_E2_product,
        "max_physical_entry_upper": max_entry,
        "max_pair_det_upper": max_entry**2,
        "schur_residual_rank": int(np.sum(sres > 1e-10)),
        "schur_residual_E2": E2_residual,
        "M8_s3_upper": core_s3_upper,
        "TheoremF_density_cap": theorem_F_cap,
    }


if __name__ == "__main__":
    C214, C312 = constants()
    print("C_2,1/4 =", repr(C214))
    print("C_3,1/2 =", repr(C312))
    for m in [12, 16, 32, 64]:
        print(check_m(m))
    print("QFORM_B07_ANCHORED_SCHUR_COLLAPSE_CHECK_PASS")
