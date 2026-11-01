from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]; BASE=HOME.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def canonical(c): return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
a011=BASE/'agents/A011/runs/20261014T035454Z-fleet05-A011-representation-existence'
a094=BASE/'agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger'
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
sources=[BASE/'BOARD.md',BASE/'claude/B18/STREAM_NOTES.md',HOME/'STATUS.md',a011/'REPORT.md',a011/'REFERENCE_REPAIR.md',a011/'CLAIMS.json',a094/'AUDIT.md',a094/'CLAIMS.json',HOME/'runs/20261014T013711Z-fleet05-A086-joint-code-referee/RECONSTRUCTION.md',protocol]
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
results={m:json.loads((RUN/f'out/{m.upper()}_RESULTS.json').read_text()) for m in ['parity','unequal','tensor']}
total=sum(x['assertions'] for x in results.values()); assert total==4262
dump(RUN/'out/EXACT_RESULTS.json',{'jobs':results,'total_assertions':total,'floating_point_signs_used':False,'domains_completed':True})
source=json.loads((a011/'CLAIMS.json').read_text(encoding='utf8'))[0]
assert source['statement_sha256']==canonical(source)
source['review_records'].append({'reviewer':'A086/fleet05','verdict':'HOLDS_AT_FULL_STATED_SCOPE','scope':'Entire parity point-edit paid-floor exact statement: arbitrary supplied full positive subprobability, all points/widths, complete mixture posterior/normalizer/CE/debt, physical created/erased accounts, infinite unchanged-reference shock and full independent terminal tensor. No generic core or hereditary reference payment inferred.','method':'Independent signed Walsh and physical-edge reconstruction; separate finite Fraction implementation; exact likelihood/prime-log identities and outward rational signs','proof':str(RUN/'RECONSTRUCTION.md'),'validation':str(RUN/'out/EXACT_RESULTS.json'),'source_claims_sha256':sha(a011/'CLAIMS.json'),'substantive_repair_supplied':False,'contributor_conflict':False})
source['status']='INDEPENDENTLY_RECONSTRUCTED_AT_FULL_STATED_SCOPE_LOCAL'
prior=next(c for c in json.loads((a094/'CLAIMS.json').read_text(encoding='utf8')) if c['claim_id']=='A086-BENT-FLIP-EXCLUSIVE-CHILD-SLACK-CERTIFICATE')
assert canonical(prior)==prior['statement_sha256']; assert any(r.get('verdict')=='HOLDS_AT_FULL_STATED_SCOPE' for r in prior['review_records'])
new={'claim_id':'A086-UNEQUAL-AMPLITUDE-NEUTRAL-POINT-FLOOR','version':1,
 'exact_statement':'Let g on six uniform data bits be -1 exactly when its first three bits equal a specified point and +1 otherwise, with three dummy bits. For every negative data point ystar, every r>=1 fresh point controls with any control point xstar, set p=2^-r,t=2^-6,rho=4pt, F=g(1-2*1_xstar*1_ystar). The actual data Fourier marginal is q=(1-4rho)P_g+3rho delta_empty+rho U_6. Given any fixed data spectral subprobability R of mass s<=1 positive on P_g support and finite cost c=CE(P_g,R), define Rprime=(1-4rho)R+3rho delta_empty+rho U_6 and Qprime=Rprime times the actual conditional control spectrum. This complete fixed output subprobability has mass (1-4rho)s+4rho, exact CE=(1-4rho)c+6rho+H(1-4rho,3rho,rho)-H(J|T)-kappa+B and exact debt (1-4rho)D(P_g||R)-kappa, where J labels the three analytical components, kappa is their measured conditional true/reference posterior KL and B is the true conditional control entropy. It has CE<=c+72 I_sel, I_sel=2rpt, I(g)=3/4, created and erased data charges C=E=6pt and I(F)=3/4+I_sel. Thus for every K, K I(F)-CE>=S_K+(K-72)I_sel with S_K=3K/4-c spent once, and supplied c<=K I(g) transfers with constant max(K,72). Any independent arbitrary Boolean terminal h with prescribed complete finite-cost reference retains the full additive CE c_h and KL D_h under the fixed product reference, with additive physical influence. This is a nonoptimal unequal-amplitude neutral negative-cell reference transfer, not an arbitrary-core, positive-point, hereditary reserve or universal FEI theorem; integer rounding is separate.',
 'hypotheses':['Uniform finite Boolean cubes; three active bits, three dummy bits, actual negative-point sign flip under fresh point controls','Fixed complete finite-cost subprobability source reference positive on the true source spectrum; optional independent terminal reference positive on its true spectrum','Analytical three-component label is not a fair physical-child sampler; costs evaluated under the actual output law','Information quantities bits; ideal CE with separate single-word rounding'],
 'statement_sha256':'','contributors':['A086/fleet05; A011 parity repair and named unequal-amplitude neutral test credited as source context'],
 'proof_source':{'path':str(RUN/'RECONSTRUCTION.md'),'locator':'Sections 1 and 4','validation':str(RUN/'out/UNEQUAL_RESULTS.json'),'tensor_validation':str(RUN/'out/TENSOR_RESULTS.json')},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_NARROW_REFERENCE_CONTINUATION_PENDING_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A011','A094','A097','A095','A039','B18','B20']}
new['statement_sha256']=canonical(new); claims=[source,prior,new]; dump(RUN/'CLAIMS.json',claims)
next_action='Expose one active bit while retaining the incoming floor/reference and source slack, then audit a positive-point edit or three-amplitude core with actual destroyed-edge charges; A011/A094 review new unequal marginal and all-r payment.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B18','packet_id':'A086','gap_id':'C020-SHARED-DATA-COLLISION-REFERENCE-PAYMENT','attempt_id':'A086-stage5-unequal-reference-floor','method':'Independent complete parity reference audit; exact signed neutral unequal-amplitude marginal; measured posterior KL and one-use physical transfer',
 'mathematical_delta':'A011 paid parity floor independently HOLDS at full scope. Prior A086 reserve receives adopted A094 full review. New neutral unequal-amplitude negative-cell data marginal is a positive three-component mixture; full floor CE<=c+72 I_sel, exact debt and arbitrary-terminal cost retained for every r>=1.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_FULL_REVIEW_HOLDS; NEW_UNEQUAL_FLOOR_AUTHOR_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A011-POINT-EDIT-PAID-REFERENCE-FLOOR@1','A086-BENT-FLIP-EXCLUSIVE-CHILD-SLACK-CERTIFICATE@1:A094 review adopted only'],
 'claims_created_or_changed':[c['claim_id']+'@'+str(c['version']) for c in claims],'source_artifacts':[str(p) for p in sources],
 'next_consumers':['A011','A094','A097','A095','A039','B18','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Generic signed magnitude profiles need a positive or otherwise paid reference change; one-use floor/slack transport through active data restrictions is unproved.'],'packet_ids':['A086']}
