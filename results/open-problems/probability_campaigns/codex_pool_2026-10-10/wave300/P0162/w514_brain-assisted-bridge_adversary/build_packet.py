"""Build the local DRAFT bundle and exact edge receipts; no live writes."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def readjson(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

def dump(name,obj):
    target=ROOT/name
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for row in claims:
        row["independent_reviewer"]="w515 (assigned; independent check pending)"
    added=[
      {"id":"w514-C003","target":"P0162","exact_statement":"For every even n>=4, the Boolean F(x,t)=g(x)-(1-t)1{x=(1,...,1)} from C002 satisfies H(F)<=2I(F), where I(F)=n/2+(n+1)2^{-n}. Thus the unbounded bad-coordinate increment ratio in C002 does not contradict FEI.","assumptions":["The explicit disjoint-pair core g from C002","Uniform measure","Base-2 entropy","n even and n>=4"],"source":{"type":"owner-own-work","artifact":"BENT_SELECTOR.md"},"proof":"Each core-coordinate influence is 1/2+p, p=2^{-n}; the selector influence is p. Spectral entropy conditioned on selector membership is at most n, hence H(F)<=n+h_2(p)<=n+(n+2)p<=2I(F). See BENT_SELECTOR.md.","independent_reviewer":"w515 (assigned; check pending)","remaining_gap":"Only this explicit family; does not imply general FEI or the existential coordinate bridge.","status":"proved special case","review_state":"unreviewed","novelty":"not claimed"},
      {"id":"w514-C004","target":"P0162","exact_statement":"For every Boolean f on a uniform d-cube and every coordinate i, put p=I_i(f) and Delta_i=H(f)-(H(f|i=+1)+H(f|i=-1))/2, using base-2 entropy. Then 0<=Delta_i<=h_2(p)+(2/ln2)p<=p log_2(1/p)+(3/ln2)p, with zero conventions. Furthermore sup_{d,f,i:p>0}[Delta_i/p-log_2(1/p)]=3/ln2.","assumptions":["Boolean codomain","Uniform cube measure","Base-2 entropy","All coordinates, not an existential choice","p>0 for the supremum"],"source":{"type":"owner-own-work","artifact":"SHARP_COORDINATE_BOUND.md","brain_lead":"claim_d15d0160e58b4c9183707be9f49462d2 (unverified; threshold upper-bound component only)"},"proof":"Grouping paired Fourier coefficients gives Delta_i=JS_2(a^2,b^2)+sum_S m_S h_2(q_S). Concavity bounds the second term by h_2(p). A scalar derivative proof gives JS_e(P,Q)<=sum(sqrt(P)-sqrt(Q))^2/2, hence JS_2(a^2,b^2)<=2p/ln2. The explicit C002 witnesses satisfy Delta_t/p-log_2(1/p)->3/ln2 by a uniform Taylor expansion. Full proof, endpoints and sign factors are in SHARP_COORDINATE_BOUND.md.","independent_reviewer":"w515 (assigned; check pending)","remaining_gap":"Full author derivation awaits independent check; this bound diverges as p decreases and does not resolve the existential coordinate step.","status":"sketch","review_state":"unreviewed","novelty":"not claimed","numerical_evidence":"sharpness_measurements.json: 6 bounded high-precision diagnostics; finite checks are not the limit proof"},
      {"id":"w514-C005","target":"P0162","exact_statement":"Fix 0<tau<1. General FEI is equivalent to a bound H(f)<=C_tau I(f) for all Boolean functions whose coordinate influences are all <tau, with C_tau independent of dimension. The restricted-class bound implies general FEI with constant max(C_tau,log_2(1/tau)+3/ln2).","assumptions":["A fixed tau independent of dimension","Uniform cube measure","Base-2 entropy","The assumed low-influence estimate covers every dimension and every Boolean function in that class"],"source":{"type":"owner-own-work (separate derivation of an existing brain lead)","artifact":"SHARP_COORDINATE_BOUND.md","brain_lead":"claim_d15d0160e58b4c9183707be9f49462d2"},"proof":"Split at a coordinate with influence >=tau until every coordinate influence is <tau. The tree terminates because dimension decreases. Apply C004's coordinate bound and I(f)=(I(g)+I(h))/2+I_i(f) at branching nodes, and the assumed C_tau bound at leaves. Induction yields the maximum constant. The converse follows by restricting the universal FEI quantifiers.","independent_reviewer":"w515 (assigned; check pending)","remaining_gap":"No dimension-free bound for the assumed low-influence class is established. This is a reduction, not a solution.","status":"sketch","review_state":"unreviewed","novelty":"not new; rederived component of existing provisional brain card"}
    ]
    existing={row["id"] for row in claims}
    claims.extend(row for row in added if row["id"] not in existing)
    (ROOT/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims),encoding="utf-8")

    def entry(key,name,kind,title,statement,assumptions,artifact):
        return {"key":key,"namespace":"probability.boolean","logical_name":name,"kind":kind,"title":title,
                "statement":statement,"proof_text":None,"assumptions":assumptions,"domain":"analysis of Boolean functions",
                "source":{"source_id":"owner:w514:P0162:"+key,"url":"file:///"+(ROOT/artifact).as_posix(),
                          "revision":"author-draft-2026-10-10; independent check pending","license":"owner-own-work","excerpt":None}}
    definition="On the uniformly measured d-dimensional Boolean cube, let f:{-1,1}^d->{-1,1}. Write hat(f)(S)=E[f(x)product_{j in S}x_j], H(f)=sum_S hat(f)(S)^2 log_2(1/hat(f)(S)^2), I_i(f)=sum_{S containing i}hat(f)(S)^2, and Delta_i(f)=H(f)-(H(f|x_i=+1)+H(f|x_i=-1))/2, with zero entropy terms interpreted as zero. A constant function has H=I=0."
    route="REFUTED ROUTE, supported by an author proof awaiting independent check: the proposed quantifiers are 'there exists finite K such that for every d>=1, every Boolean f on the uniform d-cube, and every coordinate i, Delta_i(f)<=K I_i(f)', where Delta is the base-2 Fourier entropy increment under restriction. The stronger 'every coordinate' quantifier must not be substituted for the existential coordinate in a restriction induction."
    witness="DRAFT RESULT; author derivation, independent check pending. For every even n=2m>=4, define g(x)=product_{j=1}^m(1+x_{2j-1}+x_{2j}-x_{2j-1}x_{2j})/2 and F(x,t)=g(x)-(1-t)1{x=(1,...,1)} for x in {-1,1}^n, t in {-1,1}. These functions are Boolean. Under uniform measure and base-2 Fourier entropy, p=I_t(F)=2^{-n} and Delta_t(F)=H(F)-(H(F|t=1)+H(F|t=-1))/2>=np. Nonetheless I(F)=n/2+(n+1)p and H(F)<=2I(F). This is an obstruction to an arbitrary-coordinate linear increment bound, not to FEI or to an existential good-coordinate bound."
    sharp="DRAFT RESULT; author derivation, independent check pending. For every uniform-cube Boolean f and coordinate i with p=I_i(f), its base-2 Fourier entropy increment Delta_i=H(f)-(H(f|i=1)+H(f|i=-1))/2 satisfies 0<=Delta_i<=h_2(p)+(2/ln2)p<=p log_2(1/p)+(3/ln2)p, using zero conventions at p=0. Here h_2 is binary entropy. The additive constant is exact: sup_{d,f,i:p>0}(Delta_i/p-log_2(1/p))=3/ln2. The upper bound follows from a paired-spectrum decomposition and a Jensen-Shannon/Hellinger comparison; the disjoint-pair Boolean selector witnesses attain the supremum in the limit. This bound does not solve general FEI."
    reduction="DRAFT CONDITIONAL REDUCTION; author rederivation, independent check pending. Fix 0<tau<1 independently of dimension. If all uniformly measured Boolean functions whose coordinate influences are all <tau satisfy H(f)<=C_tau I(f) with C_tau independent of dimension and base-2 Fourier entropy, then every Boolean function satisfies H(f)<=max(C_tau,log_2(1/tau)+3/ln2) I(f). Repeatedly restrict a coordinate of influence >=tau; the dimension decreases and the exact influence identity telescopes with the coordinate entropy bound. The converse is immediate. The required low-influence class estimate remains unproved here; selecting a maximum-influence coordinate is not asserted to solve that remaining case."
    entries=[entry("increment","fei-fourier-entropy-restriction-increment","definition","Fourier entropy increment under Boolean coordinate restriction",definition,["Uniform measure","Boolean codomain","Base-2 entropy"],"SHARP_COORDINATE_BOUND.md"),
             entry("linear-route","fei-arbitrary-coordinate-linear-increment-proposal","concept","Refuted route: every coordinate has bounded entropy/influence increment",route,["All dimensions","Every coordinate, not an existential choice","Base-2 entropy"],"BENT_SELECTOR.md"),
             entry("witness","fei-bent-selector-bad-coordinate-witness-draft","concept","Draft Boolean witness: bad coordinate cost diverges while FEI holds",witness,["n even and n>=4","Explicit pair-product core","Uniform measure","Base-2 entropy"],"BENT_SELECTOR.md"),
             entry("sharp","fei-sharp-logarithmic-coordinate-increment-draft","concept","Draft exact logarithmic coordinate cost",sharp,["Uniform measure","Boolean codomain","Base-2 entropy","p>0 for the supremum"],"SHARP_COORDINATE_BOUND.md"),
             entry("reduction","fei-fixed-threshold-small-influence-reduction-draft","concept","Draft conditional FEI reduction to small coordinate influences",reduction,["Fixed 0<tau<1 independent of dimension","Assumed low-influence bound covers every dimension","Uniform measure","Base-2 entropy"],"SHARP_COORDINATE_BOUND.md")]
    relations=[{"from_key":"witness","to_key":"linear-route","kind":"refutes","rationale":"For each fixed K, the quoted Boolean witness has an even n>K and Delta_t/I_t>=n, contradicting the proposed every-coordinate bound. This edge does not target general FEI."},
               {"from_key":"witness","to_key":"increment","kind":"depends_on","rationale":"The witness concerns the defined Delta_t under the stated entropy and influence normalization."},
               {"from_key":"sharp","to_key":"increment","kind":"depends_on","rationale":"The bound and supremum use this exact normalized coordinate entropy increment."},
               {"from_key":"sharp","to_key":"witness","kind":"depends_on","rationale":"Optimality of the additive constant uses the explicit witness and its analytic limit; the upper bound has a separate JS proof."},
               {"from_key":"reduction","to_key":"sharp","kind":"depends_on","rationale":"For p>=tau the quoted logarithmic coordinate bound is at most p(log_2(1/tau)+3/ln2), supplying the branching-node estimate in the finite restriction tree."}]
    bundle={"spec":"mathbrain-draft-v1","author_agent":"w514","bundle_slug":"p0162-sharp-coordinate-bridge-w514-001","entries":entries,"relations":relations}
    dump("brain_bundle/bundle_001.json",bundle)
    bykey={e["key"]:e for e in entries}
    edge_rows=[{**r,"from_quote":bykey[r["from_key"]]["statement"],"to_quote":bykey[r["to_key"]]["statement"],
                "support":"BENT_SELECTOR.md and SHARP_COORDINATE_BOUND.md; author proofs only","status":"DRAFT; independent check pending","reviewer":"w515"} for r in relations]
    (ROOT/"EXACT_EDGES.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in edge_rows),encoding="utf-8")

    recall=readjson("recall_math.json")
    raw=json.loads(recall["stdout"])
    hits=raw["hits"] if isinstance(raw,dict) else raw
    hydrated=readjson("retrieved_exact_nodes.json")["nodes"]
    selected={row["id"] for row in hydrated}
    projected=[row for row in hits if row["id"] in selected]
    failure={"id":"w514-R001","query":recall["query"],"before_command":"python -B -X utf8 readonly_recall.py math 'Fourier entropy influence hypercontractivity restriction induction'",
             "before_seconds":recall["seconds"],"before_hit_count":len(hits),"selected_cited_nodes":len(projected),
             "before_selected_status_visible":sum("status" in row for row in projected),
             "before_selected_assumptions_visible":sum("assumptions" in row for row in projected),
             "after_command":"python -B -X utf8 read_exact_nodes.py","after_selected_status_visible":sum("status" in (row.get("claim") or {}) for row in hydrated),
             "after_selected_assumptions_visible":sum("assumptions" in (row.get("claim") or {}) for row in hydrated),
             "after_statuses":[{"id":row["id"],"status":(row.get("claim") or {}).get("status"),"kind":(row.get("claim") or {}).get("kind")} for row in hydrated],
             "failure":"Title-only recall omitted the assumptions and unverified status of all three cited cards, including two lemma cards whose prose mixes analytic claims with finite computed examples.",
             "bounded_proposed_repair":"Keep ranking unchanged. Add an opt-in, by-ID full-claim receipt for at most three chosen hits, displaying statement, assumptions, claim status and provenance. Require explicit hypothesis comparison before using an unverified lemma as a theorem. read_exact_nodes.py is this task's bounded local adapter, not a deployed engine patch.",
             "scope_limit":"One query, three citation-selected cards; display coverage only. No ranking-accuracy or general brain-effectiveness improvement is claimed.",
             "math_failure":"A universal K bound at every coordinate fails on the Boolean C002 witnesses; choosing one good coordinate remains a separate unproved premise."}
    dump("RETRIEVAL_FAILURE.json",failure)
    state={"bundle":"brain_bundle/bundle_001.json","prepared":True,"submitted":False,"reviewed":False,"ingested":False,"retrievable":False,
           "current_kinds":"One definition and four concept/draft nodes; no unreviewed theorem promoted",
           "delivery_boundary":"All files remain in worker folder. Reviewer should independently check proofs, then place the requested draft at ~/math-brain-inbox/w514/bundle_001.json and coordinate validation. No live SQLite writes or integrator invocation performed."}
    dump("BUNDLE_STATE.json",state)

    source=readjson("SOURCE_STATUS.json")
    source["sources"].insert(1,{"id":"ODonnell12v1","url":"https://arxiv.org/pdf/1204.6447","revision":"2012-04-29 v1","locator":"printed page 5, FEI Conjecture; PDF page index 4","scope":"The exact primary source cited by the intake was recovered; statement agrees with this packet"})
    source["owner_solved_retired_check"]={"scope":"Targeted intake/attempt/lean scans and the recall-cited FEI owner memories only","conclusion":"No full-FEI solution or retirement found in these bounded reads. Owner LTF and plateaued special cases are separately scoped; current openness remains UNKNOWN.","memory_slugs":["fei_plateaued_constant_four_is_potapovs_theorem_not_ours_2026_09_30","fei_holds_for_linear_threshold_functions_rank_argument_2026_09_23","fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23"]}
    source["paired_access"]={"independent_first":["INDEPENDENT.md","BENT_SELECTOR.md"],"then_read":["w513/STATEMENT.md","w513/CLAIMS.jsonl","w513/STATUS.md"],"proof_available_at_read":False,"proof_audit":"pending; w513 had supplied only a statement at the recorded read"}
    dump("SOURCE_STATUS.json",source)

    patch_dir=ROOT/"patches"
    patch_dir.mkdir(exist_ok=True)
    text=(ROOT/"brain_bundle/bundle_001.json").read_text(encoding="utf-8")
    live="~/math-brain-inbox/w514/bundle_001.json"
    patch="".join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
    (patch_dir/"01_p0162_bridge_bundle.diff").write_text(patch,encoding="utf-8")
    print(json.dumps({"claims":len(claims),"bundle_entries":len(entries),"edges":len(relations),
                      "status_display_before":failure["before_selected_status_visible"],"status_display_after":failure["after_selected_status_visible"],
                      "submitted":False}))

if __name__=="__main__":
    main()
