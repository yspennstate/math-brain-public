import datetime,hashlib,json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
LEAD=TEAM/'claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring'
SOURCE=TEAM/'agents/A051/runs/20261011T233123Z-fleet05-A051-near-extremizer-definition'
OLD=AGENT/'runs/20261011T220243Z-fleet05-A052-critical-source-structure'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
full=read(ROOT/'out/FULL_SUMMARY.json');pilot=read(ROOT/'out/PILOT_SUMMARY.json');replay=read(ROOT/'out/CHANNEL_REPRODUCTION.json')
assert all(x['status']=='PASS' for x in (full,pilot,replay))
assert full['completed']==1157 and full['assertions']==68806 and replay['assertions']==1881
assert sum(g['U_certificate_pass'] for g in full['groups'])==265
assert sum(g['U_certificate_fail'] for g in full['groups'])==885
assert sum(g['failure_despite_verified_actual_descent'] for g in full['groups'])==479
assert sum(not r['certificate_exists'] for r in full['cases'] if not r['name'].startswith('NAND_case'))==7
assert sum(r['source_minimizer_physically_rechecked']['R_I_A_minus_L_A_sign']>0 for r in full['cases'] if not r['name'].startswith('NAND_case'))==4
byname={r['name']:r for r in full['cases']};reproduced={r['name']:r for r in replay['cases']}
w=byname['NAND_case_0006'];assert F(w['R_bits'][0])>F(12,5) and F(w['R_bits'][1])<F(241,100)
assert F(w['U_min_over_I_bits'][0])>F(357,100)
q=reproduced['NAND_case_0006'];assert q['rows'][0]['mask']==48
assert F(q['rows'][0]['L_A_over_I_A_bits'][1])<F(23,10)
assert F(w['source_minimizer_physically_rechecked']['actual_gap_per_influence_bits'][0])>F(11,100)
dump(ROOT/'out/WITNESS_SUMMARY.json',{'status':'EXACT_CERTIFICATES_PASS','primary_witness':
 {'name':'NAND_case_0006','tree':q['tree'],'n':6,'R_interval':w['R_bits'],'all_block_U_min_interval':w['U_min_over_I_bits'],
  'actual_block_mask':48,'actual_L_over_I_interval':q['rows'][0]['L_A_over_I_A_bits'],
  'certified_simple_bounds':{'R_lower':'12/5','R_upper':'241/100','U_min_lower':'357/100','actual_block_L_over_I_upper':'23/10','actual_strict_descent_margin_lower':'11/100'}},
 'seed_results':[{'name':r['name'],'U_certificate_exists':r['certificate_exists'],'actual_named_block_strictly_descends':r['source_minimizer_physically_rechecked']['R_I_A_minus_L_A_sign']>0} for r in full['cases'] if not r['name'].startswith('NAND_case')]})

paths=[(PROTOCOL,'Schema, revision 2026-10-11-execution-v2'),(TEAM/'BOARD.md','Stage-start board snapshot 2026-10-12 00:39 UTC; source byte pin at persistence'),
       (TEAM/'claude/B11/STREAM_NOTES.md','v2 agent A052 target and current mechanism'),
       (LEAD/'REPORT.md','R1/R2/R5/R6 derivations and scope'),(LEAD/'CLAIMS.json','Exact lead versions and hashes'),
       (SOURCE/'REPORT.md','Composition census scope, squeeze and next controls'),
       (SOURCE/'UNIVERSAL_DESCENT_SQUEEZE.md','Independent analytic review'),
       (SOURCE/'COMPOSITION_CERTIFICATES.md','Saved-family definition and finite scope'),
       (SOURCE/'CLAIMS.json','A051 exact claim versions'),
       (SOURCE/'code/descent_compositions.py','Read-only tree/physical-block definitions; not imported or executed'),
       (SOURCE/'code/check_seeded_and_replay.py','Read-only named seed clauses; not imported or executed'),
       (SOURCE/'out/full_SUMMARY.json','Frozen 1150-case formula list, root hashes/vectors and named block masks'),
       (SOURCE/'out/SEEDED_FULL_SUMMARY.json','Frozen seven seed definitions/hashes/vectors and named blocks'),
       (SOURCE/'out/AGGREGATE_CERTIFICATES.json','Selected extrema 279,287,946,962'),
       (OLD/'REPORT.md','Self-contained uniform logarithmic Sobolev proof'),
       (OLD/'CRITICAL_SOURCE_STRUCTURE.tex','Prior affine-pivot statement, sharpened by conditional majority')]
dump(ROOT/'out/SOURCE_MANIFEST.json',{'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'locator':loc} for p,loc in paths],
 'no_external_proof_premise':True,'source_definition_imports_executed':False})

lead_claims={x['claim_id']:x for x in read(LEAD/'CLAIMS.json')}
source_claims={x['claim_id']:x for x in read(SOURCE/'CLAIMS.json')}
used=[]
for id in ('CLAUDE-B11-R1','CLAUDE-B11-R2'):
    x=lead_claims[id];used.append({'claim_id':id,'version':x['version'],'statement_sha256':x['statement_sha256'],
      'status':'LOCALLY_INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE','review_source':str(ROOT/'DEPENDENCY_REVIEW.md')})
