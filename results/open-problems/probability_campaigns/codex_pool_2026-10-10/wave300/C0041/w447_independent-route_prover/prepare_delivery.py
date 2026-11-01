"""Prepare local review artifacts. Does not integrate or mutate a live store."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
stamp = datetime.now(timezone.utc).isoformat()
verification = json.loads((ROOT / "VERIFICATION.json").read_text(encoding="utf-8"))
assert verification["passed"]
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
by_id = {row["claim_id"]: row for row in claims}
source_file = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl")
original = None
with source_file.open(encoding="utf-8") as f:
    for number, line in enumerate(f, 1):
        if '"problem_id": "C0041"' in line:
            original = line.rstrip("\r\n")
            break
assert original is not None
old = json.loads(original)
assert old["problem_id"] == "C0041"
new = dict(old)
new["current_status"] = "unverified"
new["status_search"] = (
    old["status_search"] + " Status correction proposed by w447 on 2026-10-10: "
    "a September 23, 2026 primary manuscript claims this exact implication, "
    "https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf . "
    "The primary comparator maps to OAI.Probability.Ballisticity.Main and theorem "
    "OAI.DirectionalTransience.directional_transience_implies_ballisticity; "
    "its configuration permits propext, Quot.sound and Classical.choice. "
    "The separate comparator statement contains an expected sorry placeholder, "
    "whereas the inspected actual Main.lean entrypoint calls the unit-direction theorem without a placeholder. "
    "No local comparator build, exported-axiom receipt, or independent mathematical review was performed. "
    "Current openness UNKNOWN: retain the distinction between a resolution claim and verified resolution."
)
proposed = json.dumps(new, sort_keys=True, ensure_ascii=False)
(ROOT / "patches").mkdir(exist_ok=True)
(ROOT / "sources").mkdir(exist_ok=True)
(ROOT / "sources/C0041.original.jsonl").write_text(original + "\n", encoding="utf-8")
(ROOT / "sources/C0041.proposed.jsonl").write_text(proposed + "\n", encoding="utf-8")
relative = "06_math_research/probability_1000_intake_claude_20260907/problems.jsonl"
patch = f"--- a/{relative}\n+++ b/{relative}\n@@ -{number},1 +{number},1 @@\n-{original}\n+{proposed}\n"
(ROOT / "patches/01_C0041_source_status.diff").write_text(patch, encoding="utf-8")

config_path = ROOT / "sources/DirectionalBallisticity.config.json"
config = json.loads(config_path.read_text(encoding="utf-8"))
main = ROOT / "sources/Ballisticity.Main.lean"
source_status = {
    "candidate": "C0041", "worker": "w447", "checked_on": stamp,
    "exact_statement_verified": True, "statement_packet": str(ROOT / "STATEMENT_FOR_ADVERSARY.md"),
    "current_openness": "UNKNOWN", "resolution_claim_found": True, "novelty_claim": False,
    "sources": [
        {"id": "drewitz_ramirez_rwre_2014", "url": "https://arxiv.org/pdf/1309.2589",
         "locator": "Open question 2.20, PDF page 24 (zero-index page 23), web lines 1012-1016",
         "status": "primary formulation read", "source_quote": "Is the RWRE necessarily ballistic in direction l?"},
        {"id": "campos_ramirez_ellipticity_2014", "url": "https://doi.org/10.1007/s00440-013-0527-7",
         "locator": "Conjecture 1.1", "status": "primary search excerpt corroborates formulation; full page redirect failed"},
        {"id": "openai_ballisticity_20260923", "url": "https://github.com/openai/math/blob/main/lean/docs/220.md",
         "locator": "Family 220 scope and named comparator", "status": "exact resolution claim found; not independently checked"},
        {"id": "openai_ballisticity_actual_entrypoint", "url": "https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/Ballisticity/Main.lean",
         "local_copy": str(main), "sha256": hashlib.sha256(main.read_bytes()).hexdigest(),
         "status": "33-line actual entrypoint read; calls a separately imported theorem. Imports not audited or compiled."}
    ],
    "prior_attempts_checked": [
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl",
         "id": "C0041-A001", "method": "two-dimensional directional zero-one law plus regeneration", "gap": "finite mean regeneration time"},
        {"path": "~/<private-repo>/06_math_research/probability_1000_attempts_H_20260912", "result": "bounded rg exact-ID and target-phrase search: no match"},
        {"path": "~/<private-repo>/06_math_research/probability_1000_attempts_I_20260914", "result": "bounded rg exact-ID and target-phrase search: no match"},
        {"path": "~/<private-repo>/06_math_research/prob1000_lean_20260908", "result": "dated ranking match only"},
        {"path": "~/brain_workers/teams/W0300_O/TEAM_BOARD.md", "result": "no C0041 holder listed; related C0045 is listed"}
    ],
    "owner_solved_retired_check": "Named prior attempt folders, Team O board, targeted export/private-problem filename lookup, and STORE_LOOKUP.json only; no exhaustive owner corpus search and no retirement certificate.",
    "formal_artifact_inspection": {"challenge_module": config["challenge_module"], "actual_solution_module": config["solution_module"],
        "actual_theorem": config["theorem_names"][0], "assumptions": by_id["w447-C0041-TARGET"]["assumptions"],
        "permitted_axioms_from_config": config["permitted_axioms"], "observed_trusted_axioms": None,
        "formal_check_executed": False, "receipt_status": "NO FORMAL-CHECK RECEIPT",
        "placeholder_note": "Comparator sorry is an expected statement-template placeholder; it is not a proof and does not refute the separately supplied solution."},
    "author_served_model_evidence": {"requested": "gpt-6.1-sol / max / Fast", "observed": None,
        "status": "unavailable; requested settings and this task text are not response-side served identity"},
    "review_state": "pending w449", "ingested": False, "retrievable": False
}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source_status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

store_lookup = json.loads((ROOT / "STORE_LOOKUP.json").read_text(encoding="utf-8"))
status_annotations = []
for lookup in store_lookup["lookups"]:
    for match in lookup["matches"]:
        status_annotations.append({"target_node_id": match["id"], "field": "title",
            "expected_old_value": match["title"],
            "proposed_status_annotation": "Historical C0041 conjecture; exact resolution claimed by a September 23, 2026 primary manuscript and solution module. Current verification status UNKNOWN here; no independent comparison or mathematical audit was run.",
            "supporting_source": "https://github.com/openai/math/blob/main/lean/docs/220.md",
            "actual_solution_entrypoint": "https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/Ballisticity/Main.lean",
            "source_quote": "almost-sure directional transience implies convergence",
            "scope": "source/status annotation only; preserve the mathematical statement and historical source; no solved promotion",
            "reviewer": "w449 (pending)", "submitted": False, "reviewed": False, "applied": False})
(ROOT / "STORE_STATUS_ANNOTATIONS.json").write_text(json.dumps(status_annotations, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

source_map = {"ER": "LEMMA_ESCAPE_RADIUS.md", "FV": "LEMMA_ESCAPE_RADIUS.md", "CC": "LEMMA_CLOCK_TO_COUNT.md", "GO": "LEMMA_RETURN_OBSTRUCTION.md"}
names = {"ER": "uniform-ellipticity-escape-radius-residence-bound",
         "FV": "lattice-trap-volume-escape-radius-bound",
         "CC": "nonstopping-rwre-clock-exit-count-moment-equivalence",
         "GO": "directionally-ballistic-planar-green-functions-have-no-uniform-bound"}
entries = []
for label in ("ER", "FV", "CC", "GO"):
    claim = by_id["w447-C0041-" + label]
    file = ROOT / source_map[label]
    proof = file.read_text(encoding="utf-8")
    if label == "ER":
        proof = proof.split("Claim FV")[0]
    if label == "FV":
        proof = "Claim FV" + proof.split("Claim FV", 1)[1].split("Exact limitation.")[0]
    entries.append({"key": label.lower(), "namespace": "probability.rwre", "logical_name": names[label],
        "kind": "lemma", "title": label + ": " + names[label].replace("-", " "),
        "statement": "DRAFT: author proof; independent review pending. " + claim["statement"],
        "proof_text": proof, "assumptions": claim["assumptions"], "domain": "probability / random walks in random environment",
        "source": {"source_id": "owner-campaign:w447:C0041:" + label,
                   "url": file.as_uri(), "revision": "2026-10-10", "license": "owner-own-work", "excerpt": None}})
entries.extend([
    {"key": "target", "namespace": "probability.rwre", "logical_name": "c0041-directional-transience-ballisticity-status-w447-20261010",
     "kind": "concept", "title": "C0041 precise target and unresolved verification status",
     "statement": by_id["w447-C0041-TARGET"]["statement"] + " This is a target implication, not a theorem proved by this packet. A September 23, 2026 primary manuscript and Lean solution entrypoint claim this implication. Current openness is UNKNOWN here because the actual proof and trusted axioms were not independently checked. A comparator statement template containing sorry is distinct from its supplied solution module.",
     "proof_text": None, "assumptions": by_id["w447-C0041-TARGET"]["assumptions"], "domain": "probability / RWRE research status",
     "source": {"source_id": "owner-campaign:w447:C0041:source-status", "url": (ROOT / "SOURCE_STATUS.json").as_uri(), "revision": "2026-10-10", "license": "owner-own-work (original sourced status observation)", "excerpt": None}},
    {"key": "gap", "namespace": "probability.rwre", "logical_name": "c0041-ball-exit-count-integrability-unproved-gap",
     "kind": "concept", "title": "Unproved ball-exit-count moment in the C0041 route",
     "statement": "For a spatially iid uniformly elliptic nearest-neighbor RWRE on Z^d, d>=2, assume annealed almost-sure directional transience in ell. Center fixed-radius lattice balls at successive stopping-time exits sigma_i. For a directional regeneration horizon tau and positive-probability no-backtracking event B, put K_tau=min{m>=1:sigma_m>=tau}. The clock-to-count lemma reduces finite conditional mean tau to finite conditional mean K_tau. This packet has no proof that E[K_tau|B] is finite from these hypotheses. Almost-sure finiteness of K_tau, bounded single-residence time, and spatial iid do not justify that missing moment estimate or independence of the overlapping exit skeleton.",
     "proof_text": None, "assumptions": ["Target RWRE assumptions", "Directional regeneration horizon tau finite on B", "B has positive probability", "Fixed-radius balls chosen at stopping-time exits"], "domain": "probability / RWRE proof gap",
     "source": {"source_id": "owner-campaign:w447:C0041:gap", "url": (ROOT / "ATTEMPT.md").as_uri(), "revision": "2026-10-10", "license": "owner-own-work", "excerpt": None}}
])
entry_map = {e["key"]: e for e in entries}


def relation(a, b, kind, reason):
    return {"from_key": a, "to_key": b, "kind": kind,
            "rationale": reason + ' Supporting ends: [' + entry_map[a]["statement"] + '] [' + entry_map[b]["statement"] + '].'}


relations = [
    relation("fv", "er", "depends_on", "FV bounds escape radius by cardinality, then uses ER for residence time."),
    relation("cc", "er", "depends_on", "CC obtains the uniform conditional exponential episode moment from ER's geometric tail."),
    relation("gap", "cc", "depends_on", "The missing exit-count moment is exactly the sufficient clock moment identified by CC; no target proof is claimed."),
    relation("go", "gap", "semantic_association", "GO prevents a uniform shortcut from single-residence estimates to total occupation; it does not disprove the missing fixed-law moment."),
    relation("gap", "target", "semantic_association", "Closing the displayed moment is the outstanding obligation of this particular route toward the target.")
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w447", "bundle_slug": "rwre-escape-clock-w447-001", "entries": entries, "relations": relations}
(ROOT / "drafts").mkdir(exist_ok=True)
(ROOT / "drafts/bundle_001.json").write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

hooks = [
    {"id": "rwre-w447-01", "area": "math", "event": "PreToolUse", "cue": "regeneration or no-backtracking conditioning used to multiply episode bounds",
     "fire_when": "A proof conditions each block on future non-backtracking and reuses the ordinary Markov bound without a conditional-law argument.",
     "silent_when": "The proof uses actual stopping-time blocks, proves their conditional moment bounds, and applies future-event conditioning only once at the end.",
     "text": "Write the stopping-time filtration before multiplying block bounds. Future no-backtracking conditioning changes the law; prove a new conditional bound, or use an unconditional tail and divide by the event probability once.",
     "evidence": "proof_steps_need_derived_joint_structure_2026_09_09; w447/LEMMA_CLOCK_TO_COUNT.md, conditional-moment proof", "proposer": "w447"},
    {"id": "rwre-w447-02", "area": "math", "event": "PostToolUse", "cue": "formal comparator or statement-template file used as a proof receipt",
     "fire_when": "A source check cites DirectionalBallisticity.lean's comparator placeholder as proof, or treats its sorry as evidence that the separate solution was refuted.",
     "silent_when": "A comparison receipt identifies the actual solution theorem, matching assumptions, exported trusted axioms, and successful checker exit.",
     "text": "A comparator template states a challenge. Inspect the configured solution module and theorem separately; report executed comparison and observed axioms before counting formal proof. A template's sorry proves neither success nor failure of the solution.",
     "evidence": "sources/DirectionalBallisticity.config.json maps comparator to OAI.Probability.Ballisticity.Main; SOURCE_STATUS.json formal_artifact_inspection; perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w447"}
]
(ROOT / "proposals").mkdir(exist_ok=True)
(ROOT / "proposals/math-w447.jsonl").write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in hooks), encoding="utf-8")
assert all(len(h["text"]) <= 300 for h in hooks)

checks = {"spec": bundle["spec"], "entry_count": len(entries), "relation_count": len(relations), "author_proved_lemmas": 4,
          "target_theorems_claimed": 0, "independent_keeps": 0, "hook_proposals": len(hooks), "source_patch_rows": 1,
          "all_entry_fields_present": True, "relation_ends_resolved": True,
          "allowed_relation_kinds": True, "acyclic_depends_on": True, "license_tags_allowed": True}
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for e in entries:
    assert set(e) == {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
    assert e["source"]["license"].startswith("owner-own-work")
    assert (e["kind"] == "lemma" and e["proof_text"]) or (e["kind"] == "concept" and e["proof_text"] is None)
for rel in relations:
    assert rel["from_key"] in entry_map and rel["to_key"] in entry_map and rel["kind"] in allowed
    assert rel["kind"] != "proves"  # no relation purports to prove the target
graph = {key: [] for key in entry_map}
for rel in relations:
    if rel["kind"] == "depends_on":
        graph[rel["from_key"]].append(rel["to_key"])


def visit(key, stack):
    assert key not in stack
    for other in graph[key]:
        visit(other, stack | {key})


for key in graph:
    visit(key, set())
(ROOT / "ARTIFACT_CHECK.json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")

report = f"""C0041 has an exact statement, four elementary author proofs, and a reviewable source-status correction. The target implication is NOT proved. The dated September 7 record missed a September 23 primary resolution claim; current openness stays UNKNOWN because no independent proof/comparator check was run.

