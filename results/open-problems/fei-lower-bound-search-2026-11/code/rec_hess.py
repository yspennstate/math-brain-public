"""rec_hess.py - second-order behaviour of a coin gate when its inputs have unequal biases near 1/2.

Inputs of the gate may be the state g (bias 1/2 + e) or its negation (bias 1/2 - e), so the bias vector is
1/2 + e s with s in {+1, -1}^n.  For a self-dual gate with a transitive symmetry group the gradient of
U = G - c J + c vanishes at the uniform point, so U(1/2 + e s) = (e^2 / 2) s'Qs + ..., and p' - 1/2 = e d(s) + ...
with d(s) = sum_i s_i Inf_i.  If d^2 < J the Bellman value satisfies W(1/2 + e) >= c + a e^2, a = (s'Qs/2)/(J - d^2).

Prints the gradient, the Hessian by classes, and the sign vectors with the largest a (exhaustive over 2^n when
n <= 20).  usage: python rec_hess.py LABFILE [h]
"""
import sys

import numpy as np


def parts_of(m, labels):
    lab = np.array(labels, dtype=np.int64)
    used = sorted({int((l - 2) // 2) for l in lab if l >= 2})
    s0 = np.where(lab == 0, 1.0, np.where(lab == 1, -1.0, 0.0))
    rows = [s0]
    for j in used:
        rows.append(np.where(lab == 2 + 2 * j, 1.0, np.where(lab == 3 + 2 * j, -1.0, 0.0)))
    return np.array(rows), len(used)


def het_stats(m, rows, pm, pq):
    """pm: biases of the m main inputs (axis i = bit i of x), pq: biases of the coins.  Returns G, J, p', infl."""
    N = 1 << m
    L = rows.shape[0]
    a = rows.copy()
    for i in range(m):
        h = 1 << i
        p = pm[i]
        s = np.sqrt(p * (1 - p))
        a = a.reshape(L, -1, 2, h)
        lo, hi = a[:, :, 0, :], a[:, :, 1, :]
        a = np.stack([(1 - p) * lo + p * hi, s * (hi - lo)], axis=2).reshape(L, -1)
    pq = np.asarray(pq)
    a0 = a[0] + ((1 - 2 * pq)[:, None] * a[1:]).sum(axis=0)
    mean = a0[0]
    var = 1 - mean * mean
    w0 = a0 * a0
    w0[0] = 0.0
    wc = (4 * pq * (1 - pq))[:, None] * a[1:] ** 2
    allw = np.concatenate([w0, wc.reshape(-1)]) / var
    nz = allw > 1e-300
    G = float(-(allw[nz] * np.log2(allw[nz])).sum())
    idx = np.arange(N)
    infl = np.empty(m + len(pq))
    tot = w0 + wc.sum(axis=0)
    for i in range(m):
        infl[i] = tot[((idx >> i) & 1) == 1].sum() / var
    infl[m:] = wc.sum(axis=1) / var
    return G, float(infl.sum()), (1 - mean) / 2, infl


def main():
    parts = open(sys.argv[1], encoding="utf-8").readline().split()
    h = float(sys.argv[2]) if len(sys.argv) > 2 else 1e-3
    m = int(parts[0])
    rows, kk = parts_of(m, [ord(ch) - 48 for ch in parts[2]])
    n = m + kk
    half = np.full(n, 0.5)

    def U(pv, c):
        G, J, pp, _ = het_stats(m, rows, pv[:m], pv[m:])
        return G - c * J + c, pp

    G0, J0, P0, infl = het_stats(m, rows, half[:m], half[m:])
    c = G0 / (J0 - 1)
    print("n = %d (m = %d, coins %d)  G %.12f J %.12f p' %.6f c %.12f" % (n, m, kk, G0, J0, P0, c))
    print("influences:", " ".join("%.5f" % v for v in infl))
    grad = np.zeros(n)
    dP = np.zeros(n)
    for i in range(n):
        up = half.copy(); up[i] += h
        dn = half.copy(); dn[i] -= h
        a, pa = U(up, c); b, pb = U(dn, c)
        grad[i] = (a - b) / (2 * h); dP[i] = (pa - pb) / (2 * h)
    print("gradient of U:", " ".join("%+.5f" % v for v in grad))
    print("d p' / d p_i :", " ".join("%+.5f" % v for v in dP))
    u0 = U(half, c)[0]
    Q = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            if i == j:
                up = half.copy(); up[i] += h
                dn = half.copy(); dn[i] -= h
                Q[i, i] = (U(up, c)[0] - 2 * u0 + U(dn, c)[0]) / (h * h)
            else:
                v = 0.0
                for si in (1, -1):
                    for sj in (1, -1):
                        pv = half.copy(); pv[i] += si * h; pv[j] += sj * h
                        v += si * sj * U(pv, c)[0]
                Q[i, j] = Q[j, i] = v / (4 * h * h)
    np.save(sys.argv[1] + ".Q.npy", Q)
    ev = np.linalg.eigvalsh(Q)
    print("Hessian eigenvalues:", " ".join("%+.3f" % v for v in ev))
    print("diag main: %s" % " ".join("%+.2f" % Q[i, i] for i in range(m)))
    print("diag coin: %s" % " ".join("%+.2f" % Q[i, i] for i in range(m, n)))
    ones = np.ones(n)
    print("all plus: s'Qs/2 = %+.4f, d = %.5f" % (ones @ Q @ ones / 2, dP.sum()))
    if n <= 20:
        best = []
        idx = np.arange(1 << n, dtype=np.int64)
        for lo in range(0, 1 << n, 1 << 14):
            ch = idx[lo:lo + (1 << 14)]
            S = 1.0 - 2.0 * ((ch[:, None] >> np.arange(n)[None, :]) & 1)
            q = np.einsum("ai,ij,aj->a", S, Q, S) / 2
            d = S @ dP
            with np.errstate(divide="ignore", invalid="ignore"):
                a = np.where(d * d < J0 - 1e-9, q / (J0 - d * d), -np.inf)
            k = int(np.argmax(a))
            best.append((float(a[k]), float(q[k]), float(d[k]), int(ch[k])))
            kq = int(np.argmax(q))
            best.append((float(a[kq]), float(q[kq]), float(d[kq]), int(ch[kq])))
        best.sort(reverse=True)
        print("largest a = q / (J - d^2) over sign vectors (bit i set = input i negated):")
        for a, q, d, code in best[:8]:
            print("  a %+.4f  q %+.4f  d %+.5f  mask %s" % (a, q, d, format(code, "0%db" % n)[::-1]))
        best.sort(key=lambda r: -r[1])
        print("largest q:")
        for a, q, d, code in best[:5]:
            print("  q %+.4f  d %+.5f  a %s  mask %s" % (q, d, a, format(code, "0%db" % n)[::-1]))
        # second check of the leader by a direct evaluation at 1/2 + e s
        a, q, d, code = max(best)
        s = 1.0 - 2.0 * ((code >> np.arange(n)) & 1)
        for e in (1e-2, 3e-3, 1e-3):
            u, pp = U(half + e * s, c)
            print("  direct: e %.0e  U %+.4e  U/e^2 %+.4f  (p'-1/2)/e %+.5f" % (e, u, u / (e * e), (pp - 0.5) / e))


if __name__ == "__main__":
    main()
