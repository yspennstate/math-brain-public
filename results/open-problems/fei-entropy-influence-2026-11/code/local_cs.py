"""Local level witness (FLOW 11(h)(2)): for a Boolean f, a coordinate i and a set N of other coordinates,

    L^N_i = H(1[i in U] | |(U - i) n N|) = sum_k Phi(A_k, B_k),
    A_k = sum of fhat(T)^2 over T without i with |T n N| = k,   B_k = same for fhat(T + i)^2,
    Phi(p, q) = (p + q) h(q/(p + q)).

E_i = H(1[i in U] | U - i) <= L^N_i for every N, and E_i <= C Inf_i for one i (in every non-constant function of a
restriction-closed class) gives FEI on the class.  N = everything is the level witness of FLOW 11(a); N empty gives
h(Inf_i).  The question tested here: is  min over (i, N) of L^N_i/Inf_i  bounded where  min_i E_i/Inf_i  is?

Also prints, for the best pair (i, N), the two hypotheses of the two-sequence lemma:
    M0 = B_0/Inf_i^2 (the K = 0 case, free only for N = everything),  M1 = max_{K>=1} A_{>=K} B_{<=K}/Inf_i^2.

usage:
  python local_cs.py fam nmax                 built-in families up to nmax variables (nmax <= 12)
  python local_cs.py rand n count seed        random functions (uniform truth tables) and random sparse ones
  python local_cs.py file n PATH              hex truth tables, one per line (bit x set when f(x) = -1), first token
"""
import sys
import numpy as np


def wht(f, n):
    a = f.astype(np.float64).copy()
    N = 1 << n
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :] + a[:, 1, :]
        y = a[:, 0, :] - a[:, 1, :]
        a = np.stack([x, y], axis=1).reshape(N)
        h *= 2
    return a / N


def eta(x):
    return np.where(x > 1e-300, -x * np.log2(np.maximum(x, 1e-300)), 0.0)


def phi(p, q):
    return eta(p) + eta(q) - eta(p + q)


_PC = {}


def popc(m):
    """popcount table pc[N, t] = |N n t| for N, t in [0, 2^m)."""
    if m not in _PC:
        idx = np.arange(1 << m)
        bits = ((idx[:, None] >> np.arange(m)[None, :]) & 1).astype(np.int16)
        _PC[m] = bits @ bits.T
    return _PC[m]


def analyse(f, n):
    fh = wht(f, n)
    mu = fh * fh
    idx = np.arange(1 << n)
    m = n - 1
    pc = popc(m)
    out = []
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p = mu[lo]
        q = mu[lo | (1 << i)]
        inf = float(q.sum())
        if inf < 1e-12:
            continue
        E = float(phi(p, q).sum())
        # A[Nset, k], B[Nset, k]
        A = np.zeros((1 << m, m + 1))
        B = np.zeros((1 << m, m + 1))
        for k in range(m + 1):
            mask = (pc == k)
            A[:, k] = mask @ p
            B[:, k] = mask @ q
        L = phi(A, B).sum(axis=1)
        best = int(np.argmin(L))
        full = (1 << m) - 1
        Ab = A[best]
        Bb = B[best]
        M0 = float(Bb[0]) / inf ** 2
        tailA = np.cumsum(Ab[::-1])[::-1]
        headB = np.cumsum(Bb)
        M1 = float((tailA[1:] * headB[1:]).max()) / inf ** 2 if m >= 1 else 0.0
        out.append(dict(i=i, inf=inf, E=E / inf, Lfull=float(L[full]) / inf, Lbest=float(L[best]) / inf,
                        Nbest=best, M0=M0, M1=M1))
    return out


def setstr(Nset, i, n):
    """coordinates of N (in the original numbering; the compressed index skips i)."""
    cs = []
    j = 0
    for c in range(n):
        if c == i:
            continue
        if (Nset >> j) & 1:
            cs.append(c)
        j += 1
    return "{" + ",".join(str(c) for c in cs) + "}"


def report(name, f, n):
    rows = analyse(f, n)
    if not rows:
        print("%-14s constant" % name)
        return None
    rE = min(rows, key=lambda r: r["E"])
    rF = min(rows, key=lambda r: r["Lfull"])
    rL = min(rows, key=lambda r: r["Lbest"])
    print("%-14s n=%2d minE=%.4f (i=%d) | full-level min=%.4f (i=%d) | local min=%.4f (i=%d, N=%s, M0=%.3f, M1=%.3f)"
          % (name, n, rE["E"], rE["i"], rF["Lfull"], rF["i"], rL["Lbest"], rL["i"], setstr(rL["Nbest"], rL["i"], n),
             rL["M0"], rL["M1"]), flush=True)
    return rE["E"], rF["Lfull"], rL["Lbest"]


