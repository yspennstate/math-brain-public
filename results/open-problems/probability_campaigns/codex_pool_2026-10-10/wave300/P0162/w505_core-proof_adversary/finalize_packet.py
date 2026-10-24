"""Save final review receipts, source state, and a fresh reviewed-obstruction draft."""
from __future__ import annotations
import difflib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INBOX=Path("~/math-brain-inbox/w505").resolve()
now=datetime.now(timezone.utc).isoformat()
def save(name, obj):
    (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

metrics=json.loads((ROOT/"measurements.json").read_text(encoding="utf-8"))
assert metrics["complete"]
peer=Path("~/brain_workers/w504/PROOF.md")
proof=peer.read_text(encoding="utf-8")
(ROOT/"W504_PROOF_SNAPSHOT.md").write_text(proof, encoding="utf-8")
old="Its other three control blocks each have coefficients -2t."
new="For control Walsh indices (partner,z)=(1,0),(0,1),(1,1), the other three blocks have coefficients -2t,+2t,+2t, respectively; their squares are all 4t^2."
assert old in proof
patched=proof.replace(old,new,1)
patchdir=ROOT/"patches"
patchdir.mkdir(exist_ok=True)
diff="".join(difflib.unified_diff(proof.splitlines(keepends=True),patched.splitlines(keepends=True),fromfile="a/~/brain_workers/w504/PROOF.md",tofile="b/~/brain_workers/w504/PROOF.md"))
(patchdir/"01_w504_control_signs.diff").write_text(diff,encoding="utf-8")
receipts=[json.loads(line) for line in Path("~/brain_workers/w506/CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
receipt=next(r for r in receipts if r.get("id")=="P0162-REVIEW-W505-004")
assert receipt["verdict"]=="KEEP"
save("INDEPENDENT_REVIEW.json",{"reviewer":"w506","receipt_path":"~/brain_workers/w506/CLAIMS.jsonl","receipt_id":receipt["id"],"received_at":now,"receipt":receipt,"scope":"Counterexample to all-coordinate restriction induction only; no FEI resolution and no independent keep inferred for other claims."})
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for row in claims:
    if row.get("claim_id")=="w505-C003":
        row["status"]="independently checked proof"
        row["independent_reviewer"]="w506; KEEP P0162-REVIEW-W505-004"
        row["review_receipt"]="INDEPENDENT_REVIEW.json"
        row["remaining_gap"]="No gap remains in this counterexample under its stated assumptions; the universal suitable-coordinate lemma and full FEI are not proved, and novelty is not claimed."
    if row.get("claim_id")=="w505-C007":
        row["proof_or_counterexample"]="Final CPU run completed in "+str(metrics["seconds"])+" seconds; also checked w504's base-coordinate deficit formula on 20 base restrictions. Spectra/influences were exact rational; logarithms floating. Independent referee corroborated m=1..3 selector values separately."
claims.append({"claim_id":"w505-A001","target":"P0162","statement":"w504's exact entropy identity and conditional induction are valid, and the explicit family's base-coordinate bound Delta_j<=2-(n/2)2^-n<4 I_j follows from the exact formula with R(u)=u^2 log_2 u. A literal sign sentence needs correction: the nonzero control-index coefficients are -2t,+2t,+2t, not all -2t.","assumptions":["w504 PROOF.md snapshot saved in W504_PROOF_SNAPSHOT.md","n even >=2","uniform bit Walsh convention","only the explicitly defined quadratic-point-flip family"],"source":"AUDIT_W504.md; W504_PROOF_SNAPSHOT.md sections 1-4","proof_or_counterexample":"Independent transform and Jensen derivation in AUDIT_W504.md; patch fixes coefficient signs without changing squares. Numerical comparison checks 20 base-coordinate restrictions and scalar cases through n=16.","independent_reviewer":"w505 as named adversary; final referee w506 disposition pending for w504 C003/C004","remaining_gap":"The all-small-influence suitable-coordinate lemma is explicitly unproved. This audit does not prove FEI or justify arbitrary restriction closure of the family.","status":"proved special case","kind":"audit_verdict","verdict":"KEEP main conclusions; FIX literal control-block signs"})
(ROOT/"CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in claims),encoding="utf-8")
save("PEER_AUDIT.json",{"target":"P0162","prover":"w504","adversary":"w505","referee":"w506","independent_checkpoint":"ATTEMPT.md saved before paired proof read","audited_snapshot":"W504_PROOF_SNAPSHOT.md","claims_audited":["w504-P0162-C001","w504-P0162-C002","w504-P0162-C003","w504-P0162-C004","w504-P0162-C005"],"verdict":"KEEP mathematical conclusions; FIX harmless control-block sign sentence","details":"AUDIT_W504.md","patch":"patches/01_w504_control_signs.diff","single_hardest_gap":"For all Boolean f with max_i Inf_i<1/16, uniformly choose some positive-influence i with Delta_i<=K_0 Inf_i; no K_0 proof supplied.","independent_review_of_w505_obstruction":"KEEP by w506, receipt P0162-REVIEW-W505-004","next":"Attempt the fixed-tau suitable-coordinate lemma; preserve its unproved status."})
context=json.loads((ROOT/"READONLY_CONTEXT.json").read_text(encoding="utf-8"))
nodes=context["brain"]["named_target_nodes"]
save("SOURCE_STATUS.json",{"target":"P0162","checked_on":"2026-10-10","checked_at":now,"current_openness":"UNKNOWN","reason":"Historical and recent sources state the conjecture; no complete current solved/retired registry or exhaustive October primary-literature verification was available. No novelty claim.","primary_statement_verified":True,"exact_statement":"Exists one finite universal C for every n and every f:{-1,1}^n->{-1,1} under uniform measure: sum_S fhat(S)^2 log_2(1/fhat(S)^2) <= C sum_S |S| fhat(S)^2, with zero summands zero.","primary_sources":[{"url":"https://arxiv.org/pdf/1204.6447","title":"Ryan O'Donnell, Open problems in analysis of Boolean functions","locator":"printed p.5; PDF index 4, FEI statement","role":"Exact primary source named in the canonical P0162 card, verified directly."},{"url":"https://www.cs.cmu.edu/~odonnell/papers/fei.pdf","title":"O'Donnell, Wright, Zhou, The Fourier Entropy-Influence Conjecture for certain classes of Boolean functions","role":"Exact target and uniform Walsh normalization."},{"url":"https://arxiv.org/html/2606.00246v1","role":"2026 primary statement and suitable-coordinate Ansatz 1.1; restricted classes only."},{"url":"https://arxiv.org/html/2609.21563v1","role":"Potapov 2026 plateaued/partially bent results; restricted scope, not a full FEI proof."}],"ranking_record":{"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv","line":553,"tier":5,"prior_status":"attempted_un"},"canonical_named_nodes":[{"id":n["id"],"title":n["title"],"metadata":json.loads(n["metadata_excerpt"])} for n in nodes],"owner_prior_work":{"recall_top_three":["fei_holds_for_linear_threshold_functions_rank_argument_2026_09_23","fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23","fei_plateaued_constant_four_is_potapovs_theorem_not_ours_2026_09_30"],"scars_read":["perceptron_proof_open_gaps_fleet_2026_07_12","proof_steps_need_derived_joint_structure_2026_09_09"],"prior_p0162_attempt":"Uniform singleton probability spectra violate the Boolean convolution identity; entropy/mean cardinality alone is insufficient. Original attempt was author-checked only and is an unverified concept card.","F4_boundary":"Prior summary already records small-influence localization and failed coordinate rules; no novelty inferred.","F0090_boundary":"Percolation-crossing special case, not full P0162; no re-audit of its reviews performed.","H_I_search":"Targeted H/I attempt-directory keyword searches found no additional exact P0162 proof; this is not an exhaustive registry check.","attachment_path":"STUCK recorded for missing proofnet24 path; used named canonical cards instead."},"paired_proof_read":True,"paired_audit":"PEER_AUDIT.json","formal_check":{"performed":False,"receipt":None},"proof_status":"Counterexample only independently kept by w506; full FEI and suitable-coordinate premise unproved."})
bundle=json.loads((ROOT/"DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
bundle["bundle_slug"]="p0162-restriction-quantifier-obstruction-w505-002"
obstruction=next(e for e in bundle["entries"] if e["key"]=="coordinate-obstruction")
obstruction.update(kind="lemma",title="Explicit Boolean obstruction to all-coordinate FEI restriction induction",statement="For every m>=1, let N=2^(2m), u,v be independent uniform vectors in F_2^m, y an independent uniform sign, and F_m(u,v,y)=(-1)^(u dot v)-(1-y)1{u=v=0}. Then F_m is Boolean, its selector influence is I_y=1/N, and its base-2 Fourier restriction deficit satisfies Delta_y(F_m)/I_y>=log_2((2^m-1)^2+1). Consequently there is no finite universal C with Delta_i(f)<=C I_i(f) for every uniform-cube Boolean f and every coordinate i. This does not refute the full FEI conjecture or its sufficient exists-coordinate input; no novelty is claimed.",assumptions=["m is an integer >=1","uniform independent inputs","normalized Walsh coefficients","base-2 Fourier spectral entropy; 0 log 0=0"],proof_text="Write B(u,v)=(-1)^(u dot v), d=1{u=v=0}, and F=(B-d)+y d. At the exceptional point F=y; elsewhere F=B, proving Booleanity. Summing characters over v first gives Bhat(alpha,beta)=2^-m(-1)^(alpha dot beta), while dhat=1/N. For a= Bhat-1/N, b=1/N, r=a^2+b^2, the exact entropy difference of each Fourier pair is r[h_2(b^2/r)+J(2ab/r)], where J(t)=1-h_2((1+t)/2)>=0. This is at least b^2 log_2(r/b^2). For every pair, r/b^2=(sigma 2^m-1)^2+1>=(2^m-1)^2+1. Summing N equal b^2 terms yields I_y=1/N and the claimed deficit lower bound. The lower bound tends to infinity. Independent referee w506 re-derived the Walsh identity and entropy lower bound and filed KEEP in P0162-REVIEW-W505-004; the truth-table check was separate corroboration.")
obstruction["source"]["revision"]="2026-10-10-independent-KEEP-w506-P0162-REVIEW-W505-004"
bundle["relations"].append({"from_key":"coordinate-obstruction","to_existing_logical":"math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence","kind":"semantic_association","rationale":"The checked witness rules out an all-coordinate sufficient route to the exact FEI target; it does not refute the target itself."})
bundle["relations"].append({"from_key":"coordinate-obstruction","to_existing_logical":"math:probability.core:attempt-p0162-fourier-entropy-versus-total-influence","kind":"semantic_association","rationale":"The original P0162 attempt shows the Boolean constraint cannot be dropped; this witness retains Booleanity and pinpoints a different inadequate proof input, arbitrary-coordinate restriction induction."})
text=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
(ROOT/"DRAFT_BUNDLE_REVIEWED.json").write_text(text,encoding="utf-8")
for number in range(2,1000):
    target=INBOX/("bundle_%03d.json"%number)
    part=INBOX/("bundle_%03d.part"%number)
    if not target.exists() and not part.exists():
        break
else:
    raise RuntimeError("No unused inbox slot")
assert target.resolve().is_relative_to(INBOX) and part.resolve().is_relative_to(INBOX)
with part.open("x",encoding="utf-8") as out:
    out.write(text)
os.rename(part,target)
save("BUNDLE_STATE.json",{"prepared":True,"submitted":True,"latest_inbox_path":str(target),"supersedes_draft":"~/math-brain-inbox/w505/bundle_001.json","instruction":"Coordinator should validate this latest draft; retain/skip the older draft without deleting it.","reviewed":False,"review_scope":{"coordinate-obstruction":"independently checked proof, KEEP w506","full_bundle":"coordinator validation pending","remaining concepts":"conjecture/draft or definition; no theorem promotion"},"ingested":None,"retrievable":None,"ingestion_receipt":None,"retrieval_receipt":None,"states_note":"Submission is confirmed; no ingestion or retrieval claim is made without a receipt.","entries":len(bundle["entries"]),"relations":len(bundle["relations"]),"live_store_written":False})
edge_rows=[]
for logical,node_id in [("math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence","claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06"),("math:probability.core:attempt-p0162-fourier-entropy-versus-total-influence","claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba")]:
    node=next(n for n in nodes if n["id"]==node_id)
    edge_rows.append({"row_id":"w505-edge-"+str(len(edge_rows)+1),"relation":"semantic_association","from_logical":"math:combinatorics.boolean_analysis:bent-point-flip-obstruction-to-all-coordinate-fei-induction","from_statement_quote":obstruction["statement"],"to_existing_logical":logical,"to_node":node_id,"to_statement_quote":node["body_excerpt"],"state":"submitted DRAFT relation; coordinator relation audit pending","source":"READONLY_CONTEXT.json named_target_nodes; independently checked C003","independent_reviewer":"w506 checked the source counterexample, not these proposed relation rows"})
(ROOT/"EDGE_EVIDENCE.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in edge_rows),encoding="utf-8")
save("PROGRESS_REQUEST.json",{"event":"w505 P0162: w506 KEEP on explicit Boolean all-coordinate obstruction; paired base-coordinate proof audited with one harmless sign FIX; latest four-entry draft submitted.","agent":"w505","row":"S1.P0162","evidence":"~/brain_workers/w505/REPORT.md","posted":False,"reason":"Worker write-only scope permits its folder and explicitly named draft inbox; progress and global hook/mesh mutations are staged for coordinator."})
print(json.dumps({"checked_counterexample_receipt":receipt["id"],"claims":len(claims),"latest_bundle":str(target),"entries":len(bundle["entries"]),"relations":len(bundle["relations"]),"cross_bundle_relation_rows":len(edge_rows),"final_compute_seconds":metrics["seconds"],"live_store_written":False}))
