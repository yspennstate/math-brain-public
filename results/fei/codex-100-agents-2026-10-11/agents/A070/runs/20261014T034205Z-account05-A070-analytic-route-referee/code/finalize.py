import copy,hashlib,json
from pathlib import Path
run=Path(__file__).resolve().parents[1];agent=run.parents[1];team=agent.parents[1]
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(c):return sha(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=read(protocolpath);fields=protocol['required_per_run'];check=read(run/'out/CHECK.json')
assert check['status']=='PASS' and check['cases']==10384
s69=team/'agents/A069/runs/20261014T030208Z-account05-A069-geometric-transfer'
s88=team/'agents/A088/runs/20261014T024038Z-account05-A088-booleanity-referee'
old=agent/'runs/20261014T005025Z-account05-A070-analytic-route-referee'
c69=read(s69/'CLAIMS.json')[0];assert canonical(c69)==c69['statement_sha256']
source69=copy.deepcopy(c69)
c69['review_records'].append({'reviewer':'account05/A070','verdict':'HOLDS_AT_FULL_STATED_SCOPE','independent':True,'substantive_repair':False,'reviewer_conflict':False,'source':str(s69/'CLAIMS.json'),'source_sha256':sha((s69/'CLAIMS.json').read_bytes()),'proof':str(run/'DERIVATION.md')+' Section1','validation':str(run/'out/CHECK.json'),'method':'Independent two-case edge ratio, conditional Parseval, actual terminal common-tree bills and direct edge/source mask counts; no author code','registry_adoption':'UNVERIFIED'})
c69['status']='INDEPENDENTLY_ACCEPTED_BY_A070_AT_FULL_SCOPE_PENDING_B20'
prev=next(c for c in read(old/'CLAIMS.json') if c['claim_id']=='A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT')
cprev=next(c for c in read(s88/'CLAIMS.json') if c['claim_id']==prev['claim_id'])
assert cprev['exact_statement']==prev['exact_statement'] and cprev['hypotheses']==prev['hypotheses'] and cprev['statement_sha256']==prev['statement_sha256']==canonical(cprev)
cprev=copy.deepcopy(cprev);cprev['status']='A088_INDEPENDENT_ACCEPTANCE_RECEIPT_CONSUMED_PENDING_B20'
cprev['review_records'].append({'reviewer':'account05/A070','verdict':'A088_SOURCE_BOUND_ACCEPTANCE_CONSUMED_NOT_SELF_REVIEW','reviewer_conflict':True,'substantive_repair':False,'source':str(s88/'CLAIMS.json'),'source_sha256':sha((s88/'CLAIMS.json').read_bytes()),'scope':'Exact original signed-conversion/real-control version; accepted independently by A088, not by its contributor A070'})
new={'claim_id':'A070-PARTIAL-PRIVACY-TRANSFER-AND-EXPOSED-EVENT-BOUNDARY','version':1,
 'exact_statement':'For compatible subcube XOR masks q=q1*q2 on disjoint nonempty C,U,V,Y with U=U0 union U1 and V=V0 union V1, U1,V1 nonempty, every Boolean source g(C,U0,V0,Y) independent of U1,V1 has visible-edge conditional mask-disagreement probability at most theta=max(a,b,a+b-2ab)<=1/2, a=2^-|U1|,b=2^-|V1|. For the fixed hierarchy T=(T_Y,(T_C,(T_U,T_V))), Gamma_T(g)<=K I(g), K>=0, implies H(gq)<=Gamma_T(gq)<=max(12,(K+12theta)/(1-theta)) I(gq)<= (2K+12)I(gq), retaining its entire source reference. Fully exposed U can invalidate every uniform ancestral-to-final influence transfer: for t>=4, C={c},U={u},|V|=|Y|=t, q1=1-2*1{c=+,u=+},q2=1-2*1{c=+,V=all+},h=1-2*1{Y=all+},g=q1*h,f=gq=q2*h, the source sees only one exclusive coordinate and Gamma_T(g)<=7I(g), yet I(g)=1+2t2^-t,I(q)=1+t2^-t,I(f)=(3t+1)2^-t, so [7I(g)+12I(q)]/I(f) diverges. The final nonconstant core h remains and H(f)<=4I(f); this is a transfer obstruction, not a FEI disproof. The abstract Boolean edge budget also fails for norm-one real g=sqrt(2)*1{x=+} and single mask flip at x=-,z1=z2=+: I(g)=I(gq)=1/2,I(q)=3/4,theta=1/4,K=M=1 would require5/4<=5/6.',
 'hypotheses':['Finite uniform cubes; actual Boolean signs and ordinary physical influences except explicitly marked normalized-real guard; entropy/code lengths in bits','Compatible global assignments for two subcube events; sequential flips/XOR includes intersection correction','One fixed complete singleton-leaf binary hierarchy shared by source, mask and output; actual core references retained','Partial-privacy sufficient condition requires at least one source-independent coordinate in EACH exclusive block; source is arbitrary on the other indicated coordinates','Paid-source Gamma<=K I is a conditional hypothesis; no construction of arbitrary paid references or same-constant recursion asserted','Cancellation family uses nonconstant point-mask core on an independent t-bit block and binary internal block trees; t>=4','Normalized-real guard uses spectral Dirichlet influence, not Boolean pivotal counts; its source and final both have unit L2 norm'],
 'statement_sha256':'','contributors':['account05/A070'],
 'proof_source':str(run/'DERIVATION.md')+' Sections2-4',
 'proof_dependencies':[{'claim_id':c69['claim_id'],'version':1,'statement_sha256':c69['statement_sha256'],'acceptance':'Independent A070 full-scope review this run; no repair','scope':'Abstract source-independent conditional-edge influence transfer'},{'claim_id':'A069-BOOLEAN-MASK-REFUND','version':1,'statement_sha256':'aa1a04460873eb447b856faa415cf09754940fe50811ca0ab078f305faee0851','acceptance':'A070 stage3 independent acceptance','scope':'Complete hierarchy product subadditivity and W(q)<=12I(q)'}],
 'review_records':[],'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PASSED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered extension to arbitrary private-coordinate-dependent sources: fixed finite A pays7I(g)+12I(q)<=A I(gq), even with Gamma(g)<=7I(g)','Unregistered norm-one real extension of the Boolean conditional-edge influence comparison'],
 'first_unproved_line':None,'next_consumers':['A069','A088','A094','A067','B14','B20']}
