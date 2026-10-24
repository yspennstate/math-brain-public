"""Only assignment-named roots and exact scar/source metadata."""
from pathlib import Path
import subprocess

research = Path('~/<private-repo>/06_math_research')
roots = list(research.glob('probability_1000_intake_*')) + [research/'probability_1000_attempts_H_20260912', research/'probability_1000_attempts_I_20260914', research/'prob1000_lean_20260908']
existing = [str(p) for p in roots if p.exists()]
result = subprocess.run(['rg','-l','-g','*.md','-g','*.json','-g','*.jsonl','-g','*.csv','-g','*.lean','C0044|directional 0-1|directional zero.one', *existing], capture_output=True, text=True, encoding='utf-8', timeout=60)
print('C0044_MATCHING_FILES\n'+result.stdout[:16000])
memory = Path('~/.claude/projects/<project>/memory')
for slug in ('perceptron_proof_open_gaps_fleet_2026_07_12','proof_steps_need_derived_joint_structure_2026_09_09'):
    p = memory/(slug+'.md')
    print('SCAR '+str(p))
    print(p.read_text(encoding='utf-8')[:12000] if p.exists() else 'NOT AT EXACT PATH')
for worker in ('w576','w578','w579','w580','w581','w582','w583','w584','w585','w586','w587'):
    p=Path('~/brain_workers')/worker
    print('PEER_FILES '+worker+' '+', '.join(c.name for c in p.iterdir() if c.is_file()) if p.exists() else 'PEER_ABSENT '+worker)
for p in (Path('~/math-brain-inbox/BUNDLE_SPEC.md'), Path('~/primary_directive/democracy/OPEN_VOTES.json')):
    print('SPEC_OR_VOTE '+str(p))
    print(p.read_text(encoding='utf-8')[:18000] if p.exists() else 'NOT AT EXACT PATH')
