from pathlib import Path
import hashlib,json,datetime

r=Path(__file__).resolve().parents[1];root=r.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,x):p.write_text(json.dumps(x,indent=2),encoding='utf-8')
statement=('For every integer w>=4, set m=2^w,p=1/m,beta=1-p,n=mw and let f_w=1-2 product_(b=1..m)(1-A_w(x_b)) '
 'be the actual Boolean OR sign of disjoint width-w point conjunctions. For each coordinate i define '
 'epsilon_i=Inf_i, mu_i(T)=fhat(T+i)^2/epsilon_i, r_i(T)=fhat(T)^2+fhat(T+i)^2, and let bar_mu_i,bar_r_i '
 'be their pushforwards under T->|T|. Every epsilon_i=epsilon=2p beta^(m-1), I=2w beta^(m-1), and '
 '0<=D2(bar_mu_i||bar_r_i)<=3+log2(w+1/2). Defining M=sum_i epsilon_i[log2(1/epsilon_i)-D2(mu_i||r_i)] '
 'and M_degree=sum_i epsilon_i[log2(1/epsilon_i)-D2(bar_mu_i||bar_r_i)], one has '
 'M_degree/I>=w-4-log2(w+1/2), hence M_degree/I>=w/2 for w>=32, while 0<=M<=B<=H<=6I for all w>=4. '
 'The exact discarded conditional refund is M_degree-M=sum_i epsilon_i sum_t bar_mu_i(t) '
 'D2(mu_i(.|t)||r_i(.|t)), and divided by I it is at least w/2-6 for w>=32. Thus no absolute K '
 'makes M_degree<=K I for all actual Boolean signs; no FEI disproof or obstruction to full function-specific row references is asserted.')
claim={'claim_id':'A090-DEGREE-COARSENED-REFUND-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform physical cube, actual Boolean OR sign of independent point conjunctions',
 'w>=4 integer; m=2^w; disjoint width-w blocks; all coordinates relevant',
 'Normalized Fourier probabilities; entropy and KL in bits; ordinary physical influence',
 'Coarsening is residual Fourier degree, not physical restriction or full-subset exchangeability',
 'Complete normalized derivative and reference row laws; zero terms by continuity'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A090'],
 'proof_source':{'path':str(r/'REPORT.md'),'locators':['equations (1)-(19)','DEGREE_REFUND_PROOF.tex'],
 'checker':'code/check_degree.py','certificates':['out/PILOT.json','out/CHECK.json']},
 'proof_dependencies':[],'review_records':[{'reviewer':'A094','verdict':'PENDING'},{'reviewer':'A085','verdict':'PENDING_ALTERNATE'}],
 'status':'AUTHOR_PROVED_MECHANISM_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['There exists one finite absolute K such that the actual normalized derivative/reference refund coarsened to residual Fourier degree satisfies M_degree(f)<=K I(f) for every finite uniform-cube Boolean sign. This is a tested downstream shortcut, not an assertion attributed to A096 or A099.'],
 'first_unproved_line':None,'next_consumers':['A096','A001','A073','A099','A064','A094','A085','B18','B20']}
