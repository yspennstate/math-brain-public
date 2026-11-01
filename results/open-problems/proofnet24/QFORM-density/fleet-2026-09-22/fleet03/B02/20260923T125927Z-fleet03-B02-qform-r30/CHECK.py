import itertools
import math
import numpy as np

SEED = 20260923
rng = np.random.default_rng(SEED)


def e2_singular_sq(M):
    s = np.linalg.svd(M, compute_uv=False)
    lam = s * s
    return sum(lam[i] * lam[j]
               for i in range(len(lam))
               for j in range(i + 1, len(lam)))


def third_volume_data(B):
    m, n = B.shape
    rows = list(itertools.combinations(range(m), 3))
    cols = list(itertools.combinations(range(n), 3))
    terms = []
    Z = 0.0
    for R in rows:
        for S in cols:
            d = np.linalg.det(B[np.ix_(R, S)])
            w = d * d
            Z += w
            terms.append((R, S, w))
    alpha = np.zeros(m)
    beta = np.zeros(n)
    J = np.zeros((m, n))
    for R, S, w in terms:
        for i in R:
            alpha[i] += w
        for j in S:
            beta[j] += w
        for i in R:
            for j in S:
                J[i, j] += w
    return Z, alpha / Z, beta / Z, J


max_schur_relerr = 0.0
ie_violations = 0
for _ in range(100):
    B = rng.normal(size=(5, 5))
    Z, alpha, beta, J = third_volume_data(B)
    i = int(np.argmax(alpha))
    j = int(np.argmax(beta))
    if J[i, j] / Z + 1e-12 < alpha[i] + beta[j] - 1.0:
        ie_violations += 1

    rows = [k for k in range(5) if k != i]
    cols = [k for k in range(5) if k != j]
    a = B[i, j]
    c = B[np.ix_(rows, [j])].reshape(-1)
    r = B[np.ix_([i], cols)].reshape(-1)
    N = B[np.ix_(rows, cols)]
    S = N - np.outer(c, r) / a
    rhs = a * a * e2_singular_sq(S)
    relerr = abs(J[i, j] - rhs) / max(1.0, abs(J[i, j]))
    max_schur_relerr = max(max_schur_relerr, relerr)

min_joint_star_slack = float("inf")
for _ in range(200):
    B = rng.normal(size=(5, 5))
    Z, alpha, beta, J = third_volume_data(B)
    i = int(np.argmax(alpha))
    j = int(np.argmax(beta))
    rows = [k for k in range(5) if k != i]
    cols = [k for k in range(5) if k != j]
    a = B[i, j]
    c = B[np.ix_(rows, [j])].reshape(-1)
    r = B[np.ix_([i], cols)].reshape(-1)
    N = B[np.ix_(rows, cols)]
    Pc = np.eye(len(c)) - np.outer(c, c) / np.dot(c, c)
    Pr = np.eye(len(r)) - np.outer(r, r) / np.dot(r, r)
    F = np.linalg.norm(Pc @ N @ Pr, ord="fro")
    rhs = abs(a) * math.sqrt(e2_singular_sq(N)) + np.linalg.norm(c) * np.linalg.norm(r) * F
    min_joint_star_slack = min(min_joint_star_slack, rhs - math.sqrt(J[i, j]))

q = 4.0 / 3.0
Cdiff = 3 * math.e / ((3 - 2 * q) * math.sqrt(q))
Cheavy = 3 * math.exp(2 / 3) * (q - 1) ** (-1 / 6)
Cpartner = 2 ** (5 / 3) * 3 ** (1 / 4) * math.exp(1 / 2)
Cpartner_Z = Cpartner * 3 ** (1 / 8)

# Bisection for equality of diffuse and exact-rank-two branch constants.
def cd(x):
    return 3 * math.e / ((3 - 2 * x) * math.sqrt(x))


def ch(x):
    return 3 * math.exp(2 / 3) * (x - 1) ** (-1 / 6)

lo, hi = 1.000001, 1.49
for _ in range(100):
    mid = (lo + hi) / 2
    if cd(mid) - ch(mid) > 0:
        hi = mid
    else:
        lo = mid
qopt = (lo + hi) / 2

print(f"seed={SEED}")
print(f"inclusion_exclusion_violations={ie_violations}")
print(f"max_schur_relative_error={max_schur_relerr:.16e}")
print(f"min_joint_star_slack={min_joint_star_slack:.16e}")
print(f"Cdiff_q4over3={Cdiff:.15f}")
print(f"Cheavy_rank2_q4over3={Cheavy:.15f}")
print(f"Cpartner_J={Cpartner:.15f}")
print(f"Cpartner_Z_q4over3={Cpartner_Z:.15f}")
print(f"q_balance={qopt:.15f}")
print(f"C_balance={cd(qopt):.15f}")
