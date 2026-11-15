"""ro_vi.py - the entropy/influence constant of read-once formulas, by a two-variable Bellman iteration.

For a Boolean f with p = Pr[f true]: G = entropy (bits) of its non-empty Fourier weights divided by the variance,
J = total influence / variance.  For f = g1 AND g2 with independent g1, g2 of biases p1, p2 (p = p1 p2):
    w1 = p2 (1-p1)/(1-p), w2 = p1 (1-p2)/(1-p), w12 = (1-p1)(1-p2)/(1-p),
    G_f = H(w1, w2, w12) + Inf1 G_1 + Inf2 G_2,   J_f = Inf1 J_1 + Inf2 J_2,   Inf1 = (1-p1)/(1-p), Inf2 = (1-p2)/(1-p).
B_C(p) = sup over read-once formulas of bias p of G - C J satisfies
    B(p1 p2) >= H(w1,w2,w12) + Inf1 B(p1) + Inf2 B(p2),   B(1/2) >= -C (a variable),   B(p) = B(1-p) (negation),
and sup G/J over the class (the constant C_RO: G/J increases under composition, and H/I -> G/J) is the least C for
which B_C stays <= 0.  With --xor the gate g1 XOR g2 is allowed too.

The iteration starts from the variable alone and pulls: for a grid bias p and every grid p1 > p it uses p2 = p/p1
with B(p2) interpolated linearly in log-odds (an approximation: the numbers are estimates, not certificates).
usage: python ro_vi.py [--n 1201] [--span 20] [--xor 1] [--lo 4] [--hi 9] [--bis 22] [--sweeps 4000] [--dump FILE]
"""
import sys

import numpy as np


def opt(name, default, typ=float):
    return typ(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def ent3(a, b, c):
    out = np.zeros_like(a)
    for w in (a, b, c):
        with np.errstate(divide="ignore", invalid="ignore"):
            out -= np.where(w > 1e-300, w * np.log2(w), 0.0)
    return out


def build(n, span, xor):
    t = np.linspace(-span / 2, span / 2, n)
    p = 1.0 / (1.0 + 2.0 ** (-t))
    d = t[1] - t[0]
    K, I = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")     # target k, first input i
    gates = []
    # AND: p2 = p_k / p_i, needs p_i > p_k
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        p1 = p[I]; pk = p[K]
        p2 = pk / p1
        ok = (p2 < 1.0 - 1e-12) & (p2 > p[0]) & (p1 >= p2 - 1e-15)
        p2c = np.where(ok, p2, 0.5)
        x = (np.log2(p2c / (1 - p2c)) - t[0]) / d
        j0 = np.clip(np.floor(x).astype(int), 0, n - 2); fr = x - j0
        w1 = p2c * (1 - p1) / (1 - pk); w2 = p1 * (1 - p2c) / (1 - pk); w12 = (1 - p1) * (1 - p2c) / (1 - pk)
        gates.append((ok, ent3(w1, w2, w12), (1 - p1) / (1 - pk), (1 - p2c) / (1 - pk), j0, fr))
        if xor:
            # XOR: Pr[true] = p1 (1-p2) + p2 (1-p1) = pk  ->  p2 = (pk - p1) / (1 - 2 p1)
            den = 1 - 2 * p1
            p2 = np.where(np.abs(den) > 1e-9, (pk - p1) / den, -1.0)
            ok = (p2 > p[0]) & (p2 < p[-1]) & (p1 <= 0.5) & (p2 <= 0.5 + 1e-12) & (p1 <= p2 + 1e-15)
            p2c = np.where(ok, p2, 0.25)
            x = (np.log2(p2c / (1 - p2c)) - t[0]) / d
            j0 = np.clip(np.floor(x).astype(int), 0, n - 2); fr = x - j0
            v1 = 4 * p1 * (1 - p1); v2 = 4 * p2c * (1 - p2c); m1 = 1 - v1; m2 = 1 - v2
            var = 1 - m1 * m2
            w1 = v1 * m2 / var; w2 = m1 * v2 / var; w12 = v1 * v2 / var
            gates.append((ok, ent3(w1, w2, w12), v1 / var, v2 / var, j0, fr))
    return t, p, gates


def run(C, t, p, gates, sweeps, tol=1e-11):
    n = len(t)
    mid = n // 2
    B = np.full(n, -1e6)
    B[mid] = -C
    I = np.arange(n)[None, :]
    arg = None
    for s in range(sweeps):
        new = B.copy()
        for g, (ok, H, a1, a2, j0, fr) in enumerate(gates):
            b2 = B[j0] * (1 - fr) + B[j0 + 1] * fr
            v = np.where(ok, H + a1 * B[I] + a2 * b2, -np.inf)
            best = v.max(axis=1)
            new = np.maximum(new, best)
        new = np.maximum(new, new[::-1])
        new[mid] = max(new[mid], -C)
        if new.max() > 1e-9:
            return 1, s, new
        if np.abs(new - B).max() < tol:
            return 0, s, new
        B = new
    return 2, sweeps, B


def main():
    n = opt("--n", 1201, int); span = opt("--span", 20.0); xor = opt("--xor", 0, int)
    lo = opt("--lo", 4.0); hi = opt("--hi", 9.0); bis = opt("--bis", 22, int); sweeps = opt("--sweeps", 4000, int)
    t, p, gates = build(n, span, xor)
    print("grid %d points, log-odds span %.1f, gates: AND/OR/NOT%s" % (n, span, " + XOR" if xor else ""), flush=True)
    last = None
    for it in range(bis):
        C = 0.5 * (lo + hi)
        code, s, B = run(C, t, p, gates, sweeps)
        print("C %.9f  %s after %d sweeps  B(1/2) %.9f  max B %.3e" %
              (C, ("DIVERGES (C too small)", "converged", "undecided")[1 if code == 0 else (0 if code == 1 else 2)],
               s, B[n // 2], B.max()), flush=True)
        if code == 1:
            lo = C
        else:
            hi = C; last = (C, B)
    print("C_RO estimate: between %.9f and %.9f" % (lo, hi))
    if last:
        C, B = last
        print("at C = %.9f:  B(1/2) + C = %.3e" % (C, B[n // 2] + C))
        for q in (0.5, 0.45, 0.4, 0.382, 1 / 3, 0.3, 0.25, 0.2, 0.125, 0.0625, 0.01, 0.001):
            x = np.log2(q / (1 - q))
            print("  p %.4f  W = -B = %.6f" % (q, -np.interp(x, t, B)))
        if "--dump" in sys.argv:
            np.savetxt(opt("--dump", "", str), np.column_stack([t, -B]), fmt="%.12f")


if __name__ == "__main__":
    main()
