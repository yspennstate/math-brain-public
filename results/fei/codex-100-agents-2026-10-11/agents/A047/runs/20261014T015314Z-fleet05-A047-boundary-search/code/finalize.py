from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];ROOT=R.parents[1];TEAM=ROOT.parents[1]
protocolpath=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
d=json.loads((R/'out/CHECK.json').read_text());pilot=json.loads((R/'out/PILOT.json').read_text())
assert d['status']=='PASS' and d['cases']==5475 and d['shared_cases']==1024
assert pilot['status']=='PASS' and pilot['cases']==355 and pilot['runtime_seconds']<60 and d['runtime_seconds']<300
src=TEAM/'agents/A050/runs/20261014T004109Z-fleet05-A050-repair-with-scope'
review=json.loads((src/'CLAIMS.json').read_text())[0]
review['proof_source']=[str(src/p) for p in review['proof_source']]
review['review_records']=review['review_records']+[{'reviewer':'A047','verdict':'ACCEPT_AT_STATED_UNIFORM_SCOPE','source_run':R.name,'independence':'Direct centered moments and reconstructed deletion rows; no A050 checker replayed','evidence':['PROOF.md section 5','out/CHECK.json'],'scope':'All source clauses including exact identity, endpoints, sharpness and conversion; no bank-supply conclusion'}]
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A047'
statement=('For every actual Boolean sign under an independent interior product law and finite deterministic fresh-singleton physical stopping tree, let S be the coherent root Fourier set, Pi its transcript, W=S minus Q(Pi), and A contain every potentially queried coordinate. '
 'Set a_i=P(i in S) for i in A, r_i=P(i in S intersect Q), a=sum a_i, r=sum r_i, R_phys=I_phys(f)-E I_phys(f_leaf). '
 'Then a_i=4p_i(1-p_i)Inf_i^phys(f), r_i=sum_{v querying i}w_v4p_i(1-p_i)Inf_i^phys(f_v), a_i-r_i equals expected terminal spectral i-influence, and r<=R_phys. '
 'With e=I(W;Pi|S), one normalized coordinate-product deletion reference with theta_i=r_i/a_i gives the exact identity e+E KL(P(D|S)||rho(.|S))=C_coord=sum_i a_i h2(r_i/a_i), including zero/full-deletion endpoints. '
 'Thus e<=C_coord<=a h2(r/a)<=a<=I_phys(f). Actual descendant conversion together with output release costs at most 2R_phys/ln2+C_coord/2 (uniform R_phys/ln2+C_coord/2). '
 'Terminal independence of A forces C_coord=e=0 even with variable query sets and shared terminal cores. '
 'For three-bit biased parity queried first on coordinate 0 and then coordinate 1 or 2 according to outcome, e=(b1+b2-b1*b2)h2(p0), C_coord=(b1+b2)h2(p0), and exact KL=b1*b2*h2(p0), where bi=4pi(1-pi). '
 'On p0=epsilon,p1=epsilon^2,p2=3/4, common-capacity/C_coord tends to 19/3. No conditional transcript bank funding or FEI theorem is established.')
