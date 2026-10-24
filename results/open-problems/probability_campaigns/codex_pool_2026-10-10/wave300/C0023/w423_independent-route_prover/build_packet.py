"""Prepare and validate local review artifacts without integrating anything."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
measured = json.loads((ROOT / "measurements.json").read_text(encoding="utf-8"))
assert measured["status"] == "PASS"
assert measured["correct_identity_checks"] == 40
assert measured["correct_identity_failures"] == 0
now = datetime.now(timezone.utc).isoformat()


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


target = (ROOT / "STATEMENT.md").read_text(encoding="utf-8").split("Historical exact record:")[0].strip()
gap = "Under theta_d(p_c)>0, derive lattice-specific control of bridge creation over a fixed nonzero interval below p_c, sufficient to keep the integrated conditional pivotal load bounded along some scales. For a separate quenched formulation, derive genuine q<1 survival of a hypothetical critical cluster on a set of configurations of positive probability. Neither result is established here."
attempt = f"""{target}

Current openness on 2026-10-10 is UNKNOWN. The primary historical statement is verified in Duminil-Copin, Sixty years of percolation, arXiv:1712.04651, definitions pp.1-2 and Conjecture 1 p.3. A bounded current search did not verify the secondary 2026 formal-proof claim. No novelty claim or resolution claim is made.

The exact prior attempt C0023-A001 bootstrapped Barsky-Grimmett-Newman's half-space result using finite energy and uniqueness. Its own gaps are infinite half-space susceptibility and gluing across a hyperplane; I do not reuse these as proved inputs. The exact target/dedup-key checks in the named H/I and lean folders found the historical attempted_un label, not a proof receipt. Existing Team O's board did not name C0023. The export's matching card remains an unverified half-space concept. These are bounded searches, not statements that no other local work exists.

Independent route fixed in the initial ATTEMPT.md before reading any peer proof: reverse thinning, finite-volume connectivity witnesses and exact conditional bridge counts. No peer proposed proof has been read. The statement was delivered first to adversary w424 as msg-4fe478d188. Referee w425 receives this complete packet after the checks.

Assume theta_d(p_c)>0 and expose finite origin-to-boundary connection events A_n. L1 gives the exact logarithmic loss under lowering p: integral lambda_n(s)/s ds. L2 shows a bounded loss on one fixed interval would retain a positive one-arm limit below criticality, contradicting the definition of p_c. This is only an analytic reduction until one derives the geometric estimate. It is not a proof mechanism on its own.

The attempted shortcut was to estimate the number of bridges at p_c, then use that endpoint estimate to bound all subsequent damage from thinning. L3 refutes this shortcut in a broader graph class: its explicit series of parallel-path blocks has p_c=1/2, positive critical percolation, a unique infinite critical cluster almost surely, and bounded conditional exponential moments of all orders for its open pivotal counts at p_c. Its integrated loss on every fixed interval below p_c still diverges. Thus even strong endpoint information cannot simply be integrated below the endpoint.

On Z^d, finite energy supplies a positive probability of a specified finite detour, but does not by itself give a uniform detour-length or conditional-independence bound along infinitely many possible bottlenecks. Conditioning on a connection or on an infinite cluster couples the regions; no conditional per-region probabilities are multiplied here. The multiplication in L3 is justified by disjoint block edge sets, and after conditioning by the factorized event that each individual block crosses.

L4 strengthens the geometric formulation: a hypothetical infinite critical lattice cluster must have quenched thinning threshold 1. The retained annealed law is Bernoulli(p_c q), and the simultaneous conditional statement follows by Fubini, countably many rational q and monotonicity. To finish this route one would need a resilience theorem using the actual lattice iid geometry, not just existence, uniqueness, or endpoint pivotal moments.

Single hardest remaining gap: {gap}

The finite identities passed {measured['correct_identity_checks']} exact checks on {measured['unique_configurations']} configurations. The two-stage retention law passed {measured['thinning_law_checks']} checks over {measured['thinning_joint_configurations']} joint configurations. A deliberately wrong normalization omitting p failed {measured['naive_missing_p_identity_failures']}/40 checks. These validate finite calculations and detect a normalization error; they do not certify the infinite-volume target.

