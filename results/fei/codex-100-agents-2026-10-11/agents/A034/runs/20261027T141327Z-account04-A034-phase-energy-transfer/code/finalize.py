from pathlib import Path
import json,hashlib,datetime,subprocess,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out=R/'out';out.mkdir(exist_ok=True)
# The preceding fresh admission command returned exit1. Never start a compiler here.
save(out/'lean_status.json',dict(status='NOT_STARTED_MEMOK_HOLD',memok_exit_code=1,
    observed_stdout='WAIT: physical free 1.4 GB (need 4.0), commit free 2.9 GB (need 8.0)',
    source='code/GroupPayment.lean',target='grouped_payment_sharp',source_sha256=sha(R/'code/GroupPayment.lean'),
    scope='Source only: exact6/11 rounding of rational physical energies after clearing denominators. No Lean certificate for this lemma or the entropy theorem.'))
p=subprocess.run([sys.executable,'-B','-X','utf8',str(R/'code/check.py'),'boundaries'],capture_output=True,text=True,encoding='utf-8',timeout=60)
(out/'boundaries_command.txt').write_text(p.stdout+p.stderr,encoding='utf-8',newline='')
assert p.returncode==0,p.stdout+p.stderr
results={m:json.loads(read(out/f'{m}.json')) for m in ['scalar','sharpness','dense','symbolic','boundaries']}
assert all(v['status']=='PASS' for v in results.values())
assert all(v['helper_sha256']==sha(R/'code/check.py') for v in results.values())
total=sum(v['assertions'] for v in results.values());stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement=('For integer s>=2 put C=3+log2(e), R_s=64s^2, L_s=log2(s)+(s-1)log2(R_s)+C, J_s=(s-2)(1+log2(R_s))+2C, '
           'K_s=max(L_s,11J_s/3), K_s_rare=max(L_s,11J_s/6). Every ternary row u formed from at most s disjoint affine physical uniform-cube cells with intrinsic quadratic signs satisfies '
           'B(u)=sum_T uhat(T)^2 log2(1/uhat(T)^2)<=K_s E(u), retaining B(u)=mu H(P_u)+mu log2(1/mu). If mu<=1/2 use K_s_rare. A single piece has B<=C E. '
           'The rates are O(s log s); proper FOUR-cell rows have full rate<114, and support-mass<=1/2 FOUR-cell rows full rate<57. '
           'For an actual Boolean sign on disjoint independent uniform X,Y cubes with <=M complete affine Y phase cells, quadratic phases and INDIVIDUAL affine X-label maps on the cells, '
           'H(F)<=K_M I_Y and H(S_Y|S_X)<=K_M I_Y under every mixed physical restriction, with the direct single-piece bound at M1. '
           'The old complete-source rate2^(M+1), conditional rate2^M and fixed-M tensor guard degree<=M+1 remain valid. Optional integer X-degree cap d>=1 and arbitrary spectral correlations are allowed. '
           'The new scalar input is phi(|sum a_j|)<=sqrt(2) sum phi(|a_j|) for sum|a_j|<=1, phi(t)=sqrt(-t^2 ln(t^2)); factor1 if the sum is<=1/2. The squared factor2 is sharp as a scalar inequality.')
claim=dict(claim_id='A034-AFFINE-PLANE-HEREDITARY-PHASE',version=5,exact_statement=statement,
    hypotheses=['independent uniform physical X,Y cubes','actual Boolean sign F for source corollary','ternary row with disjoint nonempty affine physical cells and intrinsic quadratic signs','entropy bits; natural units only in scalar proof','finite piece count s or source phase count M; no dimension, codimension, rank or mass-ratio bound','rare-row improvement additionally mu<=1/2'],
    statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A034; A033 bounded-F2-degree mechanism credited and reconstructed'],
    proof_source='PROOF.md sections1-5',proof_dependencies=[],review_records=[],status='AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
    supersedes=['A034-AFFINE-PLANE-HEREDITARY-PHASE@4'],refutes=[],
    first_unproved_line='No row bound uniform in growing piece count, and no original-influence-priced bounded-piece decomposition for arbitrary Boolean cores. Independent reconstruction of version5 pending.',
    next_consumers=['A079','A033','A088','A094','B07','B20'])
