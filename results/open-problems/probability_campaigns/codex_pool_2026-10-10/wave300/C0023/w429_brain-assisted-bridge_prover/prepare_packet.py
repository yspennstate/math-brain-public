import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
metrics = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
rows = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
extra_rows = [{"id": "w429-C1", "status": "proved special case", "kind": "source_application_correction", "statement": "The strict finite-energy hypothesis for independent Bernoulli bond percolation holds exactly for 0<p<1; it fails at p=0 and p=1.", "assumptions": ["Independent Bernoulli edge bits with common parameter p"], "source": {"license": "owner-own-work", "artifact": "CARD_COMPARISON.md", "quoted_card": "claim_19571635c9811ef2c4fa9bf7413abff7ada34807a8dc3b1fc48636004a01b663", "source_quote": "Bernoulli percolation satisfies all three hypotheses for every p"}, "proof": "Independence gives conditional edge-open probability p almost surely. The required strict inequalities hold exactly for an interior parameter. Endpoint uniqueness conclusions are separate direct facts.", "independent_reviewer": "w431; independent Claude review required if processed as a theorem-statement correction", "remaining_gap": "Independent source-application correction review pending.", "audit_status": "PENDING"},
              {"id": "w429-P1", "status": "sketch", "kind": "peer_deduction", "statement": "w430 proposes the sufficient criterion delta<=64^(-4)/(r+1)^2 for a full sigma-field r-dependent site field on Z^d, d>=2.", "assumptions": ["Uniform bad marginal <=delta", "Full sigma-field independence beyond sup-norm range r"], "source": {"license": "owner-own-work", "author": "w430", "artifact": "~/brain_workers/w430/REVIEW_PACKET.md"}, "proof": "Partition the coordinate plane into squares of side r+1 and declare a square good iff all its sites are good. The coarse field is 1-dependent; union-bound bad probability is <=(r+1)^2 delta. Apply w429 L2 at r=1. This is a peer result, not new ownership claimed by w429.", "independent_reviewer": "w431 (pending)", "remaining_gap": "Peer lemma review and actual compatible critical block construction.", "audit_status": "PENDING"}]
existing_ids = {row["id"] for row in rows}
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as handle:
    for row in extra_rows:
        if row["id"] not in existing_ids:
            handle.write(json.dumps(row, ensure_ascii=False)+"\n")
            handle.flush()
lemmas = [row for row in rows if row["id"] in {f"w429-L{i}" for i in range(1,5)}]
assert len(lemmas) == 4
source = {"source_id": "owner-own-work:w429:C0023-finite-range-bridge", "url": "file:///~/brain_workers/w429/ATTEMPT.md", "revision": "2026-10-10-draft-pending-independent-review", "license": "owner-own-work", "excerpt": None}
names = ["local-anchor-high-density-finite-range-counterexample", "finite-range-planar-peierls-sufficient-bound", "finite-bernoulli-event-parameter-stability", "critical-block-bridge-with-explicit-range-margin"]
entries = []
for row, name in zip(lemmas, names):
    entries.append({"key": row["id"], "namespace": "probability.percolation", "logical_name": name, "kind": "lemma", "title": row["id"]+": "+name.replace("-", " "), "statement": row["statement"], "proof_text": row["proof"], "assumptions": row["assumptions"], "domain": "probability theory", "source": source})
concepts = [
    ("gap", "critical-compatible-block-construction-gap", "C0023 compatible finite-block construction: the remaining gap", "The conditional block bridge is not a proof of critical nonpercolation. Its unproved premise is a fixed, finite, deterministically compatible block construction from theta(p_c)>0 with error delta small enough for its actual sigma-field dependence range r. One self-contained sufficient condition is delta<64^(-(r+1)^2). Qualitative uniqueness and a sequence of high marginal densities with uncontrolled growing range do not supply this certificate: the local-anchor counterexample has densities tending to one and only finite good components. Peer w430 has supplied a coarsening criterion delta<64^(-4)/(r+1)^2, pending designated referee w431; it reduces the promising numerical hurdle but does not construct critical blocks."),
    ("bk-endpoints", "bernoulli-finite-energy-excludes-parameter-endpoints", "Bernoulli finite energy requires an interior parameter", "For independent Bernoulli bond percolation with common parameter p, the conditional probability that an edge is open given all other edge states equals p almost surely. Hence the strict finite-energy hypothesis 0<P(edge open | other edges)<1 holds exactly for 0<p<1. At p=0 or p=1 that hypothesis fails; uniqueness conclusions at those endpoints can be checked directly. This corrects the application sentence that all Burton-Keane hypotheses hold for every p, without refuting its interior-parameter uniqueness conclusion. Correction draft: independent review pending."),
    ("status", "critical-lattice-percolation-status-check-2026-10-10", "C0023 dated source status requires review", "The C0023 brain card records a no-resolution-found search dated 2026-09-07. On 2026-10-10, a primary pinned anthropics/formal-math artifact at commit 795efb86f191735c5481675763537cfb4ff37e55 was read and found to claim theta_d(p_c)=0 for nearest-neighbor Bernoulli BOND percolation in every d>=2. Its author reports kernel and comparator checks with propext, Classical.choice, and Quot.sound, while its README states that independent refereeing has not occurred. No local kernel replay or full proof audit was performed by w429. Present openness and acceptance remain UNKNOWN here. The old dated search is historical provenance, not a present openness certificate; no novelty or site-percolation inference is made.")
]
for key, name, title, statement in concepts:
    entries.append({"key": key, "namespace": "probability.percolation", "logical_name": name, "kind": "concept", "title": title, "statement": statement, "proof_text": None, "assumptions": [], "domain": "probability theory", "source": source})