Formal proof status: no Lean/Mathlib theorem or kernel receipt is claimed. L1-L4 have author-written full proofs in LEMMAS.md and await w425's independent mathematical verdict. The draft brain entries remain concepts with proof_text null. Submitted, reviewed, ingested and retrievable are tracked separately in SUBMISSION_STATUS.json.

NEXT: Check whether critical-cluster detour geometry controls new bridges created by thinning for every s in one fixed interval [p_c-delta,p_c]; endpoint estimates alone cannot supply this.
"""
(ROOT / "ATTEMPT.md").write_text(attempt, encoding="utf-8")

definitions = [
    ("pivotal-cost", "finite-event-conditional-open-pivotal-logarithmic-derivative", "Conditional open pivotal count gives the exact finite-event probability loss", "DRAFT AUTHOR RESULT, pending w425. For a nonempty increasing event A on finitely many independent Bernoulli(p) edges, f(p)=P_p(A)>0 and N_A counts open pivotal edges. Then lambda_A(p)=E_p[N_A|A]=p f'(p)/f(p), and f(a)/f(b)=exp(-integral_a^b lambda_A(s)/s ds) for 0<a<b<1. No independence between different pivotal indicators is assumed.", ["finite edge set", "increasing event A", "positive event probability", "0<a<b<1"], "L1"),
    ("interval-criterion", "critical-lattice-one-arm-backward-interval-pivotal-cost-criterion", "A bounded integrated pivotal cost would contradict positive critical percolation", "DRAFT CONDITIONAL RESULT, pending w425. On nearest-neighbour iid bond percolation on Z^d with 0<p_c<1, let A_n be the event that 0 connects to the vertex boundary of [-n,n]^d using edges inside it, and lambda_n(s) the conditional mean open pivotal count given A_n. If theta(p_c)>0 and some fixed 0<a<p_c has liminf_n integral_a^{p_c} lambda_n(s)/s ds finite, then theta(a)>0, contradicting a<p_c. The integrated bound is an unproved additional hypothesis. This is an analytic reduction, not a proof of critical nonpercolation.", ["nearest-neighbour independent bond law", "0<a<p_c<1", "theta(p_c)>0", "liminf integrated conditional pivotal load finite"], "L2"),
    ("endpoint-counterexample", "locally-finite-critical-jump-despite-all-endpoint-pivotal-moments", "A critical jump can coexist with bounded endpoint pivotal exponential moments", "DRAFT AUTHOR COUNTEREXAMPLE, pending w425. Let Gamma have terminals a_0,a_1,..., joining a_{n-1} to a_n by n^2 2^{n+1} internally disjoint length-(n+1) paths, with all internal vertices distinct across paths and blocks. Independent Bernoulli bond percolation has p_c=1/2 and theta_Gamma(1/2)>3/5. For A_N={a_0 connects to a_N}, for every fixed t>=0 the conditional exponential moment E_{1/2}[exp(t N_{A_N})|A_N] is bounded uniformly in N; the conditional mean is less than 3. Yet for every 0<a<1/2 its integrated conditional pivotal cost from a to 1/2 tends to infinity. There is almost surely one infinite critical cluster. Gamma is simple and locally finite but has unbounded degrees and is not transitive, so it is not a counterexample to the Z^d target.", ["explicit graph Gamma", "independent bonds", "terminal connection event A_N", "fixed moment parameter t>=0"], "L3"),
    ("endpoint-shortcut", "refuted-endpoint-pivotal-control-to-backward-critical-continuity-route", "Refuted route: endpoint pivotal control alone implies backward continuity", "REFUTED ROUTE, author-checked and pending w425: the proposed inference from uniformly bounded conditional pivotal moments at p_c to bounded pivotal cost on one fixed interval below p_c is false on general locally finite graphs. Even all conditional exponential moments at the endpoint and uniqueness of the infinite critical cluster do not suffice. The explicit chain of parallel-path blocks provides the obstruction. Whether Z^d geometry supplies the missing interval estimate is not settled by this refutation.", ["general locally finite graphs", "claim uses endpoint information only", "lattice-specific hypotheses must be handled separately"], "L3"),
    ("quenched-fragility", "hypothetical-critical-lattice-cluster-quenched-thinning-threshold-one", "Any hypothetical infinite critical lattice cluster has thinning threshold one", "DRAFT AUTHOR RESULT, pending w425. For almost every Bernoulli(p_c) nearest-neighbour bond configuration Omega on Z^d with 0<p_c<1, independent retention of its open edges with any q<1 yields no infinite component almost surely conditional on Omega. Thus every hypothetical infinite component of Omega has quenched bond-percolation threshold 1. This statement does not assert that an infinite critical component exists. The simultaneous almost-everywhere statement uses the annealed Bernoulli(p_c q) law, Fubini, rational q and monotonicity.", ["countable lattice", "independent original Bernoulli bonds", "independent retention conditional on Omega", "0<p_c<1"], "L4"),
    ("resilience-gap", "critical-lattice-reverse-thinning-geometric-resilience-gap", "Unproved geometric resilience step for the independent C0023 route", "OPEN PROOF STEP, not a theorem: under the hypothetical theta_d(p_c)>0 on nearest-neighbour iid Z^d bond percolation, derive lattice-specific control of bridge creation over a fixed nonzero interval below p_c. Sufficient analytic form: an integrable uniform bound for lambda_n(s)/s on [p_c-delta,p_c], with 0<delta<p_c. Alternative quenched form: prove a hypothetical infinite critical cluster retains percolation for some q<1 on a set of original configurations of positive probability. The exact loss identity and quenched-fragility lemma explain how either estimate would yield a contradiction; neither estimate is established here. Finite-volume continuity, uniqueness and endpoint moment bounds alone leave this step open.", ["hypothetical positive critical order parameter", "exact iid Z^d bond geometry", "a fixed parameter interval, not scale-dependent deltas"], "Hardest remaining gap"),
]
entries = []
for key, logical, title, statement, assumptions, locator in definitions:
    entries.append({
        "key": key,
        "namespace": "probability.percolation",
        "logical_name": logical,
        "kind": "concept",
        "title": title,
        "statement": statement,
        "proof_text": None,
        "assumptions": assumptions,
        "domain": "probability theory",
        "source": {
            "source_id": "owner:w423:C0023-reverse-thinning:" + key,
            "url": (ROOT / "LEMMAS.md").as_uri(),
            "revision": "2026-10-10-author-checked-independent-review-pending:" + locator,
            "license": "owner-own-work (campaign auxiliary proof or refuted route; independent review pending)",
            "excerpt": None,
        },
    })
relations = [
    {"from_key": "interval-criterion", "to_key": "pivotal-cost", "kind": "depends_on", "rationale": "The end stating 'liminf_n integral_a^{p_c}' uses the end stating 'f(a)/f(b)=exp(-integral_a^b' to pass a positive finite probability to the one-arm limit. Supporting proof: L2 applies L1."},
    {"from_key": "endpoint-counterexample", "to_key": "endpoint-shortcut", "kind": "refutes", "rationale": "The counterexample end has 'conditional mean is less than 3' and interval cost 'tends to infinity'; the route end rejects the inference from endpoint moments to interval cost. Supporting proof: L3, disjoint-block reliability and moment formulas."},
    {"from_key": "resilience-gap", "to_key": "interval-criterion", "kind": "depends_on", "rationale": "The gap's 'integrable uniform bound' is a sufficient hypothesis for the criterion's bounded 'liminf_n integral_a^{p_c}'. This relation records a proposed route, not a proved geometric bound."},
    {"from_key": "resilience-gap", "to_key": "quenched-fragility", "kind": "depends_on", "rationale": "The gap asks for retention 'for some q<1' on a positive-measure set; the fragility end gives 'no infinite component' for every q<1. If the unproved resilience step were established, L4 would supply the contradiction."},
    {"from_key": "endpoint-counterexample", "to_key": "pivotal-cost", "kind": "depends_on", "rationale": "The counterexample's integrated cost divergence follows from the exact finite-event probability loss identity and its positive critical/product-zero subcritical limits. Supporting proof: L3 invokes L1 on A_N."},
    {"from_key": "quenched-fragility", "to_key": "interval-criterion", "kind": "semantic_association", "rationale": "Both ends concern retaining a positive connection probability below a hypothetical positive critical phase: one by conditional thinning, the other by integrated finite-event pivotal cost. No equivalence of their hypotheses is asserted."},
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w423", "bundle_slug": "c0023-reverse-thinning-bridge-obstruction-w423-001", "entries": entries, "relations": relations}
write_json("bundle_001.json", bundle)

keys = {e["key"] for e in entries}
assert len(keys) == len(entries) <= 200
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for e in entries:
    assert required <= e.keys()
    assert e["kind"] == "concept" and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", e["logical_name"])
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
dependency_graph = {k: [] for k in keys}
for r in relations:
    assert r["from_key"] in keys and r["to_key"] in keys
    assert r["kind"] in allowed and r["rationale"]
    if r["kind"] == "depends_on":
        dependency_graph[r["from_key"]].append(r["to_key"])
visited, visiting = set(), set()


def visit(k):
    assert k not in visiting, "cyclic depends_on relation"
    if k not in visited:
        visiting.add(k)
        for nxt in dependency_graph[k]:
            visit(nxt)
        visiting.remove(k)
        visited.add(k)


for k in keys:
    visit(k)
write_json("BUNDLE_VALIDATION.json", {"at": now, "status": "PASS", "command": "python -X utf8 ~/brain_workers/w423/build_packet.py", "entries": len(entries), "relations": len(relations), "unreviewed_theorem_or_lemma_entries": 0, "dangling_relation_ends": 0, "depends_on_cycles": 0, "nonallowlisted_licenses": 0, "live_integrator_run": False, "mathematical_review": "pending w425; local schema checks do not constitute proof"})

hook = {
    "id": "C0023-endpoint-bridge-w423-01",
    "area": "math",
    "event": "PreToolUse",
    "cue": r"(?is)(?:critical(?:ity)?|p_c).{0,160}(?:pivotal|bridge|exponential moment).{0,160}(?:thin|continu|lower)",
    "fire_when": "At critical p_c, bounded conditional pivotal exponential moments imply thinning keeps an infinite cluster for every scale.",
    "silent_when": "Use log f(b)-log f(a)=integral_a^b lambda(s)/s ds with an established integrable uniform bound throughout the interval.",
    "text": "Endpoint bridge bounds do not control an interval below p_c. Ask for a uniform integrable bound on [p_c-delta,p_c]. The L3 graph has positive critical percolation and all endpoint pivotal exponential moments bounded, yet every backward interval loses percolation.",
    "evidence": "~/brain_workers/w423/LEMMAS.md L3; CLAIMS.jsonl w423.S1.3; measurements.json exact bounds theta>0.6, mean<3, below-critical arm<10^-40",
    "proposer": "w423",
}
assert len(hook["text"]) <= 300
assert re.search(hook["cue"], hook["fire_when"])
assert not re.search(hook["cue"], hook["silent_when"])
(ROOT / "hook_proposals").mkdir(exist_ok=True)
hook_line = json.dumps(hook, ensure_ascii=False) + "\n"
(ROOT / "hook_proposals" / "math-w423.jsonl").write_text(hook_line, encoding="utf-8")
(ROOT / "patches").mkdir(exist_ok=True)
live = "~/primary_directive/hooks1000/proposals/math-w423.jsonl"
(ROOT / "patches" / "01_endpoint_bridge_hook.diff").write_text("--- a/" + live + "\n+++ b/" + live + "\n@@ -0,0 +1 @@\n+" + hook_line, encoding="utf-8")
write_json("HOOK_VALIDATION.json", {"at": now, "status": "PASS", "fire_controls": 1, "silent_controls": 1, "text_characters": len(hook["text"]), "global_proposal_submitted": False, "global_target": live})

lemmas = (ROOT / "LEMMAS.md").read_text(encoding="utf-8")
packet = f"""w423 C0023 review packet; referee w425; created {now}.

