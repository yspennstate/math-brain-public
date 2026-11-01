import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
query = 'C0054 two dimensional random band matrices localization mistakes'
try:
    result = subprocess.run(
        ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', query],
        capture_output=True, text=True, encoding='utf-8', timeout=55,
    )
    evidence = result.stdout[:14000] + '\nSTDERR:\n' + result.stderr[:1500]
except subprocess.TimeoutExpired:
    evidence = 'RECALL_TIMEOUT_55S: use targeted MEMORY.md fallback.\n'
(root / 'recall_evidence.txt').write_text(evidence, encoding='utf-8')
print(evidence)
