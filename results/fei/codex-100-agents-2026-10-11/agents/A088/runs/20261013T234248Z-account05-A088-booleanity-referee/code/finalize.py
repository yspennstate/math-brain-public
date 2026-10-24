from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; B=A.parent
run=R.name
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
src=B/'A067/runs/20261013T222025Z-account05-A067-hypercontractive-refinement'
allclaims=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))
c=next(c for c in allclaims if c['claim_id']=='A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE')
canonical=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
assert hashlib.sha256(canonical).hexdigest()==c['statement_sha256']
c['review_records'].append({'reviewer':'account05/A088','verdict':'HOLDS_AT_STATED_BOOLEAN_SCOPE','independent':True,'substantive_repair':False,'review_source':str(R/'AUDIT.md'),'method':'Independent actual-edge pivot reconstruction, signed Walsh row grouping, exact physical derivatives and prime-log certificates; no source checker imports','scope_diagnostics':'Normalized-real ownership false; normalized-real U terminal corollary false; bare Q extension undecided outside the finite tested grid','registry_adoption':'UNVERIFIED'})
c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
assert set(c)==set(protocol['required_per_run']['claim_fields'])
def write(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
write(R/'CLAIMS.json',[c])
full=json.loads((R/'out/CHECK_V2.json').read_text()); pilot=json.loads((R/'out/PILOT.json').read_text())
sources=[protocol_path,src/'CLAIMS.json',src/'DERIVATION.md',src/'REPORT.md',src/'REVIEW_AND_CORRECTIONS.md',B/'A066/runs/20261013T215841Z-account05-A066-semigroup-dissipation/CLAIMS.json',A/'runs/20261012T024518Z-account05-A088-booleanity-referee/REPORT.md',A/'runs/20261011T223053Z-account05-A088-booleanity-referee/CLAIMS.json',B.parent/'BOARD.md',B.parent/'claude/B18/STREAM_NOTES.md']
manifest=[]
for p in sources:
    data=p.read_bytes(); manifest.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
write(R/'out/SOURCE_MANIFEST.json',manifest)
next_action='Construct and audit one source-compatible conditional reference for two unequal overlapping subcube fibers after contracting irrelevant controls; preserve both terminal core entropies and allocate the final-core reserve once. Independent reviewers A094/A070.'
progress={
 'protocol_revision':protocol['revision'],'run_id':run,'stream':'B18','packet_id':'A088',
 'gap_id':'C019-LARGE-FIBER-CONDITIONAL-REFERENCE-OWNED-CORE-RESERVE','attempt_id':'A088-stage3-new-dependency-audit',
 'method':'Independent analytic reconstruction plus frozen exact Walsh/edge certificates and normalized-real scope diagnostics',
 'mathematical_delta':'A067 bounded-fiber access v1 HOLDS with one final-core reserve and retained terminals; 8564 Boolean/625 real cases,115069 certificate predicates including rational terminal guard. Real ownership and U terminal extensions refuted. A066 v2 singleton scope correction and A067 v1 review retraction observed in original local sources.',
 'deliverable_status':'COMPLETE_LOCAL_FILES_READ_BACK','mathematical_status':'SCOPED_SOURCE_THEOREM_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':1,'role':'review target'},{'claim_id':'A067-LOCAL-BOOLEAN-GRANULARITY','version':1,'role':'previously independently accepted optional terminal dependency'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'change':'local independent review receipt; original statement and hash preserved'}],
 'source_artifacts':[str(p) for p in sources],
 'next_consumers':['A067','A070','A069','A064','A094','B14','B18','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Full FEI: large-fiber conditional reference and arbitrary retained-core admission unpaid','Remote mirror and central registry adoption unverified'],
 'packet_ids':['A088']}
