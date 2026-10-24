"""Write the complete review packet in place and submit only an explicit draft inbox file."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc).isoformat()


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def add_reviews():
    path = ROOT / "REVIEWS.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    new_rows = [
        {"review_id": "P0117-w389-R06", "reviewer": "w389", "author": "w387",
         "artifact": "~/brain_workers/w387/CLAIMS.jsonl", "claim_id": "w387-P0117-C01",
         "verdict": "KEEP", "scope": "Constant-law counterexample to the unqualified iid title only",
         "exact_statement": "For iid unit weights on nearest-neighbor Z^2, every horizontal and vertical coordinate line is a bigeodesic.",
         "assumptions": ["nearest-neighbor Z^2", "constant unit weights"],
         "reproduction": "A coordinate-line segment has ||x-y||_1 unit-weight edges. Every competitor needs at least that many nearest-neighbor steps, so its cost is at least this value. Apply to every finite segment of the line.",
         "hardest_claim_rederived": "The lower bound compares against all lattice competitors, including arbitrarily large detours.",
         "remaining_gap": "No gap in the counterexample; the atomless parent conjecture is unaffected. The route precommit has no quantitative annular obstruction yet.",
         "parent_problem_solved": False},
        {"review_id": "P0117-w389-R07", "reviewer": "w389", "author": "w388",
         "artifact": "~/brain_workers/w388/POSTERIOR_CHECK.md", "claim_id": "w388.P0117.C06",
         "verdict": "KEEP", "scope": "Product posterior given ONE entire individual output and its output-measurable distinct-edge selection",
         "exact_statement": "Independent low-to-high replacements on a deterministic finite edge set F have, given the complete individual output Y, independent raise flags with probabilities 1_high(Y_e)delta_e/(p_b+delta_e). A finite simple prefix selected from Y alone restricts that kernel legitimately.",
         "assumptions": ["independent edgewise triples", "a<b, p_a=G([0,a])>0, p_b=G([b,infinity))>0", "deterministic finite modification set and deterministic 0<=delta_e<p_a", "selection measurable from this output alone", "distinct prefix edges", "no conditioning on another coupled output or later marking success"],
         "reproduction": "With L=[0,a], H=[b,infinity), the joint flag/output densities relative to G are f_1=delta_e/p_b*1_H and f_0=1-delta_e/p_a*1_L. Their sum is positive. The ratio on H is delta_e/(p_b+delta_e), and elsewhere is zero. Independence of pairs factors the finite conditional kernel; independent exterior plus a cylinder-function/monotone-class argument extends conditioning to the whole Y. Given Y, the selected finite edge list is fixed; partitioning by its countably many possible distinct lists justifies restriction. Completion-measurable selectors have almost-sure Borel versions.",
         "hardest_claim_rederived": "The adaptive edge selection is deterministic after conditioning on the entire individual output, so the finite product is justified under exactly that sigma-algebra.",
         "remaining_gap": "The usable-prefix/cone premises, cross-site coupling, no-fork argument, common-label Busemann pairs and final budget are not certified by this posterior calculation. It does not certify the manuscript's Theorem 1.1.",
         "parent_problem_solved": False},
    ]
    existing = {row["review_id"] for row in rows}
    with path.open("a", encoding="utf-8") as stream:
        for row in new_rows:
            if row["review_id"] not in existing:
                stream.write(json.dumps(row) + "\n")
                rows.append(row)
    return rows


def source_status():
    source_path = Path(r"~/Downloads/Probability_1000_20h_20260906/sources/fpp_survey_2015/source.pdf")
    survey = fitz.open(source_path)
    recent = fitz.open(ROOT / "public_no_bigeodesics_20260924.pdf")
    value = {
        "target": "P0117", "worker": "w389", "checked_at": NOW,
        "current_openness": "UNKNOWN", "parent_problem_solved": False,
        "novelty_claim": False,
        "ranking": {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line": 552, "tier": 5, "dated_status": "attempted_un", "certifies_current_status": False},
        "exact_intake_record": {"path": "~/Downloads/Probability_1000_20h_20260906/problems.jsonl", "lines": [188, 600], "source_id": "fpp_survey_2015", "exact_scope": "Nondegenerate continuous iid planar FPP in the positive-speed setting; constant deterministic weights are excluded by the intended scope.", "historical_status_search": "2026-09-14 reported no resolution but explicitly noted degraded search engines"},
        "survey": {"title": "Auffinger, Damron and Hanson: 50 years of first-passage percolation", "url": "https://arxiv.org/pdf/1511.03262", "archived_pdf": str(source_path), "page_count_measured": len(survey), "question": 31, "section": "4.5", "physical_pdf_page_verified": 98, "printed_page_verified": 98, "excerpt": "Question 31. Do geodesic lines exist?", "source_record_statement_date": "2016-09-26", "locator_caveat": "This is the archived 160-page version. Earlier survey editions have different page numbers; the minimum-of-four moment is not stated by this short question itself.", "evidence": "survey_page_excerpt.json"},
        "precise_primary_conjecture": {"source": "Damron and Hanson, Bigeodesics in first-passage percolation", "url": "https://arxiv.org/html/1512.00804v2", "location": "Conjecture 1", "statement": "For finite nonnegative iid edge weights with a continuous common distribution on the nearest-neighbor graph Z^2, almost surely no self-avoiding bi-infinite geodesic exists. Every finite segment must minimize against all finite lattice paths.", "moment_assumption_in_conjecture": "NONE stated"},
        "working_moment_qualified_case": {"assumptions": ["nearest-neighbor Z^2", "finite nonnegative iid edge weights", "atomless common law", "E[min(X1,X2,X3,X4)^2]<infinity for four independent weights"], "extra_shape_assumption": "NONE in this working target; any imported differentiability theorem is separately conditional"},
        "established_inputs_checked": [
            {"url": "https://arxiv.org/html/1512.00804v2", "location": "Theorem 1.1", "assumptions": ["iid continuous weights", "finite mean", "differentiable full limit-shape boundary"], "conclusion": "For each preassigned deterministic direction, no bigeodesic has an end in that direction almost surely", "does_not_supply": "A simultaneous random-direction exclusion"},
            {"url": "https://arxiv.org/html/2208.11576v1", "location": "Theorem 1.1 and Section 2.4 A1", "assumptions": ["iid continuous weights", "finite second moment of the minimum of four incident weights"], "conclusion": "The probability that a prescribed distant vertex is visited by an infinite geodesic from 0 tends to zero uniformly with distance", "does_not_supply": "Vanishing raw forward-ray shell sum; that sum is at least one when rays exist"}
        ],
        "prior_attempt": {"path": "~/Downloads/Probability_1000_20h_20260906/attempts.jsonl", "line": 119, "id": "P0117-A001", "full_problem_solved": False, "gap": "Opposite-endpoint finite geodesics need not stay anchored in a fixed bounded region"},
        "owner_solved_retired_check": {"state": "NO CERTIFIED P0117 RESOLUTION IN THE TARGETED LOCAL RECORDS", "exhaustive": False, "checked": ["original P0117 ledger and attempt", "H/I attempt directories and lean ranking via targeted P0117 searches", "Open problem project/solved_register.md via FPP/geodesic/percolation terms", "Big Open problem in probability theory/README.md", "width-3 directed FPP solved memory (different model)", "canonical population store's P0117 cards"]},
        "canonical_store": {"path": "~/math-brain-build/local/population/brain.sqlite3", "mode": "read-only URI", "target_cards": 2, "truth_status": "unverified", "evidence": "live_store_check.json", "supporting_memory_slug": "prob1000_mathbrain_two_bundles_15_nodes_retrievable_2026_09_07"},
        "recent_claimed_resolution": {"title": "No bigeodesics in planar first-passage percolation", "author_as_printed": "OPENAI", "date_as_printed": "September 24, 2026", "url": "https://raw.githubusercontent.com/openai/math/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf", "pdf_pages_measured": len(recent), "actual_theorem": "Theorem 1.1", "hypotheses": ["finite nonnegative iid nearest-neighbor weights on Z^2", "atomless common law", "E[min(X1,X2,X3,X4)^2]<infinity"], "claimed_conclusion": "All self-avoiding bigeodesics are absent in one probability-one event, including random end-directions", "mathematical_certification": "NOT CERTIFIED by w389", "partial_check": "Low-to-high replacement posterior independently derived in R07; geometric transfer, no-fork, common Busemann and global budget steps remain unchecked", "evidence": ["public_manuscript_listing.json", "public_manuscript_extract.json", "public_dependency_pages.json", "POSTERIOR_REDERIVATION.md"]},
        "formal_check": {"run": False, "theorem_receipt": None, "trusted_axioms_receipt": None, "note": "PDF identity, mechanical schema validation and finite diagnostic checks are not formal mathematical proof receipts"},
        "recall": {"path": "recall.txt", "exit_code": 0, "target_id_absent_in_general_memory_recall": True, "math_store_target_present": True},
    }
    write_json("SOURCE_STATUS.json", value)


def posterior_proof():
    (ROOT / "POSTERIOR_REDERIVATION.md").write_text(
        "Independent reviewer w389: KEEP w388.P0117.C06 under individual-output conditioning.\n\n"
        "Put L=[0,a], H=[b,infinity), p_a=G(L), p_b=G(H). For a single independent triple, "
        "P(xi=1,Y in D)=delta G(D intersect H)/p_b. Also P(xi=0,Y in D)="
        "integral_D (1-delta 1_L/p_a)dG. Since a<b and delta<p_a, their sum density is positive. "
        "Its posterior ratio on H is (delta/p_b)/(1+delta/p_b)=delta/(p_b+delta), and elsewhere is zero.\n\n"
        "Independent pairs (xi_e,Y_e) on the deterministic finite modification set give the product "
        "conditional kernel. All unchanged exterior outputs are independent of these pairs. Test "
        "against exterior cylinder events, then extend by a monotone class to the entire individual "
        "output sigma-algebra. After conditioning on Y, a finite edge list chosen from Y alone is "
        "fixed. Partition by its countably many possible distinct finite lists to restrict the "
        "kernel; completion-measurable choices have almost-sure Borel versions.\n\n"
        "Densities are relative to G, so no Lebesgue density is required. This permits the finite "
        "conditional count variance sum theta_e(1-theta_e). It licenses no product after conditioning "
        "on coupled outputs at different sites, hidden-raise-dependent selection, or later marking "
        "success. The usable-prefix and cone hypotheses and the global bigeodesic argument remain "
        "separate obligations.\n", encoding="utf-8")


def submit_draft():
    local = ROOT / "drafts/bundle_001.json"
    bundle = json.loads(local.read_text(encoding="utf-8"))
    if len(bundle["entries"]) != 4 or len(bundle["relations"]) != 5:
        raise ValueError("Unexpected draft shape")
    if any(entry["kind"] not in {"concept", "definition"} for entry in bundle["entries"]):
        raise ValueError("Unreviewed draft promoted to theorem/lemma")
    inbox = Path(r"~/math-brain-inbox/w389")
    inbox.mkdir(parents=True, exist_ok=True)
    for index in range(1, 1000):
        final = inbox / f"bundle_{index:03d}.json"
        temporary = inbox / f"bundle_{index:03d}.part"
        if final.exists() and final.read_text(encoding="utf-8") == local.read_text(encoding="utf-8"):
            break
        if final.exists() or temporary.exists():
            continue
        # The task explicitly names this isolated DRAFT inbox. Never replace any
        # pre-existing file or call an integrator. The full write precedes rename.
        temporary.write_text(local.read_text(encoding="utf-8"), encoding="utf-8")
        temporary.rename(final)
        break
    else:
        raise RuntimeError("No unused authorized draft filename")
    parsed = json.loads(final.read_text(encoding="utf-8"))
    if parsed != bundle:
        raise AssertionError("Queued draft differs from validated local draft")
    lifecycle = {"agent": "w389", "bundle_slug": bundle["bundle_slug"], "as_of": NOW,
                 "prepared": {"state": "COMPLETE", "path": str(local)},
                 "submitted": {"state": "QUEUED DRAFT", "path": str(final), "atomic_rename": True},
                 "reviewed": {"state": "PENDING DESIGNATED INDEPENDENT AUDIT", "reviewer": "w392", "request_message_id": "msg-8213baa7c0", "own_claims": ["C02", "C03"]},
                 "ingested": {"state": "NOT CONFIRMED", "integrator_run_by_w389": False},
                 "retrievable": {"state": "NOT MEASURED", "live_recall_probe_run": False},
                 "entries": 4, "relations": 5, "new_lemma_or_theorem_entries": 0,
                 "resource_claim": "clm-cb070127e4"}
    write_json("BUNDLE_LIFECYCLE.json", lifecycle)
    return final


def reports(rows, final):
    counts = Counter(row["verdict"] for row in rows)
    packet = """# P0117 referee packet

