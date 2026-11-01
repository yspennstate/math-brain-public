"""Write an idempotent local review packet; publication is a separate step."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
measure=json.loads((root/"MEASUREMENTS.json").read_text(encoding="utf-8"))
recall=json.loads((root/"recall_receipt.json").read_text(encoding="utf-8"))
def write_json(name,data):
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

source={
 "target":"C0052","recorded_title":"Non-triviality of the scaling limit of the three-dimensional Ising model",
 "current_openness":"UNKNOWN","parent_problem_solved_by_this_packet":False,
 "primary":{"title":"Lectures on the Ising and Potts models on the hypercubic lattice",
  "author":"Hugo Duminil-Copin","url":"https://arxiv.org/pdf/1707.00520v1",
  "locator":"printed page 94 (PDF index 93), Conjecture 6, equations (7.1)-(7.2)",
  "short_quote":"Prove that the three-dimensional Ising model is non-trivial",
  "verification":"Primary PDF text inspected directly; source hash not freshly recomputed.",
  "intake_reported_sha256":"cc442344d0cc21c5d57163719b06dfaf1d243dee8731716bf89d21c593f98a5b"},
 "exact_formulation":{
  "model":"Free, translation-invariant, spin-flip symmetric zero-field nearest-neighbour ferromagnetic Ising state on Z^3, with 0<beta<beta_c.",
  "G":"G_beta(x,y)=E_beta[sigma_x sigma_y]",
  "U4":"E_beta[sigma_0 sigma_x sigma_y sigma_z] minus the three pair-correlation products; repeated labels are retained.",
  "chi":"chi(beta)=sum_x G_beta(0,x)",
  "xi":"xi(beta)=[lim_n -(1/n)log G_beta(0,n e1)]^(-1)",
  "g":"g(beta)=sum_{x,y,z} U4(0,x,y,z)/(chi(beta)^2 xi(beta)^3)<=0",
  "target":"g(beta) does not tend to zero as beta increases to beta_c from below.",
  "quantifier":"There is epsilon>0 such that for every delta>0 there is beta in (beta_c-delta,beta_c) with -g(beta)>=epsilon.",
  "auxiliary_target":"A uniform critical smeared fourth-cumulant deficit plus nondegenerate field convergence. This is a separate sufficient route, not an asserted equivalence to g."},
 "historical_checks":[
  {"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl","line":52,"status":"unreviewed; attempted_unsolved; primary locator recovered"},
  {"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl","line":42,"status":"C0052-A001: second-moment variance gap not closed; no independent check recorded"},
  {"path":"~/<private-repo>/06_math_research/prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md","line":592,"status":"attempted_un; no formal theorem receipt recovered"},
  {"paths":["probability_1000_attempts_H_20260912","probability_1000_attempts_I_20260914"],"status":"targeted exact-ID search returned no C0052 record; not an exhaustive owner-solved/retired check"},
  {"path":"~/brain_workers/teams/W0300_O/TEAM_BOARD.md","status":"no C0052 assignment returned by exact-ID search"}],
 "primary_literature_checked":[
  {"url":"https://arxiv.org/html/2112.04248v2","locator":"Theorem 5.4; Sections 7,8,11","scope":"zero-field ferromagnetic current identity and explicit 3D gap; 2022 context is not a current-status certificate"},
  {"url":"https://arxiv.org/html/1912.07973v2","locator":"Theorem 1.2 and Proposition 1.4","scope":"d=4 Gaussianity; dimension and upper-bound direction do not supply a d=3 lower bound"},
  {"url":"https://arxiv.org/pdf/1612.02436v4","locator":"abstract and conformal-block setup","scope":"bootstrap CFT calculation; does not provide the lattice convergence/current second-moment bridge"}],
 "status_search":"Two bounded primary-literature searches plus named local records; insufficient to certify current openness or novelty.",
 "served_model_evidence":{"requested":"gpt-6.1-sol, maximum reasoning, Fast tier",
  "response_side_identity":"UNAVAILABLE in this tool context","author_native_identity":"w478",
  "referee":"w479","different_model_review_gate":"NOT SATISFIED"},
 "formal_check_receipt":None,
 "paired_proof_read":True,"independent_checkpoint":"ATTEMPT.md L1/L2 saved before any paired proof read"}
write_json("SOURCE_STATUS.json",source)

moment="DRAFT conditional lemma: If real X_n converge in law, E X_n=0, E X_n^2=1 and E X_n^4<=3-epsilon for one fixed 0<epsilon<=2, then the limit X is centered, has variance one and E X^4<=3-epsilon, so it is non-Gaussian. Fourth-power uniform integrability is unnecessary: the fourth bound gives second-power uniform integrability, and Portmanteau bounds the limiting fourth moment. This does not supply an Ising deficit or field tightness."
invalid="REJECTED INFERENCE: A diverging mean E N_n of a nonnegative overlap count by itself implies a scale-uniform positive probability P(N_n>0). The implication is false without an anti-concentration or relative second-moment premise, even when the count is finite at each scale."
counter="DRAFT counterexample to the first-moment inference: For integer n>=2, let N_n=n^2 with probability 1/n and zero otherwise. Then E N_n=n tends to infinity, P(N_n>0)=1/n tends to zero, and E N_n^2/(E N_n)^2=n. For any nonnegative witness N with 0<E N and E N^2<=C(E N)^2, Cauchy-Schwarz instead guarantees P(N>0)>=1/C. This is a logical counterexample, not an Ising-current construction."
weighted="DRAFT conditional current bridge: On a finite ferromagnetic Ising graph at finite beta, zero external field and free boundary, choose nonzero nonnegative f. Set G_xy=E sigma_x sigma_y, V=sum f_x f_y G_xy and mu(x,y)=f_x f_y G_xy/V. For positive-weight pairs sample independent currents with source sets {x} symmetric-difference {y} and {z} symmetric-difference {t}; q is the probability x is connected to z in their union, with reflexive connectivity. Repeated sources cancel. Then 3-E[(sum f_x sigma_x/sqrt(V))^4]=2 sum mu(x,y)mu(z,t)q(x,y,z,t). A witness's relative second-moment bound must hold under this endpoint-weighted law and for the original connection event. No critical 3D bound is supplied."
event="DRAFT route obstruction: Adding independent sourceless currents enlarges source clusters and can give an upper bound on the exact two-sourced-current connection probability in the fourth-Ursell identity. A lower bound on the enlarged event cannot be reversed into a lower bound on the original event. A valid overlap witness for nontriviality must imply connection in the original union, or a separate quantitative comparison must be proved."
comparison="DRAFT conditional comparison: In a translation-invariant, spin-flip symmetric zero-field Ising state on Z^3 assume U4<=0, 0<chi,xi<infinity and A=sum_{y,z,t} -U4(0,y,z,t)<infinity. Put g=-A/(chi^2 xi^3). For any nonempty finite block B, let M=|B|, S=sum_{x in B}sigma_x, V=E S^2>0 and R=3-E S^4/V^2. Then -g>=R V^2/(M chi^2 xi^3). Thus along beta_n increasing to beta_c, bounds R_n>=r>0 and V_n/[chi_n sqrt(M_n xi_n^3)]>=b>0 imply -g(beta_n)>=r b^2>0. These near-critical premises have not been proved for C0052."
def entry(key,logical,title,statement,assumptions):
    return {"key":key,"namespace":"probability.ising.scaling","logical_name":logical,
     "kind":"concept","title":"[DRAFT] "+title,"statement":statement,"proof_text":None,
     "assumptions":assumptions,"domain":"probability / Ising scaling limits",
     "source":{"source_id":"owner-own-work:probability300:C0052:w478:"+key,
       "url":"~/brain_workers/w478/ATTEMPT.md","revision":"author-checkpoint-2026-10-10",
       "license":"owner-own-work (campaign deductions; independent review pending)","excerpt":None}}
entries=[
 entry("moment","negative-fourth-deficit-portmanteau-transfer","Fourth-deficit transfer without fourth-moment convergence",moment,["real variables","weak convergence","mean zero","unit second moment","fixed positive fourth deficit"]),
 entry("invalid-mean","rejected-diverging-overlap-mean-inference","Rejected first-moment shortcut",invalid,["this entry labels a false inference; it is not a theorem"]),
 entry("counterexample","rare-overlap-counterexample-and-second-moment-premise","Rare-overlap counterexample",counter,["integer n>=2","nonnegative witness; finite second moment for the sufficient bound"]),
 entry("weighted","endpoint-weighted-two-current-cumulant-bridge","Exact endpoint-weighted bridge",weighted,["finite graph","ferromagnetic couplings","zero field; free boundary","finite beta","nonnegative nonzero weights","source parity cancellation"]),
 entry("event","augmented-current-lower-bound-direction-obstruction","Enlarged-current event obstruction",event,["exact original two-current event distinguished from enlarged clusters","no lower comparison supplied"]),
 entry("comparison","near-critical-block-deficit-to-renormalized-coupling-comparison","Block deficit to source coupling comparison",comparison,["translation invariance; spin-flip symmetry","U4<=0","positive finite chi and xi","finite nonnegative origin Ursell sum","nonempty finite block with positive variance"])]
relations=[
 {"from_key":"counterexample","to_key":"invalid-mean","kind":"refutes","rationale":"The explicit N_n family has diverging mean and vanishing positivity probability."},
 {"from_key":"weighted","to_key":"moment","kind":"depends_on","rationale":"An actual uniform averaged connection lower bound gives a fourth deficit; the moment criterion then transfers it to any given weak scalar limit."},
 {"from_key":"event","to_key":"weighted","kind":"semantic_association","rationale":"The weighted identity uses the original two-current event; the enlarged event cannot supply its lower bound without another premise."},
 {"from_key":"comparison","to_key":"weighted","kind":"semantic_association","rationale":"Near-critical block deficits can be compared to the original infinite-volume source coupling when the explicit normalization premises hold."}]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w478",
 "bundle_slug":"c0052-adversary-current-bridge-001","entries":entries,"relations":relations}
write_json("bundle_001.json",bundle)

proofs={"moment":"ATTEMPT.md L1: tail bound (3-epsilon)/R^2 for second powers; Portmanteau for fourth powers.",
 "counterexample":"ATTEMPT.md L2: calculate E N_n=n, P(N_n>0)=1/n; Cauchy-Schwarz gives the sufficient second-moment bound.",
 "weighted":"ATTEMPT.md L3: expand U4 and insert the switching identity, including parity cancellation for coincident labels.",
 "event":"ATTEMPT.md enlarged-event paragraph: upper comparison (8.1)-(8.3) cannot be reversed.",
 "comparison":"ATTEMPT.md L4: nonnegative block Ursell sum <= |B| times the full origin sum by translation invariance."}
existing=set()
claims_path=root/"CLAIMS.jsonl"
if claims_path.exists():
    existing={json.loads(line)["id"] for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()}
claims=[]
for e in entries:
    if e["key"]=="invalid-mean":
        continue
    claims.append({"id":"w478-"+e["key"],"kind":"draft_deduction","exact_statement":e["statement"],
      "assumptions":e["assumptions"],"source":{"own_proof":"ATTEMPT.md","primary":"SOURCE_STATUS.json primary_literature_checked"},
      "proof_or_counterexample":proofs[e["key"]],"independent_reviewer":"w479; requested, pending",
      "remaining_gap":"Independent review and response-side different-model evidence; the scale-uniform C0052 current bound remains unproved.",
      "status":"sketch","novelty_claim":False})
claims.append({"id":"w478-R2","kind":"local_retrieval_repair_measurement",
 "exact_statement":f"On one fixed {measure['candidate_headers']}-header sample, whole-token matching removed {measure['before_lexical_false_matches']} substring false matches and retained {measure['valid_whole_token_headers_retained']} whole-token matches; {measure['control_passes']}/{measure['control_count']} lexical controls passed.",
 "assumptions":["local saved sample only; not an engine-wide recall evaluation","matches concern token identity, not theorem applicability"],
 "source":"MEASUREMENTS.json; store_retrieval.json","proof_or_counterexample":"python -X utf8 local_repair_measure.py",
 "independent_reviewer":"w479; pending","remaining_gap":"Global repair and representative evaluation are proposals; no live recall change made.","status":"numerical evidence"})
claims.append({"id":"w478-A1","kind":"paired_proof_audit","exact_statement":"Scoped KEEP for w477 L001 and the conditional L002/L003/L007 reductions, with the uniform current second-moment premise explicitly unproved.",
 "assumptions":["only the stated conditional conclusions are kept","no parent-problem or different-model gate satisfaction"],
 "source":"AUDIT_W477_L001.md; AUDIT_W477_MAIN.md","proof_or_counterexample":"Checked moment tails, endpoint normalization, nonnegative sums, shift, ceil(xi)^3 and the original single-current overlap event.",
 "independent_reviewer":"w478 as adversary; w479 remains referee for new w478 results",
 "remaining_gap":"Uniform near-critical Q bound; current openness UNKNOWN; served-model evidence unavailable.","status":"sketch"})
by_key={e["key"]:e for e in entries}
for i,r in enumerate(relations,1):
    claims.append({"id":f"w478-E{i}","kind":"draft_edge","exact_statement":r,
      "assumptions":["draft concept endpoints only"],"source":"bundle_001.json",
      "from_card_quote":by_key[r["from_key"]]["statement"],"to_card_quote":by_key[r["to_key"]]["statement"],
      "proof_or_counterexample":r["rationale"],"independent_reviewer":"w479; pending",
      "remaining_gap":"Coordinator validates relation and all mathematical promotion gates; no live edge added.","status":"sketch"})
with claims_path.open("a",encoding="utf-8") as f:
    for row in claims:
        if row["id"] not in existing:
            f.write(json.dumps(row,ensure_ascii=False)+"\n")

hook={"id":"current-overlap-w478-01","area":"math","event":"stage-start",
 "cue":"A proof tries to lower-bound the original sourced-current connection event using only an overlap mean or an enlarged-current event.",
 "fire_when":"EN grows and is used to assert a positive uniform connection probability without a relative second-moment or comparison estimate.",
 "silent_when":"An overlap mean is used only as a Markov upper bound, or a scale-uniform second moment under the exact witness law is supplied.",
 "text":"An overlap mean only bounds positivity from above. A lower bound needs an explicit uniform second-moment or anti-concentration estimate under the exact law. Added sourceless currents change the event; check the comparison direction.",
 "evidence":"ATTEMPT.md L2-L4; MEASUREMENTS.json exact rare-overlap family; perceptron_proof_open_gaps_fleet_2026_07_12",
 "proposer":"w478"}
assert len(hook["text"])<=300
(root/"HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")

report=f"""# w478 C0052 report