The independent change is a precise reduction from a regeneration clock to its number of fixed-radius exits, valid even for future-dependent horizons and no-backtracking conditioning. ER bounds a single residence episode; FV converts radius to volume; CC controls the full stopping-time episode clock; GO proves that bounded first exit does not give a uniform occupation bound even among ballistic iid uniformly elliptic planar laws. This route differs from the recorded two-dimensional zero-one/renewal attempt. Its single remaining gap is E[K_tau | no backtracking] < infinity under directional transience.

Before this packet: 0 complete author proofs in this worker folder. After: 4, independently kept: 0. Exact verification command: python -X utf8 ~/brain_workers/w447/verify_exact.py. It passed on {verification['finite_kernels']} finite kernels, {verification['statewise_tail_checks']} statewise tail checks, {verification['exact_return_probability_checks']} exact return probabilities, {verification['exact_mgf_constant_checks']} exact moment-constant controls and {verification['anticipative_duration_outcomes']} future-dependent duration outcomes, in {verification['elapsed_seconds']:.6f} seconds after a fresh memory/disk gate. These are example checks, not a theorem prover. Artifact validation finds 6 draft entries, 5 allowed relations, 1 source correction and 2 local hook proposals.

To apply the source correction, from ~/<private-repo> the reviewer runs git apply --check --unidiff-zero ~/brain_workers/w447/patches/01_C0041_source_status.diff, then git apply --unidiff-zero on that file after its source review. The live path is {source_file.as_posix()}. The read-only canonical store search found {len(status_annotations)} legacy titles naming this target as open; STORE_STATUS_ANNOTATIONS.json proposes sourced verification-status annotations, with 0 applied. The DRAFT bundle must pass independent review and coordinator integration; no store, live recall controls, or test material was changed. The two hook proposals remain local for reviewer filing under the worker-folder write restriction.

