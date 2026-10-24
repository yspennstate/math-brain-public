from pathlib import Path
import json,hashlib,datetime
from fractions import Fraction as F
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parents[1]
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
grid=json.loads((RUN/'out/grid_certificate.json').read_text()); winner=json.loads((RUN/'out/exact_winner.json').read_text()); boundary=json.loads((RUN/'out/boundary_certificate.json').read_text())
assert grid['complete'] and grid['cases']==458356
assert winner['exact_grid_maximum']=='26-12*log2(3)' and winner['assertions']==44
assert boundary['complete'] and boundary['assertions']==190
assert F(boundary['rows'][2]['ratio_lower'])>7
prior=ROOT/'runs/20261011T221757Z-account05-A043-prime-gate-decomposition'
source_paths=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B09\STREAM_NOTES.md'),prior/'REPORT.md',prior/'CLAIMS.json',prior/'PRIME_GATE_DEFINITION.tex',prior/'PRIME_ENDPOINT_IMPLICATION.md',prior/'out/main_census.json',Path(r'~\brain_workers\FEI100_20261011\agents\A042\runs\20261012T002547Z-account05-A042-bias-endpoint-certificates\REPORT.md')]
sources=[]
for p in source_paths:
 raw=p.read_bytes(); text=raw.decode('utf-8-sig'); sources.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':'protocol/dispatch or prime definition; source loaded; no binary sharp theorem assumed'})