bk = "math:probability.percolation:burton-keane-uniqueness-of-the-infinite-cluster"
target = "math:probability.percolation:open-problem-c0023-no-percolation-at-criticality-on-z-d-for-3-d-10"
relations = [
    {"from_key": "w429-L4", "to_key": "w429-L2", "kind": "depends_on", "rationale": "The fixed-range error condition supplies positive-probability coarse percolation."},
    {"from_key": "w429-L4", "to_key": "w429-L3", "kind": "depends_on", "rationale": "The fixed finite-event margin survives a parameter decrease."},
    {"from_key": "gap", "to_key": "w429-L1", "kind": "depends_on", "rationale": "This explicit increasing-range family refutes the unrestricted high-marginal route recorded in the gap."},
    {"from_key": "gap", "to_key": "w429-L4", "kind": "depends_on", "rationale": "The conditional lemma identifies exactly which critical block premise is absent."},
    {"from_key": "gap", "to_existing_logical": bk, "kind": "cites", "rationale": "The returned uniqueness card gives 0-or-1 infinite clusters under its full hypotheses, not a quantitative finite-block error/range bound."},
    {"from_key": "bk-endpoints", "to_existing_logical": bk, "kind": "cites", "rationale": "The card's strict finite-energy hypothesis is incompatible with its sentence claiming applicability for every Bernoulli parameter; endpoints have conditional probabilities 0 and 1."},
    {"from_key": "status", "to_existing_logical": target, "kind": "cites", "rationale": "The cited current-status search is explicitly as of 2026-09-07; later primary proof claims are located but not accepted as independently checked proofs here."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w429", "bundle_slug": "critical-percolation-finite-range-bridge-w429-001", "entries": entries, "relations": relations}
keys = {entry["key"] for entry in entries}
assert len(keys) == len(entries)
assert all(edge["from_key"] in keys and ("to_key" not in edge or edge["to_key"] in keys) for edge in relations)
assert all(entry["proof_text"] for entry in entries if entry["kind"] == "lemma")
(ROOT / "bundle_001.json").write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf-8")
inbox = Path("~/math-brain-inbox/w429")
inbox.mkdir(exist_ok=True)
dest = inbox / "bundle_001.json"
assert not dest.exists(), "Do not overwrite an existing submitted draft."
part = inbox / "bundle_001.part"
part.write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf-8")
part.rename(dest)
(ROOT / "BUNDLE_STATE.json").write_text(json.dumps({"draft_path": str(dest), "submitted": True, "reviewed": False, "reviewer": "w431 (pending)", "informal_peer_read": "w430 reported L1-L4 sound with the gap unchanged; no served-model or formal KEEP receipt established", "ingested": False, "retrievable": False, "integrator": "codex-01a12190", "served_model_evidence": "UNKNOWN; requested settings not used as proof"}, indent=2), encoding="utf-8")
patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
module = (ROOT / "block_bridge_guard.py").read_text(encoding="utf-8")
patch = "".join(difflib.unified_diff([], module.splitlines(keepends=True), fromfile="a/src/math_brain/block_bridge_guard.py", tofile="b/src/math_brain/block_bridge_guard.py"))
(patches / "01_block_bridge_guard.diff").write_text(patch, encoding="utf-8")
(ROOT / "patch_apply_check").mkdir(exist_ok=True)
hook = {"id": "percolation-w429-01", "area": "math", "event": "stage-start", "cue": "(?is)(percolation|renormalization).*(finite.?dependen|good.?block).*(high.?probab|near.?one|density)", "fire_when": "A high-marginal good-block claim is used for percolation while its dependence range or exposure-filtration bound is absent.", "silent_when": "A fixed-range error bound or uniformly small conditional failure bound for the actual exposure history is explicitly established, along with path compatibility.", "text": "High good-block density needs a dependence certificate. Write r, delta, finite determining bits and path compatibility; check a range-aware bound or conditional bounds for the actual exposure history before concluding percolation.", "evidence": "~/brain_workers/w429/MEASUREMENTS.json: 3/3 explicit finite-range high-density counterexamples; ATTEMPT.md L1-L4; scar perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w429"}
assert len(hook["text"]) <= 300
hooktext = json.dumps(hook, ensure_ascii=False)+"\n"
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hooktext, encoding="utf-8")
hookdest = Path("~/primary_directive/hooks1000/proposals/math-w429.jsonl")
with hookdest.open("a", encoding="utf-8") as handle:
    handle.write(hooktext)
report = f"""Saved four conditional/special-case lemmas and the single unproved C0023 bridge in ATTEMPT.md. L1 gives an exact high-density finite-range field with only finite components. L2-L4 give a conservative, parameter-stable percolation certificate when finite-block independence, compatibility and a range-aware error bound are proved. Current openness is UNKNOWN: SOURCE_STATUS.json distinguishes the old ranking, newer primary claims, and the absent independent/local formal replay. No novelty claim.

The brain lookup returned BK uniqueness, which supplies no quantitative block bound; CARD_COMPARISON.md records its complete hypotheses and an endpoint finite-energy application correction. The attempted domination lookup gave 0/3 needed bridge cards, including two substring matches to independent FPP. Memory recall timed out at 61.724 seconds; the named scar was read directly. These are measured failures, not deployed recall improvements.

Command: python -X utf8 verify_bridge.py. {metrics['checks']} exact geometry, coupling and guard controls passed in {metrics['elapsed_seconds']:.6f} seconds with a fresh light-work resource snapshot. On three constructed high-density nonpercolating fields, an illustrative q>=0.99 rule gave 3 false certificates and the proposed range-aware guard gave 0. Three strict-margin positive controls passed. This is a bounded reasoning safeguard measurement, not a live retrieval benchmark or proof of C0023.

Apply proposal: from ~/math-brain-build, reviewer runs git apply --check ~/brain_workers/w429/patches/01_block_bridge_guard.diff, then git apply that file. It adds src/math_brain/block_bridge_guard.py only; no live recall caller is wired. The guard's proof flags require external audited evidence. The constant is deliberately conservative and may withhold valid routes.

Seven small draft entries and seven exact relations were submitted to {dest.as_posix()}; BUNDLE_STATE.json keeps submission, review, ingestion and retrievability separate. No store mutation or integrator run. A hook proposal is filed at hooks1000/proposals/math-w429.jsonl. Referee w431 has the proof packet; integration route is codex-01a12190. Requested/served identity is not inferred.

w430's separately attributed coarsening lemma weakens the numerical condition to delta*(r+1)^2<64^(-4), pending w431. The prototype retains the independently derived conservative condition. The hardest remaining piece is a compatible critical block construction, not arithmetic or hashes.

NEXT: Independently check the contour/coarsening lemmas; construct local compatible critical blocks with delta*(r+1)^2<64^(-4), or prove conditional success for the actual exposure filtration.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
paths = ["STATEMENT.md", "ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "CARD_COMPARISON.md", "PRIOR_ATTEMPTS.md", "MEASUREMENTS.json", "COMPUTE_GATE.json", "block_bridge_guard.py", "verify_bridge.py", "bundle_001.json", "patches/01_block_bridge_guard.diff", "REPORT.md"]
packet = {"author": "w429", "referee": "w431", "independent_referee_for_w431_new_results": "w434", "scope": "L1-L4 only; no parent theorem proof", "scoped_keep": [], "audit_status": "PENDING", "hardest_gap": "Actual compatible critical blocks with a verified error/range or exposure-filtration condition.", "peer_improvement": "w430/REVIEW_PACKET.md: polynomial coarsening criterion, referee pending", "served_model_evidence": {"author": "UNKNOWN", "referee": "PENDING"}, "artifacts": [{"path": str(ROOT/path), "sha256": hashlib.sha256((ROOT/path).read_bytes()).hexdigest()} for path in paths]}
(ROOT / "REVIEW_PACKET.json").write_text(json.dumps(packet, indent=2), encoding="utf-8")
print(json.dumps({"bundle": str(dest), "entries": len(entries), "relations": len(relations), "checks": metrics["checks"], "review_packet": str(ROOT / "REVIEW_PACKET.json")}, indent=2))
