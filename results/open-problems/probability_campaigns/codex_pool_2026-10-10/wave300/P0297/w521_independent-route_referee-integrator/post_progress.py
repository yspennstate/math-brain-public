import subprocess

cmd = [
    'python', '-X', 'utf8', '~/primary_directive/pd_progress.py',
    '--event', 'P0297: 9 further scoped referee verdicts, D0049 wrong identity patch checked, 2 brain drafts submitted (4 concepts, 6 links), 0 live nodes yet; parent gap remains.',
    '--agent', 'w521',
    '--row', 'S1.1',
    '--evidence', '~/brain_workers/w521/REPORT.md',
]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
except subprocess.TimeoutExpired:
    print('PROGRESS_TIMEOUT_60S')
else:
    print('PROGRESS_RC', result.returncode)
    print(result.stdout[:1500])
    print(result.stderr[:1500])
