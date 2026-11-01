"""Preserve the interrupted check record and finish the ordinary proof report."""
from pathlib import Path
import datetime, hashlib, json

root = Path(__file__).resolve().parent
path = root/'lean_check_result.json'
raw = path.read_bytes()
data = json.loads(raw)
assert data['state'] == 'RUNNING'
now = datetime.datetime.now(datetime.timezone.utc)
start = datetime.datetime.fromisoformat(data['started_utc'])
elapsed = (now-start).total_seconds()
assert elapsed > data['timeout_seconds']
assert hashlib.sha256((root/'Prefix.lean').read_bytes()).hexdigest() == data['source_sha256']
assert 'waiting for a Lean slot' in (root/'lean_check.log').read_text(encoding='utf-8', errors='replace')

# The preceding read-only Windows process query returned exit code 0 and
# no matches for this runner/checker. Do not fabricate a compiler exit code.
(root/'lean_check_result.before_assessment.json').write_bytes(raw)
data.update(
    state='UNRECOVERED',
    exit_code=None,
    assessment_utc=now.isoformat(),
    observed_elapsed_seconds=elapsed,
    assessment=('The tool session is unavailable. A read-only Win32_Process query '
                'found no matching live run_lean_check.py or E0062/Prefix.lean '
                'process among python, Lean, lake, PowerShell, pwsh and cmd. '
                'The original result marker is stale RUNNING beyond the nominal '
                'one-hour limit, and the log records only a slot wait. '
                'The compiler outcome is unknown, not a confirmed timeout or error.'),
    original_marker='lean_check_result.before_assessment.json',
    source_sha256_observed=hashlib.sha256((root/'Prefix.lean').read_bytes()).hexdigest(),
)
path.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps(data, indent=2), flush=True)

import finalize_records
