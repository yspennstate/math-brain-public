"""Prepare a small review-only bundle; submit only to this worker's leased inbox file."""
import argparse
from datetime import datetime, timezone
import difflib
import json
from pathlib import Path
import subprocess
import sys

folder = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--submit", action="store_true")
args = parser.parse_args()

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

source_path = folder / "SOURCE_STATUS.json"
status = json.loads(source_path.read_text(encoding="utf-8"))
original_url = "https://arxiv.org/html/2603.29571v1"
if not any(source["url"] == original_url for source in status["primary_sources"]):
    status["primary_sources"].insert(1, {
        "url":original_url,
        "arxiv":"2603.29571v1",
        "authors":"Bandeira, Dmitriev, Lucca, Nizic-Nikolac, Rodder (Entry 13 by Rodder)",
        "location":"Entry 13, Definition 13.1 and Conjecture 30",
        "role":"Exact primary reference named by op-p0017 intake",
        "observed_statement":"For every dimension and log-concave measure, h(mu)>=c/sqrt(||Cov(mu)||_op); in isotropic position h(mu)>=c. Cheeger uses boundary/min(mass,1-mass).",
        "verification":"Primary displayed covariance formulation and Poincare formulation checked; current-status commentary dates from March 2026."
    })
status["primary_sources"][0]["role"] = "Original geometric source; Section 4 defines mean-zero covariance-identity isotropy and Section 5 conjectures that a hyperplane cut is within a universal factor of the optimal cut."
status["exact_cheeger_target"] = "There exists c>0, independent of n and mu, such that every isotropic log-concave probability measure on R^n has h(mu)>=c. Here h is inf over 0<mu(A)<1 of mu^+(A)/min(mu(A),1-mu(A)), with outer Euclidean Minkowski boundary (lower limit when necessary). The cited covariance-scaled statement is h(mu)>=c/sqrt(||Cov(mu)||_op)."
status["owner_solved_retired_check"] = {
    "scope":"Targeted exact-ID/title searches in the named intake directories, H/I attempts, Lean annotations, then matching current store nodes opened read-only.",
    "original_problem_record":"brain_bundle_C006p01.json: op-p0017; current status explicitly unverified; source Randomstrasse101 Conjecture 30, Entry 13.",
    "prior_attempt_record":"brain_bundle_C006a04.json: at-p0017; Gaussian Hermite expansion special case only, no independent review, no full-target claim.",
    "H_I_attempts":"No matching P0017 ID/title found in the two named directories by targeted rg.",
    "lean_annotation":"RANKED_LIST_2026-09-07_annotated.md line 598 records attempted_un; no formal-check receipt was identified.",
    "store":"file:~/math-brain-build/local/population/brain.sqlite3?mode=ro, PRAGMA query_only=ON; only the original unverified problem and Gaussian-attempt records matched the bounded query.",
    "limitation":"This bounded check does not prove absence of every owner solution elsewhere."
}
status["recall"] = {"receipt":"RECALL_RECEIPT.json","timeout_seconds":60,"observed_elapsed_seconds":74.58142450009473,"fallback_index":"No targeted KLS/Poincare match found in MEMORY.md","scar_read":"perceptron_proof_open_gaps_fleet_2026_07_12","application":"Arithmetic/status success does not establish the hardest unverified proof step."}
save_json(source_path, status)

def own_source(slug, artifact):
    return {"source_id":"owner-own-work:w355:"+slug,"url":"urn:probability-research:20261010:w355:"+artifact,"revision":"unreviewed-2026-10-10-v1","license":"owner-own-work (campaign derivation; independent review pending)","excerpt":None}

