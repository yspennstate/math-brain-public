"""Referee check for P7 Theorem 1 (census), written from the outline's statements only.

For n <= 6: enumerate every LABELED linear monotone DNF whose terms cover all n variables
(antichain, pairwise intersections <= 1) by plain backtracking over subsets, count them, and
compute max H/I and max min_i E_i/Inf_i. The labeled count must equal sum n!/Aut in the paper's
table, and the maxima must match (both are isomorphism invariants).
For n = 8: recompute the two claimed attainers directly.
"""
import itertools, math, sys
import numpy as np


def hadamard(n):
    H = np.array([[1.0]])
    for _ in range(n):
        H = np.block([[H, H], [H, -H]])
    return H


def eta(x):
    out = np.zeros_like(x)
    m = x > 0
    out[m] = -x[m] * np.log2(x[m])
    return out


def ratios(Fs, n):
    """Fs: (m, 2^n) bool, F(x)=1 iff some term is satisfied. Returns H/I and min_i E_i/Inf_i per row."""
    N = 1 << n
    f = 1.0 - 2.0 * Fs.astype(float)
    fh = f @ hadamard(n) / N            # Hadamard is symmetric; index = character set S
    wt = fh ** 2
    S = np.arange(N)
    size = np.array([bin(s).count("1") for s in S], dtype=float)
    H = eta(wt).sum(1)
    I = (wt * size).sum(1)
    mins = np.full(len(Fs), np.inf)
    for i in range(n):
        lo = S[(S >> i) & 1 == 0]
        p, q = wt[:, lo], wt[:, lo | (1 << i)]
        E = (eta(p) + eta(q) - eta(p + q)).sum(1)
        inf = q.sum(1)
        mins = np.minimum(mins, np.where(inf > 0, E / np.where(inf > 0, inf, 1), np.inf))
    return H / I, mins


def families(n):
    subs = list(range(1, 1 << n))
    pc = [bin(s).count("1") for s in range(1 << n)]
    ok = [[(pc[a & b] <= 1) and (a & b) != a and (a & b) != b for b in subs] for a in subs]
    full = (1 << n) - 1
    out = []

    def rec(start, chosen, union):
        if chosen and union == full:
            out.append(tuple(subs[k] for k in chosen))
        for k in range(start, len(subs)):
            if all(ok[k][c] for c in chosen):
                chosen.append(k)
                rec(k + 1, chosen, union | subs[k])
                chosen.pop()

    rec(0, [], 0)
    return out


def table(fams, n):
    N = 1 << n
    x = np.arange(N)
    Fs = np.zeros((len(fams), N), dtype=bool)
    for r, fam in enumerate(fams):
        for t in fam:
            Fs[r] |= (x & t) == t
    return Fs


def top2(v):
    s = np.sort(v)[::-1]
    return s[0], s[1] if len(s) > 1 else float("nan")


def main():
    paper = {1: None, 2: None,
             3: (9, 2.672488983973, 2.955889582252),
             4: (97, 2.634003390886, 3.402475551199),
             5: (2625, 2.695887520153, 3.623740399702),
             6: (185521, 2.944495303872, 3.739764017898)}
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    for n in range(1, nmax + 1):
        fams = families(n)
        hi, me = [], []
        for c in range(0, len(fams), 20000):
            a, b = ratios(table(fams[c:c + 20000], n), n)
            hi.append(a); me.append(b)
        hi = np.concatenate(hi); me = np.concatenate(me)
        (h1, h2), (m1, m2) = top2(hi), top2(me)
        line = f"n={n} labeled={len(fams)} max H/I={h1:.12f} (2nd {h2:.12f}) max minE/Inf={m1:.12f} (2nd {m2:.12f})"
        if paper.get(n):
            L, pm, ph = paper[n]
            line += f"  | paper labeled {L} {'OK' if L == len(fams) else 'MISMATCH'}," \
                    f" H/I diff {h1 - ph:+.1e}, minE/Inf diff {m1 - pm:+.1e}"
        print(line, flush=True)

    # n = 8 attainers (variables 0..7)
    c4 = lambda v: [(1 << v[0]) | (1 << v[1]), (1 << v[1]) | (1 << v[2]),
                    (1 << v[2]) | (1 << v[3]), (1 << v[3]) | (1 << v[0])]
    A = [1, 2, 4, 8] + c4([4, 5, 6, 7])          # OR of four variables + 4-cycle DNF on four others
    B = c4([0, 1, 2, 3]) + c4([4, 5, 6, 7])      # two disjoint 4-cycles
    hA, mA = ratios(table([tuple(A)], 8), 8)
    hB, mB = ratios(table([tuple(B)], 8), 8)
    print(f"n=8 OR4+C4: H/I={hA[0]:.12f} (paper max 3.889105419815) minE/Inf={mA[0]:.12f}")
    print(f"n=8 C4+C4 : H/I={hB[0]:.12f} minE/Inf={mB[0]:.12f} (paper max 3.304701322451)")


if __name__ == "__main__":
    main()
