"""Build local review material and the explicitly authorized DRAFT inbox bundle."""
import difflib
import json
from pathlib import Path
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
RESEARCH = Path("~/<private-repo>/06_math_research")
INTAKE = RESEARCH / "probability_1000_intake_claude_20260907"
for name in ("extracts", "patches", "drafts", "hooks"):
    (ROOT/name).mkdir(exist_ok=True)

def write_json(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def find_record(path,field,value):
    with path.open(encoding="utf-8") as stream:
        for line_number,line in enumerate(stream,1):
            if value not in line: continue
            row=json.loads(line)
            if row.get(field)==value: return line_number,line,row
    raise LookupError((str(path),field,value))

target_line,_,target=find_record(INTAKE/"problems.jsonl","problem_id","C0017")
attempt_line,raw_before,attempt=find_record(INTAKE/"attempts.jsonl","attempt_id","C0017-A001")
write_json(ROOT/"extracts"/"target_C0017.json",target)
write_json(ROOT/"extracts"/"attempt_C0017_before.json",attempt)
assert attempt["result"].count("has spin sigma = 2/3")==1
corrected=dict(attempt)
corrected["result"]=attempt["result"].replace("has spin sigma = 2/3","has spin sigma = 1/3 in the convention F(e) = E[exp(i sigma W_gamma(e,e_b)) 1_{e in gamma}], sin(sigma*pi/2)=sqrt(q)/2, sigma in [0,1] (Duminil-Copin, arXiv:1208.3787, Definition 3)")
corrected["correction_note"]="2026-10-10 w418 DRAFT source-convention correction: sigma=1/3 for q=1; sigma=2/3 would imply q=3 under Definition 3. Independent review by w419 pending. Other statements in this attempt are not certified by this correction."
raw_after=json.dumps(corrected,ensure_ascii=False,sort_keys=True)+"\n"
write_json(ROOT/"extracts"/"attempt_C0017_after.json",corrected)
relative="06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl"
patch=f"--- a/{relative}\n+++ b/{relative}\n@@ -{attempt_line} +{attempt_line} @@\n-{raw_before.rstrip(chr(10))}\n+{raw_after.rstrip(chr(10))}\n"
(ROOT/"patches"/"01_c0017_principal_spin.diff").write_text(patch,encoding="utf-8")

old_logical="math:probability.percolation:attempt-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic"
old_id="claim_07a861a72ebeb008dc23e9db32147327c062427adee7a530bab01f0de67bd002"
database=Path("~/math-brain-build/local/population/brain.sqlite3")
canonical={"path":str(database),"open_mode":"read-only","node_id":old_id,"logical_id":old_logical}
query_started=time.monotonic()
if database.is_file():
    try:
        with sqlite3.connect(f"file:{database.as_posix()}?mode=ro",uri=True,timeout=5) as con:
            columns=[r[1] for r in con.execute("PRAGMA table_info(nodes)")]
            if "id" not in columns:
                canonical.update({"status":"schema_not_matching_nodes_export","available_node_columns":columns})
            else:
                selected=[c for c in ("id","title","body","metadata_json") if c in columns]
                row=con.execute("SELECT "+",".join(selected)+" FROM nodes WHERE id=?",(old_id,)).fetchone()
                if row is None:
                    canonical["status"]="exact_node_id_not_found"
                else:
                    node=dict(zip(selected,row))
                    write_json(ROOT/"extracts"/"canonical_C0017_attempt.json",node)
                    canonical.update({"status":"exact_node_retrieved","legacy_spin_phrase_present":"spin sigma = 2/3" in node.get("body",""),"title":node.get("title")})
    except sqlite3.Error as exc:
        canonical.update({"status":"read_only_query_failed","error":str(exc)})
else:
    canonical["status"]="named_database_unavailable"
canonical["elapsed_seconds"]=time.monotonic()-query_started

recall=json.loads((ROOT/"recall_measurement.json").read_text(encoding="utf-8"))
measurement=json.loads((ROOT/"obstruction_measurement.json").read_text(encoding="utf-8"))
source_status={
    "target":"C0017","as_of":"2026-10-10","current_openness":"UNKNOWN","parent_problem_solved":False,
    "intake":{"path":str(INTAKE/"problems.jsonl"),"line":target_line,"statement":target["statement"],"reported_locator":target["locator"],"verification":target["verification"]},
    "primary_target_source":{"url":"https://arxiv.org/pdf/1102.5761","authors":"Christophe Garban and Jeffrey Steif","location":"Chapter II section 4; Theorem II.2 and following paragraph; printed page 24, PDF page index 25 in the as-read version","pagination_clarification":"Printed page 24 is one-based PDF page 26, consistent with the intake p.26 locator.","short_quote":"proving the conformal invariance is still a challenging open problem","scope":"Historical square-lattice conjecture; triangular site theorem. Does not certify status in 2026."},
    "observable_source":{"url":"https://arxiv.org/abs/1208.3787","full_text_url":"https://www.unige.ch/~duminil/publi/divergenceFK.pdf","location":"Definition 3 and Proposition 4, printed p.7; introductory discussion printed p.2","hypotheses":["Finite simply connected square-lattice Dobrushin domain (G,a,b)","FK model with 0<q<4 at p_c(q)","F(e)=E[exp(i sigma W_gamma(e,e_b)) 1_{e in gamma}]","sigma in [0,1] satisfies sin(sigma pi/2)=sqrt(q)/2","Interior medial vertex with four incident edges"],"result":"F(NW)-F(SE)=i(F(NE)-F(SW)); q=1 gives p_c=1/2 and principal sigma=1/3.","short_quote":"not fully preholomorphic, but rather a divergence-free differential form","does_not_supply":"A common normalized scalar limit, boundary identification, or square-bond conformal invariance."},
    "other_primary_sources":[
        {"url":"https://arxiv.org/abs/0909.4499","location":"Theorem 1 and Corollaries 1-4","scope":"Critical triangular SITE percolation; no square BOND transfer theorem"},
        {"url":"https://arxiv.org/pdf/1204.0505v2","location":"Theorem 3.4","scope":"Canonical isoradial BOND percolation with bounded angles and square-grid property; conditional invariance of certain exponents if existence holds for a member; does not include triangular site percolation or scalar observable convergence"},
        {"url":"https://arxiv.org/abs/2409.03235v6","date":"2024-12-17","scope":"Primary manuscript claims full square-bond SLE_6 convergence; validity and acceptance not independently verified here"},
        {"url":"https://arxiv.org/abs/2609.18421","date":"2026-09-16","scope":"Primary manuscript claims a half-plane one-arm exponent; neither theorem validity nor a complete conformal-invariance bridge checked here"}
    ],
    "prior_work":{"C0017_attempt":{"path":str(INTAKE/"attempts.jsonl"),"line":attempt_line,"defect":"Principal-spin convention mismatch in an author-checked, unreviewed attempt; also present in the matched population export node","scope":"Correct only that parameter. Do not certify the whole attempt."},"other_named_directories":"Targeted C0017/conformal-square searches in attempts H, attempts I, and prob1000_lean; no exact C0017 resolution surfaced in the inspected matches. No broad repository or store export read.","owner_solved_retired":"Local mathematical owner folder inspected by targeted filename/term discovery; no verified solved/retired C0017 result recovered. Absence in this bounded check is not a completeness certificate.","team_o_board":"Read; no C0017 row found by targeted search. Probability300 board names C0017 workers w408-w419; no competing shared mathematical artifact edited."},
    "brain_use":{"bounded_recall":recall,"canonical_read":canonical,"fallback":"Targeted memory-index grep gave no applicable entries; read named scar perceptron_proof_open_gaps_fleet_2026_07_12 and targeted population export nodes. The scar's local-versus-global proof obligation is a hint only.","export_match":{"path":"~/math-brain-build/export/population/nodes.jsonl","line":272,"node_id":old_id,"logical_id":old_logical,"truth_status":"unverified","short_defective_quote":"the parafermionic observable has spin sigma = 2/3"}},
    "verification_limits":"Source and artifact inspection are not mathematical proof. No formal-check receipt, admitted placeholder, independent approval, ingestion, or live recall improvement is claimed."
}
write_json(ROOT/"SOURCE_STATUS.json",source_status)

def own_source(key):
    return {"source_id":"owner-own-work:w418:C0017:"+key,"url":str(ROOT/"REVIEW_PACKET.md"),"revision":"2026-10-10; campaign derivation; independent review pending","license":"owner-own-work","excerpt":None}

entries=[
    {"key":"weak-edge-relation","namespace":"probability.percolation","logical_name":"square-medial-weak-edge-contour-relation","kind":"definition","title":"Weak four-edge contour relation in rotated coordinates","statement":"On a square grid of mesh delta, attach a complex value F to each edge midpoint. At an interior vertex v let E,W,N,S be the adjacent midpoint values. The weak four-edge relation is F_E-F_W+i(F_N-F_S)=0. This definition imposes no probability representation, boundary condition, or coherence between the horizontal and vertical edge fields.","assumptions":["delta>0","Complex edge data on a square grid"],"domain":"planar percolation observable audit"},
    {"key":"principal-spin-correction","namespace":"probability.percolation","logical_name":"c0017-principal-parafermion-spin-correction","kind":"concept","title":"DRAFT correction: q=1 has principal spin one third","statement":"Source-convention correction, independent review pending: for F(e)=E[exp(i sigma W_gamma(e,e_b)) 1_{e in gamma}], with sigma in [0,1] and sin(sigma pi/2)=sqrt(q)/2 as in Duminil-Copin arXiv:1208.3787 Definition 3, q=1 gives sigma=1/3. The value sigma=2/3 would give q=3 under that equation. This refutes only the principal-spin sentence in the legacy C0017 attempt, not every other assertion there or other spin conventions.","assumptions":["Precisely the displayed source convention and principal branch"],"domain":"FK percolation parameter audit"},
    {"key":"orientation-obstruction","namespace":"probability.percolation","logical_name":"weak-edge-identity-orientation-coherence-obstruction","kind":"concept","title":"DRAFT obstruction: weak edge identities do not identify a scalar limit","statement":"Author-derived counterexample, independent review pending: for every delta>0 assign F(e)=conjugate(z_e) on horizontal edge midpoints and F(e)=z_e on vertical ones. Then F_E-F_W=delta and F_N-F_S=i delta, so the weak four-edge relation holds exactly. The two fields are smooth and uniformly Lipschitz within their orientations on bounded domains, yet their vertex average (F_E+F_W+F_N+F_S)/4 equals Re z and has contour integral i times area around each positively oriented rectangle. Thus the weak relation and separate orientation compactness do not imply scalar holomorphicity. This is not a probability-defined percolation observable or a counterexample to conformal invariance.","assumptions":["Square grid with complex midpoint coordinate z_e","No additional boundary or probability constraints are imposed"],"domain":"discrete complex analysis obstruction"},
    {"key":"coherence-bridge","namespace":"probability.percolation","logical_name":"weak-edge-relation-common-limit-morera-bridge","kind":"concept","title":"DRAFT sufficient premise: common continuous edge limit","statement":"Conditional author derivation, independent review pending: let delta_n tend to zero in a fixed open domain D. Suppose complex edge data satisfy the weak four-edge relation at every interior grid vertex and approach a single continuous function f locally uniformly over ALL edge midpoints of both orientations along that same sequence. Summing the exact relation over a dual rectangle cancels interior edges; multiplying by i delta_n yields its boundary midpoint integral. The limiting integral of f dz is zero around every interior axis-aligned rectangle, so f is holomorphic. Separate convergence within each orientation does not supply the common-limit premise. Percolation-specific normalization, coherence and boundary identification remain gaps.","assumptions":["Fixed open domain D","One common continuous limit over all edge orientations, locally uniform on every compact subset","Exact weak edge identity along the same mesh sequence"],"domain":"conditional observable convergence bridge"},
    {"key":"hybrid-endpoint-obstruction","namespace":"probability.percolation","logical_name":"product-law-endpoint-sensitivity-substitution-obstruction","kind":"concept","title":"DRAFT obstruction: endpoint influences cannot replace hybrid influences","statement":"Author-derived counterexample, independent review pending: let f be majority of three independent bits, mu=Bernoulli(epsilon)^3, nu=Bernoulli(1-epsilon)^3 with 0<epsilon<1/2. Each endpoint exterior makes a cell section nonconstant with probability 2 epsilon(1-epsilon), and each cell TV is 1-2 epsilon. Substituting endpoint sensitivities into a telescoping bound would give 6 epsilon(1-epsilon)(1-2 epsilon), tending to zero, whereas E_nu f-E_mu f=1-6 epsilon^2+4 epsilon^3 tends to one. For replacement order 1,2,3, the actual hybrid sensitivities are 2 epsilon(1-epsilon), (1-epsilon)^2+epsilon^2, 2 epsilon(1-epsilon); their TV-weighted sum equals the true difference. At epsilon=1/100 the false bound is 14553/250000 and the difference is 249851/250000. The valid inequality with actual hybrid laws is not refuted.","assumptions":["Three-bit Boolean majority","Independent, nondegenerate endpoint product laws","Fixed replacement order 1,2,3"],"domain":"product comparison proof audit"},
    {"key":"hybrid-bridge-gap","namespace":"probability.percolation","logical_name":"c0017-common-skeleton-hybrid-sensitivity-bridge-gap","kind":"concept","title":"DRAFT C0017 gap: faithful cells and uniform hybrid estimates","statement":"Audit of w417-L1: for a Boolean event on a common finite cell skeleton, two product laws mu and nu obey |E_nu f-E_mu f| <= sum_i TV(mu_i,nu_i) P_Hi(S_i), where H_i has nu_j for j<i and mu_j for j>i on the exterior, and S_i means the section in cell i is nonconstant. The finite inequality follows by telescoping and conditioning on each actual exterior; it does not require independence between the S_i events. To use it as a square-bond/triangular-site bridge, one must construct faithful full connectivity-state laws on a common skeleton and prove their summed weighted error vanishes uniformly over all intermediate laws, including boundary cells. The endpoint-majority counterexample blocks automatic substitution of homogeneous-model influences. None of these missing percolation premises is asserted here.","assumptions":["Finite common cell state spaces","Endpoint laws are products of independent cell distributions","Boolean f","Application to C0017 additionally needs the stated representation and uniform-error premises"],"domain":"C0017 universality bridge audit"}
]
for entry in entries:
    entry.update({"proof_text":None,"source":own_source(entry["key"])})
relations=[
    {"from_key":"orientation-obstruction","to_key":"weak-edge-relation","kind":"depends_on","rationale":"The obstruction satisfies exactly F_E-F_W+i(F_N-F_S)=0, the equation defined by the target entry."},
    {"from_key":"coherence-bridge","to_key":"weak-edge-relation","kind":"depends_on","rationale":"The Morera derivation assumes precisely the defined exact weak edge relation."},
    {"from_key":"coherence-bridge","to_key":"orientation-obstruction","kind":"semantic_association","rationale":"The obstruction states that separate orientation compactness does not imply scalar holomorphicity; the bridge adds a single continuous locally uniform limit over ALL edge midpoints, which excludes that example."},
    {"from_key":"principal-spin-correction","to_existing_logical":old_logical,"kind":"refutes","rationale":"Refutes only the old phrase 'the parafermionic observable has spin sigma = 2/3' under the explicit Definition 3 convention; the correction derives sigma=1/3 for q=1. No blanket refutation of the attempt is intended."},
    {"from_key":"hybrid-bridge-gap","to_key":"hybrid-endpoint-obstruction","kind":"cites","rationale":"The gap retains P_Hi(S_i) from actual intermediate laws; the counterexample gives false endpoint bound 14553/250000 versus actual difference 249851/250000, demonstrating why endpoint substitution needs an additional theorem."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w418","bundle_slug":"c0017-w418-bridge-audit-20261010-001","entries":entries,"relations":relations}
write_json(ROOT/"drafts"/"bundle_001.json",bundle)
edge_rows=[]
by_key={e["key"]:e for e in entries}
for relation in relations:
    target_key=relation.get("to_key")
    edge_rows.append({**relation,"from_statement_quote":by_key[relation["from_key"]]["statement"],"to_statement_quote":by_key[target_key]["statement"] if target_key else "the parafermionic observable has spin sigma = 2/3","target_evidence":"same bundle" if target_key else "population nodes.jsonl line 272; canonical exact-node read recorded in SOURCE_STATUS.json","status":"draft","independent_reviewer":"w419 (pending)"})
(ROOT/"EDGES.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in edge_rows),encoding="utf-8")

claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
claims[0]["remaining_gap"]="Primary full-text source scope checked; independent review and any model-transfer theorem remain pending."
for number,entry in enumerate(entries[1:],2):
    claims.append({"id":f"w418-C0017-S1.{number}","kind":entry["key"],"status":"sketch","statement":entry["statement"],"assumptions":entry["assumptions"],"source":entry["source"],"primary_context":"https://arxiv.org/abs/1208.3787" if "hybrid" not in entry["key"] else "w417 ATTEMPT.md, L1; separately derived three-bit counterexample in PAIRED_AUDIT.md","proof_or_counterexample":"INDEPENDENT_OBSTRUCTION.md and exact stencils in obstruction_measurement.json" if "hybrid" not in entry["key"] else "PAIRED_AUDIT.md; telescoping rederivation or majority enumeration in obstruction_measurement.json","independent_reviewer":"w419 (requested, pending)","remaining_gap":"Independent mathematical check; no complete C0017 bridge is proved.","review_state":"draft"})
claims.append({"id":"w418-C0017-S1.7","kind":"measured_retrieval_reasoning_failure","status":"numerical evidence","statement":"The bounded main-brain recall returned no text before its 55-second timeout (measured 55.588161 seconds). Targeted math-brain retrieval surfaced an unverified C0017 attempt with a principal-spin convention mismatch. In the local correction candidate, source-equation mismatches fall from 1 to 0; the live brain is unchanged. The exact three-case weak-edge fixture retains two holomorphic controls and reduces false route acceptances from 1 to 0 when coherence is required.","assumptions":["Measurements only on the saved command runs and explicit local fixture","No claim of a live retrieval-quality improvement or a broad benchmark"],"source":{"path":str(ROOT/"recall_measurement.json"),"additional":[str(ROOT/"SOURCE_STATUS.json"),str(ROOT/"obstruction_measurement.json")]},"proof_or_counterexample":"Recorded command output plus exact arithmetic diagnostics; not mathematical proof certification.","independent_reviewer":"w419 (pending)","remaining_gap":"Reviewer deployment and later retrievability measurement; a local proposal is not an ingested correction."})
claims={row["id"]:row for row in claims}
(ROOT/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims.values()),encoding="utf-8")

hooks=[
    {"id":"C0017-w418-01","area":"math","event":"stage-start","cue":"A proof infers scalar holomorphicity from a weak parafermionic four-edge relation without a common-limit estimate","fire_when":"Separate horizontal/vertical compactness is used to identify one holomorphic field","silent_when":"One continuous limit over all normalized edge orientations is already proved","text":"A weak edge contour identity need not identify a scalar holomorphic limit. Check coherence across edge directions, normalization and boundary data before invoking Morera; a smooth field within each direction can still average to Re z.","evidence":"w418/INDEPENDENT_OBSTRUCTION.md; obstruction_measurement.json: 849 exact stencils, split-field contour integral i","proposer":"w418"},
    {"id":"C0017-w418-02","area":"math","event":"stage-start","cue":"A cell-replacement comparison substitutes endpoint-model sensitivities for probabilities under intermediate laws","fire_when":"Endpoint arm estimates are used in a hybrid telescoping inequality without a uniform comparison theorem","silent_when":"Sensitivity is bounded under every actual hybrid law, including boundary cells","text":"In a product-law telescoping bound, each sensitivity belongs to that step's hybrid exterior law. Endpoint pivotal bounds need an additional uniform comparison theorem. Three-bit majority has tiny endpoint sensitivity and order-one hybrid sensitivity.","evidence":"w418/PAIRED_AUDIT.md; obstruction_measurement.json: endpoint bound 14553/250000 versus difference 249851/250000","proposer":"w418"}
]
assert all(len(h["text"])<=300 for h in hooks)
(ROOT/"hooks"/"math-w418.jsonl").write_text("".join(json.dumps(h,ensure_ascii=False)+"\n" for h in hooks),encoding="utf-8")

inbox=Path("~/math-brain-inbox/w418")
inbox.mkdir(exist_ok=True)
destination=inbox/"bundle_001.json"
payload=(ROOT/"drafts"/"bundle_001.json").read_bytes()
if destination.exists():
    if destination.read_bytes()!=payload: raise FileExistsError("Existing inbox draft differs; never overwrite another submission")
else:
    part=inbox/"bundle_001.part"
    if part.exists(): raise FileExistsError("Existing .part is preserved")
    part.write_bytes(payload)
    part.rename(destination)
write_json(ROOT/"BUNDLE_STATE.json",{"bundle_slug":bundle["bundle_slug"],"local_draft":str(ROOT/"drafts"/"bundle_001.json"),"inbox_path":str(destination),"submitted":True,"reviewed":False,"ingested":False,"retrievable":False,"reviewer":"w419","proof_promotions":0,"hook_proposals":"Prepared locally for reviewer submission; no global hook controls changed"})
print(json.dumps({"source_patch":str(ROOT/"patches"/"01_c0017_principal_spin.diff"),"canonical_read":canonical,"claims":len(claims),"draft_entries":len(entries),"draft_relations":len(relations),"submitted_draft":str(destination),"reviewed":False,"ingested":False,"retrievable":False},ensure_ascii=False,indent=2))
