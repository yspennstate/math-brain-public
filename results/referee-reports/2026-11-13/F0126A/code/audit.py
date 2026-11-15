"""Independent short-path checks and artifact checks for the F0126 report."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
import hashlib
import itertools
import json
import math
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def main():
    size = 11
    steps = [-2, -1, 0, 1, 2]
    numerators = [2, 6, 5, 4, 3]
    probs = np.array(numerators) / 20
    assert sum(x * p for x, p in zip(steps, numerators)) == 0
    record = np.load(ROOT / "data/cycle_record_12600.npz")["observations"][:6]
    truth = json.loads((ROOT / "data/cycle_results.json").read_text())[0]["truth"]
    modified = truth.copy()
    modified[2] ^= 1
    P = np.zeros((size, size))
    for i in range(size):
        for step, prob in zip(steps, probs):
            P[i, (i + step) % size] += prob
    likelihood_checks = []
    for colors in (truth, modified, [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]):
        v = np.zeros(size)
        v[0] = colors[0] == record[0]
        normalized = v.copy()
        likelihood = float(v.sum())
        for color in record[1:]:
            v = (v @ P) * (np.array(colors) == color)
            normalized = (normalized @ P) * (np.array(colors) == color)
            norm = normalized.sum()
            likelihood *= norm
            if norm:
                normalized /= norm
        total = 0
        for seq in itertools.product(range(5), repeat=5):
            x = 0
            weight = 1
            if colors[0] != record[0]:
                continue
            for t, j in enumerate(seq, 1):
                x = (x + steps[j]) % size
                weight *= numerators[j]
                if colors[x] != record[t]:
                    break
            else:
                total += weight
        exact = total / 20 ** 5
        assert abs(exact - float(v.sum())) < 2e-15
        assert abs(exact - likelihood) < 2e-15
        likelihood_checks.append(dict(integer_path_weight=total, denominator=20 ** 5,
                                      likelihood=exact))

    # Return probabilities in a second form: direct 2D spatial DP.
    positions = {(0, 0): 1}
    for t in range(1, 21):
        nxt = {}
        for (x, y), weight in positions.items():
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                key = (x + dx, y + dy)
                nxt[key] = nxt.get(key, 0) + weight
        positions = nxt
        if t % 2 == 0:
            n = t // 2
            assert positions[(0, 0)] == math.comb(2 * n, n) ** 2

    rows = json.loads((ROOT / "data/cycle_results.json").read_text())
    successes = {str(t): sum(r["map_equivalent"] for r in rows if r["increments"] == t)
                 for t in (100, 500, 2000)}
    assert successes == {"100": 0, "500": 4, "2000": 8}
    sources = list((ROOT / "sources").iterdir())
    for p in sources:
        assert p.suffix == ".txt"
        s = p.read_text(encoding="utf-8")
        assert not any(ord(c) < 32 and c not in "\n\t\r\f" for c in s), p.name
    for row in map(json.loads, (ROOT / "data/source_manifest.jsonl").read_text().splitlines()):
        p = ROOT / "sources" / (row["slug"] + ".txt")
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row["text_sha256"], p.name
    forbidden = []
    for p in ROOT.rglob("*"):
        if p.is_file():
            if p.suffix.lower() in {".pdf", ".ps", ".dvi", ".png", ".jpg", ".jpeg", ".tiff", ".webp"}:
                forbidden.append(str(p.relative_to(ROOT)))
            with p.open("rb") as f:
                assert not f.read(8).startswith(b"%PDF"), p.name
    assert not forbidden, forbidden
    assert (ROOT / "REPORT.md").read_text().splitlines()[0] == "PARTIAL"
    out = dict(result="PASS", likelihood_checks=likelihood_checks,
               return_count_formula_checked_through=20, cycle_successes=successes,
               source_files=len(sources), source_manifest_hashes="PASS",
               forbidden_artifacts=forbidden, priority=os.getpriority(os.PRIO_PROCESS, 0))
    (ROOT / "data/audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
