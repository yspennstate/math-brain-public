import math
import numpy as np


def build(m, eps):
    assert m >= 2 and m % 2 == 0
    assert 0 < eps < 1/3 and eps * eps < 1/9
    c = 7/9
    M = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    a = [
        np.array([1.0, 0.0]) / math.sqrt(3),
        np.array([-0.5, math.sqrt(3)/2]) / math.sqrt(3),
        np.array([-0.5, -math.sqrt(3)/2]) / math.sqrt(3),
    ]
    pnorm2 = 2/9 - 2*eps*eps
    p = np.array([math.sqrt(pnorm2), 0.0])
    signs = np.array([1.0]*(m//2) + [-1.0]*(m//2))

    rows = [np.array([math.sqrt(c), 0.0, 0.0])]
    banks = []
    for generated_sign in (1.0, -1.0):
        bank = []
        for ar in a:
            for s in signs:
                v = ar / math.sqrt(m)
                eta = eps*s / math.sqrt(3*m)
                alpha = generated_sign*np.dot(v, p) + eta
                rows.append(np.r_[alpha, v])
                bank.append((alpha, v, eta))
        banks.append(bank)

    U = np.vstack(rows)
    A = U @ M @ U.T

    bank_stats = []
    for bank in banks:
        V = np.array([z[1] for z in bank])
        eta = np.array([z[2] for z in bank])
        S = V.T @ V
        tau = float(eta @ eta)
        leverage = np.einsum('ij,jk,ik->i', V, np.linalg.inv(S), V) + eta**2/tau
        bank_stats.append((tau, S, float(np.max(leverage))))

    eig = np.linalg.eigvalsh(A)
    nonzero = eig[np.abs(eig) > 1e-8]
    pivots = np.diag(A)[1:]
    heavy_edges = A[0, 1:]
    max_heavy_triple = 0.0
    for j in range(1, A.shape[0]):
        for k in range(j+1, A.shape[0]):
            block = A[np.ix_([0, j, k], [0, j, k])]
            max_heavy_triple = max(max_heavy_triple, abs(np.linalg.det(block)))

    return {
        'parseval_error': float(np.linalg.norm(U.T @ U - np.eye(3))),
        'nonzero_spectrum': nonzero,
        'bank_stats': bank_stats,
        'max_abs_pivot': float(np.max(np.abs(pivots))),
        'max_abs_heavy_edge': float(np.max(np.abs(heavy_edges))),
        'max_abs_heavy_triple_det': max_heavy_triple,
    }


C = 6 * 2**(1/3) * (368640/7)**(1/6)
print(f'GROUPED_FRESNEL_CONSTANT={C:.15f}')
assert C < 46.282

for m in (2, 10, 50):
    eps = 0.05
    out = build(m, eps)
    print(f'm={m}')
    print(f"  parseval_error={out['parseval_error']:.3e}")
    print(f"  nonzero_spectrum={out['nonzero_spectrum']}")
    for g, (tau, S, lev) in enumerate(out['bank_stats']):
        print(f'  bank{g}: tau={tau:.16g}, S={S.tolist()}, max_leverage={lev:.16g}')
        assert abs(tau - eps**2) < 1e-12
        assert np.linalg.norm(S - 0.5*np.eye(2)) < 1e-12
        assert abs(lev - 1/m) < 1e-12
    print(f"  max_abs_pivot={out['max_abs_pivot']:.15g}")
    print(f"  max_abs_heavy_edge={out['max_abs_heavy_edge']:.15g}")
    print(f"  max_abs_heavy_triple_det={out['max_abs_heavy_triple_det']:.15g}")
    assert out['parseval_error'] < 1e-11
    assert np.linalg.norm(out['nonzero_spectrum'] - np.array([-1.0, 1.0, 1.0])) < 1e-10

print('STATUS=PASS')
