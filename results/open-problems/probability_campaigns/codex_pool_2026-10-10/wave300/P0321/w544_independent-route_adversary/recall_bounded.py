from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
command = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'P0321 hexatic Riesz gas independent proof mistakes']
start = time.monotonic()
try:
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, encoding='utf-8', timeout=60)
    text = result.stdout + result.stderr
    code = result.returncode
except subprocess.TimeoutExpired as err:
    def decode(value):
        return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else (value or '')
    text = 'TIMEOUT after 60 seconds; use targeted memory fallback.\n' + decode(err.stdout) + decode(err.stderr)
    code = 'timeout'
(root/'recall_receipt.txt').write_text(f'command={command!r}\nreturncode={code}\nelapsed_seconds={time.monotonic()-start:.3f}\n{text}', encoding='utf-8')
print(f'recall returncode={code}; saved recall_receipt.txt')
print(text[:18000])
