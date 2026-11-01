"""Apply the review diff only in a fresh miniature repository inside w382."""
from pathlib import Path
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
sandbox = ROOT / ('patch_check_' + str(time.time_ns()))
target = sandbox / '.claude' / 'dreaming' / 'brain.py'
target.parent.mkdir(parents=True)
assert target.resolve().is_relative_to(ROOT)
target.write_bytes((ROOT/'copies'/'brain.before.py').read_bytes())
patch = ROOT/'patches'/'01_recall_retracted_tag_override.diff'
commands = [['git', 'init', '--quiet', str(sandbox)],
    ['git', '-C', str(sandbox), '-c', 'core.autocrlf=false', 'apply', '--check', str(patch)],
    ['git', '-C', str(sandbox), '-c', 'core.autocrlf=false', 'apply', str(patch)]]
for command in commands:
    completed = subprocess.run(command, capture_output=True, text=True, timeout=30)
    if completed.returncode:
        raise SystemExit(json.dumps({'command':command, 'returncode':completed.returncode,
            'stdout':completed.stdout, 'stderr':completed.stderr}))
actual = target.read_bytes()
expected = (ROOT/'copies'/'brain.after.py').read_bytes()
assert actual == expected, 'Applied diff did not reproduce the tested candidate.'
receipt = {'command':'python -X utf8 check_patch_application.py', 'passed': True,
    'sandbox':str(sandbox), 'applied_candidate_sha256':hashlib.sha256(actual).hexdigest(),
    'elapsed_seconds':round(time.perf_counter()-started,6), 'live_file_modified': False}
(ROOT/'PATCH_APPLICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
