import json,hashlib,datetime
from pathlib import Path
from check_query import spectrum,sq,ent,serial,tree,F

RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parents[1]
def write(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
results=json.loads((RUN/'out'/'CHECK_RESULTS.json').read_text(encoding='utf-8'))
pilot=json.loads((RUN/'out'/'ORDER_PILOT.json').read_text(encoding='utf-8'))
assert results['status']==pilot['status']=='PASS'
assert results['fixed_block_order_cases']==3908 and results['adaptive_trees']==556
code=4951; vals=tuple(-1 if code>>x&1 else 1 for x in range(16))
rootlaw=sq(spectrum(vals,(0,1,2,3)))
assert ent(rootlaw.values())=={2:F(3)}
witness={'truth_code':code,'bit_convention':'x_j is bit j of the row index; physical sign is (-1)^x_j; negative f entries are set bits of truth_code',
 'truth_table':vals,'spectrum':{str(s):str(p) for s,p in rootlaw.items()},'H_bits':3,
 'order_ascending_information':'3/2', 'order_descending_information':'5/2+(9/8)log2(3)-(5/4)log2(5)',
 'positive_difference':'(1/8)log2(5^10/(2^8*3^9))',
 'sign_certificate':{'numerator':5**10,'denominator':2**8*3**9,'strict_integer_inequality':5**10>2**8*3**9},
 'source':'out/ORDER_PILOT.json, code 4951'}
write(RUN/'out'/'ORDER_WITNESS.json',witness)
# AND2 verifies sharpness without logarithm approximations.
B,J,R,_,_=tree((1,1,1,-1),(0,1),(0,1))
assert B==J==R=={2:F(1)}
write(RUN/'out'/'SHARPNESS.json',{'family':'AND2 and its disjoint products','base_truth_table':[1,1,1,-1],
 'base_H':2,'base_cumulative_B':serial(B),'base_cumulative_J':serial(J),'base_refund':serial(R),
 'all_dimension_extension':'For k disjoint AND2 factors queried pair by pair, independent root spectrum and function-specific kernels tensorize; H=2k, I(S;L)=k, root posterior entropy=k.'})

oldpath=Path('~/brain_workers/FEI100_20261011/agents/A037/runs/20261011T220010Z-fleet05-A037-conditional-credit-ledger/CLAIMS.json')
original=json.loads(oldpath.read_text(encoding='utf-8'))
old=next(c for c in original if c['claim_id']=='A037-PHYSICAL-SPECTRAL-COMMON-LIFT')
old['review_records']=old['review_records']+[{'reviewer':'A063','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(RUN/'REVIEW_A037.md'),
 'method':'Direct character-sum Walsh reconstruction and full rational root-label/history probabilities; independent implementation; finite-tree proof rederived; no repair supplied',
 'executed_exact_assertions':results['exact_assertions'],'accepted_scope':'finite uniform-cube physical spectral common lift and retained residual, not generic KL or universal FEI payment'}]
old['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE'
statement=('For every finite uniform-cube Boolean sign and fixed physical block A completely queried by a deterministic adaptive order of canonical singleton kernels, under the common root spectral/physical-history lift let R_A=I(S_A;X_A|S_Ac). Then cumulative physical mixture information is J_A+R_A and cumulative erased-label entropy is B_A-R_A=H(S_A|S_Ac,X_A), where B_A=H(S_A|S_Ac) and J_A=I(X_A;S_Ac) in the actual child-spectrum experiment. Moreover 0<=R_A<=(B_A-J_A)/2. For every finite stopped canonical singleton tree, I(S;L)<=[H(f)-E H(f_L)]/2 and H(S|L)>=[H(f)+E H(f_L)]/2. The half-entropy bound is sharp for disjoint AND2 products. Query-order information is not invariant, as witnessed exactly by four-bit truth code 4951 in the supplied convention.')
hyp=['Boolean signs on finite uniform cube; entropy in bits; zero fibers omitted',
 'Canonical kernel makes deleted parent spectral label and physical branch conditionally independent given residual spectral label at each singleton',
 'Policy decisions and stopping depend only on physical history; no coordinate queried twice; transcript records its full history',
 'Fixed-block refund formula requires all and only coordinates of A queried, with complete assignment recorded; independent policy seeds may instead be conditioned on and averaged']
sthash=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A063-QUERY-COARSENING-REFUND-AND-HALF-ENTROPY-BARRIER','version':1,
 'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sthash,'contributors':['A063'],
 'proof_source':{'run_id':RUN.name,'files':['QUERY_INFORMATION_IDENTITY.tex','PHYSICAL_SPECTRAL_DISTINCTION.md','REPORT.md','out/ORDER_WITNESS.json','out/SHARPNESS.json']},
 'proof_dependencies':[{'claim_id':'A037-PHYSICAL-SPECTRAL-COMMON-LIFT','version':1,'statement_sha256':old['statement_sha256'],'acceptance':'A063 independent reconstruction at stated scope, REVIEW_A037.md'}],
 'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Query-order invariance of canonical full-label revealed information','Canonical complete physical revelation eliminates root spectral posterior entropy'],
 'first_unproved_line':None,'next_consumers':['A028','A064','A087','A094','A097','B20']}