dump(RUN/'PROGRESS.json',progress); dump(RUN/'PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: Stage 5 complete: A011 parity paid floor full scope HOLDS; prior bank A094 review adopted; neutral unequal-amplitude floor CE<=c+72 I_sel proved pending review; 4,262 exact checks PASS; FEI OPEN.\nNEXT: Active-bit restriction with incoming floor/slack, then positive-point or three-amplitude source; retain destroyed edges and full terminal CE; A011/A094 review new mixture.\n',encoding='utf8')
for file,entry in [('WORKLOG.md','Consumed A094 independent acceptance of prior reserve rather than repeating it. Reconstructed complete A011 parity inherited-reference shock and paid repair without source changes. Found exact unequal-amplitude neutral negative-cell marginal (1-4rho)P_g+3rho delta_empty+rho U_6, proved measured posterior/debt and all-r CE<=c+72I_sel with one-use source slack and arbitrary-terminal tensor. Three sequential pilots passed 4,262 assertions in 0.59/2.79/0.29 seconds; all outputs saved. Generic active-restriction/reference-change payment remains open.'),('LEARNED.md','For any point edit, data marginal is P_g-rho*g(ystar)*ghat(T)*chi_T(ystar)+rho*2^-m; unsigned mixture admission must be proved. The six-bit negative three-cell core has coefficients 3/4,-1/4,0 and exact positive marginal (1-4rho)P_g+3rho delta_empty+rho U_6. Mixing the SAME source reference with those components preserves mass and measured conditional KL; full cost <=c+72I_sel although created and erased data charges are equal. This pays one actual unequal-amplitude insertion, not arbitrary positive-point profiles or inherited-reference changes after active restrictions. A011 parity paid floor full claim independently HOLDS; A094 full review of prior A086 bent child bank was adopted. Exact cancellation log(2^r-1)+log(1/V) removes the spurious log(1-p) selector-entropy loss.')]:
 with (HOME/file).open('a',encoding='utf8') as f: f.write('\n'+now+' '+RUN.name+': '+entry+'\n')
req=json.loads(protocol.read_text())['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in req['progress_fields']}
for c in claims: assert set(c)==set(req['claim_fields'])
assert canonical(new)==new['statement_sha256']; assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf8')
for h in req['report_fields']: assert '## '+h in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'; assert len((HOME/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file():
  assert p.stat().st_size<20*1024*1024; receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'protocol_checks':'PASS','local_only':True,'files':receipts,'rolling_files':[{'path':str(HOME/f),'sha256':sha(HOME/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'protocol_checks':'PASS','claims':len(claims),'exact_assertions':total,'new_result':'unequal-amplitude neutral floor, all r>=1, pending independent review','full_FEI':'OPEN'}))
