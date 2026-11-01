# Path P_n plus the symmetric chord {j, n-1-j}: the Laplacian lambda_2 of the
# new graph equals lambda_3(P_n) = 2-2cos(2 pi/n) exactly iff (conjecturally) 4j < n-1.
# Also: which symmetric chord maximises the SRW gap.
import numpy as np
def lam(n, j):
    A = np.zeros((n, n))
    for x in range(n-1): A[x, x+1] = A[x+1, x] = 1
    A[j, n-1-j] = A[n-1-j, j] = 1
    d = A.sum(1); L = np.diag(d) - A
    l2 = np.linalg.eigvalsh(L)[1]
    S = A/np.sqrt(np.outer(d, d)); mu = np.sort(np.linalg.eigvalsh(S))[::-1]
    return l2, 1-mu[1]
ok = True
for n in list(range(6, 130)) + [150, 151, 200, 201, 300, 301, 400]:
    l3 = 2-2*np.cos(2*np.pi/n)
    ties = []; best = (-1, None)
    for j in range(0, (n-1)//2):
        l2, g = lam(n, j)
        if abs(l2 - l3) < 1e-9: ties.append(j)
        if g > best[0]: best = (g, j)
    pred = [j for j in range(0, (n-1)//2) if 4*(j+1) <= n]
    if ties != pred: ok = False; print("MISMATCH", n, ties, pred)
    cyc = 1-np.cos(2*np.pi/n)
    if n % 10 == 0 or n < 14:
        print(f"n={n}: ties j in {ties[0]}..{ties[-1]} (pred 4(j+1)<=n -> j<= {pred[-1]}); best SRW symmetric chord j={best[1]} gap {best[0]:.8f}, ratio to closing the cycle {best[0]/cyc:.5f}")
print("threshold rule 4(j+1) <= n matched for all n tested:", ok)
