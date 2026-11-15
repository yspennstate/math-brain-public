"""Check the three-way split of the spectral entropy on every Boolean function of n variables (default 4).

mu(S) = fhat(S)^2, c_S(z) = S-coefficient of f with the coordinates outside S fixed to z.
up(S) = E_z c_S(z)^2,  fhat(S) = E_z c_S(z),  abs1(S) = E_z |c_S(z)|,  p(S) = P_z[c_S(z) != 0].
A     = sum mu log2(1/up)                (containment: an independent spectral sample contains S)
B     = sum mu log2(up/mu)               (dispersion of the restricted coefficient)
Gamma = sum mu log2(abs1/|fhat(S)|)      (sign cancellation)
P     = sum mu log2(1/p)
Claims checked:  H = A + B;  A <= B + 2I - 2Var (Theorem 1);  Gamma <= B/2;  P <= A;
                 B <= (I - Var) + P + 2 Gamma  <= (I - Var) + A + 2 Gamma   (Proposition 4).
usage: python check_gamma.py [n] [sample]
"""
import sys
import numpy as np

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N = 1 << n
sample = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rng = np.random.default_rng(1)
if sample:
    F = rng.integers(0, 2, size=(sample, N), dtype=np.int8) * 2 - 1
else:
    idx = np.arange(1 << N, dtype=np.int64)
    F = (1 - 2 * ((idx[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.int8)
F = F.astype(np.float64)
M = F.shape[0]
pc = np.array([bin(s).count("1") for s in range(N)])


def partial(Fa, S):
    """c_S(z) for every z: transform only the coordinates in S, read the all-ones pattern on S."""
    a = Fa.copy()
    for i in range(n):
        if S >> i & 1:
            h = 1 << i
            lo = np.array([x for x in range(N) if not x & h])
            u, v = a[:, lo], a[:, lo | h]
            a[:, lo] = (u + v) / 2
            a[:, lo | h] = (u - v) / 2
    cols = np.array([x for x in range(N) if (x & S) == S])
    return a[:, cols]          # one column per z (2^(n-|S|) of them)


H = np.zeros(M); A = np.zeros(M); B = np.zeros(M); G = np.zeros(M); P = np.zeros(M); I = np.zeros(M); mu0 = np.zeros(M)
tot = np.zeros(M)
for S in range(N):
    c = partial(F, S)
    m = c.mean(axis=1) ** 2
    up = (c ** 2).mean(axis=1)
    ab = np.abs(c).mean(axis=1)
    p = (c != 0).mean(axis=1)
    nz = m > 0
    tot += m
    I += pc[S] * m
    if S == 0:
        mu0 = m.copy()
    H[nz] += m[nz] * np.log2(1 / m[nz])
    A[nz] += m[nz] * np.log2(1 / up[nz])
    B[nz] += m[nz] * np.log2(up[nz] / m[nz])
    G[nz] += m[nz] * np.log2(ab[nz] / np.sqrt(m[nz]))
    P[nz] += m[nz] * np.log2(1 / p[nz])
var = 1 - mu0
ok = I > 1e-12
print("n", n, "functions", M, "parseval err", np.abs(tot - 1).max())
print("max |H-(A+B)|", np.abs(H - A - B).max())
print("Thm1  max A-(B+2I-2Var)", (A - (B + 2 * I - 2 * var)).max())
print("max Gamma - B/2", (G - B / 2).max())
print("max P - A", (P - A).max())
print("Prop4 max B-((I-Var)+P+2Gamma)", (B - ((I - var) + P + 2 * G)).max())
for name, v in (("A", A), ("B", B), ("Gamma", G), ("P", P), ("H", H)):
    r = np.where(ok, v / np.where(ok, I, 1), -1)
    k = int(r.argmax())
    print("sup %s/I %.6f at row %d (H %.4f A %.4f B %.4f Gamma %.4f P %.4f I %.4f var %.4f)" % (name, r[k], k, H[k], A[k], B[k], G[k], P[k], I[k], var[k]))
bal = (mu0 < 1e-12) & (I > 1 + 1e-9)
if bal.any():
    for name, v in (("A", A), ("B", B), ("Gamma", G), ("H", H)):
        r = np.where(bal, v / np.where(bal, I - 1, 1), -1)
        k = int(r.argmax())
        print("balanced sup %s/(I-1) %.6f at row %d (H %.4f A %.4f B %.4f Gamma %.4f I %.4f)" % (name, r[k], k, H[k], A[k], B[k], G[k], I[k]))
