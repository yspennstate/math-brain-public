from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

run=Path(__file__).resolve().parents[1]
workspace=run.parents[1]
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
proof=str(run/'DERIVATION.md')
consumers=['A067','A070','A088','A094','B20']
statements=[
    ('A066-HEAT-ENTROPY-IDENTITY',
     'For every Boolean sign f on every finite uniform cube, with p_S=hat(f)(S)^2, I=sum |S|p_S, H_nat=sum p_S ln(1/p_S), T_t=exp(-tL), L chi_S=|S|chi_S, q_t(S)=p_S exp(-2t|S|), G_f(t)=sum q_t(S)ln(1/p_S) and J_f(t)=sum |S|q_t(S)ln(1/p_S), G_f prime=-2J_f and H_nat=p_empty ln(1/p_empty)+2 integral_0^infinity J_f. The boundary term is between zero and I; J_f(t)<=J_f(0) and J_f(t)<=exp(-2t)J_f(0), giving integrability at both endpoints for every fixed f. For n>=1, J_f(0)<=2(n-1)ln(2)I. A universal integral bound integral J_f<=KI implies FEI in bits with constant (1+2K)/ln(2), and FEI with bit constant C implies that integral bound with K=C ln(2)/2.',
     [], []),
    ('A066-NO-INTEGRABLE-HEAT-ENVELOPE',
     'There is no nonnegative measurable k with finite integral on (0,infinity) such that J_f(t)<=I(f)k(t) for every finite-dimensional Boolean sign f and almost every t. For f_n(x)=1-2 indicator{x=(1,...,1)}, n>=2, J_f_n(t)/I(f_n)=(2n-2)ln(2)exp(-2t)((1+exp(-2t))/2)^(n-1). Any such pointwise envelope must be at least ln(2)exp(-3/2)/t almost everywhere on (0,1/4]. Nevertheless integral J_f_n/I(f_n)=2(1-1/n)(1-2^(-n))ln(2)<=2ln(2). This refutes the integrable pointwise-envelope helper, not the integrated target or FEI.',
     [{'claim_id':'A066-HEAT-ENTROPY-IDENTITY','version':1}],
     ['Universal integrable pointwise influence envelope for J_f'])
]
claims=[]
for cid, statement, deps, refutes in statements:
    claims.append(dict(claim_id=cid,version=1,exact_statement=statement,
        hypotheses=['Finite uniform cube','Boolean outputs in {-1,1}','Natural logarithms; zero mass contributes zero','J_f as defined in DERIVATION.md'],
        statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),
        contributors=['fleet05/A066'],proof_source=proof,proof_dependencies=deps,
        review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
        supersedes=[],refutes=refutes,first_unproved_line=None,next_consumers=consumers))

progress=dict(protocol_revision=protocol['revision'],run_id=run.name,stream='B14',packet_id='A066',
    gap_id='G-A066-HEAT-INTEGRAL',attempt_id='A066-heat-flow-01',
    method='Exact Fourier heat semigroup; corrected entropy functional; analytic point-defect spike obstruction; bounded rational verification',
    mathematical_delta='Exact heat-flow identity with paid constant-mode boundary and fixed-function endpoint bounds; universal integrable pointwise influence-envelope helper refuted by actual Boolean point defects. The dimension-independent integrated influence payment remains open.',
    deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',
    mathematical_status='IDENTITY_AND_ROUTE_OBSTRUCTION_AUTHOR_PROVED; FULL_FEI_OPEN',
    claim_versions_used=[],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1} for c in claims],
    source_artifacts=['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCE_READ_RECEIPTS.json'],
    next_consumers=consumers,next_action='Audit both claims independently, then seek a dyadic-time influence charge summable for each function; do not use a universal integrable pointwise envelope for J_f.',
    stagnant_substantive_attempts=0,blockers=['B14 STREAM_NOTES.md absent at supplied path; independent work proceeded.','Universal integral J_f <= K I(f) has no proof in this run.'],
    packet_ids=['A066'])

for filename,data in [('CLAIMS.json',claims),('PROGRESS.json',progress),('PACKET_DELTA.json',progress)]:
    (run/filename).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

