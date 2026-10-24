"""Finalize independently reviewed math and a measured local patch; submit DRAFT only."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w357").resolve()
read = lambda name: json.loads((ROOT/name).read_text(encoding="utf-8"))
write = lambda name, data: (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
recall = read("RECALL_MEASUREMENTS.json")
laplace = read("LAPLACE_MEASUREMENTS.json")
assert recall["projection_modes_checked"] == 4 and recall["after_visible_hypotheses"] == 8
assert recall["default_compatibility_cases_passed"] == 4 and recall["abstention_preserved"]
assert laplace["weighted_ratios"][-1]["ratio"] > 0.99
reviews = [
    {"reviewer":"w359", "path":"~/brain_workers/w359/REVIEW_w357.md", "verdict":"KEEP L1-L6 at stated scope", "role":"independent referee"},
    {"reviewer":"w358", "path":"~/brain_workers/w358/PEER_AUDIT.md", "verdict":"KEEP L1-L6 at stated scope", "role":"independent adversary; statement-only challenge saved before paired proof"},
]
for review in reviews:
    document = Path(review["path"]).read_text(encoding="utf-8")
    assert "KEEP L1-L6" in document and "L6" in document
write("AUDIT_RECEIPTS.json", {"target":"P0017", "reviews":reviews,
      "scope":"The scoped L1-L6 deductions, not the parent KLS theorem or full October preprint proofs",
      "account_provenance":"Native peer IDs recorded; separate account identity not independently inspected",
      "formal_check_receipt":None})

draft = read("drafts/bundle_001.json")
allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
keys = {e["key"] for e in draft["entries"]}
assert len(keys) == len(draft["entries"]) <= 200
for entry in draft["entries"]:
    assert entry["kind"] in allowed_kinds and entry["statement"].strip()
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", entry["logical_name"])
    assert re.fullmatch(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+",entry["namespace"])
    if entry["kind"] in {"lemma", "theorem"}:
        assert entry["proof_text"] and entry["assumptions"]
        entry["source"]["revision"] = "author-proof-2026-10-10; independently checked by w359 and w358 at stated scope"
    else:
        assert entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
dependencies = {key:[] for key in keys}
for relation in draft["relations"]:
    assert relation["kind"] in allowed_relations and relation["from_key"] in keys
    assert bool("to_key" in relation) != bool("to_existing_logical" in relation)
    if "to_key" in relation:
        assert relation["to_key"] in keys
        if relation["kind"] == "depends_on":
            dependencies[relation["from_key"]].append(relation["to_key"])
    else:
        assert relation["to_existing_logical"] == "math:harvest.arxiv.mathematics:arxiv-2405-06616-theorem-3-13-68d962"
def visit(node, stack, finished):
    assert node not in stack, "cyclic depends_on"
    if node in finished:
        return
    for target in dependencies[node]:
        visit(target,stack|{node},finished)
    finished.add(node)
finished=set()
for key in keys:
    visit(key,set(),finished)
write("drafts/bundle_001.json",draft)
claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(row) for row in claims_path.read_text(encoding="utf-8").splitlines() if row.strip()]
for claim in claims:
    if claim.get("type") == "lemma":
        claim["status"] = "independently checked proof"
        claim["independent_reviewer"] = "w359 and w358"
        claim["independent_review_evidence"] = [review["path"] for review in reviews]
        claim["review_state"] = "KEEP on the exact scoped deduction; parent problem not solved by worker"
        claim["source"]["revision"] = "author-proof-2026-10-10; independently checked by w359 and w358 at stated scope"
    elif claim.get("type") == "edge":
        claim["review_state"] = "Supporting mathematical ends independently checked; exact edge integration review pending"
claims.append({"id":"w357-ENGINEERING-001", "target":"P0017", "type":"engineering measurement",
       "statement":"On four captured math cards, an exact-title Brascamp-Lieb query with --with-statements preserves the complete selected statement in all four CLI output modes. Two load-bearing hypotheses per mode are visible in 8/8 checks versus 0/8 before. Default outputs match in 4/4 cases; a high-support abstention is preserved.",
       "assumptions":["captured exact-ID cards only", "exact-title query", "semantic model explicitly disabled", "current source dependencies snapshotted in a private clone"],
       "source":"RECALL_MEASUREMENTS.json and test_recall_statements.py",
       "proof_or_counterexample":"Reproducible CLI comparison; engineering evidence, not mathematical proof.",
       "independent_reviewer":"claude-4a88bc43 (deployment review pending)",
       "remaining_gap":"Deployment and broader recall/proof-success effects remain unmeasured.", "status":"numerical evidence"})
claims_path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims),encoding="utf-8")
source=read("SOURCE_STATUS.json")
source["current_openness"]="UNKNOWN"
source["independent_review"]="w359 and w358 KEEP L1-L6 at stated scope; no full preprint-proof certification"
source["original_record"]["primary_url"]="https://arxiv.org/abs/2603.29571v1"
source["original_record"]["primary_title_verified"]=True
source["original_record"]["locator_check"]="Exact historical intake row; the complete target was separately verified in the October primary theorem statements"
source["canonical_checkout_check"]={"path":"~/math-research-brain", "checked":"README and targeted local SQLite path discovery",
    "result":"Only local audit databases were located; none opened because evaluation material is out of scope. No current solved/retired certification obtained from this checkout."}
write("SOURCE_STATUS.json",source)
write("BUNDLE_VALIDATION.json",{"spec":"mathbrain-draft-v1", "passed":True,
    "checks":["complete required entry fields", "proofs for lemma entries", "owner-own-work license tag", "allowed relation types", "exact internal endpoints", "acyclic depends_on", "one captured existing covariance endpoint"],
    "mathematical_evidence":"AUDIT_RECEIPTS.json", "formal_proof_claim":False,
    "integration_executed":False})
# Retain the measured recall evidence without unrelated snippets or source reads.
(ROOT / "recall_mistakes.txt").write_text(
    "Query: P0017 log-concave KLS bridge proof mistakes\n"
    "Provider: brain.py recall; completed with exit code 0.\n"
    "Top three: rank 1 unrelated result omitted (its source was not opened); rank 2 Lyons 2.6 determinant memory; rank 3 open_problem_repo_survey_famous_tracks_all_open_af449ii_now_refuted_with_two_audits_2026_09_18.\n"
    "Top-three exact P0017 identifier hits: 0. Top-three Gaussian bridge hypothesis hits: 0.\n"
    "Exact provider warning: [absent] no memory contains: p0017.\n"
    "Target-index alias routing remains a bounded proposal; the delivered patch separately exposes full selected-card statements.\n",encoding="utf-8")

payload=json.dumps(draft,ensure_ascii=False,indent=2)+"\n"
INBOX.mkdir(parents=True,exist_ok=True)
destination=(INBOX/"bundle_001.json").resolve()
part=(INBOX/"bundle_001.part").resolve()
assert destination.is_relative_to(INBOX) and part.is_relative_to(INBOX)
if destination.exists():
    assert destination.read_text(encoding="utf-8")==payload,"existing draft differs; do not overwrite peer/coordinator state"
else:
    part.write_text(payload,encoding="utf-8")
    part.rename(destination)
write("BUNDLE_LIFECYCLE.json",{"bundle":str(destination), "submitted":True, "reviewed":True,
    "review_scope":"w359 and w358 independently KEEP L1-L6; exact bundle-edge integration remains the validating coordinator's step",
    "ingested":"NOT_ASSERTED: no integrator invoked by worker and no receipt checked",
    "retrievable":"NOT_TESTED: no live-store recall gain claimed", "parent_problem_solved_by_worker":False})
packet={"worker":"w357", "target":"P0017", "date":"2026-10-10", "ready_for_review":True,
    "exact_target":"SOURCE_STATUS.json", "prior_attempt_digest":"PRIOR_ATTEMPTS.md",
    "proof":"ATTEMPT.md", "claims_and_quoted_edges":"CLAIMS.jsonl", "independent_audits":reviews,
    "math_measurements":"LAPLACE_MEASUREMENTS.json", "engineering_patch":"patches/01_recall_full_statements.diff",
    "engineering_tests":"test_recall_statements.py", "engineering_measurements":"RECALL_MEASUREMENTS.json",
    "patch_baseline":"PATCH_RECEIPT.json", "dependency_snapshot":"DEPENDENCY_SNAPSHOT.json",
    "draft_bundle":str(destination), "draft_validation":"BUNDLE_VALIDATION.json", "hook_staged":"proposals/math-w357.jsonl",
    "formal_check_receipt":None, "full_KLS_proof_claim":False,
    "single_hardest_gap":"Uniform strict Q_t bound for all nonlinear finite-energy tests at one fixed numerical noise variance; affine/Gaussian bounds and MMSE alone do not provide it.",
    "NEXT":"Derive a bound on E||Cov(f,X|Y)||^2/t^2 directly, retaining the shared Y dependence; use w358's exponential examples as controls. Coordinator can review/apply the measured CLI diff and integrate the scoped draft."}
write("REVIEW_PACKET.json",packet)
report='''P0017 now has recent full-proof claims in [Bizeul-Klartag-Lehec](https://arxiv.org/html/2610.05474v1) and [Song-Zhang](https://arxiv.org/html/2610.01447v2). I recovered the exact normalized target and the earlier Gaussian-only attempt. Current openness is UNKNOWN here; no novelty or full-KLS-proof claim is made.

I derived a conditional equivalence: a uniform posterior Dirichlet contraction q<1 at fixed noise variance t would give C_P<=t(1+q)/(1-q). The missing estimate concerns all nonlinear tests. A fixed variance-one Laplace law refutes the tempting energy-weighted MMSE route. w358 and w359 independently KEEP L1-L6 at their stated scopes; see AUDIT_RECEIPTS.json and ATTEMPT.md.

Measurement: `python -X utf8 measure_laplace.py` used 34,526 posterior evaluations in 0.070 s. Unweighted posterior covariance averaged 0.4791602; the tail-energy-weighted ratio reached 0.999998204 at L=8. The analytic limit proof, separately audited, is the mathematical evidence.

The scoped CLI patch adds `recall --with-statements`, returning full selected-card bodies and stored review provenance. `python -X utf8 test_recall_statements.py` passed all four output modes: 0/8 to 8/8 hypothesis-visibility checks, 4/4 default-output compatibility checks, preserved abstention and identifier-only background output. It uses four captured math cards with semantic models off. The opted-in field adds 598 UTF-8 bytes for this card. This measures statement visibility; wider recall accuracy and proof success remain unmeasured. A short-name query miss remains recorded. The clone required five current source dependencies because its committed version lacked the live background module.

Reviewer apply command: `git -C ~/math-brain-build apply -p5 ~/brain_workers/w357/patches/01_recall_full_statements.diff` (run the same command with `--check` first); recheck with `python -X utf8 ~/brain_workers/w357/test_recall_statements.py --code-root ~/math-brain-build/src`.

The reviewed math DRAFT is submitted at ~/math-brain-inbox/w357/bundle_001.json. Ingestion and retrievability are separately unasserted; the coordinator integrates. One evidence-backed hook is staged locally in proposals/math-w357.jsonl. All live code and stores were left untouched by this worker.

NEXT: Bound the actual nonlinear posterior cross-covariance energy while retaining its Y dependence; coordinator reviews/applies the CLI diff and integrates the scoped draft.
'''
(ROOT/"REPORT.md").write_text(report,encoding="utf-8")
print("Final review packet validated; reviewed DRAFT submitted. No live-store ingestion or live-code patch applied.")
