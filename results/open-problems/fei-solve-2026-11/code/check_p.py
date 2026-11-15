"""Second round of checks on every Boolean function of n variables (default 4), or a random sample.

g_S = D_S f as a function of the coordinates outside S;  mu = (E g_S)^2, up = E g_S^2, abs1 = E|g_S|, p = P[g_S != 0].
A1 = sum mu log2(1/abs1),  A = sum mu log2(1/up),  Gamma = sum mu log2(abs1/|fhat|),  P = sum mu log2(1/p),
Q  = sum mu log2(up/abs1^2),  B = sum mu log2(up/mu),  W_d = level weight,  M_d = sum_{|S|=d} up(S) = E C(|U|,d).
Claims checked:
  (a) H = 2 A1 + 2 Gamma (identity)            (b) A1 <= A <= 2 A1
  (c) B <= A + 2 Gamma                          (d) P <= Q <= P + I - Var, B = Q + 2 Gamma
  (e) isoperimetric step: 2 p(S) log2(1/p(S)) <= sum_{j not in S} p(S + j)  for every S
  (f) level form: B <= sum_d W_d log2(M_d / W_d)
usage: python check_p.py [n] [sample]
"""
import sys
import numpy as np

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N = 1 << n
sample = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rng = np.random.default_rng(2)
if sample:
    F = rng.integers(0, 2, size=(sample, N), dtype=np.int8) * 2 - 1
else:
    idx = np.arange(1 << (N - 1), dtype=np.int64)      # f(0) = +1 half; f -> -f changes nothing
    F = (1 - 2 * ((idx[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.int8)
    F = F[:, ::-1].copy()                               # put the fixed +1 at input 0
F = F.astype(np.float64)
M = F.shape[0]
pc = np.array([bin(s).count("1") for s in range(N)])


def partial(Fa, S):
    a = Fa.copy()
    for i in range(n):
        if S >> i & 1:
            h = 1 << i
            lo = np.array([x for x in range(N) if not x & h])
            u, v = a[:, lo], a[:, lo | h]
            a[:, lo] = (u + v) / 2
            a[:, lo | h] = (u - v) / 2
    cols = np.array([x for x in range(N) if (x & S) == S])
    return a[:, cols]


mu = np.zeros((M, N)); up = np.zeros((M, N)); ab = np.zeros((M, N)); p = np.zeros((M, N))
for S in range(N):
    c = partial(F, S)
    mu[:, S] = c.mean(axis=1) ** 2
    up[:, S] = (c ** 2).mean(axis=1)
    ab[:, S] = np.abs(c).mean(axis=1)
    p[:, S] = (np.abs(c) > 1e-12).mean(axis=1)


def wsum(term):
    out = np.zeros(M)
    for S in range(N):
        nz = mu[:, S] > 1e-15
        out[nz] += mu[nz, S] * term(S, nz)
    return out


H = wsum(lambda S, nz: np.log2(1 / mu[nz, S]))
A = wsum(lambda S, nz: np.log2(1 / up[nz, S]))
A1 = wsum(lambda S, nz: np.log2(1 / ab[nz, S]))
B = wsum(lambda S, nz: np.log2(up[nz, S] / mu[nz, S]))
G = wsum(lambda S, nz: np.log2(ab[nz, S] / np.sqrt(mu[nz, S])))
P = wsum(lambda S, nz: np.log2(1 / p[nz, S]))
Q = wsum(lambda S, nz: np.log2(up[nz, S] / ab[nz, S] ** 2))
I = (mu * pc[None, :]).sum(axis=1)
var = 1 - mu[:, 0]
print("n", n, "functions", M)
print("(a) max |H - 2A1 - 2Gamma|", np.abs(H - 2 * A1 - 2 * G).max())
print("(b) max A1 - A", (A1 - A).max(), " max A - 2A1", (A - 2 * A1).max())
print("(c) max B - (A + 2Gamma)", (B - A - 2 * G).max())
print("(d) max P - Q", (P - Q).max(), " max Q - (P + I - Var)", (Q - P - I + var).max(), " max |B - Q - 2Gamma|", np.abs(B - Q - 2 * G).max())
worst = -1e9
for S in range(N):
    rhs = np.zeros(M)
    for j in range(n):
        if not S >> j & 1:
            rhs += p[:, S | (1 << j)]
    ps = p[:, S]
    lhs = np.where(ps > 0, 2 * ps * np.log2(1 / np.where(ps > 0, ps, 1)), 0)
    worst = max(worst, (lhs - rhs).max())
print("(e) max 2p log(1/p) - sum_j p(S+j)", worst)
lev = np.zeros(M)
for d in range(n + 1):
    cols = np.where(pc == d)[0]
    W = mu[:, cols].sum(axis=1)
    Md = up[:, cols].sum(axis=1)
    nz = W > 1e-15
    lev[nz] += W[nz] * np.log2(Md[nz] / W[nz])
print("(f) max B - level form", (B - lev).max(), " max level form / I", np.where(I > 1e-12, lev / np.where(I > 1e-12, I, 1), 0).max())
ok = I > 1e-12
for name, v in (("A1", A1), ("P", P), ("Q", Q), ("Gamma", G), ("A", A), ("B", B), ("H", H)):
    r = np.where(ok, v / np.where(ok, I, 1), -1)
    k = int(r.argmax())
    print("sup %s/I %.6f (H %.4f A %.4f A1 %.4f B %.4f Gamma %.4f P %.4f Q %.4f I %.4f)" % (name, r[k], H[k], A[k], A1[k], B[k], G[k], P[k], Q[k], I[k]))
bal = (mu[:, 0] < 1e-12) & (I > 1 + 1e-9)
if bal.any():
    for name, v in (("A1", A1), ("P", P), ("Q", Q), ("Gamma", G), ("A", A), ("B", B), ("H", H)):
        r = np.where(bal, v / np.where(bal, I - 1, 1), -1)
        k = int(r.argmax())
        print("balanced sup %s/(I-1) %.6f (H %.4f A %.4f A1 %.4f B %.4f Gamma %.4f P %.4f Q %.4f I %.4f)" % (name, r[k], H[k], A[k], A1[k], B[k], G[k], P[k], Q[k], I[k]))