bundle = {
    "spec":"mathbrain-draft-v1",
    "author_agent":"w355",
    "bundle_slug":"p0017-simplex-weighted-slice-boundary-w355-001",
    "entries":[
        {
            "key":"p0017-status",
            "namespace":"probability.concentration",
            "logical_name":"p0017-kls-primary-resolution-claims-october-2026",
            "kind":"concept",
            "title":"P0017: October primary resolution claims require a current proof audit",
            "statement":"As checked on 2026-10-10, P0017 asks for a universal C_P bound for all centered covariance-identity log-concave probabilities in every dimension, equivalently a universal positive Euclidean Cheeger lower bound. Its cited source is Randomstrasse101, arXiv:2603.29571v1, Entry 13, Conjecture 30. arXiv:2610.05474v1 (2026-10-04), Theorem 1.1, announces the full Poincare bound; arXiv:2610.07728v2 (2026-10-08 revision) announces C_P<=25. This card records primary announcements only: mathematical validity and current openness have not been independently settled in this packet. The September attempted-unsolved label is dated provenance, not a current-openness certificate.",
            "proof_text":None,
            "assumptions":["Source-status observation dated 2026-10-10; not a mathematical validation of the announced proofs."],
            "domain":"probability theory",
            "source":own_source("p0017-source-status","SOURCE_STATUS.json")
        },
        {
            "key":"simplex-fibers",
            "namespace":"probability.concentration",
            "logical_name":"isotropic-regular-simplex-conditional-poincare-extremes",
            "kind":"concept",
            "title":"DRAFT: isotropic regular simplex has rare long conditional fibers",
            "statement":"Unreviewed independent derivation: for n>=2 work on H={x in R^(n+1):sum x_i=0} with its Euclidean metric, and take X uniform on vertices v_i=sqrt((n+1)(n+2))(e_i-1/(n+1)). Covariance on H is identity. Put u=(e_0-e_1)/sqrt(2), T=<X,u>, Y=X-Tu and S=lambda_0+lambda_1 in barycentric coordinates. Conditional on Y, T is uniform on an interval of length sqrt(2(n+1)(n+2)) S, and S~Beta(2,n-1). Thus ess sup conditional C_P=2(n+1)(n+2)/pi^2, mean conditional C_P=12/pi^2, ess sup conditional variance=(n+1)(n+2)/6 and mean conditional variance=1. Cheeger uses boundary/min(mass,1-mass): ess inf conditional h=sqrt(2/((n+1)(n+2))). Near-extremal fibers have positive marginal probability: P(S>1-delta)=delta^(n-1)[n-(n-1)delta] for 0<delta<1. This blocks transferring global isotropy to a uniform conditional bound; it is not a KLS refutation or novelty claim.",
            "proof_text":None,
            "assumptions":["Euclidean metric on H; n>=2; orthogonal conditioning onto u-perp; marginal-almost-everywhere conditional laws.","C_P uses variance/Dirichlet energy; h uses boundary/min(mass,1-mass).","Independent referee check pending; proof in ATTEMPT.md sections 2-4."],
            "domain":"probability theory",
            "source":own_source("p0017-simplex-fibers","ATTEMPT.md#sections-2-4")
        },
        {
            "key":"weighted-slice-energy",
            "namespace":"probability.concentration",
            "logical_name":"conditional-poincare-constant-average-cannot-separate-from-energy",
            "kind":"concept",
            "title":"DRAFT: unweighted average slice constants do not control directional energy",
            "statement":"Unreviewed independent counterexample: for each n>=2 let X be uniform on the covariance-identity regular simplex in sum-zero R^(n+1), with vertices sqrt((n+1)(n+2))(e_i-1/(n+1)). For u=(e_0-e_1)/sqrt(2), T=<X,u>, Y=X-Tu, and barycentric S=lambda_0+lambda_1, the conditional law of T is uniform of length sqrt(2(n+1)(n+2)) S. Set f=T(S-1/2)_+^2, a C1 function. Then E[f|Y]=0, partial_u f=(S-1/2)_+^2, and E Var(f|Y)/E|partial_u f|^2>(n+1)(n+2)/24, while mean conditional C_P=12/pi^2. Hence no universal directional conditional-variance bound follows by taking the unweighted average of slice constants. The valid slice estimate keeps C_P(T|Y) times conditional directional energy inside one expectation. Transverse derivatives and the conditional-mean variance require separate control in a full-gradient argument. This refutes only the stronger auxiliary bridge, not KLS; no novelty claim.",
            "proof_text":None,
            "assumptions":["n>=2; original Euclidean metric; conditional laws as in the stated simplex construction.","Only directional-u energy is used in the disproved bridge; full gradient energy is not being bounded or disproved.","Independent referee check pending; proof in ATTEMPT.md section 5."],
            "domain":"probability theory",
            "source":own_source("p0017-weighted-slice-energy","ATTEMPT.md#section-5")
        }
    ],
    "relations":[
        {"from_key":"weighted-slice-energy","to_key":"simplex-fibers","kind":"depends_on","rationale":"The displayed test ratio uses exactly the simplex fiber distribution, its affine S(Y), and conditional variance from the other entry."},
        {"from_key":"simplex-fibers","to_existing_logical":"math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant","kind":"cites","rationale":"The existing node asks for a universal positive lower bound for the Euclidean Cheeger constant of every isotropic log-concave probability measure. This entry checks a stronger conditional bridge and explicitly preserves the original target."},
        {"from_key":"p0017-status","to_existing_logical":"math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant","kind":"cites","rationale":"The existing dated node explicitly says current status unverified; the new entry supplies later primary announcements without certifying them."}
    ]
}

