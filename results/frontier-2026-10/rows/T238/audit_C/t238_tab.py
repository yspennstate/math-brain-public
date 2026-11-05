"""T238 seed-variance review: pool the source's runs (win_*.txt and win2_*.txt in the row folder) with
extra seeds run here with the source's own window.py (window.py (the source's file), unchanged) into t238_runs/.
share(c) = dist_to_lazy(c) / lazy test error (the second pass's normalisation, applied to every run).
Per d: mean, sd and range over seeds; OLS slope of share on log2 d over individual runs with its standard error;
Spearman rank correlation of test(c=1e-3) with d.
usage: python t238_tab.py (from audit_C/) -> t238_tab.json"""
import glob, json, math, re
import numpy as np
from scipy.stats import spearmanr

SRC = ["win_d8", "win_d12", "win_d12_s2", "win_d16", "win2_8_16_2", "win2_16_64_2", "win2_24_144_1", "win2_24_144_2",
       "win2_32_256_1"]
HEAD = re.compile(r"d (\d+) n (\d+) .*seed (\d+) \| lazy limit \(min-Frobenius\): test ([\d.]+)")
ROW = re.compile(r"c\s+([\d.e+-]+) .*steps\s+(\d+) train ([\d.e+-]+) \| test ([\d.]+) \| dist to lazy ([\d.]+)")
CS = [1e-3, 1e-2, 1e-1]


def parse(text, origin):
    h = HEAD.search(text)
    d, n, seed, lazy = int(h[1]), int(h[2]), int(h[3]), float(h[4])
    rows = {}
    for m in ROW.finditer(text):
        c = float(m[1])
        rows[c] = {"steps": int(m[2]), "train": float(m[3]), "test": float(m[4]), "dist": float(m[5])}
    return {"d": d, "n": n, "seed": seed, "lazy": lazy, "rows": rows, "origin": origin}


runs = []
for f in SRC:
    t = open("../" + f + ".txt").read()
    runs.append(parse(t, "source:" + f))
for f in sorted(glob.glob("t238_runs/w_*.txt")):
    t = open(f).read()
    if HEAD.search(t):  # a run still starting has no header yet
        runs.append(parse(t, "here:" + f))

out = {"runs": [], "by_d": {}, "trend": {}}
for r in runs:
    for c in CS:
        if c in r["rows"]:
            x = r["rows"][c]
            out["runs"].append({"d": r["d"], "seed": r["seed"], "c": c, "share": x["dist"] / r["lazy"], "test": x["test"],
                                "lazy": r["lazy"], "train": x["train"], "steps": x["steps"], "origin": r["origin"]})
rs = out["runs"]
for c in CS:
    print(f"\nc = {c:g}   share = dist/lazy_test (seeds)                   test error")
    xs, ys = [], []
    for d in sorted({r["d"] for r in rs}):
        s = [r for r in rs if r["d"] == d and r["c"] == c]
        sh = np.array([r["share"] for r in s]); te = np.array([r["test"] for r in s])
        out["by_d"][f"{d}_{c:g}"] = {"n_seeds": len(s), "share_mean": sh.mean(), "share_sd": sh.std(ddof=1) if len(s) > 1 else None,
                                     "share_min": sh.min(), "share_max": sh.max(), "test_min": te.min(), "test_max": te.max(),
                                     "test_median": float(np.median(te))}
        sd = f"{sh.std(ddof=1):.2f}" if len(s) > 1 else "  - "
        print(f"  d={d:2d} k={len(s)}  mean {sh.mean():.2f} sd {sd}  range {sh.min():.2f}-{sh.max():.2f}   "
              f"test median {np.median(te):.4f} range {te.min():.4f}-{te.max():.4f}")
        xs += [math.log2(d)] * len(s); ys += list(sh)
    X = np.c_[np.ones(len(xs)), xs]; y = np.array(ys)
    beta, res, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta; s2 = resid @ resid / (len(y) - 2)
    se = math.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    out["trend"][f"share_slope_per_doubling_{c:g}"] = {"slope": beta[1], "se": se, "n": len(y)}
    print(f"  OLS share on log2 d: slope {beta[1]:+.3f} per doubling, se {se:.3f}, n {len(y)}")
for c in CS:  # the same slope without d = 8 (n = 2d, where the rich flow can fail to recover the teacher)
    s = [r for r in rs if r["c"] == c and r["d"] >= 12]
    X = np.c_[np.ones(len(s)), [math.log2(r["d"]) for r in s]]; y = np.array([r["share"] for r in s])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]; resid = y - X @ beta
    se = math.sqrt(resid @ resid / (len(y) - 2) * np.linalg.inv(X.T @ X)[1, 1])
    out["trend"][f"share_slope_per_doubling_d12up_{c:g}"] = {"slope": beta[1], "se": se, "n": len(y)}
    print(f"d >= 12, c = {c:g}: slope {beta[1]:+.3f} per doubling, se {se:.3f}, n {len(y)}")
t3 = [r for r in rs if r["c"] == 1e-3]
rho, p = spearmanr([r["d"] for r in t3], [r["test"] for r in t3])
out["trend"]["spearman_test_1e-3_vs_d"] = {"rho": rho, "p": p, "n": len(t3)}
print(f"\nSpearman test(c=1e-3) vs d: rho {rho:+.3f}, p {p:.3g}, n {len(t3)}")
unconv = [r for r in rs if r["train"] > 1e-10 * 1.0001]
out["unconverged"] = unconv
print("runs stopped at the step cap above train 1e-10:", [(r["d"], r["seed"], r["c"], r["train"]) for r in unconv])
json.dump(out, open("t238_tab.json", "w"), indent=1, default=float)
