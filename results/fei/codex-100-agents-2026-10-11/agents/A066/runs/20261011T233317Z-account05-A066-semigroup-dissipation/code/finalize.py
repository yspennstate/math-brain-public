from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

run=Path(__file__).resolve().parents[1]
workspace=run.parents[1]
old=workspace/'runs'/'20261011T214539Z-account05-A066-semigroup-dissipation'
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
dependency={'claim_id':'A066-HEAT-ENTROPY-IDENTITY','version':1,
    'proof_source':str(old/'DERIVATION.md'),
    'acceptance_scope':'Source-bound independent A067 and A088 acceptance at stated scope; central adoption not asserted'}
consumers=['A067','A070','A064','A088','A094','B06','B20']
statements=[
 ('A066-POSITIVE-RESTRICTION-HEAT-LEDGER',
  'For every Boolean sign f on a finite uniform cube and physical block B, K(f)=integral J_f=(H_nat(f)-p_empty ln(1/p_empty))/2 obeys 2[K(f)-E_y K(f_y)]=M_B^+ + C_B^+ + ell_B, where q_T=sum_{U subset B}p_{U union T}=E_y p_y(T), M_T=sum_U p_{U union T}ln(q_T/p_{U union T}), C_T=E_y p_y(T)ln(p_y(T)/q_T), plus omits T=empty, and ell_B=sum_{nonempty U subset B}p_U ln(1/p_U). All three terms are nonnegative. For B={i}, C_i^+<=2 Inf_i and ell_i<=(2/e)Inf_i. The identity telescopes in every finite physical stopping tree, with retained terminal K and cumulative channel-plus-level cost <=(2+2/e)[I(f)-E I(leaf)]. If R_nat=sum_i M_i^+ and B_nat=sum_i H_nat(S_i|S_without_i), then 0<=B_nat-R_nat<=(1+2/e)I. Moreover R_nat(y product_{j=1}^m g(x^(j)))=m B_nat(g) and I=m I(g)+1, so the optimal universal constants for R_nat/I and B_nat/I are equal. A universal R_nat<=A I implies FEI in bits with constant (A+2)/ln2 via C018; no such A is proved here.',
  ['Channel-only restriction heat payment; refuted by majority calibration in second claim']),
 ('A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION',
  'For odd majority n=2m+1 and alpha=binom(2m,m)/2^(2m), every singleton physical restriction has M_i=C_i=0 and K(parent)-E K(child)=alpha^2 ln(1/alpha^2)/2, with ratio to Inf_i equal to alpha ln(1/alpha)<=1/e. Thus no finite A bounds that heat drop by A times its C006 channel term, already for Maj3. For F_{a,r}=Addr_a-2 indicator{all inputs +1} with a>=1, k=a+2^a, r>=1, D=k+r and delta=2^(-D), and any b padding coordinates, 1<=b<=r, the exact signed three-class row formulas (9)-(11) of DERIVATION.md compute the heat drop, conditional erasure, channel and level mass. For fixed a,b as r grows, M_B/I_B and C_B/I_B tend to 2ln2 and the heat-drop ratio tends to 2ln2. For b=r, rho=4^a/2^k, the erasure/channel limits are 2(1+rho)ln2 and 2(1-rho)ln2, the heat limit remains 2ln2, and the lost-level limit is 4ln2/2^k. All limits are analytic, not finite-grid extrapolations.',
  ['Universal K(f)-E K(f_y) <= A C_B for finite A, with no separate level term'])
]
claims=[]
for index,(cid,statement,refutes) in enumerate(statements):
    deps=[dependency] if index==0 else [{'claim_id':statements[0][0],'version':1}]
    claims.append(dict(claim_id=cid,version=1,exact_statement=statement,
      hypotheses=['Finite uniform cube; Boolean outputs in {-1,1}','Natural logarithms; entropy bits = nats/ln2','Zero-mass log terms vanish','Physical restrictions and actual coherent child Fourier coefficients'],
      statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['account05/A066'],
      proof_source=str(run/'DERIVATION.md'),proof_dependencies=deps,review_records=[],
      status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=refutes,
      first_unproved_line=None,next_consumers=consumers))
progress=dict(protocol_revision=protocol['revision'],run_id=run.name,stream='B14',packet_id='A066',
 gap_id='G-A066-HEAT-INTEGRAL',attempt_id='A066-restriction-heat-02',
 method='Physical Fourier-row decomposition of the reviewed heat integral; paid singleton level/channel charges; exact arbitrary-core admission and family certificates',
 mathematical_delta='Exact positive block heat drop and stopping-tree ledger; singleton level cost <=(2/e)Inf_i and channel <=2Inf_i nats. Nonempty-context erasure has the same optimal universal constant as C018. Majority and point-defected address block formulas and analytic limits checked exactly in finite domains.',
 deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',
 mathematical_status='RESTRICTION_LEDGER_AND_CALIBRATION_AUTHOR_PROVED; UNIVERSAL_C018_RESIDUAL_AND_FEI_OPEN',
 claim_versions_used=[dependency],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1} for c in claims],
 source_artifacts=['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','EMBEDDING_SPEC.json','code/check_restrictions.py','code/check_embedding.py','out/CHECK_FULL.json','out/EMBEDDING_CHECK.json'],
 next_consumers=consumers,
 next_action='A088/A094 audit the positive row ledger and exact C018 admission; attack R_nat<=A I with full signed Boolean identities and test every proposed payment on arbitrary-core y*g^m, preserving terminal entropy.',
 stagnant_substantive_attempts=0,blockers=['No universal bound on the retained nonempty-context erasure residual.'],packet_ids=['A066'])
