from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
import exact_helper as e
R=Path(__file__).resolve().parents[1];AGENT=R.parents[1];BASE=AGENT.parents[1]
OLD=R.parent/'20261023T023055Z-fleet03-A028-stopping-tree-payment'
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
REV=BASE/'agents/A029/runs/20261023T032111Z-fleet03-A029-child-deficit-transport'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):write(p,json.dumps(x,indent=2)+'\n')
def vec(d):return {int(k):F(v) for k,v in d.items()}
main=read(R/'out/check_full.json');pilot=read(R/'out/check_pilot.json');ind=read(R/'out/independent.json');obs=read(R/'out/obstruction.json')
assert all(x['status']=='PASS' for x in (main,pilot,ind,obs))
assert (main['cases'],main['queries'],main['assertions'])==(3521,8748,1088506)
assert (pilot['cases'],ind['nodes'],ind['leaves'],ind['assertions'])==(960,166,84,6781)
assert sha(R/'code/check.py')==main['script_sha256']==pilot['script_sha256']
assert sha(R/'code/base.py')==sha(OLD/'code/check.py')
oldfix=read(OLD/'out/fixture.json');fix=main['fixture']
assert fix['U']==oldfix['original_U']=='45/4' and fix['old_debit']==oldfix['old_debit']=='1/8'
# Reconcile the changed reserve: precisely the newly charged controller-shape debt.
assert not e.add(vec(oldfix['original_reserve']),e.scale(vec(fix['reserve']),-1),e.scale(vec(fix['root_shape']),-1))
assert vec(fix['root_S'])==vec(oldfix['root_Z_equals_J'])
assert e.enclosure(vec(fix['reserve']))[0]>0
prior=read(OLD/'CLAIMS.json')[0];review_claim=read(REV/'CLAIMS.json')[0]
assert prior['version']==review_claim['version']==7 and prior['statement_sha256']==review_claim['statement_sha256']
source=read(R/'out/context_receipts.json')
for p in (REV/'REVIEW_A028.md',REV/'CLAIMS.json',BASE/'agents/A029/LEARNED.md',BASE/'agents/A056/LEARNED.md'):
    source.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
