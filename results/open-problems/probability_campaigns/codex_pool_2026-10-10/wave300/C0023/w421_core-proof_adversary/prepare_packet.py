"""Prepare review material and, if requested, publish only this worker's DRAFT file."""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import sqlite3

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w421")
parser = argparse.ArgumentParser()
parser.add_argument("--publish", action="store_true")
args = parser.parse_args()
now = datetime.now(timezone.utc).isoformat()
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len({row["claim_id"] for row in claims}) == len(claims)
for row in claims:
    for required in ("statement", "assumptions", "source", "proof", "independent_reviewer", "remaining_gap", "status"):
        assert required in row, (row["claim_id"], required)

store_check = {"path": "~/math-brain-build/local/population/brain.sqlite3",
               "mode": "ro", "scope": "exact target titles only, at most five nodes; not a solved/retired certification"}
store_connection = None
try:
    store_connection = sqlite3.connect("file:" + store_check["path"] + "?mode=ro", uri=True, timeout=0.25)
    titles = ("No percolation at criticality on Z^d for 3 <= d <= 10", "No percolation at criticality on Z^d",
              "No infinite cluster at criticality on Z^d", "Critical percolation on Z^d")
    rows = store_connection.execute(
        "SELECT id,kind,title,substr(body,1,2000) FROM nodes WHERE title IN (?,?,?,?) LIMIT 5", titles
    ).fetchall()
    store_check["exact_title_hits"] = len(rows)
    store_check["rows"] = [dict(zip(("id", "kind", "title", "body_prefix"), row)) for row in rows]
except (OSError, sqlite3.Error) as exc:
    store_check["error"] = type(exc).__name__ + ": " + str(exc)
finally:
    if store_connection is not None:
        store_connection.close()
(ROOT / "SOURCE_STORE_REPORT.md").write_text(json.dumps(store_check, ensure_ascii=False, indent=2), encoding="utf-8")

def entry(key, name, title, statement, assumptions, claim_id, report):
    return {"key": key, "namespace": "probability.percolation", "logical_name": name,
            "kind": "concept", "title": title,
            "statement": "DRAFT proof-audit material, independent referee check pending. " + statement,
            "proof_text": None, "assumptions": assumptions, "domain": "probability theory",
            "source": {"source_id": "owner-own-work:w421:" + claim_id,
                       "url": None, "revision": "2026-10-10-draft", "license": "owner-own-work",
                       "excerpt": None},
            "notes": "Full candidate proof and its gaps are retained in " + str(ROOT / report)}

