import itertools
import numpy as np

rng = np.random.default_rng(0)
for n in [5, 8, 15]:
    G = rng.normal(size=(n, 3))
    U = np.linalg.qr(G)[0][:, :3]
    L = list(range(1, n))
    S = sum(np.outer(U[i], U[i]) for i in L)
    m = float(np.linalg.det(S))
    ws = {
        I: float(np.linalg.det(U[list(I), :]) ** 2)
        for I in itertools.combinations(L, 3)
    }
    cb_err = abs(m - sum(ws.values()))
    Sinv = np.linalg.inv(S)
    rho_err = max(
        abs(
            float(U[i] @ Sinv @ U[i])
            - sum(w for I, w in ws.items() if i in I) / m
        )
        for i in L
    )
    maxrho = max(float(U[i] @ Sinv @ U[i]) for i in L)
    print(
        f"n={n} m={m:.15g} cb_err={cb_err:.3e} "
        f"rho_err={rho_err:.3e} maxrho={maxrho:.15g}"
    )
    assert cb_err < 1e-12
    assert rho_err < 1e-12
print("STATUS=PASS")
