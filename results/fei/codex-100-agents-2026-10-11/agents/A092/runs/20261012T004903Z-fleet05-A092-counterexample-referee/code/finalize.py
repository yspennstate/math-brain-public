from pathlib import Path
import json,hashlib,datetime

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
SOURCE=TEAM/'agents'/'A047'/'runs'/'20261011T220210Z-fleet05-A047-boundary-search'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):(ROOT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def claim_hash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()

original=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert original['claim_id']=='A047-SHARP-FIXED-CHILD-RARE-SELECTOR'
assert original['statement_sha256']==hashlib.sha256(original['exact_statement'].encode()).hexdigest()
review=dict(original)
review['statement_sha256']=claim_hash(review)
review['status']='ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED'
review['proof_source']={'original_run':str(SOURCE),'original_report_sha256':sha(SOURCE/'REPORT.md'),'original_claim_file_sha256':sha(SOURCE/'CLAIMS.json'),'original_statement_sha256':original['statement_sha256'],'original_hash_convention':'SHA256 of exact_statement only','canonical_hash_convention':'SHA256 of compact sorted JSON containing statement and hypotheses','audit_run':ROOT.name,'audit_report':'REPORT.md','audit_code':'code/review.py','audit_output':'out/RESULT.json'}
review['review_records']=original['review_records']+[{'reviewer':'fleet05/A092','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent finite entropy asymptotic reconstruction, projection sharpness test, direct-character ordered-pair census, recursive centered truth-table transform and independent logarithm series','endpoint_pairs':65812,'finite_certificates':20,'source':'REPORT.md; code/review.py; out/RESULT.json','repair_supplied_to_this_version':False}]
review['first_unproved_line']='This fixed-child endpoint result alone does not prove a uniform finite-p envelope; complete nonreusing stopping-tree influence payment with terminal entropy remains open.'
save('CLAIMS.json',[review])
progress={
    'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A092','gap_id':'G-BIASED-TAX','attempt_id':'A092-stage2-A047-independent-review',
    'method':'Independent analytic reconstruction and exact Boolean ordered-pair/finite-sign certificates',
    'mathematical_delta':'A047 fixed-child endpoint coefficient <=1/2, sharp and balanced-realizable, accepted at scope; 65,812 pairs and 20 rational finite certificates independently reproduced. No full FEI result.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A047_AT_STATED_SCOPE_INDEPENDENTLY_REVIEWED; FULL_FEI_OPEN',
    'claim_versions_used':['A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 (review target, independently reconstructed)'],
    'claims_created_or_changed':['A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 independent review record'],
    'source_artifacts':['REPORT.md','CLAIMS.json','SEARCH_SPEC.json','code/review.py','code/independent.py','code/finalize.py','out/CENSUS.json','out/FINITE.json','out/UNEQUAL.json','out/RESULT.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':['A046','A047','A049','A050','A057','A064','A087','A085','B09','B10','B13','B19','B20'],
    'next_action':'Audit A050 equal-overlapping-magnitude physical payment L<=4 Inf and its precise terminal-inclusive nonreusing insertion at bad nodes.',
    'stagnant_substantive_attempts':0,'blockers':['Remote supervisor copy and mirror not verified; no mathematical blocker for the scoped A047 review.'],
    'packet_ids':['A092']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B19'/'STREAM_NOTES.md']
sources += [SOURCE/n for n in ['REPORT.md','CLAIMS.json','BOUNDARY_ASYMPTOTICS.tex','code/boundary.py','code/unequal.py','out/results.json','out/unequal.json']]
sources += [AGENT/'runs'/'20261011T221121Z-fleet05-A092-counterexample-referee'/'code'/'reproduce.py']
sources += list((TEAM/'agents'/'A085'/'runs').rglob('CLAIMS.json'))
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
result=json.loads((ROOT/'out'/'RESULT.json').read_text())
assert result['status']=='PASS' and result['endpoint_pairs']==65812 and result['finite_cases']==20
assert result['runtime_seconds']<60
(AGENT/'STATUS.md').write_text('STATE: A092 stage 2 complete: A047 fixed-child sharp endpoint independently accepted; 65,812 exact pairs and 20 finite certificates PASS; full FEI OPEN.\nNEXT: Audit A050 equal-overlapping-magnitude physical payment and terminal-inclusive nonreusing insertion at bad nodes; A087/A085 challenge this review.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {ROOT.name}: Read 00:49 UTC board and B19 v2 notes. Independently reviewed A047@1: coefficient Z-D=2Z+2c-2, Cauchy/completed-square cap 1/2 and Boolean balanced attainment hold. Direct integer census of all 65,812 ordered pairs and independent rational spectra/conditional laws reproduce all 20 finite certificate signs; full arithmetic runtime {result["runtime_seconds"]:.6f}s. Exact statement unchanged, no mathematical repair supplied. Packaging caught source statement-only hash instead of registry statement+hypotheses convention; normalized exported hash while preserving legacy hash in proof_source. Updated stale A071 item using A085 scoped review. Saved all run artifacts; full FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 independently accepted: fixed finite children and fixed data biases give J=Zp log2(1/p)+O(p), M=Dp log2(1/p)+O(p), Z-D=2Z+2c-2<=1/2-2(c-1/2)^2. Sharp iff c=1/2 and H projected onto support(G) equals G/2. Boolean balanced children attain 1/2 after a fresh fair character. Disjoint spectral supports give exact M=J=h2(p). All 65,812 n<=3 pairs and 20 finite signs reproduced. A fixed-child O(p) remainder is not dimension/bias uniform and cannot be inserted into a stopping-tree ledger without a separate proof. New universal finite-p tax claims require their own reviewed source versions; global terminal-inclusive influence payment stays open.\n')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
assert set(review)==set(protocol['required_per_run']['claim_fields'])
assert review['statement_sha256']==claim_hash(review)
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
for p in ROOT.rglob('*'):
    if p.is_file():assert p.stat().st_size<20_000_000
save('out/VALIDATION.json',{'status':'PASS','at_utc':now,'protocol_field_sets_exact':True,'exact_statement_and_hypotheses_unchanged':True,'canonical_statement_hash_valid':True,'original_statement_only_hash_preserved':True,'progress_copies_identical':True,'required_report_fields':True,'all_files_under_20MB':True,'endpoint_pairs':result['endpoint_pairs'],'finite_certificates':result['finite_cases'],'arithmetic_runtime_seconds':result['runtime_seconds'],'independent_review_verdict':'ACCEPT_AT_STATED_SCOPE','mirror_status':'UNVERIFIED'})
save('out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'])
print(json.dumps({'status':'PASS','accepted_claim':'A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1','endpoint_pairs':65812,'finite_certificates':20,'local_run':str(ROOT)}))
