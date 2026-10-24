"""Package proved special cases as unreviewed DRAFTs; never invoke the integrator."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w465")
claims = [json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
spec_path = Path("~/math-brain-inbox/BUNDLE_SPEC.md")
assert spec_path.is_file()
name_map = {
    "w465-L1": ("fk-edge-identity", "random-cluster-edge-connection-identity", "FK edge density from deletion connectivity"),
    "w465-L2": ("fixed-cylinder-witness", "monotone-cylinder-total-variation-edge-bound", "Fixed cylinder witness bounds the FK edge gap"),
    "w465-L3": ("pressure-bridge", "potts-fixed-cylinder-pressure-gap-bound", "Conditional Potts pressure gap from a fixed FK witness"),
    "w465-L4": ("vanishing-path-gap", "random-cluster-path-boundary-gap-geometric-decay", "Positive finite FK path boundary gaps vanish in the limit"),
    "w465-L5": ("q3-mf-barrier", "three-state-potts-mean-field-separator-error-obstruction", "Exact q=3 mean-field separator and infrared allowance obstruction"),
}
entries=[]
for claim in claims:
    key,logical,title=name_map[claim["id"]]
    entries.append({"key":key,"namespace":"probability.statmech","logical_name":logical,"kind":"lemma","title":"DRAFT: "+title,"statement":"Proved special case; awaiting independent review. "+claim["statement"],"proof_text":claim["proof"],"assumptions":claim["assumptions"],"domain":"probability theory","source":{"source_id":"owner-own-work:w465:C0048:"+claim["id"],"url":(ROOT/"ATTEMPT.md").as_uri(),"revision":"2026-10-10-unreviewed-draft-v1","license":"owner-own-work","excerpt":None}})
entries.extend([
    {"key":"finite-gap-misstep","namespace":"probability.statmech","logical_name":"finite-random-cluster-boundary-gap-limit-inference-refuted-route","kind":"concept","title":"DRAFT refuted route: finite boundary positivity as a transition certificate","statement":"Refuted inference, not a theorem: positive free/wired marginal differences in every finite volume by themselves imply a bulk first-order transition. The length-L endpoint-wired FK path has positive differences at every L, but for each fixed 0<p<1 and q>1 those differences tend geometrically to zero; its infinite-volume law is iid Bernoulli(p/[p+q(1-p)]). A valid critical-transition bridge needs a fixed-support positive limiting witness or a different argument.","proof_text":None,"assumptions":["Inference is refuted in a path family; this does not refute C0048 on Z^d,d>=3"],"domain":"probability theory","source":{"source_id":"owner-own-work:w465:C0048:finite-gap-misstep","url":(ROOT/"ATTEMPT.md").as_uri(),"revision":"2026-10-10-unreviewed-draft-v1","license":"owner-own-work","excerpt":None}},
    {"key":"critical-witness-gap","namespace":"probability.statmech","logical_name":"potts-c0048-fixed-critical-cylinder-witness-missing-bridge","kind":"concept","title":"DRAFT open bridge: a fixed positive critical Potts boundary witness","statement":"Unproved proof need for C0048, not a theorem: for each integer q>=3 and d>=3 in the zero-field ferromagnetic nearest-neighbor model, find a fixed finite cylinder event A and delta(q,d)>0 with phi^w_{p_c,q}(A)-phi^f_{p_c,q}(A)>=delta. Under a monotone coupling, a witness on M edges would give a common edge-marginal gap at least delta/M, and under the Potts Gibbs/Edwards-Sokal assumptions a pressure slope gap at least d*delta/(p_c*M). The critical wired infinite-cluster conclusion still requires its full argument; no positive witness, critical free-state nonpercolation theorem, or parent-problem solution is supplied by this draft.","proof_text":None,"assumptions":["integer q>=3,d>=3","nearest-neighbor ferromagnetic interactions","zero external field","p_c defined by wired critical percolation","the positive witness is unproved"],"domain":"probability theory","source":{"source_id":"owner-own-work:w465:C0048:critical-witness-gap","url":(ROOT/"ATTEMPT.md").as_uri(),"revision":"2026-10-10-unreviewed-draft-v1","license":"owner-own-work","excerpt":None}}
])
open_logical="math:probability.statmech:open-problem-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3"
attempt_logical="math:probability.statmech:attempt-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3"
relations=[
    {"from_key":"pressure-bridge","to_key":"fixed-cylinder-witness","kind":"depends_on","rationale":"The pressure lemma uses rho>=delta/M from the exact finite-cylinder monotone-coupling bound; the other explicit hypotheses remain necessary."},
    {"from_key":"vanishing-path-gap","to_key":"finite-gap-misstep","kind":"refutes","rationale":"Its complete path formula supplies positive differences at every finite L but zero limiting difference and no infinite cluster for p<1, contradicting the proposed general inference."},
    {"from_key":"critical-witness-gap","to_key":"fixed-cylinder-witness","kind":"semantic_association","rationale":"The concept names the unproved positive critical delta required to use the proved cylinder lemma."},
    {"from_key":"critical-witness-gap","to_key":"pressure-bridge","kind":"semantic_association","rationale":"The proved pressure consequence is conditional on the missing critical witness; this link makes no parent-proof claim."},
    {"from_key":"critical-witness-gap","to_key":"fk-edge-identity","kind":"semantic_association","rationale":"The edge-deletion identity quantifies what a local critical connectivity gap would imply, but supplies no positivity."},
    {"from_key":"critical-witness-gap","to_existing_logical":open_logical,"kind":"semantic_association","rationale":"The checked existing concept is precisely C0048; the new entry is an explicitly unproved bridge for that target."},
    {"from_key":"critical-witness-gap","to_existing_logical":attempt_logical,"kind":"cites","rationale":"The retrieved prior attempt says No result and has no independent review; this draft continues its FK route while preserving the missing critical estimate."},
    {"from_key":"q3-mf-barrier","to_existing_logical":open_logical,"kind":"semantic_association","rationale":"The exact q=3 separator exposes why the published large-d error allowance does not certify this chosen bridge at d=3; it does not settle the conjecture."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w465","bundle_slug":"potts-c0048-fixed-witness-bridge-001","entries":entries,"relations":relations}
assert len(entries)<=200 and all(entry["source"]["license"].startswith("owner-own-work") for entry in entries)
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
for entry in entries:
    assert required<=entry.keys()
    assert entry["kind"] in {"definition","lemma","theorem","concept"}
    assert bool(entry["proof_text"]) if entry["kind"] in {"lemma","theorem"} else entry["proof_text"] is None
keys={entry["key"] for entry in entries}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for relation in relations:
    assert relation["from_key"] in keys and relation["kind"] in allowed
    assert relation.get("to_key") in keys or relation.get("to_existing_logical") in {open_logical,attempt_logical}
serialized=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
local=ROOT/"drafts"
local.mkdir(exist_ok=True)
(local/"bundle_001.json").write_text(serialized,encoding="utf-8")
# The task explicitly names this worker inbox as an authorized output destination.
INBOX.mkdir(exist_ok=True)
destination=INBOX/"bundle_001.json"
if destination.exists():
    assert destination.read_text(encoding="utf-8")==serialized, "preserve a different existing artifact"
else:
    partial=INBOX/"bundle_001.part"
    assert not partial.exists(), "preserve an existing partial artifact"
    partial.write_text(serialized,encoding="utf-8")
    partial.rename(destination)
patches=ROOT/"patches"
patches.mkdir(exist_ok=True)
live=str(destination).replace("\\","/")
diff="".join(difflib.unified_diff([],serialized.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
(patches/"01_potts_fixed_witness_draft.diff").write_text(diff,encoding="utf-8")
state={"artifact":str(destination),"local_copy":str(local/"bundle_001.json"),"status":"DRAFT","submitted":True,"reviewed":False,"ingested":False,"retrievable":False,"integrator_invoked":False,"author_served_model_evidence":"unavailable","review_gate":"w467 or authorized independent referee must issue scoped KEEP; parent proof and promotion gates remain closed","validation":{"entries":len(entries),"relations":len(relations),"required_fields":"PASS","source_license_prefix":"PASS","local_relation_ends":"PASS","single_dependency_edge":"acyclic","cross_bundle_ends":"both checked in the live read-only retrieval snapshot"}}
(ROOT/"SUBMISSION_STATE.json").write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
print(json.dumps(state,indent=2))