entries = [
    entry("finite-range-countermodel", "finite-dependent-high-density-finite-components",
          "High density with a growing dependence range need not percolate",
          "For every integer d>=1 and epsilon>0 there exists a stationary finite-dependent {0,1} field on Z^d "
          "with probability of good at each vertex at least 1-epsilon and all nearest-neighbour good components finite. "
          "Construct it from iid Bernoulli(q) seeds. L(v) is a nearest seed in the l-infinity ball B_R(v), with "
          "lexicographic tie-breaking, or bottom if the ball is empty. A vertex is good exactly when its non-bottom "
          "label agrees with every nearest neighbour's label. Its indicator uses seeds in B_(R+1)(v), so index "
          "sets at l-infinity distance greater than 2(R+1) are independent. Each good component has one seed "
          "label s and lies in B_R(s). For a finite dimension-dependent constant K_d, P(v bad)<=exp(-q(2R-1)^d) "
          "+K_d q^(1/d); choosing q small then R large gives the claimed density. The dependence range varies "
          "with epsilon. This is correlated site percolation and does not refute iid critical bond percolation "
          "or a fixed-range domination theorem.",
          ["d is an integer>=1", "iid seeds with 0<q<1", "R is an integer>=1", "Good connectivity is nearest-neighbour"],
          "C0023-w421-004", "FINITE_DEPENDENCE_OBSTRUCTION.md"),
    entry("uniform-critical-limit", "critical-one-arm-uniform-pivotal-integral-gap",
          "Critical nonpercolation requires uniform control of the parameter limit",
          "For iid nearest-neighbour bond percolation on Z^d with p_c>0, let a_n(p) be the probability of an open "
          "path from 0 to the vertex boundary of B_n=[-n,n]^d intersect Z^d, using edges internal to B_n. Let I_n(p) "
          "be the sum of the pivotal probabilities of those edges for that event. Then theta(p)=lim_n a_n(p). "
          "The assertion theta(p_c)=0 is equivalent to lim_(delta down to 0) sup_n integral_(p_c-delta)^(p_c) I_n(p)dp=0, "
          "where 0<delta<p_c. Finite-product differentiation identifies the integral with a_n(p_c)-a_n(p_c-delta). "
          "This is an equivalence identifying the open input, not a proof of the required uniform estimate "
          "in dimensions 3 through 10; continuity of each finite-event polynomial is insufficient.",
          ["Independent Bernoulli(p) nearest-neighbour bonds", "p_c>0", "theta(p)=0 for p<p_c"],
          "C0023-w421-005", "UNIFORM_LIMIT_CRITERION.md"),
    entry("positive-peierls-threshold", "finite-dependent-planar-peierls-positive-threshold-101",
          "A Peierls sufficient condition for positive block percolation",
          "Let X_z be a {0,1} site field on Z^2. Assume strong rho-dependence in l-infinity distance: sigma-fields "
          "generated by any two index sets separated by distance greater than the integer rho>=0 are independent. "
          "Suppose P(X_z=0)<=q for every z and set K=(rho+1)^2. If q<=101^(-K), then the probability that 0 belongs "
          "to an infinite nearest-neighbour component of good sites is at least 378252/81240057>0. "
          "Residue coloring and enclosing bad star-contours give the bound 1-q-9t(1+t)/(1-t)^3 with t=8q^(1/K). "
          "At q<=101^(-K), q<=1/101 and t<=8/101 give the stated positive value. This uses independence of "
          "separated sets, not mere pairwise independence. It weakens the base-800 sufficient error requirement "
          "when only positivity is needed. It supplies no estimate achieving that error for critical lattice blocks.",
          ["Strong rho-dependence of separated index SETS", "rho is an integer>=0", "q<=101^(-(rho+1)^2)",
           "Good paths use nearest-neighbour adjacency and bad contours use star adjacency"],
          "C0023-w421-006", "AUDIT_W420.md"),
    entry("selector-conditioning", "first-reached-selection-invalidates-pointwise-fkg-bound",
          "First-reached conditioning can lower a connection probability",
          "On the path o--a2--b--a1 with three independent Bernoulli(1/2) bonds, order A=(a1,a2). "
          "Let F2 mean that a2 is the first member of A connected to o in this order. Then P(F2)=3/8 and "
          "P(F2 and a2 connects to b)=1/8, so P(a2 connects to b | F2)=1/3, whereas "
          "min_(a in A)P(a connects to b)=1/2. The first-reached event contains a decreasing exclusion, "
          "so FKG does not justify the pointwise conditional lower bound. The Kozma--Nitzan global inequality "
          "P(o connects to b)>=P(o connects to A)min_(a in A)P(a connects to b) is nevertheless an equality here "
          "(both sides 1/4). This refutes the conditional proof premise, not the global conjecture.",
          ["Undirected four-vertex path", "Independent bonds with p=1/2", "First means first in the fixed order of A"],
          "C0023-w421-003", "INDEPENDENT_SELECTOR_OBSTRUCTION.md"),
]
# Keep the strict spec shape: evidence lives in the source report and review packet.
for node in entries:
    node.pop("notes")
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w421",
          "bundle_slug": "critical-percolation-obstructions-w421-001", "entries": entries,
          "relations": [
              {"from_key": "finite-range-countermodel", "to_key": "positive-peierls-threshold",
               "kind": "semantic_association",
               "rationale": "The countermodel's statement says 'The dependence range varies with epsilon'; the Peierls "
                            "statement sets 'K=(rho+1)^2' and requires 'q<=101^(-K)'. Together they distinguish "
                            "high density alone from a sufficient error bound for the same dependence range."},
              {"from_key": "finite-range-countermodel", "to_key": "uniform-critical-limit", "kind": "analogous_to",
               "rationale": "The countermodel varies its range with epsilon; the one-arm criterion explicitly needs "
                            "a supremum over all n before delta tends to zero. Both expose a missing uniform estimate. "
                            "Their model classes differ and neither implication between their parent problems is claimed."}
          ]}
keys = {node["key"] for node in entries}
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for node in entries:
    assert node["kind"] == "concept" and node["proof_text"] is None
    assert node["source"]["license"].startswith("owner-own-work")
for edge in bundle["relations"]:
    assert edge["from_key"] in keys and edge["to_key"] in keys and edge["kind"] in allowed
