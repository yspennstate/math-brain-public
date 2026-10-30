from pathlib import Path
import json,hashlib,datetime,sys
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; rid=R.name
BASE=Path(r'~\brain_workers\FEI100_20261011')
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
ready=(R/'out/PREFIX_VALIDATION.json').exists()
prepare='--prepare' in sys.argv
if not prepare: assert ready,'Prefix certificate missing; do not claim final completion.'
oldR=A/'runs/20261011T224431Z-fleet05-A064-global-debt-potential'
old=json.loads((oldR/'CLAIMS.json').read_text(encoding='utf-8'))[0]
statement=old['exact_statement']+'\n\n'+('Additional version-2 theorem: For any finite uniform exclusive controller selecting independent disjoint Boolean cores u_j or constants, with duplicate descriptions of the same physical core merged, keep control probabilities q_j fixed during a finite adaptive data-only prefix. Suppose each core follows a prescribed finite continuation tree with a nonnegative C-priced potential r_j depending only on its own history and an initially fixed independent seed. Then R_t=sum_j q_j*r_j(t)+sum_j q_j*log2(1/q_j)*Var(u_j,t) is a nonnegative potential at price alpha=C+11/2: D_F<=alpha*d_F+R_t-E[R_next|history]. Its initial value is at most sum_j q_j*r_j(root)+2I_ctrl(F); at any partial stop sigma, E R_sigma<=R_root+C*Pi_I,data. If cores are exhausted to constants with zero core leaf reserves, R_sigma=0, while the actual remaining controller entropy is retained. Thus the least nonnegative alpha-priced prefix reserve is dominated by R_root. For a declared controller continuation on each actual complete-data frontier, let b_sigma dominate its reserve at the same alpha; adding E[b_sigma|history] grafts a valid full-rule potential with root bound sum_j q_j*r_j(root)+2I_ctrl(F)+E b_sigma. No linear bound on the last debit or arbitrary inherited core reserve is assumed. The positive outer bank uses kappa=(3+2/e)/ln2<11/2; the coherent scalar paird refund is nonnegative and is removed only as an upper bound, never from the exact identity. For arbitrary h and two independent dictator data cores, data-first retained entropy, influence and consistently sign-translated declared controller reserve equal H(h)/2, I(h)/2, Q_alpha(h,T)/2. The new lift does not imply universal FEI.')
hyp=old['hypotheses']+['The additional theorem uses independent disjoint data cores selected by an exclusive arbitrary physical controller; shared data among distinct cores are excluded.',
'The additional prefix exposes data only, with fixed q_j; interleaving respects declared per-core continuation trees, whose reserves depend on own history and an initially fixed independent seed.',
'C>=0; all sums finite; q_j=0 terms zero; actual stopping leaves and controller continuation are retained; no initial arbitrary-core or boundary resource bound is assumed.']
def claimhash(st,hy): return hashlib.sha256(json.dumps({'statement':st,'hypotheses':hy},sort_keys=True,separators=(',',':')).encode()).hexdigest()
new={'claim_id':old['claim_id'],'version':2,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':claimhash(statement,hyp),'contributors':['A064; positive cap source credited to A057 and signed ledger to A087; prior activation direction credited to A023'],
'proof_source':{'run_id':rid,'paths':['GLOBAL_DEBT_POTENTIAL.tex','DERIVATION.md','REPORT.md'],'prior_version_source':str(oldR/'GLOBAL_DEBT_POTENTIAL.tex'),'validation':['out/ROOT_VALIDATION.json','out/PREFIX_VALIDATION.json','out/REVIEW_WITNESSES.json']},
'proof_dependencies':[{'claim_id':old['claim_id'],'version':1,'scope':'Prior assertions retained at exact source; author-proved pending independent review'},
{'claim_id':'A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER','version':1,'scope':'Independently reconstructed in REVIEW_A087.md; exact full query decomposition and actual terminal frontier'},
{'source':'A057 PROOF.md sections1,3,4','run_id':'20261013T221645Z-fleet05-A057-coherent-restriction-remainder','scope':'Only local cap and gap with original-edge controller ownership, analytically reconstructed; unrelated suffix clause not imported'}],
'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[old['claim_id']+' v1 (same source retained)'],'refutes':old['refutes']+['Paid positive outer-prefix bank and zero dictator-core reserve justify discarding the actual arbitrary controller frontier'],
'first_unproved_line':None,'next_consumers':['A065','A030','A057','A087','A091','A094','A023','A029','A097','A099','B20']}
sourceR=BASE/'agents/A087/runs/20261013T222530Z-fleet05-A087-restriction-referee'
sourceclaims=json.loads((sourceR/'CLAIMS.json').read_text(encoding='utf-8'))
review=json.loads(json.dumps(next(x for x in sourceclaims if x['claim_id']=='A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER')))
originalsha=review['statement_sha256'];review['statement_sha256']=claimhash(review['exact_statement'],review['hypotheses'])
review['review_records'].append({'reviewer':'A064','verdict':'HOLDS_AT_EXACT_STATED_SCOPE','source_run':rid,'source':'REVIEW_A087.md','method':'Independent raw Boolean full/child Walsh sector identities; independent direct-character-sum reproduction of both exact original mass/frontier fixtures; all-dimensional finite stopped algebra; no substantive repair',
'original_recorded_statement_sha256':originalsha,'source_claim_file_sha256':hashlib.sha256((sourceR/'CLAIMS.json').read_bytes()).hexdigest(),'scope_exclusions':['No full FEI or arbitrary terminal payment','No acceptance of a different stopping frontier or omitted projected-sector mass']})
review['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_BY_A064'
(R/'CLAIMS.json').write_text(json.dumps([new,review],indent=2)+'\n',encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':rid,'stream':'B13','packet_id':'A064','gap_id':'G-R-MISMATCH','attempt_id':'A064-exclusive-priced-prefix-lift-v2',
'method':'Source-bound signed-ledger review; nonnegative refund; exclusive variance-rarity reserve; Snell domination and harmonic actual-boundary graft',
'mathematical_delta':'Price lift <=11/2; extra initial bank<=2I_ctrl; bounded expected partial terminal reserve; explicit arbitrary controller frontier retained; inherited core and boundary universal payment still open',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT' if ready else 'MATHEMATICAL_ARTIFACT_SAVED_FINAL_PREFIX_CERTIFICATE_PENDING',
'mathematical_status':'PREFIX_TRANSPORT_THEOREM_PROVED_LOCALLY; A087_SIGNED_LEDGER_HOLDS_AT_SCOPE; FULL_FEI_OPEN',
'claim_versions_used':['A064-TERMINAL-CORRECTED-GLOBAL-DEBT v1 (prior retained scope)','A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER v1 (independent A064 HOLDS)','A057 exclusive cap local sections1,3,4 (reconstructed)'],
'claims_created_or_changed':[new['claim_id']+' v2',review['claim_id']+' v1 independent review'],
'source_artifacts':['REPORT.md','DERIVATION.md','GLOBAL_DEBT_POTENTIAL.tex','REVIEW_A087.md','out/ROOT_VALIDATION.json','out/PREFIX_VALIDATION.json','out/REVIEW_WITNESSES.json'],
'next_consumers':new['next_consumers'],'next_action':'Price the first actual control reveal changing exclusive q_j during unfinished core exposure, using one owned controller influence account and the actual continuation',
'stagnant_substantive_attempts':0,'blockers':['Universal inherited core and actual controller boundary reserve bounds remain unproved','Control/data interleaving not covered by fixed-q lift','New potential independent review and mirrors pending'],'packet_ids':['A064']}
for n in ('PROGRESS.json','PACKET_DELTA.json'): (R/n).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))['required_per_run']
for c in (new,review): assert set(c)==set(protocol['claim_fields']) and c['statement_sha256']==claimhash(c['exact_statement'],c['hypotheses'])
assert set(progress)=={x.split(' (',1)[0] for x in protocol['progress_fields']}
report=(R/'REPORT.md').read_text(encoding='utf-8'); assert all('# '+x in report for x in protocol['report_fields'])
if ready:
    root=json.loads((R/'out/ROOT_VALIDATION.json').read_text()); pref=json.loads((R/'out/PREFIX_VALIDATION.json').read_text()); wit=json.loads((R/'out/REVIEW_WITNESSES.json').read_text())
    assert root['status']=='PASS_ROOT_DOMAIN' and (root['roots_finished'],root['faces_finished'],root['exact_assertions'])==(1296,5184,27224)
    assert pref['status']=='PASS' and pref['prefix_trees']==7776 and pref['root_cases']==0 and pref['root_data_faces']==0
    assert wit['status']=='PASS' and wit['exact_assertions']==11
    assert pref['helper_sha256']==hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest()
    raw_helper_hash=hashlib.sha256((R/root['helper']).read_bytes()).hexdigest()
    if root['helper_sha256']!=raw_helper_hash:
        normalized_hash=hashlib.sha256((R/root['helper']).read_text(encoding='utf-8').encode()).hexdigest()
        assert root['helper_sha256']==normalized_hash,'Unexpected source mismatch, not newline normalization'
        root['original_normalized_text_sha256']=root['helper_sha256']
        root['helper_sha256']=raw_helper_hash
        root['hash_correction']='Initial prepare_prefix receipt hashed normalized Python text; corrected to actual saved Windows file bytes. Both hashes retained; mathematical source unchanged.'
        (R/'out/ROOT_VALIDATION.json').write_text(json.dumps(root,indent=2)+'\n',encoding='utf-8')
    total=root['exact_assertions']+pref['exact_assertions']+wit['exact_assertions']
    merged={'status':'PASS','root_cases':1296,'root_data_faces':5184,'prefix_trees':7776,'distinct_prefix_states':pref['distinct_prefix_states'],
    'exact_assertion_executions':total,'root_assertions':27224,'prefix_assertions':pref['exact_assertions'],'independent_source_witness_assertions':11,
    'pilot_assertions_excluded':True,'incomplete_large_attempt_counts_excluded':True,'root_phase_runtime_seconds':root['elapsed_seconds'],'prefix_runtime_seconds':pref['runtime_seconds'],
    'source_witness_runtime_seconds':wit['runtime_seconds'],'phase_certificates':['ROOT_VALIDATION.json','PREFIX_VALIDATION.json','REVIEW_WITNESSES.json'],
    'helper_hashes':{'roots':root['helper_sha256'],'prefix':pref['helper_sha256']}}
    (R/'out/VALIDATION.json').write_text(json.dumps(merged,indent=2)+'\n',encoding='utf-8')
    rs=f"PASS:1296 roots/5184 faces with27224 exact root assertions;7776 prefix trees over{pref['distinct_prefix_states']} distinct recursive states with{pref['exact_assertions']} prefix assertions; root phase{root['elapsed_seconds']:.4f}seconds and prefix phase{pref['runtime_seconds']:.4f}seconds. Combined with the11 original-source witness assertions, total{total} exact assertion executions; pilot and incomplete large attempts excluded"
    ws=f"PASS:11 exact assertions in{wit['runtime_seconds']:.6f}seconds"
    report=report.replace('@VALIDATION_SUMMARY@',rs).replace('@REVIEW_SUMMARY@',ws)
    report=report.replace('maximum runtime240 seconds; no expected job exceeded300 MB','maximum runtime240 seconds for the combined job, then600 seconds for only its unfinished prefix phase; no expected job exceeded300 MB')
    report=report.replace('The final domain was then frozen separately','The final root domain was then frozen separately')
    report=report.replace('checkpoints were flushed after each controller.','checkpoints were flushed after each controller. The combined v4 job completed the entire root domain, then timed out during the prefix phase; ROOT_VALIDATION.json preserves that complete root receipt. The unfinished prefix alone was frozen in FROZEN_PREFIX_PHASE.json and completed via the same checker with --prefix-only. No completed root checks were rerun. The root helper receipt initially hashed newline-normalized Python text; final byte-hash verification corrected it to the saved Windows bytes and retained both hashes without changing the mathematical source.')
    (R/'REPORT.md').write_text(report,encoding='utf-8');assert '@VALIDATION_' not in report and '@REVIEW_' not in report
    (A/'STATUS.md').write_text(f"STATE: Stage complete locally: exclusive-controller priced prefix lift<=11/2, initial extra<=2I_ctrl, actual boundary retained; A087 signed ledger independently HOLDS;{total} exact assertions; new theorem review pending; FEI OPEN.\nNEXT: Price the first controller reveal changing q_j during unfinished core exposure, preserving inherited core reserves, one owned control budget and the actual continuation; A087/A094 review.\n",encoding='utf-8')
    log=(A/'WORKLOG.md').read_text(encoding='utf-8')
    entry=f"2026-10-14 final: Saved complete root certificate plus separately finished7776-tree prefix phase;{total} final exact assertion executions, excluding pilot and incomplete larger attempts. New lift and original A087 ledger/witness review are saved with all initial/expected-terminal assumptions and actual control frontier. Protocol schema/hash checks passed; mirrors and new theorem independent review remain pending.\n"
    if entry not in log: (A/'WORKLOG.md').write_text(log+entry,encoding='utf-8')
