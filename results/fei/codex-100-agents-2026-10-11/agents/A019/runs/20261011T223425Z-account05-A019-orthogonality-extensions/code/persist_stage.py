import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; B=R.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement='For every Boolean core g on a uniform data cube and all mutually disjoint fresh selector blocks W_j of positive sizes k_j, arbitrary translation vectors v_j and point indicators A_j, set F(w,y)=g(y+sum_j v_j A_j(w_j)). With rho_j=Pr[g(y)!=g(y+v_j)] and E_k=H(1-2*1_point) on k bits, H(F)=H(g)+sum_j rho_j E_kj, I_data(F)=I(g), I_W(F)=sum_j rho_j 2 k_j 2^(-k_j), M_W=0 and B_W=sum_j rho_j E_kj<=4 I_W(F). Constant 4 is optimal as I_W/|W| tends to zero. A certified core FEI constant C transfers to max(C,4), including arbitrary finite nesting with fresh selector modules. Complete-module block trees have the same payment and retain terminal core entropy. The constant 4 cannot be assigned to every singleton query, as the three-bit point module on a dictator shows.'
hyp=['Uniform independent physical coordinates; entropy in bits','Selector module blocks pairwise disjoint and fresh from current data','g Boolean; vectors may coincide or be linearly dependent','Translation activation in each module is exactly one point','An FEI bound on the arbitrary terminal core is an additional hypothesis only for full-entropy closure']
claim={
'claim_id':'A019-RARE-TRANSLATION-COLLISION','version':1,'exact_statement':statement,'hypotheses':hyp,
'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
'contributors':['A019'],'proof_source':'REPORT.md sections 1-6; NEW_SHARED_DATA_CLASS.tex; code/check_translation.py; out/CHECK.json',
'proof_dependencies':[],'review_records':[{'reviewer':'A019','verdict':'AUTHOR_ANALYTIC_PROOF_AND_EXACT_CHECKS','independent':False}],
'status':'PROVED_AT_STATED_SCOPE_INDEPENDENT_REVIEW_PENDING','supersedes':None,'refutes':[],'first_unproved_line':None,
'next_consumers':['A017','A020','A027','A028','A058','A060','A064','A090','A091']}
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B04','packet_id':'A019','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A019-rare-disjoint-translation-1',
'method':'Exact Boolean coefficient row factorization under input translations; point-defect module spectra; proper physical block stopping certificate',
'mathematical_delta':'Sharp B_W<=4 I_W with M_W=0 for arbitrary shared cores, repeated translation vectors, unbounded arity and fresh nesting; I_W/a->0 examples; singleton constant-4 guard and exact bent-splice exclusion',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'STRUCTURAL_PACKET_RESOLVED_AT_STATED_SCOPE_FULL_FEI_OPEN',
'claim_versions_used':['C035 / threshold Proposition 8.6 (source baseline; independently derived here)','A018-COLLISION-BLOCK-INTERFACE v1 (analytic reconstruction in REVIEW_DEPENDENCIES.md; not required as an unproved premise)'],
'claims_created_or_changed':['A019-RARE-TRANSLATION-COLLISION v1'],
'source_artifacts':['REPORT.md','NEW_SHARED_DATA_CLASS.tex','COLLISION_PAYMENT.md','REVIEW_DEPENDENCIES.md','code/check_translation.py','out/FROZEN_SPEC.json','out/CHECK.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':claim['next_consumers'],
'next_action':'Compute the exact signed collision correction for two rare-point translation modules sharing exactly one selector coordinate, preserving terminal core entropy and physical influence nonreuse; A091/A090 independently reconstruct current theorem.',
'stagnant_substantive_attempts':0,'blockers':['Universal factorization/stopping selection and terminal-core FEI remain open; independent extension review and supervisor adoption pending; B04 lead notes absent at stage start'],
'packet_ids':['A019']}
def put(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
put(R/'CLAIMS.json',{'claims':[claim]});put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
check=json.loads((R/'out/CHECK.json').read_text())
(B/'STATUS.md').write_text('STATE: A019 structural packet proved locally: sharp rare-translation B_W<=4I_W, M_W=0, unbounded low-disagreement/depth closure; '+str(check['assertions'])+' exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A091/A090 review; derive signed collision correction for two rare translation modules sharing one selector bit, retaining terminal core and nonreused physical block payment.\n',encoding='utf-8')
with (B/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' — A019 stage: read protocol/board and A018 handoff; lead notes absent. Replaced suggested quadratic phase direction by sparse disjoint conjunction translations of arbitrary cores. Proved exact rho-weighted collision ledger and sharp constant 4 as disagreement vanishes; explicit nested closure and block tree. Found singleton constant-4 failure at k=3 and preserved inherited bent-splice no-go. '+str(check['cases'])+' actual Boolean cases / '+str(check['assertions'])+' exact assertions PASS. A018 interface analytically reconstructed at scope. All output local; independent review/adoption pending.\n')
with (B/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n## Rare input translation collision, '+now+'\nFor F(w,y)=g(y+sum_j v_j A_j(w_j)) on disjoint selector blocks, rho_j=sum_(T dot v_j=1) ghat(T)^2 is actual translation disagreement. General Boolean module phases h_j=(-1)^A_j give exact H(F)=H(g)+sum rho_j H(h_j), I_W=sum rho_j I(h_j), I_data=I(g), M_W=0. Point indicators on k bits have empty squared mass (1-2delta)^2 and other masses 4delta^2, delta=2^-k; E_k/(2kdelta)<4 and tends to4. Thus exact low-energy closure at max(C,4), no floor on disagreement, repeated/dependent v allowed. Fresh nested steps telescope. Whole-module blocks pay once and retain arbitrary terminal entropy. Do not refine to singleton constant4: k3 dictator case has Delta_i/I_i=4(E_3-1)>4, certified by 3^9<2^16. Bent point surgery changes branch magnitudes and is excluded; equal magnitudes alone encode full FEI, so phase factorization is essential. Overlapping selector blocks break the tensor-product proof; compute one shared-coordinate correction next.\n')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
cf=protocol['required_per_run']['claim_fields'];pf=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']]
assert set(claim)==set(cf),(set(claim)^set(cf));assert set(progress)==set(pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert (B/'STATUS.md').read_text().count('\n')==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in (R/'REPORT.md').read_text()
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[B/s for s in ('STATUS.md','WORKLOG.md','LEARNED.md')]
receipts=[]
for p in files:
 data=p.read_bytes();assert len(data)<20*1024*1024
 receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
put(R/'out/PERSISTENCE_RECEIPTS.json',{'at':now,'schema_keys_exact':True,'compatibility_identical':True,'rolling_status_two_lines':True,'full_fei':'OPEN','independent_extension_review':'PENDING','mirror_receipt':'NOT_CLAIMED','files':receipts})
print(json.dumps({'status':'SAVED','files':len(receipts),'claims':1,'assertions':check['assertions']}))
