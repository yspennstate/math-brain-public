"""Prepare a conservative concept-only draft and a local review packet.

No integrator, store write, global hook deployment, or service is invoked.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w388")
source_state = json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source_state["brain_and_review"]["proof_gap"] = (
    "No vanishing root-crossing estimate obtained. The all-ray shell-rate route is withdrawn: "
    "sum shell q>=1 and sup shell q>=1/(8n). The September manuscript's all-label crossing/no-fork "
    "bridge is not independently certified."
)
source_state["brain_and_review"]["review_receipts"] = {
    "w389": "C01,C02,C04,C05 KEEP; C03 FIX accepted; C06 requested",
    "w392": "Independent check requested for w389's new shell-floor correction; pending",
}
(ROOT/"SOURCE_STATUS.json").write_text(json.dumps(source_state,indent=2),encoding="utf-8")

claim_path = ROOT/"CLAIMS.jsonl"
claims = [json.loads(line) for line in claim_path.read_text(encoding="utf-8").splitlines() if line.strip()]
history = ROOT/"CLAIM_HISTORY.jsonl"
if not history.exists():
    history.write_text("\n".join(json.dumps(c) for c in claims)+"\n",encoding="utf-8")
for c in claims:
    suffix = c["claim_id"].rsplit(".",1)[-1]
    if suffix in {"C01","C02","C04","C05"}:
        c["status"] = "independently checked proof"
        c["review_status"] = "KEEP by w389; not a formal receipt or integration approval"
        c["independent_reviewer"] = "w389; REVIEWS.jsonl, announced to w388 on 2026-10-10"
        c["remaining_gap"] = {
            "C01":"No gap in the counterexample. It does not refute the intended atomless-law target.",
            "C02":"Reduction only; P(E_n)->0 remains unproved by this worker. No novelty claim.",
            "C04":"No gap in the abstract logical counterexample; it is not an iid-FPP counterexample.",
            "C05":"Bounded positive-law localization only; no asymptotic probability result follows from finite controls.",
        }[suffix]
    elif suffix == "C03":
        c["exact_statement"] = (
            "Under the A1 class of continuous iid planar FPP with E[min of four independent weights squared]<infinity, "
            "T_x denotes the union of all infinite rays from x and q(z)=P(z in T_0). For H existence of a bigeodesic "
            "through0, P(H)<=one-half sum_{x in S_n}q(-x)<=4n sup_{x in S_n}q(x). This inequality is valid, but "
            "the proposed vanishing all-ray shell sum or o(1/n) marginal input is impossible, because T_0 hits every shell "
            "almost surely and sum_{x in S_n}q(x)>=1. That floor is recorded separately as C07, originated by w389."
        )
        c["status"] = "proved special case"
        c["review_status"] = "FIX by w389 accepted; valid incidence inequality retained, route withdrawn"
        c["remaining_gap"] = "No viable no-bigeodesic route from this all-ray statistic. The floor correction is awaiting the designated w392 check; two-ended root-crossing decay remains unresolved."
        c["revision"] = "v2 after w389 correction; v1 preserved in CLAIM_HISTORY.jsonl"
claims.append({
    "claim_id":"w388.P0117.C07",
    "exact_statement":"If T_0 is the union of all infinite simple rays from 0 and there is an infinite ray almost surely, then for S_n={||x||_infinity=n}, sum_{x in S_n}P(x in T_0)=E|T_0 intersect S_n|>=1 and max_{x in S_n}P(x in T_0)>=1/(8n). Hence vanishing all-ray shell incidence and an o(1/n) maximum shell probability are impossible. These hypotheses hold in the continuous iid FPP A1 class.",
    "assumptions":["Z^2, |S_n|=8n for n>=1","at least one infinite simple ray from0 almost surely","T_0 contains all such rays","A1 only to obtain the ray existence assertion in FPP"],
    "source":{"type":"owner-own-work","originator":"w389","artifact":"ATTEMPT.md (accepted correction)","review_source":"~/brain_workers/w389/REVIEWS.jsonl"},
    "proof_or_counterexample":"An infinite simple ray must leave each finite B_(n-1) through S_n. The shell count is therefore at least1 almost surely; take expectations and divide by its 8n possible vertices. In A1, finite geodesics from0 to ne1 have unbounded length, and anchored prefix compactness gives an infinite ray.",
    "independent_reviewer":"w392, designated independent reviewer for w389's own results; requested",
    "remaining_gap":"Designated w392 check pending. This is an obstruction to the attempted one-ended shell route, not a proof of absence or existence of bigeodesics.",
    "status":"proved special case","review_status":"pending w392; attribution preserved","created":"2026-10-10",
})
claim_path.write_text("\n".join(json.dumps(c,ensure_ascii=False) for c in claims)+"\n",encoding="utf-8")

entries=[]
def entry(key,name,title,statement,assumptions,artifact,author="w388"):
    entries.append({"key":key,"namespace":"probability.fpp","logical_name":name,"kind":"concept",
        "title":title,"statement":statement,"proof_text":None,"assumptions":assumptions,
        "domain":"probability theory",
        "source":{"source_id":f"owner-own-work:20261010:{author}:P0117:{key}",
            "url":f"urn:owner-own-work:20261010:{author}:P0117:{key}",
            "revision":"draft-review-20261010-v1","license":"owner-own-work (campaign derivation or attributed literature audit; concept only)",
            "excerpt":None}})

entry("source-state","planar-fpp-bigeodesic-source-status-20261010","P0117 source status and exact assumptions",
    "DRAFT source audit, 10 October 2026. The planar undirected nearest-neighbor FPP conjecture concerns iid finite nonnegative edge weights with an atomless common law and excludes every injective doubly infinite path whose finite segments achieve global passage times. Damron-Hanson arXiv:1512.00804v2 Conjecture1 states the moment-free target. The A1 working class adds E[min(X1,X2,X3,X4)^2]<infinity. A public OpenAI manuscript dated24 September2026, No bigeodesics in planar first-passage percolation, Theorem1.1 claims the full result in A1 without shape regularity; its main proof has not been independently certified in this packet. Current openness UNKNOWN; no novelty claim. A local source hash and a posterior sublemma audit do not certify that main theorem. The 7September2026 attempted-unsolved ranking is a historical status only.",
    ["Graph Z^2, undirected nearest-neighbor edges","iid finite nonnegative weights","atomless law","additional A1 moment only where explicitly imposed"],"SOURCE_STATUS.json")
entry("unit-counterexample","constant-weight-planar-fpp-bigeodesic-counterexample","Continuity is essential to the displayed iid target",
    "Independently checked by w389; draft concept only. The bare assertion that every planar iid nonnegative weight law has no bigeodesic is false. With t_e=1 almost surely, each horizontal line v_k=(k,c), k in Z, is a bigeodesic: its segment between i and j costs |j-i|, and every competing lattice path has at least |j-i| edges. This degenerate iid example does not refute the intended atomless-law conjecture.",
    ["Nearest-neighbor Z^2","Degenerate iid unit weights"],"CLAIMS.jsonl:C01")
entry("root-crossing","global-root-crossing-compactness-certificate","Exact root-crossing compactness certificate",
    "Independently checked by w389; draft concept only. For any finite nonnegative weights on Z^2 let B_n={||x||_infinity<=n}, S_n={||x||_infinity=n}, and E_n be existence of a simple GLOBAL geodesic through0 with endpoints on S_n and all other vertices in B_(n-1). Then E_(n+1) is a subset of E_n, and their intersection equals existence of a bigeodesic through0. Stop each arm at its first boundary hit for restriction; consistent central finite strings follow by finite-degree diagonal compactness. Consequently P(bigeodesic through0)=lim P(E_n). Under translation invariance, absence everywhere is equivalent to this limit being0. This reduction supplies no decay bound or novelty claim.",
    ["Finite nonnegative weights","Global minimizing metric, not a restricted box metric","Simple paths","Translation invariance only for the everywhere conclusion"],"CLAIMS.jsonl:C02")
entry("shell-route","all-ray-shell-incidence-route-withdrawn","All-ray shell route withdrawn after referee correction",
    "REFUTED ROUTE, retained as a draft warning. In A1 planar iid FPP let T_x contain all infinite geodesic rays fromx and q(z)=P(z in T_0). Every bigeodesic through0 yields two distinct shell vertices whose rays visit0, so P(H)<=one-half sum_{x in S_n}q(-x)<=4n max_{x in S_n}q(x). The all-ray density theorem arXiv:2208.11576 Theorem1.1 gives uniform q(z)->0, with A1's continuous law and finite second moment of the minimum of four weights. Trying to make the displayed shell sum vanish is impossible: every infinite ray from0 hits S_n, so its sum is at least1 and the maximum at least1/(8n). The valid incidence inequality does not make that contradictory premise a viable proof route. A genuinely two-ended/root-crossing statistic is required; no new decay estimate is obtained.",
    ["A1 continuous iid law, finite second moment of minimum of four weights","T_x is the union of all infinite rays"],"CLAIMS.jsonl:C03,C07")
entry("shell-floor","all-ray-shell-incidence-positive-floor","Every all-ray geodesic tree has a positive shell floor",
    "DRAFT correction originated by w389; designated w392 check pending. If T_0 is the union of infinite simple rays from0 and at least one such ray exists almost surely, then for S_n={||x||_infinity=n}, sum_{x in S_n}P(x in T_0)=E|T_0 intersect S_n|>=1 and max_{x in S_n}P(x in T_0)>=1/(8n). A ray leaves every finite box, so it supplies a shell vertex. A1 planar FPP has such rays by compactness of geodesic prefixes anchored at0. This obstructs vanishing one-sided all-ray incidence even if bigeodesics are absent; it says nothing about whether bigeodesics exist.",
    ["At least one infinite simple ray from0 almost surely","All rays included in T_0","|S_n|=8n"],"CLAIMS.jsonl:C07",author="w389")
entry("witness-union","shrinking-witness-marginals-do-not-control-existence","Uniform marginal decay does not control a growing witness union",
    "Independently checked by w389; draft concept only. For U uniform[0,1), the n^2 events A_(n,j)={floor(n^2 U)=j}, 0<=j<n^2, each have probability1/n^2 while their union has probability1 for every n; union events can thus be decreasing without their probabilities vanishing. This is a logical counterexample, not an iid FPP example. S_n has8n vertices and 32n^2-4n unordered endpoint pairs, so a union-bound route to root-crossing decay needs cardinality times the prescribed-pair bound to vanish. A uniform o(n^-2) pair bound suffices; merely tending to0 does not.",
    ["Growing set of possible witnesses","No joint union bound supplied"],"CLAIMS.jsonl:C04")
entry("bounded-localization","positive-bounded-fpp-global-distance-localization","Deterministic localization preserves global distances",
    "Independently checked by w389; draft concept only. If all weights on Z^2 satisfy0<a<=t_e<=b<infinity, then global distances between any u,v in B_n equal distances computed in B_R, R=n+ceil(4bn/a). A coordinate path costs at most4bn; every no-dearer competitor has at most floor(4bn/a) edges and stays in B_R. The finitely many such paths attain the infimum. Thus global root-crossing E_n uses only edges in B_R. Computing in B_n itself can misclassify a geodesic: an explicit positive-weight example has a B_1 minimizing path through0 costing20, but an outside ten-edge detour costs10.",
    ["Deterministically bounded positive weights","Global distances","No iid or uniqueness requirement"],"CLAIMS.jsonl:C05")
entry("posterior","output-conditioned-monotone-edge-raise-kernel","Posterior law for raises after output-measurable path selection",
    "DRAFT separately derived narrow check; w389 review pending. Take edgewise independent triples X_e~G,U_e uniform[0,1],Z_e~G conditioned on[b,infinity), independent across edges. Let a<b, p_a=G([0,a])>0,p_b=G([b,infinity))>0 and deterministic0<=delta_e<p_a on a finite deterministic set F. Put xi_e=1{X_e<=a,U_e<=delta_e/p_a}, Y_e=Z_e if xi_e=1 and X_e otherwise; outside F keep Y_e=X_e. Given the ENTIRE individual output Y, including exterior, the xi_e are independent Bernoulli with theta_e=1_[b,infinity)(Y_e)delta_e/(p_b+delta_e). Divide the joint raised-output density by the output density and factor independent coordinate kernels. A finite simple path prefix selected from Y alone is fixed by this conditioning and inherits that kernel. No other site's output or later marking success is conditioned on. This checks the September2026 manuscript's Lemma7.2 only, not its main theorem.",
    ["Independent triples and independent coordinates","Deterministic finite modified edge set","Output-only measurable selection","Distinct edges in a simple prefix"],"CLAIMS.jsonl:C06")

relations=[
    {"from_key":"unit-counterexample","to_key":"source-state","kind":"semantic_association","rationale":"The counterexample explains why the target's atomless-law qualification matters."},
    {"from_key":"root-crossing","to_key":"source-state","kind":"semantic_association","rationale":"The root-crossing event is an exact finite-path certificate for the target's two-ended existence event."},
    {"from_key":"shell-floor","to_key":"shell-route","kind":"refutes","rationale":"The route proposes a vanishing sum over all rays; the count is at least1 on every shell, so that premise is impossible."},
    {"from_key":"witness-union","to_key":"root-crossing","kind":"semantic_association","rationale":"Root crossing has a growing set of possible boundary witnesses; their uniform marginal convergence requires a union estimate."},
    {"from_key":"bounded-localization","to_key":"root-crossing","kind":"specializes","rationale":"For bounded positive weights the same global crossing event is determined inside an explicitly enlarged finite box."},
    {"from_key":"posterior","to_key":"source-state","kind":"cites","rationale":"The source-status concept records the September manuscript whose Lemma7.2 is the precise audited posterior law."},
    {"from_key":"source-state","to_existing_logical":"math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp","kind":"cites","rationale":"The existing card records a September7 attempted-unsolved status; this audit supplies the dated September24 claimed theorem and retains UNKNOWN correctness."},
    {"from_key":"root-crossing","to_existing_logical":"math:probability.core:attempt-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp","kind":"cites","rationale":"The prior attempt identifies lost anchoring; E_n explicitly anchors the compactness argument at0 without claiming a decay estimate."},
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w388","bundle_slug":"p0117-one-sided-shell-obstruction-20261010-w388","entries":entries,"relations":relations}
(ROOT/"bundle_001.json").write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding="utf-8")

# Record exact supporting ends for every proposed relation inside the worker's report area.
existing=json.loads((ROOT/"store_target_rows.json").read_text(encoding="utf-8"))
existing_by_logical={json.loads(x["metadata_json"])["logical_id"]:x for x in existing}
by_key={x["key"]:x for x in entries}
edge_rows=[]
for rel in relations:
    if "to_key" in rel:
        target=by_key[rel["to_key"]]
        quote_to=target["statement"]
    else:
        target=existing_by_logical[rel["to_existing_logical"]]
        quote_to=target["body"]
    edge_rows.append({**rel,"quote_from":by_key[rel["from_key"]]["statement"],"quote_to":quote_to,
        "independent_audit":"pending validating coordinator; relation not ingested"})
(ROOT/"EDGE_EVIDENCE.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in edge_rows)+"\n",encoding="utf-8")

hook={"id":"fpp-w388-01","area":"math","event":"stage-start",
    "cue":"A bigeodesic argument proposes vanishing boundary incidence of the union of all one-sided rays, or o(1/n) for its maximal shell-vertex probability.",
    "fire_when":"A1 iid planar FPP; T_0 contains all infinite rays and the proposed input is sum over S_n P(x in T_0)->0.",
    "silent_when":"The statistic is a genuine two-ended/root-crossing event, or the proof explicitly accounts for the unavoidable all-ray shell count.",
    "text":"Every infinite ray from0 hits each box boundary. For the union of all rays, the shell sum is at least1 and its largest vertex probability at least1/(8n). Check whether a proposed two-ended argument uses this impossible one-sided premise.",
    "evidence":"~/brain_workers/w388/ATTEMPT.md C03 correction; w389/REVIEWS.jsonl FIX; w392 check pending; MEASUREMENTS.json paired-shell controls",
    "proposer":"w388"}
assert len(hook["text"])<=300
hook_text=json.dumps(hook,ensure_ascii=False)+"\n"
(ROOT/"HOOK_PROPOSAL.jsonl").write_text(hook_text,encoding="utf-8")
patches=ROOT/"patches"
patches.mkdir(exist_ok=True)
(patches/"01_one_sided_shell_hook.diff").write_text(
    "--- a/~/primary_directive/hooks1000/proposals/math-w388.jsonl\n"
    "+++ b/~/primary_directive/hooks1000/proposals/math-w388.jsonl\n"
    "@@ -0,0 +1 @@\n+"+hook_text,encoding="utf-8")

states={"bundle":"bundle_001.json","draft_prepared":True,"submitted":False,
        "reviewed":False,"review_detail":"w389 KEEP on C01,C02,C04,C05; C03 FIX accepted; C06/C07 and bundle relations pending",
        "ingested":False,"retrievable":False,"live_store_changed":False}
state_path=ROOT/"BUNDLE_STATES.json"
state_path.write_text(json.dumps(states,indent=2),encoding="utf-8")

# The task explicitly authorizes this agent's draft inbox. No pre-existing file is replaced.
INBOX.mkdir(exist_ok=True)
dest,part=INBOX/"bundle_001.json",INBOX/"bundle_001.part"
assert dest.parent.resolve()==INBOX.resolve() and part.parent.resolve()==INBOX.resolve()
if dest.exists() or part.exists():
    raise RuntimeError("draft path already exists; do not overwrite it")
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding="utf-8")
part.rename(dest)
states.update(submitted=True,submitted_path=str(dest),submission_kind="DRAFT concept bundle; integration deliberately not invoked")
state_path.write_text(json.dumps(states,indent=2),encoding="utf-8")
print(json.dumps({"submitted":str(dest),"entries":len(entries),"relations":len(relations),"claim_rows":len(claims),"hook":"local proposal/diff only"}))
