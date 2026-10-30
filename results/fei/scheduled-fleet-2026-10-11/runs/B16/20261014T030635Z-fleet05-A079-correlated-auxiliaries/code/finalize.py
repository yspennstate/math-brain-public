import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parent.parent;BASE=AGENT.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=json.loads((ROOT/'out'/'validation.json').read_text());p=json.loads((ROOT/'out'/'pilot_validation.json').read_text())
assert v['status']=='PASS' and v['final'] and p['seconds']<60
total=sum(n for k,n in v['cases'].items() if not k.endswith('_admitted'));assert total==90540
oldrun=AGENT/'runs'/'20261014T000722Z-fleet05-A079-correlated-auxiliaries'
a32=BASE/'agents'/'A032'/'runs'/'20261014T015128Z-fleet05-A032-boolean-phase-realizability'
a34=BASE/'agents'/'A034'/'runs'/'20261014T025347Z-fleet05-A034-phase-energy-transfer'
a68=BASE/'agents'/'A068'/'runs'/'20261014T023317Z-fleet05-A068-antichain-beyond-one-order'
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
sources=[protocol,BASE/'BOARD.md',BASE/'claude'/'B16'/'STREAM_NOTES.md',oldrun/'DERIVATION.md',oldrun/'CLAIMS.json',a32/'REPORT.md',a32/'CLAIMS.json',a32/'QUADRATIC_OBSTRUCTION.md',a32/'out'/'phase_anf.json',a32/'code'/'phase_anf.py',a34/'REPORT.md',a34/'CLAIMS.json',a68/'REPORT.md']
manifest=[{'path':str(s),'sha256':sha(s)} for s in sources];save(ROOT/'out'/'SOURCE_MANIFEST.json',manifest)
old=json.loads((oldrun/'CLAIMS.json').read_text())[0]
assert old['statement_sha256']=='938777233a0b7fffcfbb415d033d99989abf54fea66bda2d6e32cc6eda6f12ef'
assert sha(oldrun/'DERIVATION.md')=='4375d67f0fd79bd6cc987a94eeff97ad2ada7f92c70a62f1ab8149a35eef3b09'
review={'reviewer':'A068','verdict':'HOLDS_AT_STATED_SCOPE','source':{'path':str(a68/'REPORT.md'),'sha256':sha(a68/'REPORT.md'),'locator':'Section 5: independent reconstruction; proof dependencies and changed downstream conclusions'},'method':'All-dimensional affine-support/rank reconstruction plus independent direct integer Walsh and rational prime-log verification; no author code import or substantive repair','registry_adoption':'NOT_VERIFIED'}
old['review_records'].append(review);old['status']='INDEPENDENTLY_RECONSTRUCTED_PENDING_REGISTRY_ADOPTION'
save(ROOT/'out'/'A068_REVIEW_RECEIPT.json',{'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256'],'proof_sha256':sha(oldrun/'DERIVATION.md'),'review_record':review})
statement='For every Boolean F on two independent uniform physical address bits X and arbitrarily many uniform data bits Y, if each nonzero conditional squared Fourier row is a coordinate-product law with at most one nonfair varying coordinate, arbitrary nonfair marginal, arbitrary Fourier signs and arbitrary fixed frequency coordinates, then H(S_Y|S_X)<=[3/2+(5/2)h2(1/10)]I_Y(F), sharply, and H(F)<=[6+2log2(65/64)]I(F). If all nonfair primitive magnitude ratios belong to {2,3,4}, the sharper bound H(F)<=[10-3log2(3)]I(F) holds. Universally for every two-address Boolean F, H(w)<=sum_J w_J H_{1/2}(p_J)+2I_X(F); hence full H(F)<=sum_J w_J[H(p_J)+H_{1/2}(p_J)]+2I_X(F). For integer height-two rows of the fixed-ratio family, ratio2 requires at least one other fair coordinate, ratio4 requires at least three, and weights are <=5/8 for ratio2 or3 and <=17/32 for ratio4. Quadratic branch signs admit exactly the equal/overlapping/disjoint affine inverse-support amplitude classification in DERIVATION.md; the low-dimensional exclusion holds for arbitrary signs.'
new={'claim_id':'A079-CUBIC-ROW-CONDITIONAL-PAYMENT','version':1,'exact_statement':statement,'hypotheses':['Normalized Walsh; entropy in bits; all influence in the original physical coordinates','Exactly two address bits and actual Boolean signs; nonzero row h_J=2 E_X F chi_J','Conditional spectra are coordinate products with at most one nonfair varying coordinate; arbitrary marginal and Fourier signs; the sharper joint bound assumes ratios2,3,4','Inverse-support classification alone assumes quadratic Fourier-sign branches; universal row ledger assumes neither product spectra nor phase degree'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A079'],'proof_source':{'path':str(ROOT/'DERIVATION.md'),'sha256':sha(ROOT/'DERIVATION.md')},'proof_dependencies':[],'review_records':[],'status':'NARROW_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A034','A068','A088','A092','A094','B16','B20']}
save(ROOT/'CLAIMS.json',[new,old])
next_action='Derive a conditional complete-core reference transfer for one actual nonproduct or multiple-nonfair-coordinate row after data exposure. Retain the signed address gap H(w)-E H_1/2(p), both terminal spectra and one unused physical reserve; do not replace the gap by a universal Renyi/I bound.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B16','packet_id':'A079','gap_id':'G-PHASE-COND','attempt_id':'A079-phase-4','method':'Consume the forced cubic 4:1 witness; classify unequal affine inverse supports under integer height2; remove phase-degree hypothesis by low-dimensional exclusion; pay full address and conditional entropy with the universal two-address row ledger.','mathematical_delta':{'conditional_constant':'3/2+(5/2)h2(1/10), sharp','whole_constant':'10-3log2(3), upper bound not claimed sharp','phase_scope':'Arbitrary signs for fixed ratios2,3,4; quadratic branches only for the detailed geometric classification','universal_interface':'H(w)<=E H_1/2(p)+2 I_X, keeping the signed gap for any extension','review_consumed':'A068 independently reconstructs A079-SHARP-QUADRATIC-TWO-PHASE-COLLISION@1 without repair'},'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'NARROW_ALL_DIMENSIONAL_TARGET_AUTHOR_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A032-AFFINE-ADMISSION-QUADRATIC-OBSTRUCTION','version':1,'use':'Source-bound actual witness and next-target motivation only; not a proof premise'},{'claim_id':'A034-SIGNED-ODD-MASK-ADMISSION','version':1,'use':'Scope and common-mask frontier; no pending result used as a proof premise'},{'claim_id':old['claim_id'],'version':1,'use':'Independent A068 review consumed; prior inequality is not a proof dependency'}],'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'change':'New narrow self-contained theorem'},{'claim_id':old['claim_id'],'version':1,'change':'Source-bound A068 review appended without changing statement/proof/contributors'}],'source_artifacts':manifest,'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Independent review of the new theorem pending','Arbitrary nonproduct/multiple-nonfair conditional transfer unpaid; no unrestricted tensor or hereditary closure'],'packet_ids':['A079']}
g=json.loads((ROOT/'out'/'general_extension_validation.json').read_text());assert g['status']=='PASS'
progress['mathematical_delta']['conditional_scope']='At most one nonfair coordinate per product row; arbitrary marginal and phase'
progress['mathematical_delta']['general_joint_constant']='6+2log2(65/64); fixed-ratio sharper constant10-3log2(3) retained'
progress['mathematical_delta']['general_extension_validation']=g
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=f'''# A079 stage4: arbitrary-phase fixed-ratio conditional payment

## exact target, quantifiers, hypotheses and units

Every actual Boolean F on exactly two uniform address bits and any number of
uniform data bits is admitted if every nonzero conditional Fourier row has a
coordinate-product spectrum, entirely fair or with one primitive magnitude
ratio2:1,3:1,4:1 and otherwise fair coordinates. Fixed frequency characters
are allowed. Fourier signs are ARBITRARY. Entropy is in bits and influence is
physical mean Fourier degree. Proved sharp conditional rate
Kcond=3/2+(5/2)h2(1/10), and joint rate Kjoint=10-3log2(3) (not claimed sharp).
The exact conditional equality case is the three-bit point defect with two
address bits and one data bit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read complete BOARD snapshot2026-10-14 02:53UTC, with the initially truncated
middle recovered in separate B07-B18 reads; B16 STREAM_NOTES.md v2 dated
2026-10-11 23:25Z; own STATUS and prior DERIVATION. Reuse the execution protocol
revision2026-10-11-execution-v2 already read in full in the preceding stage.
Read A032 stage4 REPORT/CLAIMS/QUADRATIC_OBSTRUCTION and phase_anf output/helper
(run20261014T015128Z); read A034 stage4 REPORT/CLAIMS
(run20261014T025347Z). These force the actual cubic row and leave unequal inverse
support payment open. Physical quadratic phases and Fourier-sign quadratic
phases are distinct hypotheses.

Read A068 stage4 REPORT in full (run20261014T023317Z), especially Section5:
it independently reconstructs our prior sharp same-cube quadratic collision,
pins the original statement/proof hashes and supplies no substantive repair.
The new run copies that claim with only this review record appended. Registry
adoption is not verified. Sources and SHA256s are in out/SOURCE_MANIFEST.json;
A032's actual witness source is additionally pinned separately. No new paper,
literature priority assertion, brain query/write or external message is used.

The unchanged lead target of distinct bent branches was closed as hardness
transport earlier. This run consumes new A032/A034 dependencies and develops
the precise forced cubic collision rather than repeating flat-padding tests.

## complete derivation or exact first unsupported line

DERIVATION.md gives the full proof. The inverse quadratic branch laws have flat
affine physical supports with integer height constraints. Disjoint supports
force amplitudes1 or2; proper intersections force both amplitudes1; equal
supports permit only the ratio-three nonfair case. A4:1 row requires at least
three fair frequency coordinates. For the forbidden smaller dimensions every
sign branch is automatically quadratic, so this exclusion holds for arbitrary
Fourier signs. Integer Walsh divisibility gives universal weight caps5/8 or17/32.

For EVERY two-address Boolean function, without product/phase assumptions,
H(w)<=E H_1/2(p)+2I_X. Fourier inversion pays each row's address mass; mixed-only
rows all have weight delta/4 and their extra cost is paid once by I_X>=delta.
This retains both H(w) and the complete H(S_Y|S_X). Under the fixed-ratio
admission, the regular rows pay the joint and conditional bills from physical
row influence. The ratio-three zero-fair-coordinate endpoint uses the actual
common mixed half cube and weights(5,1,1,1)/8; it gives the sharp conditional
rate, with all terminal entropy retained.

The included A032 cubic witness has row ratios4,3,3,2 and passes the new theorem.
The detailed affine-support classification remains quadratic-branch scoped;
the entropy theorem does not impose that large-dimensional phase hypothesis.
First unsupported extension: a nonproduct/multiple-nonfair complete-core
reference transfer after actual data exposure, retaining the signed gap and
both terminal bills. Direct universal Renyi/I payment is already a known failed
route and is not proposed. More address bits, arbitrary ratios, unrestricted
tensors and recursive collision closure are not established.

## executed validation with domain, arithmetic, commands and outputs

The frozen pilot command `python -X utf8 code\\check.py --pilot` passed670
cases and {p['assertions']} assertions in {p['seconds']:.3f}s. The full command
`python -X utf8 code\\check.py` passed {total} cases and {v['assertions']} assertions
in {v['seconds']:.3f}s, under its600-second cap.

Full domain: all65,536 actual Boolean truth tables with two address and two
data bits, without symmetry reduction; all24,990 ratio2,3,4 quadratic branch
pair cases on m=0,1,2,3 modulo simultaneous sign, with heavy half oriented zero;
12 frozen higher-rank/translation endpoints on m=4,5,7; A032's actual64-sign
witness; and the sharp conditional three-bit witness. No automatic dimension
growth occurred. Row-pair admissions/scalings are additional checked objects,
not extra Boolean-function counts. Every whole Boolean function in the n4
domain whose rows satisfy the magnitude admission automatically has quadratic
branches (at most one remaining free frequency bit), so the finite domain
checks the full arbitrary-phase theorem there. The larger fixtures test its
quadratic-branch subclass; the analytic low-dimension exclusion supplies the
all-phase/all-dimensional bridge.

The original full helper stopped at its600-second guard during the Boolean
sweep, with no completed full receipt or inequality failure. It is preserved
in out/FAILED_FULL_V1.json. Revised v2 rounds the rational log enclosures outward
to denominator2^96 after retaining their proved tails; this controls repeated
denominator growth without weakening certificate validity. Its frozen specs
precede the successful revised pilot and full run.

Arithmetic: integer FWHT, gcd, Fraction, exact prime-log identities, rational
atanh enclosures with proved120-term tails and outward dyadic rounding. Validation checks the normalized
full/conditional entropy chain, physical influence, common mixed mask, exact
per-row uncertainty bounds, both entropy inequalities, affine support/amplitude
forms and weight bounds, and sharp conditional equality. No floating acceptance
test or independent-review claim is made for author code. Estimated memory was
below100MB, so no300MB memok-triggering job was started; one full job ran at a
time. out/validation.json and frozen specs preserve counts and arithmetic.

## proof dependencies and changed downstream conclusions

The new theorem and universal row ledger are self-contained. A032 supplies an
actual witness and the question, not an unreviewed proof premise; A034's signed
odd-mask lemma is not assumed. A068's review of our prior claim is consumed
without modifying its statement or contributors. No original restricted claim
is refuted or superseded. This closes the unequal-support cubic fixed-ratio
case in every dimension, even beyond quadratic branch phases, and preserves
the actual conditional entropy rather than a proxy Q alone. It does not close
the universal weighted nonfair-row target or full FEI.

## one next mathematical action and independent reviewer

{next_action}
Independent reconstruction requested through this artifact: A088/A094 or A092,
especially the mixed-only address payment and exceptional ratio-three ownership.
A032/A034/A068 are immediate mathematical consumers. This is a handoff artifact,
not a sent message or claim of their downstream use.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json,
DERIVATION.md, frozen specs, code and exact out receipts are saved inside the
assigned run. STATUS has two lines; WORKLOG and LEARNED are appended.
out/PERSISTENCE_RECEIPT.json pins readback schemas, hashes and sizes. Local
persistence is verified; independent review, supervisor copying, registry
adoption and mirrors remain unverified. No save blocker exists.

**Universal bridge:** This stage moves the B16 G-PHASE-COND target toward C018
by proving a sharp all-dimensional conditional payment for one nonfair ratio
2,3,4 with arbitrary compatible phases, including the previously forced cubic
unequal-support row; it also pays the retained full joint entropy at Kjoint.
The universal two-address row ledger identifies the exact signed address gap
for further transfer, rather than discarding terminal entropy. The remaining
bridge is a nonproduct/multiple-coordinate conditional reference transfer after
data exposure with one physical reserve. NEXT is the shortest route toward
full FEI because it attacks the first operation that leaves this newly closed
admission, while arbitrary seed padding and direct Renyi payment are already
known to retain or misprice the universal obstruction.
'''
report=report.replace('arbitrary-phase fixed-ratio conditional payment','sharp arbitrary-ratio conditional payment')
report=report.replace('coordinate-product spectrum, entirely fair or with one primitive magnitude\nratio2:1,3:1,4:1 and otherwise fair coordinates.','coordinate-product spectrum with at most one nonfair varying frequency\ncoordinate, with arbitrary nonfair marginal and all other coordinates fair.')
report=report.replace('Kcond=3/2+(5/2)h2(1/10), and joint rate Kjoint=10-3log2(3) (not claimed sharp).','Kcond=3/2+(5/2)h2(1/10), and general joint rate Kall=6+2log2(65/64).\nIf all nonfair primitive magnitude ratios are2,3,4, the sharper joint rate is\nKjoint=10-3log2(3). Neither joint rate is claimed sharp.')
report=report.replace('More address bits, arbitrary ratios, unrestricted','More address bits, multiple nonfair coordinates per row, unrestricted')
report=report.replace('The detailed affine-support classification remains quadratic-branch scoped;\nthe entropy theorem does not impose that large-dimensional phase hypothesis.','The detailed affine-support classification remains quadratic-branch scoped.\nThe main conditional theorem has no phase-degree or ratio restriction: the\nGibbs/KL bound pays every regular one-nonfair row at5/2, and integer height\nleaves only ratio3 for the zero-fair-coordinate endpoint. Odd norm divisibility\nforces all its other address rows to be fair. A second Gibbs bound yields\nKall for full joint entropy, with address entropy retained.')
report=report.replace('Every whole Boolean function in the n4\ndomain whose rows satisfy the magnitude admission automatically has quadratic\nbranches (at most one remaining free frequency bit), so the finite domain\nchecks the full arbitrary-phase theorem there.','Every whole Boolean function in the n4\ndomain with at most one nonfair marginal has at most one other varying\nfrequency bit, hence affine branch signs and only ratio2 or3. The complete\nn4 sweep therefore checks the full arbitrary-ratio/arbitrary-phase theorem\nthere;10,560 functions are admitted.')
report=report.replace('It does not close\nthe universal weighted nonfair-row target or full FEI.','It does not close\nthe universal weighted nonfair-row target or full FEI. All single-nonfair\ncoordinate odds are closed, not just the three named magnitude ratios.')
insert=f'''\nThe general extension command `python -X utf8 code\\general_certificates.py`\npassed {g['assertions']} exact assertions in {g['seconds']:.3f}s: all25 height-two\none-bit pairs,647 coprime magnitude pairs among1024 screened pairs,640\nsymbolic m/q residual cases and five integer comparisons. The continuum\nGibbs/KL proof is analytic; these finite examples are not its substitute.\nThe only nonfair one-bit ratio is3:1, and121<128 certifies the exact square-root\ncomparison used to bound every other row at rate5/2. Its frozen spec and receipt\nare saved separately.\n\n'''
report=report.replace('## proof dependencies and changed downstream conclusions',insert+'## proof dependencies and changed downstream conclusions')
report=report.replace('by proving a sharp all-dimensional conditional payment for one nonfair ratio\n2,3,4 with arbitrary compatible phases, including the previously forced cubic\nunequal-support row; it also pays the retained full joint entropy at Kjoint.','by proving a sharp all-dimensional conditional payment for product rows with\nat most one nonfair coordinate, arbitrary marginal and arbitrary compatible\nphase, including the forced cubic unequal-support row; it pays retained joint\nentropy at Kall, sharpened to Kjoint for ratios2,3,4.')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: Stage4 complete: single-nonfair product rows, arbitrary odds/phases, pay sharp conditional Kcond and joint Kall; fixed ratios2/3/4 sharpen joint Kjoint; exact90540 cases PASS; prior collision reviewed by A068; FEI OPEN.\nNEXT: Nonproduct/multiple-nonfair conditional complete-core transfer with signed address gap, both terminal spectra and one physical reserve; A032/A034 consume, A088/A094 review.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} {ROOT.name}: consumed A032 forced cubic witness/A034 common-mask frontier and A068 acceptance. Classified equal/overlapping/disjoint inverse supports under height2. Low-dimensional exclusion removes phase-degree assumption for fixed ratio2/3/4; proved sharp conditional Kcond=3/2+5h2(1/10)/2 and joint Kjoint=10-3log2(3), plus universal address-row ledger. Exact{total} cases/{v["assertions"]} assertions PASS. No universal FEI/tensor/recursive closure; next signed complete-core transfer at first nonproduct row. All protocol files saved locally.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage4 (author proof pending review): exactly two-address Boolean F with conditional product rows entirely fair or with one primitive magnitude ratio2/3/4 and other coordinates fair, arbitrary Fourier signs, satisfies H(Y|X)<=Kcond I_Y, Kcond=3/2+(5/2)h2(1/10), sharp at three-bit point defect, and H<=Kjoint I, Kjoint=10-3log2(3). Universally H(w)<=E H_1/2(p)+2I_X: mixed-only rows each weigh delta/4 and I_X>=delta. Quadratic branch inverse supports: equal permits ratio3 amplitudes3/2,1/2; unequal intersecting forces1,1 and ratio power2; disjoint forces amplitudes1 or2. Ratio4 needs m>=3 fair coordinates; for m<3 every sign branch is automatically quadratic, so this dimension exclusion is arbitrary-phase. Odd divisibility of integer Walsh common magnitude forces a power of two, yielding weights<=5/8 (ratios2/3) or17/32 (ratio4). Ratio3,m0 uses common mixed half cube; other row weights1/8 cannot carry odd5/17 norm factors and must be fair. Keep the signed address gap on nonproduct extension; never ask for a universal Renyi/I bound. A068 independently accepts previous quadratic full-cube collision v1 without repair; registry adoption unverified.\n')
fields=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert all(set(c)==set(fields['claim_fields']) for c in [new,old])
assert set(progress)=={s if not s.startswith('packet_ids ') else 'packet_ids' for s in fields['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all('## '+s in report for s in fields['report_fields'])
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[f for f in ROOT.rglob('*') if f.is_file() and f.name!='PERSISTENCE_RECEIPT.json'];assert all(f.stat().st_size<20_000_000 for f in files)
save(ROOT/'out'/'PERSISTENCE_RECEIPT.json',{'schema':'PASS','report_fields':'PASS','packet_delta_identical':True,'status_two_lines':True,'local_only':True,'independent_review_new':'PENDING','files':[{'path':str(f.relative_to(ROOT)),'sha256':sha(f),'bytes':f.stat().st_size} for f in files]})
print(json.dumps({'status':'SAVED_AND_READBACK_VERIFIED','cases':total,'assertions':v['assertions'],'run':str(ROOT)},indent=2))
