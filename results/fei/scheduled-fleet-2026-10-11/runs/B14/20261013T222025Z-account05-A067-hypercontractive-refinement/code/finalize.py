from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path(__file__).resolve().parent.parent;A=R.parent.parent;B=A.parent.parent
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(name,v):(R/name).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=read(P);now=datetime.now(timezone.utc).isoformat();run=R.name
outputs=[read(R/'out'/n) for n in ['CHECK_PILOT.json','CHECK_FULL.json','DIAGNOSTIC.json']]
assert all(o['complete'] for o in outputs)
assert sum(o['assertions'] for o in outputs)==244039
sources=[
 A.parent/'A066/runs/20261013T215841Z-account05-A066-semigroup-dissipation/CLAIMS.json',
 A.parent/'A070/runs/20261013T212602Z-account05-A070-analytic-route-referee/CLAIMS.json',
]
accept={('A066-POSITIVE-RESTRICTION-HEAT-LEDGER',2),('A066-BLOCK-REFINEMENT-HEAT-TRANSFER',1),
        ('B14-LEAD-POINT-DEFECT-NEUTRALIZATION',2),('A070-TWO-EDIT-PROJECTION-CROSS-LEDGER',1)}
claims=[]
for p in sources:
    for c in read(p):
        if (c['claim_id'],c['version']) not in accept:continue
        c['review_records'].append({'reviewer':'account05/A067','verdict':'ACCEPT_AT_STATED_SCOPE','independent':True,
          'substantive_repair':False,'proof_source':str(R/'REVIEW_AND_CORRECTIONS.md'),
          'method':'Independent row-entropy, scalar joint-budget, finite-refinement, coupling and projection-operator reconstructions. Original statement/hypotheses/hash preserved.',
          'registry_adoption':'PENDING_B20'})
        c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
        claims.append(c)
assert len(claims)==4
old_path=A/'runs/20261012T004014Z-account05-A067-hypercontractive-refinement/CLAIMS.json'
old=next(c for c in read(old_path) if c['claim_id']=='A066-POSITIVE-RESTRICTION-HEAT-LEDGER')
old['review_records'].append({'reviewer':'account05/A067','verdict':'RETRACT_UNQUALIFIED_ALL_BLOCK_ACCEPTANCE; ACCEPT_SINGLETON_COMPONENT_ONLY',
  'proof_source':str(R/'REVIEW_AND_CORRECTIONS.md'),'witness':str(R/'out/CHECK_FULL.json'),
  'supplied_source_repair':False,'replacement':'A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2; all-block identity and signed transfer retained'})
old['status']='GAP_SCOPE_UNQUALIFIED_BLOCK_TREE_BUDGET; SINGLETON_COMPONENT_VALID'
old['first_unproved_line']='Unqualified cumulative channel-plus-level price on every finite physical block-query tree; n128 point-defect whole-cube tree has rate >11/4>2+2/e.'
claims.append(old)
statement=(
 'For every Boolean seed g on m>=0 uniform core coordinates X, r control coordinates Z, and final physical edit mask E, '
 'put F(x,z)=g(x)(-1)^1_E(x,z). Assume every core fiber E_x has at most k assignments, k>=1 and k2^-r<=1/4. '
 'Let I_Z and I_X be the final F control/core influence sums, and Q=H(F)-E_z H(F_z), with entropy in bits. Then '
 'Q <= K I_Z+2 I_X, K=4r/(r-log2 k)+2/ln2. The core reserve is allocated once to the combined mask; '
 'I_X(F)>=I_X(1-2*1_E)>=2 P(E)log2(1/P_X(E_x nonempty)). Empty edit sets have Q=I_Z=0. '
 'In particular k=1,r>=2 gives K=4+2/ln2 and k=2,r>=3 gives K<=6+2/ln2. '
 'Two graph-controlled events with arbitrary shared core/domains/control maps have <=2 assignments per fiber after either XOR or union-once editing. '
 'Every complete physical control-reveal tree has this access price and retains all actual core leaves. '
 'If every complete leaf satisfies U<=bI, b>=0, the reviewed local granularity certificate gives H(F)<=max(K,4+2b)I(F). '
 'For earlier control-only stopping trees with U-certified leaves, the valid bound is H(F)<=(K+2+2b)I(F), retaining remaining control influence. '
 'No arbitrary core-leaf admission is asserted. Dropping the sparse-fiber cap invalidates the ownership inequality: '
 'g=(-1)^x and E={(0,0),(1,1)} on one core and one control bit give I_X(F)=0<I_X(1-2*1_E)=1.'
)
hypotheses=[
 'Actual Boolean signs on finite uniform cubes; entropy in bits; standard physical pivotal influence.',
 'The seed g is independent of the r control coordinates; the edit mask is the actual final physical XOR or union mask.',
 'Every fiber has cardinality <=k and k2^-r<=1/4; this implies r>=2 and r-log2 k>0.',
 'The full access tree exposes every control and retains the exact actual core restrictions; its reserve is not renewed at descendants.',
 'The U conditions are hypotheses for terminal entropy payment, not consequences of the access bound.',
]
new_id='A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE'
new={'claim_id':new_id,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['account05/A067'],'proof_source':str(R/'DERIVATION.md'),
 'proof_dependencies':[{'claim_id':'A067-LOCAL-BOOLEAN-GRANULARITY','version':1,
   'acceptance_scope':'Independent A088/A070 acceptance at stated scope; needed only for conditional U-leaf corollaries, not the main access payment.',
   'proof_source':str(A/'runs/20261011T220539Z-account05-A067-hypercontractive-refinement/CLAIMS.json')}],
 'review_records':[],'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PASSED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A070','A088','A094','A069','A061','A064','B05','B06','B13','B14','B20']}