Reviewer w389, 2026-10-10. Seven peer claims reviewed: six KEEP, one FIX. REVIEWS.jsonl records exact statements, assumptions, reproductions and gaps. No parent-problem or novelty claim is certified.

The decisive correction is R03. w388's incidence inequality is valid, but the proposed vanishing raw forward-ray shell count is impossible: every infinite simple ray hits each surrounding shell. If rays exist almost surely, its expectation is at least 1 and the maximum shell probability is at least 1/(8n). w388 accepted the correction and withdrew the closing goal in ATTEMPT.md. The saved paragraph diff is historical and must not be applied to its already corrected file.

| Peer claim | Verdict | Result checked | Remaining gap |
| --- | --- | --- | --- |
| w387 C01 | KEEP | Constant-law horizontal and vertical bigeodesics | Atomless parent unaffected; annular obstruction not supplied |
| w388 C01 | KEEP | Constant-law horizontal bigeodesic | Atomless parent unaffected |
| w388 C02 | KEEP | Nested root-crossing events and anchored two-arm compactness | No decay estimate |
| w388 C03 | FIX | Keep incidence inequality; discard impossible raw shell-decay goal | Need an attainable two-sided estimate |
| w388 C04 | KEEP | Endpoint count and witness-partition counterexample | No FPP union estimate |
| w388 C05 | KEEP | Global-distance localization under 0<a<=weights<=b | No asymptotic decay and no general-law extension |
| w388 C06 | KEEP | Exact posterior given ONE individual output and its measurable distinct prefix | Coupled-output conditioning, geometric premises and full theorem not certified |

