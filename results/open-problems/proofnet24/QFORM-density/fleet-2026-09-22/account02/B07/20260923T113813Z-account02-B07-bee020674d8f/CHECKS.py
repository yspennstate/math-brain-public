import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)

# Compound-tail ladder: T_k E_k <= (k+1) E_{k+1}.
def esym(lam, k):
    return sum(np.prod(c) for c in itertools.combinations(lam, k))

min_ratio = float('inf')
for _ in range(5000):
    lam = np.sort(np.exp(rng.uniform(-6, 6, size=rng.integers(5, 13))))[::-1]
    E3, E4, E5 = esym(lam, 3), esym(lam, 4), esym(lam, 5)
    T3, T4 = lam[3:].sum(), lam[4:].sum()
    assert T3 * E3 <= 4 * E4 * (1 + 1e-10)
    assert T4 * E4 <= 5 * E5 * (1 + 1e-10)
    min_ratio = min(min_ratio, E5 / (T4*T4*E3/20))

h = (2*math.sqrt(2)-1)/1572864
H = math.sqrt(63)*h/8
astar = H/8
frac_const = 3.929131771 * 4096**(1/16)

print(f'h={h:.16e}')
print(f'H={H:.16e}')
print(f'a=H/8={astar:.16e}')
print(f'fractional_E2_constant={frac_const:.12f}')
print(f'compound_tail_random_min_ratio={min_ratio:.12f}')

# Exact rank-four stress family M_eps.
def walsh_vec(N, bit):
    idx = np.arange(N)
    return ((-1.0)**((idx >> bit) & 1))/math.sqrt(N)

for N in (8, 16):
    u = np.ones(N)/math.sqrt(N)
    y = walsh_vec(N, 0)
    w = walsh_vec(N, 1)
    v, x, z = u.copy(), y.copy(), w.copy()
    for eps in (0.01, 0.25):
        D = np.outer(x, y) + eps*np.outer(z, w)
        M = np.zeros((N+1, N+1))
        M[0, 1:] = u
        M[1:, 0] = v
        M[1:, 1:] = D
        s = np.linalg.svd(M, compute_uv=False)
        expected = np.array([1., 1., 1., eps])
        assert np.max(np.abs(s[:4] - expected)) < 1e-10
        W = 1 + eps**2
        E3 = 1 + 3*eps**2
        residual_marginal = 2/N
        print(f'stress N={N} eps={eps}: s={s[:4].round(10).tolist()} '
              f'W={W:.10f} E3={E3:.10f} residual_marginal={residual_marginal:.10f}')

# Nonzero-anchor Schur-completion obstruction at the newest partner scale.
n = 64
u = np.r_[np.full(n, astar), np.zeros(n)]
v = np.r_[np.zeros(n), np.full(n, astar)]
D = np.vstack([u, v])
P = np.array([[0., astar], [astar, 0.]])
C = D.T @ np.linalg.inv(P) @ D
Aloc = np.block([[P, D], [D.T, C]])
sv = np.linalg.svd(Aloc, compute_uv=False)
E2 = np.linalg.det(D @ D.T)
assert abs(np.linalg.norm(u)-H) < 1e-18
assert abs(np.linalg.norm(v)-H) < 1e-18
assert abs(E2-H**4) < 1e-35
assert np.max(np.abs(Aloc)) <= astar*(1+1e-12)
assert np.sum(sv > 1e-10) == 2
print(f'completion star_norms={np.linalg.norm(u):.16e},{np.linalg.norm(v):.16e}')
print(f'completion E2={E2:.16e} H4={H**4:.16e} '
      f'maxcoeff={np.max(np.abs(Aloc)):.16e} rank_tol={np.sum(sv > 1e-10)}')
print('STATUS=QFORM_B07_H3_SUPPORT_RANK4_STRESS_CHECK_PASS')