Review scope: L1 exact conditional-pivotal identity; L2 conditional backward-interval reduction; L3 explicit general-graph counterexample including uniqueness and all endpoint exponential moments; L4 simultaneous quenched-thinning statement. All four are author-written proofs awaiting independent verdicts. None resolves C0023. Current openness UNKNOWN, no novelty claim. Any new mathematical result invented by referee w425 needs the named independent referee w428; no child agents are requested or started.

{attempt}

Full author proof text follows so this packet is self-contained.

{lemmas}

Verification command: {measured['command']}. Exact identities: {measured['correct_identity_checks']} pass, {measured['correct_identity_failures']} fail; deliberately missing-p formula: {measured['naive_missing_p_identity_failures']} fail. {measured['unique_configurations']} distinct configurations, {measured['thinning_joint_configurations']} joint thinning configurations. Critical lower bound numerical display {measured['critical_connection_lower_bound']['numerical_display']}, exact comparison >3/5; endpoint bridge upper bound numerical display {measured['critical_conditional_bridge_upper_bound']['numerical_display']}, exact comparison <3. At p=0.4 block 500 connection upper bound is exactly certified below 10^-40. All infinite-volume assertions depend on the written analytic proof, not enumeration.

Please give an independent KEEP/FIX/DROP verdict for each L1-L4, with attention to L3's disjoint-block conditioning and infinite-tail uniqueness, L4's countable rational parameters, and the absent geometric interval estimate. Do not mark the C0023 target proved because auxiliary lemmas or source checks pass.

