"""Finish the review packet without deploying to a store or global hook file."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import json

ROOT = Path(__file__).resolve().parent
measure = json.loads((ROOT / "measurements.json").read_text(encoding="utf-8"))
handoff = json.loads((ROOT / "BRAIN_HANDOFF.json").read_text(encoding="utf-8"))
assert measure["passed"] == 30 and measure["failed"] == 0
assert Path(handoff["submitted_path"]).read_text(encoding="utf-8") == (ROOT / "BRAIN_BUNDLE.json").read_text(encoding="utf-8")

status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
status.update({
    "source_status": "Exact statement verified in Hutchcroft arXiv:1605.05301; original P0043 intake locator recovered, book version not independently retrieved.",
    "original_intake": {"file": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006p01.json", "key": "op-p0043", "logical_id": "math:probability.core:open-problem-p0043-absence-of-infinite-clusters-at-critical-percolation", "source_locator_as_recorded": "Lyons and Peres, Probability on Trees and Networks, paperback electronic version 19 August 2026, Conjecture 8.15, printed p.285", "locator_verification": "intake recovered; primary book fetch failed because 21 MB exceeded browser fetch limit"},
    "local_retirement_check": "No certified retirement found in the targeted H/I/Lean exact-ID checks. Exported P0043 and C0084 cards are explicitly unverified attempt/open-problem material. A peer reports a recent October collection making a full claim; its primary proof was not supplied or verified here, so current openness stays UNKNOWN.",
    "related_intake": {"file": "~/<private-repo>/06_math_research/probability_1000_intake_H_20260914/problems.jsonl", "line": 16, "id": "H0016", "claimed_source": "arXiv:2608.23661, Cerf", "verification": "secondary lookup record explicitly unverified; not relied on as primary evidence"},
    "target_store_rows": "PRIOR_TARGET_ROWS.json, exact P0043/C0084 export rows only",
    "source_correction": {"existing_logical_id": "math:probability.percolation:attempt-c0084-no-infinite-cluster-at-criticality-on-quasi-transitive-graphs-with-p-c", "existing_claim_id": "claim_074b08d2f079277d5ce5423b113d46801b9ed62cd7be7598eb47b46fb59b1aeb", "scope": "Repair the account of Hutchcroft's method: susceptibility finite only below p_c, then supermultiplicativity and left continuity of the infimum connectivity rate; no assertion of finite critical susceptibility or a branching-random-walk proof."},
    "paired_proof_read": True,
    "paired_proof_order": "INDEPENDENT.md and claims 001-003 saved before w438 ATTEMPT.md was read",
    "paired_proof_audit": "AUDIT_W438.md",
    "recall": {"result": "60-second timeout", "file": "recall.txt", "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12"},
    "current_openness": "UNKNOWN",
    "novelty_claim": False
})
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

correction_statement = "DRAFT source correction, pending independent review. In Hutchcroft's arXiv:1605.05301, the exponential-growth connectivity bound uses finite susceptibility only for p<p_c (Theorem 6). Supermultiplicativity of kappa_p(n)=inf{P_p(x connects to y):d(x,y)<=n}, followed by left continuity of sup_n kappa_p(n)^(1/n), transfers the rate bound to p_c. The proof does not require finite susceptibility at p_c or a branching-random-walk comparison. On the 3-regular tree the critical susceptibility is infinite, so an ordinary finite-critical-susceptibility interpretation of the old C0084 attempt is false. Its undefined qualifier 'spherically averaged' is not treated as a separate established theorem."
correction = {"spec": "mathbrain-draft-v1", "author_agent": "w439", "bundle_slug": "p0043-c0084-source-correction-draft-w439-002", "entries": [{"key": "source-correction", "namespace": "probability.percolation", "logical_name": "exponential-growth-critical-connectivity-proof-uses-subcritical-susceptibility", "kind": "concept", "title": "DRAFT: Correct the susceptibility endpoint in the C0084 attempt", "statement": correction_statement, "proof_text": None, "assumptions": ["iid Bernoulli bond percolation", "connected locally finite quasi-transitive graphs of exponential growth for Hutchcroft's rate bound", "the old C0084 attempt is unverified concept material", "this corrects a source description, not the full P0043 problem"], "domain": "probability theory, percolation, source auditing", "source": {"source_id": "owner-own-work:w439:p0043-c0084-source-audit-20261010", "url": "https://arxiv.org/html/1605.05301", "revision": "primary-v1-2016-05-17-audited-2026-10-10", "license": "owner-own-work (campaign source audit; mathematical facts paraphrased from attributed primary source)", "excerpt": "expected cluster size is finite for every p<p_c"}}], "relations": [{"from_key": "source-correction", "to_existing_logical": status["source_correction"]["existing_logical_id"], "kind": "cites", "rationale": "This source-audit concept identifies a specific endpoint and method-description error in the existing unverified C0084 attempt, without rejecting every sentence or the original conjecture."}]}
assert correction["entries"][0]["kind"] == "concept"
assert correction["entries"][0]["proof_text"] is None
assert correction["relations"][0]["kind"] == "cites"
body = json.dumps(correction, indent=2, ensure_ascii=False) + "\n"
(ROOT / "BRAIN_BUNDLE_CORRECTION.json").write_text(body, encoding="utf-8")
inbox = Path(handoff["submitted_path"]).parent.resolve()
assert inbox == Path("~/math-brain-inbox/w439").resolve()
for number in range(2, 1000):
    target = inbox / ("bundle_" + str(number).zfill(3) + ".json")
    if target.exists() and target.read_text(encoding="utf-8") == body:
        break
    if not target.exists():
        part = target.with_suffix(".json.part")
        if part.exists():
            raise RuntimeError("Preserve existing partial draft")
        with part.open("x", encoding="utf-8", newline="\n") as out:
            out.write(body)
        part.rename(target)
        break
else:
    raise RuntimeError("No free correction bundle name")
patch = "".join(difflib.unified_diff([], body.splitlines(keepends=True), fromfile="a/" + target.as_posix(), tofile="b/" + target.as_posix()))
(ROOT / "patches" / "03_c0084_source_correction.diff").write_text(patch, encoding="utf-8")

claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
extra = [
    {"claim_id": "w439-P0043-source-004", "kind": "source_correction", "statement": correction_statement, "assumptions": correction["entries"][0]["assumptions"], "source": {"primary": "https://arxiv.org/html/1605.05301", "locator": "Theorem 6, Lemmas 4-5, proof of Theorem 2", "source_quote": "expected cluster size is finite for every p<p_c", "old_row": status["source_correction"]["existing_claim_id"], "old_quote": "His proof uses the growth to show that the susceptibility is finite at p_c in a spherically-averaged sense via a comparison with a branching random walk with killing at rate given by the growth"}, "proof": "Primary proof uses chi(p)<infinity only below p_c; the exact critical 3-regular tree shell expectation is 3/2 for every radius, so chi(p_c)=infinity. The undefined spherical qualifier is not independently interpreted or certified.", "independent_reviewer": "w440", "remaining_gap": "Independent review pending; no live card revision applied.", "status": "sketch", "review_status": "pending"},
    {"claim_id": "w439-audit-w438-A", "kind": "independent_proof_audit", "statement": "For a deterministic finite offspring sequence a_i in {1,2}, parameter 0<p<=1 and terminal depth n, let q_n=1, q_i=1-(1-p q_(i+1))^a_i and m_i=p^i product_(j<i)a_j. Then 1/q_0=1/m_n+sum_(i<n:a_i=2) 1/[4 m_i (1-p q_(i+1)/2)].", "assumptions": ["deterministic spherically symmetric rooted tree", "iid independent edge bonds", "disjoint descendant edge sets", "0<p<=1", "finite n>=0"], "source": {"author": "w438", "file": "~/brain_workers/w438/ATTEMPT.md", "locator": "Lemma A"}, "proof": "The reciprocal difference at a branching index is 1/[4(1-p q_(i+1)/2)], and is zero at a_i=1. Unrolling scales the correction by 1/m_i. AUDIT_W438.md checks indices, endpoints, positivity and independence; 24 exact rational cases agree.", "independent_reviewer": "w439", "remaining_gap": "No gap found in this finite tree identity. A general-graph comparison is not established; w440's designated triad review is separate.", "status": "independently checked proof", "review_status": "w439 KEEP, w440 separate"}
]
seen = {c["claim_id"] for c in claims}
for c in extra:
    if c["claim_id"] not in seen:
        claims.append(c)
for c in claims:
    if c["claim_id"].startswith("w439-P0043-"):
        c["brain_states"] = {"prepared": True, "submitted": True, "reviewed": False, "ingested": "not observed", "retrievable": "not checked"}
claims_path.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in claims), encoding="utf-8")

handoff.update({"correction_submitted_path": target.as_posix(), "total_entries": 5, "total_relations": 3, "reviewed": False, "ingested": "not observed; integrator not run", "retrievable": "not checked", "last_packet_update_utc": datetime.now(timezone.utc).isoformat()})
(ROOT / "BRAIN_HANDOFF.json").write_text(json.dumps(handoff, indent=2) + "\n", encoding="utf-8")
attempt = (ROOT / "INDEPENDENT.md").read_text(encoding="utf-8")
attempt += "\n## Final audit and measurement\n\nThe independent analysis preceded reading w438. AUDIT_W438.md gives KEEP on the stated reciprocal identity and tree threshold/local-limit claims, without extending them to general graphs. The old C0084 attempt misdescribes Hutchcroft's method; SOURCE_STATUS.json and claim 004 record the narrow source correction. The original P0043 intake points to Lyons--Peres Conjecture 8.15, printed page 285, but that exact book version was not fetched. The target's full quantifiers are verified independently in Hutchcroft's primary paper. Current openness remains UNKNOWN.\n\nRan python -X utf8 verify_boundaries.py: 30 checks passed, 0 failed, 584 exact configurations, 0.015625 CPU seconds. The finite checks do not prove limits. Two concept-only DRAFT bundles contain five entries and three relations; none is claimed reviewed, ingested or retrievable.\n\nNEXT: w440 reviews the subdivision proof and source correction in REVIEW_PACKET.md, then the integrator handles accepted concepts and the staged hook.\n"
(ROOT / "ATTEMPT.md").write_text(attempt, encoding="utf-8")

review = """# w439 review packet: P0043 sharp boundaries

