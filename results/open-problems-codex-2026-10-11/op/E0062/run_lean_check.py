"""Run one serialized lake check, with persistent output and a one-hour timeout."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess

root = Path(__file__).resolve().parent
source = root / 'Prefix.lean'
record = root / 'lean_check_result.json'
log = root / 'lean_check.log'
command = ['powershell.exe', '-NoProfile', '-NonInteractive', '-Command',
           "lake env lean '" + source.as_posix() + "'"]
data = {
    'state': 'RUNNING',
    'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'command': command,
    'cwd': '~/lean_verify',
    'timeout_seconds': 3600,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'prior_session': '82004 unavailable; no matching live Lean/lake/python process found',
}
record.write_text(json.dumps(data, indent=2), encoding='utf-8')
with log.open('wb') as output:
    try:
        result = subprocess.run(command, cwd=data['cwd'], stdout=output,
                                stderr=subprocess.STDOUT, timeout=3600,
                                creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        data.update(state='COMPLETE', exit_code=result.returncode)
    except subprocess.TimeoutExpired:
        data.update(state='TIMEOUT', exit_code=None)
    except Exception as exc:
        data.update(state='ERROR', error=repr(exc), exit_code=None)
data['finished_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
data['source_sha256_after'] = hashlib.sha256(source.read_bytes()).hexdigest()
record.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps(data, indent=2), flush=True)
print(log.read_text(encoding='utf-8', errors='replace'), flush=True)
