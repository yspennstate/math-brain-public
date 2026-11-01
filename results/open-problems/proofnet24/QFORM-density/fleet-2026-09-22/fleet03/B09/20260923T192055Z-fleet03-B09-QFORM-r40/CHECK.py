import itertools
import math
import numpy as np

SEED = 20260923
TRIALS = 100
rng = np.random.default_rng(SEED)


def gram_det(M):
    M = np.asarray(M, dtype=float)
    return float(np.linalg.det(M @ M.T))


def row_marginal_three(B):
    triples = list(itertools.combinations(range(B.shape[0]), 3))
    vals = {S: max(0.0, gram_det(B[list(S)])) for S in triples}
    Z = sum(vals.values())
    marg = np.zeros(B.shape[0])
    for S, value in vals.items():
        for i in S:
            marg[i] += value
    return Z, marg / Z


def row_marginal_two(C):
    pairs = list(itertools.combinations(range(C.shape[0]), 2))
    vals = {S: max(0.0, gram_det(C[list(S)])) for S in pairs}
    Z = sum(vals.values())
    marg = np.zeros(C.shape[0])
    for S, value in vals.items():
        for i in S:
            marg[i] += value
    return Z, marg / Z


max_err_1 = 0.0
max_err_2 = 0.0
max_err_3 = 0.0

for _ in range(TRIALS):
    B = rng.normal(size=(8, 7))
    Z3, alpha = row_marginal_three(B)
    a = int(np.argmax(alpha))
    ba = B[a]
    P_a = np.outer(ba, ba) / float(ba @ ba)
    remaining = [i for i in range(B.shape[0]) if i != a]
    C = B[remaining] @ (np.eye(B.shape[1]) - P_a)
    Z2, beta = row_marginal_two(C)

    V_a = alpha[a] * Z3
    rhs_1 = float(ba @ ba) * Z2
    max_err_1 = max(max_err_1, abs(V_a - rhs_1) / max(1.0, abs(V_a)))

    b_pos = int(np.argmax(beta))
    b = remaining[b_pos]
    V_ab = beta[b_pos] * V_a
    B_H = B[[a, b]]
    Delta = float(np.linalg.det(B_H @ B_H.T))
    P_ab = B_H.T @ np.linalg.inv(B_H @ B_H.T) @ B_H
    remaining_2 = [i for i in range(B.shape[0]) if i not in (a, b)]
    D = B[remaining_2] @ (np.eye(B.shape[1]) - P_ab)
    Z1 = float(np.sum(D * D))
    max_err_2 = max(max_err_2, abs(V_ab - Delta * Z1) / max(1.0, abs(V_ab)))

    gamma = np.sum(D * D, axis=1) / Z1
    c_pos = int(np.argmax(gamma))
    c = remaining_2[c_pos]
    V_abc = gamma[c_pos] * V_ab
    rhs_3 = float(np.linalg.det(B[[a, b, c]] @ B[[a, b, c]].T))
    max_err_3 = max(max_err_3, abs(V_abc - rhs_3) / max(1.0, abs(V_abc)))

# N=64 Walsh regression from the report.
N = 64
columns = []
for j in range(N):
    s1 = 1 if (j & 1) == 0 else -1
    s2 = 1 if (j & 2) == 0 else -1
    columns.append([1, s1, s2])
B = np.asarray(columns, dtype=float).T / math.sqrt(N)
svals = np.linalg.svd(B, compute_uv=False)
Z3_walsh = float(np.linalg.det(B @ B.T))
K = B[:, [0, 1, 2]]
det_K = abs(float(np.linalg.det(K)))
partner_bound = 3.0 * det_K ** (-1.0 / 3.0)
three_hub_bound = 3.0 * math.sqrt(2.0) * Z3_walsh ** (-1.0 / 6.0)

C_diffuse = 6.0 * math.sqrt(math.e)
C_one_hub = 3.0 * 2.0 ** (4.0 / 3.0) * math.e ** (1.0 / 3.0)
C_two_hub = 3.0 * 2.0 ** (7.0 / 6.0)
C_three_hub = 6.0
C_theorem = max(C_diffuse, C_one_hub, C_two_hub, C_three_hub)

print(f"seed={SEED} trials={TRIALS}")
print(f"max relative error V_a identity   = {max_err_1:.16e}")
print(f"max relative error V_ab identity  = {max_err_2:.16e}")
print(f"max relative error V_abc identity = {max_err_3:.16e}")
print(f"Walsh singular values = {svals}")
print(f"Walsh Z3 = {Z3_walsh:.16f}")
print(f"Walsh selected |det K| = {det_K:.16f}")
print(f"partner physical-minor bound = {partner_bound:.12f}")
print(f"three-hub aggregate bound = {three_hub_bound:.12f}")
print(f"diffuse branch constant = {C_diffuse:.12f}")
print(f"one-hub branch constant = {C_one_hub:.12f}")
print(f"two-hub branch constant = {C_two_hub:.12f}")
print(f"three-hub branch constant = {C_three_hub:.12f}")
print(f"theorem constant = {C_theorem:.12f}")

assert max_err_1 < 1e-12
assert max_err_2 < 1e-12
assert max_err_3 < 1e-12
assert np.allclose(svals, np.ones(3), atol=1e-12)
assert abs(Z3_walsh - 1.0) < 1e-12
assert abs(det_K - 1.0 / 128.0) < 1e-12
assert C_theorem < 10.551
print("ALL CHECKS PASSED")