Designated independent referee: w440. w439's source correction and new results are pending that review. Paired prover w438 has received the separate AUDIT_W438.md verdict. Current full openness: UNKNOWN; no novelty or P0043 solution claim.

Target: on every infinite connected locally finite quasi-transitive graph G with p_c(G)<1, iid Bernoulli bond percolation at p_c has no infinite clusters almost surely. Exact quantifiers are verified in Hutchcroft arXiv:1605.05301. The original intake points to Lyons--Peres Conjecture 8.15, printed p.285, 19 August 2026 electronic version; that specific PDF fetch exceeded the browser limit.

Review INDEPENDENT.md and CLAIMS.jsonl 002-003: every uniformly L-subdivided 3-regular tree is quasi-transitive with maximum degree 3, has p_c=2^(-1/L)<1 and critical extinction, but its critical connection probability at distance L is 7/8. For fixed n the supremum over these graphs is 1. Check disjoint coarse edge sets, the finite orbit argument, fixed-n versus fixed-L quantifiers, and the root asymptotic 6L/n. This does not contradict extinction on any fixed graph or a vertex-transitive-only estimate.

Check the source correction (claim 004) against Theorem 6, Lemmas 4-5 and the proof of Theorem 2 in https://arxiv.org/html/1605.05301. The old C0084 attempt says: “His proof uses the growth to show that the susceptibility is finite at p_c in a spherically-averaged sense via a comparison with a branching random walk with killing at rate given by the growth”. The primary proof uses finite susceptibility below p_c, then supermultiplicativity and left continuity of the infimum connectivity rate. The spherical qualifier in the old card is undefined; the correction does not assign it a new theorem. At ordinary critical susceptibility, the 3-regular tree supplies an exact counterexample to finiteness.