claims.append(new)
cf=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==cf for c in claims)
write('CLAIMS.json',claims)
progress={
 'protocol_revision':protocol['revision'],'run_id':run,'stream':'B14','packet_id':'A067','gap_id':'FEI-B14-A067-INITIAL',
 'attempt_id':'A067-STAGE3-BOUNDED-FIBER-OWNERSHIP',
 'method':'Full block entropy/real-field channel tensorization plus final Boolean edge ownership; bounded multiplicity fibers, exact truth-table/prime-log certificates, four independent source reconstructions and one prior scope retraction.',
 'mathematical_delta':'C019 access for arbitrary combined bounded-fiber edits: Q<=K I_controls+2 I_core, K=4r/(r-log2 k)+2/ln2; two-event k2,r3 gives K<9. One final-core reserve survives signed cancellation. Terminal U admission and large-fiber conditional coding remain open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; REMOTE_MIRRORS_UNVERIFIED',
 'mathematical_status':'SCOPED_BOOLEAN_ACCESS_THEOREM_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A067-LOCAL-BOOLEAN-GRANULARITY','version':1,'scope':'conditional terminal certificate only'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'new coherent access theorem' if c is new else ('prior broad review narrowed; author v2 substituted' if c is old else 'independent acceptance receipt')} for c in claims],
 'source_artifacts':[str(R/p) for p in ['DERIVATION.md','REVIEW_AND_CORRECTIONS.md','FROZEN_SPEC.json','FROZEN_DIAGNOSTIC.json','out/CHECK_PILOT.json','out/CHECK_FULL.json','out/DIAGNOSTIC.json']],
 'next_consumers':new['next_consumers'],
 'next_action':'Replace the r-bit conditional-control alphabet price for two unequal overlapping subcube fibers by one source-compatible reference, retaining both terminal core entropies and a single final-core reserve; contract irrelevant controls first.',
 'stagnant_substantive_attempts':0,
 'blockers':['No universal arbitrary-core U admission or terminal entropy payment.','Large-fiber conditional label cost r/(r-log2 k) remains unpaid uniformly.','New authored claim awaits independent review; central adoption and supervisor copying unverified.'],
 'packet_ids':['A067']}
pf={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==pf
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)

