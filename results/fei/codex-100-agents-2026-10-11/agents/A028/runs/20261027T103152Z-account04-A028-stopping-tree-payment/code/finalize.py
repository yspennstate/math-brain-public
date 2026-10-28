import json,hashlib,datetime
from pathlib import Path
root=Path(__file__).resolve().parents[1]; home=root.parents[1]
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def load(p):return json.loads((root/p).read_text(encoding='utf-8'))
def save(p,obj):(root/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
chunks=[load(f'out/main_{a:03}_{a+100:03}.json') for a in range(0,400,100)]
assert all(x['status']=='PASS' and x['roots']==100 and x['seconds']<55 for x in chunks)
audit=load('out/audit.json');assert audit['status']=='PASS'
stats={'roots':sum(x['roots'] for x in chunks),'branch_checks':sum(x['queries'] for x in chunks),'main_assertions':sum(x['assertions'] for x in chunks),'audit_assertions':audit['assertions'],'total_assertions':sum(x['assertions'] for x in chunks)+audit['assertions'],'serial_seconds':sum(x['seconds'] for x in chunks),'negative_vacuum_fixtures':sum(x['negative_vacuum_coefficients'] for x in chunks)}
save('out/SUMMARY.json',stats)
lean=load('out/LEAN_RECEIPT.json')
lean_note='Core Lean receipt: '+str(lean.get('exit_code',lean.get('status')))+'. '+lean.get('stdout','')[:350]
if lean.get('exit_code')==0:
    formal='Only the named integer cancellation lemma is Lean-checked; the tensor, kernel and entropy theorem is an author-checked proof awaiting independent review.'
else:
    formal='Lean certification was not obtained. The saved receipt states the setup/admission/compiler outcome; the mathematical result is an author-checked proof awaiting independent review.'
statement=('For every finite disjoint tensor product of Boolean factors, every normalized covering reference q=sum_{r=1}^R w_r tensor_j nu_rj+c delta_empty with normalized nonnegative block laws, w_r>=0 and c real, and every finite adaptive physical-query tree using the local actual-phase pair kernel with the stated local ghost completion, inheritance followed by any number of finite positive cardinality tilts and vacuum calibrations preserves the same R nonnegative product components and one signed vacuum slot, provided the resulting reference is the explicitly defined normalized law. If each tilt matches actual total spectral influence, the exact ORIGINAL complete-CE ledger equals full expected terminal CE plus all weighted entropy decrements, physical kernel and outcome KL losses, and projection KL releases. All old commitments remain in the original account. The AND2 tensor source (P+delta_full)/2 has R=2 and CE<=5I/2 for even n>=4, so A096 interior-calibrated witnesses admit two product terms plus one signed vacuum term despite exponential individual-atom count. No arbitrary-core initial O(I) source, extreme-cardinality conditioning closure, nonlocal ghost closure, or universal stopping rule is asserted.')
claim={
 'claim_id':'A028-COMPACT-PRODUCT-REFERENCE-CLOSURE','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform Boolean disjoint tensor factors and finite adaptive trees; units bits.','Supplied covering normalized source has R nonnegative product components plus one possibly signed vacuum coefficient; reference probabilities themselves are nonnegative.','Local actual Boolean phase kernel, with the explicit block-local fair completion on zero local pairs.','Finite positive tilt x and positive nonempty normalizer; matching vacuum and influence is required for nonpositive CE debit. Constants reset directly to vacuum. Extreme-cardinality conditioning is excluded.','Both actual physical branches, reference branch normalizers, query contraction/outcome KL, all old commitments and complete terminal laws are retained.'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A028'],
 'proof_source':['DERIVATION.md sections1-6','out/SUMMARY.json','out/audit.json'],
 'proof_dependencies':['Finite stochastic-kernel conditional KL chain rule and Gibbs inequality, rederived in DERIVATION4.','A096 stage22 DERIVATION2 finite-positive information projection, reconstructed in DERIVATION3; section3 provides the atom-count comparison only.','Exact physical Boolean Walsh restriction and disjoint tensor factorization.'],
 'review_records':[{'reviewer':'A028','kind':'same-author separate implementation, not independent peer acceptance','checks':stats,'formal_scope':formal}],
 'status':'SCOPED_AUTHOR_PROOF_REVIEW_PENDING','supersedes':[],'refutes':[],
 'first_unproved_line':'Provide a useful arbitrary-core bounded-size physical factor/source decomposition with ORIGINAL complete CE<=C I, or a required entropy-decaying stopping rule paid from the same genuinely unused original account.',
 'next_consumers':['A096','A029','A050','A097','A094']}
save('CLAIMS.json',[claim])
next_action='A096/A029/A094 reconstruct the local ghost/finite-tilt closure and full query ledger, then test an arbitrary-core source decomposition at ORIGINAL O(I) price; another optional calibration cannot supply it.'
progress={'protocol_revision':protocol['revision'],'run_id':root.name,'stream':'B06','packet_id':'A028','gap_id':'C019-ORIGINAL-SOURCE-ADMISSION','attempt_id':'A028-stage22-structured-residual-inheritance','method':'Disjoint tensor local physical kernels and finite exponential tilts; exact Fraction reconstruction and independent prime-log ledger audit','mathematical_delta':'Replaces exponential individual-atom storage on the A096 Boolean witness by TWO product components plus one signed vacuum slot, hereditary through every finite allowed adaptive history. General supplied R-product references preserve R. Universal initial payment unchanged.','deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'SCOPED_AUTHOR_PROOF; FULL_FEI_OPEN','claim_versions_used':['A096-stage22 DERIVATION2 finite-positive projection; immutable source receipt','A029-stage21 REPORT section6 arbitrary-core calibrated-terminal reduction, scope guard only'],'claims_created_or_changed':['A028-COMPACT-PRODUCT-REFERENCE-CLOSURE@1'],'source_artifacts':['DERIVATION.md','out/SOURCE_RECEIPTS.json','out/SOURCE_EXCERPTS.json','out/SUMMARY.json','out/audit.json','out/LEAN_RECEIPT.json'],'next_consumers':['A096','A029','A050','A097','A094'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary-core original O(I) complete reference and necessary useful stopping certificate remain open.','Independent peer review and supervisor mirror verification pending.','External working-checklist call returned RuntimeError(checklist lock held too long); no shared lock changed.'],'packet_ids':['A028']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A028 stage22: compact inheritance of moment-calibrated sources

## exact target, quantifiers, hypotheses and units

For every finite tensor Boolean factorization and every supplied R-component product reference with one signed vacuum slot, prove hereditary compactness under local physical inheritance and finite positive vacuum/influence calibration. Prove full expected path cost plus full terminal CE is at most the ORIGINAL supplied complete CE. The actual AND2 tensor source has original rate5/2. Units bits. This is a scoped closure result, not universal stopping-tree payment. CLAIMS gives every hypothesis.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, fresh BOARD/B06 v2, own prior STATUS/WORKLOG/LEARNED and preceding REPORT, A02920261026T213208Z REPORT (especially calibrated-terminal hardness section6), and A09620261027T055827Z REPORT/DERIVATION1-4/CLAIMS. The current intake pins24 campaign/supplement/paper/context files with explicit decoding and selected locators in out/SOURCE_RECEIPTS and SOURCE_EXCERPTS. Byte intake and inherited baseline do not constitute a new full-paper audit. The new proof is elementary finite tensor/kernel algebra; no external literature claim or internet fact is a premise. Brain recall returned coordinate-entropy and Boolean-realizability guard cards, not a theorem proving this closure. Wake reported stale personalization and incomplete recent dream; current task/source files govern, and the alert was surfaced.

## complete derivation or exact first unsupported line

DERIVATION1-6 gives the proof. The pair kernel of a tensor Boolean function acts on the queried block; on ghost pairs the local completion is part of the hypothesis. Every product term stays a product through the actual source branch normalizer, and delta_empty never leaves empty. A cardinality tilt factorizes across blocks. Vacuum calibration changes only its scalar correction, which can be negative although the reference remains a nonnegative law. Thus R stays fixed for any finite adaptive sequence. The AND2 tensor moment law is explicitly TWO product terms plus one vacuum term (formula5), instead of the2^n-n nonnegative atom witnesses in the narrower A096 representation. This changes the representation interface; it does not refute A096.

Exact accounting is CE(root)=E CE(leaf)+sum reach*(DeltaH+kernel_KL+outcome_KL)+sum reach*projection_KL. The old bookings and both terminals remain. Matching influence is used precisely for projection KL to equal CE release; arbitrary rational tilts in the checker also verify the exact moment-mismatch correction. Finite x>0 is used in each block normalizer. Extreme-level conditioning is excluded; no divergent signed-coefficient limit is used. A giant arbitrary-core block makes the representation claim vacuous, so the first unsupported universal line is ORIGINAL complete CE<=C I with a useful bounded-size decomposition or a necessary entropy-decaying paid stopping rule.

## executed validation with domain, arithmetic, commands and outputs

Frozen v1 spec, bounded-cache v2 amendment, serial-partition v3 amendment and independent-audit spec precede their corresponding jobs. The v1 pilot passed10458 assertions. The two unpartitioned attempts hit their55-second guards at assertions145579 and327619; neither is a completed census. The final four SERIAL jobs cover the unchanged400 labelled factor representations, all first physical queries and both branches, another calibration and every second physical query. Each completed in under55seconds. Main totals: {stats['branch_checks']} branch checks and {stats['main_assertions']} assertions. Constants, singleton blocks, zero Fourier pairs, zero component branch mass and {stats['negative_vacuum_fixtures']} negative-vacuum fixtures are covered. Exact inverse-tilt fixtures reconstruct P and therefore match both moments. Fixed formula witnesses use n4,6,8; no automatic dimension escalation.

Separate code/audit.py imports no main helper:48 direct-character profiles,192 physical queries,{audit['assertions']} exact prime-log assertions, with a real omitted-vacuum fault control. Main plus separate audit total {stats['total_assertions']} assertions; pilot and failed partial runs are not added. These are same-author implementations, not peer review. Commands: python -X utf8 code/check.py pilot; code/check.py full 0 100 (then100 200,200 300,300 400 serially); code/audit.py; code/intake.py; code/lean_probe.py; code/finalize.py. Arithmetic is Fraction, integer Walsh and prime-log coefficients, with no floating probability/sign certificate. The all-dimensional claim is the written finite algebra, not extrapolation.

Estimated100MB maximum for own Python jobs; observed peaks unmeasured. Fresh memok passed before the small core Lean attempt; no Mathlib process, GPU, detached worker, remote compute, workload stop or throttling. Initial Lean submission was rejected before compiler launch because Windows newline translation changed the reviewed bytes; the repair hashes the exact saved bytes and writes explicit LF. {formal} Full receipt: out/LEAN_RECEIPT.json. No full-theorem Lean certification is claimed.

## proof dependencies and changed downstream conclusions

A096's finite-positive projection is independently reconstructed at the displayed scope, and its narrower atom-count conclusion remains intact. A029's arbitrary-core calibrated-terminal guard is retained: compactness or matched moments alone do not certify leaves. The new lemma repairs representation growth in the existing supplied-reference mechanism; it opens no new universal candidate and gives zero universal FEI constant improvement. A094's full query-loss objection is explicitly respected by equation4. Independent reconstruction is requested from A096/A029/A094 through the saved source; no external message or canonical registry mutation occurred.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

All four exact-field protocol files, derivation, frozen specs, code, failed-attempt records and exact outputs are saved inside A028. STATUS has two current lines; WORKLOG and LEARNED append durable facts. code/finalize.py checks field equality, statement hash,400-root coverage, PASS outputs, compatibility-copy equality and every file<20MB, then writes out/PERSISTENCE.json with readback hashes. Supervisor publication, mirror verification and peer acceptance remain unverified. The external working-checklist lock timed out; no lock was removed. No git, mail, brain research mutation, other-agent write, trading path or deletion was used.

Universal bridge: C019 stopping-tree payment gains a compact structured residual for C024 physical history transfer: the A096 exponential atom witness has an O(n)-entry representation with two product components and one signed vacuum slot through all finite LOCAL physical histories with finite interior calibrations, while all query KL and terminal costs stay in the ORIGINAL account. Universal source admission advances by zero: the arbitrary-core O(I) complete source and useful entropy-decaying stopping certificate remain unpaid. NEXT addresses that supplier/decomposition directly; another optional floor, atom enumeration or fixed calibrated terminal class cannot pay arbitrary-core entropy.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(home/'STATUS.md').write_text('STATE: A028 stage22 saved: R product components plus ONE signed vacuum slot hereditary under LOCAL queries/finite moment tilts;470338 exact assertions PASS; peer review pending; FEI OPEN.\nNEXT: A096/A029/A094 review compact closure/full query ledger; fund ORIGINAL arbitrary-core O(I) useful source or necessary entropy-decaying stopping rule, retaining old bills/BOTH terminals.\n',encoding='utf-8')
with (home/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — stage22: compact product-reference physical inheritance and finite vacuum/influence tilt closure, R unchanged plus one signed vacuum slot. A096 AND2 witness compresses exponential atoms to O(n) entries at original rate5/2. Final400 roots/55104 branch checks/468752 assertions plus separate1586 prime-log assertions PASS. Two earlier55sec partial attempts excluded; bounded cache and serial100-root jobs completed. {formal} Original arbitrary-core source/stopping gap remains OPEN; saved {root.name}.\n')
with (home/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Stage22: compact product references\nFor a physical tensor Boolean factorization, choose the actual-phase pair kernel with BLOCK-LOCAL ghost completion. A supplied q=sum_r w_r tensor_j nu_rj+c delta_empty, w_r>=0,c real, remains in the SAME R-product-plus-vacuum class under every query and finite positive cardinality tilt/vacuum calibration. Only the vacuum coefficient can be signed; q itself stays nonnegative. Tilts multiply each block law by x^size; the new vacuum correction merges into the same slot. Finite positive x is essential to this proof; extreme-cardinality conditioning is not claimed. For AND2 tensors, (P+delta_full)/2 has original CE<=5I/2 and R2, while the A096 calibrated witness costs2^n-n atoms in the narrower true-law-plus-positive-atoms interface. Richer product structure removes that representation cost without supplying arbitrary-core entropy payment. Exact original ledger: CEroot=E CEleaf+sum(DeltaH+kernelKL+outcomeKL)+sum projectionKL. All old bills/both terminals remain. Main470338 includes separate1586 direct prime-log assertions; failed partial attempts and pilot excluded.\n')
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
assert set(progress)==set(x.split(' (')[0] for x in required['progress_fields'])
assert load('PROGRESS.json')==load('PACKET_DELTA.json')
assert all(x in report for x in required['report_fields'])
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        b=p.read_bytes();assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/PERSISTENCE.json',{'status':'PASS','at':now,'stats':stats,'files':receipts,'formal_scope':formal,'mirror_verified':False,'peer_review_verified':False})
print(json.dumps({'status':'PASS','stats':stats,'formal_scope':formal,'saved':str(root)}))
