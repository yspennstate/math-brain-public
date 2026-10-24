from pathlib import Path
import csv
import re

BASE = Path('~')
RESEARCH = BASE / '<private-repo>/06_math_research'
TERMS = re.compile(r'P0321|hexatic|perceptron_proof_open_gaps_fleet_2026_07_12|proof_steps_need_derived_joint_structure_2026_09_09', re.I)

def snippets(path, pattern=TERMS, context=2, limit=28):
    if not path.is_file():
        print(f'MISSING {path}')
        return
    text = path.read_text(encoding='utf-8-sig', errors='replace')
    lines = text.splitlines()
    hits = [i for i, line in enumerate(lines) if pattern.search(line)]
    print(f'FILE {path} hits={len(hits)}')
    indices = set()
    for i in hits[:limit]:
        indices.update(range(max(0, i-context), min(len(lines), i+context+1)))
    for i in sorted(indices):
        print(f'{i+1}: {lines[i][:2500]}')

for folder in sorted(RESEARCH.glob('probability_1000_intake_*')):
    print('INTAKE', folder.name)
    for f in sorted(folder.rglob('*')):
        if not f.is_file() or f.suffix.lower() not in {'.csv', '.json', '.jsonl', '.md', '.txt'}:
            continue
        if f.stat().st_size > 8_000_000:
            continue
        if f.suffix.lower() == '.csv':
            with f.open(encoding='utf-8-sig', newline='') as stream:
                reader = csv.DictReader(stream)
                for row in reader:
                    if any('P0321' == str(v).strip() for v in row.values()):
                        print('RECORD', f, row)
        else:
            snippets(f, context=1, limit=8)

for name in ['probability_1000_attempts_H_20260912', 'probability_1000_attempts_I_20260914', 'prob1000_lean_20260908']:
    folder = RESEARCH/name
    print('PRIOR_FOLDER', folder, folder.exists())
    if folder.exists():
        for f in sorted(folder.rglob('*')):
            if f.is_file() and ('0321' in f.name or 'hexatic' in f.name.lower()):
                print('PRIOR_TARGET_FILE', f, f.stat().st_size)

snippets(BASE/'brain_workers/teams/W0300_O/TEAM_BOARD.md', context=2)
snippets(BASE/'brain_workers/teams/PROBABILITY300_20261010/TEAM_BOARD.md', context=2)
snippets(BASE/'.claude/projects/<project>/memory/MEMORY.md', context=0)
snippets(BASE/'.claude/dreaming/brain.py', re.compile(r'def recall|def cmd_recall|args.command.*recall|elif.*recall'), context=8, limit=8)
snippets(BASE/'primary_directive/hooks1000/AUDIT_ASSIGNMENTS.md', re.compile(r'\bw544\b'), context=1)
