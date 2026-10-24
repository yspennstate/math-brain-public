from pathlib import Path
import json,hashlib,datetime

run=Path(__file__).resolve().parents[1]; root=run.parent.parent
base=Path(r'~\brain_workers\FEI100_20261011')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
results=json.loads((run/'out/POINT_CHECK.json').read_text())
assert results['status']=='PASS' and results['actual_functions']==126 and results['coordinate_splits']==642
oldrun=root/'runs/20261011T214516Z-account05-A061-entropy-process'
reviewrun=base/'agents/A087/runs/20261011T221055Z-account05-A087-restriction-referee'
oldclaims=json.loads((oldrun/'CLAIMS.json').read_text())
reviewclaims=json.loads((reviewrun/'CLAIMS.json').read_text())
reviewmap={c['claim_id']:c for c in reviewclaims}
review_receipts=[]
for c in oldclaims:
    r=reviewmap[c['claim_id']]
    assert c['exact_statement']==r['exact_statement'] and c['hypotheses']==r['hypotheses']
    assert r['status']=='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A087'
    review_receipts.append({'claim_id':c['claim_id'],'version':1,'original_statement_sha256':c['statement_sha256'],'exact_statement_and_hypotheses_match':True,'acceptance_source':str(reviewrun/'CLAIMS.json'),'review_records':r['review_records'],'old_source_not_modified':True})
save('out/REVIEW_RECEIPTS.json',review_receipts)

