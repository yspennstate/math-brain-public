"""Aggregate fpp_cyl rows: per (n, a) count, mean/n, sd, standardized skewness, excess kurtosis (with se), capped rows."""
import json, sys, math, collections
A = collections.defaultdict(list)
meta = collections.defaultdict(lambda: [0, 0, 0.0])
for line in open(sys.argv[1] if len(sys.argv) > 1 else "fpp_rows.jsonl"):
    try:
        r = json.loads(line)
    except ValueError:
        continue
    key = (r["n"], r["a"], r["W"])
    A[key].extend(r["T"])
    m = meta[key]
    m[0] += 1; m[1] += int(r["capped"]); m[2] += r["secs"]
print("    n      a     W   count   mean/n      sd     skew (se)      exkurt (se)   rows capped secs")
for key in sorted(A):
    T = A[key]; N = len(T)
    mu = sum(T) / N
    c2 = sum((t - mu) ** 2 for t in T) / N
    c3 = sum((t - mu) ** 3 for t in T) / N
    c4 = sum((t - mu) ** 4 for t in T) / N
    sk = c3 / c2 ** 1.5 if c2 > 0 else float("nan")
    ku = c4 / c2 ** 2 - 3 if c2 > 0 else float("nan")
    n, a, W = key
    m = meta[key]
    print("%5d %6.3f %5d %7d %8.4f %7.3f %7.3f (%.3f) %7.3f (%.3f) %5d %4d %7.0f" % (
        n, a, W, N, mu / n, math.sqrt(c2), sk, math.sqrt(6.0 / N), ku, math.sqrt(24.0 / N), m[0], m[1], m[2]))
