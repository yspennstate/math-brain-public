"""Bounded exact controls and local C0041 review/draft preparation.

No live store, integration, model loads, simulation, or service operations.
The only outside write is the specifically authorized author draft inbox.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parent
started = time.monotonic()
now = datetime.now(timezone.utc).isoformat()
gate = {"issued_at_utc": now, "purpose": "exact finite arithmetic and draft schema checks",
        "max_wall_seconds": 45, "max_arithmetic_checks": 200, "simulation": False,
        "gpu": False, "model_loads": False, "live_store_writes": False}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
counts = Counter()

def check(condition, group):
    if time.monotonic() - started > gate["max_wall_seconds"]:
        raise RuntimeError("fresh local exact-check time gate exceeded")
    assert condition, group
    counts[group] += 1
    assert sum(counts.values()) <= gate["max_arithmetic_checks"]

for q in (F(1, 4), F(1, 2), F(3, 4)):
    for k in range(17):
        direct = sum((F(2**j, 2**(j+1)) for j in range(k)), F(0)) + F(2**k, 2**k)
        closed = F(k, 2) + 1
        check(direct == closed and 1 + ((1-q)/q)*direct == 1 + ((1-q)/q)*closed,
              "truncated_heavy_cost")
for ip in range(5):
    for im in range(5-ip):
        pp, pm = F(ip, 4), F(im, 4)
        for n in (1, 3, 5):
            check((pp*pm)**n <= F(1, 4)**n, "opposed_row_rarity")
        for elambda in (1, 2, 4):
            a = elambda-1
            check((1+a*pp)*(1+a*pm) <= F(1+elambda, 2)**2,
                  "two_half_box_mgf")
matches = sum(1 for word in itertools.product((-1, 1), repeat=6)
              if all(v == 1 for v in word[:3]) and all(v == -1 for v in word[3:]))
check(F(matches, 64) == F(1, 64), "finite_box_pattern_enumeration")
selected = 1-F(63, 64)**64
check(selected > F(1, 2), "adaptive_selection_64_boxes")
# Two perfectly dependent costs; survival is measurable before the second trial.
dependent_cost = sum((F(1, 2)*(2*u + u*2*u) for u in (0, 1)), F(0))
check(dependent_cost == 2 and dependent_cost <= F(2)/(1-F(1, 2)),
      "dependent_cost_positive_control")

hook = {"id": "regeneration-cost-w445-01", "area": "math", "event": "stage-start",
        "cue": "A proof infers finite expected regeneration duration from a geometric attempt count without an integrable cost bound.",
        "fire_when": "The attempt count is geometric and each failed attempt ends almost surely, therefore the expected duration is finite.",
        "silent_when": "A uniform conditional expected cost bound and survival bound are proved under the same increasing filtration, then Tonelli is applied.",
        "text": "A geometric regeneration-attempt count controls count. State the conditional law and prove a summable cost or duration bound before inferring a finite mean.",
        "evidence": "CLAIMS.jsonl:C0041-cost-001; CHECK_RESULTS.json:truncated_heavy_cost; memory:proof_steps_need_derived_joint_structure_2026_09_09",
        "proposer": "w445"}
def hook_control(case):
    return case["geometric_count"] and case["finite_mean_inference"] and not case["integrable_cost_proved"]
fire = {"geometric_count": True, "finite_mean_inference": True, "integrable_cost_proved": False}
silent = {"geometric_count": True, "finite_mean_inference": True, "integrable_cost_proved": True}
assert len(hook["text"]) <= 300 and hook_control(fire) and not hook_control(silent)
hook_line = json.dumps(hook, ensure_ascii=False)
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(hook_line+"\n", encoding="utf-8")
(ROOT / "HOOK_CONTROLS.json").write_text(json.dumps({"fire": fire, "silent": silent,
    "passed": 2, "scope": "semantic controls for a proposal; no live hook implementation tested"}, indent=2), encoding="utf-8")
(ROOT / "patches").mkdir(exist_ok=True)
live = "~/primary_directive/hooks1000/proposals/regeneration-cost-w445.jsonl"
diff = f"--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+{hook_line}\n"
(ROOT / "patches/01_regeneration_cost_hook.diff").write_text(diff, encoding="utf-8")

peer = Path("~/brain_workers/w444/ATTEMPT.md")
raw_peer = peer.read_bytes()
peer_text = raw_peer.decode("utf-8-sig")
for anchor in ("## R1:", "## L1:", "## L2:", "### L2b:", "## L3:"):
    assert anchor in peer_text, f"peer statement moved: {anchor}"
(ROOT / "sources/w444_ATTEMPT_snapshot.md").write_bytes(raw_peer)
peer_hash = hashlib.sha256(raw_peer).hexdigest()
audit_reasons = {
    "R1": "SLLN plus the integrated tail bound and Borel-Cantelli control incomplete iid cycles once their durations have a finite mean.",
    "L1": "At every deterministic L-step boundary, a forced positive-coordinate exit has conditional probability at least kappa^L. Tower iteration, tail summation and a geometric moment comparison justify the constants.",
    "L2": "The opposite sign events are disjoint for delta>0. Distinct iid site rows give the exact product and the degree-d rarity exponent dominates the linear cost exponent for d>=2.",
    "L2b": "AM-GM controls the two half-box moment-generating factors when p_++p_-<=1; Chernoff applies for fixed theta>1/2. The endpoint theta=1 is a limit.",
    "L3": "Quenched strong Markov at H handles adaptive selection; a deterministic center union bound handles rarity; nonnegative conditioning costs at most 1/q. The same deterministic N must be retained."}
rows = [{"claim": k, "verdict": "KEEP", "scope": "exact displayed assumptions only",
         "why": v, "source": str(peer), "source_sha256": peer_hash,
         "auditor": "w445", "mathematical_derivation": "PAIRED_AUDIT.md",
         "different_model_gate": "UNKNOWN; no response-side served identity supplied"}
        for k, v in audit_reasons.items()]
rows.append({"claim": "C0041 full-target inference", "verdict": "NOT_ESTABLISHED",
             "why": "No quantitative classification of all regeneration delays or integrable accounting follows from R1/L1/L2/L2b/L3. The source itself states the gap.",
             "source": str(peer), "source_sha256": peer_hash, "auditor": "w445"})
(ROOT / "AUDIT_VERDICTS.jsonl").write_text("".join(json.dumps(r)+"\n" for r in rows), encoding="utf-8")

new_claims = [
 {"claim_id":"C0041-selection-001", "type":"counterexample", "statement":"Fixed-center inward-pattern rarity does not bound an unrestricted environment-measurable selected center.",
  "assumptions":["d>=2, kappa=1/(4d); iid rows favor +e_1 or -e_1 with probability 1/2 each","Every direction has probability kappa and the favored direction has an additional 1/2","delta=1/2; r>=1; disjoint candidate boxes have centers j(2r+1)e_1"],
  "source":{"source_id":"owner-own-work:adaptive-inward-box-selection-20261010", "artifact":"PAIRED_AUDIT.md"},
  "proof_or_counterexample":"Each box event has probability 4^(-r(2r+1)^(d-1))>0 and disjoint-box events are independent. The first matching index is finite almost surely. The selected center matches with probability 1; no deterministic location bound exists.",
  "independent_reviewer":"w446; pending", "remaining_gap":"No target RWRE counterexample is claimed. This does not meet or refute L3's bounded-center/start conditions.", "status":"proved special case", "novelty_claim":False},
 {"claim_id":"C0041-classification-001", "type":"conditional-reduction", "statement":"A summable slow-delay classification error plus logarithmic-size rare-pattern certificates within a polynomial search volume yields an integrable integer-valued duration under a positive-probability conditioning event.",
  "assumptions":["d>=2; P_env(A(x,r))<=exp(-a r^d) for all centers and integer r>=1, a>0","Q=P(.|E), P(E)=q>0, c>0, r(t)=floor(c log(t+2))>=1 eventually","Q(T>t)<=epsilon_t+Q(union_{|x|_infinity<=t} A(x,r(t))) eventually; epsilon_t>=0 and sum epsilon_t<infinity"],
  "source":{"source_id":"owner-own-work:quantitative-delay-classification-reduction-20261010", "artifact":"PAIRED_AUDIT.md"},
  "proof_or_counterexample":"Bound the conditioned union by q^(-1)(2t+1)^d exp(-a r(t)^d). For d>=2 this is eventually at most (t+2)^(-3). Sum the duration tail.",
  "independent_reviewer":"w446; pending", "remaining_gap":"The classification inequality is an unproved sufficient input for actual regeneration. It is not supplied by the finite-box lemmas.", "status":"proved special case", "novelty_claim":False},
 {"claim_id":"C0041-visit-cost-001", "type":"conditional-reduction", "statement":"For a pre-exit path confined to M states, a uniform conditional probability h of no revisit at each visit yields P(T>t,confined)<=M(1-h)^(floor(t/M)-1) for integers t>=M.",
  "assumptions":["T is a stopping time; B is a deterministic set of M>=1 states","At every kth visit to every x in B before T, conditioned on the visit sigma-field, probability of no further visit before T is >=h, 0<h<1","Time and visit counts are discrete"],
  "source":{"source_id":"owner-own-work:finite-volume-visit-hazard-duration-bound-20261010", "artifact":"RECENT_BRIDGE.md"},
  "proof_or_counterexample":"Tower iteration gives P(K_x>=m)<=(1-h)^(m-1). On confinement and T>t, one of M sites has at least floor(t/M) visits; take a union bound.",
  "independent_reviewer":"w446; pending", "remaining_gap":"For RWRE one must prove the uniform visit hazard, confinement and width-tail bounds under the correct law. No full-paper or formal check is claimed.", "status":"proved special case", "novelty_claim":False}
]
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as out:
    for claim in new_claims:
        out.write(json.dumps(claim)+"\n")

statements = [
 ("geometric-attempt-count-inference", "Invalid inference from geometric attempts to finite expected duration",
  "Invalid general inference: a geometric number of attempts and almost-sure finiteness of every attempt imply finite expected total duration. An integrable accounting of elapsed costs is additionally needed."),
 ("geometric-attempt-count-infinite-cost-counterexample", "Finite geometric attempts with infinite mean cost",
  "Unreviewed draft result. Let B_i be iid Bernoulli(q), 0<q<1. Independently, let L_i be iid with P(L_i=2^k)=2^(-k-1), k>=0. With N the first success and C=1+sum_{i<N} L_i, C is finite almost surely but E C is infinite. Truncation L_i to min(L_i,2^K) gives E C=1+((1-q)/q)(K/2+1). This is an abstract cost model, not an RWRE counterexample."),
 ("conditional-attempt-cost-summability", "Conditional cost premise for integrable repeated attempts",
  "Unreviewed draft reduction. Let F_i be an increasing filtration and S_i nested events with S_1 the whole space and S_i in F_i. If E[1_{S_{i+1}}|F_i]<=r 1_{S_i}, 0<=r<1, and nonnegative costs A_i satisfy E[1_{S_i} A_i|F_i]<=a 1_{S_i}, a finite, then E[sum_i 1_{S_i} A_i]<=a/(1-r). Tower iteration and Tonelli suffice; independence is unnecessary. The cost premise still needs proof in an application."),
 ("fixed-center-rarity-adaptive-center-inference", "Invalid transfer of fixed-center rarity to an unrestricted selected center",
  "Invalid general inference: if a finite environment pattern is rare at every deterministic center in an iid environment, it is equally rare at a center chosen by searching the entire environment. A deterministic search budget, an appropriate independence argument, or another selection-bias estimate is needed."),
 ("inward-box-rarity-unrestricted-selection", "An unrestricted search finds rare inward boxes almost surely",
  "Unreviewed draft result. In Z^d, d>=2, set kappa=1/(4d). Independently at each site choose +e_1 or -e_1 with equal probability; assign kappa to each direction and an additional 1/2 to the chosen direction. For B(x,r)=x+[-r,r]^d, require drift >=1/2 in coordinate 1 below x_1 and <=-1/2 above it. For fixed x,r>=1 the probability is 4^(-r(2r+1)^(d-1)). Disjoint boxes centered at j(2r+1)e_1 are independent. The first matching box exists almost surely, so its environment-measurable center matches with probability 1. The location is unrestricted; no directional-transience or full-target counterexample is asserted."),
 ("quantitative-delay-certificate-for-regeneration-mean", "A quantitative certificate sufficient for a conditioned duration mean",
  "Unreviewed draft reduction. Let T be a nonnegative integer duration, Q=P(.|E), P(E)=q>0, d>=2, and let environment events A(x,r) satisfy P_env(A(x,r))<=exp(-a r^d), a>0. Fix c>0 and r(t)=floor(c log(t+2)). Suppose eventually Q(T>t)<=epsilon_t+Q(union_{|x|_infinity<=t} A(x,r(t))), with epsilon_t>=0 and sum epsilon_t finite. A union bound gives a summable term q^(-1)(2t+1)^d exp(-a r(t)^d), hence E_Q T is finite. The classification premise for actual regeneration is unproved."),
 ("finite-volume-visit-hazard-duration-bound", "Finite-volume visit hazards control elapsed time",
  "Unreviewed draft reduction. Let T be a stopping time for a discrete process and B a deterministic finite set of M>=1 states. At every kth visit to any x in B before T, assume conditional probability at least h, 0<h<1, of no further visit to x before T, using that visit's sigma-field. Then for integer t>=M, P(T>t and all pre-exit states lie in B)<=M(1-h)^(floor(t/M)-1). Iterate conditional next-visit bounds and use a union bound over B. This controls time only after the visit hazard and confinement are proved.")]
entries = []
for name, title, statement in statements:
    entries.append({"key": name, "namespace": "probability.rwre.proof_audit",
                    "logical_name": name, "kind": "concept", "title": title,
                    "statement": statement, "proof_text": None,
                    "assumptions": ["Independent referee review pending; apply only the hypotheses stated in this concept"],
                    "domain": "probability theory",
                    "source": {"source_id": "owner-own-work:"+name,
                               "url": "urn:math:rwre-proof-audit:"+name,
                               "revision": "2026-10-10; unreviewed draft",
                               "license": "owner-own-work (campaign derivation; draft)", "excerpt": None}})
relations = [
 {"from_key":statements[1][0],"to_key":statements[0][0],"kind":"refutes", "rationale":"The explicit model has a geometric attempt count and finite individual costs but infinite expected total cost."},
 {"from_key":statements[4][0],"to_key":statements[3][0],"kind":"refutes", "rationale":"Every deterministic inward-box center is rare, while the first unrestricted matching center satisfies the event almost surely."},
 {"from_key":statements[2][0],"to_key":statements[1][0],"kind":"semantic_association", "rationale":"The sufficient conditional-cost premise identifies the integrability estimate missing from the geometric-count inference."},
 {"from_key":statements[5][0],"to_key":statements[4][0],"kind":"semantic_association", "rationale":"The duration reduction retains a deterministic polynomial search budget, whose absence causes the adaptive-selection counterexample."},
 {"from_key":statements[6][0],"to_key":statements[2][0],"kind":"semantic_association", "rationale":"Both duration estimates iterate conditional survival bounds at a specified filtration and include an explicit finite cost accounting."}]
bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w445", "bundle_slug":"rwre-regeneration-cost-audit-20261010", "entries":entries, "relations":relations}
keys = {e["key"] for e in entries}
assert len(keys) == len(entries) <= 200
for e in entries:
    assert e["kind"] == "concept" and e["proof_text"] is None
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", e["logical_name"])
    assert e["source"]["license"].startswith("owner-own-work")
    assert all(isinstance(e["source"][f], str) and e["source"][f] for f in ("source_id","url","revision","license"))
    assert not re.search(r"C:[/\\]|w44[4-6]|Yitzchak|Shmalo|owner names|trading", e["statement"], re.I)
for relation in relations:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in ("refutes","semantic_association")
draft_text = json.dumps(bundle, ensure_ascii=False, indent=2)+"\n"
(ROOT / "DRAFT_BUNDLE.json").write_text(draft_text, encoding="utf-8")
# A single dedicated author inbox is expressly authorized by this task.
inbox = Path("~/math-brain-inbox/w445")
assert str(inbox.resolve()).lower().endswith("math-brain-inbox\\w445")
inbox.mkdir(exist_ok=True)
target = next(inbox / f"bundle_{i:03d}.json" for i in range(1, 1000)
              if not (inbox / f"bundle_{i:03d}.json").exists()
              and not (inbox / f"bundle_{i:03d}.json.part").exists())
part = target.with_suffix(".json.part")
with part.open("x", encoding="utf-8") as output:
    output.write(draft_text)
assert json.loads(part.read_text(encoding="utf-8")) == bundle
part.rename(target)  # Windows fails instead of overwriting an existing final file.

checks = {"at_utc": now, "command":"python -X utf8 ~/brain_workers/w445/finish_packet.py",
          "exact_arithmetic_passed":sum(counts.values()), "groups":dict(counts),
          "hook_semantic_controls_passed":2, "draft_schema_entries":len(entries),
          "draft_relations":len(relations), "selected_probability_64_boxes":float(selected),
          "q_one_quarter_truncated_mean":{"K0":4,"K16":28},
          "runtime_seconds":round(time.monotonic()-started, 3),
          "mathematical_proof_scope":"Finite exact controls; full proofs are the prose derivations. These are not a formal proof receipt or a walk simulation."}
(ROOT / "CHECK_RESULTS.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
source_status = {"candidate_id":"C0041", "as_of":"2026-10-10", "current_openness":"UNKNOWN", "novelty_claim":False,
 "exact_target":{"model":"One sampled-once iid field of nearest-neighbor transition rows on Z^d, d>=2", "uniform_ellipticity":"exists deterministic kappa>0; all allowed transitions >=kappa almost surely", "direction":"fixed unit vector ell", "premise":"P_0(X_n dot ell -> +infinity)=1", "conclusion":"P_0(liminf (X_n dot ell)/n>0)=1"},
 "original_source":{"source_id":"drewitz_ramirez_rwre_2014", "url":"https://arxiv.org/pdf/1309.2589", "locator":"Open question 2.20, PDF page 24 (printed page 22)", "quote":"Is the RWRE necessarily ballistic in direction l?", "status":"statement checked against primary source"},
 "prior_attempt":{"attempt_id":"C0041-A001", "result":"Regeneration-time integrability remains unproved in that attempt", "artifact":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl", "H_and_I":"No exact C0041 record found in targeted searches", "Lean_ranking":"Annotation only; no proof receipt", "Team_O":"No exact C0041 assignment found in its board", "export_search":"No exact C0041/logical-name hit in the two named population exports; no whole export was loaded"},
 "recent_claim":{"date":"2026-09-23", "url":"https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf", "title":"Directional transience implies ballisticity", "claim":"Full target with deterministic velocity and positive directional projection", "audit_scope":"Conditional time-counting step in Proposition 2.5 only; equation (5), spatial inputs and whole proof not certified"},
 "formal_check":{"performed":False, "comparator_statement_url":"https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.lean", "comparator_has_sorry":True, "comparator_role":"Challenge template; its admission does not refute the separate solution", "configuration_url":"https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.json", "actual_solution_module":"OAI.Probability.Ballisticity.Main", "actual_solution_url":"https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/Ballisticity/Main.lean", "actual_top_level_theorem":"OAI.DirectionalTransience.directional_transience_implies_ballisticity", "actual_top_level_proof":"Calls directional_transience_implies_ballisticity_unit", "configuration_permitted_axioms":["propext","Quot.sound","Classical.choice"], "transitive_axioms_checked":False, "trusted_axiom_receipt":None, "comparator_success_receipt":None},
 "independent_derivation_saved_before_paired_proof":True, "submitted":True, "draft_path":str(target), "reviewed":False, "ingested":False, "retrievable":False,
 "remaining_gap":"A finite first moment of genuine regeneration duration under the exact conditioned law. For the finite-box route, the quantitative classification premise is unproved; for the recent manuscript, the decisive crossing estimate is unverified here."}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source_status, indent=2), encoding="utf-8")
(ROOT / "SERVED_IDENTITY.json").write_text(json.dumps({"native_worker":"w445", "requested_model":"gpt-6.1-sol", "requested_reasoning":"max", "response_side_served_model_evidence":None, "status":"UNKNOWN; requested settings are not served identity", "referee":"w446", "different_model_review_gate":"pending"}, indent=2), encoding="utf-8")
packet = f"""# C0041 review packet

