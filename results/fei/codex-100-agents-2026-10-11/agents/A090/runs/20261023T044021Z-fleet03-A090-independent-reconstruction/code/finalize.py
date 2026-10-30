from pathlib import Path
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1]; base=run.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def put(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
assert c['status']=='PASS' and c['assertions']==819 and len(c['rows'])==24
assert c['checker_sha256']==sha(run/'code/check.py') and c['helper_sha256']==sha(run/'code/exact.py')
assert all(r['conditional_nonempty_shape_changed']==[True,True] for r in c['rows'] if r['new_on_spread']==r['new_off_spread']=='1')
sources=[Path('BOARD.md'),Path('claude/B18/STREAM_NOTES.md'),Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
for agent,name in [('A004','20261023T031926Z-fleet03-A004-constant-and-unit-ledger'),('A001','20261023T000044Z-fleet03-A001-quantifier-audit')]:
    src=base.parent/agent/'runs'/name
    sources.extend([src/'CLAIMS.json',src/'DERIVATION.md'])
dump(run/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
report=r'''# A090 stage8: a paid dummy query and two genuine source-profile resets

## exact target, quantifiers, hypotheses and units

All entropies, erasures, cross-entropies and KL use bits and the entire normalized spectral law, including the empty atom. Fix b(y)=+1 iff y0=y1=y2=0 on six data bits, c=b except c(0)=-1, and F=b except at y=0 where F=Maj3 on three independent bits. Binary coordinates are uniform and Walsh characters are (-1) to the parity. The original quota is 4(I(b)+I(c))/2=3; no descendant influence surplus is added.

Execute data y3, then any active coordinate in its origin/on-child, then either remaining dummy coordinate in that edited daughter. At the intermediate A004 frontier the edited daughter has k=2 active data bits among r=4, the constant sibling has its explicitly reset point reference, and the original off-sibling has the maximally spread k=3,r=5 source reference. The original initial mixture and admitted canonical resets are booked. Prescribe the next edited child's reference Q_z by the explicit source formula below with k=2,r=3, and the other child's unedited reference R_w with the same k,r. For every real z,w in [0,1], the resulting full bill is <3-248210/1000000. This is a fixed Boolean source theorem, not arbitrary-source admission. All subsequent finite adaptive histories with marginal references and no fresh reset retain this bound.

## sources actually read, revisions and theorem locators

BOARD snapshot 2026-10-23 04:35 UTC, B18 STREAM_NOTES v2, own stage7 status/helper and protocol execution-v2 were read. Current user continuation date supersedes the protocol's old campaign end. Followed productive-packet/new-dependency dispatch rather than restarting the stale five-variable census direction.

Read A004 run 20261023T031926Z, CLAIMS A004-ACTIVE-QUERY-CANONICAL-FRONTIER-REPAIR@1 and A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK@1; read A001 run 20261023T000044Z CLAIMS. Their DERIVATION files were requested for definitions but the producer arguments were also exposed. Consequently this stage DOES NOT claim statement-only independent acceptance of A004 or A001. The new dummy-frontier calculation below is an original extension, with own truth tables and own existing exact helper; no producer checker was imported. SOURCE_RECEIPTS records full source hashes. Original inputs to the extension are the Boolean definition and the displayed reference prescription, not the producer's numerical margins.

## complete derivation or exact first unsupported line

For k active bits among r data bits, write s=2^-k, t=2^-r, mu=1-2s, and g=1-2A_k, so ghat(empty)=mu, ghat(T)=-2s for active nonempty T and zero otherwise. Define V(empty)=mu^2, V(T nonempty)=(1-mu^2)/(2^r-1), and R_z=(1-z)P_g+zV. For the edited Maj3 source let p(S,T) be its true squared spectrum, S the encoder set and T the data set. Set

    q(T)=sum_S p(S,T),
    Rprime_z(T)=(1-t/s)R_z(T)+(t/s)mu*1_empty(T)+2t/2^r,
    Q_z(S,T)=Rprime_z(T)*p(S,T)/q(T).

For an unedited child the complete reference is R_z(T)*1_{S=empty}. All formulas are source-prescribed, with no inherited-reference input. Expanding g+2 psi A_r, where psi is the negative-Maj3 indicator, E psi=E psi^2=1/2, gives q(T)=ghat(T)^2+2t ghat(T)+2t^2. Substitution separately at the empty, active nonempty and other data sets gives Rprime_0=q. Also sum Rprime_z=1-t/s+(t/s)mu+2t=1. For (k,r)=(3,5),(2,4),(2,3), 0<t/s<1 and the floor is positive, so all divisions and occupied logarithms are valid. Both complete references are affine in their spread parameter and agree with their respective true law at parameter zero. Reference-only atoms are retained.

At any query, signed Walsh restrictions are a_child(T)=a(T)+epsilon*a(T+i). Hence the mean actual child law equals m=P_-i. If r=R_-i is the incoming reference marginal, then

    B_i + mean CE(P_child,r)=CE(P,R)-c_i,
    c_i=D(P||R)-D(m||r)>=0.

This follows by expanding both CE differences; c_i is nonnegative by the finite conditional-KL chain rule, including reference-only atoms. Every reset from r to Q has signed price CE(P,Q)-CE(P,r). Thus signed prices telescope exactly while all terminal CE remains present.

Let B0 denote the first y3 erasure and B1 the active query erasure at reach1/2. Let p_a be the k2,r4 edited daughter, Q_a=Q_1(k2,r4), and p_far the untouched original off-child with Q_far=V(k3,r5) at encoder-empty. Let C_a be the whole preceding full-frontier bill. It is reconstructed from actual physical spectra, not taken from the producer's numerical margin:

    C_a=B0+B1/2+CE(p_a,Q_a)/4+CE(p_far,Q_far)/2.

The constant terminal at reach1/4 has complete CE zero only AFTER its explicit reset. The checker also obtains C_a by starting with BOTH old 7m/8+U/8 resets, changing to Q_1 and R_(3/4), retaining the actual active-query conditional-KL refund, explicitly pricing the constant reset and finally pricing R_(3/4)->V in the far sibling. The two log-linear expressions coincide exactly. Rational intervals give 107981/10^6 < 3-C_a < 107982/10^6.

Now query a dummy data bit in p_a, with erasure B2, true children p0,p1, inherited marginal r and actual conditional-KL refund c2. Their new signed prices are E0=CE(p0,Q_z(k2,r3))-CE(p0,r) and E1=CE(p1,R_w(k2,r3))-CE(p1,r). The new global bill is exactly

    C_new=C_a-c2/4+E0/8+E1/8
         =B0+B1/2+B2/4+CE(p0,Q_z)/8+CE(p1,R_w)/8
                              +CE(p_far,Q_far)/2.

The fourth terminal, the earlier constant child, remains explicitly present with CE zero. Terminal reaches are 1/8,1/8,1/4,1/2 and sum to one. No new root quota appears. Direct and signed formulas agree as exact log-linear expressions for all checked choices. More generally the equality is algebraic for every real z,w.

For fixed true p, CE(p,(1-z)p+zQ) is convex, minimized at zero and therefore nondecreasing on [0,1]. The source formulas above are affine and start at the true law. Consequently (z,w)=(1,1) is the worst case for the WHOLE real rectangle. The maximal-spread margin is exactly the following sum, with all logarithms base two:

    M=-57/32 +(699/256)log 7 +(3783/2048)log 3
      +(3555/2048)log 5 -(1201/2048)log 1201
      -(791/2048)log 113 -(7/32)log 31
      -(337/1024)log 337 -(41/512)log 41 +(19/256)log 19.

Certified bounds are 248210/10^6 < M < 248211/10^6. Permuting the original three active data coordinates or the two remaining dummy data coordinates preserves the source and reference formulas; all six choices were additionally checked. At this endpoint c2/4 is approximately 0.08239050209 and (E0+E1)/8 approximately -0.05783845235. These decimals only explain the improvement; the theorem uses exact intervals. Both prescribed resets change the conditional NONEMPTY joint profile compared with inherited r, verified by unequal rational normalized nonempty probabilities. Their signed costs here are favorable: no universal positive-liability payment theorem is being inferred.

Every later finite adaptive marginal-reference continuation subtracts reach-weighted nonnegative conditional KL by the same identity, so retains this payment and all complete terminal CE. Randomized policies follow by averaging deterministic policies.

First unreconstructed implication: after this actual mixed active/dummy history, a fresh prescribed reset following exposure of an ENCODER/controller coordinate has not been shown to fit the remaining SAME account. Restricting Maj3 changes its conditional private-event mean and nonempty profile; the displayed balanced-Maj3 kernel cannot be reused without derivation. Universal construction of an O(I)-priced arbitrary-source reference also remains unpaid. The present favorable signed resets do not settle that universal step or prove FEI.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json was written before the check: fixed nine-bit source, six coordinate choices, four endpoint pairs, 24 rows, no dimension escalation; memory estimate70MB, runtime cap60seconds. Executed python -X utf8 runs/20261023T044021Z-fleet03-A090-independent-reconstruction/code/check.py. Integer Walsh transforms and Fraction probabilities reconstruct all spectra. CE identities use rational linear combinations of integer logarithms. For ln x on [1,2], the checker sums 40 terms of 2 sum t^(2j+1)/(2j+1), t=(x-1)/(x+1), and bounds the tail by 2t^81/[81(1-t^2)]. Reducing integers by powers of two and dividing by a strictly positive ln2 interval gives rigorous log2 bounds. Floats are display only. Every corner explicitly passes M>248210/10^6; maximal corners also pass M<248211/10^6.

Final check PASS: 819 exact assertions, 24 rows, runtime under2seconds. An earlier diagnostic run passed but printed an imported stale assertion counter; the counter was corrected to the helper's live count and the final run also added explicit rational margin inequalities and profile diagnostics. No failed mathematical assertion occurred. This bounded check is below300MB so no heavy-job memok admission was required. No new Lean success is asserted; prior formal admission was held. No external work was started.

## proof dependencies and changed downstream conclusions

Uses the specified neutral fixture, elementary physical Fourier restriction and KL chain rule, and the explicit A001/A004 source prescriptions. Their balanced-event data-floor normalization is rederived above. A004's earlier numeric input is independently recomputed but is not assigned independent review credit because its argument was exposed. One new narrow theorem is recorded, pending independent review. This extends a paid canonical frontier by a real dummy exposure and two actual nonempty-profile resets, using only the original quota3. It does not make the special source universal. It also does not contradict the earlier maximal first-frontier failure: the physical queried tree and references differ.

## one next mathematical action and independent reviewer

Expose one encoder/controller coordinate in the surviving k2,r3 edited child at the maximal new endpoint, derive BOTH actual residual private-event kernels and prescribed complete source references, and price their signed changes using ONLY the remaining original margin M. Retain the old full far sibling, dummy-off sibling, constant child, old reset debits and true conditional-KL refund. A004 and A094 are requested next consumers through this saved handoff; no messages were sent. A001 can check the exact margin expression and all six physical choices independently.

## actual persistence receipts or precise save blocker

All research artifacts are saved inside A090. Required protocol JSON fields, CHECK hashes, statement hashes, equality of PROGRESS/PACKET_DELTA and sub20MB sizes are checked by code/finalize.py; SOURCE_RECEIPTS and out/ARTIFACT_RECEIPTS record actual SHA256 values. Rolling STATUS, WORKLOG and LEARNED are updated. Local persistence is verified; supervisor adoption, mirrors, publication and downstream review are unverified. Brain self-care remains degraded/unverified because owner-model and state-of-mind sources are stale; no brain repair or write is claimed.

**Universal bridge:** This stage moves the C019 stopping-tree payment/C024 history-transfer frontier by one genuine dummy exposure and TWO prescribed conditional-nonempty-profile resets after an already paid active exposure. The same quota3 leaves a rigorously certified margin >248210/10^6, versus >107981/10^6 at the prior frontier; old debits and all full terminals remain. What remains is a paid controller-induced kernel/shape change and, universally, influence-priced arbitrary-source admission. Exposing a controller bit at this exact diminished account is the shortest next test because it changes the balanced private-event kernel in the live candidate, rather than proving another isolated Boolean class result.
'''
put(run/'REPORT.md',report)
statement='For the fixed neutral six-data-bit AND3 point edit encoded by Maj3 and the exact A001/A004 reference prescriptions, after y3, one active on-child query, and the maximal A004 daughter/far-sibling source resets, query either remaining dummy bit inside the edited k2,r4 daughter. Reset its edited child by Q_z(k2,r3) and its unedited child by R_w(k2,r3), for every real z,w in[0,1]. Retaining every old signed debit and complete terminal at reaches1/8,1/8,1/4,1/2, the SAME original quota3 leaves more than248210/1000000 bits. At z=w=1 the margin is less than248211/1000000. Both new conditional nonempty profiles differ from the inherited marginal. Every subsequent adaptive finite no-fresh-reset marginal-reference continuation is paid from the same account. No arbitrary-source admission or FEI conclusion follows.'
cid='A090-MIXED-DUMMY-CANONICAL-SAME-BANK'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['One fixed actual nine-bit Boolean source as fully specified in REPORT','Bits; complete normalized reference laws, empty and reference-only atoms retained','Initial source parameters lambda1,alpha3/4; next active daughter beta1 and far sibling alpha_new1; explicit constant-child reset','New real z,w in[0,1]; six coordinate choices; finite adaptive no-fresh-reset continuation','Original quota3 only; global expected payment; no independently solvent child allocation'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A090/fleet03; A001/A004 supplied earlier frontier and source prescriptions'],'proof_source':['REPORT.md','code/check.py','code/exact.py','out/CHECK.json'],'proof_dependencies':['A004-ACTIVE-QUERY-CANONICAL-FRONTIER-REPAIR@1 source prescription, earlier full margin recomputed; not independently accepted here','A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK@1 source definition','Elementary finite conditional-KL chain rule and Fourier signed restriction, rederived'],'review_records':[],'status':'PROVED_EXACTLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':'Prescribed fresh reset after actual encoder/controller exposure in surviving edited daughter with SAME unused original margin; universal influence-priced arbitrary-source admission.','next_consumers':['A004','A001','A094','A096','A097','B18','B20']}
dump(run/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B18','packet_id':'A090','gap_id':'C019-C024-SAME-OWNER-CANONICAL-RESET','attempt_id':'A090-stage8-mixed-dummy','method':'Exact physical Walsh/Fraction reconstruction; source-defined references; signed full-terminal ledger; rational logarithm intervals and convex continuum lift','mathematical_delta':'One real dummy query and two genuine nonempty-profile resets paid from SAME quota3; certified reserve>248210/1e6,24 endpoints/819 assertions; earlier active margin recomputed; source review independence not claimed.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_EXTENSION_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':['A004-ACTIVE-QUERY-CANONICAL-FRONTIER-REPAIR@1','A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK@1'],'claims_created_or_changed':[cid+'@1'],'source_artifacts':[str(p) for p in sources],'next_consumers':['A004','A001','A094','A096','A097','B18','B20'],'next_action':'One actual encoder exposure plus prescribed fresh residual-kernel reset from SAME remaining margin, all old debits and complete terminals retained.','stagnant_substantive_attempts':0,'blockers':['Universal source admission unpaid','Controller fresh-kernel reset payment unresolved','Independent extension review and supervisor publication unverified','Brain self-care owner/context sources stale; no formal-check pass claimed'],'packet_ids':['A090']}
dump(run/'PROGRESS.json',progress); dump(run/'PACKET_DELTA.json',progress)
put(base/'STATUS.md','STATE: Stage8 saved: SAME quota3 pays active-then-dummy exposure and TWO genuine source-profile resets; reserve>248210/1e6;819 exact checks/24 rows PASS; pending independent review; FEI OPEN.\nNEXT: A004/A094 review; expose one encoder bit in surviving k2,r3 daughter and price BOTH residual-kernel resets from SAME original margin, retaining all full siblings/old debits.\n')
for fn,entry in [('WORKLOG.md','Stage8: read updated BOARD/B18 notes; source arguments exposed so no statement-only A004 review credit. Original mixed-dummy extension proved: 24 endpoint rows,819 exact checks,1.36seconds; original reserve rises to>248210/1e6, actual conditional-nonempty changes in BOTH children; all old signed costs/full terminals retained. No heavy compute, no new formal pass. NEXT actual encoder kernel change. Report and four protocol artifacts saved; FEI OPEN.'),('LEARNED.md','A090-MIXED-DUMMY-CANONICAL-SAME-BANK@1: fixed AND3/Maj3 root quota3, first y3 then active then dummy in edited daughter, maximal prior daughter/far references; fresh k2,r3 edited source Q_z and off source R_w are paid for all real z,w in[0,1], margin>248210/1e6. Worst endpoint1,1 margin .24821046038. New global refund c2/4=.08239050209 and total weighted reset=-.05783845235, both conditional nonempty shapes changed. This is favorable signed profile transport, not universal positive-reset funding. Next encoder query changes private-event mean; balanced-Maj3 kernel cannot be assumed unchanged.')]:
    with (base/fn).open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' '+entry+'\n')
protocol=json.loads(sources[2].read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
for field in protocol['report_fields']:assert '## '+field in report
files=[p for p in run.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(run/'out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(run)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files])
for row in json.loads((run/'out/ARTIFACT_RECEIPTS.json').read_text(encoding='utf-8')):assert sha(run/row['path'])==row['sha256']
dump(run/'FINAL_VALIDATION.json',{'status':'PASS','timestamp':now,'claim_count':1,'exact_assertions':819,'rows':24,'required_schema_fields':'PASS','progress_compatibility':'BYTE_IDENTICAL','source_hash_binding':'PASS','artifact_hash_readback':'PASS','files_hashed':len(files),'full_fei':'OPEN','formal_check':'NOT_RUN_THIS_STAGE; previous admission held','publication':'SUPERVISOR_UNVERIFIED','brain_selfcare':'DEGRADED_UNVERIFIED','running_research_jobs':0})
print(json.dumps({'status':'PASS','files_hashed':len(files),'margin_lower':c['certified_margin_lower'],'rows':24,'assertions':819}))
