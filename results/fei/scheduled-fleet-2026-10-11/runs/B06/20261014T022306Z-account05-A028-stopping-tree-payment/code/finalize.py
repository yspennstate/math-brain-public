from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]; BASE=HOME.parents[1]
old=HOME/'runs'/'20261013T223410Z-account05-A028-stopping-tree-payment'
a12=BASE/'agents'/'A012'/'runs'/'20261014T014452Z-account05-A012-sparse-activation-accounting'
a95=BASE/'agents'/'A095'/'runs'/'20261014T010024Z-account05-A095-restricted-result-extraction'
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,t):Path(p).write_text(t,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
sources=[protocol,BASE/'BOARD.md',BASE/'claude'/'B06'/'STREAM_NOTES.md',old/'REPORT.md',old/'DERIVATION.md',old/'CLAIMS.json',a12/'DERIVATION.md',a12/'CLAIMS.json',a95/'DERIVATION.md']
sources += [BASE/'agents'/a/'LEARNED.md' for a in ['A012','A013','A095','A097']]
js(R/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
source=json.loads((a12/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert source['statement_sha256']==hashlib.sha256(source['exact_statement'].encode()).hexdigest()
review={'claim_id':source['claim_id'],'version':source['version'],'statement_sha256':source['statement_sha256'],
'original_exact_statement':source['exact_statement'],'reviewer':'A028','verdict':'HOLDS_AT_ENTROPY_INCREMENT_SUBCLAIM_SCOPE',
'scope':'Only at-most-two-shared-data literal-selector B<=4d* and Pi<=(4+2/ln2)d*; no complete admission or supplied-reference blanket review',
'proof':str(R/'DERIVATION.md')+' Section3 endpoint reconstruction',
'validation':str(R/'out'/'full_validation.json')+' includes all k2 no-private pairs and all k1 up-to-one-private-bit pairs at r1',
'contributor_status':'No repair; independent scoped reconstruction'}
js(R/'out'/'REVIEW_A012_SCOPED.json',review)
claim=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))[0]
statement=('Version 4 preserves version-3 conclusions at their original scope. New interface: '
'for all Boolean signs G(s,X),H(s,Y) on a shared k>=1 uniform physical data block with disjoint private cubes X,Y, '
'and point selector A_r on r>=1 physical bits absent from both children, p=2^-r, F=A_r G+(1-A_r)H, d=Pr(G!=H), '
'the complete control-first physical stopping-tree signed entropy payment Pi=H(F)-pH(G)-(1-p)H(H) '
'is at most [4+(4k+6log2(e)+4log2(e)/e)/r]Q, Q=2rp d. '
'For r>=k it is at most14Q, including k=r=1 using the independently reconstructed literal-overlap endpoint. '
'I(F)=Q+pI(G)+(1-p)I(H), with every shared data influence counted through actual branch weights. '
'Calibrating all shared-only atoms of supplied normalized core references yields one explicit normalized point-selector reference with '
'D_root=pD_Gcal+(1-p)D_Hcal and CE_root=pCE_Gcal+(1-p)CE_Hcal+Pi. '
'Certified terminal allowances give complete path-plus-terminal rate max(14,L_G,L_H), independent of recursive block depth when each block satisfies r>=k. '
'For even k>=4, actual quadratic bent G and its one-point-flip H satisfy Pi/Q>=(1-2^-r)[4+2(k-4)/r], '
'so selector-only payment diverges along k/r->infinity, while no unbounded full FEI ratio is asserted. '
'The width condition is not hereditary under active-control restrictions. Arbitrary interleaving, clipped-positive charges, '
'universal terminal admission and payment of excess collision from a nonreused terminal reserve remain open.')
claim.update(version=4,exact_statement=statement,hypotheses=[
'Uniform finite Boolean cubes; all entropy, CE and KL bits',
'Exactly one common data block s, disjoint private blocks X,Y; selector controls absent from children',
'Point selector on r>=1 physical bits; fixed-rate14 conclusion requires r>=k',
'Physical control-first block tree stops at original G or H with weights p,1-p',
'Signed actual entropy increments, not clipped positives, transcript or mismatched-source charges',
'Supplied terminal FEI/reference bounds remain explicit hypotheses; ideal reference costs omit prefix rounding'],
statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),proof_source={'report':str(R/'REPORT.md'),'proof':str(R/'DERIVATION.md'),'validation':str(R/'out'/'full_validation.json')},
proof_dependencies=[{'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@3','scope':'unchanged disjoint/priority components only','source':str(old/'REPORT.md'),'sha256':sha(old/'REPORT.md')},
{'claim':'A012-DISJOINT-PRIVATE-MUX-ADMISSION@2','scope':'literal-selector entropy increment endpoint only','source':str(a12/'DERIVATION.md'),'sha256':sha(a12/'DERIVATION.md'),'status':'INDEPENDENTLY_RECONSTRUCTED_AT_SUBCLAIM_SCOPE_BY_A028'},
'A095/A097 shared-row conditional-mean minority-cap baseline consumed; raw entropy point-sector adaptation proved here',
'Exact physical-tree conservation, Fourier Parseval partition, elementary semiconvexity and scalar entropy maxima'],
review_records=[],status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
supersedes=[{'claim_id':claim['claim_id'],'version':3,'reason':'Narrow shared-data point-selector interface extension; previous scopes unchanged'}],
refutes=[],first_unproved_line=None,next_consumers=['A012','A013','A027','A057','A086','A091','A094','A095','A097','B06','B20'])
js(R/'CLAIMS.json',[claim])
v=json.loads((R/'out'/'full_validation.json').read_text())
pilot=json.loads((R/'out'/'pilot_validation.json').read_text())
report=f'''# A028 stage 4: stopping payment with shared-data width accounted

## exact target, quantifiers, hypotheses and units

For every point selector A_r on r fresh uniform physical bits, and Boolean children G(s,X),H(s,Y) sharing k>=1 data bits with disjoint private cubes, prove the full control-first stopping-tree cost retaining original terminal entropies. All entropy is bits; physical uniform influence uses coordinate flips. Let p=2^-r,d=Pr(G!=H),Q=2rp d. The new all-width estimate is Pi=H(F)-pH(G)-(1-p)H(H) <=[4+(4k+6log2(e)+4log2(e)/e)/r]Q. If r>=k, Pi<=14Q, so supplied terminal constants give FULL expected signed path cost plus terminal allowance <=max(14,L_G,L_H)I(F). This includes arbitrary child biases and arbitrary private dimensions. Shared data influence is averaged in terminal influences, counted once.

The calibrated complete point-selector reference has exact weighted terminal KL conservation and the same overhead. Costs are ideal negative-log probabilities; no integer rounding or physical transcript decoding is paid. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor 2026-10-14 02:22 UTC, own STATUS, B06 STREAM_NOTES v2, and EXECUTION_PROTOCOL.json v2. Reread board slices after initial output truncation. Current A012,A013,A095,A097 LEARNED files identify the already closed one-/two-shared-bit literal muxes and growing-overlap counterfamily. Read A012 stage4 DERIVATION in full and original v2 claim; read A095 stage3 DERIVATION in full. Prior campaign/registry/plan/paper source intake remains at its recorded prior-stage scope; no new outside source is invoked. Exact source bytes are recorded in out/SOURCE_RECEIPTS.json.

Do not repeat last NEXT literally: the single-shared-data mux now has full payment in A013/A097; A012 extends it to two shared bits. A095 proves a linear literal-selector tax with a sharp leading asymptotic, and A097/A086 already own the bent/point-edit no-go. New direction is the arbitrary point-selector width parameter and its dilution of collision payment. Our current raw entropy bound is different from A095's binary-erasure packet; this adaptation pays every nonempty sector of the point gate. B06's stale arbitrary-controller assignment was closed conditionally in v2, with its universal FEI-equivalence honestly retained; no lead direction is rejected.

## complete derivation or exact first unsupported line

DERIVATION.md proves the exact coherent entropy formula. Split Fourier rows into shared-only collision sets and private sets belonging to one child. The identity V_G+V_H+sum_C(a-c)^2=4d partitions one physical disagreement account. Conditional private means imply each collision atom lambda=(a-c)^2/4<=d^2 and total Delta<=min(d,2^k d^2). A two-regime raw entropy estimate gives sum eta(lambda)<=(2k+2log2(e)/e)d. Semiconvexity of eta(x^2) bounds the weighted mean Jensen cost. Combining the exact private and shared row terms yields the stated coefficient; terminal costs are never removed. No sign fold is used when r>1, since it need not preserve that point-selector spectrum.

For r>=k>=2, exact rational constants give coefficient<=161/12<14. For k1,r>=2 it is <=137/12<14. The remaining k=r=1 endpoint follows from an independently reconstructed A012 v2 entropy-only subclaim, giving a much smaller rate<7. Constants and zero disagreement are included. The normalized reference calibrates every shared-only child atom, preserves the private conditional law including off-target mass, and has debt pD_Gcal+(1-p)D_Hcal exactly.

For the known actual bent/point-flip children on even k, the new all-r lower bound is Pi/Q>=(1-p)[4+2(k-4)/r]. It follows from the explicit point-sector spectrum and an upper-curvature bound along the bent Fourier coefficient intervals. This proves that the k/r scale cannot be removed from a selector-only payment covering arbitrary shared children. It is not another FEI counterexample: large child influence remains. The upper bound makes r=Omega(k) sufficient in scale, while the lower family makes it necessary for the full unrestricted child-pair family.

A recursive finite certificate can use paid complete point-selector blocks with r>=k and certified terminal classes, preserving the maximum rate independent of depth. It is NOT asserted hereditary under restrictions: active point-control restrictions shorten r without shrinking k. The original whole block remains paid even though an intermediate active descendant can violate the width condition. That is a nonlocal stopping certificate, not a universally good-coordinate rule.

First unsupported universal line: if r<<k, fund the excess collision entropy from one explicitly UNUSED signed terminal-core reserve, transported through the actual history with correct child weights and no shared-influence reuse. The actual lower family rules out a fixed selector-only repair. General controllers, arbitrary data/control interleaving and universal opaque terminal admission remain open.

## executed validation with domain, arithmetic, commands and outputs

The frozen spec was saved before any search. Pilot: exhaustive no-private child pairs at shared k1,r1,2 and k2,r2, plus bent k4,r1,2,4: {pilot['cases']} cases/{pilot['assertions_passed']} exact assertions PASS in {pilot['compute_seconds']:.6f}sec. Full: shared k1 with private branch dimensions0..1, all20x20 labeled pairs,r1..4; shared k2 all16x16 no-private labeled pairs,r1..4; actual bent/flip k4,6,r1,2,k: {v['cases']} cases/{v['assertions_passed']} exact assertions PASS in {v['compute_seconds']:.6f}sec. No symmetry quotient, random sample or automatic dimension increase; maximum actual dimension12.

Commands from A028: python -X utf8 runs/{R.name}/code/setup.py; then code/check.py pilot and code/check.py full in that same run path. Integer Walsh and Fraction amplitudes derive true spectra; independent physical edges verify selector influence, and exact canonical prime-log dictionaries verify the complete overhead formula and influence ownership. Rational outward atanh24 intervals verify the width-dependent upper payment, rate14 on r>=k, and all-r lower bound on every actual bent fixture. Their explicit tail, positive ln2 division and outward denominator2^48 rounding are visible in code/exact.py. The full reference identity is proved algebraically; arbitrary supplied reference laws were not enumerated.

Memory estimate128MB, pilot watchdog55sec/full300sec. No >300MB job was expected or started, so no memok-gated heavy job was needed. No GPU, background process, external write or dimension escalation occurred. Finite results corroborate the analytic proof; no finite-to-infinite extrapolation is claimed.

## proof dependencies and changed downstream conclusions

Version4 extends the existing stopping-payment candidate; v1-v3 scopes remain unchanged, and no new broad universal route is opened. A012-DISJOINT-PRIVATE-MUX-ADMISSION@2 is independently reconstructed ONLY at B<=4d* and entropy increment<7d* scope; its unchanged original statement/hash and the scoped verdict are saved. No complete grammar/reference acceptance is issued from this limited check. A095's shared-row cap is consumed as an algebraic baseline and independently adapted to raw point-sector entropy. The known bent counterfamily is credited to A097/A086/A095 rather than claimed again.

B06 now has a source-complete stopping rule covering arbitrary overlap sizes when selector width dominates the support intersection, retaining full original terminal cost. A012/A095/A097 can use its raw entropy estimate and calibrated reference to separate the removable width/r surcharge from the genuine unowned core reserve. This does not improve a universal FEI constant. Parent/child admission and inherited history refunds remain explicit obligations.

## one next mathematical action and independent reviewer

Consume A086's stage4 price-two bent/flip child reserve and A097's signed excess-collision NEXT; derive a point-selector version allocating one unused child slack to the excess term of equation(4) for r<k. Start with a non-flat shared mean profile and an actual inherited complete reference, not an independently reset exact reference. Preserve p,1-p weights across the first active-control restriction and identify the first failed source reserve. Reviewer A094, alternate A091; A012/A095 should check the collision partition and the distinction from their literal-sector tax. Saved handoffs only; no messages sent or review completion assumed.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved with DERIVATION.md, code and out directories, frozen spec, pilot/full exact outputs, scoped A012 review and source hash receipts. code/finalize.py validates exact protocol fields, headings, statement hashes, file sizes and two-line STATUS, then writes out/PERSISTENCE_RECEIPTS.json. Only A028 files are mutated. Local persistence is complete after this validator passes; independent v4 review, supervisor copies, canonical adoption and mirror verification remain unobserved.

## Universal bridge

This stage moves C019 stopping-tree payment from disjoint private branches to arbitrary shared-data blocks at rate14 when point-selector width r dominates shared size k, with an explicit all-width surcharge of order k/r and complete weighted terminal/reference debt retained. The actual all-r bent/flip lower bound identifies the precise selector-only barrier when k/r diverges; it does not refute FEI. Remaining work is a nonreused terminal-core slack payment for that excess collision, plus universal terminal admission and inherited-history transport. NEXT consumes A086/A097's existing child-reserve work at the first width-deficient restriction because it attacks the missing universal ownership bank; more fixed small-overlap classes would repeat cases already closed by A012/A013.
'''
write(R/'REPORT.md',report)
progress=json.loads((old/'PROGRESS.json').read_text(encoding='utf-8'))
progress.update(run_id=R.name,attempt_id='A028-C019-shared-width-point-selector-v4',method='Exact shared/private Fourier energy partition, raw collision entropy minority cap, semiconvexity, full terminal-debt transport and actual all-r bent certificates',
mathematical_delta='Arbitrary shared k-data point-selector payment <=[4+(4k+6b+4b/e)/r]Q; rate14 if r>=k; complete weighted terminal KL; actual lower ratio >=(1-p)[4+2(k-4)/r]; A012 entropy-only v2 subclaim reconstructed',
deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='WIDTH_DOMINATED_SHARED_DATA_STOPPING_PROVED_UNIVERSAL_FEI_OPEN',
claim_versions_used=['A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@3-preserved-scope','A012-DISJOINT-PRIVATE-MUX-ADMISSION@2-entropy-only','A095-stage3-shared-row-minority-cap','A097-stage3-bent-flip-actual-family'],
claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':4,'status':claim['status']}],
source_artifacts=[str(R/p) for p in ['REPORT.md','DERIVATION.md','code/check.py','out/full_validation.json','out/REVIEW_A012_SCOPED.json','out/SOURCE_RECEIPTS.json']],
next_consumers=claim['next_consumers'],next_action='Consume A086/A097 child-reserve interfaces; allocate inherited signed terminal slack to point-selector excess collision at first r<k descendant, preserving actual weights and complete reference',
stagnant_substantive_attempts=0,blockers=['Width condition not hereditary under active-control restrictions','Unowned excess collision for r<<k; selector-only universal repair refuted','Universal terminal FEI and inherited reference/history payment open','Independent v4 review and supervisor adoption/mirror unobserved'])
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
write(HOME/'STATUS.md','STATE: A028 stage4 saved arbitrary shared-k point-selector full payment with k/r tax and rate14 if r>=k; bent lower proves scale needed; 2630 cases/20792 exact assertions; v4 review pending; FEI OPEN.\nNEXT: A094/A091 review; consume A086/A097 terminal reserve and pay excess collision at first width-deficient restriction using inherited complete reference and original child weights.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{stamp} — stage4 {R.name}: single/two shared-bit literal mux already closed by others; changed to arbitrary shared width and point-selector r. Proved complete k/r payment and rate14 for r>=k, weighted reference debt, all-r actual bent lower. Reconstructed A012 v2 entropy-only subclaim. Pilot291/2332 and full2630/20792 exact assertions PASS (full25.426sec), estimate128MB/no heavy job. No universal FEI claim; width condition not hereditary. NEXT unused terminal slack on inherited width-deficient row.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''\n## Stage4: width-dominated shared-data point selector

* For Boolean G(s,X),H(s,Y), k shared bits and disjoint private cubes, fresh point selector widthr,p=2^-r,d=Pr(G!=H), actual full entropy payment Pi<= [4+(4k+6b+4b/e)/r]Q, Q=2rp d,b=log2(e). If r>=k>=1, rate14 suffices (r=k=1 uses A012 entropy-only endpoint). Full influence Q+pIG+(1-p)IH retains shared data once; terminal allowances give max(14,LG,LH) root rate.
* Exact shared/private ownership V_G+V_H+D=4d, D=sum_shared(a-c)^2. Raw atoms lambda=(a-c)^2/4 obey each<=d^2,total<=min(d,2^k d^2), yielding sum eta(lambda)<=(2k+2b/e)d without a sign fold. Sign-folding H preserves literal-selector spectra, but cannot be assumed for r>1 point gates.
* Calibrate all shared-only source atoms, retaining private conditional law/off-target mass. Complete root reference debt=pDG_cal+(1-p)DH_cal; CE=pCEG_cal+(1-p)CEH_cal+Pi. Ideal spectral cost only; no transcript or rounding claim.
* Known bent/point-flip actual children generalized to every point widthr satisfy Pi/Q>=(1-p)[4+2(k-4)/r] for evenk>=4. Thus k/r is the unavoidable selector-only scale, not full FEI growth. Terminal core influence stays substantial.
* r>=k is NOT hereditary under active-control restrictions: remainingr shrinks, sharedk need not. Whole-block payment can skip unpaid intermediate nodes; no all-coordinate admission or arbitrary interleaving conclusion. NEXT fund the width-deficient excess once from actual inherited terminal slack, consuming A086/A097 reserves rather than repeating fixed-overlap cases. Exact2630cases/20792assertions PASS, maximumactualdimension12.
''')
pf=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(pf['claim_fields'])
assert set(progress)==set('packet_ids' if x.startswith('packet_ids') else x for x in pf['progress_fields'])
assert all('## '+x in report for x in pf['report_fields'])
assert sha(R/'PROGRESS.json')==sha(R/'PACKET_DELTA.json')
assert len((HOME/'STATUS.md').read_text().splitlines())==2
assert v['cases']==2630 and v['assertions_passed']==20792 and v['status']=='PASS'
assert claim['statement_sha256']==hashlib.sha256(statement.encode()).hexdigest()
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
js(R/'out'/'PERSISTENCE_RECEIPTS.json',{'run_id':R.name,'schema_validation':'PASS','claim_version':4,'local_status':'SAVED',
'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
'rolling_files':[{'path':str(HOME/p),'sha256':sha(HOME/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],
'mirror_and_adoption':'UNOBSERVED; supervisor owns copying','write_scope':'A028 only'})
print(json.dumps({'status':'PASS','artifact_count':len(files),'cases':v['cases'],'assertions':v['assertions_passed'],'claim_version':4},indent=2))
