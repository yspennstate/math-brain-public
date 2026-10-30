import json
import math
import numpy as np

SEED = 202609240954
rng = np.random.default_rng(SEED)

def svals(A):
    return np.linalg.svd(A, compute_uv=False)

def sym_sqrt(G):
    w, V = np.linalg.eigh(G)
    Gh = (V * np.sqrt(w)) @ V.T
    Gmh = (V * (1.0 / np.sqrt(w))) @ V.T
    return Gh, Gmh

def theorem_quantities(M, N, rho):
    G = M.T @ M
    Gh, Gmh = sym_sqrt(G)
    g = svals(M)[-1]
    B = Gmh @ (M.T @ N) @ Gmh
    H = (B + B.T) / 2.0
    K = (B - B.T) / 2.0
    mu = np.linalg.eigvalsh(H)
    q = int(np.sum(np.abs(1.0 + mu) < rho))
    dplus = int(np.sum(mu >= -1.0 + rho - 1e-12))
    dminus = int(np.sum(mu <= -1.0 - rho + 1e-12))
    lhs = svals(M + N)
    return g, B, H, K, mu, q, dplus, dminus, lhs

TRIALS = 10000

# Suite 1: arbitrary noncommuting/skew component.
viol_branch = 0
min_branch_margin = float("inf")
for _ in range(TRIALS):
    n, m = 16, 11
    U, _ = np.linalg.qr(rng.normal(size=(n, m)))
    V, _ = np.linalg.qr(rng.normal(size=(m, m)))
    sig = np.exp(rng.uniform(math.log(1.0), math.log(3.0), size=m))
    Gh = (V * sig) @ V.T
    M = U @ Gh

    W, _ = np.linalg.qr(rng.normal(size=(m, m)))
    low_count = int(rng.integers(0, m + 1))
    eig = np.empty(m)
    eig[:low_count] = -2.0 - rng.exponential(2.0, size=low_count)
    eig[low_count:] = rng.exponential(3.0, size=m-low_count)
    rng.shuffle(eig)
    H = (W * eig) @ W.T

    K0 = rng.normal(size=(m, m))
    K = (K0 - K0.T) * rng.uniform(0.0, 4.0)
    B = H + K

    Z0 = rng.normal(size=(n, m))
    Z = (np.eye(n) - U @ U.T) @ Z0
    N = (U @ B + Z) @ Gh

    g, Bc, Hc, Kc, mu, q, dplus, dminus, lhs = theorem_quantities(M, N, 1.0)
    d = max(dplus, dminus)
    margin = lhs[d-1] - g
    min_branch_margin = min(min_branch_margin, margin)
    if margin < -1e-9:
        viol_branch += 1

# Suite 2: commutator-controlled resonance window.
viol_comm = 0
min_comm_margin = float("inf")
for _ in range(TRIALS):
    n, m = 16, 11
    U, _ = np.linalg.qr(rng.normal(size=(n, m)))
    V, _ = np.linalg.qr(rng.normal(size=(m, m)))
    sig = np.exp(rng.uniform(math.log(1.0), math.log(3.0), size=m))
    Gh = (V * sig) @ V.T
    M = U @ Gh

    W, _ = np.linalg.qr(rng.normal(size=(m, m)))
    q0 = int(rng.integers(0, 6))
    eig = list(-1.0 + rng.uniform(-0.65, 0.65, size=q0))
    for _j in range(m-q0):
        if rng.random() < 0.5:
            eig.append(-1.7 - rng.exponential(1.5))
        else:
            eig.append(-0.3 + rng.exponential(1.5))
    eig = np.array(eig)
    rng.shuffle(eig)
    H = (W * eig) @ W.T

    Kraw = rng.normal(size=(m, m))
    Kraw = (Kraw - Kraw.T) / 2.0
    kn = svals(Kraw)[0]
    target_kappa = float(rng.uniform(0.0, 0.2))
    K = Kraw * (target_kappa / kn if kn > 0 else 0.0)
    B = H + K

    Z0 = rng.normal(size=(n, m))
    Z = (np.eye(n) - U @ U.T) @ Z0
    N = (U @ B + Z) @ Gh

    g, Bc, Hc, Kc, mu, q, dplus, dminus, lhs = theorem_quantities(M, N, 0.7)
    kappa = svals(Kc)[0]
    d = m-q
    rhs = g * max(0.7-kappa, 0.0)
    margin = lhs[d-1] - rhs
    min_comm_margin = min(min_comm_margin, margin)
    if margin < -1e-9:
        viol_comm += 1

# Explicit fleet04/B12-r8-compatible physical carrier.
m, jdim = 11, 9
n = m + jdim
A0 = np.zeros((n, n))
A0[0, 0] = 4.0
A0[1, 1] = 4.0
for i in range(2, 11):
    j = m + (i-2)
    A0[i, j] = A0[j, i] = 2.0

P = np.eye(n)[:, :m]
M = A0 @ P
L = 1e6
beta = np.array([-1.0, -L, 0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

E = np.zeros((n, n))
E[0, 0] = 4.0 * beta[0]
E[1, 1] = 4.0 * beta[1]
for i in range(2, 11):
    j = m + (i-2)
    E[i, j] = E[j, i] = 2.0 * beta[i]

N = E @ P
g, B, H, K, mu, q, dplus, dminus, lhs = theorem_quantities(M, N, 1.0)

N2 = 55
C11 = max(
    8*N2*math.sqrt(6*math.pi*11),
    4*math.pi*N2,
    3*(400**(1/3))*((4*N2)**(5/6)),
    10*math.sqrt(2*math.e/3),
)

out = {
    "seed": SEED,
    "arbitrary_noncommutative_gap_suite": {
        "trials": TRIALS,
        "violations": viol_branch,
        "minimum_margin": min_branch_margin,
    },
    "commutator_defect_resonance_suite": {
        "trials": TRIALS,
        "violations": viol_comm,
        "minimum_margin": min_comm_margin,
    },
    "explicit_partner_compatible_family": {
        "L": L,
        "baseline_singular_values": svals(M).tolist(),
        "relative_H_eigenvalues": mu.tolist(),
        "relative_skew_norm": float(svals(K)[0]),
        "resonant_count_rho_1": q,
        "s10_after_addition": float(lhs[9]),
        "new_q1_bound_s10": float(g),
        "r53_one_sided_q1_bound": float(g*max(1.0 + np.sort(mu)[1], 0.0)),
        "six_mode_lower_bound_after_local_tail_1_over_4": 1.75,
        "C11": C11,
        "density_bound_after_tail": C11/1.75,
    },
}
print(json.dumps(out, indent=2))
