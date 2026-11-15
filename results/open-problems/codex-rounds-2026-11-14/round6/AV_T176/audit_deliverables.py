"""Audit quotations and independently recount finite checks using deck orders."""

from fractions import Fraction
import json
import os
from pathlib import Path
import re
import resource

ROOT = Path(__file__).resolve().parent
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
verify = (ROOT / "VERIFY.md").read_text()
quotes = 0
for name, expected in [("optimal", 1), ("compatibility", 3), ("routing", 1)]:
    source = (ROOT / "sources" / (name + ".tex")).read_text()
    environments = re.findall(
        r"\\begin\{(?:theorem|corollary)\}[\s\S]*?\\end\{(?:theorem|corollary)\}", source)
    assert len(environments) == expected
    for environment in environments:
        assert verify.count(environment) == 1
        quotes += 1
for name in ("optimal", "compatibility-header", "routing-header"):
    source = (ROOT / "sources" / (name + ".tex")).read_text()
    assert r"\author{OpenAI}" in source
    assert r"\date{September 26, 2026}" in source
for name in ("LOG.md", "PROOF.md", "VERIFY.md", "REPORT.md"):
    source = (ROOT / name).read_text()
    assert not any(ord(c) < 32 and c not in "\n\t" for c in source)
assert (ROOT / "REPORT.md").read_text().startswith("VERDICT: PARTIAL ")


def drop(deck, coin):
    h = len(deck)//2
    result = []
    for j in range(h):
        if (coin >> j) & 1:
            result += [deck[h+j], deck[j]]
        else:
            result += [deck[j], deck[h+j]]
    return tuple(result)


saved = json.loads((ROOT / "check-output.json").read_text())
supports = {}
equalities = 0
cases = 0
for item in saved["endpoint_checks"]:
    n, t = item["n"], item["t"]
    if (n, 0) not in supports:
        supports[n, 0] = {tuple(range(n))}
    for s in range(1, t+1):
        if (n, s) not in supports:
            supports[n, s] = {drop(deck, c) for deck in supports[n, s-1]
                              for c in range(1 << (n//2))}
    masks = (list(range(1 << n)) if not (n == 8 and t == 3)
             else [0, 1, 15, 85, 129, 170, 254, 255])
    # Each reachable exposed endpoint tuple creates exactly N rows x N
    # initial basis columns in the main script's complete joint-test table.
    count = 0
    for B in masks:
        exposed = [x for x in range(n) if not ((B >> x) & 1)]
        possible = {tuple(deck.index(x) for x in exposed) for deck in supports[n, t]}
        count += n*n*len(possible)
    assert count == item["basis_indicator_equalities"], (n, t, count)
    history_cases = len(masks) * 2**(t*n//2)
    assert history_cases == item["history_mask_cases"]
    assert item["max_error"] == 0
    equalities += count
    cases += history_cases
assert equalities == saved["total_basis_indicator_equalities"] == 2536256
assert cases == saved["total_history_mask_cases"] == 103884
assert cases == 4*31 + 16*341 + 256*256 + 8*4096
assert sum(x["path_cylinders"] for x in saved["path_checks"]) == 5729
assert all(x["max_error"] == 0 for x in saved["path_checks"])
assert Fraction(saved["invalid_variants"]["free_exposed_point"]["direct"]) - Fraction(
    saved["invalid_variants"]["free_exposed_point"]["flow"]) == Fraction(1, 2)
assert saved["max_rss_bytes"] < 256*1024**2
print(json.dumps({"exact_quotes": quotes, "headers": 3,
                  "independent_history_set_recount": cases,
                  "independent_basis_indicator_recount": equalities,
                  "full_path_groups": 5729,
                  "max_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "status": "passed; deck-support recount uses no flow implementation"}, indent=2))
