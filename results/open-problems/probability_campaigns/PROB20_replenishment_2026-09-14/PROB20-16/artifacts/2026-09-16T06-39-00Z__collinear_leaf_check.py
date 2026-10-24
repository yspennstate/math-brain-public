import itertools
import math
import numpy as np

SEED = 20260916
TRIALS = 3000


def atoms(K):
    n = K.shape[0]
    out = []
    for bits in itertools.product((0, 1), repeat=n):
        Q = K.astype(complex).copy()
        m = 0
        for i, bit in enumerate(bits):
            if bit:
                m += 1
            else:
                Q[i, i] -= 1
        p = ((-1) ** (n - m) * np.linalg.det(Q)).real
        out.append(p)
    return np.array(out)


def entropy(K):
    p = atoms(K)
    if p.min() < -1e-10:
        raise AssertionError(("negative atom", p.min()))
    p = np.maximum(p, 0.0)
    return -sum(x * math.log(x) for x in p if x > 0)


def strict_contraction(K, margin=0.02):
    ev = np.linalg.eigvalsh(K)
    return ev.min() > margin and ev.max() < 1 - margin


def phi(a, B, P, s):
    return a * entropy(B - (1-a)*s*P) + (1-a)*entropy(B + a*s*P)


rng = np.random.default_rng(SEED)
accepted = 0
min_full_gap = float("inf")
min_monotonic_gap = float("inf")
min_aux_gap = float("inf")
min_strength_defect = float("inf")
max_chain_residual = 0.0

for _ in range(TRIALS):
    a = rng.uniform(0.15, 0.85)
    v = rng.normal(size=2) + 1j*rng.normal(size=2)
    v /= np.linalg.norm(v)
    P = np.outer(v, np.conj(v))

    Bs, zs, Ks = [], [], []
    ok = True
    for _j in range(2):
        d = rng.uniform(0.25, 0.75, size=2)
        off = (rng.normal() + 1j*rng.normal()) * 0.04
        B = np.array([[d[0], off], [np.conj(off), d[1]]], complex)
        z = (rng.normal() + 1j*rng.normal()) * 0.04
        w = z*v
        K = np.block([
            [np.array([[a]], complex), np.conj(w)[None, :]],
            [w[:, None], B],
        ])
        if not strict_contraction(K):
            ok = False
            break
        Bs.append(B)
        zs.append(z)
        Ks.append(K)
    if not ok:
        continue

    t = rng.uniform()
    Kt = (1-t)*Ks[0] + t*Ks[1]
    Bt = (1-t)*Bs[0] + t*Bs[1]

    s0 = abs(zs[0])**2/(a*(1-a))
    s1 = abs(zs[1])**2/(a*(1-a))
    zt = (1-t)*zs[0] + t*zs[1]
    st = abs(zt)**2/(a*(1-a))
    sb = (1-t)*s0 + t*s1
    defect_formula = t*(1-t)*abs(zs[1]-zs[0])**2/(a*(1-a))
    assert abs((sb-st)-defect_formula) < 2e-15

    phia = phi(a, Bt, P, st)
    phib = phi(a, Bt, P, sb)
    monotonic_gap = phia-phib

    endpoint_phi0 = phi(a, Bs[0], P, s0)
    endpoint_phi1 = phi(a, Bs[1], P, s1)
    aux_gap = phib - ((1-t)*endpoint_phi0 + t*endpoint_phi1)

    h_a = -a*math.log(a)-(1-a)*math.log(1-a)
    chain_resid = abs(entropy(Kt) - (h_a + phia))
    full_gap = entropy(Kt) - ((1-t)*entropy(Ks[0]) + t*entropy(Ks[1]))

    assert monotonic_gap >= -1e-10
    assert aux_gap >= -1e-10
    assert full_gap >= -1e-10

    min_full_gap = min(min_full_gap, full_gap)
    min_monotonic_gap = min(min_monotonic_gap, monotonic_gap)
    min_aux_gap = min(min_aux_gap, aux_gap)
    min_strength_defect = min(min_strength_defect, sb-st)
    max_chain_residual = max(max_chain_residual, chain_resid)
    accepted += 1

print("PASS")
print("seed", SEED)
print("accepted", accepted)
print("min_full_gap", repr(min_full_gap))
print("min_monotonic_gap", repr(min_monotonic_gap))
print("min_aux_gap", repr(min_aux_gap))
print("min_strength_defect", repr(min_strength_defect))
print("max_chain_residual", repr(max_chain_residual))
