"""Finite checks for worker 064's elementary scope reductions, not the preprint.

Run from research-session: python3 computations/064_scope_checks.py
Uses only the standard library. It does not test the hereditary small-ball theorem.
"""
import hashlib
import json
import math
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def adj(a):
    return [[x.conjugate() for x in row] for row in zip(*a)]


def realify(a):
    n = len(a)
    return [[int(a[i % n][j % n].real) if (i < n) == (j < n)
             else (-1 if i < n else 1) * int(a[i % n][j % n].imag)
             for j in range(2 * n)] for i in range(2 * n)]


def main():
    rng = random.Random(640828)
    algebra_cases = 0
    for n in range(1, 9):
        for _ in range(75):
            a = [[complex(rng.randint(-4, 4), rng.randint(-4, 4)) for _ in range(n)] for _ in range(n)]
            b = [[complex(rng.randint(-4, 4), rng.randint(-4, 4)) for _ in range(n)] for _ in range(n)]
            assert realify(mul(a, b)) == mul(realify(a), realify(b))
            assert realify(adj(a)) == [list(row) for row in zip(*realify(a))]
            h = [[a[i][j] + a[j][i].conjugate() for j in range(n)] for i in range(n)]
            assert realify(h) == [list(row) for row in zip(*realify(h))]
            algebra_cases += 1

    # All entries and products above are Gaussian integers well below 2**53.
    # Native complex arithmetic is therefore exact for these finite checks.
    dyadic_cases = 0
    max_ratio = 0.0
    ln2 = math.log(2)
    for n in range(1, 257):
        for m in range(1, n + 1):
            # Exact integer bucket j=floor(log2(n/m)), avoiding floating logs.
            j = 0
            while (m << (j + 1)) <= n:
                j += 1
            assert (m << j) <= n < (m << (j + 1))
            for aspect in (1, 2, 10, 1000000):
                ell = 1 + math.log(2 * aspect)
                lhs = math.sqrt(m) * (ell + math.log(n / m)) ** 2
                rhs = math.sqrt(n) * 2 ** (-j / 2) * ell ** 2 * (j + 2) ** 2
                assert lhs <= rhs * (1 + 1e-12)
                max_ratio = max(max_ratio, lhs / rhs)
                dyadic_cases += 1

    r = 1 / math.sqrt(2)
    series_closed = (4 - 3 * r + r * r) / (1 - r) ** 3
    series_partial = sum(r ** j * (j + 2) ** 2 for j in range(300))
    assert math.isclose(series_closed, series_partial, rel_tol=1e-14)

    inputs = []
    original_paths = {
        "computations/005_sources/index_master_index.tex": "index/master_index.tex",
        "computations/005_sources/universal_family_obstruction.tex": "paper12/universal_family_obstruction.tex",
    }
    tree = json.loads((ROOT / "repository-tree.json").read_text())["tree"]
    blobs = {x["path"]: x for x in tree}
    for rel in list(original_paths) + ["agents/005.md", "agents/040.md", "agents/043.md"]:
        raw = (ROOT / rel).read_bytes()
        item = {"path": rel, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
        if rel in original_paths:
            path = original_paths[rel]
            item["baseline_path"] = path
            item["baseline_git_blob"] = blobs[path]["sha"]
            item["baseline_bytes"] = blobs[path]["size"]
            trimmed = raw[:-1]
            trimmed_sha = hashlib.sha1(b"blob " + str(len(trimmed)).encode() + b"\0" + trimmed).hexdigest()
            item["cache_equals_baseline_after_removing_one_final_byte"] = trimmed_sha == blobs[path]["sha"]
            assert raw[-1:] == b"\n" and item["cache_equals_baseline_after_removing_one_final_byte"]
        inputs.append(item)

    out = {
        "status": "PASSED_BOUNDED_SCOPE_CHECKS_ONLY",
        "seed": 640828,
        "realification_algebra_cases": algebra_cases,
        "dyadic_radius_cases": dyadic_cases,
        "max_dyadic_lhs_over_rhs": max_ratio,
        "series_closed_form": "(4-3*r+r*r)/(1-r)^3, r=1/sqrt(2)",
        "series_closed_numeric": series_closed,
        "series_partial_300_terms": series_partial,
        "inputs": inputs,
        "not_checked": [
            "Theorem 1.3 hereditary small-ball proof",
            "matrix-weighted Poincare and curvature estimates",
            "randomized algorithm implementation or bit complexity",
            "operator norms by numerical eigensolvers",
            "optimal rectangular Matrix Spencer bound",
        ],
    }
    dest = ROOT / "computations/064_scope_checks_output.json"
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