dump(R/'out/context_receipts.json',source)
claimid=prior['claim_id']
statement=('Version8 retains prior scoped clauses and adds this supplied-reference theorem. For every Boolean binary mux f=(1-c)G+cH with independent controller a=1-2c, arbitrary fully shared Boolean G,H, and root spectral references Ra,Rg,Rh positive on the true supports, inherit each reference through its own actual physical phase-sensitive pair kernel, retaining all off-target mass and actual reference outcome normalizers. At each history let p=Ec, V=Var(a), gamma=Pr(G!=H), A=Pa conditioned nonempty, beta=1-Ra(empty), B=Ra conditioned nonempty, q=(1-p)Pg+pPh, r=(1-p)Rg+pRh, z_t=(1-p)Ghat(t)+pHhat(t), w_t=V(Ghat(t)-Hhat(t))^2/4. Prescribe Q(empty,t)=r_t z_t^2/q_t and Q(U,t)=r_t(w_t/q_t)B(U) for nonempty U, with all zero-true-row reference mass at empty U. Its actual KL Dstar=D(q||r)+gamma V D(A||B). Set Da=D(Pa||Ra), Cvac=D(Bern(V)||Bern(beta)), W=weighted source KL, Z=W-D(q||r), T=W+gamma Da, S=Z+gamma Cvac. Then Dstar=T-S, S>=0, and T is a supermartingale under every adaptive physical control/data query. For EVERY finite mixed stopping tree, sum reach*(E Dstar_child-Dstar_parent)+sum reach*(T_parent-E T_child)+E S_leaf=S_root. Complete nonnegative entropy or erasure path plus changed-reference terminal CE is <=Hroot+Troot, both child/terminal KL bills retained. Raw output reset equals the signed net debt increment plus actual output erasure/outcome refunds. Root controller empty calibration and common root data reference give Sroot=Jroot exactly, but the ORIGINAL allowance must separately include gamma Da_root; it is not free JS credit or a renewed descendant bank. Genuine source CE and calibrated controller CEplus certificates, plus the scoped v5 surcharge premise, conditionally yield rate max(K+3log2(e),Lg+2p,Lh+2(1-p)). An actual four-variable dummy-DATA-query witness has J=Z=W=0, H=I=2, both source children nonconstant, yet a changed nonempty profile costs (1/4)log2(4/3)>0, refuting arbitrary JS-only payment without refuting FEI.')
next_action='At a DATA child of the already changed-reference tree, change the row empty/nonempty odds w_t/q_t while retaining the SAME original Ra/Rg/Rh, controller liability, old debit and both full terminal bills; bound the extra binary-row KL from actual unused T-contraction/S credit. A029/A056/A094 independently reconstruct v8 first.'
claim=dict(claim_id=claimid,version=8,exact_statement=statement,hypotheses=[
    'Independent finite uniform controller/data blocks; arbitrary Boolean controller and fully shared Boolean sources',
    'One fixed original controller reference and two fixed original source references, positive on true supports; each inherits through its own physical phase kernel, no fresh descendant supplier',
    'All output row ratios remain actual; the nonempty controller conditional law is the inherited external B; specified zero-row/zero-variance conventions',
    'Full controller vacuum KL, both source bills, all actual branch normalizers and output erasure/outcome refunds retained; signed transactions not clipped',
    'Old debit b requires original U-b>=Hroot+Wroot+gamma Da_root; reusing v7 allowance requires proving the additional root controller liability fits its genuinely unused credit',
    'Influence corollary additionally requires root empty calibration, genuine data/controller CE suppliers and the explicitly conditional v5 surcharge inequality'],
    statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A028'],proof_source=['DERIVATION.md sections1-6','out/check_full.json','out/independent.json','out/obstruction.json'],
    proof_dependencies=[dict(claim=claimid+'@7',scope='supplied-source conditional-label KL transport, independently accepted by A029 at scoped core; new controller debt/vacuum transport reconstructed here'),dict(claim=claimid+'@5',scope='conditional root influence corollary only; no new acceptance of prior supplier/structural assertions')],
    review_records=[dict(reviewer='A029/fleet03',reviewed_version=7,verdict='HOLDS_SUPPLIED_REFERENCE_CORE_V7_SCOPED',scope='Earlier v7 only; excludes supplier assertions, conditional corollary stays conditional, no v8 acceptance',source=str(REV/'REVIEW_A028.md'),source_sha256=sha(REV/'REVIEW_A028.md'))],
    status='V8_AUTHOR_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING; V7_SCOPED_REVIEW_HOLDS',
    supersedes=[dict(claim_id=claimid,version=7,reason='Adds fixed inherited external controller-shape law and explicit original root liability/vacuum account; prior scopes retained')],
    refutes=[dict(statement='The original JS bank alone pays every genuine prescribed nonempty-controller-profile change after physical DATA restriction',witness='a=(-1,1,1,1), G=z,H=-z with one dummy DATA coordinate; J=Z=W=0,H=I=2; query dummy; B=(1/6,1/3,1/2) costs(1/4)log2(4/3)>0',scope='Payment guard, not an assertion made by v7 and not a FEI refutation')],
    first_unproved_line='Dimension-independent influence-priced initial controller/data CE suppliers for every Boolean input, or payment for changing the DATA-row empty/nonempty odds from the same already-debited original allowance.',next_consumers=['A029','A056','A087','A091','A094','A096','A097'])
