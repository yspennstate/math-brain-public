"""Bounded, read-only recall; no live writes, subprocesses, or network."""
import contextlib, io, os, runpy, sys, threading, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
os.environ['BRAIN_RECALL_REFRESH'] = '0'
os.environ['BRAIN_RECALL_LOG'] = '0'
os.environ['BRAIN_GRAPH_LAMBDA'] = '0'
query = ' '.join(sys.argv[1:]) or 'open problems Brown measure strong convergence mistakes'
report = ROOT / 'reports'
report.mkdir(exist_ok=True)
buffer = io.StringIO()
errors = []

def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        writable = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writable and not Path(path).resolve().is_relative_to(ROOT):
            raise PermissionError('read-only recall refused an external write')
    if event in {'subprocess.Popen', 'os.system', 'socket.connect', 'os.remove', 'os.rename', 'os.rmdir'}:
        raise PermissionError('read-only recall refused ' + event)
    if event == 'sqlite3.connect' and 'mode=ro' not in str(args[0]):
        raise PermissionError('read-only recall refused a writable sqlite connection')
    if event == 'os.mkdir' and not Path(args[0]).resolve().is_relative_to(ROOT):
        raise PermissionError('read-only recall refused an external directory')

def work():
    try:
        sys.path.insert(0, '~/.claude/dreaming')
        sys.argv = ['brain.py', 'recall', query, '-n', '3']
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
            runpy.run_path('~/.claude/dreaming/brain.py', run_name='__main__')
    except SystemExit:
        pass
    except BaseException as exc:
        errors.append(type(exc).__name__ + ': ' + str(exc))

sys.addaudithook(audit)
start = time.perf_counter()
thread = threading.Thread(target=work, daemon=True)
thread.start()
thread.join(60)
elapsed = time.perf_counter() - start
state = 'TIMEOUT; use the memory-index fallback' if thread.is_alive() else 'COMPLETED'
receipt = 'query: ' + query + '\nstate: ' + state + '\nelapsed_seconds: ' + str(round(elapsed, 3)) + '\n' + '\n'.join(errors) + '\n' + buffer.getvalue()
(report / 'recall.md').write_text(receipt, encoding='utf-8')
sys.__stdout__.write(receipt[:12000])
