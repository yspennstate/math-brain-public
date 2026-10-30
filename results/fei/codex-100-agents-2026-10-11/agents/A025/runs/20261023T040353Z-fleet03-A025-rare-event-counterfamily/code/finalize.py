"""Persist stage package after exact outputs have passed; append rolling once."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]; OUT=ROOT/'out'
BASE=Path('~/brain_workers/FEI100_20261011')
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def js(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=js(PROTO); run=ROOT.name
outputs={name:js(OUT/(name+'.json')) for name in ('pilot','main','targeted','REPLAY','SCALAR','FIXTURE')}
assert all(x['status']=='PASS' for x in outputs.values())
total=sum(x['assertions'] for x in outputs.values())
mainchecks=sum(outputs[n]['assertions'] for n in ('pilot','main','targeted'))
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B05/STREAM_NOTES.md']
for ar,files in [('A022/runs/20261023T012352Z-fleet03-A022-one-point-surgery',('REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/exact.py')),
                 ('A028/runs/20261023T023055Z-fleet03-A028-stopping-tree-payment',('REPORT.md','out/DERIVATION.md')),
                 ('A025/runs/20261022T231646Z-fleet03-A025-rare-event-counterfamily',('REPORT.md','CLAIMS.json','out/HELPER_PROVENANCE.json'))]:
    sources += [BASE/'agents'/ar/f for f in files]
receipts=[]
for p in sources:
    raw=p.read_bytes(); text=raw.decode('utf-8-sig')
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'scope':'current stage intake/explicit proof interface; prior full baseline is not newly re-reviewed'})
save(OUT/'SOURCE_RECEIPTS.json',receipts)
a022=js(BASE/'agents/A022/runs/20261023T012352Z-fleet03-A022-one-point-surgery/CLAIMS.json')
assert any(c['claim_id']=='A022-ODDFACE-SURGERY-GAP-LEDGER' and c['version']==7 for c in a022)
statement=('Preserve A025@3 local-price obstruction without scope expansion. New continuation: for every t>=2, vertex v, arbitrary independent Boolean controller a, and A022@7 paid block-first uniform-depth data prefix d<=3floor(t/2)+2 of F=b(x)(1-2*1[x=v]*(1-a)/2), b the t-fold three-bit point-defect tensor, use original delta=8^-t and prescribed complete q_h tensor [(1-delta)point_empty+delta P_(a|e)] after any finite adaptive controller tree common to ALL data siblings. With original old U in[0,t/64] and full controller entropy earmark spent by its exact source telescope, the actual averaged remaining bank 4I_data+delta H(a|e)-CE-U is at least its original paid value13t/576. Its gain is exactly the original overhead Jensen release; no new source admission or positive-part clipping occurs. Every terminal KL and actual phase erasure/outcome refund is retained. Scalar reason: G_delta(s)=H((1-delta)point_empty+delta P_a)-delta H(a) is concave in s=Ea for0<delta<=1/8. The actual r-bit one-point controllers for EVERY r>=5 disprove extension to delta=1/2. No arbitrary data-dependent controller policy, arbitrary controller entropy influence supplier, FEI constant or universal-route refutation is asserted.')
claim={
 'claim_id':'A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO','version':4,
 'exact_statement':statement,
 'hypotheses':['All finite uniform Boolean cubes; bits for entropy','Original t>=2, delta=8^-t, actual point-surgery family and actual physical reaches','A022@7 source admission is consumed at its stated pending-review scope','Data references fixed during common adaptive controller tree; no data-cylinder-dependent query decisions','Original U stays booked; arbitrary source controller entropy is explicitly supplied, not influence-priced'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A025'], 'proof_source':['PROOF.md Sections1--4','code/check.py','code/independent.py'],
 'proof_dependencies':[{'claim_id':'A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO','version':3,'scope':'inherited local obstruction and stage7 ledger unchanged; not needed for new scalar proof','acceptance':'author proof pending independent review'},
                       {'claim_id':'A022-ODDFACE-SURGERY-GAP-LEDGER','version':7,'scope':'paid data prefix13t/576; references and actual-family formulas PROOF1--6','acceptance':'author proof pending independent review; conditional source admission for this numerical corollary'}],
 'review_records':[{'reviewer':'A025 independent implementation','scope':'author second reconstruction only, NOT independent-person acceptance','result':'PASS '+str(outputs['REPLAY']['assertions'])+' replay and '+str(outputs['SCALAR']['assertions'])+' scalar assertions'}],
 'status':'AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW',
 'supersedes':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@3 (extension only)'],
 'refutes':[{'statement':'G_delta is concave in controller mean for ALL activation densities','scope':'false extension only','witness':'out/SCALAR.json, actual32-entry point controller at delta1/2'}],
 'first_unproved_line':'A controller query chosen from the DATA-cylinder outcome admits its prescribed reference from the SAME diminished ancestor bank; arbitrary source-controller entropy is not influence-priced.',
 'next_consumers':['A021','A022','A028','A029','A087','A094']}
save(ROOT/'CLAIMS.json',[claim])
nextaction='After a paid nonflat data prefix, query one actual controller bit ONLY on the active data cylinder; price its inherited-to-prescribed conversion from SAME13t/576 with original Q/delta, old U, source-entropy spend and both full terminals retained. A022/A028/A087/A094 review.'
progress={
 'protocol_revision':protocol['revision'],'run_id':run,'stream':'B05','packet_id':'A025',
 'gap_id':'A025-INHERITED-REFERENCE-CONTROL-CONVERSION','attempt_id':'common-controller-after-paid-data-1',
 'method':'Exact overhead concavity plus full physical phase KL chain; consume A022 paid nonflat prefix; two independent author implementations',
 'mathematical_delta':'Actual controller-reference conversion now paid for ANY common adaptive controller-only continuation after the paid data prefix; SAME13t/576 retained. Dense activation extension has an exact Boolean counterexample.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS', 'mathematical_status':'SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@3','A022-ODDFACE-SURGERY-GAP-LEDGER@7'],
 'claims_created_or_changed':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@4'],
 'source_artifacts':[str(p) for p in sources], 'next_consumers':claim['next_consumers'],'next_action':nextaction,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent-person reconstruction pending','Data-cylinder-dependent controller continuation unpaid','Arbitrary supplied controller entropy remains unpriced by influence','Supervisor copying/remote mirrors unverified; no formal compiler run'],
 'packet_ids':['A025']}
save(ROOT/'PROGRESS.json',progress); (ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report=f'''# A025 stage8: control-reference conversion after paid nonflat data history

## exact target, quantifiers, hypotheses and units

For every t>=2 and vertex v, take A022@7's actual point surgery of the t-fold three-bit point-defect tensor with arbitrary independent controller a. After ANY paid fixed block-first uniform-depth data prefix d<=3floor(t/2)+2, price the prescribed controller-reference conversion after one physical controller bit and every finite adaptive controller-only continuation COMMON to all data siblings. Entropies are bits. The SAME actual bank4I_data+delta H(a_current)-CE-U retains at least13t/576, with original delta=8^-t, old U<=t/64, complete positive data references, both full terminal KLs, and the exact spend of original controller entropy. This closes that continuation, not arbitrary mixed histories or FEI. Local A025 price obstructions retain exactly their previous scope.

## sources actually read, revisions and theorem locators

Current BOARD, B05 STREAM_NOTES v2 and own STATUS were read at intake. Lead's original tower task was already finished in earlier stages; current protocol dispatch consumes the useful new A022 dependency. A022 stage8 run20261023T012352Z REPORT, PROOF1--7 and both helper files provide actual nonflat family, q/R references, signed history, and13t/576 admission. A028 stage7 run20261023T023055Z REPORT and out/DERIVATION give the actual-phase inheritance interface and warning about raw reset refunds. Both are author proofs at their stated review scope; no whole-chain acceptance is inferred. Own stage7 REPORT/CLAIMS and protocol v2 are the prior baseline. Source bytes are pinned in out/SOURCE_RECEIPTS.json; helper copies have pre-pilot provenance. Full earlier campaign/paper baseline was read in prior stages and is not claimed freshly re-reviewed. No new paper or web premise is used. One read-only math recall returned generic entropy/KL cards and supplied no missing FEI premise.

Brain self-care remains degraded/unverified: the owner model was about90h old and state-of-mind about75h old at intake. Those stale personal-context sources were not relied upon for mathematical premises or authority; their personalization and continuity remain affected. Current campaign files govern this stage. User's2026-10-23 14:49UTC endpoint supersedes the protocol's obsolete initial clock; no scheduling is changed.

## complete derivation or exact first unsupported line

PROOF.md1--4 is the complete all-parameter derivation. R_a=(1-delta)point_empty+delta P_a and its overhead G_delta=H(R_a)-delta H(a) depends only on s=Ea. Its second derivative is -(2delta/ln2)[ln(1+u)-2u/(1+u)], u=(1-delta)/(delta s^2)>=7. Therefore G is concave for0<delta<=1/8, including continuity across s=0. The Jensen release gamma>=0 telescopes from the ORIGINAL root overhead. No numerical search supplies that all-dimensional passage.

Across ALL original data siblings, the actual controller marginal is R_a exactly, while data CE and remaining physical data influence are affine in alpha. Thus the actual bank gain after a common controller query is EXACTLY gamma, retaining U and all inactive sibling costs. The original source-controller entropy is spent by its own telescope: spent+delta expected H(a_leaf)=delta H(a_root). It is never added again. The conclusion covers an arbitrary adaptive controller tree based on earlier CONTROL outcomes, but its policy must be identical across DATA siblings.

The target reference is a stated conversion, not misidentified as physical inheritance. The actual phase pair channel retains all off-support mass and its outcome normalizers. It gives D_parent=E+O+average D_inherited. Raw signed reset kappa therefore has net cost sigma=kappa-E-O=average D_target-D_parent. Here sigma=DeltaH_F-delta DeltaH_a-gamma. Both complete child KLs, E and O remain in the history. No bound on separately clipped positive reset costs is claimed. The extended exact signed history uses delta DeltaH_a-DeltaH_F at controller queries and preserves the full original source earmark.

For EVERY r>=5, an actual r-bit point-defect controller at delta1/2 has parent mean1-2^(1-r) and child means1-2^(2-r),1; its Jensen release is rigorously NEGATIVE. The all-r proof uses strict convexity on[7/8,1]; its first actual witness has32 entries. It refutes only the unrestricted-density concavity/payment extension. It is not an FEI counterfamily or a refutation of a universal route. The first unsupported universal line is a controller-query/stopping policy depending on the DATA-cylinder label, paid from the already diminished same bank. Pricing arbitrary supplied controller entropy by influence also remains open.

## executed validation with domain, arithmetic, commands and outputs

Frozen SEARCH_SPEC and REPLAY_SPEC precede their jobs. Pilot384 query cases/{outputs['pilot']['assertions']} exact assertions PASS in{outputs['pilot']['seconds']:.4f}s. Pilot projection exceeded the original main120s cap; SEARCH_REVISION changes only that cap to600s BEFORE main execution. Main6144 physical query cases/{outputs['main']['assertions']} assertions PASS in{outputs['main']['seconds']:.4f}s: all64 six-bit vertices, ALL16 Boolean two-bit controllers, both physical controller coordinates, data depths1,2,5, and every reached data/control child. No symmetry reduction. The initial t=3 physical-phase job was interrupted after stalling in trial factorization; it did NOT PASS. VALIDATION_REVISION records the replacement before execution. Bounded targeted t=3 omits that physical-phase audit and instead verifies complete prescribed CE/KL and bank identities by GCD-log arithmetic. Targeted t=3, vertices0,511, all16 controllers, both coordinates, depths1,2,5,6:256 query cases/{outputs['targeted']['assertions']} assertions PASS in{outputs['targeted']['seconds']:.4f}s. Production uses integer FWHT, Fraction laws, exact prime-log equalities and outward40-term atanh rational bounds with proved geometric tails.

Independent.py imports NO production/helper code: direct character sums, physical Boolean edge counts, separate complete-reference construction, GCD-refined exact rational-log equalities and48-term rational log enclosures. Pairwise coprime integer log bases certify identities without factoring large normalizers. On48 declared fixtures with three-bit zero/point/majority/nonmonotone controls, vertices0,63, depths1,2,5, complete and outcome-dependent stopped common-controller trees, it checks{outputs['REPLAY']['controller_states']} controller states/{outputs['REPLAY']['assertions']} exact assertions in{outputs['REPLAY']['seconds']:.4f}s. It retains every actual phase branch refund and terminal debt through the full stopped tree. Scalar replay verifies867 frozen Jensen pairs plus six actual dense Boolean failures r=5..10, {outputs['SCALAR']['assertions']} assertions in{outputs['SCALAR']['seconds']:.4f}s. A declared two-query receipt stores eight raw reset/refund rows and phase branch normalizers in out/FIXTURE.json, {outputs['FIXTURE']['assertions']} assertions PASS. Total{total} exact author assertions. Different implementations are not independent-person review.

Commands: python -X utf8 code/check.py pilot; code/check.py main; code/targeted.py; code/independent.py replay; code/independent.py scalar; code/fixture_gcd.py. Jobs were sequential; frozen estimates160MB production/100MB independent, below300MB, peak unmeasured. The original outer-loop runtime check failed to bound time inside trial factorization; no completed-pass claim is made for that attempt. Replacement arithmetic removes that bottleneck. No memok-gated large job, GPU, detached work, automatic dimension growth or formal compiler run was started. Shared compute snapshot at intake reported physical-memory pressure; existing work was not changed. Failure axes include zero/full activation, zero spectrum rows, off-support reference mass, original reaches/delta/Q, old U, BOTH target and inherited child KLs, phase outcome normalization, signed negative costs, all controller outcomes and rare-density boundary. No formal theorem or infinite-dimensional exhaustiveness is claimed from the finite checks.

## proof dependencies and changed downstream conclusions

The existing narrow A025 claim advances v3 to v4; its older local counterfamily/no-go scope is unchanged. New scalar concavity and signed physical continuation are self-contained. The numerical13t/576 corollary consumes A022@7's pending source admission, rather than granting a new descendant bank. A028's actual reset interface is reconstructed with standard KL chain rule, not promoted to whole-bundle acceptance. This closes A022's one-common-controller-query target and extends it to common adaptive controller trees while preserving full source entropy and actual debts. A022/A028/A029 can use that continuation; A087/A094 should challenge source ownership and data-dependent policies. FEI remains OPEN, and arbitrary controller entropy is still explicitly supplied.

## one next mathematical action and independent reviewer

{nextaction} This changes the unsupported synchronization hypothesis rather than extending another identical controller-only family. Independent-person acceptance is requested through saved consumer fields only; no messages or accepted reviews are asserted.

## actual persistence receipts or precise save blocker

REPORT, PROOF, CLAIMS, PROGRESS and identical PACKET_DELTA, two frozen specs and pilot-based runtime revision, exact code and outputs are local in the assigned A025 run. STATUS has exactly two lines; WORKLOG and LEARNED append this stage. out/ARTIFACT_CHECK records schema, statement hash, byte-identical compatibility and file hashes/size limits. No campaign registry, other agent folder, research brain, git state or external service was modified. Administrative checklist follows the existing hook exception. Independent review, supervisor copying and remote mirrors remain unverified. What I did: proved and exactly checked the stated control-reference continuation. What I stopped: only my stalled targeted check to enforce its frozen runtime cap; no other live work. What remains running: none owned by this stage after completion.

Universal bridge: This moves C024 history transfer toward C019 by paying an ACTUAL prescribed controller-reference conversion after A022's paid nonflat DATA prefix, with the SAME remaining13t/576, old U, full original controller entropy spend and every terminal KL intact. Concavity makes the controller overhead release rather than consume reserve through any common adaptive controller tree. The unpaid step is a DATA-cylinder-dependent controller decision, alongside the arbitrary influence-priced controller/source supplier. NEXT attacks precisely that conditional transaction with an existing original account; repeating longer common-controller histories would not address the universal bridge.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8',newline='')
state=f'STATE: A025 stage8: actual CONTROL conversion after paid nonflat DATA paid for all common adaptive controller trees; SAME13t/576+old U/full KL retained;{total} exact assertions PASS; review pending, FEI OPEN.\nNEXT: Query one controller bit ONLY on active data cylinder; retain SAME original Q/delta/13t576, old U, spent source entropy and BOTH full terminals; A022/A028/A087/A094 review.\n'
(AGENT/'STATUS.md').write_text(state,encoding='utf-8',newline='')
marker='20261023T040353Z'
for name,entry in [('WORKLOG.md',f'\n2026-10-23 [{marker}] Consumed A022@7 paid nonflat prefix. Proved rare reference overhead concavity, checked actual phase reset with both KLs, and preserved SAME13t/576 through arbitrary common adaptive controller tree. {total} exact author assertions PASS; dense delta1/2 Boolean witness refutes only extension. Controller entropy remains supplied; data-dependent policy open. No new universal candidate or independent acceptance.\n'),
                   ('LEARNED.md',f'\n2026-10-23 [{marker}] For0<delta<=1/8, G_delta(s)=H((1-delta)empty+delta P_a)-delta H(a) is concave in s=Ea: Gsecond=-(2delta/ln2)[ln(1+u)-2u/(1+u)]<0,u>=7. Hence original controller-reference overhead contracts under common controller conditioning across all data siblings. Actual signed reset is sigma=kappa-E-O; keep BOTH KLs and spend original delta H(a) once. Dense delta1/2 fails at mean15/16, children7/8,1. This is a prescribed reference continuation, not an arbitrary-controller FEI bound.\n')]:
    p=AGENT/name; old=p.read_text(encoding='utf-8-sig') if p.exists() else ''
    if marker not in old: p.write_text(old+entry,encoding='utf-8',newline='')
rf=protocol['required_per_run']; requiredprogress={f.split(' (')[0] for f in rf['progress_fields']}
assert set(progress)==requiredprogress
assert set(claim)==set(rf['claim_fields'])
assert all('## '+x in report for x in rf['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
assert sha(ROOT/'PACKET_DELTA.json')==sha(ROOT/'PROGRESS.json')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
manifest=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='ARTIFACT_CHECK.json':
        assert p.stat().st_size<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
save(OUT/'ARTIFACT_CHECK.json',{'status':'PASS','protocol_revision':protocol['revision'],'exact_schema':True,'statement_sha256':claim['statement_sha256'],'identical_packet_delta':True,'files':manifest,'total_assertions':total,'formal_verified':False,'independent_person_review':'PENDING','supervisor_copying':'UNVERIFIED'})
print(json.dumps({'status':'PASS','files':len(manifest),'assertions':total,'run':str(ROOT)}))
