from pathlib import Path
import json
p=Path('STATUS.md');s=p.read_text(encoding='utf8');lines=s.splitlines();lines[0]='STATE: DONE';lines[1]='NEXT: Construct a colour-aware stationary balanced convex-cell partition, or obtain uniform displacement tails with explicit non-crossing constraints and infinite first moment.';lines[2]='VERDICT: PARTIAL';s='\n'.join(lines)+'\n';s+='2026-10-11 second attempt completed: Two new approaches recorded and pursued. Proved full continuous displacement-cost classification and finite planar-optimizer equivalence, coercive finite-cost obstruction, balanced-strip-cut obstruction, and colour-blind-cell obstruction. New limited Lean certificates passed (exit 0). Uniform displacement tightness and a perfect planar Poisson construction remain unproved.\n';p.write_text(s,encoding='utf8')
claims=[json.loads(l) for l in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==15, len(claims)
assert Path('STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
assert 'exit=0' in Path('second_lean_check.log').read_text()
lean=Path('UncrossingCostChecks.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean
probe=json.loads(Path('cost_probe.json').read_text(encoding='utf8'));assert len(probe)==10
for name in ['sqrt','log1p','power_0.9','squared']:assert any(x['cost']==name and x['new_minus_old']>0 for x in probe)
assert all(x['new_minus_old']<0 for x in probe if x['cost']=='linear')
print('Final audit: 15 valid claim records; 10 cost probes; Lean exit 0; STATE DONE / VERDICT PARTIAL.')
print(Path('second_lean_check.log').read_text())
