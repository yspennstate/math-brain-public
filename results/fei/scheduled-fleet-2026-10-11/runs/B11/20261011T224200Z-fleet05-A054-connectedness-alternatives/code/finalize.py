from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every indicator g with actual connected components g_k and a component-isolating physical block A, '
'raw bit Fourier entropy satisfies F(g)<=sum_k F(g_k)+Gamma_A, with Gamma_A=[B_A(g)+(2/ln2)E_A(g)-sum_k Lambda_A(g_k)]_+, '
'B_A the mass-weighted conditional selector spectral entropy and Lambda_A=B_A+(1/ln2)sum_t Ent(v_t^2). '
'If a proper block A of size r has components R_k x V_k with disjoint subcube selectors R_k fixing d_k>=r/2 coordinates, '
'then Lambda_A(g_k)=2d_k M(g_k)=4E_A(g_k), Gamma_A<=(2/ln2)E_A(g), and Rraw(g)<=max_k Rraw(g_k)+(2/ln2)E_A(g)/E(g). '
'If all proper physical indicator restrictions have ratio at most Rraw(g), then Rraw(g)<=4+2/ln2. '
'For the actual sign f=1-2g, if all proper physical restrictions have ratio at most H(f)/I(f) and M(g)>=p0>0, '
'then H(f)/I(f)<=2/ln2+1/p0. Threshold-critical signs with positive H-KI and nonpositive proper-child deficits are excluded at K>=2/ln2+1/p0. '
'Universal separator or density admission is not asserted.')
hypotheses=['Finite uniform cube; all new entropies in bits; raw indicator energy E differs from sign influence I=4E',
'Component-isolating means each physical A-fiber meets at most one actual connected component',
'Thin-cylinder payment requires actual components with disjoint subcube selectors fixing at least half the block coordinates and connected nonempty data supports',
'Critical conclusions require a proper nonempty selector block and the stated all-proper-physical-restriction comparison; positive energies for ratios',
'Sign critical bound additionally requires support mass M(g)>=fixed p0>0; no inherited child criticality or universal class admission']
claim=dict(claim_id='A054-COMPONENT-EXCESS-PAID-THIN-SEPARATOR',version=1,exact_statement=statement,hypotheses=hypotheses,
statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hypotheses),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
contributors=['fleet05/A054'],proof_source=dict(path=str(ROOT/'CRITICAL_INTERFACE_PAYMENT.md'),sha256=sha(ROOT/'CRITICAL_INTERFACE_PAYMENT.md'),locator='sections 1--5'),
proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_EXACT_VALIDATION_PASSED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
next_consumers=['A052','A055','A026','A028','A090','A094','B20'])
save(ROOT/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B11',packet_id='A054',gap_id='FEI-B11-A054-INITIAL',attempt_id='A054-component-interface-1',
method='Raw partial-Fourier block ledger with mass-tilt; subcube cylinder credits; exact arithmetic controls; source-bound independent A052 review',
mathematical_delta='Controlled component excess proved and interface paid at (2/ln2)E_A on thin-cylinder geometry; critical raw bound 4+2/ln2; critical sign bound 2/ln2+1/p0. Universal admission remains open.',
deliverable_status='COMPLETE_SAVED_LOCAL',mathematical_status='PACKET_TARGET_PROVED_AT_STATED_CLASS_FULL_FEI_OPEN',claim_versions_used=[],
claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],
source_artifacts=['REPORT.md','COMPONENT_EXCESS.tex','CRITICAL_INTERFACE_PAYMENT.md','REVIEW_A052.md','out/EXACT_CHECK.json','out/SOURCE_MANIFEST.json'],
next_consumers=claim['next_consumers'],next_action='Test explicit component Lambda credits beyond subcube cylinders against all-proper-descendant criticality, retaining mass tilt and terminal cost; independent A090/A094 review.',
stagnant_substantive_attempts=0,blockers=['Universal critical separator geometry and uniformly positive support mass are unproved','Supervisor adoption, mirror verification and independent A054 review pending','B11 lead notes absent'],packet_ids=['A054'])
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
status='STATE: A054 packet complete locally: paid component interface and critical thin-cylinder exclusion proved; 48,045 exact checks PASS; A052 analytically reviewed; full FEI OPEN.\nNEXT: A090/A094 review; A052/A055 test explicit component Lambda credits beyond subcube selectors under all-descendant criticality, retaining mass tilt and terminal cost.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-12 completion: Full checker PASS, 278 indicators, 1846 block cases including historical controls, 507 thin-cylinder fixtures and 48,045 exact assertions in 7.742993 helper seconds. Saved one bundled claim and source-bound A052 analytic review. First universal gap: critical-source separator/density admission.\n')
manifest=json.loads((ROOT/'out/SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
other=Path('~/brain_workers/FEI100_20261011/agents')
extra=list((other/'A052/runs').glob('*/CRITICAL_SOURCE_STRUCTURE.tex'))+list((other/'A052/runs').glob('*/CLAIMS.json'))+list((other/'A052/runs').glob('*/out/COMPONENT_RATIO_SOURCE.md'))
for who in ['A051','A052','A053']:extra+=list((other/who/'runs').glob('*/REPORT.md'))
for p in extra:manifest.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,encoding='utf-8',role='analyzed B11 source'))
save(ROOT/'out/SOURCE_MANIFEST.json',manifest)
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=AGENT/name;receipts.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
save(ROOT/'out/RECEIPTS.json',receipts)
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
ckeys=set(protocol['required_per_run']['claim_fields']);pkeys=set(protocol['required_per_run']['progress_fields']);pkeys.remove('packet_ids (one primary ID, for compatibility)');pkeys.add('packet_ids')
assert set(claim)==ckeys and set(progress)==pkeys
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
print(json.dumps(dict(status='SAVED_AND_SCHEMA_CHECKED',receipts=len(receipts),run=str(ROOT),claims=1,full_fei='OPEN'),indent=2))
