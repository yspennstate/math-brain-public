"""Randomstrasse 2025 list, Conjectures 26 and 27 (intake I rows from randomstrasse_2025_v1).

Paley graph G_p on Z_p, p = 1 mod 4: i ~ j iff i - j is a quadratic residue. The source's theta is the
one that bounds the CLIQUE number, i.e. the Lovasz theta of the complement:

    theta(G) = max { sum_ij X_ij : X psd, trace X = 1, X_ij = 0 whenever i != j and ij is NOT an edge }.

  Conjecture 26: theta(G_{p,1}) ~ sqrt(p/2), where G_{p,1} is induced on the neighbours of 0.
  Conjecture 27: theta(G_{p,2}) <= (2/3) sqrt(p) for large p, where G_{p,2} is induced on the common
                 neighbours of 0 and 1.

Both are exactly computable for moderate p, the first as an LP because G_{p,1} is circulant, the second
as an SDP. This script computes them and prints the ratios the conjectures are about.
"""
import numpy as np, sys
import cvxpy as cp


def paley_qr(p):
    return set((x * x) % p for x in range(1, p))


def theta_clique(adj):
    """Lovasz theta of the complement: an upper bound on the clique number of the graph with this
    adjacency matrix (0/1, zero diagonal)."""
    n = adj.shape[0]
    if n == 0: return 0.0
    if n == 1: return 1.0
    X = cp.Variable((n, n), symmetric=True)
    cons = [X >> 0, cp.trace(X) == 1]
    # X_ij = 0 on non-edges (i != j)
    nz = np.argwhere((adj == 0) & (~np.eye(n, dtype=bool)))
    if len(nz):
        cons.append(X[nz[:, 0], nz[:, 1]] == 0)
    prob = cp.Problem(cp.Maximize(cp.sum(X)), cons)
    try:
        prob.solve(solver=cp.SCS, eps=1e-7, max_iters=60000, verbose=False)
    except Exception:
        return None
    return float(prob.value) if prob.value is not None else None


def localizations(p):
    QR = paley_qr(p)
    V1 = sorted(QR)                                   # neighbours of 0
    V2 = sorted(v for v in QR if ((v - 1) % p) in QR)  # neighbours of 0 and of 1
    def induced(V):
        m = len(V); A = np.zeros((m, m))
        for a in range(m):
            for b in range(a + 1, m):
                if ((V[a] - V[b]) % p) in QR:
                    A[a, b] = A[b, a] = 1.0
        return A
    return induced(V1), induced(V2), len(V1), len(V2)


if __name__ == '__main__':
    primes = [int(x) for x in sys.argv[1:]] or [13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113]
    print(f"{'p':>6} {'|G1|':>5} {'theta(G1)':>10} {'/sqrt(p/2)':>11} {'|G2|':>5} {'theta(G2)':>10} {'/sqrt(p)':>9} {'<= 2/3?':>8}")
    for p in primes:
        if p % 4 != 1: continue
        A1, A2, n1, n2 = localizations(p)
        t1 = theta_clique(A1); t2 = theta_clique(A2)
        if t1 is None or t2 is None:
            print(f"{p:>6} solver failed"); continue
        r1 = t1 / np.sqrt(p / 2); r2 = t2 / np.sqrt(p)
        print(f"{p:>6} {n1:>5} {t1:>10.4f} {r1:>11.4f} {n2:>5} {t2:>10.4f} {r2:>9.4f} {'yes' if r2 <= 2/3 + 1e-9 else 'NO':>8}")