required_entry = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
required_source = {"source_id","url","revision","license"}
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"]) <= 200
for entry in bundle["entries"]:
    assert required_entry <= entry.keys()
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert required_source <= entry["source"].keys()
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["assumptions"]
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert relation["kind"] in {"depends_on","cites"}
    assert relation.get("to_key") in keys or "to_existing_logical" in relation
local_draft = folder / "drafts" / "bundle_001.json"
save_json(local_draft, bundle)

hook = {
    "id":"conditional-slice-w355-01","area":"math","event":"stage-start",
    "cue":"A proof transfers global isotropy to a uniform conditional Poincare/covariance bound, or separates an unweighted average slice constant from its energy.",
    "fire_when":"The isotropic simplex bridge E Var(f|Y)<=E[C_P(T|Y)] E|partial_u f|^2 is asserted for f=T(S-1/2)_+^2.",
    "silent_when":"The proof retains E[C_P(T|Y) E(|partial_u f|^2|Y)] and explicitly controls the transverse and conditional-mean terms.",
    "text":"Global isotropy controls average conditional covariance, not every fiber. Keep a conditional Poincare constant inside its energy-weighted integral; test an isotropic simplex before using a uniform or unweighted-average slice bound.",
    "evidence":"~/brain_workers/w355/VERIFICATION.json; 5898 exact checks; n64 directional ratio 206.5366289 vs mean slice Cp 1.2158542; ATTEMPT.md C002.",
    "proposer":"w355"
}
assert len(hook["text"]) <= 300
hook_line = json.dumps(hook, ensure_ascii=False) + "\n"
(folder / "HOOK_PROPOSAL.jsonl").write_text(hook_line, encoding="utf-8")
live_hook = Path("~/primary_directive/hooks1000/proposals/math-w355.jsonl")
old_hook = live_hook.read_text(encoding="utf-8") if live_hook.exists() else ""
new_hook = old_hook + hook_line if hook["id"] not in old_hook else old_hook
patch = "".join(difflib.unified_diff(old_hook.splitlines(keepends=True),new_hook.splitlines(keepends=True),fromfile="a/"+live_hook.as_posix(),tofile="b/"+live_hook.as_posix()))
(folder / "patches").mkdir(exist_ok=True)
(folder / "patches" / "01_probability_slice_hook.diff").write_text(patch, encoding="utf-8")

states = {"prepared":True,"submitted":False,"reviewed":False,"ingested":False,"retrievable":False,"entry_count":3,"entry_kind":"concept","local_draft":str(local_draft),"reviewer":"w356","review_state":"pending","hook_state":"local proposal and reviewer patch only","coordinator_live_integration_run":False}
if args.submit:
    inbox = Path("~/math-brain-inbox/w355").resolve()
    destination = inbox / "bundle_001.json"
    claim_command = [sys.executable,"-X","utf8","-B","~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py","assert","--agent","w355","--resource",str(destination)]
    claim_check = subprocess.run(claim_command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    save_json(folder / "BUNDLE_CLAIM_ASSERT.json",{"command":claim_command,"returncode":claim_check.returncode,"stdout":claim_check.stdout,"stderr":claim_check.stderr})
    if claim_check.returncode:
        raise RuntimeError("Inbox mutation refused: covering mesh claim assertion failed")
    inbox.mkdir(parents=True, exist_ok=True)
    partial = inbox / "bundle_001.part"
    assert partial.resolve().parent == inbox == destination.resolve().parent
    content = local_draft.read_text(encoding="utf-8")
    if destination.exists():
        if destination.read_text(encoding="utf-8") != content:
            raise FileExistsError("Existing draft differs; preserve it")
    else:
        with partial.open("x", encoding="utf-8") as handle:
            handle.write(content)
        partial.rename(destination)
    states.update({"submitted":True,"submitted_at":datetime.now(timezone.utc).isoformat(),"inbox_draft":str(destination)})
save_json(folder / "BUNDLE_STATES.json",states)
save_json(folder / "BUNDLE_VALIDATION.json",{"result":"PASS","entries":3,"relations":3,"source_tag":"owner-own-work","proof_text_for_concepts":None,"depends_on_cycle":False,"live_store_write":False,"schema_check_only":True})
print(json.dumps({"states":states,"schema":"PASS","hook_text_length":len(hook["text"])}, indent=2))
