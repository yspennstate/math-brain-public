import math
import numpy as np

C_aff = 5 * 3**(3/5) / 2**(9/5)
C_out = 25 * 3**(3/5) / 2**(7/2)
C_hybrid = 3 * 2**(31/36)

print(f"C_aff={C_aff:.15f}")
print(f"C_out={C_out:.15f}")
print(f"C_hybrid={C_hybrid:.15f}")

# Deterministic regression of the global-kernel identity in Theorem 4.1.
rng = np.random.default_rng(20260923)
max_kernel_error = 0.0
for kdim in (0, 1, 3, 7):
    for _ in range(20):
        while True:
            B = rng.normal(size=(2, 2))
            if abs(np.linalg.det(B)) > 0.2:
                break
        C = rng.normal(size=(2, 2))
        C = (C + C.T) / 2
        D = rng.normal(size=(2, 2))
        D = (D + D.T) / 2
        E = rng.normal(size=(2, kdim))
        F = rng.normal(size=(2, kdim))
        G = rng.normal(size=(kdim, kdim))
        G = (G + G.T) / 2
        kappa = rng.normal(size=2)

        # Impose a_L=r_L=t_L=0 exactly at the coefficient level.
        r = C @ kappa
        s = B.T @ kappa
        t = E.T @ kappa
        a = kappa @ C @ kappa

        n = 5 + kdim
        A = np.zeros((n, n))
        iu, iv, iw = slice(1, 3), slice(3, 5), slice(5, n)
        A[0, 0] = a
        A[0, iu] = r; A[iu, 0] = r
        A[0, iv] = s; A[iv, 0] = s
        A[iu, iu] = C
        A[iu, iv] = B; A[iv, iu] = B.T
        A[iv, iv] = D
        if kdim:
            A[0, iw] = t; A[iw, 0] = t
            A[iu, iw] = E; A[iw, iu] = E.T
            A[iv, iw] = F; A[iw, iv] = F.T
            A[iw, iw] = G

        h0 = np.r_[1.0, -kappa, np.zeros(2 + kdim)]
        max_kernel_error = max(max_kernel_error, np.linalg.norm(A @ h0))

print(f"max_kernel_error={max_kernel_error:.3e}")
assert max_kernel_error < 1e-12
assert abs(C_aff - 2.7758037936536497) < 1e-13
assert abs(C_out - 4.271769166372894) < 1e-13
assert abs(C_hybrid - 5.449310176166419) < 1e-13
print("STATUS=PASS")
