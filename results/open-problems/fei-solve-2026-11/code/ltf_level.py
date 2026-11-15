"""Erasure entropy of linear threshold functions, with the level witness.

For f = sgn(w.x - theta) and each coordinate i:
  Inf_i = sum_T b_T^2,  E_i = sum_T Phi(a_T^2, b_T^2),  a_T = fhat(T), b_T = fhat(T+i), T not containing i,
  Phi(p, q) = (p+q) h(q/(p+q))  (bits),
  L_i = sum_k Phi(A_k, B_k),  A_k = sum_{|T|=k} a_T^2, B_k likewise   (level witness; E_i <= L_i).
Prints, per function: n, I, H/I, the coordinate of largest weight with E/Inf and L/Inf, and min_i E_i/Inf_i,
min_i L_i/Inf_i.

usage: python ltf_level.py n family [param] [seed] [reps]
families: gauss, unif, geom (param = ratio), two (param = number of heavy, weight sqrt(n)), maj (param = theta),
          lin (weights 1..n), fib, pow (param = exponent p, weights j^p)
"""
import sys
import numpy as np


def wht(v):
    v = v.astype(np.float64).copy()
    n = v.size.bit_length() - 1
    h = 1
    while h < v.size:
        v = v.reshape(-1, 2, h)
        x = v[:, 0, :] + v[:, 1, :]
        y = v[:, 0, :] - v[:, 1, :]
        v = np.stack([x, y], axis=1).reshape(-1)
        h *= 2
    return v / v.size


def phi(p, q):
    s = p + q
    out = np.zeros_like(s)
    m = (p > 0) & (q > 0)
    out[m] = -(p[m] * np.log2(p[m] / s[m]) + q[m] * np.log2(q[m] / s[m]))
    return out


def analyse(w, theta):
    n = len(w)
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    s = np.full(N, -float(theta))
    for j in range(n):
        bit = (idx >> j) & 1
        s += w[j] * (1 - 2 * bit)
    if np.any(np.abs(s) < 1e-12):
        return None
    f = np.sign(s)
    fh = wht(f)
    mu = fh * fh
    pc = np.zeros(N, dtype=np.int64)
    for j in range(n):
        pc += (idx >> j) & 1
    I = float((mu * pc).sum())
    nz = mu > 0
    H = float(-(mu[nz] * np.log2(mu[nz])).sum())
    res = []
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]
        a2 = mu[lo]
        b2 = mu[lo | (1 << i)]
        inf = float(b2.sum())
        if inf <= 0:
            res.append((0.0, 0.0, 0.0))
            continue
        E = float(phi(a2, b2).sum())
        lev = pc[lo]
        A = np.bincount(lev, weights=a2, minlength=n)
        B = np.bincount(lev, weights=b2, minlength=n)
        L = float(phi(A, B).sum())
        res.append((inf, E, L))
    return I, H, res


def weights(n, fam, param, rng):
    if fam == 'gauss':
        return np.abs(rng.standard_normal(n)), None
    if fam == 'unif':
        return rng.uniform(0.05, 1.0, n), None
    if fam == 'geom':
        return param ** np.arange(n) * (1 + 1e-3 * rng.standard_normal(n)), None
    if fam == 'two':
        m = int(param)
        w = np.ones(n)
        w[:m] = np.sqrt(n)
        return w * (1 + 1e-3 * rng.standard_normal(n)), None
    if fam == 'maj':
        return np.ones(n), param
    if fam == 'lin':
        return np.arange(1, n + 1) * (1 + 1e-4 * rng.standard_normal(n)), None
    if fam == 'fib':
        w = [1.0, 1.0]
        while len(w) < n:
            w.append(w[-1] + w[-2])
        return np.array(w[:n]) * (1 + 1e-4 * rng.standard_normal(n)), None
    if fam == 'pow':
        return np.arange(1, n + 1) ** param * (1 + 1e-4 * rng.standard_normal(n)), None
    raise SystemExit('family?')


def main():
    n = int(sys.argv[1])
    fam = sys.argv[2]
    param = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    reps = int(sys.argv[5]) if len(sys.argv) > 5 else 5
    thfix = float(sys.argv[6]) if len(sys.argv) > 6 else None
    rng = np.random.default_rng(seed)
    for r in range(reps):
        w, th = weights(n, fam, param, rng)
        if th is None:
            sd = float(np.sqrt((w * w).sum()))
            m = thfix if thfix is not None else rng.choice([0.0, 0.5, 1.0, 1.5, 2.0])
            th = m * sd + 1e-3 * rng.standard_normal()
        out = analyse(w, th)
        if out is None:
            print('tie, skipped')
            continue
        I, H, res = out
        if I <= 0:
            print('constant')
            continue
        imax = int(np.argmax(w))
        live = [(k, x) for k, x in enumerate(res) if x[0] > 0]
        rE = min(x[1] / x[0] for _, x in live)
        rL = min(x[2] / x[0] for _, x in live)
        worstE = max(x[1] / x[0] for _, x in live)
        inf, E, L = res[imax]
        sE = sum(x[1] for _, x in live)
        print('n=%d %s p=%g th/sd=%.2f I=%.4f H/I=%.3f H-/I=%.3f | maxw: Inf=%.2e E/Inf=%.3f L/Inf=%.3f | min E/Inf=%.3f '
              'min L/Inf=%.3f max E/Inf=%.3f' % (n, fam, param, th / float(np.sqrt((w * w).sum())), I, H / I, sE / I,
                                               inf, E / inf if inf > 0 else -1, L / inf if inf > 0 else -1, rE, rL, worstE))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
