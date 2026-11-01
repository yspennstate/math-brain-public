from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
args = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'C0120 directed polymer variance mistakes']
try:
    run = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    content = run.stdout + '\n' + run.stderr
    (base / 'RECALL_SCOPED.txt').write_text(content, encoding='utf-8')
    print(content[:6500])
except subprocess.TimeoutExpired:
    (base / 'RECALL_SCOPED.txt').write_text('Recall exceeded the instructed 60-second deadline. Use targeted MEMORY.md fallback.\n', encoding='utf-8')
    print('RECALL_TIMEOUT_60S: use targeted memory index fallback.')
