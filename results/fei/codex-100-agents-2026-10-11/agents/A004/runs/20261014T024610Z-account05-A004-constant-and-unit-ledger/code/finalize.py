from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];TEAM=HOME.parent.parent
stamp=datetime.now(timezone.utc).isoformat()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
validation=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS' and validation['assertions']==50390 and validation['runtime_seconds']<60
source=TEAM/'agents/A096/runs/20261014T013836Z-account05-A096-live-gap-ledger/CLAIMS.json'
old=next(c for c in json.loads(source.read_text(encoding='utf-8')) if c['claim_id']=='A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP')
computed=hashlib.sha256(old['exact_statement'].encode()).hexdigest();assert computed==old['statement_sha256']
source_finalizer=source.parent/'code/finalize.py';b=source_finalizer.read_bytes()
(R/'out/sources/A096-finalize.py').write_bytes(b)
manifest=json.loads((R/'out/SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
if not any(x['source']==str(source_finalizer) for x in manifest):manifest.append({'source':str(source_finalizer),'snapshot':'out/sources/A096-finalize.py','sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
save(R/'out/SOURCE_MANIFEST.json',manifest)
review={'reviewer':'A004','at_utc':stamp,'verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR',
 'source_statement_sha256':old['statement_sha256'],'source_hash_convention':'SHA256 of exact statement UTF8, per source code/finalize.py line 14',
 'method':'Independent expanded physical parity substitution, both quotient maps and explicit likelihood ratios; every partial J; direct physical bent edges and all-dimensional complete-normalizer proof',
 'scope':'All finite seeds, every J, common independent spectators, opposite binary sufficient statistic, all-even-d>=2 genuine non-product local-loss obstruction; no universal payment',
 'substantive_repair':False,'proof_source':str(R/'DERIVATION.md'),'locator':'section 1','validation':str(R/'out/VALIDATION.json')}
old['review_records'].append(review);old['status']='INDEPENDENTLY_ACCEPTED_LOCAL_BY_A004_AT_FULL_SOURCE_SCOPE_ADOPTION_PENDING'
statement=('For every actual uniform-cube Boolean seed g(z,y)=A(y)+zD(y), let delta=I_z(g), B_z=sum Phi(Ahat(T)^2,Dhat(T)^2), M_z=sum Dhat(T)^2 log2((Ahat(T)^2+Dhat(T)^2)/Dhat(T)^2), and C_z=B_z-M_z. '
 'Then 0<=C_z<=delta/ln(2). On the original parity-pair shadow g(zu,y), partner-deletion influence-weighted KL loss is L=M_z. For any fresh balanced Boolean encoder h, query actual u first in F=g(u h(x),y), then resolve the encoder completely, retaining y: the variance-weighted shadow bill Q=B_z, hence Q-L=C_z. '
 'If E_h is the fair expected cumulative inherited encoder erasure, averaged over partner branches, and T_K is the actual terminal surplus E[K I(g_leaf)-H(g_leaf)] at bit price K, then T_K-(B_z+delta E_h)=K I(g)-H(g)+JS_z(g)-(K+E_h)delta, while T_K-(M_z+delta E_h) adds C_z to that margin. '
 'For Maj3, E_h=1 under every complete adaptive encoder policy. For the actual AND2 sign seed with one positive atom at K=2, delta=1/2, B_z=1, M_z=C_z=1/2, JS_z=1 and T_2=1; both terminal children are K2-certified but the shadow-plus-inner bank has margin -1/2 whereas the KL-plus-inner bank has margin zero. '
 'Thus constant-free transfer of this exclusive terminal allowance from the KL bank to the shadow bank is false; a safe transfer adds delta/ln(2) bits (delta nats), once. No universal reserve payment or FEI disproof is asserted.')
hypotheses=['Actual finite Boolean signs, uniform disjoint physical supports, entropy/KL in bits and ordinary pivotal influence',
 'Balanced fresh encoder; physical partner u is queried before encoder resolution; complete encoder policy may be adaptive; actual terminal core laws retained',
 'Zero terms continuous; no divisions by delta at delta=0; the KL loss is on the original parity-pair shadow, not an asserted quotient of encoded F',
 'E_h averages actual fair encoder reach weights and partner branches; arbitrary real bit price K; same seed row used for both banks']
new={'claim_id':'A004-KL-SHADOW-EXCLUSIVE-TERMINAL-TRANSFER','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A004'],
 'proof_source':{'path':str(R/'DERIVATION.md'),'locator':'sections 2-5, equations (1)-(5)','validation':str(R/'out/VALIDATION.json')},
 'proof_dependencies':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'status':'independently reconstructed and accepted here; exact complete parity-row ownership'}],
 'review_records':[],'status':'SCOPED_INTERFACE_AND_EXACT_OBSTRUCTION_PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['Unrestricted same-K exclusive terminal-allowance substitution from partner-KL+inherited encoder bank to unlocked-shadow+inherited encoder bank, even when all terminal children satisfy H<=KI'],
 'first_unproved_line':None,'next_consumers':['A003','A026','A096','A087','A094','A057','B01','B06','B20']}
claims=[old,new];save(R/'CLAIMS.json',claims)
save(R/'out/SOURCE_HASH_CHECK.json',{'status':'PASS','claim_id':old['claim_id'],'version':old['version'],'recorded_hash':old['statement_sha256'],'recomputed_hash':computed,'convention':'raw exact statement UTF8; source finalizer pinned'})
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A004','gap_id':'C018-C019-SIGNED-TERMINAL-COLLISION','attempt_id':'A004-cross-route-owner-stage-4',
 'method':'Independent A096 full partner-ownership review; exact common-seed KL/shadow correction, arbitrary balanced-encoder terminal margin, actual AND2 obstruction',
 'mathematical_delta':'A096 single-partner source audit independently accepted. Q-L=C_up with 0<=C_up<=delta/ln2; exact exclusive terminal criterion proved; AND2 KL bank passes but shadow bank misses 1/2 bit. 50390 exact assertions PASS. No universal payment improvement.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_AND_SCOPED_CORRECTION_SAVED','mathematical_status':'SOURCE_AUDIT_ACCEPTED_TRANSFER_CRITERION_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'status':'independently accepted here'},{'source':'A003 stage4 DERIVATION','scope':'sections 1,3,4 directly reconstructed; not blanket independent acceptance'},{'claim_id':'A004-NORMALIZATION-LEDGER','version':2,'scope':'author reapplies full-law conventions; no self-independent acceptance'}],
 'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':old['version'],'change':'A004 independent source-scope acceptance appended; statement unchanged'},{'claim_id':new['claim_id'],'version':1,'change':'one scoped interface/obstruction bundle; review pending'}],
 'source_artifacts':['REPORT.md','DERIVATION.md','CLAIMS.json','out/SOURCE_MANIFEST.json','out/VALIDATION.json','out/PARITY_REVIEW.json','out/TERMINAL_WITNESS.json','out/BENT_CONTROLS.json'],
 'next_consumers':new['next_consumers'],'next_action':'Derive the actual first outer-data-query deficit from certified child surplus with C_up retained once, and select a physical policy owning the negative terminal margin without reusing the same bank.',
 'stagnant_substantive_attempts':0,'blockers':['No local persistence blocker. New narrow cross-route criterion awaits independent review; universal policy/refund and full FEI remain open; shared adoption/mirrors unverified.'],
 'packet_ids':['A004']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
