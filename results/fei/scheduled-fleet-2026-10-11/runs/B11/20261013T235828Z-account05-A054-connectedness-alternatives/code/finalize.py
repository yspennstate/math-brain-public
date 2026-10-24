from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dyadic(v):return F(v)
def outward(vals,places=6):
 s=10**places;a,b=map(F,vals)
 lo=a.numerator*s//a.denominator;hi=-((-b.numerator*s)//b.denominator)
 return [f'{lo//s}.{lo%s:0{places}d}',f'{hi//s}.{hi%s:0{places}d}']
check=json.loads((ROOT/'out/EXACT_CHECK.json').read_text());assert check['status']=='PASS'
phi=json.loads((ROOT/'out/BRAIN45_PHI_EXACT.json').read_text())
summary=dict(sign_phi=outward(phi['sign_phi']['bit_ratio_interval']),raw_phi=outward(phi['raw_phi']['bit_ratio_interval']),root_sign_ratio=outward(phi['root_sign_ratio_bits']),sign_masks=phi['sign_phi']['masks'],raw_masks=phi['raw_phi']['masks'])
save(ROOT/'out/PHI_DISPLAY.json',summary)
statement=('For every finite-cube indicator g partitioned into actual connected components g_k, every nonempty proper physical block A of size r has signed raw-block cross term X_A=Lambda_A(g)-sum_k Lambda_A(g_k), and raw component excess equals X_A plus the averaged labelled child excess. '
'Let R_k be physical component projections on A, mu_k=|R_k|/2^r, p_k=E g_k, p=sum_k p_k and Q_A=sum_k p_k log2(1/mu_k). Then Lambda_A(g_k)>=2p_k log2(1/mu_k) and E_A(g_k)>=p_k log2(1/mu_k)/2 without Cartesian structure. '
'If the projections are disjoint, Gamma_A=[B_A(g)+(2/ln2)E_A(g)-sum_k Lambda_A(g_k)]_+ bounds the raw component excess and is at most (2/ln2)E_A(g)+[rp-2Q_A]_+. '
'In the class Q_A>=rp/2 the interface is paid at (2/ln2)E_A(g), E_A(g)>=rp/4, and physical raw-ratio criticality forces Rraw<=4+2/ln2. '
'For f=1-2g, physical sign-ratio criticality plus p>=p0>0 forces H/I<=2/ln2+1/p0; dimension-minimal positive H-KI violations are excluded at K>=2/ln2+1/p0. '
'Brain45 sign phi over all126 proper cuts is uniquely minimized at mask15, and its raw phi is minimized exactly at masks3,5,6,9,10,12; strict sign own-ratio descent holds. No universal separator or density admission is asserted.')
hyp=['Finite uniform cube; new entropy units bits; raw indicator Fourier entropy F and energy E differ from sign H and I=4E',
'Gamma comparison requires disjoint physical component projections; otherwise labelled terminal excess is explicitly retained',
'Projection-payment class requires Q_A>=r p/2; no Cartesian, subcube or uniform fiber assumption',
'Critical ratio conclusions require comparisons for every actual proper physical restriction and positive energy; no component deletion as descendant',
'Actual sign critical bound additionally requires fixed p0>0 and p>=p0; dimension-minimality is among all Boolean fixed-K violators',
'Brain45 is the fixed star on four data bits times full three-control cube plus the opposite singleton, in the declared coordinate orientation']
claim=dict(claim_id='A054-COMPONENT-EXCESS-PROJECTION-PAYMENT',version=1,exact_statement=statement,hypotheses=hyp,
statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
contributors=['account05/A054'],proof_source=dict(path=str(ROOT/'PROJECTION_PAYMENT.md'),sha256=digest(ROOT/'PROJECTION_PAYMENT.md'),locator='sections1--5; out/BRAIN45_PHI_EXACT.json for finite control'),
proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_EXACT_CERTIFICATES_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=['A054-COMPONENT-EXCESS-PAID-THIN-SEPARATOR@1 geometric scope; original version retained'],refutes=[],first_unproved_line=None,next_consumers=['A052','A055','claude/B11','A090','A094','B20'])
save(ROOT/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B11',packet_id='A054',gap_id='FEI-B11-A054-INITIAL',attempt_id='A054-projection-cross-term-2',
method='Physical-support uncertainty plus indicator edge isoperimetry; terminal-inclusive component cross ledger; exact126-cut Brain45 descent',
mathematical_delta='Removed Cartesian/subcube assumptions from paid component interface using weighted physical projection sparsity; critical raw/sign exclusions extended. Brain45 sign phi uniquely at mask15 with strict own-ratio descent; raw minima six two-data-bit blocks. A052 phase exclusion analytically reviewed.',
deliverable_status='COMPLETE_SAVED_LOCAL',mathematical_status='GENERALIZATION_PROVED_AT_STATED_SCOPE_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],
source_artifacts=['REPORT.md','PROJECTION_PAYMENT.md','COMPONENT_EXCESS.tex','REVIEW_A052_PHASE.md','out/EXACT_CHECK.json','out/BRAIN45_PHI_EXACT.json'],next_consumers=claim['next_consumers'],
next_action='Test component projection debt and labelled child cross term on a genuinely child-certified disconnected source, preserving support mass and terminal deficit; A090/A094 reconstruct new projection credits.',
stagnant_substantive_attempts=0,blockers=['Universal proper-separator and positive-density admission remain unproved; connected support has only one component','Independent A054 review, shared-index adoption and remote mirrors pending'],packet_ids=['A054'])
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
save(ROOT/'out/REVIEW_RECORDS.json',[dict(claim_id='A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION',version=1,reviewer='account05/A054',verdict='ACCEPT_AT_STATED_SCOPE',method='Independent analytic reconstruction of row-phase admission, coupling and terminal-deficit line; no repair',source='REVIEW_A052_PHASE.md',registry_adoption='PENDING')])
paths=[Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B11/STREAM_NOTES.md'),Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
paths+=list((Path('~/brain_workers/FEI100_20261011/claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring')).glob('REPORT.md'))
a52=Path('~/brain_workers/FEI100_20261011/agents/A052/runs')
paths+=list(a52.glob('*/REPORT.md'))+[a52/'20261013T221539Z-account05-A052-critical-source-structure'/x for x in ['CRITICAL_PHASE_PROOF.md','CLAIMS.json']]
paths+=[AGENT/'runs/20261011T224200Z-account05-A054-connectedness-alternatives'/x for x in ['REPORT.md','CRITICAL_INTERFACE_PAYMENT.md','CLAIMS.json','code/check_components.py']]
save(ROOT/'out/SOURCE_MANIFEST.json',[dict(path=str(p),sha256=digest(p),bytes=p.stat().st_size) for p in paths])
(AGENT/'STATUS.md').write_text('STATE: A054 projection-interface generalization proved: Cartesian assumptions removed; Brain45 unique sign phi at mask15; 27,032 exact checks PASS; A052 phase claim reviewed; full FEI OPEN.\nNEXT: A090/A094 review; A052/A055 test projection debt plus labelled child cross terms on genuinely critical disconnected sources, retaining support mass and terminal deficit.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 / stage 20261013T235828Z: Read BOARD23:49Z, B11 leadv2 and own status. Prior 20261012 stage contains only supervisor .final marker, no mathematical artifact; no second-stage proof assumed. Independently accepted A052 Boolean-phase exclusion analytically without repair. Proved projection credit Lambda_k>=2p_k log2(1/mu_k), indicator energy>=p_k log2(1/mu_k)/2 and terminal-inclusive cross ledger; paid class no longer needs Cartesian/subcube components. Syntax typo before computation preserved and corrected. Pilot189 checks/0.103561s; full27032 checks/12.948700s, 64 skew fixtures (60 non-Cartesian), all126 Brain45 cuts. Sign phi unique mask15, raw minima six two-data-bit masks; sign strict own-ratio descent. Universal separator/density admission remains open. Required files saved/schema-checked.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 durable extension: For any component with physical A-projection measure mu and mass p, every partial Fourier row is supported in that projection. Its normalized Fourier entropy and its physical row density KL are each >=log2(1/mu), yielding Lambda_A>=2p log2(1/mu). Fiberwise indicator edge isoperimetry gives E_A>=p log2(1/mu)/2. Disjoint projections and weighted Q_A>=|A|M(g)/2 pay Gamma_A<=kappa E_A without product shape. For non-isolating blocks excess=X_A+mean labelled child excess; terminal component cross terms cannot be discarded. Brain45 sign phi is uniquely mask15; raw phi minimizes at any two of the four data bits. This control is not a critical descent obstruction.\n')
protocol=json.loads(paths[2].read_text())
ckeys=set(protocol['required_per_run']['claim_fields']);pkeys=set(protocol['required_per_run']['progress_fields']);pkeys.remove('packet_ids (one primary ID, for compatibility)');pkeys.add('packet_ids')
assert set(claim)==ckeys and set(progress)==pkeys
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p)))
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=AGENT/name;receipts.append(dict(path=str(p),bytes=p.stat().st_size,sha256=digest(p)))
save(ROOT/'out/RECEIPTS.json',receipts)
print(json.dumps(dict(status='SAVED_AND_SCHEMA_CHECKED',receipts=len(receipts),phi_display=summary,full_fei='OPEN'),indent=2))
