"""Exact forms of the step cost at one coordinate (FLOW 12(w) item 4 and 12(x)).

For f = g + x_i h (g = E_i f, h = D_i f, both functions of the other variables), p_T = ghat(T)^2, q_T = hhat(T)^2,
delta = Inf_i = sum q, rho_g = p/(1-delta), rho_h = q/delta, nu = p + q (the law of U - i):

  (A) information form   E_i = h2(delta) - (1-delta) D(rho_g || nu) - delta D(rho_h || nu)
  (B) angle form         with a = f0hat(T), b = f1hat(T), m = (a^2+b^2)/2, s = 2ab/(a^2+b^2), c = (a^2-b^2)/(a^2+b^2):
                         E_i = sum_T m h2((1+s)/2),  J_i = sum_T m (1 - h2((1+c)/2)),  Inf_i = (1/2) sum_T m (1 - s)
  (C) sandwich           delta E_{rho_h}[log2(p/q)]_+ <= E_i <= delta (1/ln 2 + 1) + delta E_{rho_h}[log2(p/q)]_+
  (D) convolution        ghat * hhat = 0 (g h = 0 pointwise), ghat * ghat + hhat * hhat = delta_empty

Then a table: where the rho_h mass sits by the size of log2(p/q), for a few named functions.

Usage: python step_info.py [seed]
"""
import sys
import numpy as np
from rand_restrict_identity import wht, ent
from relative_step import steps, rand_dnf


def h2(x):
    x = np.clip(np.asarray(x, dtype=np.float64), 0.0, 1.0)
    out = np.zeros_like(x)
    ok = (x > 0) & (x < 1)
    out[ok] = -x[ok] * np.log2(x[ok]) - (1 - x[ok]) * np.log2(1 - x[ok])
    return out


def kl(r, v):
    ok = r > 1e-300
    return float((r[ok] * np.log2(r[ok] / v[ok])).sum())


def split(f, n, i):
    idx = np.arange(1 << n)
    lo = idx[(idx >> i) & 1 == 0]
    f0, f1 = f[lo], f[lo | (1 << i)]
    return f0, f1


def forms(f, n, i):
    f0, f1 = split(f, n, i)
    a, b = wht(f0), wht(f1)
    g, h = (f0 + f1) / 2, (f0 - f1) / 2
    p, q = wht(g) ** 2, wht(h) ** 2
    delta = float(q.sum())
    nu = p + q
    e_direct = ent(np.concatenate((p, q))) - ent(nu)
    j_direct = ent(nu) - 0.5 * ent(a ** 2) - 0.5 * ent(b ** 2)
    out = {"delta": delta, "E": e_direct, "J": j_direct}
    if delta < 1e-15:
        return out
    out["A"] = float(h2(delta)) - (1 - delta) * kl(p / (1 - delta), nu) - delta * kl(q / delta, nu) if delta < 1 else 0.0
    m = (a ** 2 + b ** 2) / 2
    ok = m > 1e-300
    s = np.zeros_like(m)
    c = np.zeros_like(m)
    s[ok] = a[ok] * b[ok] / m[ok]
    c[ok] = (a[ok] ** 2 - b[ok] ** 2) / (2 * m[ok])
    out["B_E"] = float((m * h2((1 + s) / 2)).sum())
    out["B_J"] = float((m * (1 - h2((1 + c) / 2))).sum())
    out["B_inf"] = float(0.5 * (m * (1 - s)).sum())
    okq = q > 1e-300
    lr = np.full_like(q, -np.inf)
    both = okq & (p > 1e-300)
    lr[both] = np.log2(p[both] / q[both])
    pos = np.where(lr > 0, lr, 0.0)
    out["C_low"] = float((q * pos).sum())
    out["C_high"] = delta * (1 / np.log(2) + 1) + out["C_low"]
    # (D): convolution over the group of subsets = pointwise product in real space
    out["D_gh"] = float(np.abs(g * h).max())
    out["D_sq"] = float(np.abs(g * g + h * h - 1).max())
    out["lr"] = lr
    out["q"] = q
    return out


def tribes(m, w):
    n = m * w
    idx = np.arange(1 << n)
    val = np.zeros(1 << n, dtype=bool)
    for t in range(m):
        mask = ((1 << w) - 1) << (t * w)
        val |= (idx & mask) == mask
    return np.where(val, -1.0, 1.0), n


