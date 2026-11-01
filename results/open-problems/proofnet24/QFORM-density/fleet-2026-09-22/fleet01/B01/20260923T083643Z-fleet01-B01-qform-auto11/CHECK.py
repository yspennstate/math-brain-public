import math
import numpy as np


def sylvester(n: int) -> np.ndarray:
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H / math.sqrt(n)


eta = 0.25
c = 1.0 + eta
base_const = 15.0 / (2.0 ** (1.0 / 5.0))
new_const = base_const * c ** (-4.0 / 5.0)

beta = 0.25
D_beta = ((1.0 + beta) / (math.pi * beta)) * (
    2.0
    * math.pi
    * math.exp(beta / 2.0)
    * (4.0 * math.pi) ** beta
    / (1.0 - 2.0 * beta)
) ** (1.0 / (1.0 + beta))
partner_const = D_beta * c ** (-4.0 / 5.0) * 2.0 ** (-1.0 / 10.0)

print(f"base_constant={base_const:.12f}")
print(f"eta_quarter_new_constant={new_const:.12f}")
print(f"partner_D_beta={D_beta:.12f}")
print(f"eta_quarter_partner_constant={partner_const:.12f}")

for m in (8, 16, 32, 64):
    H = sylvester(m)
    u1 = H[:, 0]
    u2 = H[:, 1]
    v = H[:, 0]
    w = H[:, 1]

    # I bank has size m; J bank has distinguished e0 plus m diffuse coordinates.
    K = np.zeros((m, m + 1))
    K[:, 0] = c * u1
    K[:, 1:] += c * np.outer(u2, v)

    B = np.zeros((m + 1, m + 1))
    B[1:, 1:] = np.outer(w, w)

    A = np.block([[eta * H, K], [K.T, B]])
    s = np.linalg.svd(A, compute_uv=False)
    max_diag = float(np.max(np.abs(np.diag(A))))

    d = np.diag(A)
    max_pair_det = 0.0
    for i in range(A.shape[0]):
        for j in range(i + 1, A.shape[0]):
            det2 = d[i] * d[j] - A[i, j] ** 2
            max_pair_det = max(max_pair_det, abs(float(det2)))

    assert s[3] >= 1.0 - 1e-12
    assert abs(s[4] - 1.0) <= 1e-10
    print(
        f"m={m:2d} "
        f"s1..s6={[round(float(x), 9) for x in s[:6]]} "
        f"max_diag={max_diag:.12f} "
        f"max_pair_det={max_pair_det:.12f}"
    )

print("STATUS=PASS")