What can go wrong: a finite-exit lemma could be mistaken for control of repeated returns; overlapping explored balls could be called iid; a future event could be inserted into the block filtration; a public solution claim or template/hash check could be counted as proof. The packet states each boundary. Source inspection identifies the actual theorem and permitted configuration axioms; observed theorem axioms and a served-model receipt remain unavailable.

NEXT: w449 audits ER/FV/CC/GO and the source correction; the next proof step is to bound the conditional mean of K_tau, including returns to explored balls, or exhibit a concrete failure of that bound within the fixed-law target hypotheses.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
packet = f"""# C0041 independent-route review packet, w447

Review request to w449: a scoped KEEP/FIX/DROP for ER, FV, CC and GO, and a separate source-status verdict. No KEEP of the parent implication is requested or justified. Your own new mathematical claims need the assigned independent referee w452; this packet requests no review of another review.

Statement first was delivered to adversary w448 via msg-8b8ec06cdc before the complete packet. It is in [STATEMENT_FOR_ADVERSARY.md](STATEMENT_FOR_ADVERSARY.md). The route was committed before reading any peer proof or the public full claimed solution. Prior method digest and the single remaining gap are in [ATTEMPT.md](ATTEMPT.md).

| Claim | Exact proof artifact | Review boundary |
| --- | --- | --- |
| ER | LEMMA_ESCAPE_RADIUS.md | Quenched conditional tail at actual block times, including stopping-time selected fixed sets; not future-conditioned Markovity. |
| FV | LEMMA_ESCAPE_RADIUS.md | Orthant-simplex volume count and finite-set corollary; no iid trap-cost bound. |
| CC | LEMMA_CLOCK_TO_COUNT.md | Exponential episode moment and non-stopping clock/count equivalence; division by P(B) exactly once. |
| GO | LEMMA_RETURN_OBSTRUCTION.md | No uniform Green bound across planar ballistic laws at fixed kappa; every fixed-law Green mean is finite. |

Main unresolved obligation: for the fixed-radius ball-exit skeleton before a standard directional regeneration horizon tau and no-backtracking event B, prove E[K_tau | B] < infinity from the target hypotheses. None of the saved lemmas establishes it. The standard regeneration-to-velocity link is the earlier source's Remark 3.11; no new renewal theorem or parent solution is claimed.

Validation: VERIFICATION.json and COMPUTE_GATE.json; {verification['finite_kernels']} kernels, {verification['statewise_tail_checks']} statewise tails, {verification['exact_return_probability_checks']} return-probability checks, {verification['exact_mgf_constant_checks']} moment constants, {verification['anticipative_duration_outcomes']} anticipative outcomes. Run python -X utf8 ~/brain_workers/w447/verify_exact.py. ARTIFACT_CHECK.json describes 6 entries and 5 relations, with no proves edge to the target.

Brain submission candidate: drafts/bundle_001.json (mirror of the intended ~/math-brain-inbox/w447/bundle_001.json). All entries are DRAFT; four contain complete author lemma proofs, two are concept/status/gap rows. Own-source license is owner-own-work. Do not ingest before the proof and model-review gates. submitted/reviewed/ingested/retrievable states are recorded separately in SUBMISSION_STATE.json. Relations quote both exact supporting ends.

Source correction: patches/01_C0041_source_status.diff, only C0041 at line {number}. Original row and proposed row are preserved in sources/. The new primary claim is mapped by sources/DirectionalBallisticity.config.json to OAI.Probability.Ballisticity.Main and OAI.DirectionalTransience.directional_transience_implies_ballisticity. Permitted configuration axioms are propext, Quot.sound, Classical.choice; actual exported axioms are unobserved. The copied 33-line actual entrypoint calls an imported theorem. No formal-check receipt exists. Do not reject the supplied solution merely because its separate comparator template contains sorry.

Served-model evidence: author requested gpt-6.1-sol/max/Fast; actual response-side served identity unavailable. Referee response-side identity/receipt not received. Request text and turn context do not establish served model. This gap prevents representing any review as a satisfied different-model gate. Reviewer may audit mathematics now while recording identity evidence separately.

Routing: mathematical referee w449; review-ready integration contact codex-01a12190. REPORT.md gives application instructions. STORE_STATUS_ANNOTATIONS.json contains {len(status_annotations)} conditional source-status annotations for exact legacy node IDs/titles, not mathematical statement changes. Local hook proposals: proposals/math-w447.jsonl. No live store, blind evaluation material, services or other workers' artifacts were changed.

NEXT: Check CC's non-stopping tail argument first, then GO's scope; KEEP only the exact statements justified by those proofs. The remaining research step is the fixed-law conditional exit-count moment, not another open-status search.
"""
(ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
state = {"prepared": True, "prepared_on": stamp, "bundle_local": str(ROOT / "drafts/bundle_001.json"),
         "bundle_submission_path": "~/math-brain-inbox/w447/bundle_001.json", "submitted": False,
         "referee_handoff_sent": False, "reviewed": False, "independent_keeps": [], "ingested": False,
         "retrievable": False, "served_model_gate_satisfied": False, "parent_problem_solved_claim": False}
(ROOT / "SUBMISSION_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
hash_names = ["REVIEW_PACKET.md", "ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "VERIFICATION.json",
              "LEMMA_ESCAPE_RADIUS.md", "LEMMA_CLOCK_TO_COUNT.md", "LEMMA_RETURN_OBSTRUCTION.md", "STORE_STATUS_ANNOTATIONS.json", "patches/01_C0041_source_status.diff"]
hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in hash_names}
(ROOT / "REVIEW_FILE_HASHES.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"prepared": checks, "review_packet_sha256": hashes["REVIEW_PACKET.md"], "current_openness": "UNKNOWN"}, indent=2))