The source-faithful target uses near-critical g(beta), not just a critical block cumulant. I saved an independent obstruction, audited w477's main conditional current bridge, and proved the elementary block-to-g comparison in ATTEMPT.md L4. All new deductions await w479; C0052 is not solved by this packet and current openness is UNKNOWN.

The hardest remaining step is a bounded relative second moment for the specified near-critical, source-weighted SINGLE currents. A diverging overlap mean, spin Lebowitz inequalities, and lower bounds for enlarged four-current clusters do not provide it. My comparison additionally displays the exact block-variance/susceptibility normalization required by a block route.

Measured retrieval failure: general brain recall took {recall['elapsed_seconds']:.2f} s, with on-topic precision@3=0/3 (recall_receipt.json). A bounded math-source lookup admitted {measure['before_lexical_false_matches']}/{measure['candidate_headers']} substring false matches, such as 'raising'. A local whole-token filter removed all {measure['before_lexical_false_matches']} and retained {measure['valid_whole_token_headers_retained']} valid token matches, with {measure['control_passes']}/{measure['control_count']} controls passing in {measure['elapsed_seconds']:.4f} s. Commands: python -X utf8 recall_bounded.py; python -X utf8 store_retrieval.py; python -X utf8 local_repair_measure.py. This is a small local lexical control, not evidence of better mathematical recall generally. A narrower store scan hit its 20-second guard; the saved-header fallback returned no scaling/current theorem in that bounded sample. No corpus absence is claimed.

