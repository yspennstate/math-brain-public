from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
results={f:read(ROOT/'out'/f) for f in ['validation.json','independent.json','mixed.json','mixed_repro.json']}
assert all(x['status']=='PASS' for x in results.values())
total=sum(x['exact_assertions'] for x in results.values());assert total==5643
write(ROOT/'out/RESULTS.json',{'status':'PASS','nonpilot_assertions':total,'runs':results,'independent_external_review':'PENDING','formal_check':'NONE; analytic proof and exact finite certificates','scope':'all-dimensional character/coherent proof and half-depth owner invariant; finite checks are evidence for that proof'})
shared=Path(r'~/brain_workers/FEI100_20261011')
sources=[]
for a,run in [('A059','20261023T105800Z-account03-A059-decomposition-depth'),('A060','20261023T112129Z-account03-A060-composition-sharpness')]:
 p=shared/'agents'/a/'runs'/run/'PROOF.md';sources.append({'path':str(p),'sha256':sha(p),'scope':'full current proof read; scoped acceptance of stage19 exterior module and new obstruction consumed, not acceptance of stage20'})
for p in [ROOT.parent/'20261023T060651Z-account03-A057-coherent-restriction-remainder/PAIR_PROOF.md',shared/'claude/B12/STREAM_NOTES.md',Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]:
 sources.append({'path':str(p),'sha256':sha(p),'scope':'prior own stage or governing protocol'})
write(ROOT/'out/SOURCES.json',sources)
statement='Let m>=4 be divisible by4, c=2^-m, b(X)=(-1)^(sum X_(2j)X_(2j+1)), C=1_(X=1^m), K=b-C, G any independent finite Boolean sign, and chi_J the full character on ANY fresh nonempty physical block J. F=K+C G chi_J has ACTUAL original X-owner B0=4I_X(F)=2m-4mc. While a character remains, any core query has EXACT full decrement c D_iH(G), and every proper character query has decrement0. At the last character, with CURRENT q=(EG)^2 and CURRENT mask density t after exterior restrictions, its exact coherent decrement is sum_s Phi(Khat(s)^2,q Chat(s)^2)+J with0<=J<=2tq/ln2, bounded by T(t,q)=t[q log2(1/t)+q log2(1/q)+(9/2)q]. The q-log term is retained. One specified actual core query costs<=2c; after it, without X queries, the SAME ORIGINAL larger owner funds ALL adaptive character orders/stops and retains>=29B0/32 in every actual terminal. More generally after that core query allow EVERY adaptive interleaving of J and X with at most m/2 X queries on each path, no further core query: T(t,q)-E T(tchild,q)=tq at X while a character remains, and the SAME original owner cash and total remainder remain>=B0/8. The exact stopping inequality Hroot<=B0+E[Hleaf-Bleaf] retains BOTH full terminal profiles, all old debits and all unqueried core/exterior entropy. No hereditary pair floor, private-controller/DATA import, new source account, or designation-pair-only price is assumed. Full X exhaustion, further core queries and universal FEI/root supplier are not proved.'
claim={
 'claim_id':'A057-RARE-COHERENT-CHARACTER-ORIGINAL-OWNER','version':1,'exact_statement':statement,
 'hypotheses':['Uniform independent finite cubes; Boolean signs; entropy in bits.','m>=4 divisible by4, paired quadratic background and all-one mask; fresh nonempty character block of arbitrary size.','Exactly one optional specified old core query before the character/exterior continuation; actual cost booked once.','For mixed theorem, at most m/2 original exterior queries on EACH actual path; no further core queries; arbitrary character order and stopping.','Both old-query children and every complete residual terminal function retained; original cash allocation, never replaced by a newly assigned descendant influence ticket.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A057'],
 'proof_source':{'coherent_identity_and_payment':'PROOF.md Sections1-3, equations(1)-(8)','mixed_continuation':'MIXED_CONTINUATION.md equations(1)-(4)','certificates':['out/validation.json','out/independent.json','out/mixed.json','out/mixed_repro.json']},
 'proof_dependencies':['Finite Boolean Fourier Parseval and physical entropy erasure+JS identity; scalar JS inequality derived in PROOF.md Section2','Boolean split0<=D<=2; elementary log/Jensen inequalities proved or derived in PROOF.md','No imported old private-priority/controller/DATA estimate is needed for this scoped theorem'],
 'review_records':[{'reviewer':'A057','kind':'author proof plus two separate direct-character reproduction paths; NOT external independent acceptance','result':f'{total} nonpilot exact assertions PASS; full mixed tree31 internal nodes/32 complete terminals; no Lean certificate'}],
 'status':'PROVED_LOCAL_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN','supersedes':[],
 'refutes':[],
 'first_unproved_line':'Continue beyond the pathwise m/2 exterior cap from ACTUAL remaining original cash and CURRENT profiles; allow further core queries without an assumed root entropy price. Arbitrary root/core supplier and full FEI remain unpaid.',
 'next_consumers':['A059','A060','A091','A087','B12','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);write(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B12','packet_id':'A057','gap_id':'G-R-SELECT/NONHEREDITARY-COHERENT-OWNER-TRANSFER','attempt_id':'A057-stage20-character-plus-half-depth-v1',
 'method':'Exact coherent empty-core Fourier packet, retained q log(1/q), parity-isometry telescope and original larger-owner cash with current density conversion',
 'mathematical_delta':'Actual non-hereditary masked character block of arbitrary width funded from ORIGINAL4I_X after positive old core debit; >=29/32 owner left without X queries and>=1/8 under EVERY interleaving up to half original exterior depth. No old internal imports; all full terminals retained.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SELF_CONTAINED_SCOPED_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A057-ORIGINAL-PAIR-CAPACITY-TRANSFER@1 (prior target, exterior-only accepted by A059/A060 stage19)','A059 stage19 hereditary-block admission and length-price obstruction (consumed boundary, not theorem dependency)','A060 stage19 non-hereditary designated-pair obstruction (consumed exact target)'],
 'claims_created_or_changed':['A057-RARE-COHERENT-CHARACTER-ORIGINAL-OWNER@1'],
 'source_artifacts':['PROOF.md','MIXED_CONTINUATION.md','SPEC.json','REPRO_SPEC.json','MIXED_SPEC.json','out/RESULTS.json','out/SOURCES.json','out/EXECUTION_NOTES.json'],
 'next_consumers':claim['next_consumers'],'next_action':'A059/A060/A091 independently reconstruct exact coherent q-log packet and both-children original cash; extend past half exterior depth using ACTUAL unused cash/current quadratic or phase refunds, all old debit and full terminal/core profiles retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['new independent external review pending','full exterior exhaustion and further core queries not paid','arbitrary initial root/core supplier remains open; finite cases do not prove full FEI','supervisor mirror/adoption NOT_VERIFIED; no git or external messages used','brain wake degraded/unverified: owner model98.5h, state of mind83.1h, latest dream33.8h stale; not task authority'],
 'packet_ids':['A057']}