x=source_claims['A051-PROPER-BLOCK-DESCENT-SQUEEZE']
used.append({'claim_id':x['claim_id'],'version':x['version'],'statement_sha256':x['statement_sha256'],
             'status':'LOCALLY_INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE; CALIBRATION_ONLY','review_source':str(ROOT/'DEPENDENCY_REVIEW.md')})
statement='For every binary law on n>=2 coordinates with d_i=P(S_i=1) and sum d_i>0, define B_A=H(S_A|S_Ac), beta_A=sum_(i in A) E min(P(S_i=1|S_Ac),P(S_i=0|S_Ac)), kappa=2/ln2 and U_A=B_A+kappa beta_A. Then B_A>=sum_A B_i, beta_A>=sum_A beta_i and min_(nonempty proper A,I_A>0)U_A/I_A=min_(i:d_i>0)U_i/d_i. The analogous equality holds for Ucap_A=B_A+min(|A|,kappa beta_A), with singleton cost B_i+min(1,kappa beta_i). For Boolean uniform-cube physical restrictions L_A=B_A+J_A<=U_A; the optimized recentering certificate therefore cannot gain from block size. On the exact frozen list of 1150 saved NAND shapes at n=6..9, 265 pass U_A<=R(f)I_A and 885 fail every proper block; 479 of the failures have a directly verified proper block with L_A<R(f)I_A. All seven frozen seed/hybrid controls fail the U certificate, four despite direct strict actual descent. For F_m=product_j (-1)^(x_j y_j), m>=2, R=2, U_A/I_A=2+kappa and Ucap_A/I_A=4 for every proper block, whereas L_A=2 times the number of touched pairs and querying one full pair attains L_A/I_A=2. All physical children have ratio<=2. Products of a two-bit quadratic factor with a three-bit point defect, and their disjoint tensor powers, similarly fail every U certificate at the source ratio while admitting strict actual full-factor descent. No larger-fixed-K or high-threshold minimal-critical impossibility, FEI bound or unbounded Boolean H/I family is claimed.'
hyp=['Entropy in bits; all zero-mass fibers contribute zero; n>=2 and sum d_i>0 for normalized minima',
     'Physical-channel and tensor assertions use actual Boolean signs on finite uniform cubes; no non-Boolean spectral realizability is assumed',
     'Finite decisions refer only to the frozen source-hashed family in out/FROZEN_FULL.json and explicit seed clauses',
     'Criticality interpretation uses the exact physical-child deficit comparison, not component deletion or inherited criticality']
claim={'claim_id':'A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'contributors':['fleet05/A052'],'proof_source':{'path':str(ROOT/'SINGLETON_COLLAPSE.md'),'sha256':sha(ROOT/'SINGLETON_COLLAPSE.md'),
              'locator':'Distributional collapse proof, information-cap extension and exact tensor obstruction; finite certificates in out/cases and FULL_SUMMARY.json'},
       'proof_dependencies':[used[0]],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':['Universal own-ratio recentring-certificate admission: every nonconstant Boolean f admits proper A with U_A<=R(f)I_A',
                                'The same admission after clipping the channel price by |A|'],
       'first_unproved_line':None,'next_consumers':['claude/B11','A051','A053','A054','A055','A018','A019','A090','A094','B20']}
dump(ROOT/'CLAIMS.json',[claim])
reviews=[{'claim_id':id,'version':1,'verdict':'ACCEPT_AT_STATED_SCOPE','review_source':'DEPENDENCY_REVIEW.md'} for id in ('CLAUDE-B11-R1','CLAUDE-B11-R2','CLAUDE-B11-R5','A051-PROPER-BLOCK-DESCENT-SQUEEZE')]
reviews.append({'claim_id':'CLAUDE-B11-R6','version':1,'verdict':'ACCEPT_FULL_FACTOR_CLAUSE_ONLY; ONE_BIT_PHI_UNDEFINED_CAVEAT','review_source':'DEPENDENCY_REVIEW.md'})
dump(ROOT/'out/REVIEW_RECORDS.json',reviews)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT',
 'attempt_id':'A052-optimal-recentring-collapse-2','method':'Conditional chain rule and Jensen; optimized channel recentring; integer Walsh/rational-log census; direct physical-child reproduction',
 'mathematical_delta':'Proved optimal recentring and elementary information-cap block minima collapse to singletons. Certified 265/1150 passes, 885 failures, 479 false negatives with actual strict-descent blocks; all seven seed controls fail. Proved all-dimensional exact and strict tensor route obstructions; locally reconstructed lead analytic interfaces and A051 squeeze.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'BLOCK_UPPER_CERTIFICATE_MECHANISM_RESOLVED; SCOPED_THEOREM_PROVED_UNREVIEWED; UNIVERSAL_JOINT_PAYMENT_AND_FULL_FEI_OPEN',
 'claim_versions_used':used,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'NEW_SINGLE_BUNDLED_STRUCTURAL_THEOREM_AND_EXACT_SCOPE_REJECTION'}]+reviews,
 'source_artifacts':['SINGLETON_COLLAPSE.md','CRITICAL_SOURCE_STRUCTURE.tex','DEPENDENCY_REVIEW.md','code/recentred_census.py','code/reproduce_channel.py','out/FROZEN_PILOT.json','out/FROZEN_FULL.json','out/FROZEN_REPRODUCTION.json','out/PILOT_FAILURE.json','out/PILOT_SUMMARY.json','out/FULL_SUMMARY.json','out/CHANNEL_REPRODUCTION.json','out/WITNESS_SUMMARY.json','out/SOURCE_MANIFEST.json','out/cases/'],
 'next_consumers':['claude/B11','A051','A053','A054','A055','A018','A019','A090','A094','B20'],
 'next_action':'Change to a non-superadditive joint-channel estimate exploiting isospectral/full-factor cancellations; begin at NAND case 0006 block mask 48 and consume source-complete near-tensor/channel identities while retaining child and terminal deficits.',
 'stagnant_substantive_attempts':0,'blockers':['Universal fixed-K actual joint decrement/stopping-tree payment remains unproved; additive beta_A mechanism is settled and must not be retried by increasing block size'],
 'packet_ids':['A052']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