save(RUN/'out/source_receipts.json',sources)
statement=('For every essential prime sign gate of arity 2,3,4 at every product law with each input probability in {1/4,1/2,3/4}, the exact maximum corrected Hplus/(I-Var) is 26-12log2(3), attained by sign OR2 at (1/4,1/4). The complete certificate covers 458356 symmetry representatives of 4639338 labeled gate/bias cases. For the essential prime sign majority3 at probabilities (1-q^3,q,q), the ratio tends to 2+4/ln(2) as q decreases to zero; at q=1/8 it exceeds 73411827299/10000000000>7. Thus an all-interior-bias corrected constant 7 for nonbinary primes of arities 3 or 4 is false. No all-bias supremum, divergent family, or full FEI result is asserted.')
hypotheses=['uniform definition of genuine disjoint essential primes from A043 stage 1','corrected spectral entropy in bits and spectral influence in the normalized product basis','finite grid probabilities exactly {1/4,1/2,3/4} for the maximum theorem','output-negation and reflected-bias symmetries preserve the ratio and prime property','nonbinary boundary statement uses the actual majority3 truth table, q in (0,1/2), r=q^3','all-prime all-bias universal endpoint remains open']
claim={'claim_id':'A043-PRIME-GRID-AND-BOUNDARY','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A043/account05'],'proof_source':{'run_id':RUN.name,'paths':['REPORT.md','MAJORITY_BOUNDARY.md','out/grid_certificate.json','out/exact_winner.json','out/boundary_certificate.json','code/certify_grid.py','code/verify_winner.py','code/certify_boundary.py']},'proof_dependencies':[{'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'scope':'essential-prime definition and cofactor criterion only; exact vectorized census also checked','source':str(prior/'PRIME_GATE_DEFINITION.tex'),'status':'SOURCE_COMPLETE_ANALYTIC_INTERFACE_LEAD_RECONSTRUCTION; INDEPENDENT_REVIEW_PENDING'}],'review_records':[],'status':'FINITE_CERTIFICATE_AND_ANALYTIC_BOUNDARY_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['All interior product biases on nonbinary essential primes of arities three or four satisfy corrected Hplus <= 7(I-Var).'],'first_unproved_line':None,'next_consumers':['A042','A044','A045','A091','A090','B09','B20']}
save(RUN/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B09','packet_id':'A043','gap_id':'G-A043-CONTINUOUS-PRIME-RATIO','attempt_id':'A043-stage2-grid-and-mixed-rate-boundary','method':'exhaustive exact cofactor classification, floating discovery, weighted integer Fourier moments, outward integer logarithm intervals, rational maximum comparisons, direct Fraction boundary spectra and analytic asymptotic','mathematical_delta':'Exact n<=4 grid maximum 26-12log2(3); all 4639338 labeled grid cases covered; prime majority3 mixed-rate path tends to 2+4/ln(2) and gives a certified off-grid ratio >7.34118. Continuous biased prime supremum and full FEI remain open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'FINITE_GRID_MAXIMUM_AND_NONBINARY_BOUNDARY_PROVED; CONTINUOUS_TARGET_OPEN; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'scope':'prime definition/cofactor criterion'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['REPORT.md','MAJORITY_BOUNDARY.md','out/grid_certificate.json','out/log_intervals.json','out/exact_winner.json','out/boundary_certificate.json','out/source_receipts.json'],'next_consumers':['A042','A044','A045','A091','A090','B09','B20'],'next_action':'A091/A090 reconstruct the certificate and majority endpoint; then classify mixed-rate endpoint expansions of ternary prime symmetry classes, preserving actual variance deficit.','stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A043']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
protocol=json.loads(source_paths[0].read_text(encoding='utf-8-sig'))
fields={('packet_ids' if f.startswith('packet_ids (') else f) for f in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((RUN/'PACKET_DELTA.json').read_text())==progress
report=(RUN/'REPORT.md').read_text(encoding='utf-8'); assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
save(RUN/'out/schema_check.json',{'claim_fields':'PASS','progress_fields':'PASS','packet_ids_annotation_normalized':True,'packet_delta_identical':True,'report_fields':'PASS','grid_certificate_complete':True,'exact_grid_winner_verified':True,'boundary_direct_reconstruction':True,'finite_constant_7_nonbinary_refuted':True,'continuous_supremum':'OPEN','independent_review':'PENDING','full_FEI':'OPEN'})
summary=[]
for n in [2,3,4]:
 rows=[r for r in grid['records'] if r['n']==n]
 lo=max(F(r['lower']) for r in rows); hi=max(F(r['upper']) for r in rows)
 summary.append({'n':n,'grid_maximum_lower':str(lo),'grid_maximum_upper':str(hi),'canonical_upper_witness':max(rows,key=lambda r:F(r['upper']))})
save(RUN/'out/dimension_summary.json',summary)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT/'STATUS.md').write_text('STATE: A043 stage 2 complete: exact biased-prime grid maximum 26-12log2(3), 458356 certified representatives; prime Maj3 boundary tends to 2+4/ln2 and exceeds 7 off-grid; review pending; full FEI OPEN.\nNEXT: A091/A090 review exact grid and endpoint; classify ternary prime mixed-rate boundary expansions before extending any grid bound to all biases.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(now+': Stage 2 consumed B09 v2 finite-prime bias assignment and review-cap guard. Full grid discovery 1.1958 s; Fraction log implementation hit time cap; repaired integer interval implementation certified all 458356 representatives in 2.3398 s. Exact maximum 26-12log2(3), 44 winner checks; 190 direct Fraction boundary checks, analytic majority3 path tends to 2+4/ln2; q=1/8 is >7.34118. Protocol files and local receipts saved. Continuous all-bias target and FEI open; no divergent family or independent acceptance claimed.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage 2: On all primes n=2,3,4 with each bias in {1/4,1/2,3/4}, exact corrected ratio maximum is 26-12log2(3), at sign OR2 and quarter biases. Exhaustive integer/Fraction certificate covers 458356 representatives of 4639338 labeled cases. Quarter-bias moments have squared masses N_S^2/(D^2 3^k), so a finite rational log table suffices. Use arbitrary integers for ratio cross-products.\n\nPrime majority3 at probabilities (1-q^3,q,q) has delta=4q^2+O(q^3), corrected H=(8+16/ln2)q^2+O(q^3), hence ratio tends to 2+4/ln2. At q=1/8 its exact certified ratio exceeds 7.34118. Moderate-grid bound 7 therefore fails already on a nonbinary prime outside the grid. The all-bias supremum is not certified; this is a finite strong-helper obstruction, not ordinary FEI failure.\n')
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='receipts.json':
  raw=p.read_bytes();assert len(raw)<20*1024*1024;receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=ROOT/name;raw=p.read_bytes();receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(RUN/'out/receipts.json',{'saved_at_utc':now,'local_only':True,'review':'PENDING','remote_mirror':'NOT_VERIFIED','files':receipts})
print(json.dumps({'schema':'PASS','files_hashed':len(receipts),'representatives':grid['cases'],'per_case_exact_checks':4*grid['cases'],'winner_checks':winner['assertions'],'boundary_checks':boundary['assertions'],'grid_exact_maximum':winner['exact_grid_maximum'],'continuous_supremum':'OPEN','full_FEI':'OPEN'},indent=2))