Referee: w446. Integration contact named in the peer routing notice: codex-01a12190.
Review-ready artifacts: ATTEMPT.md, PAIRED_AUDIT.md, RECENT_BRIDGE.md, CLAIMS.jsonl, AUDIT_VERDICTS.jsonl, CHECK_RESULTS.json and DRAFT_BUNDLE.json in this worker folder.

Scoped KEEP: w444 R1/L1/L2/L2b/L3 under exactly their displayed assumptions. Source snapshot: sources/w444_ATTEMPT_snapshot.md; SHA256 {peer_hash}. This hash identifies the reviewed material; the mathematical reasons are in PAIRED_AUDIT.md. The full-target inference is NOT ESTABLISHED.

Please independently check the geometric-count heavy-tail counterexample, the conditional-cost bound, the unrestricted-center construction, the conditional classification reduction and the finite-volume visit-hazard bound. Each has explicit premises and a prose proof. Own claims await independent review; served author/referee identities and the different-model gate are unverified. No parent-problem solved claim is made.

Exact controls: {checks['exact_arithmetic_passed']} arithmetic checks passed, with 2 semantic hook controls. There are {len(entries)} concept entries and {len(relations)} allowed relations in the locally checked draft. The checks do not certify a full mathematical or formal proof. Reproduce with the command recorded in CHECK_RESULTS.json; the preparation script appends a new submission, so use verify_receipt.py for read-only verification of the saved receipts and schema.

