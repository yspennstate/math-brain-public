import json, hashlib
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[3]
run=Path(__file__).resolve().parents[1]
shared=root.parents[1]
oldrid='20261012T022241Z-account05-A068-antichain-beyond-one-order'
oldrun=root/'runs'/oldrid
rid=run.name
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
snapshot=run/'out/PREDECESSOR_REPORT.md'
snapshot.write_bytes((oldrun/'REPORT.md').read_bytes())
reviewdir=shared/'agents/A070/runs/20261013T212602Z-account05-A070-analytic-route-referee'
review=next(c for c in json.loads((reviewdir/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='A070-REVIEW-A068-REPORTED-CYCLIC-EDIT-REFERENCE')
assert sha(snapshot)==review['proof_source']['source_report_sha256']
base=json.loads((root/'runs/20261011T222313Z-account05-A068-antichain-beyond-one-order/CLAIMS.json').read_text(encoding='utf-8'))[0]
v=json.loads((run/'out/validation.json').read_text())
for c in v['cases']:
    for key in ['margin_to_8Ix_plus_2Iz_lower','entropy_margin_to_8Ix_plus_2Iz_lower']:
        c[key] = Fraction(c[key])
collision=json.loads((run/'out/collision.json').read_text())
assert v['status']=='PASS' and v['edit_case_count']==96 and v['assertions']==2589
dump(run/'out/SUMMARY.json',dict(edit_cases=96,base_cases=2,edit_exact_assertions=2589,collision_cases=32,collision_exact_assertions=196,total_current_exact_assertions=2785,edit_runtime_seconds=v['runtime_seconds'],minimum_complete_cost_margin_to_8Ix_plus_2Iz_lower=min(float(c['margin_to_8Ix_plus_2Iz_lower']) for c in v['cases']),minimum_entropy_margin_to_8Ix_plus_2Iz_lower=min(float(c['entropy_margin_to_8Ix_plus_2Iz_lower']) for c in v['cases']),minimum_margin_note='Display summaries only; exact outward intervals in validation.json are certificates',all_parameter_slack='287/1920 times base Ix',predecessor_report_sha256=sha(snapshot),predecessor_package_status='Interrupted; full validation and protocol files absent there. Preserved unchanged.',independent_review_scope='A070 accepts unchanged theorem; current full fixture package not part of that earlier review',full_FEI='OPEN'))

collision_text="""### 6. One identified private label: signed interface and failed inherited payment

For any Boolean F with distinct data coordinates 1,2 and arbitrary other coordinates, substitute x_2=epsilon x_1, epsilon in {+1,-1}, obtaining G. Index quotient subsets T by representatives excluding coordinate 2. Direct character substitution gives

    Ghat(T)=Fhat(T)+epsilon Fhat(T symmetric_difference {1,2}).

For any normalized parent reference R covering F's spectrum, define

    R_push(T)=R(T)+R(T symmetric_difference {1,2}).

The two-atom fibers partition the parent spectrum, so R_push is normalized and covers G. It satisfies Gamma_push(G)<=2 Gamma_R(F): use (a+epsilon b)^2<=2(a^2+b^2) and -log R_push(T)<=-log R(A) for either parent atom A. Terms with zero Fourier mass are omitted. This pays the parent cost, not the physical influence of G.

The naive universal replacement Gamma_push(G)<=K I(G) fails for every finite K. Take regular h=AND2 (output +1 only at (+1,+1)), constant quadratic orientations (+1,-1), and F(x_1,x_2)=h(x_1,-x_2). In spectral order empty,{1},{2},{1,2}, its coefficients are (-1/2,+1/2,-1/2,-1/2). Its accepted rank reference has weights (1/4,2/5,1/10,1/4), from level masses (1/4,1/2,1/4) and singleton rank weights proportional to (1,1/4). Identifying x_2=x_1 gives G=-1 but R_push=(1/2,1/2). Thus H(G)=I(G)=0 and Gamma_push(G)=1 bit. G itself has a free reference concentrated at the empty atom. This refutes the inherited payment, not FEI or existence of an adaptive paid output reference.

The frozen exhaustive 32-case two-bit check verifies the signed coefficient identity, factor-two inequality, Boolean normalization and influence with fresh truth tables, plus this exact reference witness. It does not certify larger colliding quadratic packets. The first unsupported line is a cancellation-aware normalized replacement reference paid by output influence, with all terminal entropy retained. A034's available stage-1 report still proposes its two-row collision ledger as NEXT; no completed ledger is assumed. These elementary identities carry no novelty claim against other streams' broader collision work.

"""
p=run/'REPORT.md'
s=p.read_text(encoding='utf-8').replace('# A068 / B14 stage 2:','# A068 / B14 stage 3:')
s=s.replace('The all-parameter proof is below; independent review of the new extension is pending.','The all-parameter proof is below. A070 independently accepted this unchanged theorem from the predecessor report; the full author validation package is completed here.')
s=s.replace('Read BOARD.md supervisor snapshot 2026-10-12 02:32 UTC,','Read BOARD.md supervisor snapshot 2026-10-13 23:39 UTC,')
source_add="""
This stage resumes the interrupted 20261012T022241Z run: its report and two-case pilots existed, but full validation and protocol package did not. The original run is preserved without modification. out/PREDECESSOR_REPORT.md preserves the exact report reviewed by A070 (SHA256 3c53ca43f4455a89c327a1671567e10bb825ce6d0b8dce5d4f943f859a0927be). Its premature persistence paragraph is not evidence of completion. All current completion statements refer exclusively to this run.

Read A070's 20261013T212602Z REPORT.md and source-bound claim A070-REVIEW-A068-REPORTED-CYCLIC-EDIT-REFERENCE v1. It reconstructs this all-parameter theorem without a mathematical repair and independently checks 16 edits with 1,932 exact assertions. Its acceptance covers the theorem and accepted base dependency, not previously absent author files. Read A034's stage-1 phase-energy REPORT.md: distinct data labels remain a hypothesis and the two-row collision ledger remains a proposed next action. No completed collision theorem is imported.

"""
s=s.replace('## complete derivation or exact first unsupported line',source_add+'## complete derivation or exact first unsupported line')
s=s.replace('## executed validation with domain, arithmetic, commands and outputs',collision_text+'## executed validation with domain, arithmetic, commands and outputs')
s=s.replace('    python -X utf8 runs/'+oldrid+'/code/check_edit.py --pilot\n','')
s=s.replace(oldrid+'/code/check_edit.py',rid+'/code/check_edit.py')
s=s.replace('Results and runtime are saved in out/pilot.json and out/validation.json and summarized in out/SUMMARY.json.','The predecessor v2 bounded pilot passed before the unchanged full job resumed here. Current out/validation.json records PASS on 96 edits and two base replays, 2,589 exact assertions, in 23.458 seconds. Results are summarized in out/SUMMARY.json. A separate frozen check, python -X utf8 runs/'+rid+'/code/check_collision.py, passed all 32 signed-identification cases and 196 assertions in under 0.01 seconds; see out/COLLISION_SPEC.json and out/collision.json.')
s=s.replace('their review is pending.','the unchanged theorem was independently reconstructed and accepted at stated scope by A070 from the preserved report. Current fixtures and the narrow collision obstruction remain available for further review.')
s=s.replace("Consume A034's independently developed two-row collision ledger before duplicating it, and apply it to the context-oriented quadratic rank reference: derive the signed paired Fourier coefficients and their normalized reference cost, retaining the regular-core terminal entropy and the already proved uniform-fallback repair.",'Use the signed paired coefficients above to construct an output reference refunding destructive cancellation at one identified pair in a quadratic-oriented regular core; retain terminal entropy and every normalization charge. A034 may supply a future ledger, but its available source does not yet do so.')
s=s.replace('Supervisor collection and independent review of the new theorem remain pending.',"Supervisor collection, shared-registry adoption, mirror verification and additional review remain pending. A070's source-bound theorem acceptance is already available and is distinct from these persistence states. The interrupted predecessor run has not been rewritten.")
s=s[:s.index('Universal bridge:')]+"""Universal bridge: this stage advances C020 whole-set witness cost by completing the lead-directed paid full-support rank reference after every one-point edit of padded cyclic quadratic-controlled majority, with all-size slack (287/1920) I_x(F_q), independent A070 reconstruction and 96 exact current fixtures. It also closes the naive inherited-reference payment after one private-data identification: a regular AND2 core gives one bit of cost at zero output influence. What remains is a signed cancellation refund and normalized replacement reference retaining terminal entropy when private labels collide, then a universal existence/payment argument. Constructing that refund at one identified pair is the shortest next route toward full FEI because it removes the precise hypothesis protecting the current complete reference and addresses an actual unpaid cost rather than adding another isolated class bound.
"""
p.write_text(s,encoding='utf-8')
statement=review['exact_statement'].split(' This accepts the exact theorem')[0]
claim=dict(claim_id='A068-CYCLIC-ONEPOINT-FULLREF',version=1,exact_statement=statement,hypotheses=review['hypotheses'][:4],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['account05/A068'],proof_source=dict(path=str(p),locators='Target and Sections 1-4',predecessor_sha256=sha(snapshot)),proof_dependencies=review['proof_dependencies'],review_records=review['review_records'],status='PROVED_AT_SCOPE_INDEPENDENT_A070_RECONSTRUCTION_REGISTRY_ADOPTION_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A070','A088','A094','B14','B20'])
obstatement='For regular AND2 with constant quadratic orientations (+1,-1), identify x2=x1. The parent rank reference (1/4,2/5,1/10,1/4) pushes forward to (1/2,1/2), while the output is constant -1. Complete inherited-reference cost is one bit and output entropy and influence are zero. Thus this inherited cost is not universally bounded by K times output influence for any finite K. This does not refute FEI or an adaptive output reference.'
obclaim=dict(claim_id='A068-IDENTIFIED-DATA-INHERITED-REFERENCE-OBSTRUCTION',version=1,exact_statement=obstatement,hypotheses=['Uniform parent bits; entropy and costs in bits','The specified parent reference is pushed forward, not replaced by an optimized output reference'],statement_sha256=hashlib.sha256(obstatement.encode()).hexdigest(),contributors=['account05/A068'],proof_source=dict(path=str(p),locator='Section 6',certificate=str(run/'out/collision.json')),proof_dependencies=[dict(claim_id=base['claim_id'],version=1,scope='Reference definition only; witness checked exactly')],review_records=[],status='EXACT_BOOLEAN_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['Unregistered proposed universal inherited-reference cost <= K I after data identification'],first_unproved_line=None,next_consumers=['A034','A070','A094','B14','B20'])
dump(run/'CLAIMS.json',[claim,obclaim])
source_paths=[shared/'BOARD.md',shared/'claude/B14/STREAM_NOTES.md',reviewdir/'REPORT.md',reviewdir/'CLAIMS.json',oldrun/'REPORT.md',root/'runs/20261011T222313Z-account05-A068-antichain-beyond-one-order/REPORT.md',shared/'agents/A034/runs/20261011T223816Z-account05-A034-phase-energy-transfer/REPORT.md',shared/'agents/A088/runs/20261011T223053Z-account05-A088-booleanity-referee/AUDIT.md']
dump(run/'out/SOURCES.json',[dict(path=str(x),sha256=sha(x),bytes=x.stat().st_size) for x in source_paths])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=rid,stream='B14',packet_id='A068',gap_id='A068-PRIVATE-DATA-SIGNED-COLLISION-PAYMENT',attempt_id='A068-stage3-edit-package-and-identification-interface',method='Resume interrupted proof; consume independent reconstruction; exact interval validation and exhaustive signed two-bit projection',mathematical_delta='All odd q>=5, all padding and every one-point edit: Gamma<=Creg Ix(G)+2Iz(G)-(287/1920)Ix(Fq). A070 theorem acceptance consumed; 96 current fixtures certified. Inherited-reference payment after identification fails on actual constant-output AND2 witness.',deliverable_status='COMPLETE_LOCAL_FOUR_FILES_CHECKED; supervisor/mirror pending',mathematical_status='CYCLIC_EDIT_TARGET_PROVED_AT_SCOPE; NAIVE_COLLISION_PAYMENT_REFUTED; FULL_FEI_OPEN',claim_versions_used=[base['claim_id']+'@1','C001 recovered regular-rank source',review['claim_id']+'@1','A069 weighted fixed-cost edit transfer'],claims_created_or_changed=[claim['claim_id']+'@1',obclaim['claim_id']+'@1'],source_artifacts=['REPORT.md','CLAIMS.json','out/SOURCES.json','out/PREDECESSOR_REPORT.md','out/validation.json','out/collision.json'],next_consumers=['A034','A070','A088','A094','B14','B20'],next_action='At one identified private-data pair construct a cancellation-aware complete reference paid by output influence, retaining terminal entropy.',stagnant_substantive_attempts=0,blockers=['Universal signed cancellation refund unproved','Narrow obstruction review and shared-registry adoption pending'],packet_ids=['A068'])
dump(run/'PROGRESS.json',progress)
(run/'PACKET_DELTA.json').write_bytes((run/'PROGRESS.json').read_bytes())
timestamp=datetime.now(timezone.utc).isoformat()
(root/'STATUS.md').write_text('STATE: Stage 3 complete: cyclic one-edit reference proved with 287/1920 base-Ix slack; A070 reconstruction accepted; 2785 exact checks PASS; inherited collision payment fails; full FEI OPEN.\nNEXT: Refund signed cancellation in a complete output reference after one private-data identification; retain terminal entropy; A070/A094 review.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+timestamp+' | '+rid+' | Resumed interrupted stage2 preserving originals and reviewed report hash. Consumed A070 reconstruction. Full v2 edit check PASS: 96 edits, 2 bases, 2589 assertions, 23.458 s. Signed identification: 32 cases, 196 assertions; regular AND2 inherited cost1 at zero influence. Current four files saved; cancellation refund open, full FEI open.\n')
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+timestamp+' | For odd q>=5 cyclic quadratic-controlled majority, padded N>=2q and any point edit, R_delta=(1-2^-N)R0+2^-N U_N has Gamma<=Creg Ix(G)+2Iz(G)-(287/1920)Ix(Fq). Balance earns H(K)<=Ix(Fq); weighted triangle pays all edit atoms. A070 independently accepts this theorem; 96 current fixtures pass outward rational intervals. Identification x2=epsilon x1 pairs coefficients a(T)+epsilon a(T xor {1,2}); pushforward reference gives Gamma_output<=2 Gamma_parent, but no output-influence payment. Regular AND2 with (+1,-1) orientations collapses to -1 while rank-reference pushforward costs1 and I=0. Refund destructive cancellation before claiming a universal collision payment. Interrupted predecessor preserved unchanged.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
required=protocol['required_per_run']
ckeys=set(required['claim_fields'])
pkeys=set('packet_ids' if x.startswith('packet_ids ') else x for x in required['progress_fields'])
assert all(set(c)==ckeys for c in [claim,obclaim])
assert set(progress)==pkeys
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((root/'STATUS.md').read_text().splitlines())==2
assert all(x.stat().st_size<20_000_000 for x in run.rglob('*') if x.is_file())
dump(run/'out/SCHEMA_CHECK.json',dict(status='PASS',claim_field_sets='exact',progress_field_set='exact',packet_delta_byte_equal=True,status_lines=2,predecessor_report_matches_independent_review=True,files_under_20_MB=True))
dump(run/'out/RECEIPTS.json',[dict(path=str(x.relative_to(run)),sha256=sha(x),bytes=x.stat().st_size) for x in sorted(run.rglob('*')) if x.is_file() and x.name!='RECEIPTS.json'])
print(json.dumps(dict(status='PASS',run_id=rid,assertions=2785,claim_count=2,predecessor_unchanged=True,four_protocol_files=True)))