hyp=['Bits; fixed independent interior product law and actual inherited centered Fourier bases','Finite deterministic tree with no repeated physical coordinate on a path','Ambient root and terminal labels retained; A fixed before the tree','Physical pivotal and biased spectral influences distinguished','All terminal entropy/influence and the signed residual retained']
claim={'claim_id':'A047-PRODUCT-COORDINATE-DELETION-REPAIR','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A047'],'proof_source':['PROOF.md','code/audit.py','out/CHECK.json','out/PARITY_BOUNDARY.json'],'proof_dependencies':[],'review_records':[],'status':'NARROW_PRODUCT_EXTENSION_PROVED_LOCALLY_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'A compatible normalized complete reference funds H(Pi|W)/2 jointly with signed erasure and all terminal Fourier entropy using nonduplicated physical influence.','next_consumers':['A050','A048','A092','A087','A039','A064','B10','B20']}
reviewnote={'source_claim':review['claim_id']+'@1','source_statement_sha256':review['statement_sha256'],'verdict':'ACCEPT_AT_STATED_SCOPE','reviewer':'A047','repair_to_source':'NONE','new_extension_separate':claim['claim_id']+'@1','evidence':['PROOF.md section 5','out/CHECK.json'],'remaining_unproved_line':claim['first_unproved_line']}
(R/'out/REVIEW_A050.json').write_text(json.dumps(reviewnote,indent=2),encoding='utf8')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B10','packet_id':'A047','gap_id':'FEI-B10-A047-INITIAL','attempt_id':'A047-boundary-04','method':'Independent A050 active-label review; exact product-biased coordinate deletion reference; analytic unequal-bias endpoint','mathematical_delta':f'A050 active-label repair independently accepted; product spectral budget and coordinate-resolved KL repair proved; {d["cases"]} cases/{d["assertions"]} exact assertions; unequal-bias common-capacity/coordinate-capacity limit19/3.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'NARROW_REPAIR_PROVED; REVIEW_ACCEPTED_AT_SOURCE_SCOPE; FULL_FEI_OPEN','claim_versions_used':['A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1 (independently reconstructed)','A048-ACTUAL-DESCENDANT-SCHEDULE-INJECTION@1 (sharpness reconstructed)'],'claims_created_or_changed':[review['claim_id']+'@1 (local independent review)',claim['claim_id']+'@1'],'source_artifacts':['REPORT.md','PROOF.md','FROZEN_SPEC.json','code/audit.py','out/PILOT.json','out/CHECK.json','out/PARITY_BOUNDARY.json','out/REVIEW_A050.json'],'next_consumers':claim['next_consumers'],'next_action':'On the controller-resolved three-output shared-core priority tree, price the actual normalized-reference H(Pi|S minus A)/2 jointly with signed erasure and full terminal core entropy; no new schedule reserve.','stagnant_substantive_attempts':0,'blockers':['Universal conditional-history bank funding remains unproved','New extension independent review and supervisor mirrors pending'],'packet_ids':['A047']}
for c in [review,claim]:assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
(R/'CLAIMS.json').write_text(json.dumps([review,claim],indent=2),encoding='utf8')
for name in ['PROGRESS.json','PACKET_DELTA.json']:(R/name).write_text(json.dumps(progress,indent=2),encoding='utf8')
sources=[protocolpath,TEAM/'BOARD.md',TEAM/'claude/B10/STREAM_NOTES.md',src/'REPORT.md',src/'PROOF.md',src/'CLAIMS.json']
for agent,run,names in [('A048','20261013T234007Z-fleet05-A048-tensor-stress',['REPORT.md','PROOF.md']),('A083','20261013T234228Z-fleet05-A083-formal-core',['REPORT.md']),('A092','20261013T222550Z-fleet05-A092-counterexample-referee',['REPORT.md']),('A039','20261013T235428Z-fleet05-A039-projection-under-restrictions',['REPORT.md'])]:
    sources.extend(TEAM/'agents'/agent/'runs'/run/name for name in names)