new['statement_sha256']=canonical(new)
claims=[c69,cprev,new];write(run/'CLAIMS.json',claims)
nextaction='Choose a normalized final reference on g=q1*h -> q2*h paying the canceled exposed event from one unused child/source slack with original core reference retained; test one non-factorizing branch perturbation under the full signed ledger.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A070','gap_id':'G-A070-STABLE-COMPLETE-ANALYTIC-CODE','attempt_id':'A070-stage4-source-transfer-private-boundary','method':'Independent actual-edge two-case proof, conditional Parseval and final terminal bills; partial-privacy edge-probability enumeration; exact paid-source cancellation family and normalized-real guard',
 'mathematical_delta':'A069 source-blind/unequal-core transfer independently accepted without repair; A088 acceptance of own prior signed conversion consumed; both residual exclusive privacy blocks suffice for source access to private coordinates with factor<=2K+12; fully exposed one-coordinate family defeats all finite ancestral influence transfer factors while retaining a paid source and nonconstant core; H(final)<=4I(final).',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_REVIEW_AND_PARTIAL_PRIVACY_PROOF_COMPLETE_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c69['claim_id'],'version':1,'statement_sha256':c69['statement_sha256'],'acceptance':'Independent A070 this stage at full stated scope'},{'claim_id':'A069-BOOLEAN-MASK-REFUND','version':1,'acceptance':'Independent A070 stage3; baseline not reopened'},{'claim_id':cprev['claim_id'],'version':1,'statement_sha256':cprev['statement_sha256'],'acceptance':'Independent A088 receipt consumed; not A070 self-review'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/PILOT.json','out/CHECK.json','out/EXECUTION_NOTE.md','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A069','A067','A088','A094','B14','B20'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':[{'scope':'Universal C020 and C019','reason':'Arbitrary paid-source admission and once-owned final-reference/child-surplus transfer for a fully exposed canceled event remain open; ancestral influence sum cannot supply it'},{'scope':'Historical cyclic-law examples','reason':'Individual original certificates unrecovered/unreplayed; no use as proof dependencies'}],
 'packet_ids':['A070']}
write(run/'PROGRESS.json',progress);write(run/'PACKET_DELTA.json',progress)
report=(run/'REPORT.md').read_text(encoding='utf-8').replace('@@CASES@@',f"{check['cases']:,}").replace('@@ASSERTIONS@@',f"{check['exact_assertions']:,}").replace('@@SECONDS@@',str(check['seconds']))
(run/'REPORT.md').write_text(report,encoding='utf-8')
sources=[protocolpath,team/'BOARD.md',team/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',s69/'REPORT.md',s69/'DERIVATION.md',s69/'CLAIMS.json',s88/'REPORT.md',s88/'CLAIMS.json',old/'CLAIMS.json']
manifest=[]
for p in sources:
 raw=p.read_bytes();raw.decode('utf-8-sig');manifest.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'scope':'Exact targets/context/accepted source versions and locators listed in REPORT; actual local source bytes read at finalization'})
