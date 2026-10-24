from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
TEAM=A.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
source=TEAM/'agents/A007/runs/20261014T100124Z-account05-A007-root-normalization'
deps=[c for c in read(source/'CLAIMS.json') if c['claim_id']=='A007-EXACT-ROOT-TILTED-OCCUPATION']
assert len(deps)==1
d=deps[0]
assert d['statement_sha256']==hashlib.sha256(d['exact_statement'].encode()).hexdigest()
dep={'claim_id':d['claim_id'],'version':d['version'],'statement_sha256':d['statement_sha256'],
     'status':'SOURCE_INTERFACE_U1_RECONSTRUCTED_SCOPED_NO_ALL_U_ACCEPTANCE',
     'proof_source':str(source/'JOINT_OCCUPATION.md')}
stmt=('For gamma=6/5 and the source-defined one-fresh-control distributed correction Psi '
      'under any fixed original positive feasible prime reference, SAME posterior eta_T, '
      'and 0<beta<=1 with beta sum lambda<=1, let v=Var(g) and '
      'M=sum_{T nonempty}ghat(T)^2 E_eta_T(|V|-1). Then 0<=M<=I(g)-v and '
      'Psi<=[log2(1/beta)/2+(3/5)log2(e)+1/20]M. An alternative bound is '
      'Psi<=(v/2)log2 beta+[log2(1/beta)/2+(3/10)log2(e)+1/20]I(g). '
      'No private leaf, bounded read or ownership-entropy tail is required. '
      'For the actual leafless K_m,m edge-prime Boolean family g=2[(OR x) AND (OR y)]-1, '
      'fixed lambda_ij=1/m and beta=1/m, every integer m>=4 satisfies '
      'Psi/I(g)>=(15/64)log2 m-217/160, and M/I(g) tends to1. '
      'All nonempty-data sectors, SAME original posterior, root/factorial credits and '
      'signed normalization are included. These are statements about the source-defined '
      'rank-stripped transferred correction, not actual optimal code cost, the infimum '
      'over references, or FEI. Inherited complete base cost, rank-transfer and '
      'control-only T=empty overhead remain separate.')
claim={'claim_id':'A015-ONE-CONTROL-EXCESS-GATE-BOUND-AND-LEAFLESS-TRANSFER-BARRIER',
       'version':1,'exact_statement':stmt,
       'hypotheses':['Uniform finite Boolean cube, base-two entropy/cost units, gamma6/5',
                     'Source-defined actual chronological forest posterior and distributed-lift correction, not an arbitrary spectral probability law',
                     'One common fresh positive control, original positive feasible lambda fixed before spectral selection, 0<beta<=1 and beta sum lambda<=1',
                     'Used sizes s_l>=1, s_l<=kappa_l<=|T|, sum s_l=|T|; actual tree-component roots with 0<pi<=1',
                     'Obstruction fixes the exact K_m,m positive edge primes and lambda=1/m,beta=1/m for every m>=4; it does not quantify over every reference'],
       'statement_sha256':hashlib.sha256(stmt.encode()).hexdigest(),'contributors':['A015'],
       'proof_source':{'bound':str(R/'ONE_CONTROL.md'),'obstruction':str(R/'LEAFLESS_SCALE.md'),
                       'review':str(R/'REVIEW_A007.md'),'certificates':[str(R/'out/EXACT_CHECK.json'),str(R/'out/LEAFLESS_EXACT.json')]},
       'proof_dependencies':[dep], 'review_records':[],
       'status':'AUTHOR_PROVED_EXACTLY_CHECKED_CONDITIONAL_ON_SOURCE_INTERFACE_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],
       'refutes':[{'statement':'M log2(sum lambda)<=K I(g) for every feasible original reference with sum lambda>=1 and absolute K',
                   'witness':'K_m,m exact positive edge primes at lambda=1/m; M/I tends to1 and sum lambda=m',
                   'scope':'Additional proposed standalone payment, no accepted registered claim refuted'},
                  {'statement':'Psi<=K I(g) for every fixed feasible uniform graph-edge reference and absolute K',
                   'witness':'Same K_m,m family, beta=1/m; full source-defined Psi lower bound in LEAFLESS_SCALE.md (10)',
                   'scope':'Fixed-reference transferred-surrogate obstruction; no variational or actual-code lower transfer'}],
       'first_unproved_line':None,'next_consumers':['A007','A008','A009','A011','A086','A094','B03','B20']}
