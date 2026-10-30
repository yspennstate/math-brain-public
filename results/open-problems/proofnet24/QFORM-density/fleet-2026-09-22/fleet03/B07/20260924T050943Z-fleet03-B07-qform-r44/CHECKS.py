import math
import numpy as np
import sympy as sp

SEED = 20260924050943
rng = np.random.default_rng(SEED)
TAU = 1.0 / 64.0
T0 = 8192.0 / 31.0

# Solve 81*tau*(T0-2*z/T0)=2*z^2.
b = 162.0 * TAU / T0
disc = b*b + 648.0 * TAU * T0
Z0 = (-b + math.sqrt(disc)) / 4.0
XSTAR = T0 - 2.0 * Z0 / T0
D_HI = 3.0 * math.sqrt(TAU / Z0)
D_LO = (2.0 * TAU / XSTAR) ** 0.25
DSTAR = max(D_HI, D_LO)

def elementary(vals, k):
    e = [0.0] * (k + 1)
    e[0] = 1.0
    for x in vals:
        for j in range(k, 0, -1):
            e[j] += e[j-1] * x
    return e[k]

def gram_e(M, k):
    s = np.linalg.svd(M, compute_uv=False)
    vals = s*s
    return elementary(vals, k)

def dist_rank(M, k):
    s = np.linalg.svd(M, compute_uv=False)
    return math.sqrt(float(np.sum(s[k:]**2)))

# Exact integer Cauchy-Binet packet checks.
exact_packet_checks = 0
for seed in range(12):
    rr = np.random.default_rng(1000 + seed)
    W0 = sp.Matrix(rr.integers(-2, 3, size=(4, 4)).tolist())
    V0 = sp.Matrix(rr.integers(-2, 3, size=(4, 3)).tolist())
    B0 = W0 * W0.T
    trB = sp.trace(B0)
    Z = (trB**2 - sp.trace(B0*B0)) / 2
    H = B0*B0 - trB*B0 + Z*sp.eye(4)
    M0 = W0.row_join(V0)
    G0 = M0*M0.T
    E = sum(G0.extract(I, I).det() for I in sp.utilities.iterables.combinations(range(4), 3))
    EB = sum(B0.extract(I, I).det() for I in sp.utilities.iterables.combinations(range(4), 3))
    packet = EB + sp.trace(V0.T*H*V0)
    assert sp.simplify(E - packet) >= 0
    exact_packet_checks += 1

high_accept = 0
low_accept = 0
max_dist_ratio = 0.0
min_packet_slack = float("inf")
max_alpha_sum_err = 0.0
max_heavy_count = 0
min_low_heavy_slack = float("inf")
max_tail_ratio = 0.0

# High-Z near-rank-two cases.
for _ in range(5000):
    r = int(rng.integers(4, 9))
    nw = int(rng.integers(3, 8))
    nv = int(rng.integers(1, 7))
    U, _ = np.linalg.qr(rng.normal(size=(r, 2)))
    W = U @ rng.normal(size=(2, nw)) + 10**rng.uniform(-8, -5) * rng.normal(size=(r, nw))
    V = U @ rng.normal(size=(2, nv)) + 10**rng.uniform(-8, -5) * rng.normal(size=(r, nv))
    W *= math.sqrt((T0*(1.02 + 0.98*rng.random())) / float(np.sum(W*W)))
    V *= 0.25 + 0.75*rng.random()

    E = gram_e(np.concatenate([W, V], axis=1), 3)
    if not E < TAU:
        continue
    B = W @ W.T
    x = np.linalg.eigvalsh(B)
    x = np.maximum(x, 0.0)
    T = float(np.sum(x))
    Z = elementary(x, 2)
    if not Z >= Z0:
        continue

    H = B@B - T*B + Z*np.eye(r)
    EB = elementary(x, 3)
    packet = EB + float(np.trace(V.T @ H @ V))
    slack = E - packet
    min_packet_slack = min(min_packet_slack, slack)

    alpha = x*(T-x)/Z
    max_alpha_sum_err = max(max_alpha_sum_err, abs(float(np.sum(alpha))-2.0))
    heavy = int(np.sum(alpha > (2.0/3.0 + 1e-12)))
    max_heavy_count = max(max_heavy_count, heavy)
    assert heavy <= 2

    d = dist_rank(np.concatenate([W,V], axis=1), 2)
    max_dist_ratio = max(max_dist_ratio, d/DSTAR)
    assert slack >= -5e-6 * max(1.0, E, packet)
    assert d <= DSTAR + 2e-5
    high_accept += 1
    if high_accept >= 500:
        break

