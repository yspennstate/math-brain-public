import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
command = ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'C0052 three-dimensional Ising scaling limit proof mistakes']
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    record = {'command': command, 'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
except subprocess.TimeoutExpired:
    record = {'command': command, 'timeout_seconds': 60, 'fallback': 'targeted memory index and named scar'}
(root / 'RECALL_RECEIPT.json').write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False)[:6500])
