"""E2/E3: candidate C1 of the joint strategy (affine partitions, arbitrary leaves) and its per-T form (P).

C1:  F(x,y) = sum_j 1_{A_j}(x) g_j(y), affine partition {A_j} of F_2^a, codims c_j, arbitrary Boolean g_j:
        H(F) <= 2 sum_j p_j c_j + sum_j p_j H(g_j).
(P): for real v, Psi = sum_j v_j 1_{A_j}, E Psi^2 = 1, w_j = p_j v_j^2:
        H(Psihat^2) <= H(w) + sum_j w_j c_j.
Points of F_2^a are ints; bit i set <=> x_i = -1.  Floating point; EVIDENCE only (the proof is analytic).
"""
import itertools
import numpy as np
from fei_lib import fwht_int, fwht_float, entropy_from_W, entropy_probs


def span(basis):
    pts = {0}
    for b in basis:
        pts |= {p ^ b for p in pts}
    return pts


def all_subspaces(a):
    """All linear subspaces of F_2^a as frozensets (a <= 4)."""
    subs = set()
    vecs = list(range(1, 1 << a))
    for k in range(a + 1):
        for basis in itertools.combinations(vecs, k):
            s = frozenset(span(basis))
            if len(s) == (1 << k):
                subs.add(s)
    return subs


def all_affine(a):
    subs = all_subspaces(a)
    aff = set()
    for s in subs:
        for v in range(1 << a):
            aff.add(frozenset(v ^ p for p in s))
    return aff


def random_affine_partition(a, rng, aff_list, prefer_large=0.5):
    uncovered = set(range(1 << a))
    cells = []
    while uncovered:
        p = rng.choice(sorted(uncovered))
        cands = [A for A in aff_list if p in A and A <= uncovered]
        sizes = np.array([len(A) for A in cands], dtype=float)
        wts = sizes ** (prefer_large * 3)
        wts /= wts.sum()
        A = cands[rng.choice(len(cands), p=wts)]
        cells.append(A)
        uncovered -= A
    return cells


def direction_space(A):
    pts = sorted(A)
    v0 = pts[0]
    return {p ^ v0 for p in pts}


def is_reducible(cells, a):
    """True iff some hyperplane u.x=const has every cell on one side (u orthogonal to all directions)."""
    dirs = set()
    for A in cells:
        dirs |= direction_space(A)
    for u in range(1, 1 << a):
        if all(bin(u & d).count('1') % 2 == 0 for d in dirs):
            return True
    return False


def codim(A, a):
    return a - int(np.log2(len(A)))


def c1_check(cells, leaves, a, n):
    """leaves: list of +-1 arrays length 2^n (one per cell). Returns (H(F), bound)."""
    N = 1 << a
    lab = np.empty(N, dtype=np.int64)
    for j, A in enumerate(cells):
        for p in A:
            lab[p] = j
    B = np.array([leaves[lab[b]] for b in range(N)])          # B[b, y]
    F = B.T.reshape(-1)
    HF = entropy_from_W(fwht_int(F), a + n)
    pj = np.array([len(A) / N for A in cells])
    cj = np.array([codim(A, a) for A in cells])
    Hg = np.array([entropy_from_W(fwht_int(g), n) for g in leaves])
    bound = 2 * np.sum(pj * cj) + np.sum(pj * Hg)
    return HF, bound


def p_check(cells, v, a):
    N = 1 << a
    psi = np.zeros(N)
    for j, A in enumerate(cells):
        for p in A:
            psi[p] = v[j]
    psi /= np.sqrt(np.mean(psi ** 2))
    Wf = fwht_float(psi) / N
    Hpsi = entropy_probs(Wf ** 2)
    pj = np.array([len(A) / N for A in cells])
    cj = np.array([codim(A, a) for A in cells])
    vv = np.array([psi[min(A)] for A in cells])
    w = pj * vv ** 2
    rhs = entropy_probs(w) + np.sum(w * cj)
    return Hpsi, rhs


if __name__ == '__main__':
    rng = np.random.default_rng(20261012)
    for a in (3, 4):
        aff = sorted(all_affine(a), key=lambda s: (len(s), sorted(s)))
        print('a=', a, 'affine subspaces:', len(aff))
        n_irr = 0
        worstP = -1e9
        worstC1 = -1e9
        seen = 0
        for trial in range(1500 if a == 3 else 600):
            cells = random_affine_partition(a, rng, aff, prefer_large=rng.random())
            irr = not is_reducible(cells, a)
            n_irr += irr
            seen += 1
            m = len(cells)
            # (P) with random real v, several draws, including sign-heavy cancellation patterns
            for _ in range(20):
                v = rng.standard_normal(m)
                if rng.random() < 0.3:
                    v = np.sign(v) * (1 + 0.1 * rng.standard_normal(m))
                Hpsi, rhs = p_check(cells, v, a)
                worstP = max(worstP, Hpsi - rhs)
            # C1 with random Boolean leaves on n=3 or n=4 data bits
            n = 3 if a == 4 else 4
            for _ in range(5):
                kind = rng.integers(3)
                if kind == 0:
                    leaves = [rng.choice([-1, 1], size=1 << n) for _ in range(m)]
                elif kind == 1:   # signed copies of one function (coherent extreme)
                    base = rng.choice([-1, 1], size=1 << n)
                    leaves = [base * rng.choice([-1, 1]) for _ in range(m)]
                else:             # small perturbations of one function
                    base = rng.choice([-1, 1], size=1 << n)
                    leaves = []
                    for _ in range(m):
                        g = base.copy()
                        k = rng.integers(0, 3)
                        idx = rng.choice(1 << n, size=k, replace=False)
                        g[idx] *= -1
                        leaves.append(g * rng.choice([-1, 1]))
                HF, bound = c1_check(cells, leaves, a, n)
                worstC1 = max(worstC1, HF - bound)
        print('  partitions', seen, 'irreducible', n_irr, ' max(H(Psi)-rhs)=', worstP, ' max(H(F)-C1bound)=', worstC1)
