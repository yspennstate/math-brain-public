"""Builds the two tables of the paper from the output of dim_check.py.

usage: python make_tables.py data/dim_200k.json tables.tex
"""
import json
import math
import sys

NAMES = {
    "half_1_2": r"$p_1=p_2=\tfrac12$",
    "half_2_4": r"$p_2=p_4=\tfrac12$",
    "third_1_2_3": r"$p_1=p_2=p_3=\tfrac13$",
    "geometric_half": r"$p_k=2^{-k}$",
}


def mean_se(xs):
    n = len(xs)
    mu = sum(xs) / n
    var = sum((x - mu) ** 2 for x in xs) / (n - 1)
    return mu, math.sqrt(var / n)


def main():
    res = json.load(open(sys.argv[1]))
    out = []
    worst_se = 0.0
    monotone = True
    out.append(r"\begin{table}[ht]\centering\small")
    out.append(r"\begin{tabular}{lccccc}\toprule")
    out.append(r"offspring law & $m$ & $d_0$ & $d_0'$ & pool average & quotient \\ \midrule")
    for name, law in res["laws"].items():
        ex = law["exact"]
        rows = {r["frac"]: r for r in law["rows"]}
        dd0, se0 = mean_se(rows[0.0]["dd"])
        h = rows[0.02]["lam"]
        quot = [(a - b) / h for a, b in zip(rows[0.02]["d"], rows[0.0]["d"])]
        q, seq = mean_se(quot)
        out.append("%s & %.3f & %.5f & %.5f & $%.5f\\pm%.5f$ & $%.5f\\pm%.5f$ \\\\" % (
            NAMES[name], ex["m"], ex["d0"], ex["slope0"], dd0, se0, q, seq))
        prev = None
        for r in law["rows"]:
            worst_se = max(worst_se, mean_se(r["d"])[1])
            if prev is not None:
                monotone = monotone and all(a > b for a, b in zip(r["d"], prev["d"]))
            prev = r
    out.append(r"\bottomrule\end{tabular}")
    out.append(r"\caption{The slope at $\lambda=0$. The fourth column is~\eqref{eq:slope}, the fifth is the pool "
               r"average of the right-hand side of~\eqref{eq:quot} at $\lambda=0$, and the last is "
               r"$(d_{\lambda}-d_0)/\lambda$ at $\lambda=0.02\,m$; the last two are means over six seeds with their "
               r"standard errors.}\label{tab:slope}")
    out.append(r"\end{table}")
    out.append("")
    fr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    out.append(r"\begin{table}[ht]\centering\footnotesize\setlength{\tabcolsep}{4pt}")
    out.append(r"\begin{tabular}{l" + "c" * len(fr) + r"}\toprule")
    out.append(r"$\lambda/m$ & " + " & ".join("%.1f" % f for f in fr) + r" \\ \midrule")
    for name, law in res["laws"].items():
        rows = {r["frac"]: r for r in law["rows"]}
        out.append(NAMES[name] + " & " + " & ".join("%.4f" % mean_se(rows[f]["d"])[0] for f in fr) + r" \\")
    out.append(r"\bottomrule\end{tabular}")
    out.append(r"\caption{Estimates of $d_\lambda$, means over six seeds. The standard errors, over the whole grid, "
               r"are at most $%.5f$.}\label{tab:dim}" % worst_se)
    out.append(r"\end{table}")
    open(sys.argv[2], "w").write("\n".join(out) + "\n")
    print("monotone in every seed along the grid:", monotone)
    print("largest standard error:", worst_se)
    for name, law in res["laws"].items():
        print(name, law["exact"])


if __name__ == "__main__":
    main()
