"""Prepare a small, unpromoted mathematical DRAFT; submission is a separate step."""
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
source = {
    "source_id": "owner-own-work:critical-tree-energy-obstruction",
    "url": None,
    "revision": "independent-derivation-2026-10-10-review-pending",
    "license": "owner-own-work",
    "excerpt": None,
}
def entry(key, logical_name, title, statement, assumptions):
    return {
        "key": key, "namespace": "probability.percolation", "logical_name": logical_name,
        "kind": "concept", "title": title, "statement": statement, "proof_text": None,
        "assumptions": assumptions, "domain": "probability theory", "source": dict(source),
    }

entries = [
    entry(
        "dyadic-tree",
        "dyadic-burst-tree-critical-survival-obstruction",
        "Draft boundary example: bounded degree does not imply critical extinction",
        "Independent review pending. Let T be the rooted tree in which each vertex at level n-1 has 8 children if n is a power of two and 2 children otherwise, for n>=1. T is infinite, connected, simple and locally finite, with maximum degree 9. For iid Bernoulli bond percolation, p_c(T)=1/2 and the root survives at criticality with probability at least 4/5. At p=1/2 the open generation mean is M_n=4^(1+floor(log_2 n)), and its normalized second moment is 1+(1/2)sum_{j<=n}1/M_j<=5/4. Two independent uniform-child rays on the host have E[2^K]=5/4, where K counts their common undirected edges. Below 1/2, M_n<=4n^2(2p)^n tends to zero. The degree-8 root is unique, so every automorphism fixes it and T has infinitely many vertex orbits. This example excludes replacing quasi-transitivity by bounded degree; it does not refute critical extinction on quasi-transitive graphs.",
        ["The exact dyadic offspring schedule stated here", "Independent Bernoulli bond percolation"]
    ),
    entry(
        "critical-fragility",
        "critical-components-have-unit-quenched-thinning-threshold",
        "Draft thinning fact: surviving critical components have threshold one",
        "Independent review pending. Let G be a countable connected locally finite graph with p_c(G)>0 and sample iid Bernoulli bond percolation at p_c(G). Almost surely every infinite open component C, regarded as a fixed graph after conditioning on the sampled field, has quenched bond threshold p_c(C)=1. For rational r<1, independent r-thinning of the sampled open bonds is unconditionally iid bond percolation at p_c(G)r<p_c(G), so its probability of any infinite component is zero. Conditioning, then intersecting over rational r and using monotonicity, proves simultaneous failure of percolation below r=1 on every C. Infinitude of C alone therefore supplies no robustness under thinning.",
        ["G countable, connected and locally finite", "p_c(G)>0", "Independent bond retention and independent subsequent thinning"]
    ),
    entry(
        "failed-transfer",
        "finite-host-ray-energy-does-not-transfer-to-critical-cluster",
        "Draft refuted inference: host ray energy passes to critical clusters",
        "Independent review pending. The proposed implication 'finite common-edge ray energy on a host graph implies that a surviving critical component inherits finite ray energy at some thinning retention r<1' is false without an additional structural premise. For two independent rays from a Borel ray measure mu write I_r(mu)=E[r^(-K)], where K counts common undirected edges. On the dyadic-burst tree, the uniform-child host measure has I_(1/2)=5/4 and critical root survival probability is at least 4/5. Nevertheless almost surely every infinite critical component C has p_c(C)=1. Such C admits no ray measure with finite I_r for r<1: the open-prefix second-moment argument would give positive percolation probability at r, a contradiction. The host is not quasi-transitive; this refutes unconditional inheritance and leaves a quasi-transitive structural premise unproved.",
        ["The dyadic-burst tree defined in this bundle", "Ray measures are on infinite simple rays of the graph in question", "Independent critical percolation and independent thinning"]
    ),
]
relations = [
    {
        "from_key": "dyadic-tree", "to_key": "failed-transfer", "kind": "refutes",
        "rationale": "The first endpoint supplies an explicit host with finite ray energy and positive critical survival; the third endpoint states the false unconditional inheritance implication and identifies its failure on that same host."
    },
    {
        "from_key": "failed-transfer", "to_key": "critical-fragility", "kind": "depends_on",
        "rationale": "Threshold one of every surviving critical component, combined with the open-prefix ray-energy sufficient condition, excludes finite energy for every retention below one."
    },
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w436", "bundle_slug": "critical-tree-energy-obstruction-20261010", "entries": entries, "relations": relations}
existing = None
existing_path = ROOT / "EXISTING_TARGET_CARD.json"
if existing_path.is_file():
    existing = json.loads(existing_path.read_text(encoding="utf-8"))
    assert existing["logical_id"] == "math:probability.core:open-problem-p0043-absence-of-infinite-clusters-at-critical-percolation"
    relations.append({
        "from_key": "dyadic-tree",
        "to_existing_logical": existing["logical_id"],
        "kind": "semantic_association",
        "rationale": "Both endpoints concern infinite clusters at the critical parameter. The new example tests why the quasi-transitive hypothesis in the existing conjecture cannot simply be replaced by bounded degree; its graph explicitly lies outside that hypothesis and does not refute the conjecture.",
    })
for item in entries:
    assert item["kind"] == "concept" and item["proof_text"] is None
    assert item["source"]["license"].startswith("owner-own-work")
assert len({item["key"] for item in entries}) == 3
keys = {item["key"] for item in entries}
assert all(rel["from_key"] in keys and (rel.get("to_key") in keys or (existing is not None and rel.get("to_existing_logical") == existing["logical_id"])) for rel in relations)
edge_rows = []
by_key = {item["key"]: item for item in entries}
for index, rel in enumerate(relations, 1):
    edge_rows.append({
        "row_id": f"S1.1.P0043-w436-E{index}",
        "from_card_quote": by_key[rel["from_key"]]["statement"],
        "to_card_quote": by_key[rel["to_key"]]["statement"] if "to_key" in rel else existing["body"],
        "relation": rel,
        "support": "INDEPENDENT_DERIVATION.md and AUDIT_w435.md; C1/C2 in CLAIMS.jsonl",
        "independent_reviewer": "w437 (pending)",
        "status": "draft concept relation, not yet independently checked",
    })
(ROOT / "EDGE_EVIDENCE.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False)+"\n" for row in edge_rows), encoding="utf-8")
drafts = ROOT / "drafts"
drafts.mkdir(exist_ok=True)
prepared = drafts / "bundle_001.json"
prepared.write_text(json.dumps(bundle, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
hook = {
    "id": "critical-graph-hypotheses-w436-01", "area": "math", "event": "stage-start",
    "cue": "A critical-percolation proof replaces quasi-transitivity by bounded degree or by a host-tree growth rate.",
    "fire_when": "An argument claims critical extinction from bounded degree and p_c<1 without checking finitely many automorphism orbits.",
    "silent_when": "The exact graph class is verified, or the degree-9 critical-survival tree is explicitly treated as non-quasi-transitive.",
    "text": "Bounded degree does not imply quasi-transitivity. A degree-9 tree has p_c=1/2 and critical survival at least 4/5. Check the automorphism orbits before applying critical-extinction results.",
    "evidence": "INDEPENDENT_DERIVATION.md C1; MEASUREMENTS.json: 4095 generations, zero failures, exact second-moment bound 5/4.",
    "proposer": "w436",
}
assert len(hook["text"]) <= 300
hook_text = json.dumps(hook, ensure_ascii=False)+"\n"
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hook_text, encoding="utf-8")
patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
live_name = "~/primary_directive/hooks1000/proposals/math-w436.jsonl"
patch = "".join(difflib.unified_diff([], hook_text.splitlines(keepends=True), fromfile="a/"+live_name, tofile="b/"+live_name))
(patches / "01_critical_graph_hypotheses_hook.diff").write_text(patch, encoding="utf-8")
print(json.dumps({"prepared":str(prepared),"entries":len(entries),"relations":len(relations),"all_kinds":"concept","hook_staged_only":True}), flush=True)
