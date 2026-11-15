"""Recompute agent's n=7 census leaders. Table = f0 | (f1 << 64) (f1 is the half with the top input = 1); bit set <=> f = -1.
E_i = sum_{T not containing i} Phi(fhat(T)^2, fhat(T+i)^2), Phi(a,b) = eta(a)+eta(b)-eta(a+b), eta(x) = -x log2 x."""
import numpy as np

n, N = 7, 128
leaders = [
    ("overall sup Q0", "fca8f0a0cc880000", "0000000000000000", 3.164564560463, "Q0"),
    ("balanced sup Q0", "fafafaf0eaeac0c0", "eae8eac0eac8c0c0", 1.901840492556, "Q0"),
    ("|mean|<=1/8 sup Q0", "fcfcf8f8eccca888", "a888a888a888a888", 2.222283760112, "Q0"),
    ("balanced max min E/Inf", "fffffffeeac8e000", "eac8e000eac8e000", 1.778965422289, "min"),
]
def eta(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = -x[m] * np.log2(x[m])
    return out
size = np.array([bin(s).count("1") for s in range(N)])
for name, h1, h0, claim, kind in leaders:
    T = int(h0, 16) | (int(h1, 16) << 64)
    b = np.array([(T >> x) & 1 for x in range(N)])
    f = 1.0 - 2.0 * b
    a = f.copy(); h = 1
    while h < N:
        a = a.reshape(-1, 2, h); a = np.stack([a[:, 0] + a[:, 1], a[:, 0] - a[:, 1]], axis=1).reshape(-1); h *= 2
    w = (a / N) ** 2
    H = float(eta(w[1:]).sum() + 0)            # entropy over all S incl. empty? use standard H over all S
    H_all = float(eta(w).sum())
    I = float((w * size).sum())
    E = []; Inf = []
    for i in range(n):
        S0 = np.array([s for s in range(N) if not (s >> i) & 1])
        A, B = w[S0], w[S0 | (1 << i)]
        E.append(float((eta(A) + eta(B) - eta(A + B)).sum()))
        Inf.append(float(B.sum()))
    mono = all(((b[[x | (1 << i) for x in range(N) if not (x >> i) & 1]] - b[[x for x in range(N) if not (x >> i) & 1]]) >= 0).all() for i in range(n))
    Q0 = sum(E) / I
    mn = min(e / v for e, v in zip(E, Inf) if v > 0)
    val = Q0 if kind == "Q0" else mn
    print("%-24s mean=%+.6f H=%.9f I=%.6f Q0=%.12f minE/Inf=%.12f monotone=%s | claim %.12f diff %.1e"
          % (name, a[0] / N, H_all, I, Q0, mn, mono, claim, val - claim))