The returned named theorem 'The fibre is an Ising partition function' is inspected in RETRIEVED_THEOREM_REPORT.json. Its finite NAE/Rademacher construction uses a negative coupling parameter, not a critical ferromagnetic nearest-neighbour state on Z^3. Its stored conditions field is empty and its trust status unverified; its actual statement/attached source, rather than that field, supplies the hypotheses. It gives no positive lower bound for the required source-conditioned current overlap. The primary current identity applies at zero field with ferromagnetic couplings; the separate 4D Gaussian theorem has the wrong dimension and bound direction for C0052.

Bounded proposed repair: use whole-token Ising matching and explicit domain/source-set/temperature/bound-direction metadata; route C0052 to its precise source and conditional gap instead of Ising-perceptron or unrelated substring hits. The lexical demonstration is measured; domain routing and global deployment remain proposals.

Apply: after independent mathematical checks, the validating coordinator may handle the concept-only bundle in the authorized inbox using BUNDLE_SPEC.md. No worker integration command was run, no live store or recall controls were edited, and no theorem promotion is authorized by this packet. HOOK_PROPOSAL.jsonl is local for coordinator submission because the worker's external-write authorization is limited to its named brain inbox and communication/progress tools.

Risk: changing beta_c blocks into near-critical g silently changes the task; enlarged events can reverse the needed inequality; source parity and zero-weight endpoint pairs must be retained. All exact assumptions and proofs are in ATTEMPT.md and CLAIMS.jsonl. Hashes are provenance, not a proof. No formal theorem check was run. Requested model settings do not certify the served model.

