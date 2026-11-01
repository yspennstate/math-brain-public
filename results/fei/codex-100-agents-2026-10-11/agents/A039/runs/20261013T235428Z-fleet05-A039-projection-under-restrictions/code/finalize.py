from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]
ROOT=HOME.parents[1]; run_id=RUN.name
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value):(RUN/name).write_text(json.dumps(value,indent=2,ensure_ascii=False),encoding='utf-8')
statement=('For every m>=1, every complete adaptive physical coordinate tree on f_m=1-2*1_zero has the same terminal-inclusive erasure optimum V_m=B_m+V_(m-1)/2, V_1=0, with a_m=2^(1-m), B_m=phi((1-a_m)^2,a_m^2)+(2^(m-1)-1)*2*a_m^2 and phi(x,y)=(x+y)h2(y/(x+y)). With I_m=m*a_m, 2-4/m<=V_m/I_m<=2+log2(e)/m, hence V_m/I_m tends to 2. For the explicitly defined activated quadratic point-flip selector B05 roots k=2,r=4 and k=4,r=8, the terminal-inclusive Bellman minima have V/I in [1.836014211380,1.836014211381] and [1.956704604624,1.956704604625], respectively; the root control orbit is uniquely optimal and the complete control-first policy attains the exact minimum. For each r=4,...,8, the actual descendant D(1,1,2,r), whose active core is (-1)^(u*v)-2*1_{u=v=w=0,y=1}, uniquely favors querying u or v; a control query followed by optimal children has the strictly positive exact gap recorded in INDEPENDENT_K4.json. Consequently control-first optimality at these roots does not extend to every descendant. The tree objective retains E_leaf H(f_leaf), and its minimum is over all actual adaptive trees, including stopping trees.')
hypotheses=['Finite uniform physical Boolean cubes; signs +/-1; binary coordinates x correspond to signs (-1)^x; information in bits',
'Physical adaptive coordinate choices depend only on the previous physical history; retain actual terminal spectral entropy; remove only irrelevant coordinates',
'B_i=H(S_i|S_-i)=h2(Inf_i)-I_P(S_i;S_-i); all-m point defect is 1 except -1 at zero',
'B05 uses b=(-1)^(sum disjoint pair products), b_prime=b-2*1_zero, a fresh selector y, and all-zero activation on r fresh controls; finite root and descendant domains exactly as stated',
'Control-first policy queries remaining activation controls, then follows an optimal core tree; no hereditary or all-even-k optimum claim']
claim_id='A039-TERMINAL-OPTIMAL-RESTRICTION-TREE'
dependencies=[{'claim_id':'A039-COHERENT-PROJECTION-TRANSFER','version':1,'use':'existing physical entropy decrement interface; needed decrement re-derived in TREE_TARGET','status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW'},
{'claim_id':'A037-PHYSICAL-SPECTRAL-COMMON-LIFT','version':1,'use':'optional root-spectral posterior interpretation only','status':'INDEPENDENTLY_REVIEWED_LOCALLY_BY_A039_IN_FIRST_STAGE'}]
claim={'claim_id':claim_id,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
'contributors':['A039'],'proof_source':{'run_id':run_id,'files':['TREE_TARGET.md','OPTIMUM_PROOF.md','REPORT.md','code/optimal_tree.py','code/verify_tree.py','code/check_and.py','out/OPTIMALITY_CERTIFICATE_K2.json','out/OPTIMALITY_CERTIFICATE_K4.json','out/INDEPENDENT_K2.json','out/INDEPENDENT_K4.json','out/AND_CERTIFICATE.json']},
'proof_dependencies':dependencies,'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
'refutes':['Hereditary control-first Bellman optimality at every physical descendant of the two certified B05 roots'],
'first_unproved_line':None,'next_consumers':['A037','A038','A040','A064','A088','A091','A094','B20']}
save('CLAIMS.json',[claim])
next_action='Compare signed common-kernel Bayes product/occupancy reset with owned selector-reserve release at a controller query of the three-state priority gate after nonconstant data exposure; retain both child cores and terminal entropy.'
progress={'protocol_revision':protocol['revision'],'run_id':run_id,'stream':'B08','packet_id':'A039','gap_id':'G-R-MISMATCH',
'attempt_id':'A039-optimal-tree-resume-1','method':'Resume productive partial packet; exhaustive symmetry-complete Bellman certificate; independent full-truth recursion; all-dimensional AND recurrence proof',
'mathematical_delta':{'all_m_AND_optimum':'Every complete tree has the same V; 2-4/m<=V/I<=2+log2(e)/m; limit 2',
'B05_finite_optimum':{'roots':[[2,4],[4,8]],'k4_V_over_I':['1.956704604624','1.956704604625'],'k4_I':'141/4096','root_optimal_orbit':'control','control_first_gap':'exactly zero'},
'descendant_obstruction':'D(1,1,2,r), r=4,...,8, strictly favors pair over control; all coordinate alternatives checked',
'universal_constant_improvement':None,'first_unsupported_universal_line':'V(f)<=K I(f) for every Boolean f, or a paid prescribed-reference reset/terminal cost on the same overlapping tree'},
'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'SCOPED_OPTIMA_AND_ORDER_OBSTRUCTION_CLOSED_AUTHOR_PROOF; UNIVERSAL_FEI_OPEN; EXTERNAL_REVIEW_PENDING',
'claim_versions_used':dependencies,'claims_created_or_changed':[{'claim_id':claim_id,'version':1,'change':'Scoped completion of lead assignment, no new broad universal candidate'}],
'source_artifacts':['TREE_TARGET.md','OPTIMUM_PROOF.md','out/FROZEN_SPEC.json','out/SECOND_CHECK_SPEC.json','out/RESUME_RECEIPTS.json','out/OPTIMUM_K2.json','out/OPTIMUM_K4.json','out/INDEPENDENT_K2.json','out/INDEPENDENT_K4.json','out/AND_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':['A038','A064','A088','A091','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
'blockers':['Universal signed reset and arbitrary terminal-reference payment are mathematical gaps, not local save/access blockers','External independent review, registry/mirror adoption and downstream use unobserved'],
'packet_ids':['A039']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
sources=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B08/STREAM_NOTES.md',
ROOT/'agents/A038/runs/20261013T223535Z-fleet05-A038-occupancy-term-audit/REPORT.md',
ROOT/'agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer/REPORT.md',
HOME/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/CLAIMS.json',
HOME/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/code/baseline_check.py',
Path('~/mop_fei100/reports/fei-2026-10-11/CLAIM_REGISTRY.json'),
Path('~/mop_fei100/reports/fei-2026-10-11/PACKET_STATUS.json')]
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size,'scope':'Actual read/source use; BOARD at stage start, new peer reports context only; no new external paper premise'} for p in sources])
now=datetime.now(timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: A039 stage 3 saved: all-m AND optimal tree ratio tends to 2; exact B05 k=2,4 optima; five data-exposed descendants refute hereditary control-first; alternate implementation PASS; external review pending; FEI OPEN.\nNEXT: Compare one signed Bayes product/occupancy reset with A038 owned reserve release on a three-state priority gate after nonconstant data exposure, retaining child cores/terminal entropy; A088/A094 review.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {run_id}: resumed productive interrupted 20261012 packet without rewriting it. Adopted k2 pilot; frozen k4 compressed DP PASS 2480 assertions/162 states/0.76953s. Independent full truth/recursive Walsh checks PASS k2 52 assertions/0.09366s and k4 376 assertions/44.35415s, all 162 canonical values and 1167 actual alternatives. Certified D(1,1,2,r), r4..8, strict control-first failure. Proved all-m AND optimum and ratio limit2; m1..16/direct m<=6 PASS60 assertions/0.06265s. Read A038/A097 new interfaces; no universal reset payment claimed. Four protocol files and rolling state saved; external review and mirror adoption pending.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nAll stopping-tree erasure objectives must include actual terminal entropy: C=sum w B_i+E H_leaf=H_root-sum w JS. Completing leaves can only decrease C, so exact minimum satisfies the complete-tree Bellman equation. For point defect m, all complete trees are optimal, V_m=B_m+V_(m-1)/2 with B_m=phi((1-a)^2,a^2)+(2^(m-1)-1)2a^2, a=2^(1-m). Analytically 2-4/m<=V_m/I_m<=2+log2(e)/m, limit2. For actual B05 k2,r4 and k4,r8 root control-first is exactly optimal, V/I approximately1.836014211380 and1.956704604624. This ordering is not hereditary: D(1,1,2,r), r4..8, uniquely favors the pair query, confirmed by independent actual-coordinate truth-table Bellman reconstruction. Keep data-exposed descendants and terminal costs when comparing A038 owned reserve with coherent Bayes reset. Finite tree optimum and A097 reference kappa do not pay arbitrary prescribed-reference transfer.\n')
claim_keys=set(protocol['required_per_run']['claim_fields'])
progress_keys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==claim_keys
assert set(progress)==progress_keys
assert json.loads((RUN/'PROGRESS.json').read_text())==json.loads((RUN/'PACKET_DELTA.json').read_text())
assert len((HOME/'STATUS.md').read_text().splitlines())==2
report=(RUN/'REPORT.md').read_text()
assert all(('# '+field) in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipts={'saved_at':now,'status':'LOCAL_READBACK_PASS','schema_keys_exact':True,'packet_delta_equals_progress':True,'statement_hash_checked':claim['statement_sha256'],'report_fields_present':True,'universal_bridge_final_paragraph':True,'files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],
'rolling_files':[{'path':str(HOME/name),'bytes':(HOME/name).stat().st_size,'sha256':digest(HOME/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],
'unobserved':['external independent review','supervisor copying','registry adoption','mirror verification','downstream mathematical use','public release']}
save('out/PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'LOCAL_READBACK_PASS','run_id':run_id,'files':len(files),'claim_id':claim_id,'max_file_bytes':max(p.stat().st_size for p in files)}))