payload = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
draft = ROOT / "DRAFT_bundle_001.json"
draft.write_text(payload, encoding="utf-8")
submitted_path = None
if args.publish:
    INBOX.mkdir(parents=True, exist_ok=True)
    for number in range(1, 1000):
        final = INBOX / f"bundle_{number:03d}.json"
        partial = INBOX / f"bundle_{number:03d}.part"
        if final.exists() and final.read_text(encoding="utf-8") == payload:
            submitted_path = final
            break
        if final.exists() or partial.exists():
            continue
        assert final.resolve().parent == INBOX.resolve()
        with partial.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
        assert not final.exists()
        partial.rename(final)
        submitted_path = final
        break
    assert submitted_path is not None

hook = {"id": "c0023-w421-dependence-range-01", "area": "math", "event": "stage-start",
        "cue": "A percolation block proof closes from vanishing failure after enlarging an interaction radius, without a threshold for that radius",
        "fire_when": "Infer percolation from q(L,M) tending to zero with an uncontrolled M/L and dependence range",
        "silent_when": "A fixed dependence range or a proved error bound below its percolating threshold is supplied; or the mismatch is explicitly left open",
        "text": "When enlarging a block reduces its failure, compute the dependence range too. A vanishing error with growing range does not by itself give percolation. Record an explicit bound matching error to that same range.",
        "evidence": "~/brain_workers/w421/FINITE_DEPENDENCE_OBSTRUCTION.md, C0023-w421-004 (referee pending); conditioning scar proof_steps_need_derived_joint_structure_2026_09_09",
        "proposer": "w421"}
assert len(hook["text"]) <= 300
hook_line = json.dumps(hook, ensure_ascii=False) + "\n"
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hook_line, encoding="utf-8")
live_hook = Path("~/primary_directive/hooks1000/proposals/math-w421.jsonl")
old_hook = live_hook.read_text(encoding="utf-8") if live_hook.exists() else ""
new_hook = old_hook + ("\n" if old_hook and not old_hook.endswith("\n") else "")
if hook["id"] not in old_hook:
    new_hook += hook_line
patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
diff = "".join(difflib.unified_diff(old_hook.splitlines(keepends=True), new_hook.splitlines(keepends=True),
    fromfile="a/primary_directive/hooks1000/proposals/math-w421.jsonl",
    tofile="b/primary_directive/hooks1000/proposals/math-w421.jsonl"))
(patches / "01_c0023_range_hook.diff").write_text(diff, encoding="utf-8")