NEXT: w479 independently checks L1-L4, especially parity cancellation and L4's normalization; then the coordinator validates the draft and pursues the near-critical relative second-moment estimate.
"""
(root/"REPORT.md").write_text(report,encoding="utf-8")
packet="""# C0052 review packet for codex-01a12190 and w479

Author w478; native identity preserved. Current source status UNKNOWN. No parent-problem solved claim. Requested model gpt-6.1-sol is not served-model evidence; response-side identity is unavailable. Different-model proof promotion gate remains unsatisfied.

Read ATTEMPT.md L1-L4 and SOURCE_STATUS.json first. L1/L2 were saved before any w477 proof read. AUDIT_W477_L001.md and AUDIT_W477_MAIN.md contain scoped KEEP for conditional results only. The observed paired ATTEMPT hash after the audited read is 9665c80c7c5662655d6f3e47d82b713a4785092f90ac5defe11b6452eb2e7c4a; L001 hash is 363f399619ea3126b1f2e9d764d86cf5eab2953750cec72b154ebfe4acaf5450.

Check L4 independently: block nonnegative Ursell sum <= |B| times the full origin sum, so -g>=R_B V_B^2/(|B| chi^2 xi^3). Assumptions include stationarity, spin-flip symmetry, U4<=0, finite positive chi and xi, finite origin sum, and positive block variance. It is conditional: the uniform near-critical block deficit and normalized variance-capture lower bound are unproved.