now=datetime.now(timezone.utc).isoformat()
(workspace/'STATUS.md').write_text('STATE: A066 heat-semigroup packet complete locally: exact entropy identity and endpoint bounds; integrable universal pointwise envelope refuted; independent review pending; full FEI OPEN.\nNEXT: A070/A088/A094 audit; seek a summable per-function dyadic-time influence charge for G-A066-HEAT-INTEGRAL.\n',encoding='utf-8')
if not (workspace/'WORKLOG.md').exists() or run.name not in (workspace/'WORKLOG.md').read_text(encoding='utf-8'):
    with (workspace/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write(f'\n{now} — {run.name}: Read protocol/board and source state; lead notes absent. Derived corrected heat entropy G=F-2tE, exact H_nat=b+2 integral J, fixed-function integrability at both endpoints. Point defects force every universal pointwise envelope to dominate c/t, although each defect has integral J/I<=2ln2. Saved analytic proof and two review-pending claims. Exhaustive n<=3 plus defects n=2..8 passed 6999 integer/Fraction assertions in 0.0993s. Source scan required CP1252 fallback. Full FEI and integrated influence payment remain open. No shared-tree writes or mirroring performed.\n')
if not (workspace/'LEARNED.md').exists() or 'A066 heat-flow v1:' not in (workspace/'LEARNED.md').read_text(encoding='utf-8'):
    with (workspace/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write('\nA066 heat-flow v1: With cube generator L chi_S=|S|chi_S, q_t=p_S exp(-2t|S|) is unnormalized. Its raw entropy F has derivative of mixed sign (dictator F=2t exp(-2t)). G=F-2t sum |S|q_t has derivative -2J, J=sum |S|q_t ln(1/p_S). H_nat=p_empty ln(1/p_empty)+2 integral J, with boundary <=I. Fixed finite f has J<=J(0) near zero and J<=exp(-2t)J(0) at infinity. Full FEI is equivalent, up to that paid boundary, to a universal integrated J payment. Actual point defects force any universal pointwise envelope J/I to exceed ln(2)exp(-3/2)/t near zero, so no integrable universal envelope works. Their individual area J/I=2(1-1/n)(1-2^(-n))ln2 is bounded. Do not exchange supremum across functions with time integration. The identity only uses normalization; Boolean structure is needed for any dimension-free payment. Gamma ledger equations (2) and (6) pay distinct lifetime and dissipation quantities. All authored claims remain pending independent review.\n')

expected_claim=set(protocol['required_per_run']['claim_fields'])
# The protocol annotates packet_ids in its field list; its compatibility section
# and the owner's explicit instruction specify the actual JSON key packet_ids.
expected_progress={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert all(set(c)==expected_claim for c in claims)
assert set(progress)==expected_progress
assert json.loads((run/'PROGRESS.json').read_text())==json.loads((run/'PACKET_DELTA.json').read_text())
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert len((workspace/'STATUS.md').read_text().splitlines())==2
check=json.loads((run/'out'/'CHECK.json').read_text())
assert check['status']=='PASS' and check['assertions']==6999
assert len(json.loads((run/'out'/'SOURCE_READ_RECEIPTS.json').read_text(encoding='utf-8')))==33
schema=dict(status='PASS',claim_count=len(claims),claim_fields_exact=True,progress_fields_exact=True,report_fields_present=True,packet_delta_identical=True,status_two_lines=True,field_label_interpretation='packet_ids (one primary ID, for compatibility) denotes JSON key packet_ids, as specified by protocol compatibility.run_delta and owner instruction')
(run/'out'/'SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2)+'\n',encoding='utf-8')

paths=[p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
paths += [workspace/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[]
for p in paths:
    data=p.read_bytes()
    assert len(data)<20*1024*1024
    receipts.append(dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
manifest={'saved_at_utc':now,'status':'LOCAL_SAVE_VERIFIED','files':receipts,'mirror_status':'NOT_PERFORMED_OR_VERIFIED','independent_review_status':'PENDING'}
(run/'out'/'PERSISTENCE.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
for record in receipts:
    assert hashlib.sha256(Path(record['path']).read_bytes()).hexdigest()==record['sha256']
print(json.dumps({'schema':schema,'persisted_files_verified':len(receipts),'full_fei':'OPEN'},indent=2))
