import copy,hashlib,json
from pathlib import Path
run=Path(__file__).resolve().parents[1];agent=run.parents[1];team=agent.parents[1]
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(c):return sha(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=read(protocol_path);fields=protocol['required_per_run']
check=read(run/'out/CHECK.json');assert check['status']=='PASS' and check['cases']==70147
s69=team/'agents/A069/runs/20261014T000110Z-fleet05-A069-geometric-transfer'
s67=team/'agents/A067/runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement'
s88=team/'agents/A088/runs/20261013T234248Z-fleet05-A088-booleanity-referee'
old=agent/'runs/20261013T212602Z-fleet05-A070-analytic-route-referee'
base=team/'agents/A069/runs/20261011T224507Z-fleet05-A069-geometric-transfer'
c69=read(s69/'CLAIMS.json')[0];assert canonical(c69)==c69['statement_sha256']
c69['review_records'].append({'reviewer':'fleet05/A070','verdict':'ACCEPT_AT_STATED_SCOPE','reviewer_conflict':False,'no_mathematical_repair':True,'source':str(s69/'CLAIMS.json'),'source_sha256':sha((s69/'CLAIMS.json').read_bytes()),'proof_reconstruction':str(run/'DERIVATION.md')+' Section 1','implementation':'Independent integer Walsh spectra versus direct ordered resampling-pair counts; no author code imported','validation':{'cases':check['cases'],'exact_assertions':check['exact_assertions'],'certificate_sha256':check['certificate_sha256']},'adoption':'PENDING_B20'})
c69['status']='INDEPENDENTLY_ACCEPTED_BY_A070_AT_SCOPE_PENDING_B20'
accepted=[]
incoming=read(s67/'CLAIMS.json');oldclaims=read(old/'CLAIMS.json')
for cid,version in [('B14-LEAD-POINT-DEFECT-NEUTRALIZATION',2),('A070-TWO-EDIT-PROJECTION-CROSS-LEDGER',1)]:
 src=next(c for c in incoming if c['claim_id']==cid and c['version']==version)
 prev=next(c for c in oldclaims if c['claim_id']==cid and c['version']==version)
 assert src['exact_statement']==prev['exact_statement'] and src['hypotheses']==prev['hypotheses']
 assert canonical(src)==src['statement_sha256']==prev['statement_sha256']
 rec=copy.deepcopy(src);rec['status']='INDEPENDENTLY_ACCEPTED_BY_A067_RECEIPT_CONSUMED_PENDING_B20'
 rec['review_records'].append({'reviewer':'fleet05/A070','verdict':'SOURCE_BOUND_A067_ACCEPTANCE_CONSUMED_NOT_SELF_REVIEW','reviewer_conflict':True,'source':str(s67/'REVIEW_AND_CORRECTIONS.md'),'source_sha256':sha((s67/'REVIEW_AND_CORRECTIONS.md').read_bytes()),'acceptance_scope':'Exact cited version; independent A067 reconstruction supplies acceptance','mathematical_repair_by_A070_this_stage':False})
 accepted.append({k:rec[k] for k in fields['claim_fields']})
audit={'claim_id':'A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT','version':1,
 'exact_statement':'For the two-bit root code L(empty)=1,L(nonempty)=3, u=(12+5x1)/13 and v=u^2/||u^2||_2=(169+120x1)/sqrt(42961) both have unit L2 norm, but W(v)=28800/42961>2W(u)=100/169, with positive integer comparison gap 571100. Thus Boolean hierarchy product-cost subadditivity does not extend to normalized real products. For every fixed hierarchy and Boolean g,q, with R_T the conditional-resampling cost refund and R_I=2 sum_i P(both g and q disagree on the physical i-edge), K I(gq)-Gamma(gq)=[K I(g)-Gamma(g)]+[K I(q)-W(q)]+R_T-KR_I for every real K. Compatible overlapping masks on c,u,v, q=(1-c)/2+(1+c)uv/2 and source g=q*y under T=(y,(c,(u,v))) retain the nonconstant final core f=y, yet R_T=13/2<12R_I=36. Their full source/mask/converted banks at K=12 are 49/2,14,-59/2 and sum to final slack 9. This refutes only refund-alone final-influence conversion, not the accepted arbitrary-source mask-cost theorem.',
 'hypotheses':['Uniform finite cubes, entropy/code units bits, fixed hierarchy chosen before the spectral sample','W(u)=Gamma(u)-1 for normalized functions; real witness explicitly renormalizes its product','Physical XOR, R_I and conversion identities require actual Boolean signs','Witness blocks C={c},U={u},V={v},Y={y}; compatible events {c=+,u=+},{c=+,v=+}; sequential flips/XOR','Source slack, mask bank and complete final core code cost are retained; no universal paid-source hypothesis'],
 'statement_sha256':'','contributors':['fleet05/A070'],'proof_source':str(run/'DERIVATION.md')+' Sections 2-3','proof_dependencies':[],'review_records':[],
 'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PASSED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered real extension Gamma(normalized uw)<=Gamma(u)+Gamma(w)-1 for all norm-one real u,w','Unregistered shortcut R_T(g,q)>=12 R_I(g,q), even for compatible overlapping masks with nonconstant final core'],
 'first_unproved_line':None,'next_consumers':['A069','A067','A088','A094','B14','B20']}