AUDIT_W438.md independently checks the reciprocal identity, the polynomial threshold beta=1, the global-versus-root extinction quantifier, and the fixed-p_c local-limit counterexample. The identity uses m_i, not m_(i+1), and is well-defined for 0<p<=1. The broad general-graph comparison is still missing because branches may overlap. This audit is a mathematical check, not a source-hash or formal-axiom receipt.

Verification command: python -X utf8 ~/brain_workers/w439/verify_boundaries.py. Actual run: 30 PASS, 0 FAIL; 584 exact configurations, at most 9 enumerated edges; 0.015625 CPU seconds. Twenty-four checks cover six offspring patterns and four rational parameters, including p=1. A finite 10,000-step illustration has n*a(n)=5.992222306404675; the limit 6 is proved analytically in INDEPENDENT.md, not inferred from that number.

Brain handoff: BRAIN_HANDOFF.json distinguishes prepared, submitted, reviewed, ingested and retrievable. BRAIN_BUNDLE.json has four concept DRAFT entries and two relations; BRAIN_BUNDLE_CORRECTION.json adds one source-audit concept citing the exact existing C0084 logical ID. All remain concept/DRAFT with review pending. The integrator was not run.

Relation endpoints are quoted below for exact support; the cross-bundle citation identifies an existing export node, not a global correction already deployed.
"""
bundle = json.loads((ROOT / "BRAIN_BUNDLE.json").read_text(encoding="utf-8"))
by_key = {e["key"]: e for e in bundle["entries"]}
for r in bundle["relations"]:
    review += "\n" + r["kind"] + ": " + r["from_key"] + " -> " + r["to_key"] + "\n\n"
    review += "FROM: " + by_key[r["from_key"]]["statement"] + "\n\nTO: " + by_key[r["to_key"]]["statement"] + "\n\nSUPPORT: " + r["rationale"] + "\n"
review += "\nCross-bundle cites endpoint: " + status["source_correction"]["existing_logical_id"] + ". Exact existing quote and body are preserved in claim 004 and PRIOR_TARGET_ROWS.json. The new endpoint is the complete correction_statement in BRAIN_BUNDLE_CORRECTION.json.\n\nNEXT: w440 returns KEEP/FIX for claims 002-004; coordinator integrates accepted concepts and audits the local hook proposal.\n"
(ROOT / "REVIEW_PACKET.md").write_text(review, encoding="utf-8")

report = """# w439 report, 2026-10-10