Submitted draft: {target}. It was written complete and renamed from a .part file. Submitted=true; reviewed=false; ingested=false; retrievable=false. Source statements contain no owner names, home paths, worker ids or private labels. The integrator alone computes ingestion digests/seals and changes the live store.

The original source is Drewitz-Ramirez Open question 2.20. A September 2026 primary manuscript and a separate actual Lean solution claim the full target. Its challenge file is a template with an admission. The actual solution module and its permitted-axiom configuration are recorded, but no transitive axiom or successful comparator receipt has been obtained. Current openness remains UNKNOWN; no novelty is claimed.

The hook is a local proposal and unified diff at patches/01_regeneration_cost_hook.diff. The broader progress-page/hook-directory writes were not performed because the worker brief restricts writes outside its folder except the explicitly named draft inbox. The attempted team_comm reply returned no-team membership; no team was created and no agent was started.

NEXT: Independently check these narrow claims; the next proof input is a summable classification error for arbitrary slow regions, or the manuscript's super-polynomial crossing estimate with all conditioning justified.
"""
(ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
report = f"""# C0041 audit report

The exact target is uniformly elliptic iid nearest-neighbor RWRE in d>=2: almost-sure directional transience should imply positive directional speed. A recent primary manuscript and separate Lean solution claim it, so current openness is UNKNOWN and this work claims no novelty or resolution.