claims=[old,claim]; write(RUN/'CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B13','packet_id':'A063',
 'gap_id':'G-R-MISMATCH','attempt_id':'A063-information-revelation-1','method':'Independent physical-lift review; exact query information/coarsening chain rule; sharp binary-entropy mechanism ceiling',
 'mathematical_delta':'A037 physical lift independently accepted at finite-tree scope; exact coarsening refund and sharp half-entropy posterior barrier proved; exact n=4 order-dependence witness; local kernel/reference distinction explicit; full FEI OPEN',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'ASSIGNED_INTERFACE_RESOLVED_EXTENSION_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':1,'change':'independent scope review'},{'claim_id':claim['claim_id'],'version':1,'change':'new narrow interface and mechanism barrier'}],
 'source_artifacts':['REPORT.md','QUERY_INFORMATION_IDENTITY.tex','PHYSICAL_SPECTRAL_DISTINCTION.md','REVIEW_A037.md','FROZEN_SPEC.json','code/check_query.py','out/CHECK_RESULTS.json','out/ORDER_PILOT.json','out/ORDER_WITNESS.json','out/SHARPNESS.json'],
 'next_consumers':['A064','A028','A039','A087','A094','A097','B20'],
 'next_action':'Compute the conditional refund under control-first versus selector-first singleton lifts on the existing sparse activated bent-defect tree; retain erased/terminal residual and the conserved physical influence budget',
 'stagnant_substantive_attempts':0,'blockers':['No universal influence payment for root posterior/erasure residual; independent review of A063 extension and supervisor adoption pending; B13 lead notes absent at initial read'],
 'packet_ids':['A063']}
