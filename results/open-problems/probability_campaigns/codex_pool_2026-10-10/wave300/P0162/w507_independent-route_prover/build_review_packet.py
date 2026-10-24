"""Build a local review packet and publish only the explicitly authorized draft.

The coordinator alone reviews and integrates. No live store or global hook changes.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
measure = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measure["status"] == "PASS"
assert measure.get("affine_phase_and_flip_vertex_checks") == 256


def write_json(name, value):
    (root / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


source_status = {
    "target_id": "P0162", "worker": "w507", "checked_utc": now,
    "exact_target": "For every n>=0 and Boolean f:{-1,1}^n->{-1,1} under the uniform product measure, H_2(f)=sum_S hat(f)(S)^2 log_2(1/hat(f)(S)^2) <= C sum_S |S|hat(f)(S)^2 for one finite C independent of n and f; zero terms are zero.",
    "primary_statement_verified": True, "current_openness": "UNKNOWN",
    "novelty_claim": False, "served_model_settings_verified": False,
    "reason_for_unknown": "Dated local ledgers and recent checked primary papers concern the conjecture or special cases. The bounded check does not certify that no later general solution or owner retirement exists.",
    "primary_sources": [
        {"authors": "Ryan O'Donnell, John Wright, Yuan Zhou", "title": "The Fourier Entropy-Influence Conjecture for certain classes of Boolean functions", "year": 2011,
         "url": "https://www.ias.edu/sites/default/files/math/csdm/10-11/rodonnell_the_fourier_entropy_influence_conjecture.pdf", "locator": "Abstract / introduction", "supports": "Exact uniform-cube Boolean FEI target, attributed to Friedgut-Kalai (1996)."},
        {"authors": "Xiao Han", "url": "https://arxiv.org/abs/2312.08271v2", "revision_date": "2025-12-10", "locator": "Abstract",
         "supports": "General bound O(I(f)+sum_k I_k(f)log(1/I_k(f))); not a dimension-independent FEI proof."},
        {"authors": "Maria Jose Gonzalez, Paul MacManus, Maria Cristina Pereyra", "url": "https://arxiv.org/html/2606.00246v2", "revision_date": "2026-06-09", "locator": "Section 4, equation (21); Appendix B, equation (32)",
         "supports": "Established restriction-entropy framework and good-coordinate sufficient criterion. The ledger here is independently rederived; no novelty claim for it.", "used_hypotheses": "Boolean functions on uniform cube; base-2 entropy."},
        {"authors": "Vladimir N. Potapov", "url": "https://arxiv.org/abs/2609.21563v1", "revision_date": "2026-09-18", "locator": "Abstract",
         "supports": "Reported special-class results for plateaued and partially bent functions, not a reported proof for all Boolean functions.", "reuse": "No theorem from this paper is needed in L1-L4."}
    ],
    "local_evidence": [
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line": 553, "value": "tier 5, P0162, attempted_un", "status_limit": "Dated ranking, not a current openness certificate."},
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a04.json", "logical_name": "attempt-p0162-fourier-entropy-versus-total-influence", "locator": "at-p0162, lines 3345-3367",
         "digest": "Abstract singleton law has H=log_2 n and mean size 1 but cannot be a Boolean squared spectrum: the x_i x_j coefficient of f^2 would be nonzero. Uses Fourier convolution / dropping Booleanity. New route instead retains Booleanity, splices restrictions and quantifies a bad coordinate."},
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006p01.json", "logical_name": "open-problem-p0162-fourier-entropy-versus-total-influence", "digest": "Dated unresolved target, cites O'Donnell Open problems in analysis of Boolean functions, PDF p.5."},
        {"paths": ["probability_1000_attempts_H_20260912", "probability_1000_attempts_I_20260914", "prob1000_lean_20260908"], "result": "Targeted P0162 / exact-title search returned no direct P0162 record in these directories. Related F0090 material exists in the Lean campaign. No formal proof receipt for P0162 was recovered."},
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_F_20260908/problems.jsonl", "locator": "F0090 closure row, line 141", "digest": "Owner's planar-percolation spectral/pivotal entropy special case is recorded closed as author-published 2026-09-13, explicitly unrefereed. It is not a general Boolean FEI solution and is not re-proved here."},
        {"path": "~/brain_workers/teams/W0300_O/TEAM_BOARD.md", "result": "No P0162 row in the checked board."},
        {"path": "~/math-brain-build/export/population", "result": "Targeted grep locates P0162/FEI in nodes/claims/edges and bundle metadata. No whole export was read; the precise read-only store query receipt is READ_ONLY_LOOKUP.json."}
    ],
    "recall": {"receipt": "RECALL_RECEIPT.json", "result": "No output before the required 60-second timeout; loaded-machine wall time was 67.695 seconds.",
               "fallback_scars": ["perceptron_proof_open_gaps_fleet_2026_07_12", "proof_steps_need_derived_joint_structure_2026_09_09"],
               "application": "A successful arithmetic run is not proof of global FEI. The exact entropy ledger uses no products of unsupported conditional bounds."},
    "lane_boundary": "APPROACH_PRECOMMIT.md was saved before any peer proof. The exact bent-base/single-point selector obstruction is the reserved result. No core-lane proof is adopted. Final method comparison and routing receipts are in READ_ONLY_LOOKUP.json and PEER_DELIVERY.json.",
    "formal_verification": {"performed": False, "theorem": None, "trusted_axioms": None, "reason": "Exact integer checks and numerical entropies are diagnostics, not a Lean theorem or an independent referee verdict."}
}
write_json("SOURCE_STATUS.json", source_status)

claims = [
    {"id": "w507.P0162.restriction-ledger", "status": "proved special case",
     "statement": "For every Boolean f on a finite uniform cube and coordinate i, with g=f|i=+1, h=f|i=-1, u=hat(g), v=hat(h), r_T=(u_T^2+v_T^2)/2 and q_T=(u_T-v_T)^2/[2(u_T^2+v_T^2)], Delta_i(f)=JS(u^2,v^2)+sum_T r_T b(q_T)>=0 and I(f)=(I(g)+I(h))/2+I_i(f). Zero r terms vanish.",
     "assumptions": ["uniform product input", "Boolean f", "base-2 entropy", "finite cube"],
     "source": {"path": "ATTEMPT.md", "locator": "L1", "prior_primary": "https://arxiv.org/html/2606.00246v2#S8"},
     "proof_or_counterexample": "Group the squared Walsh coefficients in pairs indexed by T and T union {i}, use the binary entropy identity, entropy concavity and Parseval.",
     "independent_reviewer": "w509 (pending)", "remaining_gap": "Identity is proved in the supplied derivation; no universal local charge follows."},
    {"id": "w507.P0162.canonical-global-bound", "status": "proved special case",
     "statement": "For the canonical quadratic bent splice F_m of ATTEMPT L2, every even m>=2 has I(F_m)=m/2+(m+1)/2^m and H(F_m)<=m+1<=3 I(F_m).",
     "assumptions": ["canonical quadratic base", "single flip at zero", "m even >=2", "uniform input"],
     "source": {"source_id": "owner-own-work:w507:P0162:canonical-global-bound", "path": "ATTEMPT.md", "locator": "L3"},
     "proof_or_counterexample": "Count the toggled boundary edge in each base direction and the one selector discrepancy. The Walsh law has at most 2^(m+1) atoms, so its entropy is at most m+1.",
     "independent_reviewer": "w509 (pending)", "remaining_gap": "Independent review pending; the special-case constant says nothing about a general Boolean f."},
    {"id": "w507.P0162.good-coordinate-principle", "status": "conjecture",
     "statement": "A sufficient unproved route to FEI is the existence of a universal C such that every nonconstant Boolean f on a uniform cube has some relevant i with Delta_i(f)<=C I_i(f). The dimension induction then proves H(f)<=C I(f).",
     "assumptions": ["uniform cube", "C universal", "some relevant coordinate rather than every coordinate"],
     "source": {"url": "https://arxiv.org/html/2606.00246v2", "locator": "Section 4, equation (21)"},
     "proof_or_counterexample": "The implication follows from the exact influence identity and induction on dimension. No proof of the selection inequality is supplied.",
     "independent_reviewer": "w509 (pending)", "remaining_gap": "Construct a universal valid coordinate-selection or aggregate-charging argument. This is the single hardest gap."},
    {"id": "w507.P0162.verification-evidence", "status": "numerical evidence",
     "statement": f"Bounded verification passed for {measure['all_boolean_functions_checked']} Boolean functions in dimensions 0..3, {measure['restriction_ledger_checks']} entropy ledger checks, five canonical bent splices through 11 input variables, and 256 affine-phase/vertex variants in dimension 5.",
     "assumptions": ["exact integer Walsh and boundary counts", "floating-point entropies", "structured larger values evaluated from proved formulas"],
     "source": {"path": "MEASUREMENTS.json", "command": "python -X utf8 verify_obstruction.py"},
     "proof_or_counterexample": "Reproduction script generates truth tables directly and independently compares transform coefficients, neighbor counts, the ledger and the analytic bounds.",
     "independent_reviewer": "w509 (pending)", "remaining_gap": "Numerical tests do not extend the lemma to arbitrary functions or prove the selection principle."}
]
existing = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
seen = {row["id"] for row in existing}
with (root / "CLAIMS.jsonl").open("a", encoding="utf-8") as stream:
    for row in claims:
        if row["id"] not in seen:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")

hook = {"id": "p0162-bent-split-w507-01", "area": "math", "event": "stage-start",
        "cue": "A Fourier-entropy induction charges every coordinate's restriction entropy increment by its influence, or chooses the minimum-influence coordinate without proving the charge.",
        "fire_when": "Proposed Delta_i<=8 I_i for every split; the quadratic bent splice m=10 has minimum-coordinate ratio 14.323620862.",
        "silent_when": "A proof restricts to a named valid class, or leaves the existence of a good coordinate explicitly unresolved, or independently proves its chosen coordinate's charge.",
        "text": "Check which coordinate your entropy induction charges. A bent base with one vertex flipped on one selector branch makes the minimum-influence split's Delta/I grow like dimension. Prove a good-coordinate or aggregate charge; this obstruction does not refute FEI.",
        "evidence": "~/brain_workers/w507/ATTEMPT.md L2-L4; MEASUREMENTS.json family m=10 and 256 phase/vertex controls", "proposer": "w507"}
assert len(hook["text"]) <= 300
(root / "proposals").mkdir(exist_ok=True)
(root / "proposals" / "math-w507.jsonl").write_text(json.dumps(hook) + "\n", encoding="utf-8")


def entry(key, logical, kind, title, statement, assumptions, locator):
    return {"key": key, "namespace": "probability.boolean_fourier", "logical_name": logical,
            "kind": kind, "title": title, "statement": statement, "proof_text": None,
            "assumptions": assumptions, "domain": "probability theory; analysis of Boolean functions",
            "source": {"source_id": "owner-work:w507:P0162:" + key,
                       "url": "urn:owner-work:w507:P0162:" + key,
                       "revision": "2026-10-10-draft-v1", "license": "owner-own-work; campaign derivation, independent review pending", "excerpt": None},
            "draft_review_status": "pending-w509", "proof_artifact": "~/brain_workers/w507/ATTEMPT.md " + locator}


bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w507", "bundle_slug": "p0162-bent-splice-restriction-obstruction-w507-001",
          "entries": [
    entry("delta", "fourier-restriction-entropy-increment", "definition", "Fourier restriction entropy increment",
          "For Boolean f on a uniform cube with base-2 spectral entropy H(f)=sum_S hat(f)(S)^2 log_2(1/hat(f)(S)^2), define Delta_i(f)=H(f)-(H(f|x_i=+1)+H(f|x_i=-1))/2. Total influence is I(f)=sum_S |S|hat(f)(S)^2 and coordinate influence I_i(f)=sum_{S containing i}hat(f)(S)^2. Zero entropy terms vanish.",
          ["finite uniform product cube", "f takes values -1,+1"], "L1"),
    entry("ledger", "fourier-restriction-entropy-js-ledger-draft-w507", "concept", "Draft exact entropy ledger for a Boolean restriction",
          "DRAFT derivation, independent review pending. For g=f|i=+1, h=f|i=-1, coefficients u_T,v_T, r_T=(u_T^2+v_T^2)/2 and q_T=(u_T-v_T)^2/[2(u_T^2+v_T^2)], Delta_i(f)=JS(u^2,v^2)+sum_T r_T b(q_T)>=0. Here b is binary entropy and JS=H(r)-(H(u^2)+H(v^2))/2. Zero r terms vanish. Also I(f)=(I(g)+I(h))/2+I_i(f). The identity is established territory, including arXiv:2606.00246v2 Eq.32.",
          ["uniform cube", "Boolean restrictions", "base-2 entropy"], "L1"),
    entry("bad-charge", "fourier-every-coordinate-entropy-charge-failed-strengthening", "concept", "Failed strengthening: charge every restriction by its influence",
          "The proposed strengthening would demand one finite C with Delta_i(f)<=C I_i(f) for every Boolean f on every finite uniform cube and every coordinate i. The draft bent-splice argument refutes this strengthening, and also refutes choosing the least influential relevant coordinate without an additional argument. It does not refute FEI or a condition requiring just some good coordinate.",
          ["universal constant C", "every coordinate, not an existential choice"], "L2-L4"),
    entry("bent-splice", "bent-point-splice-minimum-influence-obstruction-draft-w507", "concept", "Draft bent splice obstruction to minimum-influence entropy induction",
          "DRAFT author-derived special case, independent review pending. Let m>=4 be even, N=2^m, g:{0,1}^m->{-1,1} have |hat(g)(T)|=1/sqrt(N) for all T, and a be any vertex. Set h=g-2g(a)1_{z=a}, F(z,+1)=g(z), F(z,-1)=h(z). Then I_y(F)=1/N; each other influence is 1/2 plus or minus 1/N, so y is the unique minimum-influence coordinate. Delta_y(F)/I_y(F)>=log_2(N-2sqrt(N)+2), unbounded with m. Nevertheless H(F)<=3 I(F). Spectral entropies and the selector ratio depend only on m. This is a proof-method obstruction, not a general FEI solution or counterexample.",
          ["uniform product input", "base-2 spectral entropy", "even m>=4", "flat Boolean Walsh spectrum", "exactly one flipped vertex on one selector branch"], "L4"),
    entry("good-coordinate", "fourier-good-restriction-coordinate-principle-open", "concept", "Unproved good-coordinate principle sufficient for FEI",
          "UNPROVED selection principle: there is a finite universal C such that every nonconstant Boolean f on a uniform cube has some relevant coordinate i satisfying Delta_i(f)<=C I_i(f). If true, the exact influence decomposition and induction on dimension give H(f)<=C I(f). The bent-splice obstruction does not decide this existential principle. This sufficient route is also stated in arXiv:2606.00246v2 Eq.21.",
          ["C independent of f and dimension", "existence of some relevant coordinate", "uniform product measure"], "Single hardest remaining gap"),
    entry("guard", "fourier-induction-coordinate-charge-guard-draft-w507", "concept", "Draft proof guard for Fourier entropy induction",
          "Before using a restriction-entropy induction, distinguish a proved charge for the chosen split from a bound merely asserted for all splits or for the minimum-influence split. A bent base with a single-vertex selector splice has minimum-coordinate Delta/I growing with dimension while itself satisfying FEI. A valid class-specific charge or an explicitly unresolved selection gap should remain unaffected. Supporting local hook proposal and measurements are in the w507 review packet.",
          ["applicable when a proof attempts restriction-entropy induction"], "L2-L4")],
          "relations": [
              {"from_key": "ledger", "to_key": "delta", "kind": "depends_on", "rationale": "The identity uses the defined entropy increment and influences."},
              {"from_key": "bad-charge", "to_key": "delta", "kind": "depends_on", "rationale": "The failed strengthening is an inequality for that increment."},
              {"from_key": "bent-splice", "to_key": "bad-charge", "kind": "refutes", "rationale": "The lower bound diverges for genuine Boolean functions and for their unique minimum-influence coordinate."},
              {"from_key": "bent-splice", "to_key": "ledger", "kind": "depends_on", "rationale": "Nonnegative JS and binary conditional entropy give the exact lower bound."},
              {"from_key": "good-coordinate", "to_key": "delta", "kind": "depends_on", "rationale": "The existential principle charges the same increment."},
              {"from_key": "guard", "to_key": "bent-splice", "kind": "cites", "rationale": "This exact family supports the fire case; it refutes the strengthened route, not FEI."},
              {"from_key": "good-coordinate", "to_existing_logical": "math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence", "kind": "semantic_association", "rationale": "It is an unproved sufficient route to the exact FEI target, not a solution."},
              {"from_key": "guard", "to_existing_logical": "math:probability.core:attempt-p0162-fourier-entropy-versus-total-influence", "kind": "analogous_to", "rationale": "The older attempt rules out forgetting Booleanity; this obstruction retains Booleanity but rules out an unjustified stronger local charge."}
          ]}
write_json("DRAFT_BUNDLE.json", bundle)

inbox = Path("~/math-brain-inbox/w507")
inbox.mkdir(exist_ok=True)
destination = inbox / "bundle_001.json"
payload = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
if destination.exists():
    if destination.read_text(encoding="utf-8") != payload:
        raise RuntimeError("Existing draft differs; preserve it and choose a new bundle number")
else:
    part = inbox / "bundle_001.json.part"
    with part.open("x", encoding="utf-8") as stream:
        stream.write(payload)
    part.rename(destination)
write_json("BRAIN_SUBMISSION.json", {"bundle": str(destination), "submitted": True, "submitted_utc": now,
                                    "reviewed": False, "ingested": False, "retrievable": False,
                                    "entries": len(bundle["entries"]), "relations": len(bundle["relations"]),
                                    "integration": "Validating coordinator only; integrator was not run because the brief forbids unreviewed live-store mutation."})

comparison = measure["policy_comparison"][-1]
report = f"""P0162 remains unproved. The supplied argument establishes a useful obstruction: splitting the least influential coordinate cannot uniformly charge the restriction entropy increment to that coordinate's influence. Every bent Boolean base with one vertex flipped on one selector branch has this obstruction. The splice itself satisfies FEI with constant 3. The general selection/aggregate-charging step is the single remaining gap of this route; novelty and current openness are UNKNOWN.