fields={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']};assert set(progress)==fields
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)
notes={'stage20_validation':'All mathematical assertions passed on first execution. Original nonpilot character checks2926 plus independent277 =3203; mixed extension added2343+97=2440, final total5643. Previous stage19 total146685 is a DIFFERENT run, not a revised count.',
 'all_dimensional_bridge':'Retained q log(1/q) coherent last-query bound and pathwise cash proof, not extrapolation from m4/m8 finite audit.',
 'prior_reviews':'A059/A060 accept only stage19 exterior module; older mixed internal imports remain conditional in those reports. This stage new scoped theorem needs none of those old inputs.',
 'resource_scope':'All jobs frozen<=100MB estimate; each mathematical helper compute<6s on its saved timing, shell/wake/tool latency is separate; no >300MB job, no GPU, no detached work, no resource shedding, no formal compiler.',
 'review_cap':'Targeted completion of existing non-hereditary admission gap; one scoped proof and its mixed continuation, not a new broad full-FEI candidate.',
 'brain_selfcare':'Current-session wake executed; stale owner/state/dream notes explicitly disclosed and not used for task direction.'}
write(ROOT/'out/EXECUTION_NOTES.json',notes)
report=f'''# A057 stage20: summable coherent non-hereditary transfer

## exact target, quantifiers, hypotheses and units

Fund A060's actual non-hereditary rare pair, including an arbitrary-width character replacement, from an ORIGINAL larger physical owner after an actual positive old core debit. Preserve the exact alpha^2 log(1/alpha^2) term, all old costs and BOTH full terminal profiles. All entropies are bits. The theorem uses F=b-C+C G chi_J, paired bent b on m>=4 bits divisible by4, all-one point C of densityc=2^-m, ANY independent Boolean G and fresh nonempty character J. One specified old core query precedes any adaptive tag/exterior interleaving. The mixed continuation has at most m/2 exterior queries per path and no further core queries. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Current BOARD.md12:06 UTC, B12 lead notesv2, own STATUS and stage19 pair proof, and full execution protocol2026-10-11-execution-v2. A059 run20261023T105800Z PROOF Sections1-4 accepts stage19 exterior scope and supplies hereditary-block/length-price obstruction. A060 run20261023T112129Z PROOF Sections1-7 accepts the same exterior module and provides the normalized non-hereditary pair with price/I_pair unbounded, plus positive-old-debit ownership controls. These scoped reviews do not accept stage20. Immutable source hashes are in out/SOURCES.json. Earlier campaign/papers were read in earlier stages; no new literature claim. The current-session brain wake completed with stale owner-model98.5h/state83.1h/dream33.8h findings; those notes were not task authority.

## complete derivation or exact first unsupported line

PROOF.md gives the exact coherent Fourier remainder. A nonempty physical character separates K's empty-tag spectrum from C*G's tagged spectrum, so an old core query costs EXACTLYc D_iH(G), and all proper tag queries cost0. Only the final tag query spends a coherent bill. With CURRENT q=(EG)^2 and CURRENT event densityt, its complete decrement is L(q)+J, L=sum Phi(Khat^2,q Chat^2),0<=J<=2tq/ln2. Jensen bounds it by T(t,q)=t[q log2(1/t)+q log2(1/q)+(9/2)q]. The q-log term remains literal; at q0 the exact bill is0. This is summable independently of character width because each path has at most one final tag query.

Actual original larger owner B0=4I_X(F)=2m-4mc funds the old cost<=2c and child-current T. Without exterior queries at least29/32 of B0 remains. MIXED_CONTINUATION.md then proves EVERY interleaving of tag queries and up to m/2 exterior coordinates per path: child densities0/2t give the EXACT reserve conversion dropT=tq. Allocate increased child T from unused original cash and debit actual exterior D<=2 once. The pathwise cash inequality B0-2c-m-2^-m/2(m/2+9/2)>=B0/8 guarantees both children retain nonnegative funds and at least one-eighth of the SAME original owner. It counts either a spent or pending last-tag bill, never both. Both complete terminal functions and unqueried core/exterior entropy appear literally in the same-tree telescope.

The first unsupported line is continuing beyond half exterior depth or making further core queries with CURRENT q and ACTUAL unused original cash. A universal original root/core supplier remains unpaid. No descendant ticket is renewed and no pair-only price, new source6 account or old controller/DATA theorem is assumed.

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC.json, REPRO_SPEC.json and MIXED_SPEC.json precede their jobs. Commands from this run: python -X utf8 code/check_character.py --pilot; then code/check_character.py, code/independent_repro.py, code/check_mixed.py and code/mixed_repro.py. Main uses integer Walsh/Fraction prime-log expressions with rigorous36-term atanh bounds and tails; independent paths use DIRECT character sums, separate factorization and48-term bounds. All **{total} nonpilot exact assertions passed**, with no mathematical assertion failure.

Main character audit:71 actual roots;145 old core edges,72 with positive cost;290 last-tag edges including12 nontrivial q cases;418 proper-character zero decrements;2926 assertions. Independent character replay:6 roots,4 positive-old roots, q1/4 children, exact full-terminal telescope;277 assertions. Mixed audit:594 actual states,504 exterior and396 tag edges, current q1/4 and1,2343 assertions. Separate actual mixed tree oldY0,tag0,X0,tag1,X1:31 internal nodes and32 COMPLETE terminal leaves, positive old debit,97 assertions; entropy and owner telescopes agree exactly. Detailed outputs are saved in out/RESULTS.json. The new mixed checks explain the increase from3203 earlier in this stage to5643; stage19's146685 is a different run. All-policy and all-dimensional conclusions follow from the written proof, not finite exhaustion of policies or extrapolation. No Lean certificate or external acceptance claimed.

## proof dependencies and changed downstream conclusions

The new scoped theorem is self-contained: Parseval, actual Fourier erasure/JS identity, the scalar JS inequality derived in PROOF.md, elementary Jensen/log estimates, Boolean0<=D<=2 and original physical influence computation. It does not import old private-priority or signed-DATA estimates, unlike stage19's broader conditional mixed assembly. A060's designated-pair lower bound remains true: the payment now draws from the ORIGINAL larger X owner, not the tiny tag influence. A059's length-price obstruction remains true: proper character queries have zero entropy cost and only the last consumes the coherent ticket. The 29/32 remainder applies BEFORE any exterior queries; the1/8 guarantee applies to the broader half-depth mixed policy class. These are distinct scopes, not conflicting constants.

## one next mathematical action and independent reviewer

A059/A060/A091 should independently reconstruct the retained q-log packet, original4I_X debit and child cash conversion, including the nonconstant old AND3 child(q1/4) and BOTH full terminal profiles. Then extend past the half-depth cap using ACTUAL remaining cash and quadratic/phase refunds rather than the coarse2-per-query charge. Preserve all old core/tag bookings and CURRENT q/t; do not solve another isolated rare-character example.

## actual persistence receipts or precise save blocker

Required protocol JSON fields, statement SHA256, identical PACKET_DELTA, two-line STATUS, append-only rolling notes and all artifact sizes/hashes are checked locally; out/PERSISTENCE.json records readback. Every file is under20MB. All writes are inside A057, no git/external messages/brain writes or resource shedding. Supervisor mirroring/adoption NOT_VERIFIED. Checklist identity was not supplied by this session's hook and is checked read-only before any completion action; no old identifier is reused after the reported shared-checklist crash. Brain self-care remains degraded/unverified for the stated stale sources; current task and mathematical sources were used instead.

Universal bridge: C019 moves to an actual non-hereditary coherent block of arbitrary width after a positive internal debit and ALL interleaved tag/exterior policies up to half exterior depth, from the SAME ORIGINAL4I_X owner with>=1/8 unused and both full terminal profiles. The alpha^2 log(1/alpha^2) charge remains explicit and summable; no O(alpha^2) substitute or renewed budget is used. Full exterior/core completion and a universal root supplier remain open. Removing the depth cap through actual remaining-owner refunds is the shortest route toward a complete payment invariant, whereas more examples within this already proved character mechanism would not address the remaining universal bridge.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for x in protocol['required_per_run']['report_fields']:assert f'## {x}' in report
status=f'STATE: A057 stage20 coherent q-log character ticket paid ORIGINAL4I_X after positive core debit; ALL tag/exterior interleavings to half exterior depth retain>=B0/8; {total} exact assertions PASS; self-contained scoped proof/review pending; FEI OPEN.\nNEXT: A059/A060/A091 audit current q/t and SAME original cash/both full terminals; extend beyond half exterior depth using ACTUAL refunds, retaining old core/tag costs and arbitrary core entropy.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8');assert len(status.splitlines())==2
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} stage20 {ROOT.name}: consumed A059/A060 independent stage19 exterior acceptance and non-hereditary/length-price obstructions. New exact character interface: old coreD=cD_G; proper tagD0; final bill<=t[q log1/t+phi(q)+9q/2], q=(EG)^2. ORIGINAL larger4I_X=2m-4mc pays actual old debit and all tag policies with29/32 left; half-depth arbitrary X/tag interleavings retain>=1/8 via CURRENT profile conversion dropT=tq. {total} exact nonpilot assertions PASS including direct-character mixed tree31nodes/32fullterminals; external review pending, full FEI open. No old internal imports or source bank; no git/messages/resource shedding.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage20 durable: fresh character chi_J keeps the core spectrum disjoint from exterior K until the last tag bit. Old coreD=cD_G exactly; every proper tag queryD0, regardless of tag width. At last tag ONLY empty core pairs contribute, so exact L(q)+JS has L=sum Phi(Khat^2,q Chat^2), JS<=2tq/ln2. Retain T=t[q log1/t+phi(q)+9q/2], not O(q). In A060 all-one bent splice with m divisible4, ORIGINAL larger X influence=m/2-mc. Its4I_X owner funds one actual core debit<=2c and tag transfer with29/32 left. Interleave up to m/2 X queries per path: CURRENT T profile drop=tq, old/spent OR pending tag counted once, cash>=B0/8. This self-contained scoped theorem needs no old private-controller/DATA imports, but full X/core completion and generic root owner remain unpaid. Next: use actual refunds rather than coarse2-per-X bound to remove half-depth cap.\n')
write(ROOT/'out/PERSISTENCE.json',{'verified_at':stamp,'schemas':'PASS','statement_sha256':'PASS','PACKET_DELTA_identical':True,'nonpilot_assertions':total,'mirror':'NOT_VERIFIED; supervisor-owned','external_review':'PENDING','running_stage_jobs':0,'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='PERSISTENCE.json']})
for f in read(ROOT/'out/PERSISTENCE.json')['files']:
 assert f['bytes']<20_000_000;assert sha(ROOT/f['path'])==f['sha256']
assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
print(json.dumps({'status':'SAVED_AND_VERIFIED','nonpilot_assertions':total,'claim':claim['claim_id'],'external_review':'PENDING','full_FEI':'OPEN'}))
