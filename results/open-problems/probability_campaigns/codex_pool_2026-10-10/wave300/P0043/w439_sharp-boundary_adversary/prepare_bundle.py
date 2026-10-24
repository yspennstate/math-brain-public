"""Prepare one local packet and the explicitly named w439 DRAFT inbox only.

No integrator, live store, global hook, digest ceremony, or service is touched.
"""
from pathlib import Path
import difflib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w439").resolve()
if ROOT != Path("~/brain_workers/w439").resolve():
    raise RuntimeError("Unexpected worker folder")
if INBOX.parent != Path("~/math-brain-inbox").resolve():
    raise RuntimeError("Unexpected inbox parent")

source = {"source_id": "owner-own-work:w439:p0043-critical-boundary-20261010", "url": "~/brain_workers/w439/INDEPENDENT.md", "revision": "2026-10-10-DRAFT-pending-w440", "license": "owner-own-work", "excerpt": None}


def entry(key, logical, title, statement, assumptions):
    return {"key": key, "namespace": "probability.percolation", "logical_name": logical, "kind": "concept", "title": "DRAFT: " + title, "statement": "Independent derivation pending w440 review. " + statement, "proof_text": None, "assumptions": assumptions, "domain": "probability, Bernoulli bond percolation", "source": dict(source)}


bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w439", "bundle_slug": "p0043-critical-boundary-draft-w439-001", "entries": [
    entry("unit-threshold", "critical-extinction-requires-nonunit-threshold", "Critical extinction needs the p_c<1 boundary", "On the infinite path Z with iid Bernoulli bond percolation, p_c=1 and theta(p_c)=1. For p<1, the probability of reaching distance n is at most 2p^n and tends to zero; at p=1 the whole path is open. Thus the assertion of critical extinction on all infinite connected locally finite quasi-transitive graphs needs an exclusion of p_c=1. This does not refute the intended P0043, which includes p_c<1.", ["nearest-neighbor infinite path Z", "iid Bernoulli bonds", "theta(p) is the probability the root has an infinite cluster"]),
    entry("subdivision", "uniformly-subdivided-three-regular-tree-critical-boundary", "Exact critical boundary on subdivided 3-regular trees", "Replace every edge of the infinite 3-regular tree with L edges, for a positive integer L, and root at an original vertex. The result T_L is quasi-transitive of maximum degree 3 and has p_c=2^(-1/L)<1. Full subdivided edges are independent coarse bonds of retention p^L, so critical clusters are almost surely finite. For 1<=n<=L the critical probability of reaching graph distance n is 1-(1-2^(-n/L))^3, hence 7/8 at n=L. At radii kL, with u_0=1 and u_(k+1)=u_k-u_k^2/4, the probability is 1-(1-u_(k-1)/2)^3. Reciprocal increments tend to 1/4, so (kL) times this probability tends to 6L. Critical susceptibility is infinite because every original-vertex shell has expected connected count 3/2.", ["L is a positive integer", "uniform L-subdivision of the infinite 3-regular tree", "iid Bernoulli bonds", "root is an original degree-3 vertex", "ambient graph distance", "fixed L for the asymptotic"]),
    entry("nonuniform", "quasi-transitive-critical-one-arm-has-no-degree-uniform-decay", "Degree alone gives no uniform critical one-arm decay", "For every fixed integer n>=1, the supremum of the critical probability of reaching graph distance n, over roots of infinite connected locally finite quasi-transitive graphs of maximum degree at most 3 with p_c<1, is 1. Indeed, for the uniformly L-subdivided 3-regular tree with L>=n, that probability is 1-(1-2^(-n/L))^3 and tends to 1 as L grows. No single f(n) tending to zero can bound the entire class. A degree-only C/n bound fails already at n=L since the probability is 7/8. This does not exclude graph-dependent bounds and does not address the smaller vertex-transitive class. The family has p_c tending to 1, growing orbit count, and volume-growth rate tending to 1.", ["iid Bernoulli bond percolation at each graph's own p_c", "infinite connected locally finite quasi-transitive graphs", "maximum degree at most 3", "p_c<1", "arbitrary root", "constants are required to be uniform over graphs"]),
    entry("susceptibility", "critical-extinction-does-not-imply-finite-susceptibility", "Critical extinction can coexist with infinite susceptibility", "On the infinite 3-regular tree, iid Bernoulli bond percolation has p_c=1/2 and almost surely no infinite cluster at p_c, but E_{p_c}|C(o)| is infinite. At distance k>=1 there are 3*2^(k-1) vertices, each connected with probability 2^(-k), giving expected connected shell size 3/2. Below p_c, chi(p)=1+3p/(1-2p), which diverges as p increases to p_c. Thus finiteness of susceptibility for every p<p_c cannot be transferred to p=p_c without a further uniform integrability or domination argument; it cannot be assumed as a bridge to critical extinction.", ["infinite 3-regular tree", "iid Bernoulli bonds", "critical p=1/2 for the endpoint claim", "0<=p<1/2 for the subcritical formula"])
], "relations": [
    {"from_key": "nonuniform", "to_key": "subdivision", "kind": "depends_on", "rationale": "The exact a_L(n) formula, with fixed n and increasing L, gives the supremum 1 and rules out graph-uniform decay."},
    {"from_key": "susceptibility", "to_key": "subdivision", "kind": "specializes", "rationale": "Set L=1 in the subdivided-tree critical boundary; its original shells show divergent susceptibility despite extinction."}
]}

