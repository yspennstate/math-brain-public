from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def write(name,obj):
    (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=R/'out/EXACT_CHECK.json'
v=json.loads(check.read_text(encoding='utf-8')) if check.exists() else None
pilot=json.loads((R/'out/PILOT.json').read_text(encoding='utf-8'))
complete=bool(v and v['status']=='PASS')
validation=(f"Full check: {v['root_cases']} labeled roots plus four fixtures; {v['assertions']} exact assertions PASS in {v['seconds']:.6f}s." if complete else 'Full exact check pending; pilot passed.')
claim='A054-FIBER-ADMISSION-SINGLETON-AUDIT'
statement=('For every n>=2 and nonempty physical support U of mass p on the uniform cube, '
'f=1-2*1_U, and original actual connected-component labels, max over nonempty proper blocks A '
'of W_A/(|A|p) equals max_i Inf_i(f)/(2p). Thus the sufficient criterion W_A>=|A|p/2 '
'admits a proper block iff some Inf_i(f)>=p. Let h=H(X|L), X uniform on U, and '
'b=h-n+I(f)/(2p)>=0. Given the prior universal actual-block bound L_A<=4|A|p+a I_A, '
'a=2/ln2+4/(e ln2), a least-essential-dimension K-violation with K>a, '
'D=H-KI>0 and actual singleton child reserves S_i>=0 satisfies '
'h>=n-2n/(K-a)+b+(nD+sum_i S_i)/(2p(K-a)). At K>=4+a both sign sets '
'therefore have a component larger than 2^(n/2), and every proper block fails the sufficient '
'fiber criterion on either sign. This is a limitation of this admission rule, not a disproof of FEI.')
claims=[dict(claim_id=claim,version=1,exact_statement=statement,
hypotheses=['n>=2, finite uniform physical cube, nonempty support p>0; f is an actual Boolean sign',
'L is the original actual connected-component label; labels are retained after restriction',
'Entropy is in bits; Inf_i uses the usual Boolean flip probability',
'The critical corollary assumes K>a and least essential dimension among actual K-violations',
'For the critical corollary use the stated prior transfer/row upper bound; child deficits are actual and retained'],
statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['fleet03/A054'],
proof_source={'path':str(R/'FIBER_ADMISSION_AUDIT.md'),'sha256':sha(R/'FIBER_ADMISSION_AUDIT.md')},
proof_dependencies=[{'claim_id':'A054-OVERLAP-FIBER-PAYMENT-GIANT-COMPONENT','version':1,
'used_scope':'Only universal terminal-inclusive block bound (7)/(9); the admission identity itself is independent',
'acceptance':'AUTHOR_PROVED_SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW'}],review_records=[],
status='AUTHOR_PROOF_EXACT_CHECKS_PASS_PENDING_INDEPENDENT_REVIEW' if complete else 'AUTHOR_PROOF_VALIDATION_PENDING',
supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A051','A052','A055','A090','A094','claude/B11','B20'])]
write('CLAIMS.json',claims)
gap='G-R-SELECT'
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B11',packet_id='A054',
gap_id=gap,attempt_id='A054-stage17-fiber-admission-audit',
method='Audit and sharpen existing admission mechanism by physical conditional entropy, exact boundary counting, and same-bank critical summation; no new broad candidate.',
mathematical_delta='Exact singleton collapse of all-block fiber admission; restore nonnegative edge slack; improve both-sign critical giant-component threshold from 2^((n-1)/2) to >2^(n/2) with physical dual total correlation and actual child reserves.',
deliverable_status='COMPLETE_LOCAL' if complete else 'CHECKPOINT_VALIDATION_PENDING',
mathematical_status='WRITTEN_PROOF_WITH_EXACT_VALIDATION_FULL_FEI_OPEN' if complete else 'WRITTEN_PROOF_VALIDATION_PENDING_FULL_FEI_OPEN',
claim_versions_used=['A054-OVERLAP-FIBER-PAYMENT-GIANT-COMPONENT@1','A054-RAW-SIGN-BLOCK-TREE-TRANSFER@1'],
claims_created_or_changed=[claim+'@1'],source_artifacts=['FIBER_ADMISSION_AUDIT.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','code/check_admission.py','out/EXACT_CHECK.json'],
next_consumers=['A051','A052','A055','A090','A094','claude/B11','B20'],
next_action='Pay an original signed physical pair interaction beyond the singleton threshold from SAME D+S_pair, using actual child eligibility and mixed refund, with both complete terminals and old debit retained.',
stagnant_substantive_attempts=0,blockers=['Full FEI and universal signed-block selection remain OPEN.','New proof has no independent acceptance.','Lean compilation not admitted: memok WAIT at physical free 3.0GB versus required 4.0GB.','Supervisor copies and adoption not verified.'],packet_ids=['A054'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11 stage17 audits the existing controlled-excess payment mechanism.
For every n>=2, every actual nonempty cube support U, and every proper
nonempty physical block, entropy is in bits and f=1-2*1_U. Prove the
exact scope of sufficient fiber admission, keeping original component
labels and all actual child deficits. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision2026-10-11-execution-v2.
The requested campaign indices, plan and supplement, sources and four
context paper text versions were ingested and hashed by read_stage_sources.py;
relevant excerpts are preserved in out/SOURCE_EXCERPTS.json. They are
background, not additional proof premises. BOARD snapshot2026-10-22 22:38
UTC, B11 STREAM_NOTESv2, own STATUS and LEARNED, prior20261014T055856Z
REPORT/CLAIMS/OVERLAP_PAYMENT, prior20261014T025808Z RAW_SIGN_TRANSFER,
and the old exact helper were read. Prior20261021 stage folder contains
only a .final marker, so its missing REPORT was not treated as evidence.
Source encoding fallback is explicit: one or more context source texts
are not valid UTF-8; their original bytes are hashed, decoded as cp1252
for extraction, and never rewritten. The reader's initial strict UTF-8
failure was repaired before the manifest was emitted.

The prior controlled-excess theorem and transfer remain author-proved,
pending independent review. This stage audits their admission scope;
it does not open another broad candidate while review is pending.

# complete derivation or exact first unsupported line

FIBER_ADMISSION_AUDIT.md supplies the complete proof. Exact physical
boundary counting gives W_singleton=Inf_i/2 and
H(X_i|X_-i,L)=1-Inf_i/(2p). Conditioning reduces entropy, giving
2W_A<=I_A<=|A|max_i Inf_i. Singletons attain the maximum, so
max_A W_A/(|A|p)=max_i Inf_i/(2p), with no Fourier premise.
Thus the overlap/connected-support theorem can improve a prescribed
block but adds no existential admission beyond a high-influence singleton.
No previous inequality is refuted; its downstream scope is made exact.

The nonnegative physical dual total correlation b satisfies
h=H(X|L)=n-I/(2p)+b. Retaining R_A=I_A-2W_A restores the slack omitted
from the prior critical inequality. Summing the singleton inequalities
ONCE gives h>=n-2n/(K-a)+b+(nD+sum S_i)/(2p(K-a)). Hence at
K>=4+a every hypothetical minimal violation has a component larger
than2^(n/2) in BOTH signs. This replaces the prior2^((n-1)/2) threshold:
the change comes from a full singleton sum and the previously discarded
edge slack, not new numerical data or a changed FEI constant.

Every hypothetical critical source at this K also has maxInf below
both sign masses. The admission identity therefore proves that the
sufficient W threshold fails for EVERY proper block on either sign.
This is a conditional route obstruction; no actual FEI counterfamily
is claimed. First unsupported universal line: select and pay an actual
signed pair/block interaction beyond that sufficient threshold using
the SAME D+S_pair account, both complete child deficits and prior debit.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before pilot/full validation. Pilot20 roots
and four fixtures: {pilot['assertions']} exact assertions PASS in
{pilot['seconds']:.6f}s. {validation}
Commands: python -X utf8 code/check_admission.py --pilot, then without
--pilot, from this run's parent via the full relative script path.
The full domain is all276 labeled truth tables at n=1,2,3 (empty support
is skipped only where normalization by p is used), every proper block,
and four fixed n4/n5 overlap, connected, majority and parity fixtures.
No symmetry quotient or dimension escalation. The checker separately
counts physical edges, original-label fibers and singleton pair sizes.
Identities are canonical prime-log vectors over Fraction. Inequalities
use range-reduced32-term atanh bounds, an explicit tail, and outward
112-bit dyadics. The abstract proof supplies the all-dimensional result.

Checks target factor2, conditioning direction, p=1, point supports,
disconnected parity supports, overlap and zero influences. Arbitrary
parity labels on the full support give W_i=1 with Inf_i=0, confirming
that the actual-component/edge-constant hypothesis is necessary.
No critical source is inferred from a finite noncritical fixture.

Estimated checker memory100MB, wall limit55sec; no heavy search, GPU,
detached job, or dimension escalation. The mandatory fresh memok for
possible Lean compilation returned WAIT: physical free3.0GB, required4.0GB;
commit free24.8GB. No Lean compiler was launched. AdmissionAlgebra.lean
records only the intended normalized algebraic step and is UNCOMPILED;
there is no Lean certificate or assertion of trusted transitive axioms.
Rung: written proof with exact finite validation, pending independent review.

# proof dependencies and changed downstream conclusions

The admission identity and physical entropy/boundary identities are
self-contained. The critical corollary consumes only the prior
universal terminal-inclusive row/transfer bound L_A<=4|A|p+a I_A,
a=2/ln2+4/(e ln2), from A054-OVERLAP-FIBER-PAYMENT-GIANT-COMPONENT@1
and A054-RAW-SIGN-BLOCK-TREE-TRANSFER@1. Both source statuses remain
explicit. The exact terminal component cross term is never dropped.
No component is certified as a physical child. A051/A052/A055 should
stop trying to obtain universal admission from fiber entropy alone;
their signed interaction/child eligibility route needs extra information.

# one next mathematical action and independent reviewer

Derive one selected actual pair interaction bound from finite critical
maximality and physical child nonviolation, retaining A055 mixed refund
and the SAME D+S_pair bank. A051/A052/A055 are consumers; A090/A094
should independently reconstruct boundary normalization, exact maximum,
bank aggregation and the two-sign threshold. No messages were sent.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA are saved locally
with proof, code, frozen specification and exact outputs. STATUS is two
lines; WORKLOG and LEARNED updated under A054 only. out/RECEIPTS.json
checks exact protocol fields, statement hashes, byte lengths and the20MB
ceiling. Shared adoption, independent acceptance, mirrors and public
release are not inferred from local saves. Brain wake flagged stale
owner-model/state-of-mind notes; the warning was delivered in commentary.

# Universal bridge

This stage sharpens B11 critical block selection feeding C019 by proving
an exact ceiling on the existing fiber-interface admission mechanism:
all-block admission collapses to a singleton influence test, which
every hypothetical minimal high-K source fails. Retained edge slack
also raises both-sign giant-component exclusion by half a bit, to
strictly greater than2^(n/2), with physical correlation and SAME child
reserve terms explicit. Full FEI is still OPEN. NEXT is the signed pair
payment using actual child eligibility and mixed refund, because that
is additional information capable of crossing this precise ceiling;
another geometric admission census cannot do so.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A054 stage17: exact all-block fiber admission collapses to maxInf>=p; both-sign critical giants sharpened to >2^(n/2); '+('exact checks PASS; ' if complete else 'validation pending; ')+'FEI OPEN, review pending.\nNEXT: A051/A052/A055 pay actual signed pair beyond singleton threshold from SAME D+S_pair with mixed refund and both full terminals; A090/A094 review.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
if complete:
    for name,line in [('WORKLOG.md',f'\n{now} stage17: audited prior fiber route. Exact normalized maximum equals singleton maximum; retained edge slack improves critical two-sign component threshold to >2^(n/2). {validation} Lean held by memok; full FEI and signed selection open.\n'),('LEARNED.md','\nStage17 durable: For p>0,n>=2 and actual component labels, sup_proper W_A/(|A|p)=max_i Inf_i/(2p). Fiber admission iff maxInf>=p, so prescribed-block overlap gains are not a broader existential selection theorem. Physical dual total correlation b=H(X|L)-n+I/(2p)>=0 retains edge slack. Minimal K>a criticality gives h>=n-2n/(K-a)+b+(nD+sum S_i)/(2p(K-a)); at K>=4+a BOTH signs have a component >2^(n/2). Signed interactions, not the W sufficient threshold, must cross the remaining ceiling.\n')]:
        existing=(A/name).read_text(encoding='utf-8') if (A/name).exists() else ''
        if ('stage17: audited prior fiber route' if name=='WORKLOG.md' else 'Stage17 durable:') not in existing:
            with (A/name).open('a',encoding='utf-8') as f:f.write(line)
P=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=P['required_per_run'];expected=set(fields['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert all(set(c)==set(fields['claim_fields']) for c in claims)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('# '+s in report for s in fields['report_fields'])
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/RECEIPTS.json',{'status':'PASS','complete':complete,'protocol_fields':'EXACT','packet_delta':'BYTE_IDENTICAL','files':receipts,'independent_review':'PENDING','mirror':'UNVERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL' if complete else 'CHECKPOINT','validation':validation,'files':len(receipts),'protocol_fields':'EXACT'}))