# Low-Z rank-one-dominant W cases.
for _ in range(5000):
    r = int(rng.integers(4, 9))
    nw = int(rng.integers(3, 8))
    nv = int(rng.integers(1, 7))
    u = rng.normal(size=r); u /= np.linalg.norm(u)
    v = rng.normal(size=r); v -= u*(u@v); v /= np.linalg.norm(v)
    W = np.outer(u, rng.normal(size=nw)) + 10**rng.uniform(-8, -5)*rng.normal(size=(r,nw))
    W *= math.sqrt((T0*(1.02 + 0.98*rng.random())) / float(np.sum(W*W)))
    V = np.outer(u, rng.normal(size=nv)) + np.outer(v, rng.normal(size=nv))
    V += 10**rng.uniform(-8,-5)*rng.normal(size=(r,nv))
    V *= 0.2 + 0.8*rng.random()

    M = np.concatenate([W,V], axis=1)
    E = gram_e(M, 3)
    if not E < TAU:
        continue
    B = W@W.T
    x = np.linalg.eigvalsh(B); x = np.maximum(x,0.0)
    Z = elementary(x,2)
    if not Z < Z0:
        continue

    Uw, sw, Vhw = np.linalg.svd(W, full_matrices=False)
    x1 = sw[0]**2
    low_slack = x1 - XSTAR
    min_low_heavy_slack = min(min_low_heavy_slack, low_slack)
    assert low_slack > -2e-5

    Wrot = W @ Vhw.T
    u1 = Uw[:,0]
    rest = np.concatenate([Wrot[:,1:], V], axis=1)
    Y = rest - np.outer(u1, u1@rest)
    ZY = gram_e(Y,2)
    assert E + 5e-6*max(1.0,E,x1*ZY) >= x1*ZY

    sy = np.linalg.svd(Y, compute_uv=False)**2
    tail = float(np.sum(sy[1:]))
    assert tail*tail <= 2.0*ZY + 5e-6*max(1.0,2.0*ZY)
    max_tail_ratio = max(max_tail_ratio, (tail*tail)/(2.0*ZY) if ZY>1e-14 else 0.0)

    d = dist_rank(M,2)
    max_dist_ratio = max(max_dist_ratio, d/DSTAR)
    assert d <= DSTAR + 2e-5
    low_accept += 1
    if low_accept >= 500:
        break

assert high_accept == 500
assert low_accept == 500
assert abs(D_HI-D_LO) < 5e-14

print("QFORM-MATCHING-IMAGE-TO-PHYSICAL-R2-LIFT-v1")
print(f"T0={T0:.15f}")
print(f"tau={TAU:.15f}")
print(f"z0={Z0:.15f}")
print(f"xstar={XSTAR:.15f}")
print(f"D_hi={D_HI:.15f}")
print(f"D_lo={D_LO:.15f}")
print(f"Dstar={DSTAR:.15f}")
print(f"sqrt2_Dstar={math.sqrt(2)*DSTAR:.15f}")
print(f"nondegenerate_product_floor={DSTAR*math.sqrt((T0-DSTAR**2)/2):.15f}")
print(f"exact_packet_checks={exact_packet_checks}")
print(f"high_Z_regressions={high_accept}")
print(f"low_Z_regressions={low_accept}")
print(f"max_alpha_sum_error={max_alpha_sum_err:.3e}")
print(f"max_heavy_count={max_heavy_count}")
print(f"min_packet_slack_float={min_packet_slack:.3e}")
print(f"min_low_heavy_slack={min_low_heavy_slack:.6f}")
print(f"max_tail_ratio={max_tail_ratio:.6f}")
print(f"max_observed_dist_over_Dstar={max_dist_ratio:.6f}")
print("STATUS=PASS")