sources.extend([ROOT/'runs/20261013T221434Z-fleet05-A047-boundary-search/code/conversion.py'])
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps([{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sources],indent=2),encoding='utf8')
report=f'''# exact target, quantifiers, hypotheses and units

Independently review A050's new uniform active-label schedule repair, then repair its prospective use at unequal product biases. For every finite actual Boolean sign under an independent interior product law and fresh-coordinate singleton physical stopping tree, derive the exact coordinate-resolved normalized deletion reference. Bits; physical pivotal influence is distinguished from expected Fourier label cardinality. Full FEI remains OPEN. This is a narrow existing-mechanism repair, not a new broad potential.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start and targeted current entries, B10 STREAM_NOTES v2 (2026-10-11 23:31Z), own STATUS and previous stage code/proof interface. Read execution protocol fully, revision {protocol['revision']}. Consumed A050 run 20261014T004109Z REPORT/PROOF/CLAIMS, sections1-5; A048 run20261013T234007Z REPORT/PROOF, actual terminal-label injection and guard; A083 run20261013T234228Z report, root-to-terminal distinction; A092 run20261013T222550Z report, conversion and first unsupported line. A039's latest report was inspected for its next reset target; no optimum theorem is used. Source byte receipts are saved in out/SOURCE_RECEIPTS.json. Earlier campaign and manuscript readings remain previous-stage context; no new external theorem, citation or priority claim is used.

The lead's original finite real-versus-Boolean task is complete in earlier stages. Protocol dispatch consumes the useful new A050 dependency rather than repeating the tax or indexed-parity failure.

# complete derivation or exact first unsupported line

PROOF.md contains the complete proof. Spectral deletion uses r_i=4p_i(1-p_i) times the consumed physical i-influence; r=sum r_i<=R_phys. With a_i=root spectral i-marginal, ONE normalized conditional subset reference with coordinate probabilities r_i/a_i gives e+E KL=sum a_i h2(r_i/a_i)<=a h2(r/a). Endpoint support is checked explicitly. Thus the uniform capacity is independently accepted and a strictly sharper heterogeneous capacity is available under all interior product laws. It is invalid to substitute R_phys into a binary entropy argument without a separate check.

The exact adaptive three-bit parity injection and KL rebate are (b1+b2-b1*b2)h2(p0) and b1*b2*h2(p0). Along p0=epsilon,p1=epsilon^2,p2=3/4 the common capacity overcharges the coordinate capacity by a factor tending to19/3. These are analytic identities/expansions and exact finite certificates. The conversion extension costs <=2R_phys/ln2+C_coord/2, or R_phys/ln2+C_coord/2 at fair bias. Controller-resolved leaves have zero injection despite variable final query sets and shared terminal data.

FIRST UNSUPPORTED LINE: a normalized compatible complete reference funds H(Pi|W)/2 jointly with signed erasure and complete terminal Fourier entropy from nonduplicated physical influence. The deletion reference pays only its code cost and gives no universal bank funding. The complete spectral ledger is retained and verified exactly.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded computation. {d['cases']} cases: all278 Boolean tables n=0..3 under four fixed rational product laws and four policies (4,448 trees); all256 ordered two-bit shared core pairs in a three-controller priority function under two laws and two policies (1,024 trees); three adaptive parity boundary laws. No symmetry quotient or dimension escalation. Maximum directly enumerated n=5. Direct centered moments reconstruct squared spectra, physical edges give pivotal influence, and coherent conditional rows give exact root/transcript/terminal joints. Exact Fraction and integer-log vectors verify the budgets, conditional KL equality, normalized reference and retained terminal ledger. A borrowed A047 symbolic entropy utility is pinned; no A050 checker was replayed. Factor proposals from sympy are independently verified by integer product; primality is unnecessary for these equality certificates. No floating-point sign or numerical extrapolation is a certificate.

Commands from A047: python -X utf8 runs/{R.name}/code/audit.py --pilot, then the same without --pilot. Final pilot PASS:355 cases/{pilot['assertions']} assertions in {pilot['runtime_seconds']:.4f}s. Final main PASS:{d['cases']} cases/{d['assertions']} assertions in {d['runtime_seconds']:.4f}s. Two draft main invocations were stopped without final results after352-case checkpoints; out/VALIDATION_REPAIR.md records the arithmetic performance repair. Frozen mathematical domain and claims were unchanged. No stopped attempt is called PASS. Memory estimate100MB, no >300MB job was launched, no GPU or background job. Results saved at each dimension, shared-law batch and completed boundary set.

# proof dependencies and changed downstream conclusions

A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1 receives ACCEPT_AT_STATED_SCOPE with no source repair; proof, normalization, endpoint, sharpness and conversion are independently reconstructed. The product coordinate extension is a separate narrow contributed repair pending A050/A092 review. Both proofs are self-contained; A048's sharpness family is reconstructed explicitly. No shared registry or another agent file was modified. Consumers may use exact coordinate capacity in place of the coarser common reference, while preserving the distinction between physical and spectral budgets. No universal FEI constant improves.

# one next mathematical action and independent reviewer

On the controller-resolved three-output shared-core priority tree, place the actual prescribed complete reference on W=S minus A and pay/test H(Pi|W)/2 together with signed erasure and full terminal core entropy. No schedule charge remains at that interface. Independent reviewers for the extension: A050 primary/A092 alternate, with A087 checking influence ownership. A039/A064 are mathematical consumers. Saved handoffs only; no message was sent.

# actual persistence receipts or precise save blocker

The four required protocol files, complete proof, frozen spec, code and exact outputs are saved under this run. STATUS is exactly two lines; WORKLOG/LEARNED append this stage. Finalization verifies exact schemas, equal progress copies, successful frozen case counts and all file sizes below20MB. out/PERSISTENCE.json provides local hashes and byte counts. No local save blocker. Supervisor mirrors, downstream use and independent acceptance of the extension remain pending, not claimed.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree consumption by independently accepting A050's schedule repair, proving the correct weighted deletion budget for unequal biases and refining its normalized reference to coordinate-specific probabilities with an exact KL rebate; {d['cases']} actual Boolean/tree cases retain the full terminal ledger. The missing universal bridge remains the actual H(Pi|S minus A)/2 bank plus signed erasure and terminal entropy funded once. NEXT attacks that precise surviving interface after controller dependence is resolved, the shortest route identified toward full FEI rather than another isolated class bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
assert all(h in report for h in protocol['required_per_run']['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
(ROOT/'STATUS.md').write_text(f'STATE: A047 stage4 complete: A050 active-label repair independently accepted; product coordinate deletion/KL repair proved; {d["cases"]} cases/{d["assertions"]} exact assertions PASS; extension review pending; FEI OPEN.\nNEXT: A050/A092 review weighted coordinate repair; A039/A064 fund H(Pi|S minus A)/2 on the controller-resolved three-output shared-core tree with one influence account and full terminal entropy.\n',encoding='utf8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf8') as f:f.write(f'\n2026-10-14 stage4 ({R.name}): Read current board/B10 and A050 new repair. Independently accepted uniform scope; derived product-weighted coordinate deletion code and exact KL rebate. Adaptive unequal-bias parity common/coordinate capacity tends to19/3. Initial main stopped without result due entropy-factor performance; integer-product-checked log decompositions and factored cross-entropy repaired arithmetic; the unnecessary draft trial-primality check was removed. Final355-case pilot and {d["cases"]}-case main passed {d["assertions"]} assertions. Conditional history bank still unpaid; FEI OPEN.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf8') as f:f.write('\nStage4 durable repair: Under product biases, spectral deletion r_i=4p_i(1-p_i) times consumed physical i-influence. One coordinate-product deletion reference gives H(D|S)+E KL=sum a_i h2(r_i/a_i), no endpoint support gap. This is <=a h2(r/a)<=a<=I_phys, but R_phys cannot replace r inside h2 without justification. Terminal independence of query-superset A makes W=S minus A despite variable queried sets. Adaptive biased three-bit parity has e=(b1+b2-b1b2)h2(p0), exact KL=b1b2h2(p0); at p0=epsilon,p1=epsilon^2,p2=3/4 common/coordinate capacity tends to19/3. Reference normalization does not fund H(Pi|W)/2 or terminal Fourier entropy.\n')
assert len((ROOT/'STATUS.md').read_text().splitlines())==2
files=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json' and '__pycache__' not in p.parts:
        assert 0<p.stat().st_size<20*1024*1024
        files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'out/PERSISTENCE.json').write_text(json.dumps({'saved_at':datetime.now(timezone.utc).isoformat(),'files':files,'rolling':[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'mirror':'UNVERIFIED','extension_independent_review':'PENDING','source_review':'A050 ACCEPT_AT_STATED_SCOPE'},indent=2),encoding='utf8')
print(f'PASS: {len(files)} run files persisted; schemas, case counts, proof/source receipts and rolling files checked')
