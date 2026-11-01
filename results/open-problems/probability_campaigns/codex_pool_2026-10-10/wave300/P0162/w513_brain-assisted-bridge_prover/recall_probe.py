"""Bounded, read-only memory recall; receipt stays in this worker folder."""
import json
import pathlib
import subprocess
import time

root = pathlib.Path(__file__).resolve().parent
cmd = ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py',
       'recall', 'P0162 Fourier entropy total influence proof mistakes', '-n', '3']
started = time.perf_counter()
try:
    run = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                         errors='replace', timeout=60)
    receipt = dict(exit_code=run.returncode, stdout=run.stdout, stderr=run.stderr)
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value
    receipt = dict(status='timeout_60s', stdout=decode(exc.stdout), stderr=decode(exc.stderr))
receipt.update(command=cmd, elapsed_s=time.perf_counter()-started)
(root/'recall_receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False))