The paired finite-box lemmas R1/L1/L2/L2b/L3 receive scoped KEEP. Their missing input is a quantitative account of every long regeneration delay. I proved that a geometric number of finite attempts can have infinite mean cost, and that an unrestricted search finds a rare iid inward-box pattern almost surely. I also wrote sufficient conditional cost, classification and visit-count reductions, separating each from its unproved RWRE inputs. The recent manuscript explicitly pays for visit costs conditional on a separate strong crossing estimate; the negative controls do not refute it.

Measured checks: {checks['exact_arithmetic_passed']} exact arithmetic controls passed, plus 2 semantic hook controls; {len(entries)} draft concepts and {len(relations)} relations passed local schema checks. For q=1/4, the mean truncated total cost increases from 4 at K=0 to 28 at K=16 and diverges with K. For r=1,d=2 a fixed inward box has probability 1/64; selecting among 64 disjoint boxes raises it to {float(selected):.6f}. Commands and the fresh bounded gate are in CHECK_RESULTS.json and COMPUTE_GATE.json. No runtime recall improvement is claimed.

The draft is submitted at {target}. Its own results are concept/draft material pending w446. Integration, retrieval and different-model review are still pending. The actual Lean dependency chain and hardest crossing estimate have not been independently checked. The main risk is removing the deterministic search budget or substituting the unproved classification premise for a theorem.