write(RUN/'PROGRESS.json',progress); write(RUN/'PACKET_DELTA.json',progress)
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
schema=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
expected=[k.split(' (')[0] for k in schema['progress_fields']]
assert set(expected)==set(progress)
for c in claims: assert set(c)==set(schema['claim_fields'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
receipt=(f"Executed exact validation receipt: {results['exact_assertions']:,} assertions PASS, 3,908 fixed-block/order cases, 556 adaptive trees and 18,888 internal query nodes; runtime {results['runtime_seconds']:.3f} seconds. "
 'The initial job exceeded its frozen 60-second runtime estimate; this scheduling/runtime overrun is recorded as a compute-spec deviation, not concealed. It remained under the 30-minute job limit and did not escalate dimensions automatically. '
 f"The separate explicitly frozen n=4 pilot completed {pilot['completed_cases']} cases in {pilot['runtime_seconds']:.3f} seconds. "
 'No order difference occurred in the complete n<=3 domain. The n=4 code-4951 witness has H=3 bits, ascending information 3/2 and descending information 5/2+(9/8)log2(3)-(5/4)log2(5). '
 'Their positive difference is (1/8)log2(5^10/(2^8*3^9)); the exact sign certificate is 9,765,625>5,038,848. '
 'Its two erasure totals differ by the opposite amount, so the entropy telescope is unchanged. Certificates are in out/ORDER_WITNESS.json and out/SHARPNESS.json.\n\n')
report=report.replace('## proof dependencies and changed downstream conclusions',receipt+'## proof dependencies and changed downstream conclusions')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A063 packet saved: exact coarsening refund, sharp half-entropy revelation barrier, n=4 order witness; A037 lift independently accepted; full FEI OPEN.\nNEXT: A087/A094 review; A064 compute the refund and residual on control-first versus selector-first sparse activated bent-defect trees.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('2026-10-12: Completed 199,195 exact assertions across n<=3; original runtime 355.914 seconds exceeded frozen 60-second estimate under shared load. Separately frozen eight-case n=4 pilot took 0.059 seconds and found code-4951 order dependence, with exact integer sign certificate. Proved sharp R_A<=(B_A-J_A)/2 and retained root posterior >=half initial entropy; AND2 products attain equality. Saved A037 independent review, one narrow extension, report and protocol-exact deltas.\n')
(ROOT/'LEARNED.md').write_text('''# Durable mathematical facts

All entropies are in bits. Physical branches are fair under the actual Boolean child-spectrum experiment; spectral posteriors need not be fair. For block A, B_W=H(S_A|S_Ac) and M_W=I(X_A;S_Ac)=|A|-E H(physical posterior given residual). The decrement is their sum.

A037-PHYSICAL-SPECTRAL-COMMON-LIFT v1 was independently reconstructed by A063. Its canonical kernel depends only on the remaining spectral label and makes deleted spectral bits conditionally independent of the physical outcome. It gives cumulative J=I(root S;full transcript) and retained root posterior=sum erased B+terminal spectrum entropy.

New exact refund: querying fixed A by canonical singleton kernels gives sum p J=J_A+R_A and sum p B=B_A-R_A, R_A=I(S_A;X_A|S_Ac). Direct block lift has R_A=0. Child spectra alone do not specify a unique root-label/history coupling.

Sharp ceiling: h2(t)>=4t(1-t) implies J_h<=B_h in singleton fibers. Hence R_A<=(B_A-J_A)/2. Any stopped canonical singleton transcript reveals at most [H(f)-E H(leaf)]/2; root posterior retains at least [H(f)+E H(leaf)]/2. AND2 products attain equality in arbitrarily large dimension. Information revelation alone cannot pay the residual.

Query order matters at n=4: truth code 4951 (f(x)=-1 iff code's bit at index x is set, x_j bit j) has H=3; order 0,1,2,3 reveals 3/2, reverse reveals 5/2+(9/8)log2(3)-(5/4)log2(5). Positive difference is (1/8)log2(5^10/(2^8*3^9)), certified by 9765625>5038848. No order difference occurred in the exact complete n<=3 census.

Reference posterior divergences include the signed correction E log2(physical prior/reference posterior). They do not automatically equal actual mutual information. Isospectral children have B=J=0 despite one fair physical outcome bit. Near-identical children have B<=h2(m), J<=2m/ln2 with m=half Hellinger defect; the logarithm remains.

Compute lesson: the 3908-case exact rational pilot exceeded its 60-second estimate (355.914 seconds) on the shared machine; record that deviation. The explicitly frozen small n=4 follow-up completed in 0.059 seconds. No floating sign decisions were used.

Full FEI remains open. Next nonlocal target is the erased/root-posterior residual of the existing sparse activated bent-defect tree under control-first and selector-first policies.
'''.replace('\n+','\n'),encoding='utf-8')

base=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
paths=[base/n for n in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
paths += [supp/n for n in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
paths += [supp/'sources'/n for n in ('ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ISOSPECTRAL_SPLICING_CURATED.md')]
paths += list(Path('~/brain_workers/FEI100_20261011/context').glob('*.txt'))
paths += [ROOT.parents[1]/'BOARD.md',oldpath,oldpath.with_name('REPORT.md'),Path('~/brain_workers/FEI100_20261011/agents/A061/runs/20261011T214516Z-fleet05-A061-entropy-process/REPORT.md')]
paths += list((base/'runs').glob('*/*/REPORT.md'))
write(RUN/'out'/'SOURCE_RECEIPTS.json',{'inspection_scope':'Report describes full versus interface-focused reads; hashes are source pins, not claims that unrelated sections were independently audited',
 'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths if p.exists()],
 'missing_lead_notes':'~/brain_workers/FEI100_20261011/claude/B13/STREAM_NOTES.md'})
receipts=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json' and '__pycache__' not in str(p)]
assert all(r['bytes']<20_000_000 for r in receipts)
write(RUN/'out'/'PERSISTENCE_RECEIPTS.json',{'saved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'local_only':True,'files':receipts,'mirror_verified':False,'supervisor_adoption_verified':False,'schema_keys_checked':True})
print(json.dumps({'status':'SAVED_SCHEMA_VALIDATED','new_claim_hash':sthash,'exact_assertions':results['exact_assertions'],'artifacts':len(receipts),'source_receipts':len(paths)},indent=2))
