from pathlib import Path
import json
R=Path(__file__).resolve().parent
p=R/'CLAIMS.jsonl'; claims=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines() if l]
for c in claims:
 if c['proof_location']=='SECOND_ATTEMPT.md: Complete graph reduction':
  c['checks'][-1]='BottleneckCuts.lean: route closure and closed separating cut equivalence kernel-checked; lake env lean exited 0 without diagnostics. Dimension weights and Poisson geometry are not formalized.'
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
assert len(claims)==9
assert all(c['problem_id']=='P0231' for c in claims)
status=(R/'STATUS.md').read_text(encoding='utf8')
assert status.splitlines()[0]=='STATE: DONE' and '\nVERDICT: PARTIAL\n' in status
assert json.loads((R/'bottleneck_checks.json').read_text(encoding='utf8'))['result']=='all assertions passed'
assert 'Status: PASS.' in (R/'second_lean_check.txt').read_text(encoding='utf8')
assert all((R/f).exists() for f in ['STATUS.md','ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','SECOND_ATTEMPT.md'])
print('Second attempt finalized: STATE DONE; VERDICT PARTIAL; 9 valid claim records; exact checks and Lean pass recorded.')