sources=[(BASE/'BOARD.md','Current stage dispatch; read initial full board and relevant B13/B05/B18 scope'),(BASE/'claude/B13/STREAM_NOTES.md','Leadv2 fully read'),(PROTO,'Protocol fully read'),
(sourceR/'PROOF.md','Full signed ledger, controller cap and projected mass/frontier proof read'),(sourceR/'CLAIMS.json','Exact review target and acceptance scope'),
(BASE/'agents/A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder/PROOF.md','Sections1,3,4 proof and stale trailing scope inspected'),
(BASE/'agents/A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder/CLAIMS.json','Registered statements read; suffix excluded from new review'),
(BASE/'agents/A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget/REPORT.md','Full separator ownership and next target read'),
(BASE/'agents/A023/runs/20261012T010933Z-fleet05-A023-amortized-rarity-budget/REPORT.md','Two-event overlap paid; nonduplication'),
(BASE/'agents/A030/runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests/RESERVE_TRANSPORT.md','Full Snell/plateau distinction read; new plateau theorem not imported'),
(BASE/'agents/A030/runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests/REPORT.md','Scope and Qsource definition'),
(BASE/'agents/A062/runs/20261013T221705Z-fleet05-A062-influence-compensator/REPORT.md','Contextual arbitrary retained-child reserve gap'),
(BASE/'agents/A092/runs/20261013T222550Z-fleet05-A092-counterexample-referee/REPORT.md','Searched and inspected signed conversion scope passages; not a proof premise'),
(oldR/'CLAIMS.json','Prior A064 exactv1 retained source')]
receipt=[]
for p,scope in sources:
    raw=p.read_bytes();receipt.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':scope})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
schema={'status':'PASS','ready':ready,'claim_field_sets':'exact protocol','progress_field_set':'protocol with explanatory packet_ids suffix normalized','report_fields':'all seven present',
'packet_delta_matches':(R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes(),'statement_hashes':'canonical UTF8 JSON statement/hypotheses','mirror_verified':False}
assert schema['packet_delta_matches'];assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
(R/'out/SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2)+'\n',encoding='utf-8')
if ready: assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=list(R.rglob('*'))+[A/x for x in ('STATUS.md','WORKLOG.md','LEARNED.md')];receipts=[]
for p in files:
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json': continue
    b=p.read_bytes();assert len(b)<20*1024*1024
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'FINAL' if ready else 'IN_PROGRESS','receipts':receipts,'external_mirrors_verified':False},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'schema':'PASS','ready':ready,'new_claim_version':2,'source_review':'A087 signed ledgerv1 HOLDS','artifacts_hashed':len(receipts),'full_fei':'OPEN',**({'exact_assertion_executions':total} if ready else {})},indent=2))