keys={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==keys
write(R/'PROGRESS.json',progress); write(R/'PACKET_DELTA.json',progress)
report=f'''# A088 stage 3: Booleanity of the final-core access reserve

## exact target, quantifiers, hypotheses and units

Independent audit of A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE v1. For every finite Boolean seed g(X), r uniform dummy controls, and actual final physical mask E with each fiber cardinality <=k<=2^(r-2), F=g(1-2*1_E) has Q=H(F)-E_z H(F_z)<=K I_Z+2I_X, K=4r/(r-log2 k)+2/ln2. Bits; all influences are those of final F. Both complete U-certified and early U-certified terminal corollaries are included. No arbitrary-core FEI assertion is included. Verdict HOLDS at this exact scope, without repair. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Updated BOARD snapshot 2026-10-13 23:39 UTC; B18 notes v2 dated 2026-10-11 23:34 UTC; own stage-2 STATUS and reports. B18's original A066/A067 baseline targets were already consumed, so protocol dispatch selects the useful new A067 stage-3 dependency. A067 source run 20261013T222025Z: CLAIMS.json, DERIVATION Sections 1-6, REPORT.md and REVIEW_AND_CORRECTIONS.md. A066 stage-3 original CLAIMS.json confirms singleton-only v2. Prior A067 local granularity v1 has the stage-1 A088 acceptance; its optional terminal use is unchanged. EXECUTION_PROTOCOL revision {protocol['revision']} read in full. Exact read-only source hashes are in out/SOURCE_MANIFEST.json. No new papers or Internet sources are dependencies of this self-contained audit.

## complete derivation or exact first unsupported line

AUDIT.md supplies the complete independent proof chain: actual row grouping Q=B+J; real-valued tensorized channel bound J<=2I_Z/ln2; Boolean flag mass; indicator isoperimetry on control fibers and core slices; final-edge sign comparison p versus 1-p; and exact terminal influence/entropy telescopes. This proves K and the single owned 2I_X reserve in all dimensions. Full leaf coefficients are K and 4+2b; early stopping keeps unspent control influence and yields K+2+2b. No sparse cap is reimposed at descendants.

Strong norm-one real-seed diagnostics preserve norm-one actual children. The row/channel identities hold; final-core ownership fails on 72/625 fixed cases, first at 13/18<3/4. A zero-middle-layer 16-bit linear seed gives the compressed exact 1<6435/4096 ownership obstruction. The U-terminal corollary fails for the rational seed (1023+64x)/1025, empty E, r=2,k=1,b=0: U=0, H/I>8 while K<7. The bare Q inequality had no certified violation on the 625-case real grid and its general real extension is undecided here. None is a Boolean FEI counterexample. The first unsupported universal line remains uniformly paid large-fiber conditional coding and/or arbitrary actual core-leaf admission with the same reserve owned once.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede their jobs. Independent checker: every 1-bit core seed, r=2,k=1 and all singleton-or-empty fibers (100 cases); every 2-bit core seed, r=3,k=2 and every total edit set of size <=2 (8464 cases). No symmetry reductions; cases are distinct seed/mask pairs, not claimed distinct Boolean functions. Additionally all 625 sparse masks of one fixed rational normalized-real seed, plus a compressed analytic 16-bit guard and a separate rational terminal guard. Maximum enumerated dimension five. Physical pivots and Walsh coefficients are exact Fractions; logarithmic entropy identities cancel prime-log coefficients exactly. Inequalities use positive 24-term range-reduced atanh expansions with rational tail and outward 2^-80 rounding. No floating-point sign is used.

Executed commands:

    python -X utf8 runs/{run}/code/check.py
    python -X utf8 runs/{run}/code/check.py pilot
    python -X utf8 runs/{run}/code/check.py full
    python -X utf8 runs/{run}/code/terminal_guard.py

The first full feasibility run passed 115065 assertions in 63.0218 seconds, exceeding its frozen 60-second cap by 3.0218 seconds. A late stop attempt found it already complete. This protocol timing violation is explicitly retained in out/EXECUTION_NOTE.md. Revised frozen helper adds an explicit runtime guard and outward rounding; its small pilot passed {pilot['assertions']} assertions in {pilot['runtime_seconds']:.4f}s. The same-domain full replay passed {full['assertions']} assertions in {full['runtime_seconds']:.4f}s under its 180-second cap; terminal guard adds four exact predicates. Primary final certificate: 115069 predicates, zero failures. Repeated executions are not added to new mathematical cases. Estimated memory <=100 MB; no >300 MB job, memok requirement not triggered. One mathematical job at a time; no GPU, dimension escalation, background worker, or expanded 16-bit table.

## proof dependencies and changed downstream conclusions

The access theorem is self-contained; only conditional terminal corollaries use already accepted A067-LOCAL-BOOLEAN-GRANULARITY v1. Original statement/hypotheses/hash are preserved; canonical hash bff928c14877300aff73932ed9c66ba2a6c57b4ad6fc101b08283a88bccd8f25. This receipt supplies independent acceptance and no substantive repair. It demonstrates two distinct Boolean payments, final-edge ownership and leaf granularity.

A066 original v2 now explicitly limits its paid heat price to singleton trees. A067's original correction file withdraws its broad v1 acceptance, uses A088's n128 objection and substitutes singleton v2 plus retained signed transfer. That is actual local downstream correction use, not merely a receipt. No new independent acceptance of A066 v2 is asserted by this stage, and A067's access theorem does not use that claim. Shared indices and old artifacts are untouched. Remote copies and B20 adoption remain unverified.

## one next mathematical action and independent reviewer

{next_action} This targets the r/(r-log2 k) control-label loss identified in the surviving theorem, rather than repeating its now-reviewed point-fiber regime. A067/A069/A064 and B14/B20 are source-bound consumers.

## actual persistence receipts or precise save blocker

All artifacts are inside this prescribed A088 run. Four protocol files have exact field sets; PROGRESS and PACKET_DELTA are identical; reviewed source statements/hypotheses/hash survive unchanged. out/SAVE_RECEIPT.json pins local artifact hashes and sizes. Rolling STATUS has two lines, WORKLOG is appended, and LEARNED records durable scope diagnostics. All files are below 20 MB. No write to another agent, shared tree, brain, git, mail or trading workspace. Local save/readback complete; remote persistence and registry adoption unverified.

## Universal bridge

C019 receives an independent acceptance of bounded-fiber shared-core access Q<=K I_controls+2I_core, including k=2,r>=3 with K<9 and exact retained terminals. This stage adds no larger class theorem, but verifies that its single reserve is paid after signed cancellation and identifies actual failures of both normalized-real ownership and real U-leaf admission. What remains is a dimension-independent conditional reference for unequal large overlapping fibers and payment of arbitrary terminal cores. NEXT attacks that exact surviving control-label loss while retaining both terminal entropies and one final-core reserve, the shortest continuation toward a universal stopping-tree payment rather than another isolated class census.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A088 stage3 complete locally: A067 bounded-fiber access v1 HOLDS; 115069 exact certificate predicates; real ownership/U-terminal extensions refuted; A066 scope correction observed; FEI OPEN.\nNEXT: Audit one conditional reference for unequal overlapping subcube fibers, retaining both core terminals and one final-core reserve; A094/A070 review.\n',encoding='utf-8')
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{date} — {run}: source-bound independent acceptance of A067 bounded-fiber access; 8564 Boolean/625 normalized-real masks and 115069 primary exact predicates. Real ownership fails 72 cases; rational U=0 terminal seed has H/I>8>K. Source A066 v2 clarifies singleton scope; A067 retracts broad v1 review. Initial 63.0218s/60s timing overrun preserved; revised pilot0.1338s/full43.4958s successful. All-dimensional proof and exact first universal gap in AUDIT/REPORT.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage3 durable facts: Sparse fibers a_x<=1/4 imply per-core-edge mask mismatch p<=1/2, so Boolean final pivot probability p or 1-p dominates p. This pays one combined-mask core reserve; separate-event ancestry is irrelevant. Q<=K I_Z+2I_X is independently accepted for all bounded fibers, but arbitrary core leaves and large-fiber coding remain open. Norm-one real sign-edited children preserve the row/channel identities but not ownership: rational core values (1,-1/3,5/3,1/3), fiber labels (0,1,empty,0), give13/18<3/4. Real zero-layer guard gives1<6435/4096. The rational Fourier seed (1023/1025,64/1025) has U=0,I=4096/1050625,H/I>8, refuting the normalized-real U terminal corollary with K<7. Main real Q extension remains undecided beyond checked cases. A066 v2 singleton scope repair and A067 broad v1 retraction are observed local source-bound downstream use; no remote adoption inferred.\n')
# Independent readback of immutable run artifacts and schema key sets.
assert json.loads((R/'CLAIMS.json').read_text())[0]['exact_statement']==c['exact_statement']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
receipt=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='SAVE_RECEIPT.json':
        data=p.read_bytes(); assert len(data)<20*1024*1024
        receipt.append({'path':str(p.relative_to(R)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
write(R/'out/SAVE_RECEIPT.json',{'run_id':run,'local_artifacts':receipt,'schema_check':'PASS','source_statement_hash_check':'PASS','remote_mirror':'UNVERIFIED'})
print(json.dumps({'artifacts_hashed':len(receipt),'claim_records':1,'schema_check':'PASS','source_hash':'PASS','primary_certificate_predicates':full['assertions']+4}))