write(run/'out/SOURCE_MANIFEST.json',manifest)
if not (run/'out/START_STATUS.md').exists():
 (run/'out/START_STATUS.md').write_bytes((agent/'STATUS.md').read_bytes())
assert all(set(c)==set(fields['claim_fields']) for c in claims) and all(canonical(c)==c['statement_sha256'] for c in claims)
assert c69['exact_statement']==source69['exact_statement'] and c69['hypotheses']==source69['hypotheses'] and c69['statement_sha256']==source69['statement_sha256']
assert set(progress)=={x.split(' (',1)[0] for x in fields['progress_fields']}
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in fields['report_fields']) and report.splitlines()[-1].startswith('Universal bridge:') and '@@' not in report
write(run/'out/SCHEMA_CHECK.json',{'status':'PASS','claims':len(claims),'exact_fields':True,'canonical_hashes':True,'reviewed_source_version_unchanged':True,'prior_author_version_not_self_accepted':True,'compatibility_identical':True,'report_sections_present':True,'new_broad_FEI_candidate':False})
(agent/'STATUS.md').write_text(f"STATE: A070 stage4 complete: A069 unequal-core transfer independently HOLDS; partial-private guard proved; exposed one-coordinate paid-source/nonconstant-core bill ratio diverges; {check['exact_assertions']:,} exact checks PASS; FEI OPEN.\nNEXT: A069/A088/A094 review; pay fully exposed canceled-event debit with one final reference and unused child slack, retaining original core reference; test a non-factorizing branch perturbation.\n",encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f"2026-10-14T03:42:05Z stage4: Read board03:35/B14/status/protocol. Accepted A069 source-blind unequal-core transfer at full scope with independent edge/Parseval/terminal reconstruction; consumed A088 acceptance of own previous conversion audit. Proved source-private admission when both exclusive blocks retain unseen bits, factor<=2K+12. Fully exposed U={{u}}: paid g=q1*h, nonconstant h on t Y bits, finalq2*h has ancestral7Ig+12Iq over If unbounded, H<=4I. Certified normalized-real zero-amplitude edge failure5/4>5/6. Pilot initial syntax error prevented search; corrected pilot26cases/213checks; full{check['cases']}cases/{check['exact_assertions']}checks PASS in{check['seconds']}s. All four protocol files, rolling files and receipts saved; final-reference cancellation/child-slack payment and FEI remain open.\n")
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n## Stage 4 durable source-boundary facts\n\n- A069-SOURCE-BLIND-SHARED-EDGE-TRANSFER v1 independently accepted without repair. Actual Boolean source disagreement fixed before private averaging gives t=p or1-p; pointwise edge ratio and same-tree conditional Parseval retain both actual unequal terminal bills.\n- Partial privacy: U=U0+U1,V=V0+V1, U1,V1 nonempty, source on C,U0,V0,Y. Conditional mask edge probability <=max(a,b,a+b-2ab)<=1/2, a=2^-|U1|,b=2^-|V1|. Paid source Gamma<=K I transfers at max(12,(K+12theta)/(1-theta))<=2K+12. One source-private coordinate is safe in a width>=2 exclusive block.\n- Fully exposed boundary t>=4: q1 flips c+,u+; q2 flips c+,V-all+ (|V|=t); h point mask on |Y|=t; g=q1*h and finalq2*h. Gamma(g)<=7I(g), Ig=1+2t2^-t, Iq=1+t2^-t, If=(3t+1)2^-t, R_I=2-2^-t. Ancestral[7Ig+12Iq]/If diverges while actual Hf<=4If and nonconstant h stays. No finite uniform unsigned ancestral influence conversion can replace a selected signed final reference.\n- Norm-one real guard: g=sqrt(2)1{x+}, q single flip atx-,z1=z2+ gives gq=g, Ig=If=1/2,Iq=3/4,theta1/4. Boolean K=M=1 edge factor5/3 fails5/4>5/6. The discrete actual-pivot comparison is indispensable; this does not certify failure of a bare real entropy access inequality.\n- A088 stage4 independent acceptance of own prior signed-conversion audit consumed, no self-review. Historical cyclic-law certificates still unrecovered/unreplayed and excluded from dependencies.\n')
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in list(run.rglob('*'))+[agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
 if p.is_file() and p.name!='PERSISTENCE.json':
  raw=p.read_bytes();assert len(raw)<20_000_000;receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw)})
write(run/'out/PERSISTENCE.json',{'status':'LOCAL_SAVE_READBACK_COMPLETE','files':receipts,'central_adoption_verified':False,'supervisor_copy_verified':False,'remote_mirror_verified':False})
assert all(sha(Path(p['path']).read_bytes())==p['sha256'] for p in receipts)
print(json.dumps({'status':'PASS','cases':check['cases'],'exact_assertions':check['exact_assertions'],'claims':len(claims),'files_receipted':len(receipts)}))
