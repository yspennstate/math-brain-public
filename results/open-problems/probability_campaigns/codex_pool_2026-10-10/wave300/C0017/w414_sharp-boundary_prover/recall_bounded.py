from pathlib import Path
import subprocess
import sys

out = Path(__file__).with_name('RECALL.txt')
command = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'C0017 percolation boundary bridge proof mistakes']
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    text = result.stdout + '\nSTDERR:\n' + result.stderr
    out.write_text(text, encoding='utf-8')
    print(text[:10000])
except subprocess.TimeoutExpired:
    text = 'TIMEOUT 60 seconds; use targeted MEMORY.md fallback.\n'
    out.write_text(text, encoding='utf-8')
    print(text)
