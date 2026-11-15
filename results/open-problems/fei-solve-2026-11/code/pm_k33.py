"""Truth tables of the PM(K33) host (9 variables) and of its lift with nine coins (18 variables), as hex.

Construction as in 12_cognitive_architecture/top10_7_10_agent/rank10_check_pmk33_lift_1109.py: on the 3 x 3 grid
f(x) = 1 when some row or column is all ones; O = the minority side; S = the 18 points off O with the largest number
of neighbours in O, matched in 9 Hamming-adjacent pairs; the lift G(x, y) = O(x) off S and = the coin y_j on pair j.
Output lines "name hex" with bit z of the integer set when the function is -1 at z.

usage: python pm_k33.py OUTDIR
"""
import sys
import os

m = 9
N = 1 << m


def bit(x, i):
    return (x >> i) & 1


def build():
    lines = [[3 * r + c for c in range(3)] for r in range(3)] + [[3 * r + c for r in range(3)] for c in range(3)]
    f = [any(all(bit(x, j) for j in L) for L in lines) for x in range(N)]
    O = f if 2 * sum(f) <= N else [not v for v in f]
    d = N - 2 * sum(O)
    cnt = [sum(O[x ^ (1 << i)] for i in range(m)) for x in range(N)]
    top = max(cnt[x] for x in range(N) if not O[x])
    S = [x for x in range(N) if not O[x] and cnt[x] == top]
    assert len(S) == d
    Sset = set(S)
    mate = {}

    def aug(v, seen):
        for i in range(m):
            w = v ^ (1 << i)
            if w in Sset and w not in seen:
                seen.add(w)
                if w not in mate or aug(mate[w], seen):
                    mate[w] = v
                    return True
        return False
    p = sum(aug(v, set()) for v in S if bin(v).count("1") % 2 == 0)
    assert p == 9
    site = {}
    for j, (w, v) in enumerate(mate.items()):
        site[w] = j
        site[v] = j
    host = 0
    for x in range(N):
        if O[x]:
            host |= 1 << x
    lift = 0
    for y in range(1 << p):
        for x in range(N):
            if x in site:
                neg = (y >> site[x]) & 1
            else:
                neg = 1 if O[x] else 0
            if neg:
                lift |= 1 << (x | (y << m))
    return host, lift


def main():
    out = sys.argv[1]
    host, lift = build()
    with open(os.path.join(out, "pm_k33_host_n9.txt"), "w", encoding="utf-8") as fh:
        fh.write("pm_k33_host %x\n" % host)
    with open(os.path.join(out, "pm_k33_lift_n18.txt"), "w", encoding="utf-8") as fh:
        fh.write("pm_k33_lift %x\n" % lift)
    print("host bits %d  lift bits %d" % (bin(host).count("1"), bin(lift).count("1")))


if __name__ == "__main__":
    main()