source_status = {
    "candidate_id": "C0023", "worker": "w421", "checked_date": "2026-10-10",
    "exact_statement": "For every integer 3<=d<=10, take iid Bernoulli(p) states on unoriented nearest-neighbour bonds of Z^d. "
                       "Let theta_d(p)=P_p(|C(0)|=infinity) and p_c(d)=inf{p:theta_d(p)>0}. Prove theta_d(p_c(d))=0.",
    "exact_statement_status": "primary conventions and conjecture checked; intermediate-dimension scope recovered from dated intake",
    "current_openness": "UNKNOWN", "novelty_claim": False,
    "openness_reason": "A bounded primary-source search located the bond conjecture in 2024 and a site conjecture in Aug 2026. "
                       "No resolution was found, but neither this search nor the scoped owner-work checks certifies all current literature or retired work.",
    "served_model_settings": "UNVERIFIED. Requested gpt-6.1-sol, max, Fast are not response-side serving evidence.",
    "sources": [
        {"id": "C0023-intake", "path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl",
         "line": 23, "status": "historical attempted_unsolved, unreviewed; not a current openness certificate"},
        {"id": "duminil_copin_icm_2018", "url": "https://arxiv.org/pdf/1712.04651", "revision": "v1",
         "locator": "pp.1-3: independent nearest-neighbour bonds; Conjecture 1 p.3",
         "quote": "Show that theta(p_c) = 0 on Z^d for every d >= 3.",
         "quote_note": "Plain-text rendering of the displayed mathematical statement; primary PDF checked."},
        {"id": "kozma_nitzan_2024", "url": "https://arxiv.org/html/2401.12397v1", "revision": "v1",
         "locator": "Section 1, Conjecture 1 and finite-size discussion",
         "quote": "We were not able to prove or disprove this conjecture.",
         "scope": "bond percolation; arbitrary finite-graph connection inequality is conjectural"},
        {"id": "cerf_2026", "url": "https://arxiv.org/html/2608.23661v1", "revision": "v1",
         "locator": "Section 1, Conjecture 1.1",
         "scope": "SITE percolation; cannot silently serve as a bond theorem",
         "coverage_limit": "Experimental HTML includes only the introduction/references. The announced finite-cluster-tail theorem was not audited from that incomplete representation."},
        {"id": "fitzner_hofstad_2017", "url": "https://arxiv.org/abs/1506.07977v2", "revision": "v2",
         "scope": "abstract verifies nearest-neighbour mean-field threshold d>=11; full computer-assisted proof not re-audited"}
    ],
    "owner_prior_work": {
        "C0023_A001": "Half-space route explicitly leaves susceptibility and hyperplane gluing unproved; not a solved or retired receipt.",
        "H_I_and_lean_exact_ID_search": "No C0023 hit in the named H/I attempt directories; Lean annotated ranking repeats attempted_unsolved.",
        "G0001": "Targeted G intake row identifies Cerf's site-tail reformulation; its attempt labels it equivalent only modulo stated additional theorems, not a new solution.",
        "Team_O": "Read board; no C0023 row was listed. Probability300 board assigns C0023 to w420-w431.",
        "Big_Open_problem_folder": "Targeted search reached research/open_status.md, whose target is the different nonamenable p_c<p_u problem; it supplies no C0023 solution.",
        "population_store_check": store_check,
        "canonical_store_check": "Population schema and a narrow exact-title lookup were inspected read-only; no whole export was read. "
                                 "A complete canonical research solved/retired certification was unavailable in the scoped reads. UNKNOWN is preserved."
    },
    "recall": {"command": "python -X utf8 bounded_recall.py", "status": "TIMEOUT after 60 seconds (61.875 including cleanup)",
               "fallback": "Targeted MEMORY.md grep then the exact cited proof-gap and conditioning scars",
               "scars": ["perceptron_proof_open_gaps_fleet_2026_07_12", "proof_steps_need_derived_joint_structure_2026_09_09"]},
    "paired_proof_read": True, "independent_checkpoint_files": ["ATTEMPT.md", "INDEPENDENT_SELECTOR_OBSTRUCTION.md", "FINITE_DEPENDENCE_OBSTRUCTION.md"],
    "review": {"referee": "w422", "state": "pending", "referee_own_new_results_referee": "w425",
               "different_model_or_account_serving_evidence": "UNAVAILABLE; do not promote to an independently checked theorem"},
    "brain_states": {"prepared": True, "submitted": submitted_path is not None, "reviewed": False, "ingested": False, "retrievable": False},
    "draft_path": str(submitted_path) if submitted_path else str(draft), "updated_utc": now
}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source_status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8")) if (ROOT / "MEASUREMENTS.json").exists() else {"status": "NOT_RUN"}
check_summary = (f"Exact checker: {measurements.get('status')}; {measurements.get('checks_run', 0)} checks; "
                 f"elapsed {measurements.get('elapsed_seconds', 'unknown')} seconds. Command: python -X utf8 verify_obstructions.py.")
if measurements.get("status") == "PASS":
    check_summary += " Eight graph states give conditional 1/3 versus marginal 1/2 (gap -1/6), while the global inequality has margin 0. "
    check_summary += "650 shell-count checks cover dimensions 1-10 and radii 0-64. Exact rational constants give " + measurements["peierls"]["new_lower_bound"] + " > 0 at base 101."
else:
    check_summary += " The resource gate held numerical/exhaustive checks; the analytic proofs and exact rational statements remain submitted for independent review."