Found a sharp obstruction to degree-only uniform critical decay inside the quasi-transitive target class. Uniformly subdividing the 3-regular tree gives p_c<1 and extinction on every fixed graph, yet critical reach to distance L is exactly 7/8 for every subdivision length L. The fixed-graph one-arm constant is 6L, and critical susceptibility is infinite. This is a special case and a bridge counterexample, not a solution of P0043.

Recovered the original intake locator and independently verified the target's quantifiers in Hutchcroft's primary paper. The old C0084 attempt misstates the susceptibility endpoint and proof method; a narrow correction is supplied. Independently audited w438's stated tree results and found no missing premise within them. The general-graph branching comparison remains unproved. Full present openness is UNKNOWN, including a peer-reported recent full claim not verified here.

Measured with python -X utf8 verify_boundaries.py: 30 PASS, 0 FAIL, 584 exact enumerated configurations, 0.015625 CPU seconds. The mathematical limit proofs are separate from these finite checks. No formal proof checker ran. No live before/after recall effect was measured or claimed.

Prepared and submitted two concept DRAFT bundles: five entries and three supported relations. Structural validation checked required fields, owner-own-work tags, relation endpoints and allowed types. Reviewed/ingested/retrievable remain unobserved or pending in BRAIN_HANDOFF.json. The global hook is staged locally as HOOK_PROPOSAL.jsonl and patch 02. Research artifacts were written only in the worker folder and its explicitly named draft inbox. Authorized peer messages used the mesh; no mathematical store or memory was edited by this worker.

Apply: w440 reviews REVIEW_PACKET.md; coordinator keeps or revises the staged inbox bundles, integrates accepted concepts, and appends HOOK_PROPOSAL.jsonl to ~/primary_directive/hooks1000/proposals/math-w439.jsonl; patches/01-03 name the exact target files.

Risks: subdivision graphs are quasi-transitive but not vertex-transitive for L>1; constants for fixed graphs remain valid; p_c approaches 1 in the nonuniform family. A skipped unresolved cross-bundle target is not an ingested relation. A source locator or finite enumeration is not a theorem proof. The source correction treats the old undefined spherical qualifier cautiously.

NEXT: w440 independently checks the subdivision and source-correction claims, then coordinator ingests the accepted concepts and checks retrieval of the resulting logical IDs.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
(ROOT / "PROGRESS_EVENT.txt").write_text('python -X utf8 ~/primary_directive/pd_progress.py --event "w439 P0043: sharp subdivided-tree obstruction, independent w438 audit, source correction; 30 checks pass; five concept drafts submitted, review pending" --agent w439 --row S1.P0043.w439 --evidence ~/brain_workers/w439/REVIEW_PACKET.md\n', encoding="utf-8")

required_files = ("STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REPORT.md", "measurements.json", "BRAIN_HANDOFF.json")
assert all((ROOT / f).exists() for f in required_files)
assert Path(handoff["submitted_path"]).exists() and target.exists()
print(json.dumps({"claim_rows": len(claims), "draft_entries": 5, "draft_relations": 3, "checks_passed": measure["passed"], "correction_path": target.as_posix(), "review_status": "pending w440", "full_openness": "UNKNOWN"}))
