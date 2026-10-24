"""Run the required recall with live writes, child processes and networking denied."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import sys
import time

worker = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
os.environ['BRAIN_RECALL_REFRESH'] = '0'
os.environ['BRAIN_RECALL_QUERY_EMBED'] = '0'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
blocked = []
started = time.monotonic()

def audit(event, args):
    denied = event in {'subprocess.Popen', 'os.system', 'os.remove', 'os.rmdir', 'os.rename', 'os.replace', 'socket.connect', 'os.mkdir'}
    if event == 'open':
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing:
            denied = True
    if event == 'sqlite3.connect':
        denied = 'mode=ro' not in str(args[0])
    if denied:
        blocked.append(event)
        raise PermissionError('w532 read-only recall guard: ' + event)

ticks = 0
def trace(frame, event, arg):
    global ticks
    ticks += 1
    if ticks % 1024 == 0 and time.monotonic() - started > 60:
        raise TimeoutError('recall exceeded its cooperative 60-second gate')
    return trace

output = io.StringIO()
receipt = {'query': 'P0309 Riesz crystallization probability proof mistakes', 'limit': 3, 'deadline_seconds': 60, 'refresh_disabled': True, 'live_writes_denied': True}
sys.addaudithook(audit)
sys.path.insert(0, '~/.claude/dreaming')
sys.argv = ['brain.py', 'recall', receipt['query'], '-n', '3']
try:
    sys.settrace(trace)
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        runpy.run_path('~/.claude/dreaming/brain.py', run_name='__main__')
    receipt['status'] = 'returned'
except SystemExit as exc:
    receipt['status'] = 'returned'
    receipt['exit_code'] = exc.code
except Exception as exc:
    receipt['status'] = 'fallback_required'
    receipt['error'] = type(exc).__name__ + ': ' + str(exc)
finally:
    sys.settrace(None)
receipt['elapsed_seconds'] = time.monotonic() - started
receipt['blocked_events'] = blocked
# The guard deliberately forbids even our own open-for-write during recall.
# Print results; the invoking shell saves these within the worker folder.
print(json.dumps(receipt, ensure_ascii=False))
print(output.getvalue()[:16000])
