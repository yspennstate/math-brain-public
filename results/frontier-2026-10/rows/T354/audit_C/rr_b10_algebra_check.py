"""Brute-force check of the combinatorial identities in remainder_rr.py (agent C, 20 Oct 2026, T354 RR b1=0 audit 2).
Over ALL permutations of a small n, at each position p: E[g_a Z-part] (first order), E[g A^2] (current-epoch second moment, Q2),
and the max of |earlier-epoch weighted sum| against beta^s (1 - beta^(n-1)) Smax. Random data, not the test model."""
import itertools, numpy as np
rng = np.random.default_rng(7)
n, b = 6, 0.8
g = rng.normal(size=n) + 0.3
V = np.mean(g * g); Z = g * g - V; C = np.mean(g ** 3) - np.mean(g) * V
M00 = np.mean(g * Z * Z)
M0l = np.mean([g[a] * Z[a] * Z[c] for a, c in itertools.permutations(range(n), 2)])
Mjj = np.mean([g[a] * Z[c] * Z[c] for a, c in itertools.permutations(range(n), 2)])
Mjl = np.mean([g[a] * Z[c] * Z[e] for a, c, e in itertools.permutations(range(n), 3)])
perms = list(itertools.permutations(range(n)))
worst1 = worst2 = 0.0
for p in range(n):
    w = b ** np.arange(p + 1)
    s1, s2 = w[1:].sum(), (w[1:] ** 2).sum()
    f1 = C * (1 - s1 / (n - 1))
    f2 = M00 + 2 * s1 * M0l + s2 * Mjj + (s1 * s1 - s2) * Mjl
    e1 = e2 = 0.0
    for P in perms:              # P[p] is the current sample, P[p-j] the sample j steps back
        A = sum(w[j] * Z[P[p - j]] for j in range(p + 1))
        e1 += g[P[p]] * A; e2 += g[P[p]] * A * A
    e1 /= len(perms); e2 /= len(perms)
    worst1 = max(worst1, abs(e1 - f1)); worst2 = max(worst2, abs(e2 - f2))
    print("p %d  first: brute %.12f formula %.12f   second: brute %.12f formula %.12f" % (p, e1, f1, e2, f2))
print("max abs diff first %.2e second %.2e" % (worst1, worst2))
Smax = Z[Z > 0].sum(); wf = b ** np.arange(n)
mx = max(abs(np.dot(wf, Z[list(P)])) for P in perms)
print("earlier epoch (s=0): max |sum| over perms %.9f, bound (1-b^(n-1)) Smax %.9f, Smax = sum|Z|/2: %s" % (mx, (1 - b ** (n - 1)) * Smax, np.isclose(Smax, np.abs(Z).sum() / 2)))