statement='For every n>=1 and x0 in the uniform sign cube, f=1-2 indicator{x=x0} has d_i=2^(1-n)=d for every coordinate, H_n=-2(1-d)^2 log2(1-d)-2d(2-d)log2(d), and D_i/d=(H_n-H_(n-1)/2)/d. These rates are 0 at n=1, 4 at n=2, strictly decrease for n>=3 and tend to 4, with sharp supremum R_3=12-(9/2)log2(3). The log-charge rate is L_n=lambda_i/d=1-d+d log2((1-2d+2d^2)/d^2); its sharp supremum is L_3=L_4=(3+log2(10))/4, it strictly decreases for n>=4 and tends to 1. KL_2(nu_i||q_i)=n-1-L_n. Every nonconstant physical descendant is a point function; therefore R_3 I(g_t)-H(g_t) is a supermartingale for every fair adaptive fresh-coordinate policy on this family, and the minimal nonnegative reserve Q* with zero constant-leaf boundary is identically zero at every C>=R_3. The drift price R_3 is sharp for this class.'
hyp=['uniform finite cube and Boolean sign output','n>=1; pure one-point defect, translated vertices allowed','entropy and KL in bits; normalized Fourier coefficients','H_0=0; 0 log 0 interpreted continuously','nu_i=b_T^2/d_i, q_i=a_T^2+b_T^2 and lambda_i=sum b_T^2 log2(q_i/b_T^2)','fair adaptive policy queries fresh coordinates using only physical history and independent policy seed','Q*_v=max(0,D_v-Cd_v+average Q*_children), zero at constant leaves']
claim={'claim_id':'A061-POINT-COORDINATE-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A061'],'proof_source':{'run_id':run.name,'path':'POINT_CERTIFICATE.md','validation':'out/POINT_CHECK.json'},'proof_dependencies':[{'claim_id':'A061-FAIR-TREE-PROCESS','version':1,'review':'A087 independently accepted; used only for process consequence'}],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A062','A064','A065','A087','A094','B13','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B13','packet_id':'A061','gap_id':'G-R-SELECT','attempt_id':'A061-point-coordinate-1','method':'Consume independent A087 baseline review; source-bound B13 sandwich/KL handoff; closed-form point spectra, analytic series monotonicity, exact polynomial log-rate sign, Fraction/prime-log and rational interval verification','mathematical_delta':'Point-function all-dimensional sharp drift price R3=12-(9/2)log2(3) and sharp log-charge price L3=L4=(3+log2(10))/4 proved; exact KL=n-1-L_n; all-rule Q*=0 at C>=R3. First-stage baseline independently accepted and retired. General signed coordinate KL bound remains unproved.','deliverable_status':'COMPLETE_LOCAL; NEW_CLAIM_REVIEW_PENDING','mathematical_status':'LEAD_POINT_TARGET_RESOLVED; C019_GENERAL_PAYMENT_OPEN; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A061-FAIR-TREE-PROCESS','version':1,'status':'A087_ACCEPTED_AT_STATED_SCOPE'},{'claim_id':'A061-LOG-COMPENSATION','version':1,'status':'A087_ACCEPTED_AT_STATED_SCOPE'},{'claim_id':'B13-LOGCHARGE-KL-FORM','version':1,'use':'review handoff; directly checked on point family'},{'claim_id':'B13-LOGCHARGE-SANDWICH','version':1,'use':'source-bound handoff to A087; not independent acceptance by contributor A061'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['REPORT.md','POINT_CERTIFICATE.md','REVIEW_HANDOFF.md','FROZEN_SPEC.json','code/check_points.py','out/POINT_CHECK.json','out/PILOT_FAILURE.md','out/REVIEW_RECEIPTS.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':'Consume independent review and derive exact signed multi-defect cancellation loss in the coordinate KL remainder, beginning with the existing B15 three-point n=5 witness and its actual physical descendants, with terminal costs retained.','stagnant_substantive_attempts':0,'blockers':['Universal constant coordinate KL remainder unproved; new point theorem independent review pending.'],'packet_ids':['A061']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
sourcepaths=[base/'BOARD.md',base/'claude/B13/STREAM_NOTES.md',base/'claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/CLAIMS.json',root/'STATUS.md',oldrun/'PROGRESS.json',oldrun/'CLAIMS.json',reviewrun/'REPORT.md',reviewrun/'CLAIMS.json',Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
sources=[]
for p in sourcepaths:
    raw=p.read_bytes();sources.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('out/SOURCE_RECEIPTS.json',{'time_utc':now,'board_snapshot_read':'2026-10-11 23:29 UTC','lead_notes':'B13 v2 23:1xZ','sources':sources,'receipt_scope':'byte versions accessed; mathematical read locators in REPORT.md; not blanket source acceptance'})
report=(run/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('out/POINT_CHECK.json supplies assertion counts, runtime and the full rational interval endpoints.',f"out/POINT_CHECK.json supplies {results['exact_assertions']:,} exact assertions passed, {results['seconds']:.3f} seconds of checker runtime, and the full rational interval endpoints.")
(run/'REPORT.md').write_text(report,encoding='utf-8')
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
(root/'STATUS.md').write_text('STATE: A061 stage 2 complete: point-function sharp all-dimensional drift R3=4.8676687 and log-charge L3=L4=1.5804820 proved; 39,870 exact assertions PASS; prior baseline A087 accepted; new claim review pending; FEI OPEN.\nNEXT: A087/A094 review point theorem and B13 sandwich/KL handoff; derive signed multi-defect coordinate KL loss on existing B15 n=5 three-point witness with physical descendants and terminal costs retained.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — Stage 2 followed B13 v2 point-function target and consumed A087 independent acceptance of both stage-1 claims. Saved exact H, D/d, lambda/d, KL; proved sharp maxima n=3 for D/d and n=3,4 for lambda/d, all-dimensional monotone tails, and zero Q* at sharp drift price. 126 translated functions /642 splits and n<=128 formula checks passed 39,870 exact assertions in {results["seconds"]:.3f}s. Two interval pilots failed near-unit cancellation; preserved them, repaired log reduction with reciprocal/reversed endpoints at fixed domain and 64 terms. New bundled claim review pending; universal coordinate KL remains unpaid.\n')
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 2: pure point defects have constant/point children and equal coordinate d=2^(1-n). R_n=(H_n-H_(n-1)/2)/d has sharp max R3=12-(9/2)log2 3 and decreases to4 for n>=3. L_n=1-d+d log2((1-2d+2d^2)/d^2) has sharp max L3=L4=(3+log2 10)/4 and tends to1; its successive-dimension sign is exactly q(d)^2-8d^2 q(d/2)=1-4d. KL=n-1-L_n pays the full rare logarithm up to a sharp constant. For interval small log(1-d), reciprocal reduction avoids cancellation from log2(2-2d)-1. A087 independently accepted both A061 v1 baseline claims; retire baseline, do not rerun it. Point symmetry/constant child is lost for multiple signed defects, the next universal-coordinate obstacle.\n')
protocol=json.loads(sourcepaths[-1].read_text())
assert set(progress)=={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((run/'PROGRESS.json').read_text())==json.loads((run/'PACKET_DELTA.json').read_text())
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        raw=p.read_bytes();assert len(raw)<20*1024*1024
        receipts.append({'path':str(p.relative_to(run)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'files':receipts,'protocol_schema_checked':True,'local_only':True,'new_theorem_independently_reviewed':False,'supervisor_copy_or_mirror_verified':False})
print(json.dumps({'status':'COMPLETE_LOCAL_SCHEMA_CHECKED','run':str(run),'exact_assertions':results['exact_assertions'],'prior_baseline_independent_acceptances':len(review_receipts),'new_claims':1,'receipt_files':len(receipts)},indent=2))
