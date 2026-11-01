# E0095: exact effect of adding ONE edge to the cycle C_n and the path P_n.
# Three notions of speed: Laplacian algebraic connectivity lambda_2(L),
# simple random walk (SRW) spectral gap 1 - lambda_2(P), P = D^{-1}A, and the
# uniform-stationary (Metropolised / max-degree) walk K = I - L/d_max.
import numpy as np, itertools, sys
np.set_printoptions(precision=6, suppress=True)

def lap_cycle(n):
    A = np.zeros((n, n))
    for j in range(n):
        A[j, (j+1) % n] = A[(j+1) % n, j] = 1
    return A

def lap_path(n):
    A = np.zeros((n, n))
    for j in range(n-1):
        A[j, j+1] = A[j+1, j] = 1
    return A

def gaps(A):
    d = A.sum(1); L = np.diag(d) - A
    lam = np.linalg.eigvalsh(L)
    # SRW: eigenvalues of P = D^{-1}A are those of D^{-1/2} A D^{-1/2}
    Dm = np.diag(1/np.sqrt(d)); S = Dm @ A @ Dm
    mu = np.sort(np.linalg.eigvalsh(S))[::-1]
    srw_gap = 1 - mu[1]
    srw_abs = 1 - max(mu[1], -mu[-1])
    return lam[1], srw_gap, srw_abs, lam

def study(name, A0, n):
    l2, g, ga, lam = gaps(A0)
    print(f"{name} n={n}: base lambda_2(L)={l2:.8f} lambda_3(L)={lam[2]:.8f} SRW gap={g:.8f} abs gap={ga:.8f}")
    rows = []
    for u in range(n):
        for v in range(u+1, n):
            if A0[u, v]: continue
            A = A0.copy(); A[u, v] = A[v, u] = 1
            l2n, gn, gan, _ = gaps(A)
            rows.append((u, v, l2n, gn, gan))
    rows = np.array(rows)
    print("  Laplacian lambda_2 after one edge: min %.8f max %.8f (base %.8f, base lambda_3 %.8f)" %
          (rows[:, 2].min(), rows[:, 2].max(), l2, lam[2]))
    print("  SRW gap after one edge:            min %.8f max %.8f (base %.8f)" % (rows[:, 3].min(), rows[:, 3].max(), g))
    best = rows[np.argmax(rows[:, 3])]
    print("  best SRW edge: (%d,%d) gap %.8f ; ratio to base %.6f" % (best[0], best[1], best[3], best[3]/g))
    bestL = rows[rows[:, 2] > rows[:, 2].max() - 1e-9]
    print("  edges attaining max Laplacian lambda_2:", [(int(r[0]), int(r[1])) for r in bestL][:12], "count", len(bestL))
    return rows

for n in [8, 9, 12, 13, 20, 21, 40, 41, 80]:
    rows = study("cycle", lap_cycle(n), n)
    # check Theorem: SRW gap never above the cycle's
    l2, g, _, _ = gaps(lap_cycle(n))
    assert rows[:, 3].max() <= g + 1e-12, "SRW gap increased!"
    assert abs(rows[:, 2].max() - l2) < 1e-10 and abs(rows[:, 2].min() - l2) < 1e-10
    print("  CHECK cycle: every chord leaves lambda_2(L) unchanged and SRW gap <= cycle gap: OK")
for n in [8, 9, 12, 13, 20, 21, 40, 41, 80]:
    rows = study("path", lap_path(n), n)
    l2, g, _, lam = gaps(lap_path(n))
    assert rows[:, 2].max() <= lam[2] + 1e-12
    end = rows[(rows[:, 0] == 0) & (rows[:, 1] == n-1)][0]
    print("  end edge (0,n-1): lambda_2 = %.8f = lambda_3(P_n)? %s ; SRW gap %.8f" % (end[2], abs(end[2]-lam[2]) < 1e-10, end[3]))
    # which symmetric chords tie the Laplacian optimum
    ties = [(int(r[0]), int(r[1])) for r in rows if abs(r[2] - lam[2]) < 1e-10]
    print("  chords with lambda_2(P_n + e) = lambda_3(P_n):", ties)
