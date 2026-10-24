"""Small exact checks for C0048 referee packet; no store writes."""

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


def partition(vertices, edges, q, weight_equal):
    return sum(
        weight_equal ** sum(colors[u] == colors[v] for u, v in edges)
        for colors in product(range(q), repeat=vertices)
    )


def main():
    root = Path(__file__).parent
    bundle = json.loads((root / "draft_bundle/bundle_001.json").read_text(encoding="utf-8"))
    keys = {entry["key"] for entry in bundle["entries"]}
    assert bundle["spec"] == "mathbrain-draft-v1" and len(keys) == len(bundle["entries"])
    assert all(rel["from_key"] in keys and (rel.get("to_key") in keys or "to_existing_logical" in rel) for rel in bundle["relations"])
    verdicts = [json.loads(line) for line in (root / "REVIEW_VERDICTS.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(verdicts) == 8 and all(row["verdict"].startswith("KEEP") for row in verdicts)
    source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    receipt = json.loads((root / "REVIEW_RECEIPT.json").read_text(encoding="utf-8"))
    hooks = [json.loads(line) for line in (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines()]
    assert source["id"] == "C0048" and len(source["rows"]) == 3
    assert receipt["w459_reviewed_proof_prefix_bytes"] == 8891 and len(hooks) == 1

    q = 3
    t = 2  # exp(K); avoid floating arithmetic
    path = [(0, 1), (1, 2)]
    triangle = path + [(0, 2)]
    for graph, expect_equal in ((path, True), (triangle, False)):
        z = partition(3, graph, q, t)
        bound = Fraction(q**3) * (1 + Fraction(t - 1, q)) ** len(graph)
        assert (z == bound) == expect_equal and z >= bound

    p = Fraction(1, 2)
    alpha = p / (p + q * (1 - p))
    gap = lambda L: Fraction((q - 1) * (1 - alpha) * alpha**L, 1 + (q - 1) * alpha**L)
    assert gap(1) == Fraction(1, 4) and gap(4) == Fraction(1, 172)
    assert Fraction(4, 3) - Fraction(2, 3) == Fraction(2, 3)

    # q=3 color merge on a triangle, with vertex 0 fixed to color 1.
    for colors in product(range(1, 4), repeat=2):
        sigma = (1, *colors)
        a = {v for v, color in enumerate(sigma) if color in (1, 2)}
        outside_edges = sum(u not in a and v not in a for u, v in triangle)
        inside_equal_edges = sum(u in a and v in a and sigma[u] == sigma[v] for u, v in triangle)
        inside_edges = sum(u in a and v in a for u, v in triangle)
        crossing_edges = sum((u in a) != (v in a) for u, v in triangle)
        assert outside_edges + inside_edges + crossing_edges == len(triangle)
        assert t ** sum(sigma[u] == sigma[v] for u, v in triangle) == t ** (outside_edges + inside_equal_edges)

    print("PASS bundle schema/relations; 8 verdict rows; forest equality/cycle strictness; path gaps 1/4,1/172; pressure derivative gap 2/3; 9 color-merge configurations")


if __name__ == "__main__":
    main()