Check L3's exact endpoint-weighted law, zero-weight pairs, repeated sources and reflexive connectivity. A lower bound for augmented four-current clusters is inadequate for the original event. Check L1's one-sided Portmanteau transfer; fourth-moment equality is unnecessary. L2 supplies an explicit obstruction, not an Ising counterexample.

CLAIMS.jsonl contains full statements, assumptions, evidence, reviewer and remaining gaps, including four exact draft edges with both endpoint texts. bundle_001.json has only concept entries, all marked DRAFT; no lemma/theorem card is proposed for immediate promotion. BUNDLE_LIFECYCLE.json separates prepared, submitted, reviewed, ingested and retrievable.

MEASUREMENTS.json and recall_receipt.json give the measured failure and bounded local repair control. No blind evaluation materials were opened; no Ising simulation, GPU training, agents or background runners were started. validate_packet.py checks the draft shape and edge acyclicity; this is not a mathematical proof check. REVIEW_HASHES.json identifies the finished artifacts. Integrate only through the validating coordinator after applicable gates.

NEXT: referee L1-L4; if kept, validate and stage the concept draft while leaving the scale-uniform current estimate unresolved.
"""
(root/"REVIEW_PACKET.md").write_text(packet,encoding="utf-8")
write_json("BUNDLE_LIFECYCLE.json",{"prepared":True,"submitted":False,"reviewed":False,
 "ingested":False,"retrievable":False,"local_path":str(root/"bundle_001.json"),
 "intended_inbox":"~/math-brain-inbox/w478/bundle_001.json",
 "promotion":"concept-only DRAFT; independent/different-model gate pending"})
write_json("INBOX_CLAIM.json",{"claim_id":"clm-c47cf412f3","agent":"w478",
 "resource":"~/math-brain-inbox/w478","expires_at":"2026-10-10T07:15:03Z"})
names=("ATTEMPT.md","SOURCE_STATUS.json","CLAIMS.jsonl","AUDIT_W477_L001.md","AUDIT_W477_MAIN.md",
       "REPORT.md","REVIEW_PACKET.md","bundle_001.json","MEASUREMENTS.json","HOOK_PROPOSAL.jsonl")
write_json("REVIEW_HASHES.json",{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names})
print(json.dumps({"prepared":True,"draft_concepts":len(entries),"draft_edges":len(relations),
 "claims_rows":sum(1 for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()),
 "review":"~/brain_workers/w478/REVIEW_PACKET.md","published":False}))
