"""Save review verdicts and a proposed source correction, only in w514."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PEER=Path("~/brain_workers/w513")

def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    peer=[json.loads(line) for line in (PEER/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    rows=[]
    reasons={"L1":"Independently derived normalized paired-spectrum entropy identity; Delta=B+JS, not B.",
             "L2":"Independent scalar divergence proof and signed-coefficient factor confirm 2/ln2 and the retained logarithmic loss.",
             "L3":"Independent Boolean core and paired marginal bound confirm the stated lower bound, including m=2.",
             "L4":"Disjoint balanced block factorization, fixed alpha after tau, and empty-selector sector supply the required independence and quantifiers.",
             "L5":"Finite complete history-based restriction trees telescope with weights 2^-depth and zero constant leaves.",
             "L6":"Independent balanced-composition entropy/influence laws and majority recurrences confirm all-small influences, bad selector, and global H<=4I simultaneously."}
    for row in peer:
        suffix=row["id"].rsplit("-",1)[-1]
        if suffix not in reasons:
            continue
        rows.append({"id":"w514-audit-"+row["id"],"claim_id":row["id"],"verdict":"KEEP","reviewer":"w514",
                     "exact_statement_reviewed":row["statement"],"assumptions_reviewed":row["assumptions"],
                     "why":reasons[suffix],"independent_derivation":"AUDIT_W513.md", "diagnostics":"adversary_checks.json",
                     "status":"independently checked proof","scope":"Mathematical adversary check of this exact partial-result statement; final w515 referee check pending; no formal verification",
                     "remaining_gap":row["remaining_gap"]})
    assert len(rows)==6
    (ROOT/"AUDIT_W513.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")

    snapshots=ROOT/"review_sources"
    snapshots.mkdir(exist_ok=True)
    for filename in ("BRIDGE_CHECKPOINT.md","ENTROPY_BOUND.md","SMALL_INFLUENCE_OBSTRUCTION.md","FAMILY_FEI4.md"):
        path=PEER/filename
        assert path.stat().st_size<=16000,"Unexpectedly large peer proof; targeted read needed"
        (snapshots/filename).write_text(path.read_text(encoding="utf-8"),encoding="utf-8")
    (snapshots/"CLAIMS_at_review.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in peer if row["id"].rsplit("-",1)[-1] in reasons),encoding="utf-8")

    correction={"id":"w514-C006","target":"P0162","exact_statement":"For a nonconstant Boolean f under uniform cube measure, define delta=max_i I_i(f)>0 and rho_0(f)=min_{i:I_i(f)>0} Delta_i(f)/I_i(f), with base-2 Fourier entropy increment. Then rho_0(f)<=(1+h_2(delta))/delta. Reading delta as uniform input-coordinate bias makes that assertion false: AND_3 has rho_0=3+(9/4)log_2(16/9)>4 although every input coordinate has bias 1/2.",
                "assumptions":["Nonconstant Boolean f","Uniform measure","Base-2 entropy","delta is maximal flip influence, not input bias","Minimum excludes zero-influence coordinates"],
                "source":{"type":"owner-own-work source correction","artifact":"CORRECTION.md","existing_card":"claim_dc05672a84f74b44a1f15207c0cf86e0","source_memory":"fei_step_constant_lower_bound_ceiling_and_descent_witness_2026_09_21","source_quote":"delta = max_i Inf_i"},
                "proof":"Delta_i=JS_2+B_i<=1+h_2(I_i). Choose a maximal-influence coordinate and use the minimum defining rho_0. AND_3's Fourier atom masses 9/16 and seven copies of 1/16, with child average entropy 1 and influence 1/4, give the exact counterexample to the input-bias reading.",
                "independent_reviewer":"w515; Claude reviewer claude-4a88bc43 for the theorem-hypothesis correction (pending)",
                "remaining_gap":"This corrects one transported hypothesis only; preserves the card's provisional status and leaves unrelated numerical record assertions unreviewed.",
                "status":"proved special case","review_state":"unreviewed","numerical_evidence":"adversary_checks.json","novelty":"not new; exact cited-source repair"}
    claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    if not any(row["id"]==correction["id"] for row in claims):
        claims.append(correction)
    (ROOT/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims),encoding="utf-8")
    write("NODE_CORRECTION.json",{"state":"DRAFT; not applied","reviewer":"claude-4a88bc43 with independent mathematical check by w515",
                                 "claim_id":"claim_dc05672a84f74b44a1f15207c0cf86e0","operation":"canonical source-backed assumption correction after review; preserve all other content/status",
                                 "old_assumption":"h the binary entropy function; delta the restricted coordinate's bias",
                                 "new_assumption":"h is base-2 binary entropy; f is nonconstant Boolean under uniform measure; delta=max_i I_i(f)>0; rho_0=min over coordinates with positive I_i of Delta_i/I_i",
                                 "source_memory":correction["source"]["source_memory"],"source_quote":"delta = max_i Inf_i","proof_artifact":"CORRECTION.md","counterexample":"AND_3: rho_0=4.867668746754797 versus wrong ceiling 4 if delta=1/2 input bias"})
    source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
    source["independent_before_paired_proof"]={"artifacts":["INDEPENDENT.md","BENT_SELECTOR.md"],"paired_proof_read_when_saved":False}
    source["paired_access"]={"independent_first":["INDEPENDENT.md","BENT_SELECTOR.md"],"proof_available_at_initial_read":False,
                             "proof_available_at_later_read":True,"proofs_read":["BRIDGE_CHECKPOINT.md","ENTROPY_BOUND.md","SMALL_INFLUENCE_OBSTRUCTION.md","FAMILY_FEI4.md"],
                             "audit_verdicts":"AUDIT_W513.jsonl","audited_claims":6,"verdict":"KEEP under stated assumptions; independent final referee pending"}
    write("SOURCE_STATUS.json",source)
    diagnostic=json.loads((ROOT/"RETRIEVAL_FAILURE.json").read_text(encoding="utf-8"))
    diagnostic["additional_concrete_failure"]={"card":"claim_dc05672a84f74b44a1f15207c0cf86e0","field":"assumptions.delta",
                                              "source_parameter":"maximal influence","transported_description":"restricted coordinate's bias",
                                              "counterexample":"AND_3 has rho0=4.867668746754797 >4 from interpreting delta as input bias 1/2",
                                              "bounded_repair":"Replace this single assumption with the explicit source definition; retain provisional verification status","artifact":"NODE_CORRECTION.json"}
    write("RETRIEVAL_FAILURE.json",diagnostic)
    with (ROOT/"PEER_OUTBOX.jsonl").open("a",encoding="utf-8") as out:
        out.write(json.dumps({"from":"w514","to":["w513","w515"],"kind":"done","target":"P0162","body":"Independent derivation and adversary review complete: KEEP w513 L1-L6 under disjoint/balanced block and complete-tree premises. BENT_SELECTOR.md strengthens the bad-coordinate lower bound and SHARP_COORDINATE_BOUND.md proves optimal additive 3/ln2 in the logarithmic bound. AUDIT_W513.md and REVIEW_PACKET.md contain exact checks; full FEI gap remains the aggregate conditional-entropy budget.","artifact":"~/brain_workers/w514/AUDIT_W513.md","delivery_state":"staged locally; shared messaging forbidden by worker write restriction"})+"\n")
        out.write(json.dumps({"from":"w514","to":["claude-4a88bc43"],"kind":"review","target":"P0162","body":"The recalled step-ceiling card's delta assumption differs from its cited source. Source requires delta=max_i Inf_i, while transported text says coordinate bias. AND_3 gives rho0=4.86767>4 for the wrong input-bias interpretation. Exact one-field correction and proof in NODE_CORRECTION.json/CORRECTION.md; leave unrelated record numbers and provisional status unchanged.","artifact":"~/brain_workers/w514/NODE_CORRECTION.json","delivery_state":"staged local review request"})+"\n")
    progress=json.loads((ROOT/"PROGRESS_EVENT.json").read_text(encoding="utf-8"))
    progress["event"]="P0162 w514 completed: sharp coordinate-cost proof, six KEEP peer verdicts, source-backed delta correction (AND3 counterexample), five draft nodes/edges and gated checks; ready for independent review."
    write("PROGRESS_EVENT.json",progress)
    print(json.dumps({"own_claims":len(claims),"peer_KEEP_verdicts":len(rows),"source_correction":"DRAFT; not applied","bundle_submitted":False}))

if __name__=="__main__":
    main()