assert set(progress)=={k.split(' (',1)[0] for k in protocol['required_per_run']['progress_fields']}
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
report=(R/'REPORT.md').read_text(encoding='utf-8')
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
save(R/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields':'EXACT','progress_fields':'EXACT','report_fields':'ALL_PRESENT','final_universal_bridge':'PASS','compatibility_byte_identical':True,'source_hash':'PASS','validation_assertions':validation['assertions']})
(HOME/'STATUS.md').write_text('STATE: A004 stage 4 complete locally: A096 partner ownership independently accepted; exact KL/shadow terminal criterion and AND2 half-bit obstruction proved; 50,390 assertions PASS; FEI OPEN.\nNEXT: A003/A026/A096 review; derive actual first outer-data-query refund from certified child surplus, keeping C_up once and full terminal core on one influence budget.\n',encoding='utf-8')
entry=f'\n{stamp}: Stage 4 independently accepted A096 single-partner ownership without repair. Proved Q-L=C_up<=delta/ln2 and exact exclusive terminal margin; AND2 K2 child certificates pay KL+inner exactly but miss shadow+inner by 1/2 bit. Checked 278 seeds/2122 parity lifts/60 compositions/120 unlocking trees/4 bent controls: 50390 assertions PASS in {validation["runtime_seconds"]:.3f}s. Source hash convention verified. No universal constant improvement or FEI counterexample.\n'
if 'Stage 4 independently accepted A096' not in (HOME/'WORKLOG.md').read_text(encoding='utf-8'):
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson='Stage 4: A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 independently accepted by A004 at full source scope. At one seed row, partner deletion L=M_z and unlocked shadow Q=B_z differ exactly by C_up in [0,delta/ln2] bits, [0,delta] nats. For balanced encoder with inherited E_h, terminal margin T_K-(B_z+delta E_h)=K I(g)-H(g)+JS_z-(K+E_h)delta; KL bank adds C_up. Maj3 E_h=1. AND2 K2 gives delta=1/2,B=1,M=C_up=1/2,JS=1,T2=1: KL+inner fits, shadow+inner lacks1/2 bit despite certified children. This refutes only the constant-free exclusive terminal transfer, not FEI or A003 stated claims. Retain full core law and one ownership; next selected-policy child-slack refund.'
if lesson not in (HOME/'LEARNED.md').read_text(encoding='utf-8'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+lesson+'\n')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in str(p) and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/name;receipts.append({'path':'../../'+name,'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/RECEIPTS.json',{'status':'SAVED_LOCAL_READBACK','at_utc':stamp,'files':receipts,'shared_or_remote_verification':False})
print(json.dumps({'status':'LOCAL_COMPLETE','assertions':validation['assertions'],'reviewed_claims':1,'new_scoped_claims':1,'receipted_files':len(receipts),'schema':'PASS'}))
