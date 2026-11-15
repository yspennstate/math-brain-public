"""check_search.py - recompute the leaders of mono_search output files with the separate transform of merge_census.py.

usage: python check_search.py FILE [FILE ...] [--top K]
For each file: best value per objective, number of runs, and for the top distinct tables the recomputed statistics,
influence vector, E/Inf vector, number of non-dummy variables and a monotonicity check.
"""
import sys

from merge_census import stats


def is_monotone(tab, n):
    N = 1 << n
    for x in range(N):
        if (tab >> x) & 1:
            for i in range(n):
                if not (x >> i) & 1 and not (tab >> (x | (1 << i))) & 1:
                    return False
    return True


def main():
    args = sys.argv[1:]
    top = 2
    if "--top" in args:
        k = args.index("--top")
        top = int(args[k + 1])
        del args[k:k + 2]
    for fn in args:
        rows = []
        n = obj = None
        with open(fn, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("# mono_search") or line.startswith("# fei_search"):
                    kv = dict(t.split("=") for t in line.split()[2:])
                    n, obj = int(kv["n"]), int(kv["obj"])
                    continue
                if line.startswith("#") or "|" not in line:
                    continue
                a, b, c = line.split("|")
                rows.append((float(a.split()[3]), c.strip()))
        if not rows:
            print(fn, "no runs yet")
            continue
        best = {}
        for v, h in rows:
            best[h] = v
        lst = sorted(best.items(), key=lambda t: -t[1])
        vals = sorted((v for v, _ in rows), reverse=True)
        print("== %s n=%d obj=%d runs=%d best=%.12f median=%.12f distinct tables=%d"
              % (fn, n, obj, len(rows), vals[0], vals[len(vals) // 2], len(lst)))
        name = ["minE", "ruleMax", "Q0", "HI", "balHI1"][obj]
        K = n - 1
        half = 1 << K
        for h, v in lst[:top]:
            tab = int(h, 16)
            f0, f1 = tab & ((1 << half) - 1), tab >> half
            st = stats(f1, f0, K)
            live = [i for i in range(n) if st["inf"][i] > 0]
            print("  %.12f recomputed %s=%.12f diff=%.1e  minE=%.9f ruleMax=%.9f Q0=%.9f H=%.9f I=%.9f mean=%.6f live=%d monotone=%s"
                  % (v, name, st.get(name, float("nan")), abs(st.get(name, float("nan")) - v), st["minE"], st["ruleMax"], st["Q0"], st["H"], st["I"], st["mean"],
                     len(live), is_monotone(tab, n)))
            print("     inf  ", " ".join("%.6f" % x for x in st["inf"]))
            print("     E/inf", " ".join("%.6f" % (st["E"][i] / st["inf"][i]) if st["inf"][i] > 0 else "nan" for i in range(n)))
            print("     table", h)


if __name__ == "__main__":
    main()
