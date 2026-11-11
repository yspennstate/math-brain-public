"""Summary of the outputs of sim_mn.

usage:  python summarize_sim.py data_dir [out.json]

For every n found in data_dir (files n<N>_s<seed>.graphs.csv and .hist.csv) the script prints the number of graphs,
the mean, standard deviation and range of M_n, the mean of R_n, the real level k* at which the exact first moment
E N_{n,k} equals one (interpolated linearly in log E N_{n,k}), and for the levels k around k* the observed frequency
of {M_n >= k}, the observed mean number of pairs at hopcount >= k, and the exact E N_{n,k}. It also compares the
observed number of pairs at each hopcount d with its exact mean (n/2) f_{n,d}.
"""
import glob
import json
import math
import os
import re
import sys

from first_moment import ALPHA, b, expected_pairs


def main():
    d = sys.argv[1]
    sizes = {}
    for g in glob.glob(os.path.join(d, "n*_s*.graphs.csv")):
        n = int(re.match(r"n(\d+)_s", os.path.basename(g)).group(1))
        sizes.setdefault(n, []).append(g)
    out = []
    for n in sorted(sizes):
        ms, rs = [], []
        hist = {}
        for g in sorted(sizes[n]):
            rows = [ln.strip().split(",") for ln in open(g) if ln.strip() and not ln.startswith("rep")]
            ms += [int(r[1]) for r in rows]
            rs += [int(r[2]) for r in rows]
            h = g.replace(".graphs.csv", ".hist.csv")
            for ln in open(h):
                if ln.strip() and not ln.startswith("hop"):
                    k, c = ln.strip().split(",")
                    hist[int(k)] = hist.get(int(k), 0) + int(c)
        m = len(ms)
        assert sum(hist.values()) == m * n * (n - 1) // 2, (n, m)
        mean = sum(ms) / m
        sd = math.sqrt(sum((x - mean) ** 2 for x in ms) / (m - 1))
        kmax = int(ALPHA * math.log(n)) + 60
        en = expected_pairs(n, kmax)
        k1 = max(k for k in range(1, kmax) if en[k] >= 1.0)
        kstar = k1 + math.log(en[k1]) / math.log(en[k1] / en[k1 + 1])
        levels = []
        for k in range(k1 - 3, k1 + 5):
            obs_pairs = sum(c for h, c in hist.items() if h >= k) / m
            levels.append({"k": k, "freq_M_ge_k": sum(1 for x in ms if x >= k) / m, "mean_pairs_ge_k": obs_pairs,
                           "EN_exact": en[k]})
        profile = []
        for dd in sorted(hist):
            exact = en[dd] - en[dd + 1]
            profile.append({"d": dd, "mean_pairs_observed": hist[dd] / m, "mean_pairs_exact": exact})
        row = {"n": n, "graphs": m, "mean_M": mean, "sd_M": sd, "se_mean_M": sd / math.sqrt(m), "min_M": min(ms),
               "max_M": max(ms), "mean_R": sum(rs) / m, "alpha_log_n": ALPHA * math.log(n), "b_n": b(n),
               "k_star": kstar, "M_counts": {str(v): ms.count(v) for v in sorted(set(ms))}, "levels": levels,
               "profile": profile}
        out.append(row)
        print("n=%d graphs=%d  M: mean %.3f (s.e. %.3f) sd %.3f range %d..%d   R: mean %.3f   alpha log n %.2f  "
              "b_n %.2f  k* %.2f  mean M - k* %.2f"
              % (n, m, mean, sd / math.sqrt(m), sd, min(ms), max(ms), sum(rs) / m, ALPHA * math.log(n), b(n), kstar,
                 mean - kstar))
        for lv in levels:
            print("    k=%d  freq(M>=k)=%.4f  mean pairs>=k: observed %.4f  exact %.4f"
                  % (lv["k"], lv["freq_M_ge_k"], lv["mean_pairs_ge_k"], lv["EN_exact"]))
        bulk = [p for p in profile if p["mean_pairs_exact"] >= 0.01 * n * (n - 1) / 2]
        print("    hopcounts holding at least one per cent of the pairs: largest relative difference between the "
              "observed and the exact mean %.4f"
              % max(abs(p["mean_pairs_observed"] / p["mean_pairs_exact"] - 1.0) for p in bulk))
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as fh:
            json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
