from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1];TEAM=AGENT.parents[1]
SOURCE=TEAM/'agents'/'A050'/'runs'/'20261013T212442Z-account05-A050-repair-with-scope'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):(ROOT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def chash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
original=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert original['claim_id']=='A050-OUTPUT-CONDITIONAL-TAX-REPAIR'
legacy=hashlib.sha256(original['exact_statement'].encode()).hexdigest()
assert original['statement_sha256'] in [legacy,chash(original)]
accepted=dict(original)
accepted['statement_sha256']=chash(accepted)
accepted['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
prior=TEAM/'agents'/'A046'/'runs'/'20261013T215251Z-account05-A046-current-candidate-intake'/'CLAIMS.json'
prior_record=json.loads(prior.read_text(encoding='utf-8-sig'))[0]
assert prior_record['exact_statement']==original['exact_statement'] and prior_record['hypotheses']==original['hypotheses']
accepted['review_records']=prior_record['review_records']+[{'reviewer':'account05/A092','verdict':'ACCEPT_AT_STATED_SCOPE','source':'REPORT.md; code/audit.py; out/RESULT.json; out/UNDERREFUND.json','method':'Independent analytic repair and sharpness reconstruction; recursive centered truth-table spectra; direct coherent root/transcript joint; exact prime-log entropy cancellations; independent extreme-endpoint sign certificate','substantive_repair_supplied':False}]
accepted['proof_source']={'original_run':str(SOURCE),'original_report_sha256':sha(SOURCE/'REPORT.md'),'original_claim_sha256':sha(SOURCE/'CLAIMS.json'),'original_statement_sha256':original['statement_sha256'],'canonical_statement_sha256':accepted['statement_sha256'],'prior_review':str(prior),'independent_review_run':ROOT.name,'independent_report':'REPORT.md','independent_code':'code/audit.py'}
new={
    'claim_id':'A092-UNIFORM-SIGNED-TRANSCRIPT-BANK-CONVERSION','version':1,
    'exact_statement':'For every Boolean sign f on a finite uniform cube and every finite deterministic physical singleton stopping tree without repeated coordinates along a path, use the function-specific coherent coupling of root Fourier set S0 and physical transcript Pi, extending to a computing tree only to attach the actual output Y=f(X). Put R=I(f)-E I(f_leaf), J_T=sum_v w_v J_v, and C_T=H(Pi|Y)-H(Pi|S0). Then C_T=J_T-I(Pi;Y) and -I(Pi;Y)<=C_T<=(2/ln2)*R-I(Pi;Y). Consequently [C_T]_+/2<=R/ln2. This bounds the signed output-to-root-spectral conditional-bank conversion; it does not supply H(Pi|S0), reference-reset credit, arbitrary witness conditioning or terminal Fourier entropy payment.',
    'hypotheses':['finite actual Boolean sign; uniform physical inputs','finite deterministic adaptive singleton physical stopping tree; inherited fair branches; no repeated query on a path','function-specific coherent root-spectral/transcript coupling with branch kernel childhat_b(T)^2/(2q_T) on positive fibers','actual output attached by any finite computing completion; stopped transcript remains the prescribed prefix','Shannon entropy in bits; physical influence equals spectral influence only in this uniform scope','same consumed influence R cannot be spent again in descendant or reference accounts'],
    'statement_sha256':'','contributors':['account05/A092'],
    'proof_source':{'run_id':ROOT.name,'path':'REPORT.md','locator':'complete derivation: new quantitative conversion proof','code':'code/audit.py','output':'out/RESULT.json; out/SHARED_CONTROL.json'},
    'proof_dependencies':[],'review_records':[],
    'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
    'refutes':[],
    'first_unproved_line':'A prescribed normalized compatible reference funds the root-spectral or witness-conditioned bank and all signed reset/erasure/terminal residuals from the remaining exclusive influence budget.',
    'next_consumers':['A050','A057','A064','A037','A039','A091','A095','A087','A085','B19','B20']}
new['statement_sha256']=chash(new)
save('CLAIMS.json',[accepted,new])
progress={
    'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A092','gap_id':'G-R-MISMATCH','attempt_id':'A092-stage3-output-bank-review-conversion',
    'method':'Independent source repair audit, original Boolean underrefund certificate, exact physical/spectral transcript joint and signed bank conversion',
    'mathematical_delta':'A050@1 accepted unchanged; original lambda=49/100 underrefund witness independently certified; new uniform conversion C_T=J_T-I(Pi;Y)<=2R/ln2-I(Pi;Y) proved pending review. Full FEI OPEN.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A050_INDEPENDENT_REVIEW_ACCEPTED; A092_CONVERSION_PENDING_REVIEW; FULL_FEI_OPEN',
    'claim_versions_used':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (review target)','A037-PHYSICAL-SPECTRAL-COMMON-LIFT@1 (credited interface reconstructed directly)','C005 uniform JS mechanism (reconstructed directly)','A048-SHARP-TAX-PAYMENT-SCOPE@1 (source context, not assumed)'],
    'claims_created_or_changed':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 independent A092 review','A092-UNIFORM-SIGNED-TRANSCRIPT-BANK-CONVERSION@1'],
    'source_artifacts':['REPORT.md','CLAIMS.json','SEARCH_SPEC.json','code/audit.py','code/finalize.py','out/RESULT.json','out/UNDERREFUND.json','out/CONTROLS.json','out/SHARED_CONTROL.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':['A050','A057','A064','A037','A039','A091','A095','A087','A085','B19','B20'],
    'next_action':'Compute root-spectral-to-prescribed-witness conditional bank and signed reference reset on the priority shared-control tree, retaining the bounded conversion cost and every terminal core bill.',
    'stagnant_substantive_attempts':0,'blockers':['Complete compatible-reference funding and universal terminal-inclusive payment remain mathematically open; remote persistence unverified.'],
    'packet_ids':['A092']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B19'/'STREAM_NOTES.md',prior]
sources += [SOURCE/n for n in ['REPORT.md','PROOF.md','CLAIMS.json','FROZEN_SPEC.json','out/CHECK.json']]
for a,run in [('A048','20261012T013822Z-account05-A048-tensor-stress'),('A037','20261011T220010Z-account05-A037-conditional-credit-ledger')]:sources.append(TEAM/'agents'/a/'runs'/run/'CLAIMS.json')
sources.append(Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_REDUCTION.md'))
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
result=json.loads((ROOT/'out'/'RESULT.json').read_text())
assert result['status']=='PASS' and result['roots']==556 and result['trees']==2236
assert result['runtime_seconds']<120
under=json.loads((ROOT/'out'/'UNDERREFUND.json').read_text());assert under['net_gt_I']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A092 stage 3 complete: A050 half-output refund independently accepted; original underrefund certified; uniform signed bank conversion proved; 51,907 exact assertions PASS; full FEI OPEN.\nNEXT: Price root-spectral-to-prescribed-witness bank/reset on the shared-control tree with terminal CE and one influence account; A087/A085 review the conversion.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {ROOT.name}: Read current board, B19 notes and protocol. Consumed newer A050 repair instead of old scalar endpoints; independently accepted original theorem without repair. Rebuilt original rare four-variable lambda=0.49 certificate from truth table, exact spectrum and reciprocal-stabilized rational logs. Checked 556 roots/2236 trees, {result["assertions"]} exact assertions in {result["runtime_seconds"]:.6f}s. Derived uniform signed bank conversion C_T=J_T-I(Pi;Y)<=2R/ln2-I(Pi;Y), pending independent review. Compatible witness bank/reset and terminal Fourier entropy remain unpaid. Saved all required artifacts; no remote copy claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 independently accepted: half-output-conditional bank pays positive scalar tax by I(Pi;Y)/2<=I_phys/2; lambda<1/2 fails on essential biased point-defect computing trees. Original q=1-((2^128-1)/2^128)^2, r=4, lambda=.49 underrefund independently certified; use reciprocal log reduction for near-one complements. A092 new uniform coupling bound: C_T=H(Pi|Y)-H(Pi|S0)=J_T-I(Pi;Y), between -I(Pi;Y) and 2I_removed/ln2-I(Pi;Y). Positive half conversion costs at most I_removed/ln2 once. This does not fund H(Pi|S0) or arbitrary reference side conditioning; exact substitution recovers the original erasure+JS+terminal ledger. Terminal output and Fourier entropy remain distinct.\n')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
for c in [accepted,new]:
    assert set(c)==set(protocol['required_per_run']['claim_fields']) and c['statement_sha256']==chash(c)
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
for p in ROOT.rglob('*'):
    if p.is_file():assert p.stat().st_size<20_000_000
save('out/VALIDATION.json',{'status':'PASS','at_utc':now,'protocol_field_sets_exact':True,'claim_hashes_canonical':True,'progress_copies_identical':True,'required_report_fields':True,'all_files_under_20MB':True,'rolling_status_two_lines':True,'result':result,'original_underrefund_certified':True,'A050_review':'ACCEPT_AT_STATED_SCOPE','new_conversion_review':'PENDING','mirror_status':'UNVERIFIED'})
save('out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'])
print(json.dumps({'status':'PASS','claims':2,'trees':result['trees'],'assertions':result['assertions'],'run':str(ROOT)}))
