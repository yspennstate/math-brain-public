from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]; HOME_A022=RUN.parents[1]
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
statement=('For every Boolean seed h on m>=1 uniform bits, every tensor power t>=1, and every flipped tensor vertex, '
'write W_T=2^m hhat(T), M=#{T:W_T!=0}, rho=M/2^m, lambda=M^-1 sum_(W_T!=0) log2|W_T|, delta_t=2^-mt. '
'For the actual fair selector between h^tensor(t) and its one-point flip, its conditional selector entropy L_t satisfies '
'|L_t/delta_t-2(1-rho^t)-rho^t(2t lambda+log2 e)|<=12(rho/2)^t. '
'Hence L_t/delta_t tends to 2 when rho<1 and grows as 2t lambda+log2 e+O(2^-t) when rho=1. '
'For arbitrary finite actual flip sets D, coefficient half-difference t_S=2^-n sum_(v in D) f(v)chi_S(v), '
'q_S=(fhat(S)-t_S)^2+t_S^2, e_S=t_S^2, mu=|D|2^-n; '
'L=mu[log2(1/mu)-D2(e/mu||q)]+R, 0<=R<=mu/ln2. '
'For one point e is the minority fiber mass in every packet. Adjacent flips have e_S=2 delta^2[1+epsilon(-1)^(j in S)], '
'so mismatch occupies exactly one Fourier half-cube; the common flipped edge contributes zero to influence change.')
claim={
'claim_id':'A022-SIGNED-SURGERY-TENSOR-LOG-LEDGER','version':1,'exact_statement':statement,
'hypotheses':['Actual Boolean signs, uniform cube','m>=1, integer t>=1; fixed tensor seed for limiting dichotomy','Entropy and KL in bits','Zero packets omitted; mu=0 interpreted as zero','Selector-local cost, not total FEI ratio'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A022'],
'proof_source':{'run_id':RUN.name,'path':'POINT_SURGERY.tex','certificate':'SURGERY_LOG_CERTIFICATE.md','verifier':'code/check_surgery.py','output':'out/EXACT_CHECK.json'},
'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Universal selector-local fixed price L<=K*mu on full-support tensor-seed point surgeries; existing bent control is not claimed new'],
'first_unproved_line':None,'next_consumers':['A020','A021','A023','A028','A053','A064','A077','A087','A094']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(RUN/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={
'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B05','packet_id':'A022',
'gap_id':'G-R-MISMATCH','attempt_id':'A022-surgery-1','method':'Signed exact Walsh surgery; integer parity and tensor occupancy; uniform scalar log bound; rational finite verification',
'mathematical_delta':'Exact arbitrary-seed point/adjacent spectral and edge-interaction formulas; every point mismatch equals minority; tensor support/log-cost dichotomy with explicit 12(rho/2)^t remainder',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'PACKET_SCOPE_PROVED_PENDING_REVIEW_FULL_FEI_OPEN',
'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
'source_artifacts':['REPORT.md','POINT_SURGERY.tex','SURGERY_LOG_CERTIFICATE.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/EXACT_CHECK.json'],
'next_consumers':claim['next_consumers'],
'next_action':'A023 inserts exact support-dependent bills into a declared physical restriction-tree comparison, with terminal entropy and single-use influence; A087/A094 independently reconstruct this proof',
'stagnant_substantive_attempts':0,'blockers':['B05 STREAM_NOTES.md missing at supplied path; independent review and supervisor adoption pending'], 'packet_ids':['A022']}
expected_progress={name.split(' (')[0] for name in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
for name in ['PROGRESS.json','PACKET_DELTA.json']:(RUN/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
check=json.loads((RUN/'out/EXACT_CHECK.json').read_text())
(HOME_A022/'STATUS.md').write_text('STATE: A022 local packet complete: exact signed surgery and uniform tensor logarithm classification; 563,961 exact assertions passed; review pending; full FEI OPEN.\nNEXT: A087/A094 reconstruct; A023 use support-dependent bills in a physical stopping-tree ledger with terminal cost and no reused influence.\n',encoding='utf-8')
with (HOME_A022/'WORKLOG.md').open('a',encoding='utf-8') as fp:fp.write(f'2026-10-12: Finished one-point/adjacent formulas, exact influence interaction and tensor support dichotomy. Frozen verifier passed {check["assertions_passed"]:,} assertions in {check["elapsed_seconds"]:.6f}s. Persisted rational log endpoints and protocol metadata; independent review pending. Source loader cp1252 fallback repaired for a paper text. No global tree payment established.\n')
with (HOME_A022/'LEARNED.md').open('a',encoding='utf-8') as fp:fp.write('For one-point flips on n>=1 uniform bits, normalized signed Fourier ratios are even integers; hence mismatch e is always the minority fiber mass. For adjacent flips ratios can be odd and the physical/minority normalizations can differ. For fixed tensor seed support fraction rho and uniform-support log Walsh mean lambda, |L_t/delta_t-2(1-rho^t)-rho^t(2t lambda+log2 e)|<=12(rho/2)^t. Thus fixed positive zero fraction kills tensor-local logarithm growth, while full support preserves it. This is a selector-local classification, not FEI or an optimized-tree result.\n')
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=HOME_A022/name;b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(RUN/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_field_checks':'claim fields exact; progress fields exact after interpreting protocol annotation packet_ids (one primary ID, for compatibility) as packet_ids, per explicit compatibility instruction','file_limit_bytes':20_000_000,'independent_review':False,'mirror_verified':False,'files':receipts},indent=2),encoding='utf-8')
print(json.dumps({'saved_files':len(receipts),'claim_field_check':True,'progress_field_check':True,'max_file_bytes':max(x['bytes'] for x in receipts),'assertions':check['assertions_passed'],'final_checker_seconds':check['elapsed_seconds']},indent=2))