Brain deliverable: bundle_001.json has six concept/draft entries and six relations; no theorem/lemma promotion. SOURCE_STATUS.json, CLAIMS.jsonl, measurements.json and BUNDLE_VALIDATION.json are beside this packet. SUBMISSION_STATUS.json separately tracks submission, mathematical review, ingestion and actual retrieval. No live integrator or recall-control edit is authorized or performed.

NEXT: Independently check the L3 bridge moment and loss estimates, then assess the proposed uniform bridge-creation bound on a fixed interval below p_c.
"""
(ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")

report = f"""C0023 is not proved by this attempt; current openness remains UNKNOWN. I recovered its exact nearest-neighbour iid bond model and historical primary statement, and fixed a reverse-thinning route before reading any peer proof. The prior recorded route used half-space gluing.

The useful change is one audit guardrail: endpoint pivotal control cannot justify a fixed decrease of p. L3 gives a fully specified locally finite graph with a positive critical order parameter, a unique infinite critical cluster, and bounded conditional pivotal exponential moments of every order at the endpoint. Its connection probability nevertheless vanishes below criticality. L1, L2 and L4 provide the exact loss identity and the conditional lattice reductions; the absent geometric resilience estimate is named explicitly.

Run: {measured['command']}. The deliberately incorrect normalization failed 40/40 finite checks; the exact identity passed 40/40, on 544 configurations. Eight thinning-law checks covered 10,098 joint configurations. Exact rational bounds give theta(p_c)>0.6, endpoint conditional mean <3, and a connection probability at p=0.4 below 10^-40 at block 500. Run cost: {measured['cpu_seconds']} CPU seconds, {measured['peak_traced_python_bytes']} traced Python bytes. These measure local checks, not a deployed recall gain or a solution of the target.

