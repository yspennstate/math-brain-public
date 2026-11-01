"""Lightweight artifact checks; mathematical controls run only with a fresh green governor."""
from pathlib import Path
import collections
import datetime
import json
import math
import time
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
start = time.perf_counter()
checks = []


def check(name, predicate):
    if not predicate:
        raise AssertionError(name)
    checks.append(name)


before = json.loads((ROOT / "SOURCE_ROW_BEFORE.json").read_text(encoding="utf-8"))
after = json.loads((ROOT / "SOURCE_ROW_AFTER.json").read_text(encoding="utf-8"))
patch = (ROOT / "patches/01_C0120_source_scope.diff").read_text(encoding="utf-8").splitlines()
check("one exact target row", before["problem_id"] == after["problem_id"] == "C0120")
check("patch before matches recorded row", json.loads(patch[3][1:]) == before)
check("patch after matches proposed row", json.loads(patch[4][1:]) == after)
check("patch touches only line 120", patch[2] == "@@ -120 +120 @@" and len(patch) == 5)
check("proposed statement is ground state", "M_n" in after["statement"] and "log Z_n" not in after["statement"])
check("proposed statement fixes model", "standard Gaussian" in after["statement"] and "east/north" in after["statement"])
check("proposed row does not certify openness", "UNKNOWN" in after["status_search"] and after["current_status"] == "unverified")
check("proposed row preserves audit gate", after["verification"] == "unreviewed" and after["result_status"] == before["result_status"])
check("unrelated fields preserved", all(after[k] == v for k, v in before.items() if k not in {"statement", "status_search", "locator"}))

issues_before = {"observable": "log Z_n" in before["statement"],
                 "dimension": "general dimension" in before["statement"],
                 "weight_scope": "general weights" in before["status_search"]}
issues_after = {"observable": "log Z_n" in after["statement"],
                "dimension": "general dimension" in after["statement"],
                "weight_scope": "general weights" in after["status_search"]}
check("three source-scope mismatches removed", sum(issues_before.values()) == 3 and not any(issues_after.values()))

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
check("seven unique claim rows", len(claims) == len({c["id"] for c in claims}) == 7)
for claim in claims:
    check(claim["id"] + " fields", all(claim.get(k) for k in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status")))
    check(claim["id"] + " honest review", claim["status"] != "independently checked proof" and not claim["novelty_claim"])

bundle = json.loads((ROOT / "bundle_001.json").read_text(encoding="utf-8"))
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {e["key"] for e in bundle["entries"]}
check("bundle spec and cardinality", bundle["spec"] == "mathbrain-draft-v1" and len(keys) == len(bundle["entries"]) == 7)
for e in bundle["entries"]:
    check(e["key"] + " schema", required <= e.keys())
    check(e["key"] + " draft only", e["kind"] == "concept" and e["proof_text"] is None and e["statement"].startswith("DRAFT;"))
    check(e["key"] + " accepted own-work tag", e["source"]["license"].startswith("owner-own-work"))
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
graph = {key: [] for key in keys}
for rel in bundle["relations"]:
    check("relation endpoints " + rel["from_key"] + "/" + rel["to_key"], rel["from_key"] in keys and rel["to_key"] in keys and rel["kind"] in allowed and bool(rel["rationale"]))
    if rel["kind"] == "depends_on":
        graph[rel["from_key"]].append(rel["to_key"])


def visit(node, ancestors):
    check("acyclic " + node, node not in ancestors)
    for nxt in graph[node]:
        visit(nxt, ancestors | {node})


for key in keys:
    visit(key, set())
inbox = Path("~/math-brain-inbox/w495/bundle_001.json")
check("complete inbox matches local draft", json.loads(inbox.read_text(encoding="utf-8")) == bundle)
status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
check("separate pipeline states", status["brain_pipeline"] == {"prepared": True, "submitted": True, "reviewed": False, "ingested": False, "retrievable": False})
hook = json.loads((ROOT / "hooks/math-w495.jsonl").read_text(encoding="utf-8"))
check("hook length and evidence", len(hook["text"]) <= 300 and all(hook.get(k) for k in ("cue", "fire_when", "silent_when", "evidence")))

state_file = Path("~/.claude/compute/compute_state.json")
governor = json.loads(state_file.read_text(encoding="utf-8-sig"))
stamp = datetime.datetime.strptime(governor["ts"], "%Y-%m-%d %H:%M:%S")
age = (datetime.datetime.now() - stamp).total_seconds()
gate = {k: governor.get(k) for k in ("ts", "host", "status", "mode", "reasons", "cpu_pct", "mem_avail_mb", "mem_load_pct", "commit_used_pct", "disk_free_gb", "proc_count")}
gate["age_seconds_at_read"] = age
green = 0 <= age <= 60 and governor.get("status") not in {"distress", "critical"} and governor.get("mode") != "throttle" and governor.get("cpu_pct", 100) < 85 and governor.get("mem_avail_mb", 0) > 8192 and governor.get("commit_used_pct", 100) < 85
gate["mathematical_controls_allowed"] = green
controls = {"status": "SKIPPED_RESOURCE_GATE", "cases": 0, "note": "No numerical experiment or graph replay runs unless this exact fresh gate is green."}
if green:
    graph_cases = []
    for r in range(1, 7):
        m = n = 2**r
        paths = []
        for leaf in range(m):
            path = [("tree", k, leaf // 2**(r-k)) for k in range(r)]
            path += [("chain", leaf, j) for j in range(n)]
            paths.append(path)
        occupancy = collections.Counter(v for path in paths for v in path)
        first = sum((Fraction(count, m)**2 for count in occupancy.values()), Fraction())
        check("exact graph first chaos r=" + str(r), first == Fraction(3) - Fraction(2, m))
        check("equal path lengths r=" + str(r), all(len(p) == n+r for p in paths))
        adjacency = collections.defaultdict(set)
        for path in paths:
            for x, y in zip(path, path[1:]):
                adjacency[x].add(y)
        check("bounded outdegree r=" + str(r), max(map(len, adjacency.values())) <= 2)
        graph_cases.append({"r": r, "paths": m, "vertices": len(occupancy), "path_length": n+r, "first_chaos_exact": str(first)})
    ratios = []
    threshold = (2/5)*math.exp(-1.5)
    for i in range(705):
        t = 1 + i/64
        q = lambda x: math.erfc(x/math.sqrt(2))/2
        ratio = q(t+1/t)/q(t)
        check("Mills ratio control " + str(i), ratio >= threshold*(1-1e-12))
        ratios.append(ratio)
    controls = {"status": "PASS_LIMITED_CONTROLS", "cases": len(graph_cases)+len(ratios), "graph_cases": graph_cases, "mills_ratio_min": min(ratios), "mills_ratio_bound": threshold, "note": "Finite exact graph identities and floating-point tail controls are not an asymptotic theorem certificate."}

measurements = {"command": "python -X utf8 validate_packet.py", "source_scope_mismatches_before": sum(issues_before.values()), "source_scope_mismatches_after": sum(issues_after.values()), "artifact_checks_passed": len(checks), "claim_rows": len(claims), "draft_entries": len(bundle["entries"]), "draft_relations": len(bundle["relations"]), "mathematical_controls": controls, "compute_gate": gate, "elapsed_seconds": time.perf_counter()-start, "math_review": "pending; artifact checks do not prove the lemmas"}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(measurements, indent=2) + "\n", encoding="utf-8")
print(json.dumps(measurements, indent=2))
