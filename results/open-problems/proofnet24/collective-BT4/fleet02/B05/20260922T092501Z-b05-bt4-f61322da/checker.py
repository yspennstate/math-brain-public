#!/usr/bin/env python3
import json

def succ2(n, c):
    return {(c + 1) % n, (c + 2) % n}

violations = []
per_n = {}
examples = []

for n in range(3, 201):
    survivors = 0
    for c1 in range(n):
        for c2 in range(n):
            common = succ2(n, c1) & succ2(n, c2)
            if len(common) < 2:
                continue
            targets = set(common)
            if c1 in targets or c2 in targets:
                continue
            survivors += 1
            expected = c1 == c2 and targets == succ2(n, c1)
            if not expected:
                violations.append({
                    "n": n,
                    "c1": c1,
                    "c2": c2,
                    "targets": sorted(targets),
                })
            if len(examples) < 8:
                examples.append({
                    "n": n,
                    "c1": c1,
                    "c2": c2,
                    "targets": sorted(targets),
                })
    per_n[str(n)] = survivors

result = {
    "checked_cycle_orders": [3, 200],
    "claim": "two distinct heavy targets reachable by length-2 same-support paths through one exposed remainder vertex from each packed inport force a common inport c and targets {c+,c++}",
    "survivors_total": sum(per_n.values()),
    "per_n_all_equal_n": all(per_n[str(n)] == n for n in range(3, 201)),
    "violations": violations,
    "examples": examples,
    "status": "PASS" if not violations else "FAIL",
}
print(json.dumps(result, sort_keys=True, indent=2))