write(R/'CLAIMS.json',[claim])
next_action='Pay empty-control scale plus inherited complete core/reference cost jointly on K_m,m using one replacement feasible reference or an exact same-reference numerator; retain control-only overhead and all signed credits before arbitrary leafless incidence.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A015',
          'gap_id':'G-J-COST','attempt_id':'A015-stage6-one-control-excess-gates-and-leafless-full-transfer',
          'method':'Scoped source reconstruction; analytic all-incidence one-control coefficient bound; exact actual-Boolean leafless all-dimensional fixed-reference falsifier',
          'mathematical_delta':'One-control Psi <=[log(1/beta)/2+3log(e)/5+1/20]M, M<=I-Var. On SAME uniform K_m,m edge reference, complete nonempty-data Psi/I >=15log(m)/64-217/160; old root/factorial and signed normalization retained. No universal FEI conclusion.',
          'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_TRANSFER_BOUND_PROVED_FIXED_REFERENCE_FULL_CORRECTION_UNBOUNDED_FEI_OPEN_REVIEW_PENDING',
          'claim_versions_used':[d['claim_id']+'@1','A007-DISTRIBUTED-CORE-COMPONENT-LIFT@1'],
          'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'New narrow transfer theorem and complete leafless fixed-reference obstruction'}],
          'source_artifacts':[str(R/x) for x in ['REPORT.md','ONE_CONTROL.md','LEAFLESS_SCALE.md','REVIEW_A007.md','out/EXACT_CHECK.json','out/LEAFLESS_EXACT.json','out/LEAN_RESULT.json']],
          'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
          'blockers':['Independent review and supervisor mirror/adoption unobserved','Universal once-fixed reference/inherited complete cost payment remains open','Core Lean helper returned RUNTIME_UNVERIFIED, no kernel certification'],
          'packet_ids':['A015']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
spec=read(R/'FROZEN_SPEC.json');spec2=read(R/'FROZEN_SPEC_LEAFLESS.json')
assert spec['case_count']['base_functions']==189 and spec2['case_count']['physical_functions']==5
outputs=[read(R/'out'/x) for x in ['PILOT.json','EXACT_CHECK.json','LEAFLESS_PILOT.json','LEAFLESS_EXACT.json']]
assert all(x['status']=='PASS' for x in outputs)
assert sum(x['counts']['assertions'] for x in outputs)==75785
assert outputs[1]['counts']['tables']==189 and outputs[3]['counts']['functions']==5
assert all(x['elapsed_seconds']<55 for x in outputs)
protocol=read(PROTOCOL)['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['report_fields'])
assert report.rstrip().split('\n')[-2]=='# Universal bridge' or '# Universal bridge\n\n' in report
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B03/STREAM_NOTES.md',source/'JOINT_OCCUPATION.md',source/'CLAIMS.json',
         A/'runs/20261014T062347Z-account05-A015-minterm-barrier-analysis/REPORT.md']
write(R/'out/SOURCES.json',[{'path':str(x),'sha256':sha(x),'scope':'Read source/protocol; paper baseline inherited and not a new theorem premise'} for x in sources])
(A/'STATUS.md').write_text('STATE: A015 stage6 saved: one-control Psi paid by extra gates M<=I-Var; SAME leafless K_m,m full correction/I >=15log(m)/64-3/2;75785 exact checks PASS; FEI OPEN, review pending.\nNEXT: Jointly pay empty-control scale and inherited complete core/reference cost on SAME K_m,m obstruction, retaining all sectors and one fixed reference; A007/A008/A086/A094 review.\n',encoding='utf-8')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
entry=f'\n{now} Stage6: resumed last substantive stage5; later scheduled folders only markers. One-control extra-gate transfer and complete leafless K_m,m fixed-reference correction obstruction saved;75785 final successful exact assertions (pilot overlap included). Core Lean timed out/runtime unverified, not certified. Full FEI OPEN. NEXT: {next_action}\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
lesson='\nStage6 (2026-10-21): For one fresh control, SAME original eta gives Psi <=[log2(1/beta)/2+3log2(e)/5+1/20]M, M=sum P E(k-1)<=I-Var. This pays arbitrary incidence without an ownership tail. K_m,m exact edge primes at lambda=1/m,beta=1/m have M/I->1; within-side L0=m^-s,J1=s!m^-s2^(4(s-1)/5). Complete source-defined Psi/I >=15log2(m)/64-217/160 for m>=4, all nonempty-data sectors and normalization retained. Empty-control data scale remains after root/factorial refunds. This is fixed-transfer/surrogate failure only, not infimum-code growth or FEI. Controller-only overhead and inherited base R_g stay separate. Core Lean helper returned RUNTIME_UNVERIFIED; no formal certification.\n'
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(lesson)
files=[x for x in R.rglob('*') if x.is_file() and x.name!='RECEIPTS.json']
assert all(x.stat().st_size<20*1024*1024 for x in files)
write(R/'out/RECEIPTS.json',{'saved_at':now,'status':'LOCAL_SCHEMA_HASH_AND_OUTPUT_CHECKS_PASS',
                           'mathematical_review':'Pending independent review; not established by this file checker',
                           'mirror':'UNOBSERVED','files':[{'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in files]})
print(json.dumps({'status':'PASS','files':len(files),'assertions':75785,'claim':claim['claim_id'],'full_FEI':'OPEN'}))