Run: python -X utf8 verify_obstruction.py. It passed {measure['all_boolean_functions_checked']} exhaustive Boolean functions, {measure['restriction_ledger_checks']} restriction ledger checks and 256 affine-phase/vertex controls in {measure['elapsed_seconds']:.3f} seconds, with maximum ledger residual {measure['maximum_float_ledger_residual']:.3g}. For the 11-variable canonical splice, the minimum-influence split ratio is {comparison['minimum_influence_split_ratio']:.9f}; the best observed coordinate ratio is {comparison['best_observed_split_ratio']:.9f}. The high-precision formula gives 260.328085123 at 257 variables. These larger evaluations are not exhaustive truth-table tests.

The six-entry draft is at {destination}. Submitted=true; reviewed=false; ingested=false; retrievable=false. The reviewer should check ATTEMPT.md L1-L4, then let the validating coordinator integrate concept material or promote only kept claims. No live system diff is needed: these are new math artifacts. The hook is staged in proposals/math-w507.jsonl; its global publication and the staged progress event require a permitted coordinator write. No unreviewed live-store or global-hook deployment occurred.

NEXT: Independently audit the universal bent-splice proof and pursue a valid good-coordinate or aggregate entropy charge.
"""
(root / "REPORT.md").write_text(report, encoding="utf-8")

packet = """# P0162 review packet for w509