The counterexample's degrees are unbounded and it is not transitive, so it cannot refute the Z^d conjecture. The four full author proofs in REVIEW_PACKET.md still need w425's mathematical review. The six brain entries remain concepts, with license owner-own-work and proof_text null. Submission, review, ingestion and retrieval have separate state fields. No store writes or live integrator run occurred.

Apply: the reviewer adds the single hook line represented by patches/01_endpoint_bridge_hook.diff to ~/primary_directive/hooks1000/proposals/math-w423.jsonl; the diff headers name that live path. Its fire/silent controls pass locally. Global hook and progress-page writes are staged locally under the worker-folder restriction. The supplied PROGRESS_EVENT.json contains the prescribed post command. The validating coordinator may integrate the accepted draft after review; the bundle spec's automatic integrator command was not run because this task reserves live integration to that coordinator.

NEXT: w425 checks L3's uniform moment proof and L4's simultaneous-q proof; the next mathematical step is a lattice-specific bound on bridges created by thinning over one fixed interval below p_c.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
write_json("PROGRESS_EVENT.json", {"event": "w423 C0023: four auxiliary author proofs saved; exact checks 40/40 pass; endpoint-control counterexample; lattice interval gap remains", "agent": "w423", "row": "w423.S1.3", "evidence": str(ROOT / "REVIEW_PACKET.md"), "global_page_posted": False, "command_for_reviewer": 'python -X utf8 ~/primary_directive/pd_progress.py --event "w423 C0023: four auxiliary proofs, exact checks 40/40, endpoint-control counterexample; lattice gap remains" --agent w423 --row w423.S1.3 --evidence ~/brain_workers/w423/REVIEW_PACKET.md'})
write_json("SUBMISSION_STATUS.json", {"prepared": {"status": True, "at": now}, "local_schema_validated": {"status": True, "at": now}, "submitted": {"status": False, "path": None}, "reviewed": {"status": False, "reviewer": "w425", "verdict": None}, "ingested": {"status": False, "coordinator_receipt": None}, "retrievable": {"status": False, "recall_receipt": None}, "mathematical_target_resolved": False})