def pts(n):
    return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)


def families(nmax):
    rows = []
    for n in range(2, nmax + 1, 2):
        rows.append(("AND_%d" % n, n, np.where(pts(n).all(axis=1), -1.0, 1.0)))
    for n in range(3, nmax + 1, 2):
        rows.append(("MAJ_%d" % n, n, np.where(pts(n).sum(axis=1) * 2 > n, -1.0, 1.0)))
    for w in (2, 3, 4):
        for s in range(2, 7):
            if w * s <= nmax:
                b = pts(w * s).reshape(-1, s, w)
                rows.append(("TRIBES_%dx%d" % (w, s), w * s, np.where(b.all(axis=2).any(axis=1), -1.0, 1.0)))
    for k in (1, 2, 3):
        n = k + (1 << k)
        if n <= nmax:
            b = pts(n)
            addr = (b[:, :k] * (1 << np.arange(k))[None, :]).sum(axis=1)
            rows.append(("ADDR_%d" % k, n, 1.0 - 2.0 * b[np.arange(1 << n), k + addr]))
    for k in range(2, nmax, 2):
        b = pts(k + 1)
        ip = (b[:, 0:k:2] * b[:, 1:k:2]).sum(axis=1) % 2
        f = 1.0 - 2.0 * ip
        star = (b[:, :k] == 0).all(axis=1)
        rows.append(("BENTPT_%d" % k, k + 1, np.where(star, 1.0 - 2.0 * b[:, k], f)))
    for k in range(2, nmax + 1, 2):
        b = pts(k)
        ip = (b[:, 0:k:2] * b[:, 1:k:2]).sum(axis=1) % 2
        rows.append(("BENT_%d" % k, k, 1.0 - 2.0 * ip))
    # depth-3 read-once: OR of ANDs of ORs, and majority of majorities
    if nmax >= 8:
        b = pts(8).reshape(-1, 2, 2, 2)
        rows.append(("OR_AND_OR_8", 8, np.where(b.any(axis=3).all(axis=2).any(axis=1), -1.0, 1.0)))
    if nmax >= 9:
        b = pts(9).reshape(-1, 3, 3)
        inner = (b.sum(axis=2) >= 2)
        rows.append(("MAJ3_MAJ3", 9, np.where(inner.sum(axis=1) >= 2, -1.0, 1.0)))
    # AND of w majorities of r (the single-set witness should lose about log w here)
    for w, r in ((2, 3), (3, 3), (4, 3), (2, 5)):
        if w * r <= nmax:
            b = pts(w * r).reshape(-1, w, r)
            inner = (b.sum(axis=2) * 2 > r)
            rows.append(("AND%d_MAJ%d" % (w, r), w * r, np.where(inner.all(axis=1), -1.0, 1.0)))
            rows.append(("XOR%d_MAJ%d" % (w, r), w * r, np.where(inner.sum(axis=1) % 2 == 1, -1.0, 1.0)))
    if nmax >= 12:
        b = pts(12).reshape(-1, 3, 2, 2)
        rows.append(("OR_AND_OR_12", 12, np.where(b.any(axis=3).all(axis=2).any(axis=1), -1.0, 1.0)))
    return rows


def main():
    mode = sys.argv[1]
    tops = [0.0, 0.0, 0.0]
    if mode == "fam":
        for name, n, f in families(int(sys.argv[2])):
            r = report(name, f, n)
            if r:
                tops = [max(a, b) for a, b in zip(tops, r)]
    elif mode == "rand":
        n, count, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        rng = np.random.default_rng(seed)
        for c in range(count):
            if c % 2 == 0:
                f = rng.choice([-1.0, 1.0], 1 << n)
            else:
                f = np.where(rng.random(1 << n) < rng.choice([0.05, 0.1, 0.25]), -1.0, 1.0)
            r = report("rand%d" % c, f, n)
            if r:
                tops = [max(a, b) for a, b in zip(tops, r)]
    elif mode == "file":
        n = int(sys.argv[2])
        with open(sys.argv[3], encoding="utf-8") as fh:
            for ln, line in enumerate(fh):
                tok = line.split()
                if not tok:
                    continue
                try:
                    v = int(tok[-1], 16)
                except ValueError:
                    continue
                f = np.array([-1.0 if (v >> x) & 1 else 1.0 for x in range(1 << n)])
                r = report("line%d" % ln, f, n)
                if r:
                    tops = [max(a, b) for a, b in zip(tops, r)]
    print("sup over the functions read:  minE %.4f   full-level %.4f   local %.4f" % tuple(tops))


if __name__ == "__main__":
    main()
