from pathlib import Path
import csv
import subprocess

ROOT = Path('~/<private-repo>/06_math_research')
ranking = ROOT / 'probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv'
if ranking.exists():
    with ranking.open(encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            if any(str(v) == 'C0049' for v in row.values()):
                print('RANKING:', row)

roots = list(ROOT.glob('probability_1000_intake_*'))
roots += [ROOT / 'probability_1000_attempts_H_20260912', ROOT / 'probability_1000_attempts_I_20260914', ROOT / 'prob1000_lean_20260908']
roots = [p for p in roots if p.exists()]
r = subprocess.run(['rg', '-n', '-m', '3', '-C', '3', '--max-columns', '1100', '--max-columns-preview', '-g', '*.md', '-g', '*.csv', '-g', '*.jsonl', '-g', '*.json', '-g', '*.lean', r'\bC0049\b', *map(str, roots)], capture_output=True, text=True, encoding='utf-8', timeout=45)
print('EXACT-ID MATCHES:\n' + r.stdout[:18500])

memory = Path('~/.claude/projects/<project>/memory')
scar = memory / 'perceptron_proof_open_gaps_fleet_2026_07_12.md'
print('PROOF-GAP SCAR:', scar)
if scar.exists():
    print(scar.read_text(encoding='utf-8')[:8000])
else:
    r = subprocess.run(['rg', '-n', '-m', '3', 'perceptron_proof_open_gaps', str(memory / 'MEMORY.md')], capture_output=True, text=True, encoding='utf-8', timeout=15)
    print(r.stdout)

spec = Path('~/math-brain-inbox/BUNDLE_SPEC.md')
print('BUNDLE SPEC:')
print(spec.read_text(encoding='utf-8')[:14000] if spec.exists() else 'MISSING')

for folder in ['w589', 'w590', 'w339', 'w341']:
    p = Path('~/brain_workers') / folder / 'STATUS.md'
    print('PEER STATUS:', p)
    if p.exists():
        print(p.read_text(encoding='utf-8')[:2200])

retired = Path('~/Big Open problem in probability theory')
if retired.exists():
    r = subprocess.run(['rg', '--files', str(retired), '-g', '*percol*', '-g', '*cluster*', '-g', '*SLE*', '-g', '*C0049*'], capture_output=True, text=True, encoding='utf-8', timeout=30)
    print('OWNER RELEVANT PATHS:\n' + r.stdout[:3200])
