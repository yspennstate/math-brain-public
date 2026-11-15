"""Small standard-library verifier for the saved finite certificate and reports."""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c


def main():
    summary = json.loads((ROOT / "summary.json").read_text())
    audit = json.loads((ROOT / "audit.json").read_text())
    exact = json.loads((ROOT / "exact_a5.json").read_text())
    assert sum(x["weighted_pairs"] for x in summary["summaries"]) == 15016
    assert sum(x["representative_pairs"] for x in summary["summaries"]) == 982
    assert all(x["histogram_matches"] and x["counts_match"] and x["miss_counts_match"]
               for x in audit["checks"])
    rows = list(csv.DictReader((ROOT / "exact_a5_newton.csv").open()))
    assert len(rows) == 61
    cs = [int(r["charpoly_coefficient"]) for r in rows]
    ts = [int(r["trace_A_power"]) for r in rows]
    for k in range(1, 61):
        assert int(rows[k]["word_returns"]) * 60 == ts[k]
        assert k * cs[k] + sum(cs[k-j] * ts[j] for j in range(1, k+1)) == 0
    factors = [([1, -4], 1), ([1, -1], 4), ([1, 1], 4), ([1, 0], 6),
               ([1, -5, 5], 3), ([1, 0, -5], 4), ([1, 3, 1], 8),
               ([1, -1, -7, 4], 5)]
    expanded = [1]
    for f, multiplicity in factors:
        for _ in range(multiplicity):
            expanded = multiply(expanded, f)
    assert cs == expanded
    pairs = list(csv.DictReader((ROOT / "pairs.csv").open()))
    witness = next(r for r in pairs if r["n"] == "5" and r["sigma"] == "0 1 3 4 2"
                   and r["tau"] == "4 2 0 1 3")
    assert abs(float(witness["gap"]) - (3-math.sqrt(5))/8) < 1e-13
    assert abs(float(witness["natural_gap"]) - (1-math.sqrt(5)/4)) < 1e-13
    assert exact["full_charpoly_matches_word_return_newton"]
    assert exact["four_distinct_generators"] and exact["group_order"] == 60
    assert (ROOT / "REPORT.md").read_text().splitlines()[0].startswith("VERDICT: COMPUTED ")
    for name in ("LOG.md", "PROOF.md", "REPORT.md", "SOLVED_ELSEWHERE.md", "pairs.csv",
                 "summary.json", "audit.json", "exact_witness.json", "exact_a5.json",
                 "exact_a5_newton.csv"):
        assert (ROOT / name).stat().st_size > 0
    print("PASS: 15016 pairs; 982 weighted representatives; all audit comparisons match.")
    print("PASS: all 60 Newton identities and integer expansion of the reported factorization.")
    print("PASS: exact radical gaps agree with the independently enumerated A5 witness.")
    print("PASS: required reports and data are present; verdict is COMPUTED.")
    print("gap_A5 =", (3-math.sqrt(5))/8, "natural_gap =", 1-math.sqrt(5)/4)
    print("latest_exact_run_seconds =", exact["elapsed_seconds"],
          "rss_bytes =", exact["peak_rss_bytes"])


if __name__ == "__main__":
    main()
