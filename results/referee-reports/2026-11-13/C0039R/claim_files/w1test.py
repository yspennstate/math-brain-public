"""C0039 test: is W1_Hamming(P_Q, P_Q') <= ||Q - Q'||_1 (trace norm) for Hermitian contractions on a finite set?

P_Q(X = A) = (-1)^{|A^c|} det(Q - I_{A^c}).  W1 by the transport LP with cost |A xor B|.
On a finite group, normalised d-bar = W1/|E| and tau|Q-Q'| = tr|Q-Q'|/|E|, so the general finite inequality
implies Lyons' question for finite groups.  Prints the worst ratio found.
"""
import itertools, sys, json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 4
TRIALS = int(sys.argv[3]) if len(sys.argv) > 3 else 200

subsets = list(range(1 << N))
pop = np.array([bin(a).count('1') for a in subsets])
cost = np.array([[bin(a ^ b).count('1') for b in subsets] for a in subsets], float).ravel()
M = len(subsets)
A_eq = lil_matrix((2 * M, M * M))
for a in range(M):
    for b in range(M):
        A_eq[a, a * M + b] = 1
        A_eq[M + b, a * M + b] = 1
A_eq = A_eq.tocsr()


def law(Q):
    p = np.empty(M)
    for a in subsets:
        D = Q.copy()
        for e in range(N):
            if not (a >> e) & 1:
                D[e, e] -= 1
        p[a] = ((-1) ** (N - pop[a]) * np.linalg.det(D)).real
    return np.clip(p, 0, None) / max(p.clip(0).sum(), 1e-300)


def w1(p, q):
    # last column-sum row is implied by the others; dropping it avoids rounding infeasibility
    r = linprog(cost, A_eq=A_eq[:-1], b_eq=np.concatenate([p, q])[:-1], bounds=(0, None), method='highs')
    return r.fun if r.status == 0 else float('nan')


def rand_contraction(complex_=True):
    X = rng.normal(size=(N, N)) + (1j * rng.normal(size=(N, N)) if complex_ else 0)
    U, _ = np.linalg.qr(X)
    lam = rng.choice([rng.uniform(0, 1, N), rng.integers(0, 2, N).astype(float)])
    return (U * lam) @ U.conj().T


def trnorm(H):
    return np.abs(np.linalg.eigvalsh(H)).sum()


def ratio(Q, Qp):
    t = trnorm(Q - Qp)
    v = (w1(law(Q), law(Qp)) / t) if t > 1e-12 else 0.0
    return (0.0 if v != v else v), t


best = (0, None)
for k in range(TRIALS):
    Q = rand_contraction(k % 2 == 0)
    mode = k % 3
    if mode == 0:
        Qp = rand_contraction(k % 2 == 0)
    else:  # small non-commuting perturbation, kept a contraction
        H = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); H = (H + H.conj().T) / 2
        eps = 10 ** rng.uniform(-3, -0.5)
        w, V = np.linalg.eigh(Q + eps * H)
        Qp = (V * np.clip(w, 0, 1)) @ V.conj().T
    r, t = ratio(Q, Qp)
    # local hill-climb on the worst ones
    if r > best[0] * 0.95:
        for _ in range(40):
            H = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); H = (H + H.conj().T) / 2
            w, V = np.linalg.eigh(Qp + 0.05 * H)
            Qc = (V * np.clip(w, 0, 1)) @ V.conj().T
            rc, tc = ratio(Q, Qc)
            if rc > r:
                Qp, r, t = Qc, rc, tc
    if r > best[0]:
        best = (r, (Q, Qp, t))
        print(f'trial {k}: ratio {r:.6f} (tr norm {t:.4g})', flush=True)

r, (Q, Qp, t) = best
print('N', N, 'worst ratio', round(r, 6))
json.dump({'N': N, 'ratio': r, 'trnorm': t, 'Q': [[str(x) for x in row] for row in Q],
           'Qp': [[str(x) for x in row] for row in Qp]}, open(f'worst_N{N}_s{sys.argv[1] if len(sys.argv)>1 else 0}.json', 'w'))