save(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B07',packet_id='A034',gap_id='G-PHASE-COND',
    attempt_id='A034-stage22-v5-signed-scalar-entropy',method='Sharp signed scalar square-root entropy control, Euclidean triangle inequality, weighted energy Cauchy and reconstructed6/11 mass-group domination.',
    mathematical_delta='Improves arbitrary-mass proper-row full transfer O(s^2 log s) to O(s log s); FOUR-cell<292 becomes<114 and rare FOUR-cell<57. Complete-source M4 rate32 remains unchanged.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='AUTHOR_PROOF_PENDING_REVIEW; FULL_FEI_OPEN',
    claim_versions_used=['A034-AFFINE-PLANE-HEREDITARY-PHASE@4 reconstructed; not assumed independently accepted'],claims_created_or_changed=[claim['claim_id']+'@5'],
    source_artifacts=['PROOF.md','FROZEN_SPEC.json','code/check.py','code/GroupPayment.lean','out/scalar.json','out/sharpness.json','out/dense.json','out/symbolic.json','out/boundaries.json','out/lean_status.json','out/INTERNAL_REVIEW.md'],
    next_consumers=claim['next_consumers'],next_action='A079/A033 reconstruct dominant-amplitude scalar branch and weighted energy payment. Then remove mass-group logarithmic-width/piece-count cost or influence-price a bounded-piece decomposition of arbitrary cores.',
    stagnant_substantive_attempts=0,blockers=['Independent review pending','Lean compilation not started after fresh memok exit1','Universal growing-piece-count payment remains open'],packet_ids=['A034'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
table='\n'.join(f"| {m} | {v.get('cases') or v.get('compositions',0)} | {v['assertions']} | {v['seconds']:.3f} |" for m,v in results.items())
report=f'''# A034 stage22: linear piece-count phase transfer

## exact target, quantifiers, hypotheses and units

{statement}

Rung: complete author proof with exact finite checks, independent review pending. This is a strengthening of the existing pending phase-row candidate. Full FEI is OPEN. The old balanced proper-row rate below6.5 is retained. The old complete-source M4 rate32 uses a complete partition; the new proper-row rate114 permits an arbitrary proper union. Those two constants have different hypotheses. The improvement292->114 on the SAME arbitrary-mass proper-four-cell scope comes from the new coherent entropy estimate.

## sources actually read, revisions and theorem locators

Current BOARD.md B07 and named referee/coordination entries, B07 STREAM_NOTES.md v2 (11 October23:45), own STATUS, stage21 PROOF sections1-5 and integer/Fraction helper, and EXECUTION_PROTOCOL v2 fields/dispatch/review/compute requirements. Earlier full protocol/paper recovery remains in stage21; no new uninspected paper theorem is assumed. All essential mathematics is reconstructed here, including the previously used derivative gap, support isoperimetry and mass-group energy argument. The prior helper is imported ONLY for log intervals, Walsh transforms, influences and group definitions; its __main__ modes do not execute. Every output pins its SHA256. The single two-wording math recall returned the known nonBoolean control and unrelated entropy cards; none is a new proof premise. Personal owner-model/state/dream notes remain stale and are not used as mathematical evidence. Source receipts are recorded at final receipt time, not represented as a historical board snapshot.

## complete derivation or exact first unsupported line

PROOF.md is the full derivation. Its new scalar step splits at c=exp(-1/2). If all magnitudes are<=c, monotonicity below c and the decreasing ratio phi(t)/t prove the factor1 inequality. If a magnitude a>c occurs, the total amplitude condition forces all remaining absolute amplitudes<=1-a, hence t=|sum a_j|>=2a-1 and t^2>=2a^2-1. Either F(t^2)<=F(a^2) by monotonicity above1/e, or concavity along the segment from t^2 to1 gives F(t^2)<=2F(a^2). The endpoint a=1 is separate, and all zero-log terms are continuous. The scalar factor2 is asymptotically sharp using(1-epsilon,-epsilon); removing the l1 hypothesis is actually refuted in the checker.

Physical disjoint ternary groups have sum_g |vhat_g(T)|<=sum_g mu_g<=1 at EACH Fourier coordinate. Apply the scalar inequality, then the Euclidean triangle inequality to entropy-amplitude vectors: B(u)<=2(sum_g sqrt(B(v_g)))^2. Retain the full B, not merely normalized entropy. The rare case has factor1. Group-specific bills are L_g E_g, not the old common maximum L_s. Weighted Cauchy gives an account proportional to sum L_g rather than q max L_g. Reconstruct E_total>=(6/11)sum E_g. Then log2(m)<=m-1 and conservation sum m_g=s give sum L_g<=(s-2)(1+log2R)+2C for q>=2. A one-group row is handled directly. No infinite limit is used except the separately justified scalar sharpness ratio, and no limit is needed for the row theorem.

All physical restriction histories retain cellwise affine carriers; rows still have<=M quadratic affine intersections. The exact full entropy ledger is sum_J B(u_J), and sum_J E(u_J)=I_Y(F) on the SAME physical function. No influence bank is renewed. Fixing old coordinates forces a fresh data tensor factor to have phase degree<=M+1; AND_(M+2) is excluded. The three-bit point defect remains admitted; normalized psi_N fails ternary/unit-sign admission and violates each fixed claimed rate at large N. Optional d>=1 is retained but unnecessary to the constant. Arbitrary correlations of spectral auxiliaries are permitted; correlated physical laws are outside scope.

The first unsupported universal line is bounding the remaining mass-group width/count independently of growing pieces, or constructing an original-influence-priced bounded-piece source for arbitrary Boolean cores. A singleton representation may have exponentially many cells. No universal C018/C019 result or full-FEI resolution follows.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes searches. Commands: `python -B -X utf8 code/check.py MODE` for scalar, sharpness, dense, symbolic and boundaries. Integer Walsh and physical squared differences, Fraction arithmetic,16-term atanh logarithm intervals with geometric remainders, and directed rational square roots using integer isqrt are used. For inequalities, entropy UPPER intervals are compared against certified LOWER right sides; overlapping intervals do not count as proof. Singleton equalities are checked exactly.

| Job | Cases | Exact assertions | Seconds |
|---|---:|---:|---:|
{table}

Total {total:,} exact assertions PASS. Scalar grids are fully exhaustive only on their frozen rational domains; no finite grid proves the scalar theorem. The proof handles the continuum. The63 dyadic sharpness cases include k64 ratio>1.99 with rigorous intervals. The negative missing-l1 tuple is(1,-1/16), and fails the proposed inequality as required. The32 dense actual rows on14 physical Y bits use four affine cells of codimensions1,12,13,14, all16 signs and two quadratic choices. They exercise unequal mass groups and both the new coherent bill and full row bound. A real fresh-halfcube activation gives exact B'=B/2+mu and E'=E/2+mu/4, so the rare-row certificate is not a renormalized substitute. The activation identities are independently checked on a tiny physical row. The256 symbolic36-bit states use a NEW bit-mask shifted-intersection implementation and cover1/2/3/4 groups at the sharp6/11 factor; no2^36 truth table is allocated. The4095 ordered compositions up to12 test the group-size algebra. All jobs finish below55 seconds, estimate<=70MB, no automatic dimension escalation or heavy search.

The initial current compute snapshot was ok with7060MB available physical memory; WindowsTerminal was the largest listed private holder. The later fresh memok returned exit1: physical free1.4GB, commit free2.9GB. These are different observation times, not conflicting capacity claims. No job expected above300MB and no compiler was started after that hold. The core Lean source formalizes ONLY clearing denominators in9 first<=16 energy and32 summed<=33 first to6 summed<=11 energy. It remains UNCOMPILED; source is not a formal certificate. No Mathlib compiler, GPU, remote job, window or detached process was launched.

## proof dependencies and changed downstream conclusions

The source-level v4 row mechanism was reconstructed, not treated as independently accepted. v5 preserves the stable source class, guards, original physical account and old sharper subcases, while replacing the entropy bottleneck. The cost is O(s log s) instead of O(s^2 log s), at unchanged hypotheses for the proper-row theorem. Only this existing pending candidate is strengthened; no unrelated broad candidate is opened. The scalar helper is generic, but the final row payment uses actual signed Boolean-cell minimum weights. No independently reviewed downstream adoption is claimed.

## one next mathematical action and independent reviewer

A079/A033 reconstruct the scalar dominant-amplitude concavity branch and group-specific weighted Cauchy payment. A088/A094 audit complete conditional entropy, proper/complete distinction, every physical restriction and same-IY ownership. Review remains pending; no messages or peer writes were made. Next mathematical action: remove the accumulated group logarithmic-width/piece-count cost, or pay a bounded-piece arbitrary-core decomposition from the original unused influence. The scalar factor2 is already sharp, so pursuing it below2 is the wrong next mechanism.

## actual persistence receipts or precise save blocker

The four protocol artifacts, complete proof, frozen spec, scripts, five PASS outputs, source receipts and explicit Lean admission hold are saved locally. PROGRESS and PACKET_DELTA are identical with packet_ids=[A034]. Exact protocol field sets, statement SHA256, helper hashes, artifact sizes and all final artifact hashes are checked in out/protocol_validation.json and out/artifact_receipts.json. STATUS has exactly two lines; dated WORKLOG and LEARNED entries record this stage. All files are below20MB. Independent acceptance, supervisor copying and GitHub/brain mirrors are unverified. No git, messaging, brain/shared-tree write or other agent mutation was used. Brain self-care remains degraded/unverified for stale owner-model, state-of-mind and dream guidance; current task files and self-contained mathematics supply this stage's evidence.

## Universal bridge

G-PHASE-COND advances by replacing a q-fold coherent-entropy cost with a sharp scalar factor2 and a group-specific square-root payment, reducing the complete proper-row bound from O(s^2 log s) to O(s log s), arbitrary-mass FOUR-cell rate292 to114, and adding rare FOUR-cell rate57. The full conditional spectrum, row-mass entropy and SAME original I_Y are retained throughout; the complete-source rate32 remains unchanged on its stronger domain. The universal unpaid step is the growing logarithmic-width/piece-count bill or its influence-priced arbitrary-core decomposition, not an omitted terminal or a mass-disparity case. NEXT targets that remaining geometric source cost because further improvements to the already sharp scalar factor cannot supply a dimension-independent full-FEI constant.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='')
audit='''# Internal adversarial review, not independent acceptance

The hardest new step is scalar signed cancellation near a unit amplitude. The proof uses both the l1<=1 hypothesis and concavity of -z ln z; its actual negative control drops only l1 and fails. The factor2 sharpness cases approach the dangerous unit endpoint, including k64. A generic normalization-only control would not suffice.

The extrapolation denominators 1-a^2 and1-t^2 are positive in the branch c<a<1,t<a. The a=1 and zero cases are separate. t>=2a-1 is positive because c>1/2, so its square is valid. The logarithm uses F(0)=0 by continuity. Euclidean triangle is applied to finite entropy-amplitude vectors, not to correlated random coordinates. No independence of spectral auxiliaries is invoked.

The full bill B includes row-mass entropy. Disjoint physical ternary values give the coefficientwise l1<=mu condition; normalization of an arbitrary real wavefunction does not. Rare activation preserves a physical Boolean/ternary construction and retains its fresh-coordinate energy. Source maps restrict separately, including unequal ranks.

The old group energy estimate is reconstructed with6/11, tested by an independent bit-mask correlation implementation. Equal-scale cancellation stays within groups; comparing original components is false on constant covers and is not used. The one-group case is handled directly rather than forcing the q>=2 algebra.

The group-size inequality log2(m)<=m-1 holds for every positive integer by induction2^(m-1)>=m. All L_g are positive; weighted Cauchy uses no division by zero. At most-s rows use monotonic displayed constants; a single cell has the direct boundC. The proper-row114, rare-row57 and complete-source32 apply to different hypotheses.

Unresolved: no bound independent of growing pieces, no arbitrary-core original-influence-priced bounded-piece decomposition, no independent acceptance. The Lean rounding source was NOT compiled after memok returned1; no formal certificate is claimed.
'''
(out/'INTERNAL_REVIEW.md').write_text(audit,encoding='utf-8',newline='')
(A/'STATUS.md').write_text(f'STATE: A034 stage22 v5 saved: COMPLETE proper-row transfer O(s log s), FOUR-cell<114 (was292), rare<57; {total} exact assertions PASS; source32 unchanged; review pending, Lean not started; FEI OPEN.\nNEXT: A079/A033/A088/A094 audit scalar cancellation and weighted group payment; remove accumulated logarithmic-width/piece-count cost or influence-price arbitrary-core bounded-piece decomposition.\n',encoding='utf-8',newline='')
tag='A034-stage22-v5-signed-scalar-entropy'
entry=f'\n{stamp} {tag}: full proof and exact finite validation saved. Scalar factor2 is sharp, yields O(s log s) vs prior O(s^2 log s); proper FOUR-cell<114, rare<57, complete-source32 unchanged. {total} assertions PASS; no compiler after memok1; review pending, full FEI OPEN.\n'
for name in ['WORKLOG.md','LEARNED.md']:
    f=A/name
    if tag not in read(f):
        with f.open('a',encoding='utf-8',newline='') as stream:stream.write(entry)
durable='''\nStage22 mechanism: for phi(t)=sqrt(-t^2 ln t^2), sum|a_j|<=1 implies phi(|sum a_j|)<=sqrt2 sum phi(|a_j|); sum|a_j|<=1/2 gives factor1. Dominant amplitude a>exp(-1/2) forces t^2>=2a^2-1 and concavity pays factor2. For disjoint ternary physical groups, sqrt(Btotal)<=sqrt2 sum sqrt(Bg). Use group-specific Lg, not q*maxLg: B<=2(sumLg)(sumEg), Etotal>=6/11 sumEg. Group sizes m sum to s; sumLg<=(s-2)(1+log(64s^2))+2(3+loge) at q>=2. This improves complete proper-row cost to O(s log s), general FOUR<114 and rare FOUR<57. All source restrictions/tensor guards remain; complete-source FOUR32 is a separate stronger-hypothesis bound. Scalar factor2 is sharp, so NEXT must attack remaining geometric group-width/piece complexity, not seek scalar<2.\n'''
if 'Stage22 mechanism:' not in read(A/'LEARNED.md'):
    with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(durable)
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
pf=json.loads(read(protocol))['required_per_run']
assert set(progress)=={s.split(' (')[0] for s in pf['progress_fields']}
assert set(claim)==set(pf['claim_fields'])
assert all(f in report for f in pf['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
sources=[protocol,Path(r'BOARD.md'),Path(r'claude\B07\STREAM_NOTES.md'),R.parent/'20261026T214048Z-account04-A034-phase-energy-transfer/PROOF.md',R.parent/'20261026T214048Z-account04-A034-phase-energy-transfer/code/check.py']
save(out/'source_receipts.json',[dict(path=str(p),sha256=sha(p),scope='targeted current reads; full mathematics reconstructed in PROOF') for p in sources])
save(out/'protocol_validation.json',dict(status='PASS',timestamp=stamp,progress_fields=sorted(progress),claim_fields=sorted(claim),report_fields=pf['report_fields'],exact_assertions=total,compatibility_identical=True,lean='NOT_STARTED_MEMOK_HOLD',full_fei='OPEN'))
files=[p for p in R.rglob('*') if p.is_file() and p.name!='artifact_receipts.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(out/'artifact_receipts.json',[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files])
assert all(sha(R/x['path'])==x['sha256'] for x in json.loads(read(out/'artifact_receipts.json')))
print(json.dumps(dict(status='FINAL_VERIFIED_LOCAL',exact_assertions=total,files=len(files)+1,claim_version=5,proper_four_rate='<114',rare_four_rate='<57',full_fei='OPEN',independent_review='PENDING',lean='NOT_STARTED_MEMOK_HOLD')))
