from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s,h):return hashlib.sha256(json.dumps({'exact_statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
check=json.loads(read(R/'out/CHECK.json'));assert check['status']=='PASS' and check['assertions']==4780
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json');pr=json.loads(read(protocol))
src=B/'agents/A016/runs/20261021T183838Z-fleet03-A016-addressing-benchmark'
source_claim=json.loads(read(src/'CLAIMS.json'))[0]
assert source_claim['claim_id']=='A016-NONFLAT-ACTIVATION-SAME-BANK' and source_claim['version']==1
assert source_claim['statement_sha256']=='831e172392c1fc7b4d64c0cd90d833762b3ac0c0874a88f9a602ee13705f0fc0'
endpoint={
 'seed_slope_log_bound':3**3<2**5,
 'eta_small_bound':Q(3,1024)<Q(1,128),
 'log_correction_bound':Q(1,4096)<Q(1,128),
 'profile_remainder':Q(63,64)-Q(1,128)-Q(1,64)==Q(123,128),
 'm256_gap':Q(5,16)*Q(256,32)+Q(123,128)==Q(443,128),
 'bank_failure_endpoint':Q(7,2)-Q(443,128)-1==Q(-123,128),
 'all_k_profile_endpoint':(Q(2*5)+Q(9,2))/32==Q(29,64),
 'all_k_decrease_polynomial_coefficients':['2','5/2'],
 'source': 'For f(k)=(2k+9/2)2^-k, 2^(k+1)(f(k)-f(k+1))=2k+5/2>0 for all k>=5.'}
assert all(v for k,v in endpoint.items() if isinstance(v,bool));put(R/'out/RATIONAL_ENDPOINTS.json',endpoint)
s=('For g the three-bit sign negative only at000, G_m its disjoint m-fold product and '
 'A=point_k*(1-G_m)/2, k>=5,m>=1, put rho=2^-k,p=rho*(1-(3/4)^m)/2, '
 'h=chi_u(1-A)+chi_q A, F=1 at gate0 and hs at gate1 for the independent two-bit point-defect mask. '
 'Supply Q_h=(P_h+point_q)/2 and Q_F(e,T)=[Q_h(T_core)P_s(T_mask)+point_empty(T)]/4 '
 'at both gate frequencies. Let c=CE(P_hq,(P_hq+point_empty)/2), J_A the indicator flip influence. '
 'Then c-J_A>(5/16)*rho*m+123/128. All core/root/immediate fresh or inherited activation-child '
 'references remain rate4 eligible. Under q then complete adaptive activation-bit exposure with '
 'only marginal reference inheritance, the SAME original half-core bank S=2*(1-p+J_A/2)-c/2, '
 'after its exact first insertion, conversion and weighted positive final terminal deficit, '
 'has remainder<-123/128 whenever rho*m>=8. In particular k=5,m>=256 fails; '
 'the diagonal m=4^k has Inf_q(F)=p/2<2^-k/4 tending to0 and c-J_A tending to infinity. '
 'No universal fixed additive admission c<=J_A+M is possible for these references. This refutes '
 'that admission and specified allocation only, not A016 conditional theorem or full FEI.')
h=['Independent finite uniform physical Boolean cubes; all logarithms base2.',
 'The specified seed, event, references, exact booked first debit and source bank are retained.',
 'Only q then activation coordinates are exposed, and complete continuation retains both full terminal signs.',
 'k>=5,m>=1 are arbitrary integers; symbolic tensor counts do not replace Boolean realizability.',
 'No claim is made that the full signed original physical reserve is insufficient.']
c={'claim_id':'A020-UNBOUNDED-NONFLAT-ADMISSION-NOGO','version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':digest(s,h),'contributors':['A020'],
 'proof_source':['REPORT.md complete derivation1--6','code/check.py','out/CHECK.json','out/RATIONAL_ENDPOINTS.json'],
 'proof_dependencies':[{'claim':'A016-NONFLAT-ACTIVATION-SAME-BANK@1','scope':'Sections1--4 conditional ledger; independently reconstructed without admission reset','original_statement_sha256':source_claim['statement_sha256']}, {'source':'A020 stage6 supplied reference','scope':'Starting family/reference conventions only; new tensor coefficients derived here'}],
 'review_records':[{'reviewer':'A020','kind':'author analytic proof and exact verification','result':'7 symbolic cases +2 literal Boolean families;4780 exact assertions PASS; all-k diagonal proved analytically'}, {'reviewer':'Lean','kind':'not a certificate','result':'memok exit1; no compiler launched; scalar source UNCOMPILED'}],
 'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['The proposed universal extension c<=J_A+M for any finite dimension-independent M at the specified references','Universal sufficiency of the specified original half-core allocation even when all supplied immediate references are rate4 eligible'],
 'first_unproved_line':'Construct/pay a different conserved global signed physical source after one tensor-bit exposure; full FEI remains open.',
 'next_consumers':['A016','A018','A019','A090','A091','A094','B04','B20']}
review_s=('A016-NONFLAT-ACTIVATION-SAME-BANK@1 REPORT sections1--4 have a correct general '
 'endpoint and original-bank identity R=C_end-c-1-2p+J_A-E-D, at the stated references and '
 'complete adaptive continuation; the stated admission c<=J_A+2 suffices for R>5/128. '
 'This partial review does not accept the whole three-bit/all-history theorem or assert universal admission.')
review_h=['Original A016 claim statement/hash retained, without repair.','Only REPORT sections1--4 endpoint/conditional-bank interface reviewed; not section5 finite-width admission or partial-history margin.']
rev={'claim_id':'A020-REVIEW-A016-CONDITIONAL-ADMISSION-LEDGER','version':1,'exact_statement':review_s,'hypotheses':review_h,'statement_sha256':digest(review_s,review_h),'contributors':['A020'],
 'proof_source':['REPORT.md derivation1','code/check.py truth reconstruction and full-reference scalar ledger'],
 'proof_dependencies':[{'claim':'A016-NONFLAT-ACTIVATION-SAME-BANK@1','original_statement_sha256':source_claim['statement_sha256'],'source_path':str(src/'REPORT.md')}],
 'review_records':[{'reviewer':'A020','result':'PARTIAL_HOLDS','scope':'Exact endpoint/conditional-bank only; no repair or whole-report acceptance','at_utc':now}],
 'status':'PARTIAL_INDEPENDENT_RECONSTRUCTION_HOLDS','supersedes':[],'refutes':[],
 'first_unproved_line':'Source finite-width partial-history theorem outside review scope; arbitrary-width unconditional admission is false.',
 'next_consumers':c['next_consumers']}
for x in [c,rev]:assert set(x)==set(pr['required_per_run']['claim_fields'])
put(R/'CLAIMS.json',[c,rev])
progress={'protocol_revision':pr['revision'],'run_id':R.name,'stream':'B04','packet_id':'A020',
 'gap_id':'G-LOWSEL-COLLISION-SAME-REFERENCE-HISTORY-BANK',
 'attempt_id':'A020-stage7-unbounded-admission-tensor-falsifier',
 'method':'Consume A016 conditional admission; exact Boolean tensor spectrum, full normalized references and conserved no-reset ledger; analytic all-k diagonal.',
 'mathematical_delta':'No universal bounded-offset admission c<=J_A+M. Actual rare Boolean family keeps all immediate references rate4 eligible but SAME original half-bank remainder<-123/128 when2^-k*m>=8; selector influence tends0 along m=4^k.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_NOGO_PROVED_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim':'A016-NONFLAT-ACTIVATION-SAME-BANK','version':1,'scope':'conditional sections1--4','statement_sha256':source_claim['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':1} for x in [c,rev]],
 'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/FIRST_FAILURE.json','out/RATIONAL_ENDPOINTS.json','out/LEAN_ADMISSION.json'],
 'next_consumers':c['next_consumers'],
 'next_action':'Expose one actual tensor-block bit with SAME root Q and booked J_first, padding unqueried; transport the FULL unused signed physical reserve rather than refuted half-core admission. A016/A019 review no-go; A090/A091/A094 audit ownership.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI open. Whole signed bank replacement unpaid. Independent review and supervisor/mirror adoption pending. Lean compiler admission held; no formal certificate.'],
 'packet_ids':['A020']}