dump(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B06',packet_id='A028',gap_id='C019',attempt_id='A028-v8-inherited-controller-shape-vacuum-payment',
    method='Transport one original controller KL weighted by harmonic disagreement; retain Bernoulli vacuum calibration KL and source conditional-label slack',
    mathematical_delta='All mixed-history genuine nonempty-controller-profile changes from ONE inherited root controller reference are paid, including both terminal CE and actual refunds. Extra root liability gamma Da is explicit, not supplied by JS. Exact zero-J dummy-query witness proves that liability cannot be omitted. Old rate4 seven-variable allowance pays it without renewal.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_AUTHOR_PROOF_EXACT_CHECKED; V8_REVIEW_PENDING; FULL_FEI_OPEN',
    claim_versions_used=[claimid+'@7 (A029 scoped supplied-reference acceptance)',claimid+'@5 (conditional surcharge ONLY)'],claims_created_or_changed=[claimid+'@8'],
    source_artifacts=['DERIVATION.md','out/FROZEN_SPEC.json','out/FROZEN_OBSTRUCTION.json','out/context_receipts.json','out/check_pilot.json','out/check_full.json','out/independent.json','out/obstruction.json','out/compute_snapshot.json'],
    next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
    blockers=['Universal initial source/controller CE suppliers not constructed','DATA-row odds or arbitrary fresh conditional profiles not paid','V8 independent peer review pending; v5 optional surcharge retains its conditional status','Remote publication belongs to campaign supervisor; no remote acceptance observed'],packet_ids=['A028'])
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
policy_counts=[dict(nodes=p['nodes'],leaves=p['leaves'],adaptive=p['adaptive']) for p in main['policies']]
report=f'''# A028 v8: one inherited controller reference pays changing nonempty shape

## exact target, quantifiers, hypotheses and units

For every finite uniform Boolean mux with independent controller and arbitrary shared data, carry ONE original supplied controller reference and the two original source references through EVERY adaptive physical mixed stopping tree. Pay complete nonnegative entropy/erasure path cost and terminal CE after replacing the true nonempty controller shape by its inherited external law. Entropy/KL/CE units are bits; influence is the physical Boolean flip convention. This scoped transport is proved; full FEI is OPEN. Initial reference certificates and additional controller root liability are hypotheses, not new free resources.

## sources actually read, revisions and theorem locators

Current BOARD, B06 STREAM_NOTES v2 and own STATUS/LEARNED were read at intake. The lead's arbitrary-controller assignment is already fulfilled in earlier stages; this resumes the explicit v7 NEXT. Archived execution protocol v2 and v7 proof/helper were read/pinned; full campaign/paper source baseline from earlier completed stages is retained rather than re-audited. Current A029 stage7 REVIEW_A028.md and its claim match the original v7 statement hash: scoped supplied-reference theorem HOLDS independently, earlier supplier assertions excluded. This acceptance is consumed and is not new v8 acceptance. A029 LEARNED records its small-profile-change theorem and asks to carry the CURRENT changed reference onward. A056 LEARNED stage19 gives a padding-stable degree tilt but explicitly leaves its influence-priced initial supplier open. Neither is used as a new supplier premise. Paths and source hashes are in out/context_receipts.json; shared source trees are unchanged. Current owner full-FEI-only and 23-Oct campaign clock govern older archived dates.

## complete derivation or exact first unsupported line

DERIVATION.md sections1-6 give the complete proof. At a history Pa is the controller spectrum, V=Var(a), A=Pa conditioned nonempty, beta=1-Ra(empty), and B=Ra conditioned nonempty for the ACTUAL inherited root reference Ra. In the output reference, retain the true empty/nonempty data-row probabilities but use B instead of A within the nonempty sector. Its exact output debt is Dstar=D(q||r)+gamma V D(A||B), where gamma=Pr(G!=H). Full controller KL decomposes as Da=Cvac+V D(A||B), Cvac=D(Bern(V)||Bern(beta)). Thus T=Wdata+gamma Da, S=Zdata+gamma Cvac, Dstar=T-S and S>=0.

T is a physical supermartingale: DATA leaves Da unchanged and makes gamma harmonic while Wdata contracts; CONTROL leaves gamma fixed, makes Wdata harmonic and contracts Da by the actual controller erasure/outcome KL. Therefore Atot=T-E Tchild>=0. Every finite mixed tree satisfies sum reach*sigma+sum reach*Atot+E Sleaf=Sroot, sigma=E Dstar_child-Dstar_parent. Raw output reset=kappa=sigma+actual Ef+actual Of, so refunds cannot be discarded. Complete path+terminal CE=Hroot+Troot-sum reach*Atot-E Sleaf. Both source children, full terminal KL, off-target masses and all branch normalizers stay present.

Root controller calibration and a common original data reference give Sroot=Jroot exactly. But Troot includes the real original controller liability gamma Da_root. It is not paid by the root JS identity. If U is an existing original allowance with old debit b, admission is U-b>=Hroot+Wdata_root+gamma Da_root; using a former v7 budget requires proving its UNUSED credit covers the added liability. With genuine source CE and calibrated controller CEplus certificates plus the conditional v5 surcharge, the influence rate is max(K+3log2(e),Lg+2p,Lh+2(1-p)). No such certificates for arbitrary Boolean sources are manufactured by this transport.

An exact guard proves why the extra liability matters: a two-control point defect, G=z,H=-z and a dummy data coordinate have Pg=Ph, J=Z=W=0, H(f)=I(f)=2. Querying the dummy leaves both source children nonconstant and spends zero entropy. Replacing the controller's uniform nonempty law by(1/6,1/3,1/2) adds exactly(1/4)log2(4/3)>0 to terminal CE, exceeding the tight old allowance2. This refutes arbitrary JS-only profile payment, not v7 and not FEI. The root controller liability in v8 is exactly this missing amount. Dummy padding preserves the guard.

The first unsupported universal line is supplying influence-priced initial source/controller CE references for every Boolean input; changing the data-row binary odds w_t/q_t is also outside the present target family. The inherited external B supplies genuine nonempty changes but does not license arbitrary fresh descendant laws.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede searches. Pilot: all controller dimensions0..1 and same-data-cube source pairs in dimensions0..1, eight reference choices/root, no symmetry quotient: {pilot['cases']} cases/{pilot['queries']} physical queries/{pilot['assertions']} assertions, PASS in {pilot['seconds']:.3f}s. Main changes the DOMAIN from last stage: controller dimensions0..2, data dimensions0..1, eight reference choices/root, rather than last stage's data dimensions0..2/controller0..1/four references. It has3,520 enumerated roots plus ONE predeclared nonflat seven-variable weighted-controller fixture and its three stopping policies: {main['cases']} cases/{main['queries']} checked root/tree queries/{main['assertions']} assertions in {main['seconds']:.3f}s. The changed assertion count reflects this different focused domain, not dropped failures. Policy node/leaf counts: {json.dumps(policy_counts)}.

Spectra, reference inheritance and normalizers are exact Fractions. Prime-log rational vector equality checks every KL/CE identity; outward 24-term atanh rational bounds certify signs. Code/independent.py imports neither main checker nor exact_helper; direct characters and a separately decomposed conditional-label erasure reconstruct {ind['nodes']} mixed-tree nodes/{ind['leaves']} leaves/{ind['assertions']} assertions in {ind['seconds']:.3f}s, including {ind['positive_shape_node_visits']} positive-shape and {ind['nonzero_vacuum_node_visits']} nonzero-vacuum node visits. Reused independent utilities are a pinned prefix from v7; old state/tree implementations were excluded. This is an author's different representation, not an independent peer acceptance. The obstruction uses direct spectra and exact integer4>3 for its strict sign. All PASS.

The nonconstant seven-variable fixture retains the SAME old U=4I=45/4 and old debit1/8 from v7, with I=45/16. Its new root reserve has exact vector -1/64+(745/512)log2(3)+(155/128)log2(5)+(121/512)log2(11)-(35/64)log2(7)>0. It is smaller than the v7 reserve by EXACTLY gamma Da_root, the charged controller-shape debt, as checked from both saved receipts. Thus no quota or influence constant changed and the controller liability was not renewed. Every query and terminal receipt is retained in out/check_full.json.

Commands: python -X utf8 code/prepare.py; code/check.py pilot; code/check.py full; code/prepare_independent.py; code/independent.py; code/obstruction.py; code/finalize.py; code/verify.py (each Python script invoked with python -X utf8). Frozen estimates180MB or less, no expected>300MB job, no GPU or detached process. Peak memory was not measured. Main59.4s is below480s cap; pilot6.1s is below60s. Compute snapshot at09:43 local showed1303MB available, commit93.5%, disk18.6GB, so checks stayed bounded/sequential; no work was stopped or throttled. No Lean/compiler certificate is claimed.

## proof dependencies and changed downstream conclusions

Version8 extends the same A028 candidate. A029's scoped independent acceptance now applies to v7's supplied-reference core; it does not cover v8, earlier bundled suppliers, or the conditional v5 surcharge. The new derivation uses only Parseval, physical KL chain rule, v7 conditional-label slack and harmonic disagreement. V5 enters only the explicit optional root-rate corollary. Data/source covariance is retained through the actual gamma, not an independence assumption. The exact JS-only guard rules out claiming the added controller-shape cost for free. Full FEI remains OPEN, and no broad extra unreviewed candidate is introduced.

## one next mathematical action and independent reviewer

{next_action} A029 should reconstruct the vacuum/source slack and sign conventions; A056 should audit source-specific physical kernels and conditional nonempty inheritance; A094 should challenge the original earmark, zero-J guard and all terminal bills. These are saved consumer requests for supervisor routing; no messages were sent.

## actual persistence receipts or precise save blocker

The four protocol files, complete proof, frozen specs, source/compute receipts and exact/independent scripts and outputs are saved only in A028. PACKET_DELTA is byte-identical to PROGRESS. Final schema, statement hash, nonempty counts, guard failures, two-line STATUS and file sizes are checked by code/verify.py; out/persistence.json hashes the package. Rolling WORKLOG and LEARNED are appended. No peer review, canonical adoption or remote mirror is inferred; supervisor publication remains unverified. Brain self-care is degraded/unverified because owner-model/state-of-mind notes are stale; these were not mathematical premises.

## Universal bridge

This stage moves C019/C024 from the true conditional controller profile to a genuinely changed nonempty shape inherited from ONE externally supplied original controller reference, through every adaptive mixed physical history. Full path and terminal CE remain paid from the same admitted original T account, with vacuum KL and controller root liability explicit; the fixed rate4 witness keeps its old debit and pays the liability from old unused credit. Universal FEI constant improvement is zero: initial influence-priced suppliers and data-row odds changes remain unpaid, and a zero-J Boolean witness proves arbitrary profile payment cannot be declared free. NEXT attacks the remaining binary-row KL on an already paid changed-reference history, which tests the missing full-reference transaction rather than opening another isolated function class.
'''
write(R/'REPORT.md',report)
write(AGENT/'STATUS.md','STATE: A028 v8 saved ALL mixed-history inherited nonempty-controller-profile payment with explicit ORIGINAL controller liability/vacuum KL; exact checks PASS; JS-only obstruction certified; v8 review pending; FEI OPEN.\nNEXT: A029/A056/A094 review; change DATA-row empty/nonempty odds after paid history from SAME unused T/S account, original controller reference, old debit and BOTH full terminal bills.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{stamp} — {R.name}: consumed A029 scoped v7 acceptance; v8 fixed original controller-reference nonempty shape paid across ALL mixed trees by T=W+gamma Da, S=Z+gamma Cvac. Main3521 cases/1088506 assertions, independent166 nodes/6781 checks PASS. Zero-J actual dummy-DATA witness needs extra(1/4)log2(4/3), so controller liability cannot be free. Same old4I/old1/8 fixture pays original gamma Da from prior reserve. Initial universal suppliers and row-odds conversion OPEN; v8 review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n## Stage8: fixed inherited controller reference changes the nonempty shape\n\nFor arbitrary controller/shared-source mux, replace only the true conditional nonempty controller profile A by B from ONE original full controller reference Ra, inherited through its OWN physical phase channel. Output debt Dstar=D(q||r)+gamma V D(A||B). The complete controller KL is Da=Cvac+V D(A||B), Cvac=D(Bern(V)||Bern(1-Ra0)). With data source debt W and conditional-label slack Z, set T=W+gamma Da and S=Z+gamma Cvac; then Dstar=T-S. DATA makes gamma harmonic and leaves Da fixed; CONTROL contracts Da and leaves gamma fixed; W behaves as in v7. Thus T is a supermartingale and every mixed tree has sum sigma+sum Atot+E Sleaf=Sroot, full path+CEleaf<=Hroot+Troot. Raw output reset=sigma+actual Ef+Of. Root calibration/common data reference give Sroot=Jroot but the ORIGINAL gamma Da liability is separate and must fit UNUSED original quota. Same prior4I fixture pays it with old1/8 retained; reserve decreased exactly by gamma Da, no rate change. A029 independently accepted v7 supplied-reference core, not v8 or prior suppliers. Guard: a=point defect2,G=z,H=-z plus dummyDATA, J=Z=W0,H=I2; dummy query then B=(1/6,1/3,1/2) costs(1/4)log2(4/3)>0. Thus arbitrary JS-only profile payment is false, not FEI. Universal initial suppliers and DATA-row odds changes remain unpaid.\n')
proto=read(PROTO)
assert set(claim)==set(proto['required_per_run']['claim_fields'])
fields=set(proto['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields and all('## '+k in report for k in proto['required_per_run']['report_fields'])
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ('persistence.json','verify.json')]
assert all(p.stat().st_size<20_000_000 for p in files)
dump(R/'out/persistence.json',dict(status='LOCAL_SAVED_HASHED',created_utc=stamp,files=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files],independent_v8_review='PENDING',remote_mirror='UNVERIFIED'))
print(json.dumps(dict(status='LOCAL_PACKAGE_WRITTEN',files=len(files),claim_version=8,full_FEI='OPEN')))
