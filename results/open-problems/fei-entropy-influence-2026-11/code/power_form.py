"""The power form of the erasure sum fails on balanced monotone towers.

For a Boolean f put  S_i(f) = sum_{U containing i} |fhat(U)| |fhat(U - i)|  and  r_i(f) = S_i(f) / Inf_i(f).
Since log2(1+x) <= (2 / (e ln 2)) sqrt(x), a bound  sum_i S_i <= C I  would imply FEI. It is false:
for f = F(psi, ..., psi) with psi balanced, and i the coordinate at inner position i of block b,
    r(f) = r_i(psi) + (|psihat({i})| / Inf_i(psi)) r_b(F),
and |psihat({i})| = Inf_i(psi) for monotone psi, so a balanced monotone tower of depth L has r = L r(F)
whenever r(F) > 0.

This script checks the composition formula by direct transforms: a balanced monotone, not self-dual base on
four variables, composed with itself (16 variables).
"""
import numpy as np


def wht(v):
    v = np.array(v, dtype=np.float64)
    n = v.size.bit_length() - 1
    h = 1
    while h < v.size:
        v = v.reshape(-1, 2, h)
        v = np.concatenate((v[:, 0, :] + v[:, 1, :], v[:, 0, :] - v[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return v / (1 << n)


def ratios(f, n):
    fh = wht(f)
    idx = np.arange(1 << n)
    out = []
    for i in range(n):
        up = idx[(idx >> i) & 1 == 1]
        s = float(np.abs(fh[up] * fh[up ^ (1 << i)]).sum())
        inf = float((fh[up] ** 2).sum())
        out.append((s, inf, s / inf if inf > 0 else float("nan"), abs(float(fh[1 << i]))))
    return out, float(fh[0])


def base():
    # true set: every set of size >= 3, and the pairs {0,1}, {2,3}, {0,2}; bit j of x set = variable j true
    f = np.ones(16)
    for x in range(16):
        pc = bin(x).count("1")
        if pc >= 3 or x in (0b0011, 0b1100, 0b0101):
            f[x] = -1.0
    return f


def compose(F, k, psi, m):
    n = k * m
    x = np.arange(1 << n)
    y = np.zeros_like(x)
    for j in range(k):
        blk = (x >> (j * m)) & ((1 << m) - 1)
        y |= (psi[blk] < 0).astype(np.int64) << j
    return F[y]


def main():
    F = base()
    r1, mean = ratios(F, 4)
    print("base: mean %.6f" % mean)
    for i, (s, inf, r, a) in enumerate(r1):
        print("  coordinate %d  S %.6f  Inf %.6f  r %.6f  |fhat({i})| %.6f" % (i, s, inf, r, a))
    f2 = compose(F, 4, F, 4)
    r2, mean2 = ratios(f2, 16)
    print("depth two: mean %.6f" % mean2)
    worst = 0.0
    for b in range(4):
        for i in range(4):
            s, inf, r, a = r2[b * 4 + i]
            pred = r1[i][2] + (r1[i][3] / r1[i][1]) * r1[b][2]
            worst = max(worst, abs(pred - r))
            print("  block %d inner %d  r %.6f  predicted %.6f" % (b, i, r, pred))
    print("worst |direct - formula| = %.3e" % worst)
    tot1 = sum(s for s, _, _, _ in r1) / sum(inf for _, inf, _, _ in r1)
    tot2 = sum(s for s, _, _, _ in r2) / sum(inf for _, inf, _, _ in r2)
    print("sum_i S_i / I: depth one %.6f, depth two %.6f" % (tot1, tot2))


if __name__ == "__main__":
    main()
