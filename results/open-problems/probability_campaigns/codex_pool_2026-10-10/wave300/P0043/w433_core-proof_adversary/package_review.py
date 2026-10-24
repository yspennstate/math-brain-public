"""Prepare local, unpromoted mathematical audit concepts and review receipts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATE = "2026-10-10"
ATTEMPT_URL = "file:///~/brain_workers/w433/ATTEMPT.md"
NS = "probability.percolation"
entries = []

def concept(key, name, title, statement, assumptions, section):
    entries.append({
        "key": key, "namespace": NS, "logical_name": name,
        "kind": "concept", "title": "DRAFT: " + title,
        "statement": "Independent mathematical audit draft; referee review pending, with no novelty claim. " + statement,
        "proof_text": None, "assumptions": assumptions,
        "domain": "probability theory",
        "source": {
            "source_id": "owner-own-work:w433:P0043:" + key,
            "url": ATTEMPT_URL + "#section-" + str(section),
            "revision": "campaign-2026-10-10-v1",
            "license": "owner-own-work (campaign audit and independently derived special cases)",
            "excerpt": None
        }
    })

concept("target", "critical-quasitransitive-percolation-scope-audit-w433",
    "Critical quasi-transitive percolation: scope and unverified present status",
    "The target concerns independent Bernoulli bond percolation on an infinite connected locally finite quasi-transitive graph G with p_c(G)<1: no infinite cluster should exist at p_c(G). The p_c<1 assumption is necessary, since the two-sided line has p_c=1 and its p=1 cluster is the whole line. The historical primary statement is Hutchcroft (2016), Conjecture 1.1. A 2026-09-24 public manuscript and accompanying Lean solution claim the full target, but this worker has not reproduced their verification; present openness is UNKNOWN, not certified open or solved.",
    ["independent Bernoulli bond percolation", "G infinite, connected, locally finite and quasi-transitive", "p_c(G)<1 for the target"], 1)

concept("thinning", "critical-component-quenched-thinning-fragility-audit-w433",
    "Critical infinite components must be maximally fragile under independent thinning",
    "For a countable connected locally finite graph G with p_c(G)>0, almost surely each infinite component H of G[p_c(G)], if any exists, has its own bond threshold p_c(H)=1. Independent q thinning gives the iid law at p_c(G)q<p_c(G). Its zero survival probability makes the nonnegative conditional survival probability zero almost surely; intersect over vertices and rational q<1. This is a reduction only: it does not prove that infinite critical components are absent.",
    ["countable connected locally finite G", "p_c(G)>0", "iid critical bonds", "thinning variables independent of the entire critical configuration"], 2)

concept("comb", "density-one-comb-thinning-obstruction-audit-w433",
    "Density one does not guarantee survival of thinning",
    "Every infinite connected nearest-neighbor tree T embedded in Z^d has p_c(T)=1: at most (2n+1)^d simple root paths have length n, so their q-open union has probability at most (2n+1)^d q^n. In Z^2 the connected acyclic graph retaining all vertical edges and only the horizontal row y=0 spans every vertex and has density one, yet has p_c=1. This comb is not quasi-transitive and is not an iid lattice cluster; it refutes density-only robustness and does not refute the critical quasi-transitive target.",
    ["integer d>=1", "T infinite, connected and acyclic", "nearest-neighbor lattice edges", "independent q bond thinning"], 3)

concept("dependence", "high-marginals-growing-dependence-obstruction-audit-w433",
    "Arbitrarily high open marginals with bounded components and finite dependence",
    "Give Z^d iid continuous site labels. For integer R>=1 let c(x) be the minimum-label site in the radius-R sup-norm box about x, and open x exactly when c(x) equals c(y) for all nearest neighbors y. This translation-invariant field is independent on sets separated by sup-norm distance greater than 2R+2. Every open component has one common winner z and lies in the radius-R box about z, so it has at most (2R+1)^d sites. Its exact open marginal is (2R-1)^d/((2R+1)^d+2d(2R+1)^(d-1)), which tends to one. For d=2,R=399 this is 635209/641597>0.99, while no component is infinite. Thus a block proof needs quantitative control of both its error and its dependence range. This construction does not assert iid Bernoulli, FKG or insertion tolerance.",
    ["integer d>=1", "integer R>=1", "iid continuous site labels", "open rule defined by agreement of local minima"], 5)

concept("pivotal", "critical-window-pivotal-mass-gap-audit-w433",
    "Critical-window uniform pivotal control is an unproved input",
    "For a fixed root o in a countable connected locally finite graph with 0<p_c<1, let f_n(p) be the finite-ball probability of an open root connection to its distance-n sphere, and I_n=f_n'. The identity theta_o(p_c)=0 is equivalent to lim_{delta down to 0} sup_{n>=1} integral_{p_c-delta}^{p_c} I_n(p) dp=0. A uniform L^r bound on a fixed interval below p_c for some r>1 suffices. Uniform L^1 mass or pointwise derivative limits do not suffice. The paired proof's general quasi-transitive uniform bound remains unproved; the equivalence is not a proof of the full target.",
    ["countable connected locally finite G", "independent Bernoulli bond law", "0<p_c<1", "finite-ball root-to-sphere events with n>=1"], 8)

concept("tree-bound", "regular-tree-critical-window-derivative-bound-audit-w433",
    "A tightened derivative control on regular trees",
    "On the D-regular tree, D>=3, write b=D-1 and c_b=(b-1)/(2b)*(1-1/b)^(b-2). For every n>=1 and 0<=p<=1/b, the derivative f_n'(p) of the root-to-radius-n connection probability satisfies f_n'(p)<=D/c_b. Forward-tree survival satisfies s_m(p)<=1/(1+c_b*m), while open pivotals give p*s_m'(p)<=m*s_m(p); the root derivative is at most D*(m+1)/(1+c_b*m)<=D/c_b. At p=0 use polynomial continuity. For D=3 this gives 12 on [0,1/2], improving the paired proof's valid bound 27 on [1/4,1/2]. This supplies a regular-tree special case of pivotal uniform control only; cyclic subexponential graphs remain outside this argument.",
    ["integer D>=3", "iid Bernoulli bonds on the D-regular tree", "n>=1", "0<=p<=1/(D-1)"], 8)

relations = [
    {"from_key": "thinning", "to_key": "target", "kind": "semantic_association", "rationale": "The thinning argument describes a necessary property of any hypothetical critical infinite component; it does not prove the target."},
    {"from_key": "comb", "to_key": "thinning", "kind": "analogous_to", "rationale": "The comb is an explicit maximally fragile infinite connected graph, illustrating why density cannot rule out the property forced by critical thinning. The laws and quasi-transitivity assumptions differ."},
    {"from_key": "dependence", "to_key": "target", "kind": "semantic_association", "rationale": "The local-minimum field refutes a generic high-marginal block-proof shortcut; it is not a counterexample to iid critical percolation."},
    {"from_key": "pivotal", "to_key": "target", "kind": "semantic_association", "rationale": "Critical-window uniform pivotal control at every root is an equivalent reformulation of the zero-critical-percolation conclusion, not an established input."},
    {"from_key": "tree-bound", "to_key": "pivotal", "kind": "specializes", "rationale": "The regular-tree uniform derivative estimate implies the critical-window condition on this special graph class, leaving the general input unproved."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w433", "bundle_slug": "p0043-criticality-audit-w433-001", "entries": entries, "relations": relations}
draft_dir = ROOT / "drafts"
draft_dir.mkdir(exist_ok=True)
(draft_dir / "bundle_001.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
by_key = {entry["key"]: entry for entry in entries}
edge_rows = [{**rel, "from_statement_quoted": by_key[rel["from_key"]]["statement"], "to_statement_quoted": by_key[rel["to_key"]]["statement"], "review_status": "DRAFT; w434 pending"} for rel in relations]
(ROOT / "RELATION_EVIDENCE.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in edge_rows) + "\n", encoding="utf-8")

hook = {
    "id": "probability-w433-01", "area": "math", "event": "stage-start",
    "cue": "A block-percolation proof infers domination or percolation solely from marginal probabilities tending to one while its dependency range depends on the chosen scale.",
    "fire_when": "The proof obtains error epsilon after expanding inspection radius R, then invokes a k-dependent domination threshold without bounding k(R) and checking epsilon against that threshold.",
    "silent_when": "A fixed finite dependence range and a quantitative valid error threshold are established, or a complete conditional exploration argument supplies the joint bound, or the obligation remains explicitly unproved.",
    "text": "Before using high block probabilities, fix the dependence range and check the required error at that same scale. Marginals can exceed 99% in a translation-invariant finite-dependent field with every component finite when the range grows.",
    "evidence": "w433/ATTEMPT.md section 5; MEASUREMENTS.json high_density_obstruction: 635209/641597>0.99, component bound 638401; memory slug proof_steps_need_derived_joint_structure_2026_09_09",
    "proposer": "w433"
}
assert len(hook["text"]) <= 300
hook_line = json.dumps(hook, ensure_ascii=False)
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hook_line + "\n", encoding="utf-8")
patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
live_path = "~/primary_directive/hooks1000/proposals/probability-w433.jsonl"
(patch_dir / "01_probability_quantifier_hook.diff").write_text("--- a/" + live_path + "\n+++ b/" + live_path + "\n@@ -0,0 +1 @@\n+" + hook_line + "\n", encoding="utf-8")

formal_receipt = {
    "status": "NOT_REPRODUCED", "target": "P0043", "checked_date": DATE,
    "actual_theorem": "OAI.CriticalPercolation.BondGraph.no_percolation_at_criticality",
    "solution_module": "OAI.Probability.CriticalPercolation.Main",
    "solution_url": "https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/CriticalPercolation/Main.lean",
    "comparator_url": "https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.json",
    "assumptions": ["BondGraph V E with labelled bonds, allowing loops and multiplicities", "Infinite V", "G.fullGraph.Connected", "G.LocallyFinite (incident bonds finite)", "G.QuasiTransitive (finite vertex orbits under bond-preserving automorphisms)", "G.criticalProbability<1"],
    "conclusion": "G.law G.criticalProbability G.percolates = 0",
    "permitted_axioms_in_configuration": ["propext", "Quot.sound", "Classical.choice"],
    "actual_trusted_axioms": "UNKNOWN; no dependency-closure or kernel/comparator run performed",
    "visible_solution_body": "Located: proof uses main_failure_topological_classification_counterexample and compact_open_virtually_nilpotent_quotient_of_sparse_polynomial. The imported dependency chain was not exhaustively read or verified.",
    "challenge_placeholder": "The comparator challenge has an intentional sorry. It is not the separately supplied solution and does not count as proof.",
    "kernel_verification": "NOT_RUN", "statement_fidelity": "Top-level assumptions inspected; full measure and imported-definition semantics not independently verified",
    "mathematical_proof_certified": False,
    "primary_manuscript_access": "Public PDF linked by scope note; web raw access returned unsupported octet-stream, and shell public download failed DNS. No mathematical verdict on that PDF is claimed."
}
(ROOT / "FORMAL_CHECK_RECEIPT.json").write_text(json.dumps(formal_receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

source_status = {
    "target": "P0043", "worker": "w433", "checked_date": DATE,
    "current_openness": "UNKNOWN", "novelty_claim": False, "full_target_proved_here": False,
    "complete_statement": "For independent Bernoulli bond percolation on every infinite connected locally finite quasi-transitive graph G with p_c(G)<1, G[p_c(G)] has no infinite cluster almost surely.",
    "original_id_record": {"path": "~/Downloads/Probability_1000_20h_20260906/problems.jsonl", "lines": [46, 143], "source_id": "lyons_peres_20260819", "locator": "Conjecture 8.15, printed p.285", "historical_status": "source_says_open", "current_status_in_record": "unverified"},
    "original_attempt": {"path": "~/Downloads/Probability_1000_20h_20260906/attempts.jsonl", "line": 43, "attempt_id": "P0043-A001", "result": "Known regular-tree critical extinction only", "full_problem_solved": False, "independent_review": "none", "gap": "Loops in general critical clusters invalidate an independent-branching replacement"},
    "ranking_source": {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line": 549, "record_date": "2026-09-07", "status": "attempted_un", "tier": 5},
    "primary_statement_checked": {"url": "https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2016.07.013.pdf", "author": "Tom Hutchcroft", "year": 2016, "locators": ["Introduction", "Conjecture 1.1", "Theorems 1.2-1.3", "Lemmas 1-2", "Theorem 2.5"], "scope": "Exponential-growth subclass proved; general conjecture stated with p_c<1"},
    "recent_claim": {"url": "https://github.com/openai/math/blob/main/lean/docs/213.md", "manuscript_title": "No percolation at criticality on quasi-transitive graphs", "manuscript_date": "2026-09-24", "scope_claim": "full quasi-transitive bond theorem with p_c<1", "status": "CLAIMED_RESOLUTION_NOT_REPRODUCED", "receipt": "FORMAL_CHECK_RECEIPT.json"},
    "prior_work_checked": [
        "Named P0043 original problems/attempts ledger rows; original regular-tree case already known, no novelty claimed",
        "Named H0016 duplicate record in probability_1000_intake_H_20260914/problems.jsonl line 16; not an independent graph-wide result",
        "No P0043-labelled row found by targeted searches in attempts_H_20260912 or attempts_I_20260914; this is not an exhaustive mathematical absence claim",
        "prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md P0043 row; no formal proof receipt supplied by that row",
        "Team O board: related C0084 held by w344; w433 avoids that worker's general ten-problem source packet",
        "Named owner percolation project selected nonuniqueness p_c<p_u on nonamenable graphs, not this criticality theorem; no solved/retired certificate for P0043 inferred",
        "Named math-brain population nodes: C0084 open-problem card at line 1737 and author-unreviewed attempt mechanism at line 260",
        "Canonical math-research-brain README and targeted named-store location probe; store result recorded separately if located"
    ],
    "brain_scars_used": ["prob1000_proofs_directory_audit_what_is_spent_and_what_is_live_2026_09_08", "perceptron_proof_open_gaps_fleet_2026_07_12", "proof_steps_need_derived_joint_structure_2026_09_09"],
    "note": "Source matching and visible theorem declarations do not certify a mathematical or formal proof. No current open/solved classification is asserted."
}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source_status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress = {"event": "w433 P0043: independent thinning/dependence obstructions, paired-proof audit, regular-tree derivative bound 27 to 12; 626 exact controls pass; full target remains unproved here", "agent": "w433", "row": "S1.w433.8", "evidence": str(ROOT / "REVIEW_PACKET.md"), "state": "prepared locally for reviewer posting under folder-only write restriction"}
(ROOT / "PROGRESS_EVENT.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "BRAIN_DELIVERY_STATUS.json").write_text(json.dumps({"prepared": True, "submitted": False, "reviewed": False, "ingested": False, "retrievable": False, "draft_entries": len(entries), "draft_relations": len(relations), "claim_id": "clm-619fd2ede2", "notes": "Submission alone is not review or ingestion. All entries are concepts; no unreviewed theorem promotion."}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"prepared_entries": len(entries), "prepared_relations": len(relations), "local_draft": str(draft_dir / "bundle_001.json"), "hook_characters": len(hook["text"])}))