assert set(progress)=={x.split(' (')[0] for x in pr['required_per_run']['progress_fields']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
sources=[protocol,B/'BOARD.md',B/'claude/B04/STREAM_NOTES.md',src/'REPORT.md',src/'CLAIMS.json',A/'runs/20261021T162111Z-fleet03-A020-selector-boundary-tests/REPORT.md',B/'agents/A018/runs/20261022T202507Z-fleet03-A018-shared-data-collision-law/REPORT.md',B/'agents/A019/runs/20261022T221313Z-fleet03-A019-orthogonality-extensions/REPORT.md']
put(R/'out/SOURCE_RECEIPTS.json',{'as_of':now,'note':'Current byte receipts of inspected sources. Static baseline carried from prior stages; no independent review inferred from hashes.','files':[{'path':str(p),'sha256':sha(p)} for p in sources]})
(A/'STATUS.md').write_text('STATE: A020 stage7 saved: universal c<=J_A+O(1) admission FALSE; actual eligible-reference tensor family exhausts SAME half-bank, remainder<-123/128; vanishing-selector diagonal;4780 exact assertions PASS; FEI OPEN, review pending.\nNEXT: One actual tensor-bit query with SAME Q/booked first debit and unqueried padding; transport FULL unused signed physical reserve; A016/A019 review no-go, A090/A091/A094 audit complete terminals.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' — Stage7: consumed A016 three-bit nonflat theorem and independently reconstructed its conditional endpoint/bank. Exact g3 tensor event gives c-J_A>(5/16)2^-k*m+123/128; refs still rate4 eligible; SAME half-bank remainder<-123/128 if2^-k*m>=8. All-k diagonal m=4^k has vanishing selector influence and divergent gap; full FEI not refuted. Corrected typo H0>5/2 to exact H0>17/8, archived failure, unchanged frozen domain. Full7 scalar+2 truth cases/4780 assertions PASS1.0876516s. memok held Lean at2.7GB free; source uncompiled. Four protocol files and rolling handoff locally saved; new independent review/mirror pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
## Stage7 unbounded-width admission barrier

- A016 already proved our old fixed-width nonflat NEXT. Its exact original-bank identity is R=C_end-(c-J_A)-1-2p-E-D, with original first debit and complete terminals. Its conditional c<=J_A+2 theorem remains valid; the condition is not universal.
- Actual seed g3 negative only at000 has H0=4-(9/8)log2(3)>17/8 and I0=3/4, so H0/2-I0>5/16. With G_m=g3 tensor m, B=(1-G_m)/2 and A=point_k B, k>=5, exact c-J_A>(5/16)2^-k*m+123/128. All supplied core/root/immediate fresh and inherited activation-child references remain rate4 eligible. The SAME original half-bank has remainder<-123/128 when2^-k*m>=8 (k5,m>=256). No larger fixed additive allowance repairs admission.
- The diagonal m=4^k keeps p/2<2^-k/4 tending0 while the admission gap diverges. The spectral histogram is binomial(m,b)7^b atoms of mass9^(m-b)/16^m, so verification need not allocate2^(3m) coefficients. General tensorization shows any universal bounded-offset admission would force false FEI constant2. This is a route obstruction, not a FEI counterexample or proof that the FULL original signed reserve cannot pay.
- Next change mechanism: expose one actual bit of a tensor block with padding still live, SAME Q and exact J_first. Carry full signed physical surplus rather than the exhausted half-core allocation. Retain both full terminals and any positive deficit. Finite certificate4780 exact assertions; all-k proof analytic; independent review pending. Lean admission held; no compiler certificate.
''')
report=read(R/'REPORT.md')
for label in pr['required_per_run']['report_fields']:assert ('## '+label) in report
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for p in R.rglob('*'):
 if p.is_file():
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json':json.loads(read(p))
put(R/'out/PERSISTENCE_RECEIPTS.json',{'as_of':now,'local_only':True,'schemas':'PASS','claim_statement_sha256':c['statement_sha256'],'source_claim_unchanged':source_claim['statement_sha256'],'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'],'rolling':[{'path':p.name,'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]})
receipt=json.loads(read(R/'out/PERSISTENCE_RECEIPTS.json'))
assert all(sha(R/v['path'])==v['sha256'] for v in receipt['files'])
print(json.dumps({'status':'SAVED_AND_READBACK_PASS','assertions':check['assertions'],'cases':len(check['scalar'])+len(check['truth']),'source_review':'PARTIAL_HOLDS','new_claim':'PENDING_INDEPENDENT_REVIEW','full_FEI':'OPEN'}))
