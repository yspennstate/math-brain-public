"""Numerical checks for "The risk tail of minimum-norm ReLU interpolation on the sphere".

1. Lemma 3.2, the tent identity sigma(s+t) + sigma(s-t) - 2 sigma(s) = (|t| - |s|)_+.
2. E sigma(u.X)^2 = 1/(2d) for X uniform on the sphere (Monte Carlo).
3. Proposition 3.3: the tents interpolate, and their cost is at most H K_{n,d} / delta.
4. Lemma 4.2: the competitor interpolates, and its cost is at most 2/s + 2 + Lambda (H + 2).
5. Theorem 3.4: E sin(Theta)^(-2r) equals the beta-function ratio, and (d-2)/(d-3) at r = 1.

Run: python check_tents.py   (numpy and scipy; about a minute)
"""
import math
import numpy as np
from scipy import integrate, special

rng = np.random.default_rng(20261115)
relu = lambda v: np.maximum(v, 0.0)
fails = 0


def check(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + (" " + detail if detail else ""))
    fails += 0 if ok else 1


def sphere(n, d):
    g = rng.standard_normal((n, d))
    return g / np.linalg.norm(g, axis=1, keepdims=True)


# 1. tent identity
s, t = rng.uniform(-3, 3, 10**6), rng.uniform(-3, 3, 10**6)
err = np.abs(relu(s + t) + relu(s - t) - 2 * relu(s) - relu(np.abs(t) - np.abs(s))).max()
check("tent identity on 1e6 random (s, t)", err < 1e-12, f"max error {err:.1e}")

# 2. second moment of one atom
for d in (2, 3, 5, 10):
    X = sphere(400000, d)
    u = sphere(1, d)[0]
    m = (relu(X @ u) ** 2).mean()
    check(f"E sigma(u.X)^2 = 1/(2d), d={d}", abs(m - 1 / (2 * d)) < 5e-3 / d, f"{m:.5f} vs {1/(2*d):.5f}")


# 3. tents (Proposition 3.3)
def tents(x, y):
    n, d = x.shape
    C = 8 * (n - 1) * math.sqrt(d - 1)
    S = np.sqrt(np.clip(1 - (x @ x.T) ** 2, 0, None))
    np.fill_diagonal(S, np.inf)
    delta = S.min()
    units, cost = [], 0.0
    for i in range(n):
        di = S[i].min()
        for _ in range(10000):  # Lemma 3.1 holds with probability > 1/2
            g = rng.standard_normal(d)
            g -= (g @ x[i]) * x[i]
            z = g / np.linalg.norm(g)
            if all(abs(z @ x[j]) >= S[i, j] / C for j in range(n) if j != i):
                break
        else:
            raise RuntimeError("no direction found")
        L = C / di
        for c, w in ((y[i], L * z + x[i]), (y[i], L * z - x[i]), (-2 * y[i], L * z)):
            units.append((c, w))
            cost += abs(c) * np.linalg.norm(w)
    F = lambda P: sum(c * relu(P @ w) for c, w in units)
    K = n * (2 + 32 * (n - 1) * math.sqrt(d - 1))
    return F, cost, K, delta


worst = 0.0
ok_interp = True
for trial in range(300):
    n, d = int(rng.integers(2, 9)), int(rng.integers(2, 7))
    x = sphere(n, d)
    y = rng.uniform(-1, 1, n)
    F, cost, K, delta = tents(x, y)
    ok_interp &= np.abs(F(x) - y).max() < 1e-8
    worst = max(worst, cost / (K / delta))
check("tents interpolate (300 random configurations)", ok_interp)
check("tent cost <= H K_{n,d}/delta", worst <= 1.0, f"largest ratio {worst:.3f}")


# 4. competitor (Lemma 4.2)
def competitor(theta, Z, tau):
    a, b = math.cos(theta / 2), math.sin(theta / 2)
    sn = math.sin(theta)
    d = Z.shape[1]
    e1, e2 = np.eye(d)[0], np.eye(d)[1]
    x1, x2 = a * e1 + b * e2, a * e1 - b * e2
    v = b * e1 - a * e2
    F0 = lambda P: relu(P @ e1) / a - relu(P @ v) / (a * b)
    k = Z.shape[0]
    for _ in range(1000):
        U = sphere(k, d)
        U[:, 0] = -np.abs(U[:, 0]) - 0.3
        U /= np.linalg.norm(U, axis=1, keepdims=True)
        M = relu(Z @ U.T)  # M[i, j] = sigma(u_j . z_i)
        if abs(np.linalg.det(M)) > 1e-3 and (U @ x1).max() < 0 and (U @ x2).max() < 0:
            break
    Minv = np.linalg.inv(M)
    h = tau - F0(Z)
    c = Minv @ h
    F = lambda P: F0(P) + relu(P @ U.T) @ c
    cost = 1 / a + 1 / (a * b) + np.abs(c).sum()
    Lam = np.abs(Minv).sum()
    P = np.vstack([x1, x2, Z])
    target = np.concatenate([[1.0, -1.0], tau])
    return np.abs(F(P) - target).max(), cost, 2 / sn + 2 + Lam * (np.abs(tau).max() + 2)


ok_i, ok_c = True, True
for trial in range(200):
    d = int(rng.integers(2, 6))
    k = int(rng.integers(1, min(d, 4) + 1)) if d > 2 else 1
    Z = sphere(k, d)
    Z[:, 1] = np.abs(Z[:, 1]) + 0.3  # one side of e2-perp, margin kappa
    Z /= np.linalg.norm(Z, axis=1, keepdims=True)
    kappa = Z[:, 1].min()
    theta = min(0.5, kappa / 2) * rng.uniform(0.01, 1)
    tau = rng.uniform(-1, 1, k)
    e, cost, bound = competitor(theta, Z, tau)
    ok_i &= e < 1e-7
    ok_c &= cost <= bound + 1e-9
check("competitor interpolates (200 configurations)", ok_i)
check("competitor cost <= 2/s + 2 + Lambda (H + 2)", ok_c)

# 5. beta ratios
for d in (2, 3, 4, 5, 8):
    Cd = math.gamma(d / 2) / (math.sqrt(math.pi) * math.gamma((d - 1) / 2))
    for r in (0.25, 0.4 * (d - 1), 1.0):
        if not r < (d - 1) / 2:
            continue
        num, _ = integrate.quad(lambda th: Cd * math.sin(th) ** (d - 2 - 2 * r), 0, math.pi, limit=200)
        ratio = special.beta((d - 1 - 2 * r) / 2, 0.5) / special.beta((d - 1) / 2, 0.5)
        check(f"E sin^-2r Theta, d={d}, r={r:.2f}", abs(num - ratio) < 1e-6 * ratio, f"{num:.6f} vs {ratio:.6f}")
    if d >= 4:
        ratio = special.beta((d - 3) / 2, 0.5) / special.beta((d - 1) / 2, 0.5)
        check(f"(d-2)/(d-3) at r=1, d={d}", abs(ratio - (d - 2) / (d - 3)) < 1e-12)

print("ALL PASS" if fails == 0 else f"{fails} FAILED")
raise SystemExit(1 if fails else 0)