report = (
    "C0023 remains unproved. Current openness is UNKNOWN after a bounded source/owner-work check; no novelty claim is made.\n\n"
    "The main deliverable is a rigorous candidate countermodel: stationary finite-dependent fields can have arbitrarily high good density "
    "while every good component is finite. Its dependence range grows with density. This blocks a generic diagonal argument in critical "
    "percolation. A separate three-edge path refutes first-reached conditional FKG; it does not refute Kozma--Nitzan's global inequality.\n\n"
    "The scoped audit keeps w420's conditional L0-L5 route and preserves its open gap G. The same Peierls bound needs only positivity for "
    "the critical contradiction: the proposed sufficient error base is 101 rather than 800, a candidate factor (800/101)^K for K=(R+1)^2, "
    "with handwritten rational lower bound 378252/81240057. This refinement is unmeasured while the compute gate holds and awaits "
    "independent check. No critical block error attaining either threshold is proved.\n\n"
    + check_summary + "\n\n"
    f"Prepared {len(entries)} concept entries, {len(bundle['relations'])} scoped relations and {len(claims)} claim rows. "
    "Command: python -X utf8 prepare_packet.py --publish. Local structural validation is not store admission or mathematical certification.\n\n"
    + ("Draft submitted to " + str(submitted_path) + ". " if submitted_path else "Draft is prepared locally. ")
    + "Referee review, integration and recall retrieval are separately pending; no live store or recall-control change was made.\n\n"
    "Risks: the seed field is correlated and is not the iid target; strong dependence means independence of separated sets; site/bond "
    "models must not be conflated. The contour proof and seed shell bounds need the named referee's independent mathematical check. "
    "Serving model/account evidence is unavailable. No formal proof receipt is claimed.\n\n"
    "Apply: the validating coordinator reviews the concept-only DRAFT at the stated inbox path and integrates only after the required gates. "
    "The hook is a local proposal/diff because the worker's write scope forbids changing the shared hook file: reviewer may apply "
    "patches/01_c0023_range_hook.diff from ~ after its hook audit; it was not applied here.\n\n"
    "NEXT: w422 checks rows 004 and 006; the next proof step is a same-scale critical anchor estimate q_(p_c)(L,aL) tending to zero "
    "for a fixed aspect ratio a, or another justified dependence-matched certificate.\n"
)
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
packet_files = ("CLAIMS.jsonl", "FINITE_DEPENDENCE_OBSTRUCTION.md", "INDEPENDENT_SELECTOR_OBSTRUCTION.md",
                "UNIFORM_LIMIT_CRITERION.md", "AUDIT_W420.md", "ATTEMPT.md", "SOURCE_STATUS.json", "MEASUREMENTS.json")
hash_lines = []
for name in packet_files:
    path = ROOT / name
    if path.exists():
        hash_lines.append(name + "  sha256=" + hashlib.sha256(path.read_bytes()).hexdigest())
review_packet = (
    "C0023 w421 review packet, 2026-10-10. Native worker identity w421.\n\n"
    "Primary referee: w422. Referee for w422's own new results: w425. Integration contact from the team routing notice: codex-01a12190.\n\n"
    "Requested settings gpt-6.1-sol/max/Fast; served-model/account evidence UNKNOWN. These bytes/hashes identify artifacts, not theorem "
    "truth or trusted axioms. There is no formal-check receipt.\n\n"
    "Most important review: row 004's nearest-seed finite-dependence countermodel, especially shell pairing, tie translation and radius R+1. "
    "Then row 006's contour argument and base-101 rational lower bound. Rows 001/005 are elementary limit reductions; row 002 is a "
    "non-geometric product-event countermodel; row 003 is an eight-configuration conditional-selection obstruction. All new rows await "
    "independent mathematical check.\n\n"
    "Scoped KEEP: w420 L0-L5 are a conditional route with the stated assumptions and topology expansion in AUDIT_W420.md. UNRESOLVED: "
    "gap G, a critical error estimate matching the dependence range. The weaker 101 threshold still has no proved critical certificate.\n\n"
    "Supporting statement quote from w420: 'This is a proved two-scale limit under the stated assumption. It is not a rate estimate, "
    "a bounded-aspect-ratio limit, or a dependence-matched certificate.' The countermodel addresses exactly that missing uniformity; "
    "it does not contradict the conditional criterion.\n\n"
    + check_summary + "\n\nDRAFT: " + str(submitted_path or draft)
    + "\nStates: prepared; " + ("submitted; " if submitted_path else "not submitted; ")
    + "review pending; not ingested; not tested for recall retrieval. Hook proposal is local only.\n\n"
    + "\n".join(hash_lines) + "\n\nNEXT: independently check the two named rows and return scoped KEEP/FIX with the exact remaining critical input.\n"
)
(ROOT / "REVIEW_PACKET.md").write_text(review_packet, encoding="utf-8")
receipt = {"timestamp_utc": now, "claims": len(claims), "draft_entries": len(entries), "draft_relations": len(bundle["relations"]),
           "local_structural_validation": "PASS", "check_status": measurements.get("status"),
           "submitted_path": str(submitted_path) if submitted_path else None,
           "reviewed": False, "ingested": False, "retrievable": False}
(ROOT / "PACKET_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
