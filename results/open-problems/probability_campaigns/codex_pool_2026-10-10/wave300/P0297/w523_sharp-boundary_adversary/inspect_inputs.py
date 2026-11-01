"""Bounded, read-only discovery for the assigned P0297 task."""
from pathlib import Path
import subprocess
import json
import os

ROOT = Path('~')
JOB = ROOT / 'brain_workers/w523'
RESEARCH = ROOT / '<private-repo>/06_math_research'

def excerpt(path, patterns, radius=2, max_matches=8):
    path = Path(path)
    if not path.exists():
        print('MISSING', path)
        return
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    hits = [i for i, line in enumerate(lines) if any(p.lower() in line.lower() for p in patterns)][:max_matches]
    print('FILE', path)
    for i in sorted({j for hit in hits for j in range(max(0, hit-radius), min(len(lines), hit+radius+1))}):
        print(f'{i+1}: {lines[i]}')

def rg(args, timeout=50, limit=14000):
    try:
        r = subprocess.run(['rg', *args], capture_output=True, text=True, encoding='utf-8', timeout=timeout)
        print(r.stdout[:limit])
        if r.returncode not in (0, 1):
            print('RG_ERROR', r.stderr[:1000])
    except subprocess.TimeoutExpired:
        print('RG_TIMEOUT', args)

print('WORKER FILES', [(p.name, p.stat().st_size) for p in JOB.iterdir() if p.is_file()])
print('BUNDLE_SPEC')
print((ROOT / 'math-brain-inbox/BUNDLE_SPEC.md').read_text(encoding='utf-8')[:18000])
print('TARGET FILENAMES')
rg(['--files', str(RESEARCH), '-g', '*0297*', '-g', '*[Ll]iouville*'])
intakes = sorted(p for p in RESEARCH.glob('probability_1000_intake_*') if p.is_dir())
print('INTAKE FOLDERS', [p.name for p in intakes])
for folder in intakes:
    rg(['-l', '-F', 'P0297', str(folder), '-g', '*.json', '-g', '*.jsonl', '-g', '*.csv', '-g', '*.md'], limit=5000)
print('PRIOR ATTEMPT TARGET ROWS')
for name in ['probability_1000_attempts_H_20260912', 'probability_1000_attempts_I_20260914', 'prob1000_lean_20260908']:
    p = RESEARCH / name
    if p.exists():
        rg(['-n', '-F', 'P0297', str(p), '-g', '*.json', '-g', '*.jsonl', '-g', '*.csv', '-g', '*.md', '-g', '*.lean', '-m', '2'], limit=9000)
print('MEMORY INDEX HITS')
excerpt(ROOT / '.claude/projects/<project>/memory/MEMORY.md', ['Liouville', 'P0297', 'perceptron_proof_open_gaps_fleet_2026_07_12'], radius=1, max_matches=9)
print('TEAM COMM RELEVANT IMPLEMENTATION')
p = ROOT / '<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'
lines = p.read_text(encoding='utf-8').splitlines()
for a, b in [(73, 91), (241, 263), (288, 302)]:
    print('\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1, b)))
print('PEER FILENAMES ONLY')
for who in ['w522', 'w524', 'w515', 'w518', 'w525']:
    p = ROOT / 'brain_workers' / who
    if p.exists():
        print(who, [(x.name, x.stat().st_size) for x in p.iterdir() if x.is_file()])
print('AUDIT ASSIGNMENT')
excerpt(ROOT / 'primary_directive/hooks1000/AUDIT_ASSIGNMENTS.md', ['w523'], radius=1, max_matches=5)
