import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
published=json.loads((root/'publish_receipt.json').read_text(encoding='utf-8'))
validation=json.loads((root/'validation_receipt.json').read_text(encoding='utf-8'))
core=json.loads((root/'measurements.json').read_text(encoding='utf-8'))
extended=json.loads((root/'measurements_extended.json').read_text(encoding='utf-8'))
corrections=json.loads((root/'correction_measurements.json').read_text(encoding='utf-8'))
assert validation['passed']
assert published['entries']==22 and published['relations']==32
assert all(c['passed'] for c in core['checks']+extended['checks'])
draftpath=Path(published['draft_path'])
assert draftpath.read_text(encoding='utf-8')==(root/'drafts/bundle_001.json').read_text(encoding='utf-8')
board=Path('~/brain_workers/teams/W0300_O/TEAM_BOARD.md')
next_candidate=None
for line in board.open(encoding='utf-8-sig'):
    match=re.match(r'- \[ \] ([A-Z]\d{4}) ',line)
    if match and not re.search(r' - (?:w\d+|claude-\S+)(?:\s|$)',line):
        next_candidate=match.group(1);break
(root/'NEXT_TASK.json').write_text(json.dumps({'observed_next_unassigned_id':next_candidate,
    'board':str(board),'shared_claim_made':False,'instruction':'Recheck the live board in the next session before claiming; first packet awaits required independent audits.'},indent=2),encoding='utf-8')
report=f"""Prepared the first ten assigned problems for independent review: 22 typed draft nodes (15 author-proved lemmas, seven concepts/candidates), 32 edges, and 64 quoted endpoints. Every one of the 22 external edges resolved against the read-only store. The complete draft is at {draftpath.as_posix()}. There are 30 saved source/result rows including superseded revisions; they represent 22 final entries, not 30 separate new mathematical results.

The main repair is C0068's reversed scale comparison: for d>6, V^(-1/3)<<V^(-2/d), and an explicit epsilon sequence lies above the critical window but below the proposed crossover. C0101's ceiling-curvature bound also fails: a=1/2,x=0 gives second difference 2>3/2. Both have proved corrections and refutes edges. With python -X utf8 measure_corrections.py, the old assertions passed 0/6 exact cases and the corrections passed 6/6. This measures the assertion checks, not deployed recall performance.

P0174 has a reconstructed full candidate C=1 proof with the strict fourth-order equality check. The cached Hasebe-Ueda Lemma 3.1 and diameter convention are checked; only its sufficient direction is used. Independent full proof KEEP and novelty clearance remain outstanding. The other problems have special cases, conditional reductions or refuted routes, with limits in reports/<id>_attempt.md. No open problem is reported solved. The apparent C0010 resolving card traces to a held P0475 alias; the positive-phase C0089 literature combination remains unmatched to exact sources.

Validation: python -X utf8 check_math.py passed seven groups in {core['elapsed_seconds']:.3f} s; python -X utf8 check_extended.py passed ten groups in {extended['elapsed_seconds']:.3f} s. validate_bundle.py passed schema, license-prefix, quote, target and dependency checks. These are local checks, not an integrator or mathematical audit. Lean returned SETUP_UNVERIFIED because compute admission was distressed or unknown, so no result is Lean-checked.

Apply after the required independent KEEP receipts: the node draft is already in w332's inbox, and patches/01_math_nodes.diff records its exact addition. The reviewer can run python -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w332. Apply patches/02_math_hooks.diff by adding hooks/math-w332.jsonl at its named proposal path; both hooks pass their fire and silent controls. This worker did not ingest or modify live SQLite. AUDIT_REQUEST.md is the blind handoff to w346. Outbound mesh sends and shared progress/hook writes are prohibited by COMMON.md, so those artifacts are staged locally in PROGRESS.md and hooks/.

NEXT: w346 audits the 22 entries and 32 edges; the reviewer lands KEEP rows. Recheck {next_candidate or 'the first unassigned row'} on the live board before the next claim.
"""
(root/'REPORT.md').write_text(report,encoding='utf-8')
progress=f"""Ready for the reviewer to post after the required checks, under the worker write restriction:

python -X utf8 ~/primary_directive/pd_progress.py --event "w332: 10 problems; 22 draft nodes; 32 edges; 2 refutations; w346 pending" --agent w332 --row S1.w332.002 --evidence ~/brain_workers/w332/REPORT.md

Metadata-only audit handoff line:
w332 w346 22 32 {draftpath.as_posix()} ~/brain_workers/w332/AUDIT_REQUEST.md
"""
(root/'PROGRESS.md').write_text(progress,encoding='utf-8')
status=(root/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0]='STATE: NEEDS_REVIEW'
status[1]='NEXT: w346 blindly audits drafts/bundle_001.json; reviewer lands KEEP entries/edges, then rechecks the next unassigned board row.'
status.append('2026-10-10: Final packet measured and complete: 22 entries, 32 relations, 64 endpoint quotes, 30 versioned rows; 17 mathematical check groups pass; correction cases improve 0/6 to 6/6. Draft atomically placed at '+draftpath.as_posix()+'. REPORT.md, AUDIT_REQUEST.md, two local hook proposals and patches are ready. No solved-problem or Lean-checked claim. Pending independent KEEP and reviewer integration.')
(root/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
receipt={'state':'NEEDS_REVIEW','draft':draftpath.as_posix(),'entries':22,'relations':32,'result_rows':30,
    'check_groups':len(core['checks'])+len(extended['checks']),'before_passed':corrections['before_passed'],
    'after_passed':corrections['after_passed'],'live_store_writes_by_worker':0,
    'outbound_messages_by_worker':0,'solved_open_problems_claimed':0,'next_candidate_observed':next_candidate}
(root/'completion_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
