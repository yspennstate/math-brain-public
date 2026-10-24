"""Prepare a narrow archive diff and exact measurements; never mutate the archive."""
from datetime import datetime, timezone
from fractions import Fraction as R
from itertools import islice
import json
from pathlib import Path
import time

root=Path(__file__).resolve().parent
gate_path=root/'COMPUTE_GATE_CORRECTION.json'
gate=json.loads(gate_path.read_text(encoding='utf-8'))
if gate['state'] != 'fresh' or any(gate[k] for k in ('network','gpu','training')):
    raise SystemExit('Fresh CPU-only gate required')
gate.update(state='consumed',started_utc=datetime.now(timezone.utc).isoformat())
gate_path.write_text(json.dumps(gate,indent=2),encoding='utf-8')
start=time.monotonic()

live=Path('~/<private-repo>/06_math_research/probability_1000_intake_D_20260908/attempts.jsonl')
with live.open(encoding='utf-8') as stream:
    original=next(islice(stream,42,43))
record=json.loads(original)
if record.get('attempt_id') != 'D0049-A001':
    raise SystemExit('Line 43 changed; re-grep the exact attempt before preparing a diff')
assert 'd_gamma = 2Q/xi' in record['key_identity']
assert 'd_gamma = 2 Q / xi' in record['method']
old_record=dict(record)
record['key_identity']=record['key_identity'].replace('d_gamma = 2Q/xi','d_gamma = gamma/xi')
record['method']=record['method'].replace('d_gamma = 2 Q / xi','d_gamma = gamma / xi')
record['normalization_correction']={
    'author':'w522','date':'2026-10-10','review_status':'pending w524',
    'source':'https://arxiv.org/abs/1905.11790','locator':'equation (1.5)',
    'reason':'xi=gamma/d_gamma, so 2Q/xi=(1+4/gamma^2)d_gamma; known Brownian anchor would be 10 instead of 4.',
    'scope':'Only the two normalization strings are corrected; other original claims remain unaudited.'}
changed={k for k in old_record if old_record[k] != record[k]}
assert changed == {'key_identity','method'}
assert set(record)-set(old_record) == {'normalization_correction'}
proposed=json.dumps(record,ensure_ascii=False,sort_keys=True)+'\n'
(root/'PRIOR_D0049_ORIGINAL.json').write_text(original,encoding='utf-8')
(root/'PRIOR_D0049_PROPOSED.json').write_text(proposed,encoding='utf-8')
patch_dir=root/'patches'
patch_dir.mkdir(exist_ok=True)
target=live.as_posix()
patch=('--- a/'+target+'\n+++ b/'+target+'\n@@ -43 +43 @@\n-'+original.rstrip('\r\n')+'\n+'+proposed)
(patch_dir/'02_d0049_normalization.diff').write_text(patch,encoding='utf-8')

hook_target=Path('~/primary_directive/hooks1000/proposals/math-w522.jsonl')
hook_line=(root/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8').strip()+'\n'
if hook_target.exists():
    existing=hook_target.read_text(encoding='utf-8')
    if 'P0297-w522-01' in existing:
        raise SystemExit('Hook ID already exists; do not overwrite another submission')
    line_count=len(existing.splitlines())
else:
    line_count=0
hook_patch=('--- a/'+hook_target.as_posix()+'\n+++ b/'+hook_target.as_posix()+'\n@@ -'+str(line_count)+',0 +'+str(line_count+1)+' @@\n+'+hook_line)
(patch_dir/'01_lqg_kpz_guard.diff').write_text(hook_patch,encoding='utf-8')

rows=[]
for g in (R(1,4),R(1,2),R(3,4),R(1),R(5,4),R(3,2),R(7,4),R(15,8)):
    for D in (R(5,2),R(3),R(7,2),R(4),R(9,2),R(5),R(6),R(8)):
        if len(rows) >= gate['max_cases'] or time.monotonic()-start > gate['max_runtime_seconds']:
            raise RuntimeError('Compute gate exceeded')
        xi=g/D
        Q=2/g+g/2
        before=2*Q/xi-D
        after=g/xi-D
        assert before == 4*D/(g*g) and before > 0 and after == 0
        rows.append({'gamma':str(g),'D':str(D),'before_residual':str(before),'after_residual':str(after)})
s=R(8,3)
anchor_before=(1+4/s)*4
anchor_after=R(4)
assert anchor_before == 10 and anchor_after == 4
result={'gate_id':gate['gate_id'],'command':'python -X utf8 .\\prepare_correction.py',
        'grid_cases':len(rows),'before_inconsistent_cases':sum(r['before_residual']!='0' for r in rows),
        'after_inconsistent_cases':sum(r['after_residual']!='0' for r in rows),
        'brownian_anchor':{'gamma_squared':'8/3','known_D':4,'before_formula':float(anchor_before),
                          'after_formula':float(anchor_after),'absolute_error_before':6,'absolute_error_after':0},
        'elapsed_seconds':time.monotonic()-start,'rows':rows,
        'scope':'Before/after algebraic consistency of a staged source correction. No live mutation, no original-target proof, no independent mathematical receipt.'}
(root/'CORRECTION_MEASUREMENTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