def maj(n):
    idx = np.arange(1 << n)
    pc = np.zeros(1 << n)
    for j in range(n):
        pc += (idx >> j) & 1
    return np.where(pc > n / 2, -1.0, 1.0), n


def pendant(k):
    """x_1 unless x_2..x_{k+1} are all ones, then x_1 AND x_{k+2} (coordinate k+2 has influence 2^-(k+1))."""
    n = k + 2
    idx = np.arange(1 << n)
    x1 = (idx & 1) == 1
    allk = ((idx >> 1) & ((1 << k) - 1)) == (1 << k) - 1
    last = ((idx >> (k + 1)) & 1) == 1
    val = np.where(allk, x1 & last, x1)
    return np.where(val, -1.0, 1.0), n


def table(name, f, n, coords):
    edges = [(-np.inf, 0.0), (0.0, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0), (8.0, np.inf)]
    for i in coords:
        r = forms(f, n, i)
        d = r["delta"]
        if d < 1e-15:
            print(f"  {name} i={i}: influence 0")
            continue
        lr, q = r["lr"], r["q"]
        parts = []
        for lo, hi in edges:
            sel = (lr > lo) & (lr <= hi) if np.isfinite(lo) else (lr <= hi)
            parts.append(f"{q[sel].sum() / d:.3f}")
        print(f"  {name} i={i}: Inf {d:.5f}  E/Inf {r['E'] / d:.4f}  J/Inf {r['J'] / d:.4f}  log2(1/Inf) {np.log2(1 / d):.3f}"
              f"  E_rho_h[log2(p/q)]_+ {r['C_low'] / d:.4f}   rho_h mass by log2(p/q) in (-inf,0],(0,1],(1,2],(2,4],(4,8],(8,inf): "
              + " ".join(parts))


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = np.random.default_rng(seed)
    worst = {"A": 0.0, "B_E": 0.0, "B_J": 0.0, "B_inf": 0.0, "C": 0.0, "D": 0.0}
    count = 0
    fs = []
    for n in (5, 6, 7, 8):
        for _ in range(30):
            fs.append((rng.choice([-1.0, 1.0], size=1 << n), n))
        for _ in range(30):
            w = int(rng.integers(2, 4))
            fs.append((rand_dnf(n, w, int(rng.integers(2, 2 ** w + 3)), rng, monotone=bool(rng.integers(2)))[0], n))
    for f, n in fs:
        f = np.asarray(f, dtype=np.float64)
        for i in range(n):
            r = forms(f, n, i)
            if r["delta"] < 1e-15 or r["delta"] > 1 - 1e-15:
                continue
            count += 1
            worst["A"] = max(worst["A"], abs(r["A"] - r["E"]))
            worst["B_E"] = max(worst["B_E"], abs(r["B_E"] - r["E"]))
            worst["B_J"] = max(worst["B_J"], abs(r["B_J"] - r["J"]))
            worst["B_inf"] = max(worst["B_inf"], abs(r["B_inf"] - r["delta"]))
            worst["C"] = max(worst["C"], r["C_low"] - r["E"], r["E"] - r["C_high"])
            worst["D"] = max(worst["D"], r["D_gh"], r["D_sq"])
    print(f"{count} (function, coordinate) pairs, seed {seed}")
    print("largest |A - E|, |B_E - E|, |B_J - J|, |B_inf - Inf|:",
          f"{worst['A']:.2e} {worst['B_E']:.2e} {worst['B_J']:.2e} {worst['B_inf']:.2e}")
    print(f"largest violation of the sandwich (C) (<= 0 means none): {worst['C']:.2e};  (D) residual {worst['D']:.2e}")
    print("where the rho_h mass sits:")
    for (m, w) in ((3, 3), (4, 3), (3, 4), (2, 6)):
        f, n = tribes(m, w)
        table(f"tribes {m}x{w}", f, n, [0])
    for n in (9, 11, 13):
        f, n = maj(n)
        table(f"maj {n}", f, n, [0])
    for k in (3, 5, 7, 9):
        f, n = pendant(k)
        table(f"pendant k={k}", f, n, [0, 1, n - 1])
    f = rng.choice([-1.0, 1.0], size=1 << 12)
    table("random n=12", f, 12, [0])


if __name__ == "__main__":
    main()
