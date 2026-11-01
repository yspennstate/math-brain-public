"""Independent bounded exact checks of w570's collision and corank routes."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import time
from verify_boundaries import rank

ROOT = Path(__file__).resolve().parent


def stirling(n):
    values = [1]
    for k in range(1, n + 1):
        nxt = [0] * (k + 1)
        for j in range(1, k + 1):
            nxt[j] = (values[j - 1] if j - 1 < len(values) else 0) - (k - 1) * (values[j] if j < len(values) else 0)
        values = nxt
    return values


def main():
    started = time.perf_counter()
    source = Path("~/brain_workers/w570/ATTEMPT.md")
    raw = source.read_bytes()
    snapshot = ROOT / "source_snapshots/w570_ATTEMPT_audited.md"
    snapshot.parent.mkdir(exist_ok=True)
    snapshot.write_bytes(raw)
    counts = []
    for n in range(1, 5):
        collision_count = cross_count = row_count = column_count = 0
        for bits in product((0, 1), repeat=(n - 1)**2):
            d = [[0] * n for _ in range(n)]
            for k, bit in enumerate(bits):
                d[1 + k // (n - 1)][1 + k % (n - 1)] = bit
            rows = [tuple(row) for row in d]
            columns = [tuple(row[j] for row in d) for j in range(n)]
            collision_count += len(set(rows)) < n or len(set(columns)) < n
            if n >= 2:
                r = rows[0] == rows[1]
                c = columns[0] == columns[1]
                row_count += r
                column_count += c
                cross_count += r and c
        total = 2**((n - 1)**2)
        s = stirling(n)
        complementary = sum(s[a] * s[b] * 2**((a - 1) * (b - 1)) for a in range(1, n + 1) for b in range(1, n + 1))
        assert collision_count == total - complementary
        if n >= 2:
            assert Fraction(row_count, total) == Fraction(1, 2**(n - 1))
            assert Fraction(column_count, total) == Fraction(1, 2**(n - 1))
            assert Fraction(cross_count, total) == 2 * Fraction(row_count, total) * Fraction(column_count, total)
        counts.append({"n": n, "normalized_matrices": total, "collision_count": collision_count,
                       "collision_probability": str(Fraction(collision_count, total)),
                       "specified_cross_pair_count": cross_count})

    corank_checks = []
    t4 = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    for n in range(5, 13):
        d = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(4):
            for j in range(4):
                d[i][j] = t4[i][j]
        for i in range(4, n - 1):
            d[i][i] = 1
        b = [[1] * n] + [[1] + [1 - 2 * x for x in row] for row in d]
        assert rank(b) == n - 1
        assert len({tuple(r) for r in b}) == n
        assert len({tuple(r[j] for r in b) for j in range(n)}) == n
        kernel = [0, 1, -1, -1, 1] + [0] * (n - 5)
        assert all(sum(x * y for x, y in zip(row, kernel)) == 0 for row in b)
        corank_checks.append({"n": n, "rank": n - 1, "no_projective_collisions": True,
                              "kernel_support": 4})

    # P2's missing dimension premise: n=1, epsilon=1 is inside [0,sqrt(2)).
    assert 1 < math.sqrt(2) and abs(1) <= 1
    result = {"verdict": "PASS", "fresh_gate": {"max_collision_dimension": 4,
               "max_normalized_matrices": 512, "max_corank_dimension": 12,
               "no_gpu_or_external_compute": True},
              "author_artifact": str(source), "author_artifact_sha256": hashlib.sha256(raw).hexdigest(),
              "snapshot": str(snapshot), "collision_checks": counts, "corank_checks": corank_checks,
              "P2_boundary": "FIX: add n>=2 to the support-at-most-two witness equivalence; n=1,epsilon=1 disproves the unqualified sentence.",
              "scope": "Exact bounded checks accompany the direct mathematical audit; they are not a proof of C0029 or a served-model receipt.",
              "elapsed_seconds": time.perf_counter() - started}
    (ROOT / "PEER_MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": "PASS", "normalized_matrices": sum(c["normalized_matrices"] for c in counts),
                      "corank_dimensions": 8, "P2_boundary": "FIX", "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
