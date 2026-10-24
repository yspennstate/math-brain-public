"""Save final scoped mathematical verdicts and a revised, unintegrated concept draft."""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
PEERS = ROOT.parent


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def put_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def save_peer_verdicts():
    rows = [
        {
            "review_id": "P0117-w389-R08", "claim_id": "w387-P0117-C02", "scope": "L1 finite-cylinder pinned reduction",
            "exact_statement": "For finite nonnegative weights on nearest-neighbor Z^2, A_n(v) is existence of a simple centered 2n-edge path shortest in the induced l1-ball B_n(v). These finite-cylinder events decrease and their intersection is exactly a full-lattice bigeodesic through v. For random weights P(bigeodesic through v)=lim_n P(A_n(v)).",
            "assumptions": ["finite nonnegative weights", "nearest-neighbor Z^2", "simple centered paths", "finite-ball minimization at each level"],
            "reproduction": "A competing shorter central segment in B_n splices into the B_(n+1) witness; nonnegative loops can be erased. Therefore central restriction gives nesting. The finite sets of centered witnesses form a finitely branching tree. An infinite branch is simple. Every finite competing full-lattice path lies inside some later ball, so a sufficiently late witness compares against it and proves global optimality. Conversely every bigeodesic supplies all witnesses. Continuity from above gives the probability identity; stationarity and a countable vertex union give the simultaneous-absence reduction.",
            "hardest_claim_rederived": "Box-constrained certificates become globally minimizing only at the intersection: each fixed competitor is compared inside a later ball, not inside the initial small ball.",
            "remaining_gap": "No decay of P(A_n(0)) is proved; this reduction does not solve P0117."
        },
        {
            "review_id": "P0117-w389-R09", "claim_id": "w387-P0117-C03", "scope": "L2 exclusion of prescribed infinite paths",
            "exact_statement": "Under iid finite nonnegative nondegenerate weights on Z^2, every prescribed infinite simple path is almost surely not a geodesic. The conclusion holds for any countable prescribed family and any path sampled independently of the weights.",
            "assumptions": ["iid finite nonnegative nondegenerate edge weights", "path geometry deterministic or sampled independently of the weights"],
            "reproduction": "Choose 0<=a<b with q=P(t<=a)>0 and p=P(t>=b)>0. Infinitely many turns yield infinitely many disjoint square trials: two high path edges versus two low opposite edges, each with probability p^2 q^2. A simple path visits any finite edge neighborhood only finitely often, so deterministic greedy extraction is possible. If turns are finite, the tail is straight; choose m with m(b-a)>2a and separated m-edge blocks with parallel m+2-edge detours, each trial probability p^m q^(m+2)>0. In either case disjoint edge trials are independent and the probability of avoiding the first k shortcuts tends to zero. Countable union and conditional Fubini give the two stated extensions.",
            "hardest_claim_rederived": "Disjoint trial supports can be selected from the fixed infinite path before observing weights, and a local strict shortcut alone excludes global geodesicity even if its detour meets another part of the path.",
            "remaining_gap": "Weight-selected paths are not covered; an uncountable union of null fixed-path events is not licensed."
        },
        {
            "review_id": "P0117-w389-R10", "claim_id": "w387-P0117-C04", "scope": "L3 selected-path probability counterexample",
            "exact_statement": "With iid Uniform[1,2] weights, the full-lattice geodesic from (0,0) to (1,1) is almost surely the cheaper of the two two-edge square routes. For a fixed route, its two edges >=7/4 and the other two <=5/4 has probability 1/256. For the selected minimizing route the same high-selected/low-other event, also conditional on which route was selected, has probability zero.",
            "assumptions": ["iid Uniform[1,2] edge weights on nearest-neighbor Z^2", "route selected as the minimizer from those same weights"],
            "reproduction": "Every other simple route has at least four edges and cost >=4, whereas each square-route cost is <4 almost surely. Their independent continuous sums are distinct almost surely. Four fixed-edge threshold events have product probability (1/4)^4=1/256. A selected route of cost >=7/2 cannot beat the other route of cost <=5/2, so the event is empty up to the null exceptions.",
            "hardest_claim_rederived": "This is a counterexample inside the actual full lattice, since positivity and parity exclude all longer routes as competing minimizers.",
            "remaining_gap": "No gap in this counterexample; it refutes a probability-transfer step, not absence of bigeodesics."
        },
        {
            "review_id": "P0117-w389-R11", "claim_id": "w387-P0117-C05", "scope": "L4 fixed-path exponential bound and deterministic dictionaries",
            "exact_statement": "For iid finite nonnegative nondegenerate weights, choose 0<=a<b, p=P(t>=b)>0, q=P(t<=a)>0, integer L>=2 with L(b-a)>2a, R=2(L+1), D=1+2R(R+1), eta=p^L q^(L+2). Each prescribed simple N-edge path has geodesic probability <=(1-eta)^ceil(floor(N/L)/D). A deterministic finite dictionary has the corresponding cardinality union bound. It tends to zero if log|P_N|-kappa ceil(floor(N/L)/D) tends to minus infinity, kappa=-log(1-eta).",
            "assumptions": ["iid finite nonnegative nondegenerate edge weights", "simple candidate path fixed before weights", "deterministic finite candidate dictionaries", "L>=2 and L(b-a)>2a; p,q>0"],
            "reproduction": "Partition into M=floor(N/L) blocks. A turning block supplies a two-edge square shortcut with probability p^2 q^2>=eta; otherwise simplicity makes the block straight and supplies an L+2-edge parallel detour, with probability eta and cost <=(L+2)a<Lb. Each support lies in the l1-ball of radius L+1 around its distinct block start. Overlapping supports require start distance <=R, so each greedy selection removes at most D candidates. There are at least ceil(M/D) disjoint edge supports, chosen deterministically, and their shortcut events are independent. A geodesic avoids all of them, giving the product bound. Union bounds require no independence between dictionary members. A ray with covered prefixes for every N lies in each dictionary-success event; a bound tending to zero excludes it.",
            "hardest_claim_rederived": "The greedy packing constant D counts distinct block starts within a radius-R lattice ball; independence applies only after geometric extraction before weight observation. A full reproduction is in SHORTCUT_REDERIVATION.md.",
            "remaining_gap": "G1: no deterministic dictionary with a diverging entropy deficit covering all potential bigeodesic arms, no vanishing uncovered-candidate probability, and no selection-valid resampling alternative have been established. Pointwise log|P_N|<cN with bounded deficit is insufficient."
        }
    ]
    existing = {row["review_id"] for row in read_jsonl(ROOT / "REVIEWS.jsonl")}
    with (ROOT / "REVIEWS.jsonl").open("a", encoding="utf-8") as stream:
        for row in rows:
            if row["review_id"] in existing:
                continue
            row.update(reviewer="w389", author="w387", artifact="~/brain_workers/w387/ATTEMPT.md", verdict="KEEP", parent_problem_solved=False, novelty_claim=False, status="independently checked proof")
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()


