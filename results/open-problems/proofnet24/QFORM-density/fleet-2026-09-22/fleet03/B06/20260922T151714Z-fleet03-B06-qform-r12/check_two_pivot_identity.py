import math
import numpy as np

C_H = 2*(48*(1+math.sqrt(2)))**(2/5)
D = (15/2)**(5/6)
C_2 = C_H*D*2**(1/6)
C_3 = (8/(3**(3/4)))*(C_2**(3/4))
print(f"C_H={C_H:.12f}")
print(f"D={D:.12f}")
print(f"C_2={C_2:.12f}")
print(f"C_3={C_3:.12f}")

rng = np.random.default_rng(20260922)
max_rel = 0.0
checked = 0
for _ in range(500):
    n = int(rng.integers(4, 13))
    R, _ = np.linalg.qr(rng.normal(size=(n, 3)))
    vals = []
    while len(vals) < 3:
        x = float(rng.uniform(-4, 4))
        if abs(x) >= 1:
            vals.append(x)
    Lam = np.diag(vals)
    M = R @ Lam @ R.T
    pairs = []
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            a = M[i, i]
            d = M[i, i]*M[k, k] - M[i, k]**2
            if abs(a) > 1e-8 and abs(d) > 1e-8:
                pairs.append((i, k, a, d))
    if not pairs:
        continue
    i, k, a, d = pairs[int(rng.integers(0, len(pairs)))]
    I = [i, k]
    J = [j for j in range(n) if j not in I]
    AII = M[np.ix_(I, I)]
    S = M[np.ix_(J, J)] - M[np.ix_(J, I)] @ np.linalg.inv(AII) @ M[np.ix_(I, J)]
    eig = np.linalg.eigvalsh(S)
    gamma = eig[np.argmax(np.abs(eig))]
    U = R[I, :]
    Delta = np.linalg.det(U @ U.T)
    rhs = np.linalg.det(Lam)*Delta/d
    rel = abs(gamma-rhs)/max(1.0, abs(gamma), abs(rhs))
    max_rel = max(max_rel, rel)
    checked += 1
print(f"random_identity_checks={checked}")
print(f"max_relative_error={max_rel:.3e}")
assert checked == 500
assert max_rel < 1e-10