report='''# A067 stage 3: final-mask ownership for shared-core edits

## exact target, quantifiers, hypotheses and units

Pay C019 access for two rare graph-controlled edits sharing an arbitrary Boolean core and control block. Let g(x) be Boolean, z contain r dummy controls, and F=g*(-1)^1_E use the actual final edit mask. Sequential flips use XOR; union-once edits use union. If every core fiber has at most k assignments and k*2^-r<=1/4, the proved universal access statement is

    H(F)-E_z H(F_z) <= K I_controls(F)+2 I_core(F),
    K=4r/(r-log2 k)+2/ln2.

For one assignment per fiber and r>=2, K=4+2/ln2<7. For two assignments per fiber and r>=3, K<=6+2/ln2<9. Every quantity belongs to the final F. One reserve is charged across the whole control tree. The theorem allows arbitrary seed dimension, edit domains and graph control maps, and both events may share their complete active core. It does not admit arbitrary terminal core leaves.

If every actual full-reveal leaf satisfies U<=bI, the complete entropy ledger yields H(F)<=max(K,4+2b)I(F). Thus b=1 gives the same <7/<9 constants in the two regimes. Early U stopping retains remaining control influence and has the larger coefficient K+2+2b. All information is in bits, all physical functions are Boolean signs on uniform cubes. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-13 22:15 UTC at stage start, B14 STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, own STATUS.md and stage-2 DERIVATION/code/CLAIMS. Re-read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2, and inspected current CLAIM_REGISTRY navigation. Campaign/supplement and threshold/percolation text background from earlier stages is retained; no new paper theorem is invoked without reconstruction.

New originals read: A088 run 20261012T024518Z REPORT/AUDIT/CLAIMS and n128 scope certificate; A066 run 20261013T215841Z DERIVATION Sections 1-5 and exact v2/transfer claims; A070 run 20261013T212602Z REPORT/DERIVATION/CLAIMS, corrected neutralization Section 1 and projection cross Section 4; A069 run 20261012T043929Z DERIVATION (A1)-(A4),(S1)-(S5); A061 run 20261013T215821Z REPORT and PADDING_EDIT_PROOF Sections 1-5. Actual source hashes are saved in out/SOURCE_MANIFEST.json.

A088 independently accepted the prior A067 padding-access theorem, so that baseline is not reopened. A061 now proves the arbitrary-core local point-edit limits (lambda,B,D)=(1,2,4) and retains the terminal deficit; repeating the one-edit limit is retired. A070 refutes a physical-intersection-only cross bill, including with nonempty retained cores, so this stage works with the final combined mask instead of assuming signed edit orthogonality. The stream lead's direction is followed; its original boundary issue has the explicit A070 v2 repair independently reviewed here.

## complete derivation or exact first unsupported line

DERIVATION.md gives the entire proof. Entropy tensorization, the two-point scalar channel, Boolean edge isoperimetry and the full physical restriction identity are reconstructed on the page. The channel bound J_controls<=2 I_controls/ln2 is already dimension-free and extends to real coefficient fields; it is not the novel Boolean payment.

The nonempty-control spectral mass is exactly alpha=E_x[4a_x(1-a_x)], with a_x the final fiber density. Its empty/nonempty flag gives the control erasure price at most 8r*rho+4rho*log2(1/epsilon), where rho is total edit probability and epsilon is active-core support density. Control-fiber isoperimetry pays the first part at rate 4r/(r-log2 k). The new Boolean ownership step pays the second: on each core edge the edit mismatch probability is <=1/2, so the final F edge is pivotal with at least that probability irrespective of the seed edge's sign. Thus I_core(F)>=I_core(final mask)>=2rho*log2(1/epsilon). This charges a reserve 2I_core ONCE after cancellation, never the sum of two separate ancestral reserves.

All actual leaf entropy remains in H(F)=Q+E H(F_z). The U certificate is conditional, and the early-tree proof keeps unrevealed control influence rather than replacing root control influence by spent influence. No small-fiber hypothesis is silently imposed again at descendants. A one-core/one-control-bit Boolean witness refutes the final-edge ownership comparison when the sparse-fiber cap is removed.

The precise dimension loss is the conditional label step H(S_controls|flag,core)<=r, compared with control-fiber physical influence 2rho(r-log2 k). It yields the displayed r/(r-log2 k), not a logarithm introduced by the real log-Sobolev channel. On a codimension-two subcube with r-2 irrelevant controls, H=2 and I=1 exactly, but the crude flag alphabet bound grows as h2(3/4)+(3/4)r. This isolates a removable dimension overcount. Unequal overlapping large fibers need a conditional source-compatible reference after irrelevant controls are contracted.

The first unsupported universal line is a uniformly paid large-fiber conditional reference and/or actual arbitrary-core leaf admission, with the same final-core reserve owned once. The main access theorem is complete at its stated scope; no line in its proof assumes FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded all searches; FROZEN_DIAGNOSTIC.json preceded the fixed diagnostic replay. No symmetry reduction, author code import, automatic dimension escalation, GPU or background process. Estimated memory <=100 MB, so the >300 MB memok gate was not triggered. One mathematical job ran at a time. Every job was frozen below 60 seconds and completed below that cap.

Commands from this agent folder:

    python -X utf8 runs/20261013T222025Z-account05-A067-hypercontractive-refinement/code/check.py pilot
    python -X utf8 runs/20261013T222025Z-account05-A067-hypercontractive-refinement/code/check.py full
    python -X utf8 runs/20261013T222025Z-account05-A067-hypercontractive-refinement/code/check_diagnostic.py

Pilot: 12 fixed fixtures, 291 assertions, 0.0111 seconds. Full: 14,098 cases, 243,717 assertions, 3.7483 seconds. Domains are all 110 graph-fiber configurations with all m=0,1 seeds and r=2; all 5,476 m=1 Boolean seed/fiber configurations with r=3 and <=2 assignments per fiber; all 8,464 m=2 seed/edit sets of cardinality <=2 in the 32-point cube; and 48 explicit m=3/4/6 constant/dictator/Maj3/pointdefect/bent/addressing fixtures at r=3,4. Maximum dimension 10. Cases overlap and are executions, not a count of distinct functions.

The full checker reconstructs every final Boolean truth table, integer Walsh coefficients, physical core/control pivots, each actual restricted core spectrum, exact influence telescope, alpha and row Parseval. Entropy equalities use rational prime-log coefficient maps, cancelling symbolically before interval evaluation. Signs use 20-term range-reduced positive atanh intervals with proved tail, division by a positive ln2 interval and outward rounding to denominator 2^80. The checker certifies the sharper erasure inequality separately and retains all terminal influence/entropy. A SHA256 digest binds the ordered case certificates; the smallest positive reserve margin and all larger named fixture records are saved.

Of the full cases, 14,094 complete trees meet U<=I at every leaf. Four pointdefect fixtures fail that admission; their actual rejected truth tables and exact U/I are saved in out/DIAGNOSTIC.json. They are not declared certified by the access bound. Early U stopping is also checked on the 12 pilot and 48 named fixtures, with remaining control influence retained. The diagnostic adds eight fixed cases and 31 assertions in 0.0013 seconds: three padded-subcube alphabet-loss certificates, the four leaf rejections, and one compressed real-field ownership guard. The guard uses 16 formal singleton coefficients and a binomial edge count, not a 16-bit truth table or an expanded Boolean search. Final primary certificates contain 244,039 assertions; all executed diagnostic revisions total 244,096. out/EXECUTION_HISTORY.json records the successful initial diagnostic and both real-guard revisions separately; overlapping replays are not counted as new functions. No mathematical failure occurred.

The fixed certificates also reconstruct A066's n128 block-scope inequality using rational ln2 lower bound 842/1215, the ownership-cap counterexample, and A070's exact disjoint-edit cross 1/2. All-dimensional quantifiers and growing-dimension diagnostics are supplied by the analytic proof, not an extrapolation from the finite domain.

## proof dependencies and changed downstream conclusions

The main theorem is self-contained. Only the optional terminal corollaries use A067-LOCAL-BOOLEAN-GRANULARITY v1, already independently accepted by A088/A070. Physical identities/telescopes are reconstructed; neither conjectural C018 erasure payment nor universal C019 access is a dependency. The non-Boolean channel bound is separated from the new final-edge Boolean ownership argument, which uses actual sign pivots. An exact normalized real control psi=(1/4)sum of 16 input signs is unchanged by edits at its zero middle layer and z00; its core spectral energy is 1, while the mask core influence is 6435/4096. This invalidates real-field reserve ownership even with the same sparse-fiber cap and confirms the new Boolean step.

REVIEW_AND_CORRECTIONS.md independently reconstructs four incoming versions without repair: A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2; A066-BLOCK-REFINEMENT-HEAT-TRANSFER v1; B14-LEAD-POINT-DEFECT-NEUTRALIZATION v2; A070-TWO-EDIT-PROJECTION-CROSS-LEDGER v1. Source statements/hypotheses/hashes are preserved in CLAIMS.json with acceptance receipts. The repaired neutralization version is A070-authored, not a repair authored by this reviewer. Central adoption remains pending.

Correction: my prior A066 v1 acceptance reconstructed a singleton price but did not explicitly exclude its unqualified block-tree wording. That broad acceptance is withdrawn, using A088's exact Boolean n128 objection; only the block identity and singleton components remain accepted. The author's explicit v2 and retained signed transfer replace it. The majority/address calibration depended only on the block identity and stays accepted. Old run files are unchanged. This correction cannot invalidate the self-contained access theorem.

The source-bound live B14 queue is consumed before opening one new coherent candidate: A067 stage 2 has A088 acceptance, A069 stage 2 has A070 acceptance, and the four remaining repaired/transfer candidates receive the independent reconstructions above. The new candidate is pending independent review and within the two-candidate cap. Receipt, supervisor adoption, downstream mathematical use and remote verification are distinct.

## one next mathematical action and independent reviewer

Build one conditional reference for two unequal overlapping subcube fibers after removing irrelevant controls. Price its actual final-mask control spectrum against physical control influence, keep both actual core leaf entropies, and allocate the existing final-core reserve once. This targets the explicit r-bit label loss that limits the current bounded-multiplicity theorem; another point-edit limit or physical-overlap-only cross bound would repeat a closed or refuted route. Independent reviewers: A070 and A088/A094; consumers A069/A061/A064 and B05/B06/B13/B14/B20.

## actual persistence receipts or precise save blocker

The four protocol files, complete derivation, independent reviews/correction, frozen specifications, code and exact outputs are confined to this prescribed A067 run. out/SAVE_RECEIPT.json records actual local SHA256 hashes and byte sizes, and out/SOURCE_MANIFEST.json pins read-only inputs. Code validates exact protocol key sets, original reviewed statements, new canonical statement hash and byte-identical PROGRESS/PACKET_DELTA. All files are below 20 MB. STATUS has exactly STATE/NEXT lines; WORKLOG is appended and LEARNED records durable facts. No shared indices, other agent folders, brain databases, git trees, mail or remote publication were touched. Local persistence is verified; supervisor copies, mirrors and independent acceptance of the new theorem are unverified.

## Universal bridge

C019 advances from a one-point padding strip to arbitrary final edits with bounded control-fiber multiplicity, including two graph-controlled events sharing their entire active core: Q<=K I_controls+2I_core, with K<9 for k=2,r>=3 and one cancellation-aware final-core reserve. Conditional U-certified complete leaves close the full ledger at max(K,4+2b), but arbitrary core admission remains unpaid and large fibers retain the explicit r/(r-log2 k) label loss. NEXT replaces that precise control-label overcount on unequal overlapping subcube fibers while preserving terminal entropy and the owned reserve; it is the shortest route beyond the now-paid two-event access regime, rather than another isolated one-point class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
assert all('## '+s in report for s in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
(A/'STATUS.md').write_text('STATE: Stage 3 complete: bounded-fiber shared-core access paid by K I_controls+2 I_core; 244039 primary exact checks; four reviews and A066 scope correction saved; FEI open.\nNEXT: Replace r-bit labels for unequal overlapping subcube fibers with one conditional reference and owned final-core reserve; A070/A088/A094 review.\n',encoding='utf-8')
# Refresh this stage's last rolling entry without duplicating it.
for rolling in ['WORKLOG.md','LEARNED.md']:
    path=A/rolling
    prior=path.read_text(encoding='utf-8')
    pos=prior.rfind('\n## ')
    if pos>=0 and run in prior[pos:]:path.write_text(prior[:pos],encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {now} — {run}\nConsumed A088 acceptance and A066 block-scope objection, A061 one-edit cap/terminal law and A070 signed two-edit countercertificate. Proved a new self-contained bounded-fiber theorem: Q<=K I_controls+2 I_core, K=4r/(r-log2 k)+2/ln2, provided k2^-r<=1/4. k2/r3 has K<9; combined final-mask ownership spends one core reserve despite shared events and cancellation. Conditional complete U leaves give max(K,4+2b); early stopping retains remaining control influence. Located dimension loss at the conditional r-label bound and certified the irrelevant-control subcube example. Final primary pilot/full/diagnostic certificates contain 244039 exact assertions; all executed revisions total244096; 4 full leaf admissions fail and their exact witnesses are retained. Independently accepted four incoming versions and narrowed my prior unqualified A066 v1 acceptance, substituting explicit singleton v2. No mathematical failure; full FEI and large-fiber/core admission gaps remain open. Next: conditional reference for unequal overlapping subcube fibers.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## Stage 3 durable facts ({run})\nFor F=g(x)(-1)^1_E with dummy r controls, maximum fiber cardinality k satisfying k2^-r<=1/4, Q=H(F)-E_z H(F_z)<=K I_Z(F)+2 I_X(F), K=4r/(r-log2 k)+2/ln2. Boolean final-edge ownership I_X(F)>=I_X(mask) follows because mismatch probability <=1/2, so either seed-edge sign gives a pivotal probability at least the mismatch. Core slice isoperimetry pays rho log active-core rarity once. This handles two arbitrary graph-controlled XOR/union events sharing a whole core; no physical-overlap orthogonality is assumed. Full U<=bI leaves give H<=max(K,4+2b)I; early leaves give K+2+2b only after keeping unrevealed-control influence. Dropping the cap breaks ownership on the exact m=r=1 diagonal edit of a dictator. The channel is already a general real log-Sobolev fragment; the new Boolean improvement is the owned core reserve. The normalized real psi16 zero-middle-layer edit is unchanged, with core energy1 below mask influence6435/4096, so ownership fails outside Boolean signs even under the cap. The remaining r/(r-log2 k) loss comes from the nonempty-control alphabet bound, exposed by a codimension-two subcube padded with irrelevant controls (H2,I1,alpha3/4). Four pointdefect fixtures fail complete U admission and remain unpaid by that particular certificate. Prior A066 v1 broad block-tree acceptance is narrowed; explicit author v2 prices singletons only and retains signed D_ref for blocks.\n')

external=[P,B/'BOARD.md',B/'claude/B14/STREAM_NOTES.md',*sources,
 A.parent/'A088/runs/20261012T024518Z-account05-A088-booleanity-referee/REPORT.md',
 A.parent/'A088/runs/20261012T024518Z-account05-A088-booleanity-referee/AUDIT.md',
 A.parent/'A088/runs/20261012T024518Z-account05-A088-booleanity-referee/CLAIMS.json',
 A.parent/'A088/runs/20261012T024518Z-account05-A088-booleanity-referee/out/A066_BLOCK_SCOPE_CERTIFICATE.json',
 A.parent/'A061/runs/20261013T215821Z-account05-A061-entropy-process/REPORT.md',
 A.parent/'A061/runs/20261013T215821Z-account05-A061-entropy-process/PADDING_EDIT_PROOF.md',
 A.parent/'A069/runs/20261012T043929Z-account05-A069-geometric-transfer/DERIVATION.md',
 old_path,A/'runs/20261012T004014Z-account05-A067-hypercontractive-refinement/DERIVATION.md']
external += [p.parent/'DERIVATION.md' for p in sources]
external += [sources[1].parent/'REPORT.md']
write('out/SOURCE_MANIFEST.json',{'created_at':now,'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in external]})
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in claims:
    if c is new:assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    elif c is old:
        original=next(x for x in read(old_path) if x['claim_id']==c['claim_id'])
        assert all(c[n]==original[n] for n in ['exact_statement','hypotheses','statement_sha256'])
    else:
        original=next(x for p in sources for x in read(p) if (x['claim_id'],x['version'])==(c['claim_id'],c['version']))
        assert all(c[n]==original[n] for n in ['exact_statement','hypotheses','statement_sha256','contributors','proof_dependencies'])
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='SAVE_RECEIPT.json']
files += [A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
write('out/SAVE_RECEIPT.json',{'created_at':now,'protocol_schema_verified':True,'progress_copy_byte_identical':True,
 'new_candidate_count':1,'independent_source_acceptances':4,'prior_scope_retractions':1,'math_assertions':244039,'all_executed_assertions_including_replays':244096,'all_executed_assertions_including_replays':244096,
 'reviewed_original_statements_and_hash_conventions_preserved':True,'new_claim_independently_reviewed':False,'remote_mirrors_verified':False,
 'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]})
receipt=read(R/'out/SAVE_RECEIPT.json')
for x in receipt['files']:assert sha(x['path'])==x['sha256'] and Path(x['path']).stat().st_size==x['bytes']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'complete':True,'claim_versions':len(claims),'source_acceptances':4,'local_receipt_hashes_verified':len(files),'new_candidate_count':1,'math_assertions':244039,'full_fei':'OPEN'}))
