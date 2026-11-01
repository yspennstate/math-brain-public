from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
OLD=A/'runs/20261023T012352Z-fleet03-A022-one-point-surgery'
SRC=BASE/'agents/A021/runs/20261023T045725Z-fleet03-A021-rare-core-asymptotics'
S25=BASE/'agents/A025/runs/20261023T040353Z-fleet03-A025-rare-event-counterfamily'
def read(p): return p.read_text(encoding='utf-8')
def save(p,s):
    with p.open('w',encoding='utf-8',newline='\n') as f: f.write(s)
def js(p,o): save(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(read(p))
old=load(OLD/'CLAIMS.json')[0]; dep=load(SRC/'CLAIMS.json')[0]
refs=[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'scope':s} for c,s in [(old,'original numerical data-prefix admission; pending external review'),(dep,'active-only controller transaction and original versus conditional density; scalar and relevant identity reconstructed')]]
outs={n:load(R/'out'/f'{n}.json') for n in ['pilot','main','replay']}
assert all(z['status']=='PASS' for z in outs.values())
total=sum(z['assertions'] for z in outs.values())
statement=('Refinement of A022 ledger v7, inherited assertions retaining their original scopes: for all t>=2, arbitrary controlled single-vertex surgery of g tensor t with g negative only at000, every prescribed block-first synchronized DATA frontier d<=3floor(t/2)+2, interleaved with arbitrary finite adaptive CONTROL trees only on active data cylinders, has EXACT bank B=4I_remaining_data+delta sum_active p H(a_current)-C-U=Bpure_d+sum_executed_control p gamma_w>=13t/576. Here delta=8^-t is ORIGINAL, w=2^-d, gamma_w is the Jensen gap of J_w(s)=G_delta(s)+(1-w)log2(1-delta+delta s^2), and G_delta is defined in PROOF Section2. Controller references R_delta,a are prescribed on active leaves and frozen on inactive descendants; all DATA rounds query EVERY frontier leaf. Complete positive DATA references, old0<=U<=t/64, every complete terminal KL, original signed controller entropy spend and all prior Jensen gains are retained. B+D+E is invariant with signed DATA and CONTROL increments of PROOF(4). No source entropy is regranted. Unequal DATA-depth stopping cuts, arbitrary source entropy priced by influence, and full FEI remain OPEN.')
claim={
'claim_id':old['claim_id'],'version':8,'exact_statement':statement,
'hypotheses':['Uniform independent original DATA/CONTROL cubes; entropies in bits; t>=2','Fixed block-first data order; synchronized frontier DATA depths in paid domain','Only active DATA cylinders may query controller bits; arbitrary finite outcome-adaptive controller subtrees','Prescribed original-delta R_current on active leaves; freeze R on inactive leaves; q_h as A022@7; all complete KL and old U retained'],
'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
'contributors':['A022 fleet03 stage9','A021 stage19 supplies active-only continuation interface'],
'proof_source':{'current':'PROOF.md','validation':['out/pilot.json','out/main.json','out/replay.json'],'inherited_numerical_admission':str(OLD/'PROOF.md')},
'proof_dependencies':refs,
'review_records':[{'reviewer':'A022 author','status':'ANALYTIC_DERIVATION_AND_TWO_IMPLEMENTATIONS_CHECKED','independent_person':False,'assertions':total,'scope':'exact mixed frontier identity, signed history, same reserve; whole chain external review pending'}],
'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':{'claim_id':old['claim_id'],'version':7},'refutes':[],
'first_unproved_line':'An outcome-dependent DATA stopping depth breaks the synchronized affine comparison; same-account payment for that continuation and influence-priced arbitrary controller source are not proved.',
'next_consumers':['A021','A025','A028','A029','A087','A094','B05']}
js(R/'CLAIMS.json',[claim])
next_action='Make one DATA query on only one active controller-outcome leaf, creating unequal DATA depths; price its signed affine term from SAME diminished original account with original delta/current q/R, old U, previous Gamma, source spend and all complete terminal KLs. A021/A025 reconstruct; A028/A029/A087/A094 review.'
report=f'''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. Pay the next synchronized DATA query after A021@2's active-only controller conversion, and repeat that interleaving without renewing its account. For all t>=2 and every Boolean independent controller, prescribed block-first DATA depths d<=3floor(t/2)+2 retain the SAME13t/576 reserve after old0<=U<=t/64, when arbitrary adaptive controller trees operate only on active DATA cylinders between rounds. Every DATA round queries all frontier leaves. Entropies are bits; arbitrary unequal-depth DATA cuts are excluded.

# sources actually read, revisions and theorem locators

Current BOARD, B05 STREAM_NOTES v2, own STATUS and recent LEARNED were read. A021 stage19 run20261023T045725Z REPORT and complete PROOF1--5 provide the newly paid active-only conversion and its explicit next-DATA gap; its claim is {dep['claim_id']}@{dep['version']}, SHA256 {dep['statement_sha256']}. A025 stage8 run20261023T040353Z REPORT supplies the common-policy predecessor and actual reset warning; no whole-bundle independent acceptance is inferred. Own stage8 run20261023T012352Z complete PROOF1--7 and helper supply numerical admission and original reference ownership. EXECUTION_PROTOCOL v2 was reread, as were machine-wide AGENTS instructions. The broader campaign/paper baseline was read in prior stages, not newly reviewed here. Current deadline2026-10-23 14:49UTC overrides obsolete protocol dates. Source paths/hashes are in out/SOURCE_RECEIPTS.json.

Brain self-care remains degraded/unverified: stale personal-context model and state-of-mind sources affect personalization and continuity. They are not mathematical premises; current campaign files govern.

# complete derivation or exact first unsupported line

PROOF1--4 gives the complete all-parameter argument. Relevant A021 scalar curvature and transaction are reconstructed: each actual active CONTROL node contributes p*gamma_w>=0, using ORIGINAL delta and actual data reach w. A DATA round conserves complete controller CE by Parseval while keeping each leaf's own frozen reference, and conserves the original source entropy earmark. Remaining DATA influence and DATA CE are affine in activation mean. The active controller leaves partition the original controller cube, so their mean corrections average to the original mean. Consequently each DATA-round bank change is EXACTLY that of the original pure-DATA account. Induction yields B=Bpure_d+Gamma, with Gamma the sum of all previously paid controller Jensen gaps. The reserve13t/576 follows from A022@7; no controller entropy or old booking is renewed.

Both complete child KLs and all inactive leaves remain in B+D+E=constant, with DATA increment reach*(4Inf-DeltaH_F) and CONTROL increment delta*p*DeltaH_a-reach*DeltaH_F. The ORIGINAL controller entropy equals remaining earmark plus signed spend. A literal-control witness leaves strictly positive inactive controller CE=(1/2)log2(64/63), so those costs cannot be silently omitted or reset. First unsupported line: unequal DATA-depth, controller-outcome-dependent stopping breaks the synchronized affine comparison; payment of that next transaction from the same residual account is not established. Arbitrary source entropy still needs an influence supplier.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC preceded pilot/main; REPLAY_SPEC preceded the separate reconstruction. Pilot4 cases/{outs['pilot']['assertions']} exact assertions PASS in{outs['pilot']['elapsed_seconds']:.4f}s. Main128 cases/{outs['main']['assertions']} assertions PASS in{outs['main']['elapsed_seconds']:.4f}s: t=2, vertices0,1,7,63, ALL16 two-bit controllers, two mixed schedules, DATA depths0..5, outcome-stopped second controller query. No symmetry or exhaustive-all-vertices claim. Production uses integer FWHT, exact physical edges, Fraction probabilities, prime-log identities and outward40-term atanh bounds with a proved geometric tail.

Standalone replay imports NO production/helper code: direct character sums, Fourier-degree influence, separately constructed complete references, separate prime-log algebra and48-term outward rational enclosures. On32 fixtures (vertices0,63, all16 controllers, depth1 CONTROL then DATA, stopped depth3 CONTROL then DATA) it checks{outs['replay']['assertions']} assertions in{outs['replay']['elapsed_seconds']:.4f}s. It verifies the mixed bank, full signed history, source-spend identity and positive frozen-inactive-cost witness. This is author reproduction, not independent-person review. Total{total} assertions include the pilot. Finite checks do not provide the all-dimensional step: PROOF2--4 does.

Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/replay.py. Frozen estimates100MB/80MB are below300MB; no large admitted job, formal compiler, GPU, automatic dimension increase or detached work. Peak memory is unmeasured. No Lean/formal certification is claimed. Compute snapshots read status ok; existing work was not changed. All mathematical jobs finished.

# proof dependencies and changed downstream conclusions

Advance the same A022 ledger from v7 to v8, preserving every inherited scope. A022@7 supplies the original numerical bound and remains pending external review. The necessary A021@2 controller transaction and scalar concavity are reconstructed, without claiming independent acceptance of its entire bundle. The new result removes the restriction that all DATA queries precede all active-only CONTROL queries: any number of synchronized rounds may interleave without spending the existing reserve. It does not remove the supplied-source premise, pay clipped raw resets, or prove FEI.

# one next mathematical action and independent reviewer

{next_action} Review requests are recorded in consumer fields only; no messages or acceptances are asserted. This changes the synchronized-depth hypothesis, rather than extending an already paid controller-only tree.

# actual persistence receipts or precise save blocker

REPORT, PROOF, CLAIMS, PROGRESS, byte-identical PACKET_DELTA, frozen specs, source receipts, code and exact outputs are saved only under this assigned run. STATUS has two lines; WORKLOG and LEARNED are updated. out/ARTIFACT_CHECK.json validates protocol key sets, claim digest, compatibility bytes, hashes and20MB limits. No research write changes campaign sources, another agent's folder, brain, git or external services. Independent-person review, supervisor copying and remote mirrors remain unverified. Nothing owned by this stage remains running.

**Universal bridge:** This advances C024 history transfer toward C019 by closing the actual next DATA transaction after a paid active-only CONTROL conversion, with an EXACT repeated-history identity B=Bpure_d+Gamma and the SAME13t/576 reserve. Original delta/current references, all prior gains and source spend, old U and both complete terminal debts remain. The universal gaps are unequal-depth stopping and arbitrary influence-priced source admission. NEXT makes one actual DATA branch asynchronous from the already diminished account; that tests the first missing universal stopping transaction instead of another isolated seed class.
'''
save(R/'REPORT.md',report)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH','attempt_id':'A022-stage9-mixed-synchronized-data-control','method':'consume A021@2; affine DATA transaction plus original controller Jensen-gain invariant','mathematical_delta':'Pay next DATA query and arbitrary repeated synchronized DATA/active-only CONTROL interleaving: B=Bpure_d+Gamma>=13t/576 from SAME original account. Source spend, frozen inactive refs, old U and every terminal KL retained.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_AUTHOR_CHECKED; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':refs,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':8}],'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','SEARCH_SPEC.json','REPLAY_SPEC.json','code/check.py','code/replay.py','code/exact.py','code/finalize.py','out/pilot.json','out/main.json','out/replay.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Independent-person review pending','Unequal DATA-depth stopping continuation open','Arbitrary controller entropy supplier open','Supervisor mirrors unverified','Brain self-care degraded; personal continuity unverified'],'packet_ids':['A022']}
js(R/'PROGRESS.json',progress); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sources=[BASE/'BOARD.md',BASE/'claude/B05/STREAM_NOTES.md',SRC/'REPORT.md',SRC/'PROOF.md',SRC/'CLAIMS.json',S25/'REPORT.md',OLD/'PROOF.md',OLD/'CLAIMS.json',OLD/'code/exact.py',Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),Path(r'~\AGENTS.md')]
js(R/'out/SOURCE_RECEIPTS.json',{'hash_time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'Finalization hashes; BOARD is a mutable intake/status source, immutable proof versions and statements are bound separately. No earlier campaign baseline is claimed freshly read.','sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources]})
save(A/'STATUS.md',f'STATE: A022 stage9 saved: next DATA and arbitrary synchronized DATA/active-only CONTROL interleaving paid; EXACT B=Bpure+Gamma>=13t/576, SAME original delta/U/source spend/all KL;{total} exact assertions PASS; review pending; FEI OPEN.\nNEXT: One DATA query only on one active controller-outcome leaf: unequal depths; retain SAME diminished original bank, current q/R, prior Gamma, old U/source spend and full terminal KL. A021/A025/A028/A029/A087/A094 review v8.\n')
entries={
'WORKLOG.md':f'\n2026-10-23 05:39UTC assigned stage9 ({R.name}): consumed A021@2 and A025@4; independently reconstructed relevant J curvature/controller identity, proved next DATA affine cancellation with frozen inactive references and repeated B=Bpure+Gamma invariant. Pilot4/main128/replay32 fixtures;{total} exact assertions PASS. Source and full signed history retained. No new source entropy payment or unequal-depth claim; external review/mirrors pending. All mathematical jobs ended.\n',
'LEARNED.md':'\nStage9 mixed-history fact: for ORIGINAL delta and arbitrary current controller a, J_w(s)=G_delta(s)+(1-w)log2(1-delta+delta s^2) is concave for delta<=1/64. Active-only CONTROL gains p*JensenGap (not w*p again). A synchronized next DATA round passes each leaf its SAME R, so complete controller CE is conserved by Parseval; source remaining delta sum_active p H(a) is unchanged. DATA CE and DATA influence are affine in alpha; active controller means average to ORIGINAL mean. Therefore B_frontier=Bpure_depth+sum_prior_controller p*gamma_w for any repeated synchronized DATA/active-only CONTROL history, retaining original delta/current q/R, old U, source spend and EVERY terminal KL. Inactive references freeze at exit, not at later active controller state: literal controller leaves inactive CE=(1/2)log2(64/63)>0. This preserves13t/576 within old paid depth range but supplies no arbitrary controller influence bound or unequal-depth DATA stopping theorem.\n'}
for name,entry in entries.items():
    prior=read(A/name)
    if ('Stage9 mixed-history fact:' if name=='LEARNED.md' else R.name) not in prior: save(A/name,prior+entry)
protocol=load(sources[-2]); req=protocol['required_per_run']
assert set(progress)=={s.split(' (')[0] for s in req['progress_fields']}
assert set(claim)==set(req['claim_fields'])
assert all('# '+s in report for s in req['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_CHECK.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
js(R/'out/ARTIFACT_CHECK.json',{'status':'PASS','protocol_keys':'exact','statement_sha256':claim['statement_sha256'],'progress_delta_identical':True,'rolling_status_lines':2,'total_assertions':total,'independent_person_review':'PENDING','formal_certification':'NOT_CLAIMED','mirror_verification':'PENDING_SUPERVISOR','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'status':'PASS','claim_version':8,'assertions':total,'files':len(files),'statement_sha256':claim['statement_sha256']}))