Exact target and assumptions: CLAIMS.jsonl first row; SOURCE_STATUS.json supplies primary attribution, bounded current-status evidence and the owner-percolation-special-case distinction. Precommitted independent route: APPROACH_PRECOMMIT.md.

Main proof: ATTEMPT.md L1-L4. Please independently rederive the hardest claim: for an arbitrary Boolean flat-spectrum base and arbitrary flipped vertex, rephase its Walsh coefficients and prove that exactly (N+sqrt(N))/2 have positive sign; then check the lower entropy charge and the unique minimum-influence selector. Check every influence sign and the dimension restriction m>=4. The canonical family separately includes m=2. A KEEP here is a partial-result verdict, not a proof of FEI.

Reproduction: python -X utf8 ~/brain_workers/w507/verify_obstruction.py. MEASUREMENTS.json distinguishes exact integer computations, floating entropy checks and extended 180-digit evaluations. COMPUTE_GATE.json records the latest fresh gate. No formal theorem/axiom receipt is claimed.

Strongest conclusion: no universal local bound valid for every coordinate, or automatically for the minimum-influence coordinate, can support this induction. The splice still has H<=3I. The exact identity is established literature; no claim that its derivation is new. The single global gap is the unproved good-coordinate/aggregate-charging principle.

Brain delivery: DRAFT_BUNDLE.json mirrors the six concept/definition entries in math-brain-inbox/w507/bundle_001.json. BRAIN_SUBMISSION.json records four separate states. The unproved selection principle is a concept; no parent conjecture has become a theorem. New sources carry owner-own-work. Definitions and concepts have proof_text=null as required by BUNDLE_SPEC.md; their full derivations remain in ATTEMPT.md.

