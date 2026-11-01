from pathlib import Path
import datetime
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parent
source = root / 'FiniteChecks.lean'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
assert source.read_bytes().isascii()
assert 'sorry' not in source.read_text()
assert 'native_decide' not in source.read_text()
args = ['lake', 'env', 'lean', str(source)]
started = datetime.datetime.now().isoformat(timespec='seconds')
record = {'state': 'RUNNING', 'started_local': started, 'cwd': '~/lean_verify',
          'command': args, 'source_sha256': digest, 'timeout_seconds': 3600}
report = root / 'lean_result.json'
report.write_text(json.dumps(record, indent=2), encoding='utf8')
(root / 'lean_check.txt').write_text('STATE: RUNNING\nFresh ASCII-source check; no prior success claimed.\nSource SHA256: '+digest+'\n', encoding='utf8')
print('Starting one shared-slot Lean check; source SHA256 '+digest, flush=True)
try:
    with (root / 'lean_stdout.txt').open('w', encoding='utf8') as out:
        result = subprocess.run(args, cwd='~/lean_verify', stdout=out,
                                stderr=subprocess.STDOUT, timeout=3600)
    record['exit_code'] = result.returncode
    record['state'] = 'PASSED' if result.returncode == 0 else 'FAILED'
except subprocess.TimeoutExpired:
    record['state'] = 'TIMEOUT'
    record['exit_code'] = 124
record['finished_local'] = datetime.datetime.now().isoformat(timespec='seconds')
record['source_unchanged'] = digest == hashlib.sha256(source.read_bytes()).hexdigest()
assert record['source_unchanged']
report.write_text(json.dumps(record, indent=2), encoding='utf8')
output = (root / 'lean_stdout.txt').read_text(encoding='utf8')
(root / 'lean_check.txt').write_text('STATE: '+record['state']+'\nExit code: '+str(record['exit_code'])+'\nSource SHA256: '+digest+'\nCommand: '+' '.join(args)+'\nWorking directory: ~/lean_verify\nSource unchanged during check: true\n\n'+output, encoding='utf8')
print('LEAN RESULT '+record['state']+' exit '+str(record['exit_code']), flush=True)
print(output, flush=True)
