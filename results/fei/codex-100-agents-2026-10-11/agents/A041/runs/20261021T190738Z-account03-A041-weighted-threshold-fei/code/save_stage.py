from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parent.parent;O=R/'out'
def save(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=Path('math-open-problems/reports/fei-2026-10-11')
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
prior=A/'runs/20261014T083216Z-account05-A041-weighted-threshold-fei'
reviewbase=Path('agents/A045/runs/20261021T165712Z-account03-A045-biased-realizability-referee')
external=json.loads((reviewbase/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert external['statement_sha256']=='ce2b1fec390b3a4c95326ac3e172d77076303d633b838c50aa8dff0382d152e2'
sourcepaths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sourcepaths.append(base/'source_material/reductions/paper/biased.tex')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
sourcepaths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sourcepaths += [prior/x for x in ['REPORT.md','TWO_DIRECTION_REFERENCE.md','CLAIMS.json','code/check_stage.py','out/SOURCE_RECEIPTS.json']]
sourcepaths += [reviewbase/x for x in ['REPORT.md','PROOF.md','CLAIMS.json']]
sourcepaths += [Path('~/brain_workers/FEI100_20261011')/x for x in ['BOARD.md','claude/B09/STREAM_NOTES.md']]
context=Path('context')
sourcepaths += list(context.glob('*.txt'))
receipts=[];excerpts=[]
for p in sourcepaths:
 raw=p.read_bytes()
 try:t=raw.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError:t=raw.decode('cp1252');encoding='cp1252'
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,'scope':'source-complete report/proof or relevant-locator inspection; byte receipt is not a claim of full mathematical audit'})
 if p.suffix=='.txt':
  lines=t.splitlines();hits=[i for i,line in enumerate(lines) if any(k in line.lower() for k in ['theorem d.','corrected','symmetric threshold','mutually singular','spectral and pivotal'])][:10]
  excerpts.append('\n## '+p.name+'\n'+'\n'.join(f'{i+1}: '+' | '.join(lines[max(0,i-1):i+3]) for i in hits))
save(O/'SOURCE_RECEIPTS.json',receipts)
(O/'PAPER_LOCATORS.md').write_text('\n'.join(excerpts)+'\n',encoding='utf-8',newline='\n')
review={'claim_id':external['claim_id'],'version':external['version'],'source_statement_sha256':external['statement_sha256'],'source_actual_statement_utf8_sha256':hashlib.sha256(external['exact_statement'].encode()).hexdigest(),'source_claim_file_sha256':sha(reviewbase/'CLAIMS.json'),'verdict':'HOLDS','reviewer':'A041/account03','independent_method':'direct centered AND coefficient; integer second moment; phase-independent Boolean mean quantization','scope':'exact source statement and hypotheses; permits degree-weighted sharing; no full-FEI implication','repair_supplied':False,'proof':'PROOF.md section4','checks':'out/SHARP_CHECKS.json'}
save(O/'A045_REVIEW.json',review)
statement='For actual two-weight thresholds with independent interior product biases, let K_star be the complete max of the canonical squared-tail references, and r(U,T) the smaller nonzero jump count of the two directional physical coefficient profiles on an occupied mixed label. Then P(U,T)<=r(U,T)K_star(U,T), and C_star<=E_mixed+sum_mixed P ln r. The positive complete normalization tax is <=D_mixed ln2. For the gate with at most one zero among a+b inputs, a,b>=2, both profiles have at most two jumps at every bias, P<=2K_star, and for a=b=m the complete top-label ratio is 2-1/(m^2+(m-1)^2), proving factor2 sharp. It has a real two-weight representation for every1<w<2 and C_star<=(460+81ln2)Delta by the established symmetric-threshold baseline. Free pointwise P<=K_star and overlap sum min(K_A,K_B)>=M are false, already on a fair four-bit threshold. No unrestricted jump-count or universal signed-payment bound is asserted.'
claim={'claim_id':'A041-SHARP-QUADRATIC-COHERENCE-CHARGE','version':1,'exact_statement':statement,'hypotheses':['actual physical two-weight threshold on distinct independent Bernoulli inputs','interior product biases; deterministic coordinates contract','complete canonical squared-tail references, including off-support mass','r and logarithms used only on positive actual support; M=0 trivial','baseline-paid family additionally uses the accepted all-bias symmetric-threshold theorem'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A041/account03'],'proof_source':{'path':'PROOF.md','sha256':sha(R/'PROOF.md'),'checks':['out/OVERLAP_CHECKS.json','out/SHARP_CHECKS.json']},'proof_dependencies':['A045-QUADRATIC-TAIL-ENERGY-NORMALIZED-REFERENCE@1','A041-stage5 complete max-reference construction','supplied threshold_paper_38pp Theorem D (only family entropy payment)'],'review_records':[],'status':'ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['unregistered free pointwise quadratic domination P<=K_star','unregistered overlap lower bound sum min(K_A,K_B)>=M'],'first_unproved_line':None,'next_consumers':['A044','A045','A043','A090','A091','B20']}
save(R/'CLAIMS.json',[claim])
prior_versions=[{'claim_id':x['claim_id'],'version':x['version'],'statement_sha256':x['statement_sha256']} for x in json.loads((prior/'CLAIMS.json').read_text(encoding='utf-8')) if x['claim_id'] in ('A041-TWO-DIRECTION-COMPLETE-QUADRATIC-REFERENCE','A045-QUADRATIC-TAIL-ENERGY-NORMALIZED-REFERENCE')]
claim['proof_dependencies']=prior_versions+['supplied threshold_paper_38pp Theorem D; exact bytes in out/SOURCE_RECEIPTS.json; used only for family entropy payment']
save(R/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B09','packet_id':'A041','gap_id':'G-BIASED-LTF-MIXED-SIGNED-CROSS-ENTROPY','attempt_id':'A041-sharp-log-coherence-v1','method':'independent admission review; exact rational finite falsification; all-bias alternating-sum formulas; signed Cauchy replacement','mathematical_delta':'Sharp factor2 two-jump reference control; free atom and overlap domination refuted; universal mass tax sharpened to D ln2; A045 admission obstruction independently HOLDS. Universal signed payment remains open.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_OBSTRUCTIONS; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':external['claim_id'],'version':1,'statement_sha256':external['statement_sha256']},'A045-QUADRATIC-TAIL-ENERGY-NORMALIZED-REFERENCE@1','A041-stage5 source-complete run20261014T083216Z','threshold_paper_38pp Theorem D'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['PROOF.md','out/A045_REVIEW.json','out/SOURCE_RECEIPTS.json','out/OVERLAP_CHECKS.json','out/SHARP_CHECKS.json','out/FORMAL_STATUS.json'],'next_consumers':['A044','A045','A043','A090','A091','B20'],'next_action':'Bound joint diagonal tail entropy plus actual coherence logarithm beyond two jumps from SAME mixed deficit, with ordinary KL, off-support mass and both full terminals retained.','stagnant_substantive_attempts':1,'blockers':['Universal C_star-M KL<=K D not proved.','New A041 claim awaits independent review; supervisor copying/adoption/mirror unverified.'],'packet_ids':['A041']}
progress['claim_versions_used']=[progress['claim_versions_used'][0]]+prior_versions+['threshold_paper_38pp Theorem D; exact source hash in out/SOURCE_RECEIPTS.json']
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
formal=O/'FORMAL_STATUS.json'
if not formal.exists():save(formal,{'rung':'ANALYTIC_PROOF_EXACT_CHECKS','Lean':'PENDING_SUBMITTED','statement':'example (x y : R) : (x+y)^2 <=2*(x^2+y^2)','limit':'Only the scalar Cauchy step was submitted; no claim of full formalization.'})
status='STATE: Stage6 complete locally: sharp factor2 two-jump quadratic coherence, free domination/overlap refuted, tax<=D ln2; A045 admission scoped HOLDS;15,701 exact assertions; full FEI OPEN.\nNEXT: Pay joint diagonal tail entropy plus actual coherence logarithm beyond two jumps from SAME mixed deficit with full KL/off-support/terminals; A044/A045 consume, A090/A091 review.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8',newline='\n')
stamp=datetime.now(timezone.utc).isoformat()
entry=f'\n## {stamp} — account03 stage6\nRecovered source-complete stage5 from20261014; later account05 folders empty. Independently accepted A045 exclusive-profile admission obstruction at originalce2b1fec... scope. Free P<=K_star and overlap>=M failed exactly. All-bias at-most-one-zero gate has sharp top ratio2-1/[m^2+(m-1)^2], while two-jump Cauchy supplies P<=2K and full reference payment at baseline rate plusln2. Generic replacement has logarithmic jump-count charge, still unpaid universally. Tax sharpened2D/e toD ln2. 840+95 fixed cases,15,701 exact primary assertions. No full FEI result; no work stopped or detached. Run:{R.name}.\n'
if R.name not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
 with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
learn='\n## Stage6: sharp coherence charge\n* Canonical signed r-jump physical profiles give P<=r_A K_A and P<=r_B K_B, hence C_star<=E_mix+sum P ln min(r_A,r_B); this logarithmic charge is not yet paid universally.\n* Actual at-most-one-zero gate with a=b=m has top P/K_star=2-1/[m^2+(m-1)^2] at EVERY interior bias. It is a real two-weight threshold for1<w<2,t=aw+b-w. Thus free domination is false and pointwise factor2 is sharp in the two-jump class.\n* Every coefficient profile of that gate has at most two jumps, giving P<=2K and C_star<=(460+81ln2)Delta using the accepted symmetric baseline; full terminals remain paid.\n* Fair four-bit N>=3: M17/64,D39/64,Z29/64,overlap13/64. Overlap>=M is false. D-Z=reference high-degree slack+overlap-M; no general Z<=D proof follows from840 finite tests (max56/61).\n* Positive complete mass tax improves2D/e toD ln2 because M<=D and Z<=D+M. This sharpens an already-paid cost and does not pay signed cross-entropy.\n* A045 exclusive integer-profile obstruction@1 independently HOLDS at originalce2b1fec... hash: integer second moment forces every AND top-packet fraction>=1, but d/(d-1)<=3/2 leaves degree sharing viable; normalized AND3 deletion empty mass3/5 rejects all phases.\n* Never infer completed mathematics from empty later account05 directories. Source-complete stage5 is20261014T083216Z.\n'
if '## Stage6: sharp coherence charge' not in (A/'LEARNED.md').read_text(encoding='utf-8'):
 with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(learn)
expected_claim=set(protocol['required_per_run']['claim_fields']);expected_progress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==expected_claim;assert set(progress)==expected_progress
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'REPORT.md').read_text(encoding='utf-8').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
for h in protocol['required_per_run']['report_fields']:assert '# '+h in (R/'REPORT.md').read_text(encoding='utf-8')
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
save(O/'SCHEMA_VALIDATION.json',{'schema_fields_exact':True,'progress_compatibility_bytes_equal':True,'status_two_lines':True,'report_fields_and_final_bridge':True,'files_below20MB':True,'primary_assertions':15701,'local_only':True})
files=[p for p in R.rglob('*') if p.is_file()]
save(O/'PERSISTENCE_RECEIPTS.json',[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files if p.name!='PERSISTENCE_RECEIPTS.json'])
print(json.dumps({'run':R.name,'protocol':'PASS','files':len(files),'claims':1,'independent_review':review['verdict'],'full_FEI':'OPEN'}))
