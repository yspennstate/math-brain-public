"""collapse_agg.py <rows.jsonl> [...]: skewness of the line-to-line passage time by (c, n) for widths W = c n^(2/3).
Each row's T is one batch of samples; rows of the same (c, n) are pooled. se of skew = sqrt(6/N)."""
import collections, json, math, sys

pool = collections.defaultdict(list)
W = {}
for f in sys.argv[1:]:
    for ln in open(f, encoding="utf-8"):
        try:
            r = json.loads(ln)
        except Exception:
            continue
        if r.get("capped"):
            continue
        key = (float(r["c"]), int(r["n"]))
        pool[key] += r["T"]
        W[key] = r["W"]
print("%5s %6s %5s %7s %8s %7s %6s" % ("c", "n", "W", "N", "skew", "se", "z"))
for key in sorted(pool):
    x = pool[key]
    N = len(x)
    m = sum(x) / N
    s2 = sum((v - m) ** 2 for v in x) / N
    s3 = sum((v - m) ** 3 for v in x) / N
    g = s3 / s2 ** 1.5 if s2 > 0 else float("nan")
    se = math.sqrt(6.0 / N)
    print("%5.2f %6d %5d %7d %8.3f %7.3f %6.1f" % (key[0], key[1], W[key], N, g, se, g / se))