audit['statement_sha256']=canonical(audit)
claims=[c69,*accepted,audit];write(run/'CLAIMS.json',claims)
nextaction='Construct one normalized output reference for g(c,Y) with two unequal certified conditional cores under compatible overlapping masks; pay total signed conversion with both terminal bills and one physical influence partition.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A070','gap_id':'G-A070-STABLE-COMPLETE-ANALYTIC-CODE','attempt_id':'A070-stage3-mask-refund-independent-audit','method':'Independent conditional-variance/XOR proof, integer Walsh versus direct resampling counts, normalized-real product and exact physical-edge conversion diagnostics',
 'mathematical_delta':'A069 simultaneous Boolean mask refund independently accepted without repair; A067 acceptance of own prior v2 repair/cross claim consumed; normalized-real extension refuted; nonconstant terminal-core witness rules out refund-alone final-influence conversion while preserving all signed banks.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_REVIEW_COMPLETE_EXACT_DIAGNOSTICS_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A069-STABLE-HIERARCHY-EDIT-PAYMENT','version':1,'acceptance':'A070 stage1 independent acceptance; baseline not reopened'},{'claim_id':c69['claim_id'],'version':1,'statement_sha256':c69['statement_sha256'],'acceptance':'A070 independent scope acceptance this stage'},*({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'acceptance':'A067 exact source-bound acceptance consumed, not A070 self-review'} for c in accepted)],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/PILOT.json','out/EXECUTION_NOTE.md','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A069','A067','A088','A094','B14','B20'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':[{'scope':'Universal C020/C019 conversion','reason':'No selected output reference or once-owned final-influence payment for unequal arbitrary conditional cores; exact refund retains source Gamma'},{'scope':'Historical cyclic-law replay','reason':'Original individual certificates not recovered; not used as dependencies or asserted checked'}], 'packet_ids':['A070']}
write(run/'PROGRESS.json',progress);write(run/'PACKET_DELTA.json',progress)
report=(run/'REPORT.md').read_text(encoding='utf-8').replace('@@CASES@@',f"{check['cases']:,}").replace('@@ASSERTIONS@@',f"{check['exact_assertions']:,}").replace('@@SECONDS@@',str(check['seconds']))
(run/'REPORT.md').write_text(report,encoding='utf-8')
sourcefiles=[protocol_path,team/'BOARD.md',team/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',old/'REPORT.md',old/'CLAIMS.json',s69/'REPORT.md',s69/'DERIVATION.md',s69/'CLAIMS.json',s67/'REPORT.md',s67/'REVIEW_AND_CORRECTIONS.md',s67/'CLAIMS.json',s88/'REPORT.md']
manifest=[]
for p in sourcefiles:
 raw=p.read_bytes();raw.decode('utf-8-sig');manifest.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'scope':'Exact source/dependency/review locators in REPORT; current source bytes read at finalization'})
