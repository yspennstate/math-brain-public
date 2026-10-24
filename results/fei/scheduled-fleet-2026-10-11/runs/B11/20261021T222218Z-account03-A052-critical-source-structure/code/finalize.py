from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
B=Path(r'~\brain_workers\FEI100_20261011')
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def put(name,text): (R/name).write_text(text,encoding='utf-8')
def js(name,obj): put(name,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
guard=json.loads((R/'out/PATH_GUARD.json').read_text(encoding='utf-8'))
pilot=json.loads((R/'out/PAIR_PILOT.json').read_text(encoding='utf-8'))
full=json.loads((R/'out/PAIR_FULL.json').read_text(encoding='utf-8'))
coded=json.loads((R/'out/CODED.json').read_text(encoding='utf-8'))
assert guard['status']=='PASS' and guard['checks']==2445
assert not pilot['failures'] and not full['failures'] and coded['exhaustive']
assert pilot['checks']+full['checks']+guard['checks']==84247
dependency={'claim_id':'A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION','version':1,'statement_sha256':'e5b7d55818d52b67c4844061b2553f5c652e703f790476a8f6880ca9afefd1e7','acceptance':'independently reconstructed without repair; see REVIEW_A051.md'}
statement='For every integer m>=3, M=2^m and r=M-2, let C consist of zero and the vertex-edge incidence vectors of the path on r+1 vertices, indexed bijectively by y in F_2^m, and f_m(x,y)=(-1)^(x dot c_y). This actual Boolean function has full affine spectral dimension r+m, minimum influence over its full affine Fourier-label orbit, H=2m, I=2r/M+m/2, and original data coordinates 2,3 satisfy C_2=C_3=0 but C_{23}=2/M>0. Both restrictions at either coordinate retain entropy 2m and have influence I-2/M>0, hence strictly larger H/I. Therefore affine minimality and full affine span, even with Booleanity, do not imply any finite-multiple singleton domination at every physical pair; actual descendant criticality excludes this family.'
claim={'claim_id':'A052-AFFINE-MINIMAL-PATH-COLLISION-OBSTRUCTION','version':1,'exact_statement':statement,'hypotheses':['uniform finite cubes; Boolean signs; entropy bits','m integer >=3','path-incidence construction; coordinates indexed from zero','collision normalization given in PATH_CODE_PROOF.md section3'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A052'],'proof_source':['PATH_CODE_PROOF.md','out/PATH_GUARD.json','code/path_guard.py'],'proof_dependencies':[dependency],'review_records':[{'reviewer':'A052','kind':'author audit plus exact independent-representation checks','verdict':'PASS','scope':'all-m analytic derivation; direct nine-bit and implicit m3..6 checks; not independent-agent acceptance'}],'status':'AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[{'claim_id':'EXPLORATORY-AFFINE-PAIR-SINGLETON-DOMINATION','version':0,'exact_false_statement':'Full affine span and minimum affine-orbit influence imply C_ij<=2(C_i+C_j) for every original physical pair.','scope':'new exploratory statement only; no registered source theorem refuted'}],'first_unproved_line':None,'next_consumers':['A051','A055','A090','A094','B11','B20']}
js('CLAIMS.json',[claim])
put('REVIEW_A051.md','''# Independent reconstruction of A051 affine reduction

Source: A051/runs/20261021T193146Z-account03-A051-near-extremizer-definition/AFFINE_SELECTION.md, claim A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1, statement hash e5b7d55818d52b67c4844061b2553f5c652e703f790476a8f6880ca9afefd1e7. Verdict HOLDS at the stated analytic scope. No repair supplied. This is a local review receipt, not registry adoption.

Reconstruction: Fourier-label translation is character modulation; an invertible linear change of labels comes from the transposed inverse input map. Both preserve Booleanity and squared-weight multiset. At fixed K>0, maximal deficit therefore minimizes influence over this finite orbit. Replacing coordinate row i by any v containing i is invertible, and independent output centering gives min(w(v),1-w(v))>=p_i. Conversely every vector of centered cost <t is supported on coordinates of cost <t. The dimension of their span bounds the number of independent such cheap vectors. At each sorted coordinate cost this gives the sorted-basis cost lower bound, including ties and zero marginals; summation proves global orbit minimality.

For compression, take the affine hull a+V of the actual support, choose original coordinate projections forming a basis of V*, and choose a0 in a+V to center their marginal majority values. Their joint projection is onto, so all chosen majority bits can be set simultaneously even when a0 is not an occupied spectral atom. Modulation by a0 and linear completion produce a genuine d-bit Boolean function preserving squared coefficients and entropy, with influence at most the original sum. Thus any K>=0 violation compresses at the SAME K, and a least-dimensional violation has full affine span. Finite orbit minimization proves the stated universal reduction and cap identity; constants cover d=0, so no empty maximum is used. Padding gives monotonicity of the cap and proves the finite epsilon-nearness claim.

The local near-maximal comparisons lose at most epsilon/K; centering alone loses epsilon/(2K). Applying the row comparison to e_i+e_j gives q_ij<=min(p_i,p_j)/2, or the displayed epsilon/(2K) tolerance. Divisions require K>0 as stated; no marginal is divided by zero. The physical bank remains D+S_A=L_A-K I_A in the ORIGINAL coordinate system. No transformed child is substituted for an original physical child. The simplex probability-law obstruction is non-Boolean because the ei+ej convolution coefficient is a single nonzero pair product. No full-FEI claim follows.

The current direct Walsh checker independently identifies affine-minimal counts 2,2,10,42,2642 in dimensions0..4 by the necessary-and-sufficient inequalities, without adopting A051's transform count. The analytic sorted-basis reconstruction, not those counts alone, accepts the entire orbit characterization. The new path-incidence application supplies an actual Boolean scope guard beyond the source's non-Boolean simplex warning.
''')
next_action='Use actual physical-child eligibility quantitatively to bound a selected pair signed interaction relative to the SAME unused D+S_pair bank, retaining all terminals and A055 mixed T; affine minimum-basis inequalities alone cannot remove orientation.'
prog={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT','attempt_id':'stage7-affine-minimum-path-obstruction','method':'Independent affine reduction review; exact small-cube and coded-spectrum falsification; explicit all-m path-incidence Boolean family with physical-child audit.','mathematical_delta':'Full-span affine-minimal Boolean spectra can have zero singleton collisions and joint collision2/M; physical query preserves H and strictly improves H/I. This removes the affine-only pair route without admitting a false critical witness.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SCOPED_AUTHOR_PROOF_AND_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[dependency],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new explicit Boolean route obstruction'},{'claim_id':dependency['claim_id'],'version':1,'change':'independent local analytic acceptance without repair'}],'source_artifacts':['PATH_CODE_PROOF.md','REVIEW_A051.md','out/PATH_GUARD.json','out/PAIR_PILOT.json','out/PAIR_FULL.json','out/CODED.json','out/LEAN.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal signed pair payment with physical criticality still unproved.','Lean finite-endpoint attempt timed out; no Lean proof receipt.'],'packet_ids':['A052']}
js('PROGRESS.json',prog); js('PACKET_DELTA.json',prog)
report='''# exact target, quantifiers, hypotheses and units

A052/B11 stage7 targets whether the new affine minimum-basis restriction removes the signed-pair orientation cost. All functions are actual Boolean signs on finite uniform cubes; H and collision/entropy ledgers use bits and the previously fixed Fourier normalization. A complete all-m counterfamily to that intermediate assertion is given, with an explicit physical-descendant exclusion. Full FEI remains OPEN. The current owner deadline23October2026 14:49UTC supersedes the older protocol clock.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL revision2026-10-11-execution-v2 read in full; README/CURRENT_STATUS, claim/obstruction/packet registries, B11 next action and plan A052 acceptance contract inspected. BOARD B11 current rows and lead STREAM_NOTESv2 read at stage start. Own last substantive stage is14October stage6; later launch-only folders are not mathematical results. A051 AFFINE_SELECTION sections1--6 and A055 DERIVATION sections1--4 were read, with their latest REPORTs and claim hashes. Own stage4 SIGNED_PAIR_PROOF, stage5 WEAK_CRITICAL_PROOF and stage6 MONOCHROMATIC_FLOW_PROOF were read. Supplement campaign/seed/claim/counterexample/mapping scope refreshed, along with component, rare-moment and block-restriction source notes. Four supplied manuscript versions were decoded explicitly as cp1252 and their available scope/composition locators inspected; this is not a new full-manuscript proof audit or proof dependency. One two-wording read-only math recall returned background, no additional theorem used. Source hashes are in out/SOURCE_RECEIPTS.json. Wake flagged stale personal-context notes; current owner instructions govern.

# complete derivation or exact first unsupported line

PATH_CODE_PROOF sections1--4 give the full all-dimensional auxiliary result. For m>=3 use the zero row plus path-incidence rows as an injective addressing map. Its exact squared spectrum is uniform on C times the address cube. Forest boundary parity proves every minimum-basis inequality; incidence rank proves full affine span. The original data pair2,3 has no singleton spectral adjacency but exactly one diagonal code pair. Hence C2=C3=0 and C23=2^(1-m)>0. At m3 this is1/4. No finite multiplier of singleton collisions dominates this pair, even with actual Booleanity and full affine-orbit minimality.

Criticality changes the argument at a specified line: querying either coordinate preserves the entire entropy but removes influence2/M. Thus each actual child has larger ratio. At K=H/I the signed child bank is NEGATIVE, S_i=-K2/M, and must never be assigned the nonnegative reserve of a least-dimensional witness. This is a guard on an insufficient admission test, not a high-K critical counterexample or a failure of pair selection. Its own H/I tends to4 and is bounded. Historical component-pruning failures remain valid; no component indicator is substituted for the parent. Their prior stage1 physical-child exclusions are consumed rather than re-reported as new checks.

FIRST UNSUPPORTED LINE: bound a selected pair's signed interaction, including A055's mixed refund T, relative to SAME unused D+S_pair using actual physical child eligibility in addition to affine minimality. The new counterexample itself has a complete proof; that universal payment remains open.

# executed validation with domain, arithmetic, commands and outputs

All frozen specifications precede their respective jobs. From A052 run python -X utf8 followed by this run's code/check_pair.py, then code/check_pair.py --full. It checks all65,814 labelled tables in dimensions0..4, finds affine-minimal counts2,2,10,42,2642, and verifies the proposed pair inequality on that finite domain:81,802 counted predicates PASS. Runtimes0.490s and6.605s. This finite pass did not license a universal theorem. code/coded_rows.py exhausts12,870 eight-element subsets of F2^4, checks24 affine-minimal injected addressing codes and finds no failure (0.974s). This is a complete search of that specified code domain only.

code/path_guard.py uses a different fixed six-data/three-address-bit path code. It checks all512 integer Walsh coefficients independently by direct character sums, all512 signed convolution identities, all511 nonzero parity minimum-basis inequalities, full rank, both values of both physical queries, exact coefficient multisets and separate physical edge influences. An independent direct four-point physical-row calculation gives the same C23=1/4. It also checks structural profiles at m3..6 without creating their exponentially large truth tables. All2,445 counted predicates PASS in8.027s; combined84,247 with the small-cube tests. These counters do not include12,870 code eligibility cases. Arithmetic is integer/Fraction; H=6 follows from exactly64 equal squared atoms, so no floating logarithm or sign decision is used.

Every frozen Python job estimates50--65MB and caps55s; all observed runtimes are below9s. No job expected above300MB, GPU, detached process, automatic dimension increase or changed running work. The fixed path family is a deliberate constructive test after the small-cube result, not an exhaustive nine-bit search. Lean core finite-endpoint attempt records RUNTIME_UNVERIFIED after47.5s at timeout45; no certificate or formal theorem is claimed. Proof rung: author-checked analytic proof and exact finite certificate, pending independent-agent review. The Lean source concerns only integer endpoint signs, not the full structural proof.

# proof dependencies and changed downstream conclusions

REVIEW_A051 independently accepts A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1 without repair, including the original-coordinate bank limitation. A055's mixed-refund obstruction is consumed at its stated scope; it is not newly independently accepted. The exploratory affine-only pair domination is refuted, while every registered original theorem remains intact. The strengthened critical admission must retain actual child inequalities; neither a non-Boolean relaxation nor an arbitrary affine-minimal Boolean source supplies child credit. No universal FEI constant improves.

# one next mathematical action and independent reviewer

NEXT_ACTION_PLACEHOLDER

A055 and A094 should independently reconstruct the path spectrum and physical-child exclusion; A051 should consume the obstruction to affine-only payment. A090 reviews the full retained-bank scope. These are local source-bound handoffs; no messages were sent.

# actual persistence receipts or precise save blocker

Four protocol files, complete proof, independent A051 review, frozen specifications, code, outputs and source hashes saved under A052 only. Finalizer checks exact protocol field sets, compatibility-copy byte equality, required headings, two-line STATUS and20MB cap. out/PERSISTENCE_RECEIPT.json records sizes/hashes; local persistence is verified. Supervisor copies, registry adoption, brain ingestion, independent review of the new application and downstream use remain unverified. No local save blocker.

## Universal bridge

This stage moves C019 stopping-tree payment through B11 critical selection by closing an attractive but false affine-only shortcut: full-span affine-minimal actual Boolean sources still have a completely hidden pair collision, and their exact signed child deficit identifies the missing hypothesis. It also supplies independent acceptance of the SAME-K affine reduction. There is zero claimed universal constant gain. What remains is the reserve-relative signed interaction bound with physical child eligibility, mixed refunds and every terminal retained. NEXT is the shortest continuation because it uses the exact hypothesis that excludes this family; another affine-only inequality or larger finite census would leave the universal debt untouched.
'''.replace('NEXT_ACTION_PLACEHOLDER',next_action)
put('REPORT.md',report)
sources=[P/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [B/'BOARD.md', B/'claude/B11/STREAM_NOTES.md']
sources += list((B/'context').glob('*.txt'))
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
sources += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += [supp/'sources'/x for x in ['ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md','ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']]
for who,run,names in [('A051','20261021T193146Z-account03-A051-near-extremizer-definition',['AFFINE_SELECTION.md','REPORT.md','CLAIMS.json']),('A055','20261021T171306Z-account03-A055-extremal-obstruction-referee',['DERIVATION.md','REPORT.md','CLAIMS.json']),('A052','20261014T015635Z-account05-A052-critical-source-structure',['SIGNED_PAIR_PROOF.md']),('A052','20261014T044609Z-account05-A052-critical-source-structure',['WEAK_CRITICAL_PROOF.md']),('A052','20261014T124751Z-account05-A052-critical-source-structure',['MONOCHROMATIC_FLOW_PROOF.md','REPORT.md'])]:
    sources += [B/'agents'/who/'runs'/run/x for x in names]
js('out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources])
status='STATE: Stage7 saved: full-span affine-minimal Boolean path codes refute singleton-only pair collision bound; exact child exclusion;84247 predicates PASS; A051 reviewed; FEI OPEN.\nNEXT: '+next_action+'\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,text in [('WORKLOG.md',f'\n{stamp} Stage7: independently reconstructed A051 affine reduction, then tested singleton-only pair collision. All n<=4 and24 four-data-bit codes pass, but explicit nine-bit path code has C2=C3=0,C23=1/4. Direct Walsh/convolution/physical child checks PASS; actual children retain H6 and reduce I3 to11/4. All-m proof saved; child eligibility, not affine minimality, is the missing input. Lean timed out; no certification. Full FEI OPEN.\n'),('LEARNED.md','\nStage7 durable obstruction: f_m(x,y)=(-1)^(x dot c_y), with zero plus path-incidence code on2^m-1 vertices, is actual Boolean, full affine span and affine influence-minimal. H=2m,I=2(2^m-2)/2^m+m/2. Original data pair2,3 has C2=C3=0,C23=2^(1-m)>0. Thus affine minimality cannot remove the orientation correction even for Boolean spectra. Querying either internal data bit preserves H and removes influence2^(1-m), strictly raising ratio; at K=H/I actual S_i=-K2^(1-m)<0. This is NOT a physically critical witness. Use child eligibility quantitatively before charging a critical bank; finite n<=4 passes had hidden this obstruction.\n')]:
    marker='Stage7: independently reconstructed A051' if name=='WORKLOG.md' else 'Stage7 durable obstruction:'
    if marker not in (A/name).read_text(encoding='utf-8'):
        with (A/name).open('a',encoding='utf-8') as f: f.write(text)
put('CHECKPOINT.md','Stage7 complete locally. All-m path-code proof and exact counterexample saved. Affine-only pair domination refuted; genuine high-K physical criticality route unresolved. NEXT: '+next_action+'\n')
assert set(prog)=={field.split(' (')[0] for field in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for heading in protocol['required_per_run']['report_fields']: assert '# '+heading in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in paths)
js('out/PERSISTENCE_RECEIPT.json',{'checked_at_utc':stamp,'schema_checks':'PASS','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','artifacts':len(paths),'claim':claim['claim_id'],'exact_predicates':84247}))
