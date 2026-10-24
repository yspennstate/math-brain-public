# Cycle plus a uniformly random perfect matching, large n: second adjacency eigenvalue
# against the Alon-Boppana / Friedman value 2 sqrt 2, and the lazy-walk TV mixing time
# against 3 log_2 n (Lubetzky-Sly / Lubetzky-Peres cutoff location for cubic graphs).
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, time
rng = np.random.default_rng(20260909)
def cycle_plus_matching(n):
    perm = rng.permutation(n)
    rows = list(range(n)) + [(j+1) % n for j in range(n)]
    cols = [(j+1) % n for j in range(n)] + list(range(n))
    for k in range(0, n, 2):
        a, b = perm[k], perm[k+1]
        rows += [a, b]; cols += [b, a]
    A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    if A.max() > 1: return None   # matching edge coincided with a cycle edge; resample
    return A
def tmix(A, eps=0.25):
    n = A.shape[0]; dist = np.zeros(n); dist[0] = 1; t = 0
    P = (A/3.0).T.tocsr()
    while 0.5*np.abs(dist - 1/n).sum() > eps:
        dist = 0.5*(dist + P @ dist); t += 1
    return t
print("n, lambda_2(A), lambda_min(A), 2sqrt2=%.5f, lazy t_mix(1/4), 3log2 n" % (2*np.sqrt(2)))
for n in [1000, 4000, 16000, 64000]:
    A = None
    while A is None: A = cycle_plus_matching(n)
    t0 = time.time()
    ev = sla.eigsh(A.astype(float), k=3, which='LA', return_eigenvectors=False)
    evm = sla.eigsh(A.astype(float), k=1, which='SA', return_eigenvectors=False)
    ev = np.sort(ev)[::-1]
    tm = tmix(A)
    print(f"{n:6d}  lambda_2={ev[1]:.5f}  lambda_min={evm[0]:.5f}  t_mix={tm}  3log2n={3*np.log2(n):.2f}  ratio={tm/(3*np.log2(n)):.3f}  ({time.time()-t0:.1f}s)")