required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"]) == 4
for e in bundle["entries"]:
    assert required <= set(e)
    assert e["kind"] == "concept" and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert "pending w440 review" in e["statement"]
for r in bundle["relations"]:
    assert r["from_key"] in keys and r["to_key"] in keys
    assert r["kind"] in {"depends_on", "specializes"}

body = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
(ROOT / "BRAIN_BUNDLE.json").write_text(body, encoding="utf-8")
INBOX.mkdir(parents=True, exist_ok=True)
candidate = INBOX / "bundle_001.json"
if candidate.exists() and candidate.read_text(encoding="utf-8") != body:
    for number in range(2, 1000):
        candidate = INBOX / ("bundle_" + str(number).zfill(3) + ".json")
        if not candidate.exists():
            break
    else:
        raise RuntimeError("No unused bundle name")
if not candidate.exists():
    part = candidate.with_suffix(".json.part")
    if part.exists():
        raise RuntimeError("Unexpected existing .part; preserve it")
    with part.open("x", encoding="utf-8", newline="\n") as out:
        out.write(body)
    part.rename(candidate)

hook = {"id": "percolation-boundary-w439-01", "area": "math", "event": "stage-start", "cue": "(?i)(critical percolation|p_c).{0,100}(uniform|susceptibility|exponential decay|limit)", "fire_when": "An argument transfers finite subcritical susceptibility to criticality, or asks for graph-uniform critical one-arm decay from degree alone.", "silent_when": "A fixed finite tree recurrence with disjoint branches is being checked, or a theorem already supplies graph-dependent constants and the needed limit control.", "text": "Check the endpoint and uniformity: critical extinction can have infinite susceptibility. Subdivided degree-3 trees have p_c<1 but critical reach to distance L is 7/8 for every L. State any uniform control before passing to a critical or graph limit.", "evidence": "~/brain_workers/w439/INDEPENDENT.md (claims 002-003); measurements.json: 30 PASS, 584 exact configurations; memory slug perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w439"}
assert len(hook["text"]) <= 300
hook_body = json.dumps(hook, ensure_ascii=False) + "\n"
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hook_body, encoding="utf-8")
patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
for filename, live, contents in (
    ("01_p0043_boundary_bundle.diff", candidate.as_posix(), body),
    ("02_percolation_boundary_hook.diff", "~/primary_directive/hooks1000/proposals/math-w439.jsonl", hook_body),
):
    patch = "".join(difflib.unified_diff([], contents.splitlines(keepends=True), fromfile="a/" + live, tofile="b/" + live))
    (patches / filename).write_text(patch, encoding="utf-8")

state = {"prepared": True, "submitted": True, "submitted_path": candidate.as_posix(), "submitted_at_utc": datetime.now(timezone.utc).isoformat(), "reviewed": False, "reviewer": "w440", "ingested": "not observed; integrator not run", "retrievable": "not checked", "entries": 4, "relations": 2, "kind": "concept DRAFT only", "hook_proposal": "local staging only; reviewer applies patch 02", "structural_validation": "4 complete concept entries, accepted owner-own-work tag, 2 allowed relations with exact local endpoints, one acyclic depends_on edge"}
(ROOT / "BRAIN_HANDOFF.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
print(json.dumps(state))
