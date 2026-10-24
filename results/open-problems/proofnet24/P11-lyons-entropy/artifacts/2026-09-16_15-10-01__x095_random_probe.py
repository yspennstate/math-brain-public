import numpy as np, math

# NONPROOF diagnostic for the P11 Lyons three-site track.
# Sampling is not a global certificate. Any robust negative candidate must be
# rechecked with exact arithmetic or rigorous interval bounds before use.
SEED = 20260916
N = 20000
rng = np.random.default_rng(SEED)

masks = list(range(8))
subs = {m: [i for i in range(3) if (m >> i) & 1] for m in masks}


def atom_probs(K):
    p = []
    for m in masks:
        A = K.copy()
        Sc = [i for i in range(3) if not ((m >> i) & 1)]
        if Sc:
            A = A.copy()
            A[Sc, Sc] -= 1.0
        p.append(((-1) ** (3 - len(subs[m]))) * np.linalg.det(A).real)
    return np.array(p)


def adj(A):
    return np.linalg.det(A) * np.linalg.inv(A)


def phi_data(K):
    p = atom_probs(K)
    if np.min(p) <= 0:
        raise ArithmeticError("nonpositive atom")
    p0, p1, p2, p12, p3, p13, p23, p123 = p
    c = np.array([
        math.log(p2 * p3 / (p0 * p23)),
        math.log(p1 * p3 / (p0 * p13)),
        math.log(p1 * p2 / (p0 * p12)),
    ])
    tau = math.log(p0 * p12 * p13 * p23 / (p1 * p2 * p3 * p123))
    M = np.diag(c) + tau * K
    d = np.linalg.det(M).real

    Es = []
    for m in range(1, 8):
        A = K.copy()
        Sc = [i for i in range(3) if not ((m >> i) & 1)]
        if Sc:
            A = A.copy()
            A[Sc, Sc] -= 1.0
        Es.append(((-1) ** (3 - len(subs[m]))) * adj(A))

    pp = p[1:]
    V = np.diag(pp) - np.outer(pp, pp)
    T = np.empty((7, 7))
    v = np.empty(7)
    for i, E in enumerate(Es):
        v[i] = np.trace(M @ E).real
        for j, F in enumerate(Es):
            T[i, j] = np.trace(M @ E @ M @ F).real
    C = T + d * V
    C = (C + C.T) / 2
    evC = np.linalg.eigvalsh(C)

    # Deliberately skip numerically singular systems. A floating inverse in
    # this regime can manufacture false negative values of s-2.
    if evC[0] <= 1e-14 * max(1.0, evC[-1]):
        return None
    s = float(v @ np.linalg.solve(C, v))
    sign, ld = np.linalg.slogdet(C)
    if sign <= 0:
        return None
    phi = math.exp(ld) * (s - 2.0) if ld < 700 else math.inf
    return p, s, phi, evC[0], evC[-1]


def random_K(i):
    Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(Z)
    diag = np.diag(R)
    phase = np.ones(3, dtype=complex)
    nz = np.abs(diag) > 0
    phase[nz] = np.conj(diag[nz]) / np.abs(diag[nz])
    Q = Q @ np.diag(phase)
    if i % 2 == 0:
        x = rng.uniform(-10.0, 10.0, 3)
        lam = 1.0 / (1.0 + np.exp(-x))
    else:
        lam = rng.uniform(0.02, 0.98, 3)
    return Q @ np.diag(lam) @ Q.conj().T


best_gap = (math.inf, None)
best_phi = (math.inf, None)
robust_negative = []
accepted = 0
skipped = 0
for i in range(N):
    K = random_K(i)
    out = phi_data(K)
    if out is None:
        skipped += 1
        continue
    p, s, phi, cmin, cmax = out
    accepted += 1
    gap = s - 2.0
    if gap < best_gap[0]:
        best_gap = (gap, (K.copy(), p.copy(), s, phi, cmin, cmax))
    if phi < best_phi[0]:
        best_phi = (phi, (K.copy(), p.copy(), s, phi, cmin, cmax))
    if gap < -1e-8:
        robust_negative.append((gap, K.copy()))

print("NONPROOF_DIAGNOSTIC")
print(f"seed={SEED}")
print(f"requested_samples={N}")
print(f"accepted={accepted}")
print(f"skipped_ill_conditioned={skipped}")
print(f"robust_negative_gap_count={len(robust_negative)}")
gap, dat = best_gap
K, p, s, phi, cmin, cmax = dat
print(f"min_s_minus_2={gap:.16e}")
print(f"s_at_min_gap={s:.16e}")
print(f"phi_at_min_gap={phi:.16e}")
print("eigK_at_min_gap=" + " ".join(f"{x:.16e}" for x in np.linalg.eigvalsh(K)))
print(f"min_atom_at_min_gap={p.min():.16e}")
print(f"C_condition_proxy_at_min_gap={cmax / cmin:.16e}")
ph, dat2 = best_phi
print(f"min_phi={ph:.16e}")
print(f"s_minus_2_at_min_phi={dat2[2] - 2:.16e}")
print("NOTE=sampling_is_not_a_global_certificate")
