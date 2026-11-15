"""neg_check.py - explicit check of an input-negated coin gate at a homogeneous bias.

Builds the full truth table on m + k inputs from the labels ("m k labels" in LABFILE), negates the inputs in MASK
(binary string, character i = input i, main inputs first, then the used coins in increasing order), and takes the
p-biased transform of the whole table axis by axis.  Prints G, J, p' and U = G - c J + c.
usage: python3 neg_check.py LABFILE MASK c e [e ...]
"""
import sys

import numpy as np


def main():
    parts = open(sys.argv[1], encoding="utf-8").readline().split()
    mask = sys.argv[2]
    c = float(sys.argv[3])
    m = int(parts[0])
    lab = [ord(ch) - 48 for ch in parts[2]]
    used = sorted({(l - 2) // 2 for l in lab if l >= 2})
    k = len(used)
    n = m + k
    assert len(mask) == n
    N = 1 << n
    idx = np.arange(N)
    x = idx & ((1 << m) - 1)
    f = np.zeros(N)
    labx = np.array(lab)[x]
    f[labx == 0] = 1.0
    f[labx == 1] = -1.0
    for jj, j in enumerate(used):
        y = 1.0 - 2.0 * ((idx >> (m + jj)) & 1)
        f = np.where(labx == 2 + 2 * j, y, np.where(labx == 3 + 2 * j, -y, f))
    flip = sum(1 << i for i, ch in enumerate(mask) if ch == "1")
    f = f[idx ^ flip]
    size = np.array([bin(v).count("1") for v in range(N)], dtype=np.float64)
    for e in [float(v) for v in sys.argv[4:]]:
        p = 0.5 + e
        s = np.sqrt(p * (1 - p))
        a = f.copy()
        h = 1
        while h < N:
            a = a.reshape(-1, 2, h)
            lo, hi = a[:, 0, :], a[:, 1, :]
            a = np.stack([(1 - p) * lo + p * hi, s * (hi - lo)], axis=1).reshape(-1)
            h *= 2
        mean = a[0]
        var = 1 - mean * mean
        w = a * a
        w[0] = 0.0
        w /= var
        nz = w > 1e-300
        G = float(-(w[nz] * np.log2(w[nz])).sum())
        J = float((w * size).sum())
        pp = (1 - mean) / 2
        U = G - c * J + c
        print("e %+.4g  G %.10f J %.10f p'-1/2 %+.6e  U %+.6e  U/e^2 %+.4f  (p'-1/2)/e %+.5f"
              % (e, G, J, pp - 0.5, U, U / (e * e) if e else 0.0, (pp - 0.5) / e if e else 0.0))


if __name__ == "__main__":
    main()
