"""Recompute H, I, mean and H/(I-1) of fam.txt line 211 (n=18, 'PM_K33_plus_9_coins') with a plain Walsh-Hadamard transform.
Convention (theirs): bit x of the table integer set <=> f(x) = -1."""
import sys
import numpy as np

path = sys.argv[1]
line = open(path).read().splitlines()[210].split()
n, hx = int(line[0]), line[1]
T = int(hx, 16)
N = 1 << n
raw = T.to_bytes(N // 8, "little")
b = np.unpackbits(np.frombuffer(raw, dtype=np.uint8), bitorder="little")[:N]
f = 1.0 - 2.0 * b
a = f.copy()
h = 1
while h < N:
    a = a.reshape(-1, 2, h)
    a = np.stack([a[:, 0] + a[:, 1], a[:, 0] - a[:, 1]], axis=1).reshape(-1)
    h *= 2
c = a / N
w = c ** 2
size = np.array([bin(s).count("1") for s in range(N)], dtype=float)
nz = w > 0
H = float(-(w[nz] * np.log2(w[nz])).sum())
I = float((w * size).sum())
infl = [float(w[(np.arange(N) >> i) & 1 == 1].sum()) for i in range(n)]
print("n=%d mean=%.9f parseval=%.12f H=%.9f I=%.9f H/(I-1)=%.9f H/I=%.9f" % (n, c[0], w.sum(), H, I, H / (I - 1), H / I))
print("influences:", " ".join("%.4f" % x for x in infl))
# which inputs matter, and is it monotone in each coordinate?
for i in range(n):
    idx = np.arange(N)
    lo = idx[(idx >> i) & 1 == 0]
    d = b[lo | (1 << i)].astype(int) - b[lo].astype(int)
    print("  x%-2d up %d down %d" % (i, (d > 0).sum(), (d < 0).sum()))