write(run/'out/SOURCE_MANIFEST.json',manifest)
(run/'out/START_STATUS.md').write_bytes((agent/'STATUS.md').read_bytes())
assert all(set(c)==set(fields['claim_fields']) for c in claims)
assert all(canonical(c)==c['statement_sha256'] for c in claims)
assert set(progress)=={k.split(' (',1)[0] for k in fields['progress_fields']}
assert all('## '+h in report for h in fields['report_fields']) and report.splitlines()[-1].startswith('Universal bridge:')
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
write(run/'out/SCHEMA_CHECK.json',{'status':'PASS','claims':len(claims),'statement_hashes_canonical':True,'claim_and_progress_field_sets_exact':True,'report_sections_present':True,'compatibility_copy_identical':True,'prior_author_versions_not_self_accepted':True,'new_universal_FEI_candidate':False})
(agent/'STATUS.md').write_text(f"STATE: A070 stage3 complete: A069 Boolean mask refund independently HOLDS; A067 accepted prior repair/cross ledger; {check['exact_assertions']:,} exact checks PASS; normalized-real extension and refund-only conversion refuted; FEI OPEN.\nNEXT: A088/A094 review; construct one output reference for unequal shared-control core branches with signed final-influence conversion, both terminal bills and one physical budget.\n",encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f"2026-10-14T00:50:25Z stage3: Read BOARD/B14/status and consumed A069 Boolean mask refund as a new useful dependency. Independently reconstructed and accepted v1 at scope, without repair. Consumed A067's independent acceptances of own neutralization v2 and cross ledger v1. Certified normalized-real product failure (integer gap 571100), and nonconstant final-core witness R_T=13/2 versus 12R_I=36; complete source/mask banks restore final slack9. Pilot57cases/236checks passed; first full attempt stopped by55s guard, no certificate counted. Same-domain v1.1 full replay passed {check['cases']}cases/{check['exact_assertions']}checks in {check['seconds']}s under180s cap. All protocol files saved; source-compatible unequal-core conversion and full FEI remain open.\n")
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n## Stage 3 durable referee facts\n\n- A069-BOOLEAN-MASK-REFUND v1 independently accepted at scope: conditional resampling gives W=2 sum b P(disagreement); Boolean XOR gives exact nonnegative product refund, and compatible masks have Gamma(gq)<=Gamma(g)+12I(q). Source Gamma is retained. This is code-cost payment, not physical stopping-tree ownership.\n- The Boolean hypothesis is indispensable: norm-one u=(12+5x1)/13 and normalized square v=(169+120x1)/sqrt(42961) under the two-bit root code have W(v)=28800/42961>2W(u)=100/169, integer gap571100. Conditional variance versus inequality-disagreement and XOR both fail for real values.\n- Exact physical bank: KI(gq)-Gamma(gq)=(KI(g)-Gamma(g))+(KI(q)-W(q))+R_T-KR_I, R_I twice joint physical-edge pivots. Positive mask bank alone does not pay signed conversion.\n- Compatible overlapping q=(1-c)/2+(1+c)uv/2, g=q*y, T=(y,(c,(u,v))), final y: Gamma_g=11/2, Gamma_final=3, Iq=3/2, R_T=13/2,R_I=3. At K12 the conversion is-59/2; source49/2 plus mask14 yields final9. Both source slack and nonconstant terminal core must remain.\n- A067 stage3 independently accepted repaired neutralization v2 and own cross-ledger v1; source-bound receipt consumed, no self-review. Historical cyclic-law individual certificates remain unavailable/unreplayed; do not claim their reproduction.\n')
receipts=[]
for p in list(run.rglob('*'))+[agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
 if p.is_file() and p.name!='PERSISTENCE.json':
  raw=p.read_bytes();assert len(raw)<20_000_000;receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw)})
write(run/'out/PERSISTENCE.json',{'status':'LOCAL_SAVE_READBACK_COMPLETE','files':receipts,'B20_adoption_verified':False,'supervisor_copy_verified':False,'remote_mirror_verified':False})
print(json.dumps({'status':'PASS','cases':check['cases'],'exact_assertions':check['exact_assertions'],'claims':len(claims),'files_receipted':len(receipts)}))
