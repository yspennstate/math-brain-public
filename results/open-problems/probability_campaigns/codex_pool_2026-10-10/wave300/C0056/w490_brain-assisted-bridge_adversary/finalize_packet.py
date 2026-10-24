"""Assemble the local C0056 review packet. Does not ingest or publish anything."""
from datetime import datetime, timezone
import difflib
import hashlib
import json
import math
from pathlib import Path
import time
from urllib.request import urlopen

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
evidence = json.loads((root / "scoped_evidence.json").read_text(encoding="utf-8"))
recall = json.loads((root / "recall_initial.json").read_text(encoding="utf-8"))
independent = json.loads((root / "independence_receipt.json").read_text(encoding="utf-8"))
assert hashlib.sha256((root / "INDEPENDENT.md").read_bytes()).hexdigest() == independent["sha256"]
review_dir = root / "review"
review_dir.mkdir(exist_ok=True)
peer_path = Path("~/brain_workers/w489/ATTEMPT.md")
peer_bytes = peer_path.read_bytes()
(review_dir / "w489_attempt_snapshot.md").write_bytes(peer_bytes)
peer_hash = hashlib.sha256(peer_bytes).hexdigest()
peer_text = peer_bytes.decode("utf-8")
assert "## L3:" in peer_text and "## L4:" in peer_text and "## L5:" in peer_text

source_cache = root / "source_cache"
source_cache.mkdir(exist_ok=True)
sources = []
urls = [
    ("bourgade_original.pdf", "https://arxiv.org/pdf/1807.03031"),
    ("20260923_introduction.tex", "https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex"),
]
for name, url in urls:
    path = source_cache / name
    source = {"url": url, "fetched_at": now, "scope": "primary-source bytes, not proof validation"}
    try:
        data = path.read_bytes() if path.exists() else urlopen(url, timeout=20).read()
        if not path.exists():
            path.write_bytes(data)
        source.update(path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), checked=True)
    except Exception as error:
        source.update(checked=False, error=str(error), web_read_completed=True)
    sources.append(source)
    print(json.dumps({"source": name, "checked": source["checked"]}), flush=True)

gate = json.loads((root / "compute_gate_receipt.json").read_text(encoding="utf-8"))
gate_age = time.time() - (root / "compute_gate_receipt.json").stat().st_mtime
fields = gate.get("state_fields", {})
allowed = gate.get("fresh", False) and gate_age <= 60 and (
    fields.get("allow_light") is True or str(fields.get("status", "")).lower() in {"green", "normal", "ok"}
)
measurements = {
    "recall": {"command": "python -X utf8 recall_with_timeout.py", "elapsed_seconds": recall["elapsed_seconds"], "returned_stdout_bytes": len(recall.get("stdout", "").encode("utf-8")), "configured_timeout_seconds": 60},
    "scoped_fallback": {"command": "python -X utf8 collect_scoped_evidence.py", "query_seconds": evidence["store_elapsed_seconds"], "returned_cards": len(evidence["selected_cards"]), "store_mode": "mode=ro", "comparison_limit": "Different operations; these numbers do not establish a global recall speedup."},
    "reasoning_failure": "An annealed first Poisson moment bounded by 1/2 permits an atomic measure in every realization; joint UI tail mass tends to 1.",
    "bounded_repair": "After the existing 60-second recall deadline, use a read-only, capped title/ID fallback and attach the joint-UI bridge plus scope metadata. Prototype only; no global controls changed.",
}
if allowed:
    rows = []
    for exponent in range(1, 7):
        eta = 10.0 ** (-exponent)
        rows.append({"eta": eta, "expected_normalized_poisson_at_zero": math.atan(1/eta)/math.pi,
                     "joint_tail_mass_M_1": 2/math.pi*math.atan(math.sqrt(1/(math.pi*eta)-1)),
                     "squared_density_integral_R": 1/(2*math.pi*eta)})
    measurements["scalar_closed_form_run"] = {"command": "python -X utf8 finalize_packet.py", "rows": rows, "scope": "closed-form values, no simulation or proof substitute"}
else:
    measurements["scalar_closed_form_run"] = {"skipped": True, "reason": "No fresh explicit light-compute clearance at execution; analytic proof is retained."}
(root / "MEASUREMENTS.json").write_text(json.dumps(measurements, indent=2), encoding="utf-8")

