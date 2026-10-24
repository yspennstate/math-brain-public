"""Bind the final peer revisions and save the first-order correction once."""
import json
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import os
import sqlite3

BASE = Path(__file__).resolve().parent
def save(name, obj):
    (BASE / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

for worker in ["w360", "w361"]:
    dest = BASE / "peer_snapshots" / worker
    dest.mkdir(parents=True, exist_ok=True)
    for name in ["CLAIMS.jsonl", "ATTEMPT.md", "INDEPENDENT_OBSTRUCTION.md"]:
        origin = Path("~/brain_workers") / worker / name
        if origin.exists():
            (dest / name).write_bytes(origin.read_bytes())

reviews = [json.loads(x) for x in (BASE/"PEER_REVIEWS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
for row in reviews:
    if row["review_id"] == "w362-R004":
        row.update({"prior_verdict": "KEEP on the conditional implication", "verdict": "FIX", "scope": "Infeasible full-kernel decay premise in the provisional proof route", "reproduction": "Finite orthogonal expansion gives the unweighted kernel H(t)>=L=sum_{|S|=1}||f_S||^2. If L>0, H(t)<=C n F(n^(1/3)t) for every t forces F to be bounded below by L/(Cn), contradicting integrability. The independent square calculation has L=1/4. FIRST_ORDER_FLOOR_AUDIT.md checks the correction. The earlier conditional algebra was valid, but the input neglected this persistent term.", "fix": "Bound L_n separately and apply the integrable envelope to R_n(t)=H_n(t)-L_n. Retain a uniform lower persistence interval. The revised implication is reviewed in R008.", "remaining_gap": "The first-order bound, remainder envelope, and persistence inputs are all unproved. No parent solution.", "status": "independently checked proof"})

new = [
 {"review_id": "w362-R005", "reviewer": "w362", "author": "w361", "claim_id": "w361-C002", "verdict": "KEEP", "scope": "Tie-free finite square counterexample", "source_path": "peer_snapshots/w361/INDEPENDENT_OBSTRUCTION.md", "reproduction": "For iid Exp(1) edges, the competing sum has survival exp(-s)(1+s), and selection probability is 1/2. Conditional density is 2 exp(-2(x+y))(1+x+y). With I_k=k!/2^(k+1), each mean is 2(I1 I0+I2 I0+I1 I1)=5/8 and the product moment is 2(I1^2+2 I2 I1)=3/8. Covariance is 3/8-25/64=-1/64. The continuous path sums tie with probability zero.", "remaining_gap": "This finite example does not give a planar asymptotic exponent; uniqueness only fails to restore the asserted independence.", "status": "independently checked proof"},
 {"review_id": "w362-R006", "reviewer": "w362", "author": "w361", "claim_id": "INDEPENDENT_OBSTRUCTION.md exact repair premise", "verdict": "KEEP", "scope": "Conditional independence criterion", "source_path": "peer_snapshots/w361/INDEPENDENT_OBSTRUCTION.md", "reproduction": "For independent U,V and event E with P(E)=Z>0, use the defined conditional selection likelihood w(u,v). The selected joint density relative to mu times nu is w/Z; marginal densities are a/Z and b/Z, where a and b are the two stated integrals. Independence is exactly w/Z=ab/Z^2, hence w=ab/Z almost everywhere. The discrete likelihood matrix must have rank one. For the square its counts matrix determinant is 4*1-3*3=-5, so it fails.", "remaining_gap": "A proposed selected-path factorization must establish this premise under its own actual selection event; iid original weights alone do not establish it.", "status": "independently checked proof"},
 {"review_id": "w362-R007", "reviewer": "w362", "author": "w361", "claim_id": "w361-C004", "verdict": "KEEP", "scope": "First-order floor and impossibility of the provisional envelope", "source_path": "peer_snapshots/w361/ATTEMPT.md", "reproduction": "Multiply the independently derived weighted energy sum by exp(t) and separate |S|=1. This gives H(t)=L+R(t), R>=0, and Var=L+integral exp(-t)R. REFEREE_RECEIPT.json independently yields square masses 1/4,3/32,0,1/64, hence L=1/4 and R=(3/16)exp(-t)+(1/16)exp(-3t). H>=L>0 makes an integrable all-time full-kernel envelope impossible.", "remaining_gap": "The identity gives no asymptotic bound on L_n or R_n and no crossover scale.", "status": "independently checked proof"},
 {"review_id": "w362-R008", "reviewer": "w362", "author": "w361", "claim_id": "w361-C005", "verdict": "KEEP", "scope": "First-order-corrected conditional implication only", "source_path": "peer_snapshots/w361/ATTEMPT.md", "reproduction": "Assume L_n<=C n^(2/3), R_n(t)<=C n F(n^(1/3)t) with nonnegative integrable F, and H_n(t)>=c n on [0,c' n^(-1/3)], all uniform in n. The separated identity and substitution give upper bound C n^(2/3)(1+integral F). The persistence interval gives lower bound c c' exp(-c')n^(2/3). Both quantifiers and the retention factor are correct.", "remaining_gap": "All three quantitative hypotheses remain unproved; this is not a theorem establishing the lattice exponent.", "status": "independently checked proof"}
]
seen = {r["review_id"] for r in reviews}
reviews.extend(r for r in new if r["review_id"] not in seen)
(BASE/"PEER_REVIEWS.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in reviews), encoding="utf-8")

receipt = json.loads((BASE/"REFEREE_RECEIPT.json").read_text(encoding="utf-8"))
mass = {int(k): F(v) for k,v in receipt["spectral_variance_mass_by_order"].items()}
assert mass[1] == F(1,4)
assert 2*mass[2] == F(3,16) and 4*mass[4] == F(1,16)
assert mass[1]+sum((mass[k] for k in mass if k>=2),F(0)) == F(23,64)
save("FLOOR_RECEIPT.json", {"proof_reproduction_source": "REFEREE_RECEIPT.json", "first_order_energy": "1/4", "unweighted_remainder": "(3/16)exp(-t)+(1/16)exp(-3t)", "variance": "23/64", "spectral_coefficients_match": True, "recomputed_lattice_experiments": 0, "mathematical_proof": "FIRST_ORDER_FLOOR_AUDIT.md", "scope": "Finite binary square and the conditional spectral reduction only"})

namespace = "probability.first-passage-percolation"
source = {"source_id": "owner-own-work:w361:p0104:first-order-correction", "url": "file:///~/brain_workers/w361/ATTEMPT.md", "revision": "as-checked-2026-10-10-first-order-corrected", "license": "owner-own-work", "excerpt": None}
entries = [
 {"key": "first-order-floor", "namespace": namespace, "logical_name": "independent-refresh-unweighted-energy-first-order-floor", "kind": "lemma", "title": "Unweighted refresh energy has a first-order spectral floor", "statement": "For a square-integrable function f of finitely many independent coordinates, let f_S be its orthogonal coordinate-average product projections. Refresh each coordinate independently at rate one, and set C_f(t)=Cov(f(W),f(W^t)), E_f(t)=-C_f'(t), and H_f(t)=exp(t)E_f(t). Then L=sum_{|S|=1}||f_S||_2^2 is the limit of H_f(t), R_f(t)=H_f(t)-L=sum_{|S|>=2}|S|exp(-(|S|-1)t)||f_S||_2^2 is nonnegative, and Var(f)=L+integral_0^infinity exp(-t)R_f(t)dt. If L>0, no bound H_f(t)<=A F(Bt) for all t>=0 can hold with finite positive A,B and a nonnegative integrable F. The weighted energy E_f itself tends to zero; the floor concerns the unweighted convention only.", "proof_text": "The independent refresh operator multiplies each f_S by exp(-|S|t), and orthogonality gives C_f(t)=sum_{S nonempty}exp(-|S|t)||f_S||^2. Differentiate the finite sum, multiply by exp(t), and separate |S|=1. Integrating the remaining terms gives their squared norms. If the proposed envelope held with L>0, then F(s)>=L/A for all s>=0, contradicting integrability. Independently rederived by w362; its exact square reproduction has L=1/4 and variance 23/64.", "assumptions": ["finite independent product coordinates", "f in L2", "independent rate-one refresh", "L>0 for the impossible-envelope assertion"], "domain": "probability, resampling, first-passage-percolation proof auditing", "source": source},
 {"key": "corrected-crossover", "namespace": namespace, "logical_name": "planar-fpp-first-order-separated-crossover-unproved-input-route", "kind": "concept", "title": "DRAFT: separate first-order energy in the FPP crossover route", "statement": "For iid Uniform[1,2] undirected nearest-neighbor Z^2 FPP, T_n=T(0,n e1), let the UNWEIGHTED refresh kernel be H_n(t)=exp(t)(-C_n'(t)), L_n its first-order spectral limit, and R_n=H_n-L_n. A sufficient conditional route to variance comparable to n^(2/3) is: L_n<=C n^(2/3); R_n(t)<=C n F(n^(1/3)t) for every t>=0 with one nonnegative integrable F; and H_n(t)>=c n for 0<=t<=c' n^(-1/3). Constants are independent of n. The separated variance identity gives upper bound C n^(2/3)(1+integral F) and lower bound c c' exp(-c') n^(2/3). ALL THREE quantitative inputs remain unproved. The earlier all-time integrable envelope on the full unweighted H_n ignores a positive first-order floor and is infeasible; do not promote this corrected conditional route into a proof of its inputs or a solution of P0104.", "proof_text": None, "assumptions": ["the specified bounded planar FPP model", "all three unproved crossover inputs with uniform constants"], "domain": "probability, first-passage percolation, draft conditional proof route", "source": source}
]
relations = [{"from_key": "corrected-crossover", "to_key": "first-order-floor", "kind": "depends_on", "rationale": "The route explicitly uses 'L_n its first-order spectral limit, and R_n=H_n-L_n'; the lemma supplies 'Var(f)=L+integral_0^infinity exp(-t)R_f(t)dt'. This separation repairs the impossible full-unweighted-kernel envelope; the quantitative inputs remain unproved."}]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w362", "bundle_slug": "p0104-first-order-correction-20261010", "entries": entries, "relations": relations}
save("bundle_floor_local.json", bundle)
floor_receipt_path = BASE/"FLOOR_BUNDLE_RECEIPT.json"
if not floor_receipt_path.exists():
    inbox = Path("~/math-brain-inbox/w362").resolve()
    number = 1
    while (inbox/f"bundle_{number:03}.json").exists() or (inbox/f"bundle_{number:03}.json.part").exists():
        number += 1
    dest = inbox/f"bundle_{number:03}.json"
    part = inbox/f"bundle_{number:03}.json.part"
    assert dest.parent.resolve()==inbox and part.parent.resolve()==inbox
    with part.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n")
        handle.flush(); os.fsync(handle.fileno())
    part.rename(dest)
    assert json.loads(dest.read_text(encoding="utf-8"))==bundle
    save("FLOOR_BUNDLE_RECEIPT.json", {"path": str(dest), "entries": 2, "relations": 1, "submitted": True, "reviewed": "w361-C004 and C005 independently checked by w362-R007/R008; secondary login gate not claimed", "ingested": "NOT_VERIFIED", "retrievable": "NOT_VERIFIED", "live_store_writes": 0, "submission_time_utc": datetime.now(timezone.utc).isoformat()})

with (BASE/"RELATION_EVIDENCE.jsonl").open("a", encoding="utf-8") as handle:
    rel=relations[0]
    handle.write(json.dumps({**rel,"bundle":"p0104-first-order-correction-20261010","from_statement":entries[1]["statement"],"to_statement":entries[0]["statement"],"status":"draft for coordinator audit"},ensure_ascii=False)+"\n")

c=sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",uri=True,timeout=5)
original=json.loads((BASE/"bundle_local.json").read_text(encoding="utf-8"))
store_rows={}
for e in original["entries"]+entries:
    logical="math:"+e["namespace"]+":"+e["logical_name"]
    result=c.execute("SELECT id,title,body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchall()
    store_rows[logical]={"matches":len(result),"matching_statement":any(body==e["statement"] for _,_,body in result)}
c.close()
save("SUBMISSION_STORE_PRESENCE.json", {"checked_utc":datetime.now(timezone.utc).isoformat(),"read_only":True,"results":store_rows,"recall_engine_retrieval_tested":False})

progress=json.loads((BASE/"PROGRESS_EVENT.json").read_text(encoding="utf-8"))
progress["event"]="P0104 referee: source and 16/16 checks complete; 7 KEEP and 1 FIX; first-order floor corrected; 6 draft entries submitted; crossover unproved."
save("PROGRESS_EVENT.json",progress)
print(json.dumps({"peer_verdicts":{v:sum(r["verdict"]==v for r in reviews) for v in ["KEEP","FIX","DROP"]},"original_draft_entries":4,"floor_draft_entries":2,"floor":"1/4","parent_solved":False,"store_presence":store_rows},indent=2))