save(r/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':r.name,'stream':'B18','packet_id':'A090',
 'gap_id':'OPEN-C018-TERMINAL-KL','attempt_id':'A090-independent-reconstruction-3',
 'method':'Audit of normalized terminal-refund degree compression; actual Boolean block-spectrum and binomial likelihood-ratio proof with exact generating-function certificates',
 'mathematical_delta':'On actual tribes, degree-only refund retains cost/I>=w/2 while full retained M/I<=6; discarded within-degree conditional KL/I>=w/2-6. New mechanism boundary, not FEI disproof.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'DEGREE_COMPRESSION_REFUTED_NEW_PROOF_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A096-TERMINAL-KL-REFUND-AUDIT','version':1,
 'status':'Prior scoped normalized identities independently reviewed by A073/A099; row definitions consumed and identity rederived; no universal lower bound assumed'},
 {'claim_id':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS','version':1,
 'status':'Independent A096/A099 review receipts consumed; not a proof dependency of the new obstruction'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new self-contained all-width actual-Boolean mechanism obstruction, pending independent review'}],
 'source_artifacts':['REPORT.md','CLAIMS.json','DERIVATION_CHECKPOINT.md','DERIVATION_REFINEMENT.md',
 'DEGREE_REFUND_PROOF.tex','FROZEN_SPEC.json','code/check_degree.py','out/PILOT.json','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Audit a proposed full conditional reference retaining or paying the within-degree KL term on the same tribes and parity-tensor activation rows, with one physical influence reserve and terminal core entropy.',
 'stagnant_substantive_attempts':0,
 'blockers':['No dimension-independent signed-Boolean lower bound on the full terminal divergence has been supplied; universal payment remains open.'],
 'packet_ids':['A090']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:save(r/name,progress)
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
fields=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(fields['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
check=json.loads((r/'out'/'CHECK.json').read_text());assert check['status']=='PASS'
report=r/'REPORT.md';s=report.read_text(encoding='utf-8')
s=s.replace("The new downstream exclusion is stronger than A001's influence-only reference scope:",
 "The new downstream exclusion adds a function-dependent boundary beyond A001's influence-only reference scope:")
assert all('## '+h in s for h in fields['report_fields'])
assert s.rfind('## Universal bridge')>s.rfind('## actual persistence')
report.write_text(s,encoding='utf-8')
(root/'STATUS.md').write_text(
 'STATE: Stage 3 complete: degree-coarsened terminal refund fails on actual tribes, M_degree/I>=w/2 vs full M/I<=6; 12,836 exact checks PASS; review pending; FEI OPEN.\n'
 'NEXT: A094/A085 reconstruct within-degree KL obstruction; A096/A001/A073 supply one full conditional reference retaining that refund and terminal core entropy.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | '+r.name+' | Read current board/B18/status. Prior tail accepted by A096/A099; normalized refund already reviewed, not repeated. '
 'Derived actual-tribes degree compression obstruction: D_degree<=3+log2(w+1/2), M_degree/I>=w/2 (w>=32), '
 'full M<=H<=6I; missing within-degree divergence/I>=w/2-6. '
 'Saved before compute; pilot557 checks/0.0147s, main12836 checks/1504 packets/2.169s PASS. '
 'New author proof pending review; no source positive theorem refuted and no FEI disproof.\n')
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage 3: For normalized derivative/reference rows, degree coarsening loses exactly '
 'sum_i eps_i sum_t mu_bar_i(t) KL(mu_i(.|t)||r_i(.|t)); M_degree-M equals this nonnegative loss. '
 'For actual OR of m=2^w width-w point conjunctions, every eps=2/m*(1-1/m)^(m-1), I=2w beta^(m-1). '
 'Coordinate transitivity gives mu_bar(t)=(t+1)W_(t+1)/I and r_bar(t)=(1-t/n)W_t+(t+1)W_(t+1)/n; '
 'it does not give uniformity of full subsets within degree. '
 'Active count Bin(m,1/m) and forced-block likelihood ratio yield mu_bar(t)<=(2p/beta+2beta*t)nu_t. '
 'Head/tail proof gives D_degree<=3+log2(w+1/2), so M_degree/I>=w/2 for w>=32, whereas '
 'true M<=B<=H<=6I. Conditional within-degree refund/I diverges. '
 'New obstruction pending independent review; full A096 terminal KL target stays open and is not refuted.\n')
base=root.parent
inputs=[protocol,root.parents[1]/'BOARD.md',root.parents[1]/'claude'/'B18'/'STREAM_NOTES.md',
 base/'A096'/'runs'/'20261013T220343Z-fleet05-A096-live-gap-ledger'/'CLAIMS.json',
 base/'A099'/'runs'/'20261014T001305Z-fleet05-A099-candidate-assembly'/'CLAIMS.json',
 base/'A001'/'runs'/'20261013T213937Z-fleet05-A001-quantifier-audit'/'CLAIMS.json',
 Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_REDUCTION.md')]
manifest=[]
for p in inputs:
 b=p.read_bytes();manifest.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(r/'out'/'SOURCE_MANIFEST.json',manifest)
save(r/'out'/'SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,
 'report_fields_present':True,'progress_delta_byte_equal':True,'statement_hash_checked':True,'self_acceptance':False})
receipts={'timestamp':now,'status':'LOCAL_SAVED','external_copy':'NOT_PERFORMED','files':[]}
for p in list(r.rglob('*'))+[root/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]:
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  receipts['files'].append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(r/'out'/'RECEIPTS.json',receipts)
print(json.dumps({'schema':'PASS','new_claim':'AUTHOR_PROVED_PENDING_REVIEW','assertions':check['assertions'],
 'degree_packets':check['residual_degree_packets'],'receipted_files':len(receipts['files'])}))