Please return KEEP/FIX/DROP with your independently reproduced argument in your own permitted artifacts and send its path. If you add your own new mathematical lemma, w512 is your named independent referee. No live store integration is requested from an unreviewed worker run.

NEXT: Check L4's sign-count and edge-count argument, then decide whether the drafted obstruction and proof guard can land.
"""
(root / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
write_json("PROGRESS_READY.json", {"agent": "w507", "row": "S1.P0162.w507",
    "event": "P0162: derived universal bent-splice obstruction to minimum-influence entropy induction; bounded verification passed; six draft brain entries submitted, referee check pending.",
    "evidence": str(root / "REVIEW_PACKET.md"), "publication": "staged for permitted coordinator; no global progress write under folder-only restriction"})
(root / "STATUS.md").write_text("STATE: WORKING\nNEXT: Validate the completed draft schema, resolve the named-peer handoff receipts, and set NEEDS_REVIEW.\n\n" + now + ": Complete proof packet and six-entry brain draft saved; verification passed. Global FEI remains unproved; review/ingestion/retrievability are false.\n", encoding="utf-8")
print(json.dumps({"packet": str(root / "REVIEW_PACKET.md"), "brain_draft": str(destination),
                  "claims": len(existing) + sum(r["id"] not in seen for r in claims),
                  "policy_comparison_m10": comparison, "verification_seconds": measure["elapsed_seconds"]}))
