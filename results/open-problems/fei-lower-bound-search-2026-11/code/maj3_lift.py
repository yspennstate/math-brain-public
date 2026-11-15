"""maj3_lift.py - Q_b on Maj_3 o psi for every balanced monotone psi on 3 or 4 variables (asked by an agent,
mesh 10 Nov 20:58Z: does the slowly-varying-weight lift of FLOW 12(gg) start to show?).
Table convention of merge_census.stats: bit x set <=> value -1; (f1, f0) = (x_n = 1 half, x_n = 0 half)."""
import itertools
from merge_census import stats


def monotone_tables(m):
    N = 1 << m
    out = []
    for tab in range(1 << N):
        ok = True
        for x in range(N):
            if (tab >> x) & 1:
                for i in range(m):
                    if not (x >> i) & 1 and not (tab >> (x | (1 << i))) & 1:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            out.append(tab)
    return out


def compose_maj3(psi, m):
    n = 3 * m
    N = 1 << n
    mask = (1 << m) - 1
    tab = 0
    for x in range(N):
        v = [(psi >> ((x >> (m * j)) & mask)) & 1 for j in range(3)]
        if sum(v) >= 2:
            tab |= 1 << x
    return tab, n


def row(name, tab, n):
    half = 1 << (n - 1)
    st = stats(tab >> half, tab & ((1 << half) - 1), n - 1)
    print("%-28s n=%2d H/I=%.6f minE=%.6f Q0=%.6f Q05=%.6f Q1=%.6f Q1-Q0=%+.6f I=%.6f" %
          (name, n, st["HI"], st["minE"], st["Q0"], st["Q05"], st["Q1"], st["Q1mQ0"], st["I"]))


for m in (3, 4):
    seen = set()
    for psi in monotone_tables(m):
        if bin(psi).count("1") != (1 << m) // 2:
            continue
        # canonical form under variable permutations
        best = None
        for p in itertools.permutations(range(m)):
            t = 0
            for x in range(1 << m):
                if (psi >> x) & 1:
                    y = 0
                    for i in range(m):
                        if (x >> i) & 1:
                            y |= 1 << p[i]
                    t |= 1 << y
            best = t if best is None or t < best else best
        if best in seen:
            continue
        seen.add(best)
        half = 1 << (m - 1)
        s0 = stats(best >> half, best & ((1 << half) - 1), m - 1)
        live = sum(1 for v in s0["inf"] if v > 0)
        row("psi %0*x (live %d)" % ((1 << m) // 4, best, live), best, m)
        tab, n = compose_maj3(best, m)
        row("  Maj3 o psi", tab, n)