claims = [json.loads(s) for s in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
for c in claims:
    if c.get("id") in {"w423.S1.1", "w423.S1.2", "w423.S1.3"}:
        c["source"]["kind"] = "owner-own-work"
new_claims = [
    {"id": "w423.S1.5", "candidate": "C0023", "statement": "Forty exact conditional-pivotal identities and eight exact thinning laws pass on the bounded verification corpus; the missing-p normalization fails forty of forty checks. The L3 analytic bound comparisons are theta(1/2)>3/5, lambda_N(1/2)<3 uniformly in N, and f_500(0.4)<10^-40.", "assumptions": ["eight specified finite graphs, at most eight edges", "five rational Bernoulli parameters", "retention pair b=3/4, a=3/8", "L3 graph for analytic bound comparisons"], "source": {"kind": "local exact calculation", "command": measured["command"], "file": "measurements.json"}, "proof_or_counterexample": "Fraction arithmetic exhausts configurations and uses exact Taylor interval bounds for displayed exponential comparisons; full infinite-volume arguments are separate in LEMMAS.md.", "independent_reviewer": "w425 (pending)", "remaining_gap": "Finite checks do not establish the lattice geometric estimate or independently certify C0023.", "status": "numerical evidence"},
    {"id": "w423.S1.6", "candidate": "C0023", "statement": "Exact recovered target: for iid nearest-neighbour Bernoulli bond percolation on Z^d, integer 3<=d<=10, theta_d(p_c(d))=0, with theta_d(p)=P_p(|C(0)|=infinity) and p_c(d)=inf{p:theta_d(p)>0}.", "assumptions": ["full lattice", "iid nearest-neighbour bonds", "3<=d<=10"], "source": {"kind": "primary historical statement", "url": "https://arxiv.org/pdf/1712.04651", "locator": "definitions pp.1-2; Conjecture 1 p.3", "source_status_file": "SOURCE_STATUS.json"}, "proof_or_counterexample": "This corrects the provisional model-scope row w423.S1.0; it is a target statement, not a proof.", "independent_reviewer": "w425 (pending)", "remaining_gap": gap, "status": "conjecture", "current_openness": "UNKNOWN"},
]
by_id = {c["id"]: c for c in claims}
for c in new_claims:
    by_id[c["id"]] = c
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in by_id.values()), encoding="utf-8")
(ROOT / "STATUS.md").write_text("STATE: WORKING\nNEXT: Claim the narrow mesh resource, submit the validated concept bundle atomically, and deliver REVIEW_PACKET.md to w425.\n\n2026-10-10: Exact C0023 bond statement and prior half-space attempt recovered. Statement delivered first to w424 (msg-4fe478d188). L1-L4 author proofs and the single geometric interval gap saved.\n2026-10-10: Exact finite checks PASS (40 identities, 544 configurations, 10,098 joint thinning configurations). Six-entry concept draft and six supported relations pass local schema checks; hook fire/silent controls pass. No peer proof read; no live store write or integrator run.\n", encoding="utf-8")
print(json.dumps({"status": "PREPARED", "claims": len(by_id), "draft_entries": len(entries), "draft_relations": len(relations), "proof_packet": str(ROOT / "REVIEW_PACKET.md"), "live_integrator_run": False}, indent=2))