def save_receipts():
    wanted = {"P0117-w392-review-w389-C02", "P0117-w392-review-w389-C03", "P0117-w392-review-w389-relations"}
    receipts = []
    for line in (PEERS / "w392/CLAIMS.jsonl").read_text(encoding="utf-8").splitlines():
        if not any('"' + key + '"' in line for key in wanted):
            continue
        row = json.loads(line)
        if row.get("id") in wanted:
            receipts.append(row)
    if {row["id"] for row in receipts} != wanted:
        raise AssertionError("Missing designated independent receipt")
    (ROOT / "AUDIT_RECEIPTS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in receipts), encoding="utf-8")
    claims = read_jsonl(ROOT / "CLAIMS.jsonl")
    for row in claims:
        if row["claim_id"] not in {"P0117-w389-C02", "P0117-w389-C03"}:
            continue
        suffix = row["claim_id"].split("-")[-1]
        row["status"] = "independently checked proof"
        row["independent_reviewer"] = "w392"
        row["independent_review"] = {"review_id": "P0117-w392-review-w389-" + suffix, "verdict": "KEEP", "receipt": "AUDIT_RECEIPTS.jsonl", "scope": "exact reduction or shell lower bound; no parent solution", "account_provenance": "native agent identity recorded; different-login quorum not certified"}
        row["remaining_gap"] = ("The iid estimate E|D_n|=o(n^2) remains unproved; the independently checked reduction does not solve P0117." if suffix == "C02" else "This checked shell lower bound refutes one proposed closing premise. A genuinely two-sided occupation-decay estimate remains missing.")
    (ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")
    return receipts


def revise_bundle(receipts):
    from prepare_bundle import validate
    bundle = json.loads((ROOT / "drafts/bundle_001.json").read_text(encoding="utf-8"))
    bundle["bundle_slug"] += "-v2-reviewed"
    for entry in bundle["entries"]:
        entry["statement"] = entry["statement"].replace("AUTHOR-CHECKED DRAFT for P0117; w392 independent audit pending", "INDEPENDENTLY KEPT BY w392 for the stated scope; DRAFT ingestion pending")
        entry["statement"] = entry["statement"].replace("AUTHOR-CHECKED AUDIT SCAR; w392 independent review pending", "AUDIT SCAR INDEPENDENTLY KEPT BY w392 for the stated scope; DRAFT ingestion pending")
        entry["source"]["revision"] = "independently-checked-by-w392-2026-10-10-v2"
        entry["source"]["license"] = "owner-own-work (w392 independent KEEP for exact scope; draft ingestion pending)"
    for rel in bundle["relations"]:
        rel["rationale"] = rel["rationale"].replace("an attainable equivalent target", "a logically equivalent but unproved target")
        rel["rationale"] = rel["rationale"].replace("Author-checked draft; independent audit pending.", "Independent w392 KEEP recorded in AUDIT_RECEIPTS.jsonl; no occupation decay is proved.")
        rel["rationale"] = rel["rationale"].replace("Independent audit pending.", "Independent w392 KEEP recorded in AUDIT_RECEIPTS.jsonl.")
    validate(bundle)
    local = ROOT / "drafts/bundle_002.json"
    put_json(local, bundle)
    quotes = {entry["key"]: entry["statement"] for entry in bundle["entries"]}
    evidence = read_jsonl(ROOT / "RELATIONS_EVIDENCE.jsonl")
    for row, rel in zip(evidence, bundle["relations"], strict=True):
        row["from_statement_quote"] = quotes[rel["from_key"]]
        if "to_key" in rel:
            row["to_statement_quote"] = quotes[rel["to_key"]]
        row["rationale"] = rel["rationale"]
        row["independent_review"] = "P0117-w392-review-w389-relations: KEEP_WITH_WORDING_FIX; required wording corrected in v2"
        row["bundle_version"] = "bundle_002.json"
    (ROOT / "RELATIONS_EVIDENCE.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in evidence), encoding="utf-8")
    inbox = Path("~/math-brain-inbox/w389")
    final = inbox / "bundle_002.json"
    if final.exists():
        if json.loads(final.read_text(encoding="utf-8")) != bundle:
            raise AssertionError("Existing reviewed draft differs; preserve it")
    else:
        temporary = inbox / "bundle_002.json.part"
        if temporary.exists():
            raise AssertionError("Unexpected existing part file; preserve it")
        put_json(temporary, bundle)
        temporary.rename(final)
    lifecycle = json.loads((ROOT / "BUNDLE_LIFECYCLE.json").read_text(encoding="utf-8"))
    lifecycle.update(bundle_slug=bundle["bundle_slug"], as_of=datetime.now(timezone.utc).isoformat())
    lifecycle["prepared"] = {"state": "COMPLETE", "path": str(local)}
    lifecycle["submitted"] = {"state": "QUEUED REVIEWED DRAFT", "path": str(final), "atomic_rename": True}
    lifecycle["reviewed"] = {"state": "DESIGNATED INDEPENDENT KEEP; WORDING FIX APPLIED", "reviewer": "w392", "receipt": "AUDIT_RECEIPTS.jsonl", "receipt_ids": [r["id"] for r in receipts], "own_claims": ["C02", "C03"], "different_login_quorum_certified": False}
    lifecycle["superseded_submissions"] = [{"path": str(inbox / "bundle_001.json"), "state": "PRESERVED; SUPERSEDED BY bundle_002.json", "action": "Coordinator should select bundle_002.json only; w389 has not edited or deleted the old queued draft"}]
    put_json(ROOT / "BUNDLE_LIFECYCLE.json", lifecycle)
    put_json(ROOT / "bundle_validation.json", {"status": "PASS", "command": "python -X utf8 refresh_reviewed_packet.py", "entries": 4, "relations": 5, "lemma_or_theorem_entries": 0, "relation_ends_quoted": 5, "source_license_prefix": "owner-own-work", "depends_on_acyclic": True, "independent_review": "w392 KEEP for C02/C03; relation wording corrected", "different_login_quorum_certified": False, "mathematical_proof_certificate": False, "live_store_write": False})
    return final


def write_reports(final):
    reviews = read_jsonl(ROOT / "REVIEWS.jsonl")
    counts = Counter(row["verdict"] for row in reviews)
    (ROOT / "REPORT.md").write_text(f"""P0117 referee packet is ready for review. One impossible closing estimate was corrected: the expected raw forward-ray shell count is always at least one when a ray exists. w388 accepted the correction. A stationary two-sided boundary-occupation identity provides an equivalent, still unproved decay target. w392 independently kept this identity and the shell lower bound.

I independently checked {len(reviews)} peer claims ({counts['KEEP']} KEEP, {counts['FIX']} FIX), including w387's finite-cylinder reduction, fixed-path shortcuts, selected-path counterexample and exponential bound, and w388's individual-output posterior kernel. The hardest shortcut proof is reproduced in SHORTCUT_REDERIVATION.md; the posterior derivation is in POSTERIOR_REDERIVATION.md. REVIEWS.jsonl records exact assumptions and gaps.

Measurements: `python -X utf8 check_congestion.py` passed 6 finite cases and 102 inner-vertex cases in 0.0509 seconds of calculation. Endpoint witness controls have union probability one despite each marginal being 1/n^2, for n=2,4,16,64. The shell-floor correction removes the proposed goal sum q->0: before, one peer closing goal asked for this; after, it is explicitly withdrawn and replaced by a two-sided obligation. These are finite diagnostics and a documented proof correction; no numerical estimate of infinite-iid occupation decay or live recall improvement is claimed. `python -X utf8 verify_packet.py` checks required artifacts and the submitted/local draft match; its result is FINAL_CHECKS.json.

Four concept/definition entries and five relations are queued at `{final.as_posix()}`. w392's three receipts are in AUDIT_RECEIPTS.jsonl. The required relation wording is now 'logically equivalent but unproved'. Use bundle_002.json only; the older queued bundle_001.json remains preserved and is superseded. Submission, independent review, ingestion and retrieval are separate in BUNDLE_LIFECYCLE.json. Ingestion and retrieval are unconfirmed. Different-login quorum is not certified by native agent IDs alone.

Source status: the archived survey's Question 31 is on page 98 in the 160-page version. The original ranking is September 7, 2026. A primary September 24, 2026 manuscript claims absence for atomless iid finite nonnegative weights with E[min(t1,t2,t3,t4)^2]<infinity; its full proof has not been audited here. Current openness is UNKNOWN. Source identity, finite diagnostics and schema checks are not formal proof receipts, and no full solution or novelty is claimed.

What could go wrong: treating a confined shortest path as a global witness at one fixed scale; substituting forward-ray occupation for two-sided occupation; multiplying shortcut probabilities after path selection; conditioning the posterior lemma on coupled outputs or later success; treating a partial lemma as the parent theorem. The reviewed records explicitly exclude these extensions.

How to apply: the validating coordinator should review and ingest the corrected `bundle_002.json` through the normal DRAFT workflow. w389 has not edited live code or stores. The historical patches/01_shell_decay_correction.diff is superseded by w388's accepted fix and must not be applied. PROGRESS_EVENT.json and HOOK_PROPOSAL.jsonl stage coordinator actions locally because this worker may not write the global progress/proposal paths.

NEXT: Prove E|D_n|=o(n^2) for the atomless iid target by a genuinely two-sided estimate, or supply a selected-path resampling law or deterministic candidate cover with a diverging entropy deficit.
""", encoding="utf-8")
    table = "\n".join(f"| {r['review_id']} | {r['author']} | {r['claim_id']} | {r['verdict']} |" for r in reviews)
    (ROOT / "REVIEW_PACKET.md").write_text(f"""P0117 remains unproved in this packet. Current openness is UNKNOWN because the recent primary claimed resolution has not been checked in full.

| Review | Author | Claim | Verdict |
|---|---|---|---|
{table}

Every verdict has an exact statement, assumptions, independent reproduction and remaining gap in REVIEWS.jsonl. w388's R03 FIX retains its incidence inequality and withdraws its impossible vanishing shell-count goal. w387 L1-L4 KEEP is restricted to finite-cylinder reduction, prescribed paths, the actual Uniform[1,2] selection counterexample and deterministic dictionaries. No shortcut probability is multiplied after selection by the weights. The entropy condition requires a diverging deficit, or a strict limiting rate gap.

Own C02 and C03 were independently kept by w392. The five relations received KEEP_WITH_WORDING_FIX; the requested wording and pending-review metadata were corrected in bundle_002.json. AUDIT_RECEIPTS.jsonl preserves the exact receipts. Native reviewer identity is known; different-login quorum is not certified. C01 is an elementary constant-law counterexample and remains outside the bundle.

Load-bearing reproductions: ATTEMPT.md (occupation sandwich, centered compactness and shell floor); SHORTCUT_REDERIVATION.md (w387 shortcut independence and dictionary bound); POSTERIOR_REDERIVATION.md (w388 posterior kernel under a single entire individual output).

Measurements: 6 exact finite cases / 102 inner vertices, 0.0509 seconds calculation. Four draft entries / five relations / zero lemma or theorem promotions. Queued reviewed draft: `{final.as_posix()}`. Ingestion and retrievability remain unconfirmed; no live integrator was run. FINAL_CHECKS.json records the mechanical artifact checks separately from mathematical review.

The single parent gap is an iid two-sided decay estimate E|D_n|=o(n^2), equivalently vanishing centered two-arm witness probability. Fixed-path shortcuts do not prove that estimate, and the forward-ray shell sum is bounded below by one.

NEXT: Derive a two-sided occupation estimate or a selection-valid resampling/candidate-cover bound.
""", encoding="utf-8")
    (ROOT / "AUDIT_REQUEST.md").write_text("Completed designated audit: w392 kept C02/C03 and kept all five relations subject to one wording fix. Receipt IDs and exact statements are in AUDIT_RECEIPTS.jsonl. The requested fix is applied in drafts/bundle_002.json and the separately queued bundle_002.json. No parent proof, independent-login quorum, ingestion or retrievability is claimed.\n", encoding="utf-8")
    progress = json.loads((ROOT / "PROGRESS_EVENT.json").read_text(encoding="utf-8"))
    progress.update(event="P0117 w389: 11 scoped peer verdicts; w392 kept occupation identity and shell-floor scar; reviewed 4-node/5-edge concept draft queued as bundle_002; parent decay gap open", agent="w389", row="S1.P0117.w389", evidence=str(ROOT / "REPORT.md"))
    progress["command_for_coordinator"] = ('python -X utf8 ~/primary_directive/pd_progress.py --event "' + progress["event"] + '" --agent w389 --row S1.P0117.w389 --evidence ~/brain_workers/w389/REPORT.md')
    put_json(ROOT / "PROGRESS_EVENT.json", progress)
    (ROOT / "ATTEMPT.md").open("a", encoding="utf-8").write("\nIndependent audit receipt, 2026-10-10: w392 KEEP for C02 and C03; exact receipts in AUDIT_RECEIPTS.jsonl. Relation wording fix applied in bundle_002.json. The iid estimate E|D_n|=o(n^2) is still the hardest missing step; no full P0117 solution is claimed.\n")
    with (ROOT / "STATUS.md").open("a", encoding="utf-8") as stream:
        stream.write("2026-10-10: Saved 11 independent peer verdicts (10 KEEP, 1 FIX), recorded w392 KEEP receipts for own C02/C03, and queued revised bundle_002.json (4 concepts/definitions, 5 relations). Older queued draft is preserved and superseded; no live integration. Final mechanical check and named-peer notices remain.\n")
    print(json.dumps({"peer_reviews": len(reviews), "verdicts": dict(counts), "own_independent_keep": ["C02", "C03"], "queued_reviewed_draft": str(final), "parent_problem_solved": False}))


if __name__ == "__main__":
    save_peer_verdicts()
    saved_receipts = save_receipts()
    queued = revise_bundle(saved_receipts)
    write_reports(queued)
