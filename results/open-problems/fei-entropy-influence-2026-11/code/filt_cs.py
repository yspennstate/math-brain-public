"""Filtration witness (FLOW section 12).

Fix a coordinate i and an ordering pi of the other coordinates.  Label a set T (not containing i) by the position of
its last element in the ordering (0 for the empty set).  Then
    L^pi_i = H(1[i in U] | label(U - i)) = sum_k Phi(A_k, B_k)  >=  E_i,
    A_k = E[(Delta_k g)^2],  B_k = E[(Delta_k h)^2],   g = E_i f = (f_+ + f_-)/2,  h = D_i f = (f_+ - f_-)/2,
with Delta_k the martingale differences of the filtration that reveals the coordinates in the order pi.
With a(R) = sum_{T in R} fhat(T)^2 and b(R) = sum_{T in R} fhat(T + i)^2 (zeta transforms), the minimum over all
orderings is a shortest path in the subset lattice:
    best(R) = min_{j in R} best(R - j) + Phi(a(R) - a(R - j), b(R) - b(R - j)),  best(empty) = Phi(a(empty), b(empty)).
Also printed for the best ordering: M = max_{K>=1} A_{>=K} B_{<=K} / Inf_i^2 (the hypothesis of the two-sequence
lemma, FLOW 11(d)); in martingale terms A_{>=K} = E Var(g | first K-1 coordinates), B_{<=K} = E (E[h | first K])^2.

usage:
  python filt_cs.py fam nmax
  python filt_cs.py rand n count seed
  python filt_cs.py file n PATH        hex truth tables (last token of each line; bit x set when f(x) = -1)
"""
import sys
import numpy as np
from local_cs import wht, phi, families


def zeta(v, m):
    a = v.copy()
    for j in range(m):
        a = a.reshape(-1, 2, 1 << j)
        a[:, 1, :] += a[:, 0, :]
        a = a.reshape(-1)
    return a


def best_order(p, q, m):
    """returns (best value, ordering as list of compressed coordinates, M of that ordering)."""
    a = zeta(p, m)
    b = zeta(q, m)
    size = 1 << m
    idx = np.arange(size)
    best = np.full(size, np.inf)
    arg = np.full(size, -1, dtype=np.int8)
    best[0] = float(phi(a[0], b[0]))
    pc = np.zeros(size, dtype=np.int8)
    for j in range(m):
        pc += ((idx >> j) & 1).astype(np.int8)
    for layer in range(1, m + 1):
        R = idx[pc == layer]
        for j in range(m):
            sel = R[(R >> j) & 1 == 1]
            prev = sel ^ (1 << j)
            da = np.maximum(a[sel] - a[prev], 0.0)
            db = np.maximum(b[sel] - b[prev], 0.0)
            cand = best[prev] + phi(da, db)
            upd = cand < best[sel]
            best[sel[upd]] = cand[upd]
            arg[sel[upd]] = j
    order = []
    R = size - 1
    while R:
        j = int(arg[R])
        order.append(j)
        R ^= 1 << j
    order.reverse()
    # two-sequence hypothesis along the best ordering
    R = 0
    inf = float(b[size - 1])
    tot_a = float(a[size - 1])
    M = 0.0
    for j in order:
        prev = R
        R |= 1 << j
        # A_{>=K} = weight of g on labels K and later = tot_a - a(R_{K-1});  B_{<=K} = b(R_K)
        M = max(M, (tot_a - float(a[prev])) * float(b[R]) / inf ** 2)
    return float(best[size - 1]), order, M


def analyse(f, n):
    mu = wht(f, n) ** 2
    idx = np.arange(1 << n)
    rows = []
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p = mu[lo]
        q = mu[lo | (1 << i)]
        inf = float(q.sum())
        if inf < 1e-12:
            continue
        E = float(phi(p, q).sum())
        val, order, M = best_order(p, q, n - 1)
        full = [c for c in range(n) if c != i]
        rows.append(dict(i=i, inf=inf, E=E / inf, F=val / inf, order=[full[j] for j in order], M=M))
    return rows


def report(name, f, n):
    rows = analyse(f, n)
    if not rows:
        print("%-14s constant" % name)
        return None
    rE = min(rows, key=lambda r: r["E"])
    rF = min(rows, key=lambda r: r["F"])
    worst = max(rows, key=lambda r: r["F"])
    print("%-14s n=%2d minE=%.4f (i=%d) | filtration min=%.4f (i=%d, M=%.3f, order=%s) | max_i filtration=%.4f"
          % (name, n, rE["E"], rE["i"], rF["F"], rF["i"], rF["M"], "".join("%x" % c for c in rF["order"]),
             worst["F"]), flush=True)
    return rE["E"], rF["F"], rF["M"]


def main():
    mode = sys.argv[1]
    tops = [0.0, 0.0, 0.0]
    if mode == "fam":
        for name, n, f in families(int(sys.argv[2])):
            r = report(name, f, n)
            if r:
                tops = [max(x, y) for x, y in zip(tops, r)]
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
                tops = [max(x, y) for x, y in zip(tops, r)]
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
                    tops = [max(x, y) for x, y in zip(tops, r)]
    print("sup over the functions read:  minE %.4f   filtration %.4f   M %.3f" % tuple(tops))


if __name__ == "__main__":
    main()
