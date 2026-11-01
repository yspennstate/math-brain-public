from __future__ import annotations
import json, re, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def write(name, obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
def own_source(key):
    return {"source_id":"owner:campaign:P0003:w405:"+key,"url":None,"revision":"2026-10-10-draft","license":"owner-own-work","excerpt":None}
def entry(key,kind,title,statement,assumptions,proof=None):
    return {"key":key,"namespace":"probability.saw_bridges","logical_name":"w405-"+key,"kind":kind,"title":title,"statement":statement,"proof_text":proof,"assumptions":assumptions,"domain":"probability theory; self-avoiding walks","source":own_source(key)}
entries=[
entry("finite-restriction","lemma","DRAFT: finite weighted-path restriction and fixed-length counting",
"On a finite embedded graph, weighted vertex-simple marked paths avoiding a closed obstacle have probability Z_deleted/Z_original; conditioning on positive-probability avoidance gives the same weighted law on the deleted graph. For uniform n-step rooted paths, summed over free endpoints, the analogous probability is c_n(deleted)/c_n(original).",
["Graph finite; alternatively locally finite and only fixed-n rooted paths are used","Original path mass or count is positive","Obstacle avoids the marks","Delete every vertex and embedded closed edge trace meeting the obstacle","Surviving path weights and endpoint conventions are unchanged"],
"Surviving paths are exactly avoiding paths, by deletion of both vertices and crossed edges. The correspondence preserves each weight and length. Summing and normalizing proves the ratio and the positive-mass conditional law. A locally finite graph has finitely many n-step paths from a fixed root, so the counting argument also applies there."),
entry("outer-buffer-transfer","lemma","DRAFT: avoidance transfer through positive outer buffers",
"Let K_n converge weakly to K in the Hausdorff space of nonempty compact subsets of compact metric S. For nonempty closed A, closed A_m obey N_r_m(A) subset A_m subset N_R_m(A), with 0<r_m<=R_m tending to zero. If every fixed-m avoidance probability has limit q_m and q_m tends to q, then P(K avoids A)=q, even with positive contact mass.",
["S compact metric; all random sets nonempty compact","A nonempty closed","A_m closed","Both radii positive and tend to zero","First take n to infinity for each fixed m; q_m exists","Then take m to infinity; q_m tends to q"],
"Write d_n=dist(K_n,A) and d=dist(K,A). The distance map is Hausdorff-Lipschitz. Buffer inclusions give P(d_n>R_m)<=P(K_n avoids A_m)<=P(d_n>r_m). Portmanteau yields P(d>R_m)<=q_m<=P(d>=r_m). Both outer probabilities tend to P(d>0) as positive radii vanish. Compactness identifies positive distance with avoidance. No diagonal limit or atom-free hypothesis is used."),
entry("raw-avoidance-route","concept","REFUTED route: unconditional weak-limit avoidance transfer",
"The inference that uniform or weak convergence of simple curves automatically preserves avoidance of every fixed closed boundary hull is false. The event can change at a contact-only limiting trace.",
["Refuted inference, not a theorem","No positive outer-buffer probability information is supplied"]),
entry("boundary-contact-example","lemma","DRAFT: simple-curve boundary-hull contact counterexample",
"In D=(-1,1)^2 with a=(-1,0), b=(1,0), let A=[-1/4,1/4] times [-1,0]. The simple polygonal curves a->(0,1/n)->b avoid A and converge uniformly to a trace hitting A. Their deterministic avoidance probabilities are 1 and 0 respectively.",
["Closed rectangular boundary hull","Positive n","Same piecewise linear parameterization for comparison"],
"Above x in [-1/4,1/4] the curve has height (1/n)(1-|x|)>0. Its limiting horizontal segment has height zero there and meets A. The maximum uniform distance between these parameterizations is 1/n."),
entry("length-mixture","lemma","DRAFT: length-mixture identity and non-transfer example",
"For a finite path ensemble with c_k paths of length k, fugacity-weighted obstacle avoidance is sum_k pi_x(k)p_k, with pi_x(k)=x^k c_k/sum_j x^j c_j and p_k=c_k(deleted)/c_k. This average need not equal a fixed-length p_n. On a marked cycle with two arcs of lengths N,N+2 and an obstacle on the longer arc, p_N=1, p_(N+2)=0, and the weighted ratio is 1/(1+x^2), for every N>=2.",
["Finite ensemble; or absolutely convergent positive total fugacity sum","x>0 and positive denominator","Terms with c_k=0 omitted","For the example, precisely the two simple marked cycle paths are allowed"],
"Group the path weights by length in the finite restriction identity. On the example cycle there is one path of each stated length. Only the shorter path avoids the obstacle. Division of x^N by x^N+x^(N+2) gives 1/(1+x^2), differing from p_N by x^2/(1+x^2)."),
entry("ensemble-substitution-route","concept","REFUTED route: fugacity mixture determines fixed-length paths",
"One cannot identify a uniform fixed-n path law from a fugacity-weighted avoidance ratio alone. Fugacity weights cancel at fixed n, while the unrestricted-length law mixes n. Concentration, coefficient estimates, or an actual ensemble transfer theorem is an additional input.",
["Refuted general inference","The cycle example is not claimed to refute the honeycomb scaling conjecture"]),
entry("chordal-conditional-route","concept","DRAFT conditional chordal SLE route; not a P0003 solution",
"In a bounded Jordan domain with smooth marked boundary neighborhoods, assume curve tightness with simple interior limits, all fixed-buffer critical endpoint partition ratios equal to the normalized boundary conformal derivative to power 5/8, and convergence of that derivative along the actual buffer hulls. Finite restriction and positive outer-buffer transfer then give the smooth-hull avoidance law used by LSW Proposition 3.3 and Theorem 6.1 to identify SLE(8/3). None of the SAW tightness or ratio inputs is proved here. This is a distinct ensemble from P0003.",
["Curve metric is uniform modulo increasing reparameterization","Every subsequential limit is simple, connects the fixed marks, and otherwise lies in the domain","Closed buffers satisfy the two-sided positive metric neighborhood inclusions and preserve simple connectivity","For each fixed buffer, the critical two-endpoint partition-ratio limit exists and is the stated 5/8 derivative","Actual buffer derivatives converge","After mapping to H, traces are connected, unbounded, meet R only at 0, and have connected complement in C","The standard measurable passage from oriented simple traces to curve classes needs referee confirmation"]),
entry("p0003-ensemble-ledger","concept","DRAFT source correction: P0003 is fixed-length with a free endpoint",
"The verified primary locator for P0003 is Grimmett, arXiv:2205.07318v1, Question 2.2, PDF p.3: uniformly chosen n-step honeycomb walks rooted at the origin, with a free endpoint, under suitable rescaling, are conjectured to approach SLE(8/3). The source question leaves normalization, curve metric and SLE geometry unspecified. The critical chordal boundary-endpoint conjecture is related but not interchangeable without a proved bridge. Current openness remains UNKNOWN.",
["Primary mathematical question recovered, not a current openness certificate","The related chordal source is Duminil-Copin--Smirnov arXiv:1007.0575v2 Conjecture 1","No ensemble equivalence has been proved in this packet"])
]
relations=[
{"from_key":"outer-buffer-transfer","to_key":"raw-avoidance-route","kind":"semantic_association","rationale":"The refuted route says raw avoidance need not pass to a weak limit; the buffer lemma supplies the stated positive-buffer hypotheses under which an avoidance probability does pass."},
{"from_key":"boundary-contact-example","to_key":"raw-avoidance-route","kind":"refutes","rationale":"The route asserts automatic preservation of every fixed closed-hull avoidance event; the example's probabilities are explicitly 1 before the uniform limit and 0 at the limit."},
{"from_key":"length-mixture","to_key":"finite-restriction","kind":"depends_on","rationale":"The finite restriction identity is a ratio of path weights; grouping those same weights by length proves the mixture identity."},
{"from_key":"length-mixture","to_key":"ensemble-substitution-route","kind":"refutes","rationale":"The rejected inference identifies a fugacity average with a fixed-n value; the two-arc example gives 1/(1+x^2) versus 1 for every N."},
{"from_key":"chordal-conditional-route","to_key":"finite-restriction","kind":"depends_on","rationale":"The conditional chordal route uses exact edge-deleted partition ratios as discrete avoidance probabilities."},
{"from_key":"chordal-conditional-route","to_key":"outer-buffer-transfer","kind":"depends_on","rationale":"The conditional chordal route takes the fixed-buffer mesh limits and then the buffer limit using the lemma's exact quantifier order."},
{"from_key":"chordal-conditional-route","to_key":"p0003-ensemble-ledger","kind":"semantic_association","rationale":"One entry concerns fixed boundary endpoints and mixed lengths; the other concerns origin-rooted fixed length and a free endpoint. This is an explicit distinction, not a claimed reduction."},
{"from_key":"p0003-ensemble-ledger","to_existing_logical":"math:probability.core:open-problem-p0003-hexagonal-self-avoiding-walk-scaling-limit","kind":"cites","rationale":"The existing card says 'rescaled uniform n-step' and cites Grimmett Question 2.2; the campaign observation recovers the primary source and records the free endpoint and unspecified geometry."}
]
receipt_path=ROOT/"PORTMANTEAU_RECEIPT.json"
if receipt_path.exists():
    r=json.loads(receipt_path.read_text(encoding="utf-8"))
    if r.get("node"):
        meta=json.loads(r["node"]["metadata_json"])
        logical=meta.get("logical_id")
        if logical:
            relations.append({"from_key":"outer-buffer-transfer","to_existing_logical":logical,"kind":"depends_on","rationale":"The full Portmanteau card supplies open/closed inequalities under weak convergence. Apply those to scalar distance variables; do not invoke its boundary-zero equality clause on raw avoidance events."})
bundle={"spec":"mathbrain-draft-v1","author_agent":"w405","bundle_slug":"p0003-buffer-and-ensemble-bridge-w405-20261010","entries":entries,"relations":relations}
write("DRAFT_BUNDLE.json",bundle)
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
keys={e["key"] for e in entries}
assert len(entries)<=200 and len(keys)==len(entries)
for e in entries:
    assert e["kind"] in {"definition","lemma","theorem","concept"}
    assert e["source"]["license"].startswith("owner-own-work")
    assert e["statement"] and isinstance(e["assumptions"],list)
    if e["kind"] in {"lemma","theorem"}: assert e["proof_text"]
for r in relations:
    assert r["from_key"] in keys and r["kind"] in allowed
    assert ("to_key" in r)^("to_existing_logical" in r)
    if "to_key" in r: assert r["to_key"] in keys
adj={k:[] for k in keys}
for r in relations:
    if r["kind"]=="depends_on" and "to_key" in r: adj[r["from_key"]].append(r["to_key"])
def visit(k,active,done):
    assert k not in active, "depends_on cycle"
    if k in done:return
    for v in adj[k]:visit(v,active|{k},done)
    done.add(k)
done=set()
for k in keys:visit(k,set(),done)
m=json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
assert m["measurements"]["fixture_checks"]==22 and m["measurements"]["passed"]==22
write("BUNDLE_VALIDATION.json",{"schema_check":"PASS","entry_count":len(entries),"relation_count":len(relations),"depends_on_acyclic":True,"fixture_passes":22,"independent_referee_status":"pending w407","not_a_mathematical_proof_receipt":True,"not_an_ingestion_receipt":True})

newclaims=[
{"id":"w405-L3","kind":"lemma-and-refuted-route","statement":entries[4]["statement"],"assumptions":entries[4]["assumptions"],"source":own_source("length-mixture"),"proof_or_counterexample":entries[4]["proof_text"],"independent_reviewer":"w407 (pending)","remaining_gap":"No coefficient or ensemble transfer theorem for fixed-n honeycomb SAW is supplied.","status":"proved special case"},
{"id":"w405-S1","kind":"source-correction","statement":entries[7]["statement"],"assumptions":entries[7]["assumptions"],"source":{"url":"https://arxiv.org/pdf/2205.07318","locator":"Question 2.2, PDF p.3","quote":"suitably rescaled"},"proof_or_counterexample":"Compare the verified primary question with the full stored P0003 card and the distinct Duminil-Copin--Smirnov boundary-endpoint formulation.","independent_reviewer":"w407 (pending)","remaining_gap":"Specify target geometry and rescaling before an exact convergence theorem; verify any claimed ensemble equivalence.","status":"sketch"},
{"id":"w405-M1","kind":"measured-reasoning-failure-and-bounded-repair","statement":"In deterministic fixtures, raw avoidance transfer has error 1 (simple curves) or 0.6 (positive contact mass); the positive-buffer conclusion has error 0. A critical length-mixture ratio differs from the fixed-length value by 0.22654091966098644.","assumptions":["Only the explicit fixtures in verify_bridge.py","Not a population-wide recall score or solved theorem"],"source":{"path":"~/brain_workers/w405/MEASUREMENTS.json","command":"python -B -X utf8 verify_bridge.py"},"proof_or_counterexample":"22 of 22 bounded checks passed. Proposed repair is the typed buffer/ensemble obligation ledger and a narrow source-ensemble hook; no live recall controls changed.","independent_reviewer":"w407 (pending)","remaining_gap":"Reviewer applies/ingests after mathematical review; live improvement is unmeasured.","status":"numerical evidence"}
]
claims_path=ROOT/"CLAIMS.jsonl"
claims=[json.loads(x) for x in claims_path.read_text(encoding="utf-8").splitlines() if x.strip()]
existing={c["id"] for c in claims}
for c in claims:
    if c["id"] in {"w405-L1","w405-L2","w405-R1"}:
        c["peer_audit"]={"reviewer":"w406","verdict":"KEEP","path":"~/brain_workers/w406/AUDIT_w405.md","scope":"original chordal L1/L2/R1 text; fixed-n addition and L3 are not covered","account_separation_verified":False}
    if c["id"]=="w405-C1":
        c["peer_audit"]={"reviewer":"w406","verdict":"KEEP AS CONDITIONAL SKETCH ONLY","path":"~/brain_workers/w406/AUDIT_w405.md"}
for c in newclaims:
    if c["id"] not in existing:claims.append(c)
claims_path.write_text("".join(json.dumps(c,ensure_ascii=False)+"\n" for c in claims),encoding="utf-8")
source={
"worker":"w405","target_id":"P0003","current_openness":"UNKNOWN","exact_statement":entries[7]["statement"],
"primary_sources":[{"id":"arxiv:2205.07318v1","url":"https://arxiv.org/pdf/2205.07318","locator":"Question 2.2, PDF p.3","role":"actual fixed-n free-endpoint target","checked":"primary full text read 2026-10-10"},{"id":"arxiv:1007.0575v2","url":"https://www.unige.ch/~smirnov/papers/saw-j.pdf","locator":"Section 4 Conjecture 1, p.1662","role":"distinct chordal critical-fugacity formulation; Theorem 1 gives fugacity only"},{"id":"arxiv:math/0209343v2","url":"https://arxiv.org/pdf/math/0209343","locator":"Definition 3.1, Proposition 3.3, Theorem 6.1","role":"conditional continuum identification, not a discrete SAW convergence proof"}],
"owner_solved_retired_check":{"scope":"Targeted P0003 records in cited H/I attempts, Lean annotated list, intake directories and cited Big Open problem directory","finding":"No verified closure found in checked artifacts; bounded negative search, not exhaustive absence certificate"},
"recent_primary_check":{"scope":"bounded public searches for 2025/2026 hexagonal SAW/SLE scaling","finding":"No verified closing proof established in this run; openness UNKNOWN"},
"retrieval_receipts":["MATH_BRAIN_RECEIPT.json","NARROW_MATH_BRAIN_RECEIPT.json","PORTMANTEAU_RECEIPT.json"],
"draft_delivery":{"submitted":False,"reviewed":False,"ingested":False,"retrievable":False},
"independent_review":{"w406":"KEEP L1/L2/R1; C1 conditional only, original version scope","w407":"full referee verdict pending","different_account_separation":"not verified"},
"source_hash_or_formal_check_is_not_a_mathematical_proof":True}
write("SOURCE_STATUS.json",source)
hook={"id":"saw-ensemble-w405-01","area":"math","event":"stage-start","cue":"SAW proof promotion uses chordal restriction or fugacity ratios for a uniform fixed-n free-endpoint target without a verified ensemble bridge","fire_when":"P0003's fixed-n origin-rooted target is called solved using only a chordal mixed-length partition ratio","silent_when":"A conditional result is explicitly limited to critical-fugacity paths between fixed boundary endpoints","text":"Check the SAW ensemble before applying restriction: P0003 fixes length and has a free endpoint. Fugacity ratios mix lengths. Keep the ensemble bridge and fixed-length count asymptotics explicit; a chordal conditional result alone does not close this target.","evidence":"w405 ATTEMPT.md L3/R2; MEASUREMENTS.json: critical ratio 0.773459080339 versus fixed-length 1; PORTMANTEAU_RECEIPT.json and primary Grimmett Q2.2","proposer":"w405"}
(ROOT/"HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")
patches=ROOT/"patches"
patches.mkdir(exist_ok=True)
live="~/primary_directive/hooks1000/proposals/math-w405.jsonl"
(patches/"01_saw_ensemble_hook.diff").write_text("--- a/"+live+"\n+++ b/"+live+"\n@@ -0,0 +1 @@\n+"+json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")
write("PROGRESS_ROW.json",{"agent":"w405","row":"S1.w405-L2","event":"P0003: proved buffered avoidance lemma, exposed fixed-n/chordal mismatch, 22/22 bounded checks; draft bundle and referee packet ready.","evidence":str(ROOT/"REVIEW_PACKET.md"),"delivery":"local queued row; shared progress script not run under folder-only write constraint"})
write("HANDOFF_RECEIPT.json",{"adversary":"w406","statement_first_message_id":"msg-ae5fbe8c07","source_correction_message_id":"msg-875bf3d37e","referee":"w407","full_packet":str(ROOT/"REVIEW_PACKET.md"),"delivery_state":"pending-peer-registration: mesh send returned recipient w407 is not registered","independent_referee_verdict":"pending","draft_inbox_claim":"clm-166d8618ef"})
print(json.dumps({"entries":len(entries),"relations":len(relations),"claims":len(claims),"schema":"PASS","tests":"22/22"},indent=2))
