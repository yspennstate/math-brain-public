"""Targeted filename/content searches only, not a corpus export."""
from pathlib import Path
import subprocess

BASE = Path('~/<private-repo>/06_math_research')

def rg(args, cap=6500):
    r = subprocess.run(['rg', *args], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=45)
    print(r.stdout[:cap], flush=True)
    if r.stderr:
        print(r.stderr[:500], flush=True)

for folder in sorted(BASE.glob('probability_1000_intake_*')):
    print('INTAKE', folder, flush=True)
    rg(['-n', '-m', '2', '-F', 'C0017', str(folder), '-g', '*.json', '-g', '*.jsonl', '-g', '*.csv', '-g', '*.md'], 4500)
for name in ['probability_1000_attempts_H_20260912', 'probability_1000_attempts_I_20260914', 'prob1000_lean_20260908']:
    print('PRIOR', name, flush=True)
    rg(['-l', '-F', 'C0017', str(BASE/name)], 3000)
print('MEMORY INDEX', flush=True)
rg(['-n', 'perceptron_proof_open_gaps_fleet_2026_07_12|conformal|percolation', '~/.claude/projects/<project>/memory/MEMORY.md'], 2500)
print('OWNER PERCOLATION FILENAMES', flush=True)
r = subprocess.run(['rg', '--files', '~/Big Open problem in probability theory'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=45)
print('\n'.join(p for p in r.stdout.splitlines() if any(k in p.lower() for k in ['percol', 'conformal', 'retired', 'solved']))[:4000], flush=True)
