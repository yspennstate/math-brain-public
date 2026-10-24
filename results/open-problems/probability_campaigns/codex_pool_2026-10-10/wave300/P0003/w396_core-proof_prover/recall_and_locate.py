from pathlib import Path
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
MEM = Path('~/.claude/projects/<project>/memory')
args = ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'P0003 self-avoiding walk proof mistakes', '-n', '3']
start = time.monotonic()
try:
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    receipt = {'command': args, 'elapsed_seconds': round(time.monotonic()-start, 3), 'returncode': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}
except subprocess.TimeoutExpired as e:
    receipt = {'command': args, 'elapsed_seconds': round(time.monotonic()-start, 3), 'status': 'TIMEOUT_60_SECONDS', 'fallback': 'Targeted memory-index grep; required perceptron scar.'}
(ROOT/'recall_receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False), flush=True)
scar = MEM/'perceptron_proof_open_gaps_fleet_2026_07_12.md'
if scar.is_file():
    text = scar.read_text(encoding='utf-8')
    print('REQUIRED_SCAR: '+str(scar)+'\n'+text[:18000], flush=True)
index = MEM/'MEMORY.md'
if index.is_file():
    matches = [line for line in index.read_text(encoding='utf-8').splitlines() if any(term in line.lower() for term in ['self-avoid', 'self_avoid', 'hexagon', 'perceptron_proof_open_gaps'])]
    print('INDEX_MATCHES: '+json.dumps(matches[:12], ensure_ascii=False), flush=True)

base = Path('~/<private-repo>/06_math_research')
dirs = [p for p in base.iterdir() if p.is_dir() and (p.name.startswith('probability_1000_intake_') or p.name in ['probability_1000_attempts_H_20260912', 'probability_1000_attempts_I_20260914', 'prob1000_lean_20260908'])]
cmd = ['rg', '-l', '-F', 'P0003', *map(str, dirs)]
r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=120)
(ROOT/'p0003_source_paths.txt').write_text(r.stdout, encoding='utf-8')
print('P0003_SOURCE_PATHS:\n'+r.stdout, flush=True)
