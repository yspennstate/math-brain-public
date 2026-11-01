"""Targeted, read-only packet inventory. Writes only this worker's folder."""
from pathlib import Path
import csv
import json
import subprocess

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'context'
OUT.mkdir(exist_ok=True)
BASE = Path('~')

def show_file(relative, limit=120):
    p = BASE / relative
    if not p.exists():
        print('MISSING', p, flush=True)
        return
    data = p.read_text(encoding='utf-8-sig')
    lines = data.splitlines()
    print('\nFILE', p, 'LINES', len(lines), flush=True)
    print('\n'.join(f'{i+1}: {s}' for i, s in enumerate(lines[:limit])), flush=True)

ranking = BASE / '<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv'
if ranking.exists():
    with ranking.open(encoding='utf-8-sig', newline='') as f:
        rows = [r for r in csv.DictReader(f) if any('P0017' == str(v).strip() for v in r.values())]
    (OUT / 'ranking_P0017.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('RANKING_P0017', json.dumps(rows, ensure_ascii=False), flush=True)
    with (ROOT / 'SOURCE_AUDITS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps({'id':'w350-S1.P0017.001','verdict':'FIX','subject':'current status inferred from historical ranking','source':str(ranking),'source_row':rows,'finding':'Historical title/tier/prior attempted_un do not certify current openness or a sound proof. Recover normalized exact primary statement and prior attempts before a proof attempt.','current_openness':'UNKNOWN','reviewer':'w350','date':'2026-10-10'})+'\n')

for relative in [
    'brain_workers/teams/W0300_O/TEAM_BOARD.md',
    'brain_workers/w348/STATUS.md', 'brain_workers/w348/ATTEMPT.md',
    'brain_workers/w349/STATUS.md', 'brain_workers/w349/ATTEMPT.md',
    'brain_workers/w353/STATUS.md',
    'math-brain-inbox/BUNDLE_SPEC.md',
]:
    show_file(relative)

def targeted_rg(label, args):
    try:
        p = subprocess.run(['rg', *args], capture_output=True, text=True, encoding='utf-8', timeout=30)
        (OUT / (label+'.txt')).write_text(p.stdout, encoding='utf-8')
        print('\nRG', label, 'EXIT', p.returncode, flush=True)
        print('\n'.join(p.stdout.splitlines()[:100]), flush=True)
        if p.stderr:
            print(p.stderr[:1000], flush=True)
    except subprocess.TimeoutExpired:
        print('RG TIMEOUT', label, flush=True)

targeted_rg('audit_assignment', ['-n', '-C', '2', 'w350', str(BASE/'primary_directive/hooks1000/AUDIT_ASSIGNMENTS.md')])
targeted_rg('scar_index', ['-n', '-i', 'perceptron_proof_open_gaps|KLS|log.concave|method_grow_mathbrain_safely|referee_pass_before_shipping', str(BASE/'.claude/projects/<project>/memory/MEMORY.md')])
research = BASE / '<private-repo>/06_math_research'
dirs = list(research.glob('probability_1000_intake_*')) + [research/'probability_1000_attempts_H_20260912',research/'probability_1000_attempts_I_20260914',research/'prob1000_lean_20260908']
for directory in dirs:
    if directory.exists():
        targeted_rg(directory.name, ['-l','-i','-g','*.md','-g','*.csv','-g','*.json','-g','*.jsonl','-g','*.lean','P0017|dimension.free log.concave|Kannan.Lov.sz.Simonovits',str(directory)])
