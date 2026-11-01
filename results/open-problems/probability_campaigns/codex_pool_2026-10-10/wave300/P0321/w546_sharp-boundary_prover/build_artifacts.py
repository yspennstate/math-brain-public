"""Prepare scoped draft concepts; never open the mathematical store for writing."""
from __future__ import annotations
import difflib
import json
from pathlib import Path
from datetime import datetime, timezone

root=Path(__file__).resolve().parent
claims_path=root/"CLAIMS.jsonl"
claims=[json.loads(line) for line in claims_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
assert len(claims)==5 and len({c["claim_id"] for c in claims})==5
for claim in claims:
    claim["exact_statement"]=claim["exact_statement"].replace("|x|^-|G|^2/(4pi beta mu)","|x|^[-|G|^2/(4pi beta mu)]").replace("|x-y|^-m^2/(2pi beta K)","|x-y|^[-m^2/(2pi beta K)]")
    claim["source"]["license"]="owner-own-work"
    if claim["claim_id"].endswith("L01"):
        claim["peer_review_receipt"]="~/brain_workers/w547/AUDIT_W546_L01.md"
        claim["peer_review_status"]="KEEP original stated Gaussian/L1 scope; assigned w548 review pending"
claims_path.write_text("".join(json.dumps(c,ensure_ascii=False)+"\n" for c in claims),encoding="utf-8")
p=root/"LEMMA_L03.md"
s=p.read_text(encoding="utf-8").replace("B r^-m^2/(2pi beta K)","B r^[-m^2/(2pi beta K)]").replace("Lambda^-m^2/(2pi beta K)","Lambda^[-m^2/(2pi beta K)]")
p.write_text(s,encoding="utf-8")

v=json.loads((root/"VERIFICATION.json").read_text(encoding="utf-8-sig"))
sv=json.loads((root/"VERIFICATION_SMOOTH.json").read_text(encoding="utf-8-sig"))
assert v["status"]==sv["status"]=="PASS"
sample=next(r for r in sv["rows"] if r["gaussian_increment_variance"]==1.0)
namespace="probability.statisticalmechanics"

def entry(key,name,kind,title,statement,assumptions,artifact):
    return {"key":key,"namespace":namespace,"logical_name":name,"kind":kind,"title":title,"statement":statement,"proof_text":None,"assumptions":assumptions,"domain":"probability and statistical mechanics","source":{"source_id":"owner-own-work:w546:P0321:"+key,"url":"file:///~/brain_workers/w546/"+artifact,"revision":"author proof 2026-10-10; pending w548 independent review","license":"owner-own-work","excerpt":None}}

entries=[
 entry("gaussian-increments","cutoff-planar-gaussian-angle-field-with-stationary-increments","definition","Cutoff planar Gaussian angle-increment field","For beta,K,Lambda>0, g is the centered real Gaussian field on R^2 anchored by g(0)=0 with covariance E[g(x)g(y)]=integral_{0<|k|<Lambda}(exp(i k.x)-1)(exp(-i k.y)-1)/(beta K |k|^2) d^2k/(2pi)^2. The integral is a finite positive Gram kernel. Its stationary increment variance v(x-y)=F(Lambda|x-y|)/(pi beta K), with F(z)=integral_0^z(1-J0(t))dt/t, is (pi beta K)^-1 log|x-y|+O(1) at large separation. This is an explicit auxiliary field, not a microscopic Riesz Gibbs identification.",["beta,K,Lambda positive and finite","real symmetric Gaussian spectral construction","finite ultraviolet cutoff"],"LEMMA_L03.md"),
 entry("quantized-counterexample","stationary-increment-quantized-angle-defeats-variance-order-inference","concept","DRAFT: quantized angle variance does not determine periodic order","DRAFT AUTHOR-PROVED AUXILIARY COUNTEREXAMPLE, pending independent w548 review. Let g be the cutoff planar Gaussian increment field, m=6, h=2pi/m, and U,V independent uniforms in [0,h), independent of g. Set q(x)=h floor((g(x)+V)/h), theta=U+q. The field q has stationary increments. With v=Var[g(x)-g(y)], v<=Var[q(x)-q(y)]<=v+h^2/4, so its variance grows logarithmically with bounded error. However E exp[i6(theta(x)-theta(y))]=1 identically and E exp(i6theta(x))=0. This disproves a variance-only inference for periodic order, not the existence of a hexatic Riesz Gibbs phase.",["specified Gaussian increment field g","independent global uniform offsets U,V","h=2pi/6","abstract angle-lift construction"],"LEMMA_L04.md"),
 entry("smooth-counterexample","smooth-monotone-angle-perturbation-breaks-variance-to-order-inference","concept","DRAFT: smooth bounded perturbations can retain orientational order","DRAFT AUTHOR-PROVED AUXILIARY COUNTEREXAMPLE, pending independent w548 review. Let g be the cutoff planar Gaussian increment field, m=6, h=2pi/m, 0<A<1/m, and U,V independent uniforms on [0,h), independent of g. Put f_A(t)=t+A sin(mt), q_A(x)=f_A(g(x)+V)-f_A(V), theta_A=U+q_A. The map f_A is smooth strictly increasing, |q_A-g|<=2A, and q_A has stationary increments. With v=Var[g(x)-g(y)], Var[q_A(x)-q_A(y)]=v+A^2(1-exp(-m^2v/2)). Yet C_m(x-y)=E exp[i m(theta_A(x)-theta_A(y))] tends to J1(mA)^2>0. Its m-fold phase field is stationary with zero one-point mean. Hence even a smooth bounded monotone perturbation with logarithmic variance correct to O(1) can fail algebraic decay of periodic order. This is not a Riesz Gibbs model or a P0321 solution.",["specified real Gaussian stationary-increment field with finite UV cutoff","m=6; 0<A<1/m","independent global uniforms U,V","no microscopic Gibbs identification"],"LEMMA_L05.md"),
 entry("rejected-bridge","rejected-logarithmic-angle-variance-to-sixfold-decay-bridge","concept","Rejected route: logarithmic variance alone implies sixfold decay","DRAFT ROUTE AUDIT, pending independent w548 review. The proposed implication that stationary angle increments with Var(theta(x)-theta(y))=c log|x-y|+O(1), c>0, automatically give algebraically vanishing E exp[i6(theta(x)-theta(y))] is FALSE for general non-Gaussian fields. The quantized construction has correlation 1, and the smooth bounded monotone construction has positive plateau J1(6A)^2 despite preserving the Gaussian variance within A^2. Gaussianity or direct periodic characteristic-function estimates must be part of a valid inference. These auxiliary counterexamples do not refute P0321.",["proposed bridge assumes stationary increments and logarithmic variance","bridge does not assume an exactly Gaussian angular law"],"LEMMA_L05.md"),
 entry("transfer-gap","riesz-hexatic-microscopic-characteristic-function-transfer-gap","concept","DRAFT: the unresolved microscopic hexatic transfer gap","P0321 OPENNESS UNKNOWN as checked 2026-10-10; no solution claimed. The remaining gap in this attempt is a uniform defect-sensitive transfer from an actual neutralized two-dimensional Riesz Gibbs ensemble on a nonempty finite-temperature interval to the orientational characteristic function and fast positional decorrelation in the SAME thermodynamic state, with measurable bond observables specified. Defect-free phonons give a positive orientational plateau and algebraic positional order; a Gaussian variance approximation alone also fails by the explicit non-Gaussian counterexamples. Control of dislocations/disclinations and of periodic characteristic functions is missing. This is a draft gap record, not a theorem about the Gibbs gas.",["actual Riesz Gibbs law and neutralization must be specified","phase interval is nonempty and at finite positive temperature","moment estimates alone are insufficient"],"ATTEMPT.md")
]
relations=[
 {"from_key":"quantized-counterexample","to_key":"gaussian-increments","kind":"depends_on","rationale":"The explicit construction q=h floor((g+V)/h) uses the specified stationary Gaussian increments; its variance differs from v by at most h^2/4."},
 {"from_key":"smooth-counterexample","to_key":"gaussian-increments","kind":"depends_on","rationale":"The construction f_A(g+V)-f_A(V) uses the same g, and the Gaussian increment characteristic function enters its exact variance and Fourier correlation."},
 {"from_key":"smooth-counterexample","to_key":"quantized-counterexample","kind":"analogous_to","rationale":"Both preserve logarithmic increment variance up to a bounded error and retain periodic long-range order; the smooth version additionally uses a strictly increasing smooth f_A."},
 {"from_key":"quantized-counterexample","to_key":"rejected-bridge","kind":"refutes","rationale":"The rejected bridge predicts vanishing sixfold correlation from c log r+O(1) variance, but q has that variance and its sixfold correlation is identically 1."},
 {"from_key":"smooth-counterexample","to_key":"rejected-bridge","kind":"refutes","rationale":"The rejected variance-only inference predicts decaying periodic order; the smooth stationary-increment example has variance v+O(1) and positive limit J1(6A)^2."},
 {"from_key":"transfer-gap","to_key":"smooth-counterexample","kind":"cites","rationale":"The gap record requires characteristic-function transfer because the smooth construction shows covariance accuracy alone can give the wrong order behavior."},
 {"from_key":"transfer-gap","to_existing_logical":"math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases","kind":"semantic_association","rationale":"This is the remaining gap of the P0321 attempt. The existing card asks for intermediate orientational order without crystalline positional order; no solves/proves relation is asserted."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w546","bundle_slug":"p0321-smooth-variance-bridge-counterexamples-20261010","entries":entries,"relations":relations}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
keys={e["key"] for e in entries}
assert len(keys)==len(entries)<=200
for e in entries:
    assert required<=e.keys() and e["kind"] in {"definition","concept"} and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work") and e["statement"]
for r in relations:
    assert r["kind"] in allowed and r["from_key"] in keys
    assert "to_existing_logical" in r or r["to_key"] in keys
local=root/"DRAFT_BUNDLE.json"
payload=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
local.write_text(payload,encoding="utf-8")
inbox=Path("~/math-brain-inbox/w546")
inbox.mkdir(parents=True,exist_ok=True)
destination=inbox/"bundle_001.json"
if destination.exists():
    raise FileExistsError("Existing draft preserved; inspect and select a new bundle number")
part=inbox/"bundle_001.part"
part.write_text(payload,encoding="utf-8")
part.rename(destination)
now=datetime.now(timezone.utc).isoformat()
state={"observed_at":now,"submitted":{"status":True,"path":str(destination),"claim":"clm-06f37f46f1"},"reviewed":{"status":False,"scope":"Assigned w548 review pending; w547 kept only L01, which is not submitted as a new lemma"},"ingested":{"status":None,"note":"No coordinator ingestion receipt observed; no store write attempted"},"retrievable":{"status":None,"note":"No new-node recall verified; submission is not retrieval"},"entry_count":len(entries),"relation_count":len(relations),"duplicate_control":"Gaussian L01-L03 retained in the proof packet only; new concepts focus L04-L05, disjoint from w543 Gaussian covariance lane and w547 endpoint limits"}
(root/"BRAIN_STATE.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
source_path=root/"SOURCE_STATUS.json"
source=json.loads(source_path.read_text(encoding="utf-8-sig"))
source.update(submitted=True,reviewed=False,ingested=None,retrievable=None)
source["handoff_receipts"]["w548_full_packet"]="msg-fd1778fb1c"
source["brain_state_artifact"]="BRAIN_STATE.json"
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding="utf-8")
hook={"id":"variance-periodic-order-w546-01","area":"math","event":"stage-start","cue":"An attempted proof of hexatic/sixfold order infers characteristic-function decay from logarithmic variance or bounded covariance error without a Gaussian law.","fire_when":"A proof says logarithmic angle variance plus stationarity implies algebraic sixfold decay.","silent_when":"The proof has exact Gaussian angular laws or direct periodic characteristic-function estimates and states its Gibbs transfer gap.","text":"For periodic order, covariance is not enough. Smooth monotone bounded perturbations can preserve log angle variance within O(1) yet retain a positive sixfold plateau. Require Gaussianity or characteristic-function control; state the microscopic defect-transfer gap.","evidence":"~/brain_workers/w546/LEMMA_L05.md; VERIFICATION_SMOOTH.json: variance error <=1/144, plateau 0.05869400558416215. Scar: perceptron_proof_open_gaps_fleet_2026_07_12.","proposer":"w546"}
assert len(hook["text"])<=300
hook_line=json.dumps(hook,ensure_ascii=False)+"\n"
(root/"HOOK_PROPOSAL.jsonl").write_text(hook_line,encoding="utf-8")
patchdir=root/"patches"; patchdir.mkdir(exist_ok=True)
patch="".join(difflib.unified_diff([],hook_line.splitlines(keepends=True),fromfile="a/~/primary_directive/hooks1000/proposals/math-w546.jsonl",tofile="b/~/primary_directive/hooks1000/proposals/math-w546.jsonl"))
(patchdir/"01_periodic_order_hook.diff").write_text(patch,encoding="utf-8")
report=f"""The deliverable is a sharp obstruction to a proposed hexatic proof bridge: even a smooth strictly increasing bounded perturbation of a Gaussian angle field can preserve its logarithmic increment variance to O(1) while its sixfold correlation stays positive. Five author-proved auxiliary claims and their complete proofs are saved; P0321 itself is unproved and current openness is UNKNOWN.

The source is Lewin VI.B, pp.66-67. The prior store contained two unverified P0321 records, including a one-point rotational-mixture warning. This packet adds the disjoint non-Gaussian variance/characteristic-function obstruction. Gaussian derivations are retained for review, while the submitted bundle omits new Gaussian lemma entries to avoid overlap with w543/w547.

Measurement: python -X utf8 verify_smooth.py passed in {sv['cpu_seconds']:.6f} CPU seconds. At Gaussian increment variance 1, the perturbed variance is {sample['smooth_increment_variance']:.12f}; a Gaussian prediction using that variance is {sample['gaussian_prediction_using_smooth_variance']:.12g}, while direct quadrature gives {sample['sixfold_direct_integral']:.12f}. The correlation differs by a factor {sample['actual_to_gaussian_prediction']:.6g}. Direct quadrature versus Fourier-series error is at most {sv['correlation_max_direct_series_error']:.3g}. The exact limiting plateau is {sv['orientational_plateau']:.12f}. This compares an invalid moment-based inference with the actual auxiliary law, not a deployed recall-performance improvement.

python -X utf8 verify_boundary.py also passed: angular-log error {v['angular_log_formula_max_absolute_error']:.3g}; projector identity error {v['projector_angular_identity_max_absolute_error']:.3g}; eta_6 measured {v['critical_eta6_measured_64_to_256']:.10f} against 0.125. These are numerical coefficient checks; proofs are in LEMMA_L01.md through LEMMA_L05.md. There is no formal theorem-prover receipt or microscopic Gibbs proof.

Submitted {len(entries)} DRAFT definition/concept entries and {len(relations)} supported relations at {destination.as_posix()}, after exclusive claim clm-06f37f46f1. Assigned w548 review, ingestion, and retrieval remain separate unconfirmed states. w547 kept L01 only. Source and progress receipts are in SOURCE_STATUS.json and BRAIN_STATE.json.

Apply: the reviewer checks REVIEW_PACKET.md, then the validating coordinator integrates accepted DRAFT concepts; append the local HOOK_PROPOSAL.jsonl to its authorized rolling proposal file using patches/01_periodic_order_hook.diff. The worker does not apply live changes or run integrate_drafts.py. A progress-page event is staged locally because the worker brief forbids other writes outside its folder except the explicit brain draft destination.

Risk: the counterexamples are angle fields, not Gibbs point configurations. The microscopic defect-sensitive characteristic-function transfer and fast positional decorrelation in the same finite-temperature Gibbs state remain the hardest gap.

NEXT: w548 audits the exact non-Gaussian constructions; the next mathematical step is a characteristic-function transfer hypothesis with errors relative to the target correlation.
"""
(root/"REPORT.md").write_text(report,encoding="utf-8")
rp=root/"REVIEW_PACKET.md"
rp.write_text(rp.read_text(encoding="utf-8")+f"\nFinal measurement: VERIFICATION_SMOOTH.json is PASS. Smooth plateau {sv['orientational_plateau']:.12f}, variance error <=1/144, direct-series error {sv['correlation_max_direct_series_error']:.3g}. DRAFT_BUNDLE.json contains {len(entries)} entries focused on L04-L05; Gaussian L01-L03 are comparison material. Submission states are in BRAIN_STATE.json.\n",encoding="utf-8")
progress={"agent":"w546","row":"S1.P0321.boundary","event":"Saved five auxiliary proofs; smooth bounded variance-error counterexample checked, five DRAFT concepts submitted, w548 review pending","evidence":str(root/"REPORT.md"),"posting_status":"staged only under write-scope restriction"}
(root/"PROGRESS_ROW.json").write_text(json.dumps(progress,indent=2),encoding="utf-8")
(root/"STATUS.md").write_text("STATE: WORKING\nNEXT: Confirm final review handoff and artifact integrity; then set NEEDS_REVIEW.\n2026-10-10: Five author-proved auxiliary results saved; P0321 unproved, openness UNKNOWN.\n2026-10-10: Both fresh-gate quadrature checks PASS. Main smooth counterexample keeps variance within 1/144 yet retains plateau 0.058694005584.\n2026-10-10: Five DRAFT definition/concept entries submitted atomically after exclusive claim clm-06f37f46f1; no integration or recall claim.\n2026-10-10: Statement-first handoff msg-9691cd9081; full w548 proof request msg-fd1778fb1c. w547 KEEP on L01 only; assigned referee review pending.\n",encoding="utf-8")
print(json.dumps({"submitted":str(destination),"entries":len(entries),"relations":len(relations),"auxiliary_claims":len(claims),"hook_characters":len(hook["text"]),"measured_actual_gaussian_ratio":sample["actual_to_gaussian_prediction"]},indent=2))
