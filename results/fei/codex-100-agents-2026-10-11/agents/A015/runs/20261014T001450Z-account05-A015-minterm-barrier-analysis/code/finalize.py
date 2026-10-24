from pathlib import Path
import json, hashlib, datetime

BASE=Path(__file__).resolve().parents[1]
AGENT=BASE.parents[1]
ROOT=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
A6=ROOT/'agents/A006/runs/20261013T214427Z-account05-A006-posterior-forest-optimization'
A7=ROOT/'agents/A007/runs/20261013T220854Z-account05-A007-root-normalization'
A1=ROOT/'agents/A001/runs/20261013T213937Z-account05-A001-quantifier-audit'
FOREST=Path(r'~\mop_fei100\reports\fei-2026-10-11\source_material\reductions\paper\forests.tex')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (BASE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
upstream=json.loads((A6/'CLAIMS.json').read_text(encoding='utf-8'))
original=next(c for c in upstream if c['claim_id']=='A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS')
claim=json.loads(json.dumps(original))
claim['review_records'].append({'reviewer':'A015','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','proof_source':str(BASE/'REVIEW_A006.md'),'validation':str(BASE/'out/EXACT_CHECK.json'),'method':'Independent Leibniz polynomial expansion versus direct chronological BFS events on signed Boolean prime tables; full analytic chain reconstructed','reviewer_supplied_substantive_repair':False,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
claim['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':BASE.name,'stream':'B03','packet_id':'A015','gap_id':'G-J-COST','attempt_id':'A015-stage3-actual-singleton-location',
 'method':'Unchanged-scope independent dependency review; direct physical-singleton queue and surrogate mass diagnostics with exact Boolean certificates',
 'mathematical_delta':'A006 determinant-moment v1 independently HOLDS. Rare-switch prime posterior erases h2(1/4)+(3/4)log2 r labels while retaining physical y: S_y=1/4, Q_selected(y)>11/120 for all r>=1. Higher-degree whole-set and Psi payment OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS',
 'mathematical_status':'DEPENDENCY_INDEPENDENTLY_ACCEPTED_SCOPED_DIAGNOSTIC_CHECKED_FULL_FEI_OPEN',
 'claim_versions_used':['A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS@1'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'Added local independent unchanged-scope acceptance; no new broad candidate'}],
 'source_artifacts':[str(BASE/'REVIEW_A006.md'),str(BASE/'SINGLETON_INTERFACE.md'),str(BASE/'out/EXACT_CHECK.json')],
 'next_consumers':['A006','A007','A086','A094','B03','B20'],
 'next_action':'Insert physical singleton allocation into the SAME A007 whole-set posterior on a nonconstant terminal-core activation; expose signed Psi with terminal CE and one influence budget retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal whole-set spectral cost and signed Psi remain unproved','Application independent review and supervisor adoption unobserved'],
 'packet_ids':['A015']}
save('PROGRESS.json',progress); (BASE/'PACKET_DELTA.json').write_bytes((BASE/'PROGRESS.json').read_bytes())
sources=[(ROOT/'BOARD.md','Stage-start supervisor snapshot, 2026-10-14 00:19 UTC'),(ROOT/'claude/B03/STREAM_NOTES.md','v2 complete'),(AGENT/'STATUS.md','Inherited stage-2 status; archived read hash before update'),(AGENT/'LEARNED.md','Inherited durable facts before update'),(PROTOCOL,'Entire revision v2'),(A6/'REPORT.md','Complete'),(A6/'CLAIMS.json','Original statement/version/hash'),(A6/'FOREST_MOMENTS.md','Entire mathematical proof'),(A7/'REPORT.md','Complete report; LIFT.md not independently reviewed'),(A1/'REPORT.md','First 12500 characters including derivation and validation commands'),(FOREST,'Entire source queue and posterior theorem'),(PROTOCOL.parent/'CLAIM_REGISTRY.json','Metadata, gap map and A015/B03 query')]
save('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in sources])
checks=json.loads((BASE/'out/EXACT_CHECK.json').read_text(encoding='utf-8')); pilot=json.loads((BASE/'out/PILOT.json').read_text(encoding='utf-8'))
assert checks['status']==pilot['status']=='PASS'
assert checks['assertions']==7471 and pilot['assertions']==578
assert sum(row['ownership_cases'] for row in checks['rare_switch'])==1994
assert claim['exact_statement']==original['exact_statement'] and claim['statement_sha256']==original['statement_sha256']
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==pf
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+f in report for f in protocol['required_per_run']['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
(AGENT/'STATUS.md').write_text('STATE: A015 stage 3 complete: A006 determinant v1 independently HOLDS; actual prime-singleton posterior erases growing labels while retaining physical location; 8,049 exact checks PASS; FEI OPEN.\nNEXT: A006/A007/A086 review; couple physical singleton allocation to the SAME whole-set posterior on a nonconstant terminal core, retaining signed Psi and complete core CE.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 stage 3 ('+BASE.name+'): consumed current board/A006/A007 rather than rerunning class bounds. Independently reconstructed whole A006 v1 without repair. Signed rare-switch exact prime tables, 1994 assignments and five forced prime stars checked by independent chronological BFS versus Leibniz determinants; pilot578+full7471 assertions PASS, runtime7.662s/.671s. Derived general singleton surrogate and actual-event formula, and rare-switch posterior refund h2(1/4)+.75log2 r with S_y=1/4, Q_selected(y)>11/120 all r. Saved proof/receipts. Whole-set Psi/universal influence payment remains open; no new broad candidate.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nA006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS@1 independently reconstructed by A015, unchanged scope/no repair: determinant parent/attachment mass must be factorial-moment weighted for chronological children; it remains surrogate B mass. Exact signed-table BFS checks complement prior monotone reviews.\nFor original gamma=6/5, M_l=1 singleton mass S_j=sum_l lambda_l*pi_l*rank_l(j)^(-gamma), signed residual log(D/S_j), D=product(1+lambda*pi)-1. Actual one-root/size-one/zero-child contribution=(1/(4D))sum_l lambda_l*pi_l*theta_1(j)/Z_1(l). These are distinct quantities. q_j=S_j/(6sum lambda*pi) is subprobability; singleton spectral cost=W1[log(D/(6t))+H(rho)+KL(rho||q)], retaining all signs and missing mass.\nRare switch exact signed primes yz, y(-c_i), z(all c): feasible lambda 1/4,3/(4r),1/4 and y first give S_y=1/4, D<=5/11, selected actual singleton output mass>11/120. Posterior entropy h2(1/4)+(3/4)log2 r cancels exactly the expected labels, while physical y stays identifiable. A growing raw prime-label bill can therefore be refunded on a dominant output. This is no whole-set/FEI proof; arbitrary terminal core CE and A007 signed Psi must remain. A001 influence-vector-only reference no-go rules out promoting sorted influences into universal structural sufficiency.\n')
paths=[p for p in BASE.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[AGENT/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in paths)
save('out/RECEIPTS.json',{'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths],'protocol_fields':'PASS','same_progress_packet_delta':(BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes(),'reviewed_statement_preserved':True,'independent_application_review':'PENDING','remote_mirror':'UNVERIFIED'})
receipts=json.loads((BASE/'out/RECEIPTS.json').read_text(encoding='utf-8'))
assert all(sha(Path(r['path']))==r['sha256'] for r in receipts['files'])
print(json.dumps({'persistence':'PASS','files':len(paths),'assertions':checks['assertions']+pilot['assertions'],'run':str(BASE)}))