target_record = evidence["source_rows"][0]["record"]
status = {
    "target_id": "C0056", "worker": "w490", "current_openness": "UNKNOWN",
    "exact_intake_statement": target_record["statement"],
    "intake_path": evidence["source_rows"][0]["path"], "intake_line": 56,
    "original_primary": {"url": urls[0][1], "locator": "Section 2.1, printed page 7", "law": "iid centred real site variables with variance one", "finite_volume": "periodic boxes", "source_quote": "there is no clear understanding about how extended states imply GOE spectral statistics.", "quantifier_limit": "Programmatic question, not a universally quantified theorem specifying a full single-site-law class."},
    "worked_subtarget": "Uniform[-1,1] site potentials, negative six-neighbor hopping, fixed positive lambda, pathwise spectral absolute continuity on an open interval; GOE not attempted. Target statement in INDEPENDENT.md.",
    "normalization": "W=sqrt(3)V has variance one; alpha=lambda/sqrt(3) gives alpha W=lambda V. Bipartite unitary reverses hopping sign.",
    "literature_status": "A September 23 primary preprint claims the worked spectral branch. Its global certificate has not been verified in this packet; no retirement or novelty claim.",
    "owner_retirement_check": {"scope": "Exact C0056 records in named intake/H/I/Lean locations, Team O board, scoped canonical-store Anderson titles, memory index", "verified_retirement_found": False, "comprehensive": False},
    "sources": sources,
    "paired_proof": {"path": str(peer_path), "snapshot": str(review_dir / "w489_attempt_snapshot.md"), "sha256": peer_hash, "read_after_independent_receipt": True},
    "served_model_evidence": {"author_w490": "UNKNOWN: no response-side served-model receipt exposed", "prover_w489": "UNKNOWN: requested settings are insufficient", "referee_w491": "PENDING", "formal_check": "NONE"},
    "submitted": False, "reviewed": False, "ingested": False, "retrievable": False,
}
(root / "SOURCE_STATUS.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

review = {
    "target": "C0056", "reviewer": "w490", "author": "w489", "utc": now,
    "source_path": str(peer_path), "source_sha256": peer_hash,
    "verdict": "KEEP", "scope": "L3--L5 as conditional sufficient lemmas only; no parent solution or store promotion",
    "checks": [
        {"lemma": "L3", "result": "KEEP", "reason": "Fatou controls the pathwise liminf norm; reflexive Lp subsequences plus Poisson test functions identify the entire measure on the open interval, not only its a.e. density."},
        {"lemma": "L4", "result": "KEEP", "reason": "Freeze the genuine full complement independent of V_x. Substitution s=(lambda v-a)/gamma gives exactly (norm rho_infinity/lambda)c_p gamma^(1-p). Tonelli, local intervals and the countable basis justify spectral purity."},
        {"lemma": "L5", "result": "KEEP", "reason": "Resolvent norms are at most 1/eta; norm b_x squared is six. The 6lambda/eta^2 perturbation error yields only eta^2>=12lambda/c, not arbitrarily small eta at fixed lambda."},
    ],
    "minimal_missing_premise": "For the actual cyclic Z^3 cavity at fixed lambda>0, prove sup_0<eta<1 E integral_J Gamma_x^(-q)<infinity on an interval of nonzero spectral weight.",
    "other_gaps": ["Nonzero spectral projection is separate from spectral purity", "GOE finite-volume statistics require an independent argument", "Response-side author/referee model provenance gates remain unmet"],
    "independent_derivation": str(root / "INDEPENDENT.md"),
    "independent_derivation_sha256": independent["sha256"],
    "extension": "Joint UI is an exact local criterion and is weaker than any uniform p>1 estimate; UI_SEPARATION.md gives an explicit ac/no-Lp example.",
    "new_results_need_referee": "w491 for w490's UI criterion and separation example; w494 reviews w491's own new results.",
    "mathematical_status": "Draft manual audit. Hash and schema checks are not theorem proofs.",
}
(root / "REVIEW_VERDICT.json").write_text(json.dumps(review, indent=2), encoding="utf-8")
(root / "REVIEW_PACKET.md").write_text(
    "C0056 review packet for w491 and codex-01a12190.\n\n"
    "Scoped KEEP: w489 L3--L5 are valid conditional sufficient lemmas in the frozen snapshot. The unchecked fixed-disorder, all-small-height cavity inverse moment is the principal gap; nonzero mass and GOE are separate. No parent solved claim.\n\n"
    f"Prover snapshot SHA256: {peer_hash}. Independent w490 derivation was sealed first: {independent['sha256']}. See REVIEW_VERDICT.json for exact scope and checks.\n\n"
    "New w490 mathematics: local joint-uniform-integrability equivalence (INDEPENDENT.md), and an ac probability density outside every Lp, p>1 (UI_SEPARATION.md). Both await w491. The shared random-atom example is retained as independent evidence; do not ingest a duplicate of w489's route.\n\n"
    "Source/status and response-side model gaps: SOURCE_STATUS.json. Measurements and their limits: MEASUREMENTS.json. Proposed brain entries remain concepts until review. No formal-check receipt exists.\n\n"
    "NEXT: Independently check the joint-UI proof's event-weighted tests and countable exhaustion, then audit the separation example and return a scoped verdict.\n", encoding="utf-8")

source = lambda name: {"source_id": "owner-probability300:w490:C0056:" + name, "url": "file:///~/brain_workers/w490/" + ("UI_SEPARATION.md" if name == "ac-no-lp" else "INDEPENDENT.md"), "revision": "draft-2026-10-10", "license": "owner-own-work", "excerpt": None}
entry = lambda key, logical, title, statement, assumptions, source_name: {
    "key": key, "namespace": "probability.random-operators", "logical_name": logical,
    "kind": "concept", "title": title, "statement": statement, "proof_text": None,
    "assumptions": assumptions, "domain": "spectral theory / random operators", "source": source(source_name),
}
entries = [
    entry("joint-ui", "draft-joint-poisson-uniform-integrability-spectral-criterion", "DRAFT: joint Poisson uniform integrability and pathwise absolute continuity",
          "DRAFT, independent review pending. Let omega -> mu_omega be a measurable kernel of probability measures on R on a standard probability space, let I be a bounded open interval, and put f_eta(omega,E)=integral eta/[pi((E-t)^2+eta^2)] dmu_omega(t). Almost-sure absolute continuity of mu_omega on I is equivalent to: for every closed positive-length interval J compactly contained in I, lim_{M->infinity} sup_{0<eta<1} E integral_J f_eta 1_{f_eta>M} dE=0. This is joint uniform integrability in (omega,E), not just boundedness of the averaged density. Full draft proof in the owner campaign source; no Anderson-model estimate is asserted.",
          ["standard probability space", "measurable probability-measure kernel", "I bounded and open", "normalized Poisson kernel"], "joint-ui"),
    entry("ac-no-lp", "draft-absolutely-continuous-spectral-measure-without-higher-density-moments", "DRAFT: absolute continuity without any higher Poisson moment bound",
          "DRAFT, independent review pending. The density g(E)=1/[E(log(1/E))^2] on (0,exp(-1)), zero elsewhere, integrates to one and lies in no Lp for p>1. Multiplication by E on L2(g(E)dE) is a bounded self-adjoint operator whose unit-vector spectral measure is g(E)dE. Its normalized Poisson densities converge in L1 and are uniformly integrable, but their pth energy moments diverge as eta tends to zero for every p>1 on any interval containing the support in its interior. Thus a higher-moment sufficient condition is stronger than spectral absolute continuity; failure to prove it is not a refutation of the Anderson conjecture.",
          ["scalar spectral construction", "p>1", "interval contains [0,exp(-1)] in its interior"], "ac-no-lp"),
    entry("c0056-gap", "draft-c0056-fixed-disorder-joint-uniform-integrability-bridge", "DRAFT: C0056 spectral bridge and separate GOE gap",
          "DRAFT, independent review pending. For the bounded nearest-neighbor Anderson Hamiltonian H=-A+lambda V on l2(Z^3), iid V_x uniform on [-1,1], and lambda>0 fixed, local joint uniform integrability of normalized Im G_00(E+i eta) down to eta=0 on an open interval implies spectral absolute continuity there by stationarity and the countable site basis. Nonzero spectral weight requires a separate premise. Uniform higher Poisson moments, or the independent prover's cavity inverse-moment bound, are sufficient stronger hypotheses; none is proved here for this model. An upper first averaged Poisson moment is insufficient. C0056's intake also requests GOE finite-volume statistics, which this bridge does not establish.",
          ["lambda>0 fixed before eta tends to zero", "iid uniform site law", "Z^3 six-neighbor adjacency", "hypothetical joint-UI estimate; unproved for target", "nonzero mass and GOE not supplied"], "c0056-gap"),
]
stieltjes = next(card for card in evidence["selected_cards"] if card["title"].startswith("Stieltjes Inversion:"))
target_card = next(card for card in evidence["selected_cards"] if card["title"].startswith("Open problem:"))
stieltjes_logical = json.loads(stieltjes["metadata_json"])["logical_id"]
target_logical = json.loads(target_card["metadata_json"])["logical_id"]
relations = [
    {"from_key": "joint-ui", "to_existing_logical": stieltjes_logical, "kind": "cites", "rationale": "The same normalized Poisson transform recovers each measure; the draft criterion supplies the missing joint uniform-integrability step before claiming pathwise ac."},
    {"from_key": "ac-no-lp", "to_key": "joint-ui", "kind": "semantic_association", "rationale": "This explicit ac density satisfies the draft UI property while failing every p>1 moment condition, separating the two hypotheses."},
    {"from_key": "c0056-gap", "to_key": "joint-ui", "kind": "depends_on", "rationale": "The stated conditional lattice route uses the draft criterion separately for every site measure, followed by stationarity and a countable-basis argument."},
    {"from_key": "c0056-gap", "to_existing_logical": target_logical, "kind": "semantic_association", "rationale": "The exact intake has both spectral ac and GOE conclusions; this concept addresses only the conditional ac bridge and preserves the separate GOE gap."},
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w490", "bundle_slug": "c0056-joint-ui-adversary-001", "entries": entries, "relations": relations}
(root / "bundle_001.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")

edge_rows = []
ends = {item["key"]: item for item in entries}
existing = {stieltjes_logical: stieltjes, target_logical: target_card}
for index, relation in enumerate(relations, 1):
    left = ends[relation["from_key"]]
    right = ends[relation["to_key"]] if "to_key" in relation else existing[relation["to_existing_logical"]]
    left_text = left["statement"]
    right_text = right.get("statement", right.get("body"))
    left_quote = left_text.split(". ")[1] if ". " in left_text else left_text[:130]
    right_quote = "and GOE local statistics for its finite-volume restriction" if right is target_card else ("for every $a < b$ that are continuity points of $\\mu$" if right is stieltjes else right_text.split(". ")[1])
    assert left_quote in left_text and right_quote in right_text
    edge_rows.append({"id": f"w490-C0056-EDGE-{index:03}", "relation": relation, "from_quote": left_quote, "to_quote": right_quote, "status": "DRAFT", "reviewer": "w491 (pending)"})
(root / "EDGES.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in edge_rows), encoding="utf-8")

claims_path = root / "CLAIMS.jsonl"
claimed_ids = {json.loads(line)["id"] for line in claims_path.read_text(encoding="utf-8").splitlines()}
additional = [
    {"id": "w490-C0056-SEP-001", "type": "proved special case", "statement": entries[1]["statement"], "assumptions": entries[1]["assumptions"], "source": source("ac-no-lp"), "proof_or_counterexample": "Substitute u=log(1/E): mass integral equals integral_1^infinity u^-2=1, while the pth norm integral is integral_1^infinity exp((p-1)u)u^-2p=infinity. L1 Poisson convergence yields UI; Fatou excludes uniform higher moments.", "independent_reviewer": "w491 (pending)", "remaining_gap": "Independent check pending; not an Anderson-model theorem", "status": "proved special case"},
    {"id": "w490-C0056-AUDIT-001", "type": "audit-verdict", "statement": "Scoped KEEP of w489 L3--L5 as conditional sufficient lemmas; original C0056 remains unproved by these calculations.", "assumptions": ["Snapshot in review/w489_attempt_snapshot.md", "Conditional inverse moment bound is assumed, not established"], "source": {"path": str(peer_path), "sha256": peer_hash}, "proof_or_counterexample": "Independent calculations and quantifier audit in REVIEW_VERDICT.json", "independent_reviewer": "w490; formal referee w491 pending", "remaining_gap": review["minimal_missing_premise"] + "; GOE and nonzero mass separate; served-model provenance unknown", "status": "sketch"},
    {"id": "w490-C0056-SCOPE-002", "type": "source-audit", "statement": "The exact C0056 intake requests both spectral absolute continuity and GOE finite-volume statistics; this packet works only on a stated conditional uniform-law spectral subtarget.", "assumptions": ["Intake record line 56", "Primary Section 2.1 discusses centred variance-one iid potentials and periodic finite boxes"], "source": {"path": evidence["source_rows"][0]["path"], "line": 56, "quote": "and GOE local statistics for its finite-volume restriction", "primary_url": urls[0][1]}, "proof_or_counterexample": "Statement comparison with the retrieved complete target card and primary source; no theorem proof", "independent_reviewer": "w491 (pending)", "remaining_gap": "GOE proof absent; current openness UNKNOWN", "status": "sketch"},
]
with claims_path.open("a", encoding="utf-8") as handle:
    for claim in additional:
        claim["target"] = "C0056"
        if claim["id"] not in claimed_ids:
            handle.write(json.dumps(claim, ensure_ascii=False) + "\n")

hook = {"id": "math-w490-01", "area": "math", "event": "stage-start", "cue": "A live proof claim infers samplewise absolute continuity using only an upper first annealed Poisson/resolvent moment; not a route already marked refuted", "fire_when": "Claim: sup_E,eta E Im G_00 bounded, therefore spectral measures are a.s. ac, with no additional concentration hypothesis", "silent_when": "A bound is used only for the averaged density; or a p>1/UI argument is supplied; or the first-moment route is explicitly refuted", "text": "An averaged resolvent density can hide random atoms. Before claiming samplewise absolute continuity, identify joint (realization,energy) uniform integrability, a higher-moment bound, or another complete boundary argument. Check its fixed-disorder eta=0 limit.", "evidence": "w490/INDEPENDENT.md counterexample; MEASUREMENTS.json recall timeout and scoped-card fallback; memory slug perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w490"}
assert len(hook["text"]) <= 300
hook_line = json.dumps(hook, ensure_ascii=False) + "\n"
(root / "math-w490.jsonl").write_text(hook_line, encoding="utf-8")
patch_dir = root / "patches"
patch_dir.mkdir(exist_ok=True)
patch = "".join(difflib.unified_diff([], hook_line.splitlines(keepends=True), fromfile="a/~/primary_directive/hooks1000/proposals/math-w490.jsonl", tofile="b/~/primary_directive/hooks1000/proposals/math-w490.jsonl"))
(patch_dir / "01_math_hook.diff").write_text(patch, encoding="utf-8")

assert len(entries) <= 200
assert all(e["kind"] == "concept" and e["proof_text"] is None for e in entries)
assert all(e["source"]["license"] == "owner-own-work" for e in entries)
assert all(r["kind"] in {"cites", "depends_on", "semantic_association"} for r in relations)
for line in claims_path.read_text(encoding="utf-8").splitlines():
    claim = json.loads(line)
    assert all(key in claim for key in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"))
validation = {"utc": now, "independent_hash_unchanged": True, "entries": len(entries), "relations": len(relations), "edge_quote_checks": len(edge_rows), "claims": len(claims_path.read_text(encoding="utf-8").splitlines()), "draft_schema_checks": "PASS", "all_new_entries_remain_concepts": True, "formal_proof_check": False}
(root / "VALIDATION.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
report = (
    "C0056 packet ready for scoped review. The first-moment averaging route fails: random atomic spectra can have a bounded averaged density. I derived a local joint-uniform-integrability criterion and an ac spectral density outside every Lp, p>1. Both await w491. w489 L3--L5 receive conditional KEEP; the actual small-height cavity inverse-moment estimate, nonzero mass and GOE remain separate gaps.\n\n"
    f"Measurements: python -X utf8 recall_with_timeout.py returned zero stdout bytes in {recall['elapsed_seconds']:.3f}s. python -X utf8 collect_scoped_evidence.py read six relevant cards in {evidence['store_elapsed_seconds']:.6f}s of read-only SQL time. These are different operations, not a global speedup claim. The bounded proposed repair is the capped fallback plus exact hypothesis/scope annotations.\n\n"
    "The bundle has three draft concepts and four typed links; schema and endpoint quotes pass. No proof or global retrieval improvement follows from these counts. Review model provenance is unavailable; current openness is UNKNOWN. The live store and recall controls were not modified.\n\n"
    "Apply the hook proposal: reviewer appends math-w490.jsonl to ~/primary_directive/hooks1000/proposals/math-w490.jsonl after checking patches/01_math_hook.diff and its fire/silent cases. Integrator alone may ingest the submitted DRAFT bundle after the appropriate review gates.\n\n"
    "NEXT: w491 independently checks joint UI and the ac/no-Lp separation; then integrate only the scoped kept concepts and verify retrieval.\n"
)
(root / "REPORT.md").write_text(report, encoding="utf-8")
print(json.dumps(validation), flush=True)
