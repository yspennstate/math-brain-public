from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[1]
def save(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('Every finite Boolean function admits a terminating genuine disjoint read-once decomposition into essential primes, constants and literals, where a prime has no block B of size 2 through n-1 with exactly two distinct cofactor rows. The corrected product-biased inequality Hplus<=C(I-Var) holds for all primes of all arities and all interior product laws iff it holds for every Boolean function under every interior product law, with the same C. Either condition implies ordinary uniform FEI with constant max(C,log2(e)). The exact labeled census has 10,104,57240 essential primes and 0,114,7354 essential decomposable functions at n=2,3,4 respectively. No finite universal C is proved.')
hypotheses=['Boolean sign functions on finite cubes','genuine disjoint physical supports, no variable reuse','remove irrelevant coordinates before classifying essential gates','constants and unary literals terminal; essential binary gates prime','product orthonormal Fourier basis and spectral influence','corrected entropy in bits; all interior product laws and all prime arities in conditional antecedent','the implication antecedent remains open; no converse from ordinary uniform FEI asserted']
claim={
 'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A043/fleet05'],
 'proof_source':{'run_id':RUN.name,'paths':['REPORT.md','PRIME_GATE_DEFINITION.tex','PRIME_ENDPOINT_IMPLICATION.md','out/main_census.json','out/independent.json']},
 'proof_dependencies':[{'source':'out/source_manifest.json','theorem':'threshold 38pp Section 7 Proposition 7.1 equations (67)-(70), Corollary 7.2; reconstructed in PRIME_ENDPOINT_IMPLICATION.md','status':'SOURCE_COMPLETE_BASELINE_RECONSTRUCTED'}],
 'review_records':[], 'status':'ANALYTIC_PROOF_AND_EXACT_CENSUS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[], 'first_unproved_line':None,'next_consumers':['A044','A059','A091','A090','B20']}
save(RUN/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B09','packet_id':'A043',
 'gap_id':'FEI-B09-A043-INITIAL','attempt_id':'A043-stage1-cofactor-primes',
 'method':'exact cofactor-row criterion, well-founded disjoint factorization, induced product-law transport and strong-entropy cancellation; fixed n<=4 exact census',
 'mathematical_delta':'Packet reduction proved: all-product corrected prime FEI+ equivalent to universal corrected product FEI+ at the same constant and sufficient for ordinary uniform FEI at max(C,log2(e)); no finite C proved. Census certifies unbounded-arity threshold primes and most essential n=4 tables remain prime.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING',
 'mathematical_status':'DECOMPOSITION_AND_CONDITIONAL_ENDPOINT_PROVED_UNREVIEWED; FULL_FEI_OPEN',
 'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','PRIME_GATE_DEFINITION.tex','PRIME_ENDPOINT_IMPLICATION.md','out/source_manifest.json','out/pilot_census.json','out/main_census.json','out/independent.json'],
 'next_consumers':['A044','A059','A091','A090','B20'],
 'next_action':'A091/A090 independently reconstruct the prime criterion and induced-bias cancellation; A044 apply the criterion to a non-symmetric family and seek a bias-uniform corrected prime payment.',
 'stagnant_substantive_attempts':0,'blockers':[], 'packet_ids':['A043']}
save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
expected_progress_fields={('packet_ids' if x=='packet_ids (one primary ID, for compatibility)' else x) for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress_fields
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((RUN/'PACKET_DELTA.json').read_text())==progress
main=json.loads((RUN/'out/main_census.json').read_text())
ind=json.loads((RUN/'out/independent.json').read_text())
assert main['complete'] and main['counts'][3]['prime']==57240
assert main['assertions']==205811
assert ind['n3_prime']==104 and ind['n3_decomposable']==114
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
save(RUN/'out/schema_check.json',{'protocol_revision':protocol['revision'],'exact_claim_fields':True,'exact_progress_fields':True,'protocol_field_annotation_normalization':{'packet_ids (one primary ID, for compatibility)':'packet_ids'},'packet_delta_identical':True,'all_report_fields_present':True,'census_complete':True,'independent_finite_reconstruction':True,'independent_review':False,'full_FEI':'OPEN'})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT/'STATUS.md').write_text('STATE: A043 packet complete locally: prime decomposition and corrected all-bias endpoint equivalence proved; 205,811 main exact assertions; review pending; full FEI OPEN.\nNEXT: A091/A090 review cofactor criterion and induced-bias cancellation; A044 seek a bias-uniform payment on surviving non-symmetric primes.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(now+': Completed terminating disjoint prime proof, all-product corrected endpoint equivalence, ordinary uniform consequence max(C,log2(e)), and unbounded-arity threshold primes. v1 checker stopped with no result; v2 pilot passed 1487 assertions in 0.0070 s; full n<=4 census passed 205811 assertions in 39.0173 s. Independent n=3 substitution generation passed '+str(ind['assertions'])+' assertions. All files local; independent review and supervisor/mirror copy pending.\n')
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='receipts.json':
  raw=p.read_bytes(); assert len(raw)<20*1024*1024
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=ROOT/name; raw=p.read_bytes(); receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(RUN/'out/receipts.json',{'saved_at_utc':now,'local_only':True,'independent_review':'PENDING','remote_mirror':'NOT_VERIFIED','files':receipts})
print(json.dumps({'schema_checks':'PASS','run_files_hashed':len(receipts),'main_assertions':main['assertions'],'independent_assertions':ind['assertions'],'prime_counts':[x['prime'] for x in main['counts']],'full_FEI':'OPEN'},indent=2))