Apply instruction: after review, the validating integrator can ingest the authorized draft. Apply patches/01_regeneration_cost_hook.diff to add exactly one proposal line to the named live proposal path; this worker did not edit that live file or any store. Recheck with python -X utf8 ~/brain_workers/w445/verify_receipt.py.

NEXT: Referee checks the narrow claims; the next concrete proof step is a certificate for arbitrary low-crossing regions with a summable classification error under the actual regeneration law.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
evidence_hashes = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                   for name in ("ATTEMPT.md","PAIRED_AUDIT.md","RECENT_BRIDGE.md","CLAIMS.jsonl","REVIEW_PACKET.md")}
(ROOT / "EVIDENCE_HASHES.json").write_text(json.dumps({"purpose":"review artifact identification only; no draft-ingestion digest or seal generated", "sha256":evidence_hashes}, indent=2), encoding="utf-8")
(ROOT / "PROGRESS_READY.txt").write_text("w445 C0041: scoped KEEP of five finite-box reductions; two counterexamples and three conditional reductions saved; seven concept drafts submitted, full regeneration integrability unproved. Evidence: REVIEW_PACKET.md.\n", encoding="utf-8")
print(json.dumps({"checks":checks, "draft":str(target), "peer_snapshot_sha256":peer_hash}, indent=2))
