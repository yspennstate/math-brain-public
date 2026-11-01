"""Prepare review artifacts only inside w450. No live-store or inbox writes."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
attempt = ROOT.joinpath("ATTEMPT.md").read_text(encoding="utf-8")
receipt = json.loads(ROOT.joinpath("exact_receipt.json").read_text(encoding="utf-8"))
assert receipt["status"] == "PASS"

def section(n):
    text = attempt.split(f"L{n}. ",1)[1]
    stop = f"L{n+1}. " if n < 5 else "Source checkpoint:"
    return text.split(stop,1)[0].strip()

source = {"type":"owner-own-work","path":str(ROOT.joinpath("ATTEMPT.md"))}
claims = [json.loads(ROOT.joinpath("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()[0])]
statements = {
1:"For a killed nearest-neighbour UE walk on a finite connected U containing 0 and x, conditional on all kernels outside x, G_U^omega(0,x)=h/(sum_e omega(x,e)q_e), where h=P_omega^0(H_x<T_U) (h=1 for x=0), q_e=P_omega^(x+e)(T_U<H_x) (q_e=1 outside U). The quantities h,q are independent of the x kernel under the iid site law. Conditional occupation-weighted drift is E_pi[d_ell(p)/(p dot q)]/E_pi[1/(p dot q)].",
2:"For every iid nearest-neighbour environment on Z^d, d>=2, with all transitions >=kappa>0, and a unit ell such that d_ell(p)>=0 almost surely and m=E[d_ell(p)]>0, every finite connected U containing 0 and x has E[G_U(0,x)d_ell(omega(x))]/E[G_U(0,x)] >= kappa*m/[1-(2d-1)kappa]. In particular E_0[(X_(T_U)-X_0) dot ell] >= this constant times E_0[T_U].",
3:"Let d>=2, a=1/(2d), 0<b<a and theta in (0,1]. At iid sites choose the balanced row p0(e)=a with probability 1-theta and row p+(+e1)=a+b, p+(-e1)=a-b, p+(e)=a transversely with probability theta. Every finite-domain Kalikow drift in e1 is at least 2*b*theta/[1+(1-theta)*b/a]. The bound is sharp over arbitrary nonnegative exit vectors q, with no assertion of geometric or speed sharpness. The standard Kalikow criterion and L5 give a deterministic velocity with v dot e1 at least that bound. At theta=0 or b=0 the e1 speed is zero.",
4:"In an iid UE environment on Z^2 with rows p+=(9/20,1/20,1/4,1/4) and p-=(1/20,9/20,1/4,1/4), P(p+)=51/100, the mean e1 local drift is 1/125>0, but the annealed Kalikow drift at x=0 in U={0,-e1}, starting at 0, is -62753/3982809<0. For general type probability theta the signed numerator has sign 31280*theta^2+223282*theta-127281, giving exactly the negative-drift interval 1/2<theta<theta_star, with theta_star in (53/100,531/1000). This is a counterexample to a mean-drift-to-Kalikow bridge; no directional transience claim is made for this law.",
5:"For a law satisfying L2 or L3 and admitting an almost-sure deterministic velocity v, the corresponding uniform occupation-drift lower bound c also satisfies v dot ell>=c. Proof uses discounted single-site Green functions and an Abelian limit; it needs no separate regeneration moment assumption. Velocity existence for these restricted laws follows from the standard Kalikow-to-ballisticity theorem, treated as an external dependency."
}
assumptions = {
1:["finite connected U contains 0 and x","nearest-neighbour UE kernel","iid site law for the conditional expectation statement"],
2:["d>=2","iid site kernels","deterministic uniform ellipticity kappa>0","fixed unit direction","nonnegative local directional drift almost surely","positive mean m"],
3:["d>=2","iid binary site kernels as explicitly stated","0<b<1/(2d)","0<theta<=1","standard Kalikow implication used only for velocity existence"],
4:["d=2","iid two-type law explicitly stated","kappa=1/20","finite domain U={0,-e1}","no premise or conclusion about full-walk directional transience"],
5:["iid law L2 or L3","almost-sure deterministic velocity exists","nearest-neighbour increments bounded by 1"]
}
for n in range(1,6):
    claims.append({"id":f"w450-L{n}","target":"C0041","statement":statements[n],
      "assumptions":assumptions[n],"source":dict(source,section=f"L{n}"),
      "proof_or_counterexample":section(n),"independent_reviewer":{"assigned":"w452","status":"pending","received":False},
      "remaining_gap":"No gap in this author proof; independent check pending. Parent C0041 regeneration-time integrability remains unproved here.",
      "status":"proved special case","novelty":"not claimed",
      "measurement_receipt":"exact_receipt.json" if n in (3,4) else None,
      "external_dependency":"Sznitman-Zerner Kalikow-to-ballisticity implication; scope recorded in arXiv:1902.08920 introduction" if n in (3,5) else None})
claims.append({"id":"w450-C0041-target","target":"C0041","statement":json.loads(ROOT.joinpath("SOURCE_STATUS.json").read_text(encoding="utf-8"))["exact_target"],
  "assumptions":["d>=2","nearest-neighbour","iid site environments","uniform ellipticity","fixed unit direction","annealed probability-one directional transience"],
  "source":{"url":"https://arxiv.org/abs/1309.2589","locator":"Open question 2.20, PDF p.24, printed p.22"},
  "proof_or_counterexample":"Only the restricted L2/L3 classes are covered here. A recent public proof claim is recorded separately; it is not accepted as independently verified.",
  "independent_reviewer":{"assigned":"w452","status":"pending"},"remaining_gap":"For general signed local drift, prove an integrable regeneration time from directional transience without adding a quantitative ballisticity assumption.",
  "status":"conjecture","current_openness":"UNKNOWN","novelty":"not claimed"})
ROOT.joinpath("CLAIMS.jsonl").write_text("".join(json.dumps(c,ensure_ascii=False)+"\n" for c in claims),encoding="utf-8")

def draft_entry(key, name, title, statement, assumption_list, kind="concept"):
    return {"key":key,"namespace":"probability.randomenvironment","logical_name":name,"kind":kind,"title":title,
      "statement":statement,"proof_text":None,"assumptions":assumption_list,"domain":"probability theory",
      "source":{"source_id":"owner-own-work:w450:c0041-boundary:"+key,"url":str(ROOT.joinpath("ATTEMPT.md")),
        "revision":"author-proof-2026-10-10-review-pending","license":"owner-own-work","excerpt":None}}

entries = [
draft_entry("kalikow-definition","finite-domain-kalikow-directional-drift","Finite-domain Kalikow directional drift",
 "For an iid uniformly elliptic nearest-neighbour RWRE, let U be a finite connected domain containing 0 and x, T_U its first exit, G_U^omega(0,x)=E_omega^0[sum_(n<T_U) 1_(X_n=x)], and d_ell(omega(x))=sum_e omega(x,e)(e dot ell). The finite-domain Kalikow directional drift at x is E[G_U^omega(0,x)d_ell(omega(x))]/E[G_U^omega(0,x)]. The weighting by the Green function depends on the site's kernel.",assumptions[1],"definition"),
draft_entry("nonnegative-bound","nonnegative-local-drift-kalikow-lower-bound","DRAFT: Nonnegative local drift gives a uniform occupation bound",
 "DRAFT; author proof, independent review pending. "+statements[2],assumptions[2]),
draft_entry("rare-bias-bound","rare-positive-bias-among-balanced-sites-velocity-bound","DRAFT: Quantitative rare-positive-bias special case",
 "DRAFT; author proof, independent review pending. "+statements[3],assumptions[3]),
draft_entry("discount-transfer","discounted-green-occupation-to-velocity-bound","DRAFT: Discounted occupation bound transfers to velocity",
 "DRAFT; author proof, independent review pending. "+statements[5],assumptions[5]),
draft_entry("false-bridge","refuted-positive-mean-drift-to-kalikow-bridge","Refuted auxiliary bridge: positive mean implies positive Kalikow drift",
 "REFUTED PROPOSED BRIDGE, not a theorem: the proposed universal implication is that in an iid uniformly elliptic nearest-neighbour environment on Z^2, E[d_e1(omega(0))]>0 forces positive finite-domain Kalikow e1 drift at every x in every finite connected U containing 0. The explicit two-site example in this bundle contradicts that implication. This refuted bridge has no directional transience hypothesis and is distinct from C0041.",
 ["hypothetical iid UE law on Z^2","positive mean local e1 drift"]),
draft_entry("two-site-obstruction","iid-positive-mean-negative-kalikow-two-site-example","DRAFT: Exact iid two-site obstruction to a mean-drift bridge",
 "DRAFT; author counterexample, independent review pending. "+statements[4],assumptions[4]),
draft_entry("c0041-status","c0041-historical-question-current-status-caution","C0041: Historical question and unverified recent resolution claim",
 "STATUS NOTE 2026-10-10: C0041 asks whether iid uniformly elliptic nearest-neighbour RWRE on Z^d, d>=2, that is annealed almost surely transient in a fixed direction must be ballistic in that direction. The 2013 source is Open question 2.20 (PDF p.24, printed p.22). The stored September-7 search is dated. A September-23-2026 public manuscript and separate Lean proof entrypoint claim the full conclusion; no independent rebuild or transitive trusted-axiom receipt was obtained here. Current openness UNKNOWN. Do not confuse the admitted comparator statement with the separate proof or mark C0041 solved from a source/hash check.",
 ["dated source-status note","no parent-target proof certified by w450"])
]
relations = [
 {"from_key":"nonnegative-bound","to_key":"kalikow-definition","kind":"depends_on","rationale":"The conclusion bounds exactly the occupation-weighted ratio in the definition."},
 {"from_key":"rare-bias-bound","to_key":"nonnegative-bound","kind":"specializes","rationale":"The binary balanced/positive-drift law has nonnegative local drift and permits a stronger exact ratio bound."},
 {"from_key":"rare-bias-bound","to_key":"discount-transfer","kind":"depends_on","rationale":"The velocity lower bound uses the discounted transfer after the standard criterion gives a velocity."},
 {"from_key":"discount-transfer","to_key":"kalikow-definition","kind":"depends_on","rationale":"The finite-domain ratio proof extends to discounted Green functions and an Abelian velocity limit."},
 {"from_key":"two-site-obstruction","to_key":"false-bridge","kind":"refutes","rationale":"Both ends refer to iid UE Z^2; mean drift 1/125 is positive, but the specific finite-domain Kalikow drift is -62753/3982809."},
 {"from_key":"two-site-obstruction","to_key":"kalikow-definition","kind":"depends_on","rationale":"The computed negative quantity is exactly the defined finite-domain occupation ratio."},
 {"from_key":"c0041-status","to_existing_logical":"math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic","kind":"semantic_association","rationale":"Adds a dated source-status caution to the exact existing target without asserting a proof or refutation."}
]
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w450","bundle_slug":"c0041-green-boundary-w450-001","entries":entries,"relations":relations}
draft = ROOT.joinpath("draft")
draft.mkdir(exist_ok=True)
draft_file = draft.joinpath("bundle_001.json")
bundle_text = json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
draft_file.write_text(bundle_text,encoding="utf-8")
hook = {"id":"C0041-w450-01","area":"math","event":"stage-start","cue":"positive (mean|average|annealed) local drift used to infer positive Kalikow or occupation-weighted drift",
 "fire_when":"A signed local-drift law is justified only by its positive first-step mean before a Kalikow argument.",
 "silent_when":"Local directional drift is proved nonnegative almost surely, or the occupation ratio is already bounded using its exact dependence.",
 "text":"Positive mean local drift does not imply positive occupation-weighted drift when local signs vary. Condition outside the site and keep G=h/(p dot q). IID UE two-site example: mean 1/125, Kalikow -62753/3982809.",
 "evidence":str(ROOT.joinpath("exact_receipt.json"))+":counterexample; ATTEMPT.md L4","proposer":"w450"}
assert len(hook["text"]) <= 300
hook_dir = ROOT.joinpath("hook_proposals")
hook_dir.mkdir(exist_ok=True)
hook_text = json.dumps(hook,ensure_ascii=False)+"\n"
hook_dir.joinpath("probability-boundary-w450.jsonl").write_text(hook_text,encoding="utf-8")
patch_dir = ROOT.joinpath("patches")
patch_dir.mkdir(exist_ok=True)
for patch_name, live, content in (
 ("01_c0041_draft.diff","~/math-brain-inbox/w450/bundle_001.json",bundle_text),
 ("02_probability_hook.diff","~/primary_directive/hooks1000/proposals/probability-boundary-w450.jsonl",hook_text)):
    patch = "".join(difflib.unified_diff([],content.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
    patch_dir.joinpath(patch_name).write_text(patch,encoding="utf-8")
states = {"prepared":True,"submitted":False,"reviewed":False,"ingested":False,"retrievable":False,
 "intended_inbox":"~/math-brain-inbox/w450/bundle_001.json",
 "staged_bundle":str(draft_file),"reason_not_submitted":"Worker-folder write restriction: reviewer must apply the inbox diff after review.",
 "served_model_evidence":{"author":"UNAVAILABLE: response-side served-model identity not exposed","referee":"UNAVAILABLE: review pending"}}
ROOT.joinpath("SUBMISSION_STATE.json").write_text(json.dumps(states,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"claims":len(claims),"draft_entries":len(entries),"relations":len(relations),"checks":receipt["cases"],"state":"prepared; not ingested"}))