for name,data in [('CLAIMS.json',claims),('PROGRESS.json',progress),('PACKET_DELTA.json',progress)]:
    (run/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

sources=[protocol_path,old/'DERIVATION.md',old/'CLAIMS.json',
 Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),
 Path(r'~\brain_workers\FEI100_20261011\claude\B14\STREAM_NOTES.md'),
 Path(r'~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\REVIEW_A066.md'),
 Path(r'~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\REPORT.md'),
 Path(r'~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\REPORT.md'),
 Path(r'~\brain_workers\FEI100_20261011\claude\B14\runs\20261011T224500Z-claude-B14-granularity-neutralization\CLAIMS.json'),
 Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\BLOCK_RESTRICTION_IDENTITY_2026-09-18.md')]
source_receipts=[]
for p in sources:
    data=p.read_bytes()
    source_receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
        'scope':'Source bytes read; stage report specifies targeted versus complete textual review. Mutable board/notes hash is the current save-time observation, not a claim of an immutable campaign commit.'})
(run/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(source_receipts,indent=2)+'\n',encoding='utf-8')

full=json.loads((run/'out'/'CHECK_FULL.json').read_text())
embedding=json.loads((run/'out'/'EMBEDDING_CHECK.json').read_text())
assert full['status']==embedding['status']=='PASS'
assert full['counts']=={'exhaustive_blocks':1844,'majority_blocks':24,'direct_address_blocks':20,'histogram_blocks':33}
assert full['assertions']==29463
now=datetime.now(timezone.utc).isoformat()
(workspace/'STATUS.md').write_text('STATE: A066 stage 2 complete locally: positive restriction heat ledger, singleton level/channel paid, exact C018 constant admission; majority/address certificates PASS; new claims review pending; FEI OPEN.\nNEXT: A088/A094 audit; bound nonempty-context erasure R_nat using full signed Booleanity, testing arbitrary-core y*g^m and retaining stopping-tree terminal entropy.\n',encoding='utf-8')
if not (workspace/'WORKLOG.md').exists() or run.name not in (workspace/'WORKLOG.md').read_text(encoding='utf-8'):
    with (workspace/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write(f'\n{now} — {run.name}: Consumed BOARD 23:29 and B14 v2; original A066 claims independently accepted by A067/A088 at scope. Derived 2 Delta K=M_B^+ + C_B^+ + ell_B, positive under every physical restriction. Singleton level <=2/e influence, channel <=2 influence (nats); tree telescope keeps leaves. R_nat and C018 erasure have exactly the same optimal universal constant by character/tensor admission. Closed Maj_n singleton formula and all padding-block defected-address histograms/limits. Pilot 796 checks; full 29463 checks in 15.4155s; embedding {embedding["assertions"]} checks in {embedding["runtime_seconds"]:.4f}s. Initial interval export exceeded Python digit limit; repaired by outward dyadic export and reran full job. Universal retained-erasure payment remains open.\n')
if 'A066 restriction heat v1:' not in (workspace/'LEARNED.md').read_text(encoding='utf-8'):
    with (workspace/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write('\nA066 restriction heat v1: K=(H_nat-b_empty)/2 is monotone under physical block restriction. Exact drop 2 Delta K=M_B^+ + C_B^+ + ell_B; plus excludes the empty residual Fourier row and ell_B is entropy of Fourier masses supported wholly in the erased block. Singleton C^+<=2 Inf_i and ell_i<=2/e Inf_i use one physical influence budget. The level bound needs Boolean |hat(f)({i})|<=Inf_i; normalized singleton real spectra violate it. R_nat=sum M_i^+ differs from full erasure B_nat by at most (1+2/e)I, but their optimal universal constants are exactly equal: R_nat(y*g^m)=m B_nat(g), I=mI(g)+1. Deleting an empty context does not evade arbitrary tensor cores. Odd majority has zero singleton M,C yet positive heat drop alpha^2 ln(1/alpha^2)/2: the level mass becomes a child constant. Defected addressing fixed padding block has M/I,C/I->2ln2; full-padding proportions are 2(1+rho)ln2 and 2(1-rho)ln2, with heat ratio2ln2 and level ratio4ln2/2^k. Terminal entropy and retained M^+ remain unpaid universally. Exact interval exports should use outward dyadic rounding to avoid huge LCM-denominator string limits.\n')

assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
expected={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
assert (run/'PACKET_DELTA.json').read_bytes()==(run/'PROGRESS.json').read_bytes()
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.strip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert len((workspace/'STATUS.md').read_text().splitlines())==2
schema={'status':'PASS','claims':len(claims),'claim_fields_exact':True,'progress_fields_exact':True,
 'report_fields_complete':True,'final_universal_bridge_paragraph':True,'packet_delta_identical':True,
 'status_two_lines':True,'check_full_assertions':full['assertions'],'embedding_assertions':embedding['assertions']}
(run/'out'/'SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2)+'\n',encoding='utf-8')
paths=[p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
paths += [workspace/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[]
for p in paths:
    data=p.read_bytes(); assert len(data)<20*1024*1024
    receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(run/'out'/'PERSISTENCE.json').write_text(json.dumps({'saved_at_utc':now,'status':'LOCAL_SAVE_VERIFIED',
    'files':receipts,'mirror_status':'NOT_PERFORMED_OR_VERIFIED','new_claim_review_status':'PENDING'},indent=2)+'\n',encoding='utf-8')
for record in receipts:
    assert hashlib.sha256(Path(record['path']).read_bytes()).hexdigest()==record['sha256']
print(json.dumps({'schema':schema,'verified_local_files':len(receipts),'new_claim_review':'PENDING','full_fei':'OPEN'},indent=2))