I independently reconstructed C02's centered-prefix tree and C06's joint densities/product kernel. POSTERIOR_REDERIVATION.md states the exact conditioning boundary.

Own C02 is a distinct stationary occupation identity: the expected fraction of the inner box on ANY full-lattice boundary-to-boundary finite geodesic tends to the probability of a bigeodesic through 0. Own C03 is the shell floor. Designated referee w392 has request msg-8213baa7c0; AUDIT_REQUEST.md identifies the prefix tree, tie handling, inclusions, measurability and probability checks. Own claims and their relations remain draft concepts pending that receipt.

SOURCE_STATUS.json separates the ranking and version-specific survey question, the moment-free primary conjecture, conditional/fixed-origin established results, and the September 24 claimed moment-qualified resolution. Current openness is UNKNOWN. The latter's replacement posterior has been narrowly checked; geometric transfer, no-fork, common-label Busemann and global budget arguments are not certified here.

The draft has four entries and five relations, with both endpoint statements saved in RELATIONS_EVIDENCE.jsonl, including two confirmed existing P0117 cards. Shape, license-prefix and DAG checks passed. These mechanical checks and the finite diagnostics are not mathematical proof certificates. BUNDLE_LIFECYCLE.json separately tracks submission, review, ingestion and retrieval.

NEXT: Derive an attainable two-sided estimate implying E|D_n|=o(n^2), with the designated C02/C03 audit before any theorem promotion.
"""
    (ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
    write_json("PATCH_STATUS.json", {"patch": "patches/01_shell_decay_correction.diff", "state": "SUPERSEDED_BY_PEER_CORRECTION", "live_path": "~/brain_workers/w388/ATTEMPT.md", "reason": "w388 already accepted and applied R03. Preserve the historical proposal; do not apply to the corrected artifact."})
    measurements = json.loads((ROOT / "measurements.json").read_text(encoding="utf-8"))
    report = (
        "P0117 referee deliverable: found an impossible closing goal and w388 accepted the correction. "
        "Its valid shell-incidence inequality remains. Every infinite ray crosses every shell, so the "
        "raw expected forward-ray shell count is at least 1 and its maximum probability at least 1/(8n); "
        "the proposed vanishing count and o(1/n) rate cannot hold. REVIEWS.jsonl has "
        f"{len(rows)} peer verdicts: {counts['KEEP']} KEEP and {counts['FIX']} FIX.\n\n"
        "The independent route is a stationary occupation identity: E|D_n|/|B_n| tends to the "
        "probability of a bigeodesic through 0 when D_n includes all global boundary-to-boundary "
        "minimizers through the inner box. Its required iid o(n^2) estimate is unproved. Own results "
        "are explicitly draft concepts pending w392; the audit request is queued. w388's new "
        "posterior lemma was separately rederived and kept only under individual-output conditioning.\n\n"
        f"Measurements: python -X utf8 check_congestion.py passed {measurements['inclusion_cases_passed']} "
        f"exact finite cases covering {measurements['inner_vertex_cases_checked']} inner-vertex cases "
        f"in {measurements['elapsed_seconds']:.4f} seconds of calculation. For constant weights the "
        "crossing-line count divided by box area falls from 1/17 at n=8 to 1/1025 at n=512, while "
        "occupied density stays 1. This diagnoses the count/occupation distinction and does not test "
        "iid atomless asymptotics. python -X utf8 prepare_bundle.py validates four entries, five "
        "relations, allowed source tags and acyclic dependencies; each relation has both ends quoted.\n\n"
        "Exact sources are in SOURCE_STATUS.json. The archived 160-page survey puts Question 31 "
        "on physical/printed page 98; older editions use other locators. A September 24 public "
        "Theorem 1.1 claims the full atomless iid case under the minimum-of-four second moment. "
        "Its full argument is not certified in this packet, so current openness is UNKNOWN. "
        "Source identity and mechanical checks are not formal proof receipts.\n\n"
        f"The complete DRAFT is queued at {final}. Submission, designated review, ingestion and "
        "retrieval are separate states in BUNDLE_LIFECYCLE.json. Brain deployment and recall "
        "measurement remain for the validating coordinator. HOOK_PROPOSAL.jsonl and "
        "PROGRESS_EVENT.json are staged locally under this worker's write boundary. The explicit "
        "task inbox and named-peer mesh are the only shared outputs used.\n\n"
        "Apply: the validating coordinator audits drafts/bundle_001.json and ingests its queued "
        "copy after the required independent keeps; the paragraph diff in patches/ is already "
        "superseded by w388's accepted correction.\n\n"
        "Risks: confusing a global minimizer with a box minimizer; selecting one path when ties "
        "require the full union; extending the posterior product to coupled outputs or later "
        "success events; treating a partial lemma as the parent proof.\n\n"
        "NEXT: Establish an attainable all-endpoint two-sided estimate yielding E|D_n|=o(n^2); "
        "obtain w392's C02/C03 audit before theorem promotion.\n"
    )
    (ROOT / "REPORT.md").write_text(report, encoding="utf-8")
    write_json("PROGRESS_EVENT.json", {"agent": "w389", "row": "S1.P0117.w389.R03", "event": "P0117: w388 accepted shell-floor correction (raw shell count >=1); 7 peer audits and 4-node/5-relation draft ready; parent unproved", "evidence": str(ROOT / "REVIEWS.jsonl"), "state": "STAGED_FOR_COORDINATOR", "reason": "Worker-local write boundary; explicit task authorizes named draft inbox and peer mesh, not global progress-page files", "command_for_coordinator": "python -X utf8 ~/primary_directive/pd_progress.py --event \"P0117 w389: accepted shell-floor correction; 7 peer audits; 4 nodes/5 relations drafted; parent unproved\" --agent w389 --row S1.P0117.w389.R03 --evidence ~/brain_workers/w389/REVIEWS.jsonl"})


if __name__ == "__main__":
    rows = add_reviews()
    source_status()
    posterior_proof()
    final = submit_draft()
    reports(rows, final)
    print(json.dumps({"queued_draft": str(final), "peer_reviews": len(rows), "verdicts": dict(Counter(row['verdict'] for row in rows)), "parent_problem_solved": False, "own_review": "PENDING w392"}))
