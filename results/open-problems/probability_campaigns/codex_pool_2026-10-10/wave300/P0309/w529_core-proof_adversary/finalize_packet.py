"""Freeze the cited source rows and write the review packet in this folder only."""
import json
from datetime import datetime, timezone
from pathlib import Path

folder = Path(__file__).resolve().parent
base = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907")
targets = [(base / "brain_bundle_C006p02.json", "op-p0309"), (base / "brain_bundle_C006a05.json", "at-p0309")]
records = []
for path, key in targets:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    selected = [entry for entry in data["entries"] if entry.get("key") == key]
    assert len(selected) == 1, f"Expected one cited target record in {path}"
    records.append({"path": str(path), "key": key, "record": selected[0]})
(folder / "P0309_SOURCE_RECORDS.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
source_path = folder / "SOURCE_STATUS.json"
status = json.loads(source_path.read_text(encoding="utf-8"))
status.update(full_original_statement_recovered=True, original_record_fully_quantified=False,
    exact_original_request="Prove existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted in the review.",
    original_record={"path": str(targets[0][0]), "key": "op-p0309", "kind": "concept", "status_in_record": "source_says_open; current status unverified; unsolved", "saved_exact_entry": "P0309_SOURCE_RECORDS.json"},
    source_provenance_checked="Read the two actual cited bundle files and selected only op-p0309 and at-p0309 by exact entry key; this is provenance, not a mathematical proof.")
status["primary_source"]["inference"] = "The recovered original request cites Lewin Section VI, PDF pages 59-61 and 66-67. It is qualitative about exponent regimes and the meaning of crystalline phase; the explicit neutral 0<s<3 model is a narrowed working subtarget. The experimental HTML display date is not a new paper revision."
status["targeted_prior_work"]["exact_old_attempt"] = {"path": str(targets[1][0]), "key": "at-p0309", "finding": "The prior author checked only the infrared harmonic approximation around an assumed crystal. It explicitly leaves defects, anharmonic fluctuations, competing configurations, Gibbs construction and positional order open; no independent review."}
status["targeted_prior_work"]["paired_prover"] = "Read w528 STATEMENT_FOR_ADVERSARY.md after saving independent C1-C3, then its actual ATTEMPT.md after saving C6-C8. L1-L6 kept only as scoped auxiliaries; reconstruction input G remains unproved."
status["targeted_prior_work"]["owner_solved_retired_check"] = "Targeted named intake/attempt/Lean and population-export checks produced no owner solution or retirement receipt for this target. Absence of a located receipt does not certify present openness."
source_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")

claims = [json.loads(x) for x in (folder / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x]
measurement = json.loads((folder / "MEASUREMENTS.json").read_text(encoding="utf-8"))
bundle = json.loads((folder / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
assert measurement["checks_passed"] and bundle["submitted"]["state"] and bundle["local_validation"] == "passed"
bundle["ingested"] = {"state": "unverified", "receipt": None, "reason": "Coordinator integration not invoked or verified by this worker"}
bundle["retrievable"] = {"state": "unverified", "receipt": None, "reason": "No live-store retrieval receipt"}
(folder / "BUNDLE_STATE.json").write_text(json.dumps(bundle, indent=2), encoding="utf-8")

packet = """P0309 adversary review packet, 10 October 2026.

The hardest unresolved input in the proposed route is a volume-uniform crystalline reconstruction estimate for the unrestricted neutral Riesz gas. It must produce same-particle-count continuum repairs with a positive energy gain and a finite exponential bound on their pushforward reference-measure density, including the real background/exterior energy and dipole sector. Phase coherence and the unperturbed Gibbs limit remain separate inputs. This packet supplies no complete solution or novelty claim; current openness is UNKNOWN.

The recovered source request is qualitative: prove low-positive-temperature crystalline phases for the three-dimensional Coulomb or Riesz gas in the review's predicted regimes. SOURCE_STATUS.json identifies the exact original record and primary source. P0309_SOURCE_RECORDS.json freezes only the two cited problem/old-attempt entries. The chosen 0<s<3 canonical jellium subtarget does not settle the unspecified full exponent range.

Review in this order: CORE_AUDIT.md (the main gap, entropy counterexample and exact conditional comparison); ATTEMPT.md (independent translation/acoustic/Fourier reductions); ADDITIONAL_LEMMAS.md (short-range vacancy and precisely specified harmonic model); CLAIMS.jsonl (all exact assumptions and review states); PEER_VERDICT.jsonl (scope audit of w528 L1-L6).

| Claim | Result and scope | Independent review |
|---|---|---|
| C1 | A global translation refutes a fixed-reference bulk defect penalty on a torus | w530 KEEP in its REVIEW.md |
| C2 | Mean-zero nearest-neighbor acoustic mode defeats a uniform displacement spectral gap | Pending |
| C3 | Matched-particle mismatch and projected displacement moments bound finite-volume Fourier order | Pending |
| C4 | Vacancies have positive conditional probability for ordinary soft s>3 grand-canonical DLR | Pending; not asserted for neutral long-range canonical gas |
| C5 | Cubic Gaussian harmonic inverse trace is at most 13/16 | Pending; no Riesz Hessian or defect control |
| C6 | An extensive pointwise energy gap can coexist with bad-event probability tending to one | Pending; generic two-sector model |
| C7 | A valid area-formula repair with multiplicity M and Jacobian at least J gives probability at most M exp(-beta Delta)/J | Pending; Riesz repair not constructed |
| C8 | An exact translated rigid-template repair has null continuum image and zero Jacobian | Pending; full-dimensional repairs remain possible |

The exact finite-volume order input to attempt is: find a nonzero reciprocal G, measurable phase fitting and matching under the full gas, and volume-independent epsilon_beta,v_beta with E(m/N)<=epsilon_beta and N^-1 E sum_matched(G.u)^2<=v_beta, such that 2 epsilon_beta+v_beta/2<1. C3 then gives E|A_G|^2 >= (1-2 epsilon_beta-v_beta/2)^2. Extracting a genuinely periodic unperturbed infinite-volume Gibbs state is still required.

The repair premise in C7 is explicitly conditional. A contour-count estimate A^n and energy/density constants tau,h would give q/(1-q), q=A exp(h-beta tau)<1, only after actual contour coverage, same-N admissibility, energy gain and entropy domination are proved. w528's L6 already states the entropy hypothesis and is not refuted by C6.

Validation: python -X utf8 ~/brain_workers/w529/verify_math.py. MEASUREMENTS.json records 2,665 bounded evaluations, 0.046875 CPU seconds, 36 matching/phase cases, exact translation-distance controls and harmonic/acoustic constants. These are sanity checks. No formal theorem receipt, Lean proof or live-brain performance claim is made. The proofs and their assumptions are in the cited Markdown.

Brain handoff: BUNDLE_STATE.json records a submitted, locally validated DRAFT with 9 entries and 7 relations. C1 is a checked lemma; all other results and the unproved reconstruction program remain draft concepts. Integration and retrieval receipts are absent. Do not turn numerical controls or compact-charge estimates into a full-target proof.

NEXT: Independently check C2-C8, then test whether a full-dimensional dipole-controlled repair has an entropy bound uniform in the carrier distance and container volume.
"""
(folder / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
report = f"""P0309 is not proved. I isolated the missing unrestricted crystalline reconstruction estimate and audited w528's L1-L6 as scoped auxiliaries. The source record and Lewin's review are recovered; the original request remains qualitative and current openness is UNKNOWN.

The main finding is that energy gain alone cannot bound a continuum Gibbs defect probability. The saved two-sector counterexample has bad probability 0.9999938558 at n=4 even though the naive energy factor is exp(-4)=0.0183156389. A correct repair comparison needs multiplicity/Jacobian or equivalent pushforward-density control. Exact rigid repairs collapse configuration volume. The prior attempt already noticed finite harmonic infrared variance; my discrete bound 13/16 is a scoped quantitative supplement, not a proof of the unrestricted gas.

Measured delivery: 0 to {len(claims)} saved claim rows; 0 to {bundle['entries']} submitted draft entries and {bundle['relations']} relations. python -X utf8 ~/brain_workers/w529/verify_math.py passed {measurement['evaluations']:,} finite checks in {measurement['runtime_cpu_seconds']:.6f} CPU seconds. MEASUREMENTS.json preserves the command and numbers. C1 has an independent w530 KEEP. C2-C8 await review. No live-brain improvement is measured; this is a reviewable mathematical contribution.

Apply: the validating coordinator reviews C2-C8 and integrates the DRAFT at {bundle['submitted']['path']} through the normal inbox pipeline; preserve the concept/draft labels and the unproved G input. No worker integration command was run. BUNDLE_STATE.json separately records submitted, reviewed, ingestion-unverified and retrieval-unverified.

The material risks are scope errors: C4 is only an ordinary s>3 grand-canonical DLR result; C5 is an exactly quadratic model; C3 supplies finite-volume registered order without constructing a periodic Gibbs law. The original title does not fix a full exponent range or an order criterion. CORE_AUDIT.md and REVIEW_PACKET.md state the proof gaps.

A measured entropy hook is prepared in HOOK_PROPOSAL.jsonl and patches/01_continuum_defect_entropy_hook.diff. The folder-only worker brief prevents direct writing to the shared hook proposals directory. Apply that diff from ~ after the hook's pair audit.

NEXT: Referee-check C2-C8 and audit a full-dimensional dipole carrier repair's energy and entropy uniformly in the carrier distance.
"""
(folder / "REPORT.md").write_text(report, encoding="utf-8")
hook = (folder / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").rstrip("\n")
patch_dir = folder / "patches"
patch_dir.mkdir(exist_ok=True)
relative = "primary_directive/hooks1000/proposals/math-w529.jsonl"
patch = f"diff --git a/{relative} b/{relative}\nnew file mode 100644\n--- /dev/null\n+++ b/{relative}\n@@ -0,0 +1 @@\n+{hook}\n"
(patch_dir / "01_continuum_defect_entropy_hook.diff").write_text(patch, encoding="utf-8")
status_text = (folder / "STATUS.md").read_text(encoding="utf-8")
status_text += f"{datetime.now(timezone.utc).isoformat()}: Source records independently selected by exact key; review packet/report and hook diff saved. DRAFT submitted: 9 entries, 7 relations; ingestion and retrieval unverified.\n"
(folder / "STATUS.md").write_text(status_text, encoding="utf-8")
print(json.dumps({"packet": "REVIEW_PACKET.md", "report": "REPORT.md", "source_records": len(records), "claim_rows": len(claims), "bundle": bundle["submitted"]["path"], "complete_target_proof": False}))