protocol=read(PROTOCOL)['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: Stage 2 complete locally: optimal recentering block certificate collapses to singletons; 265/1150 pass, 885 fail, 479 exact false negatives; 70,687 full/replay checks PASS; full FEI OPEN.\nNEXT: Replace additive beta_A pricing by a joint-channel cancellation bound on NAND case 0006 mask 48; consume A053/A018/A019 identities; A090/A094 review pending.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' — Stage 20261012T003906Z: read updated BOARD/B11 lead and A051 composition/squeeze. Independently reconstructed lead R1/R2/R5 and A051 squeeze. Proved distributional singleton collapse for optimal beta_A and information-capped bound. Initial pilot seed-label count failure preserved and repaired; complete pilot 924 assertions PASS. Full frozen 1157-case census 68,806 assertions PASS in 36.049s: NAND counts 265 pass/885 fail, 479 failures with strict actual physical-block descent. Direct 5-case replay 1,881 assertions PASS. Analytic tensor obstructions retain criticality scope and bounded H/I. Mechanism changed to exact joint-channel cancellation, not a larger block search. Saved all artifacts locally; no shared/external writes.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 2: optimal beta recentring loses block cancellation

- For any binary law B_A>=sum_A B_i and beta_A>=sum_A beta_i by chain rule and conditional Jensen. Therefore min proper U_A/I_A=min relevant U_i/I_i for U_A=B_A+(2/ln2)beta_A. The clipped Ucap_A=B_A+min(|A|,(2/ln2)beta_A) also has a singleton minimum. Larger blocks cannot repair either surrogate.
- On the saved 1150 n=6..9 NAND formula list: 265 pass U_A<=R I_A, 885 fail every block; 479 failures still admit a directly checked strict actual-decrement block. All seven named seed/hybrid controls fail, four despite actual strict descent. These are exact finite certificates, not a universal theorem.
- Quadratic tensors F_m=product (-1)^(x_j y_j) have R=2 and every U_A/I_A=2+2/ln2, capped ratio 4; actual L_A=2 touched_pairs and J_A=number of singly touched pairs. A complete factor costs J_A=0. These sources are non-strict physical-ratio-critical, but not dimension-minimal/indecomposable/high-ratio witnesses. No FEI counterexample follows.
- The strict tensor of a two-bit quadratic factor with a three-bit point defect has 2<R<3, every surrogate singleton ratio>4, but full-factor actual descent ratio 2. Tensor powers preserve this scoped failure and their bounded root ratio.
- Six-bit NAND case 0006: exact 12/5<R<241/100, every U_A/I_A>357/100, while block mask 48 has L_A/I_A<23/10 and actual strict margin>11/100. This is the frozen next joint-channel benchmark.
- A051's universal co-singleton bound phi<=nR/(n-1) makes phi/R<=1.33 automatic at n>=4. It is calibration, not new payment. New work must retain actual J_A and child/terminal deficits rather than increase the same additive upper-bound block search.
''')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in p.parts]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(ROOT/'out/RECEIPTS.json',{'generated_at':now,'local_only':True,'remote_mirror_verified':False,
 'protocol_schema_checks':'PASS','all_output_status_checks':'PASS','per_case_certificates':len(list((ROOT/'out/cases').glob('*.json'))),
 'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],
 'rolling_files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in (AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md')]})
print(json.dumps({'status':'PASS','claim_fields':'EXACT','progress_fields':'EXACT','receipt_files':len(files),'case_certificates':len(list((ROOT/'out/cases').glob('*.json'))),'max_file_bytes':max(p.stat().st_size for p in files),'local_only':True}))
