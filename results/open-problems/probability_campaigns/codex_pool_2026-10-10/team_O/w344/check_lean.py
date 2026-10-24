import hashlib
import json
import os
import pathlib
import subprocess

here = pathlib.Path(__file__).resolve().parent
source = here / 'C0004Counterexample.lean'
reviewed = hashlib.sha256(source.read_bytes()).hexdigest()
env = dict(os.environ)
env['LEAN_CHECK_DIR'] = str(here / 'lean_receipts')
env['PYTHONDONTWRITEBYTECODE'] = '1'
command = ['python', '-X', 'utf8', '~/.claude/dreaming/lean_check.py', '--file', str(source), '--core', '--target', 'mean_equality_and_dependence', '--reviewed-sha256', reviewed, '--timeout', '55', '--json']
result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', env=env, timeout=85)
receipt = {'command': command, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr, 'scope': 'Only the named arithmetic lemma; not the general DGFF density problem.'}
(here / 'lean_check_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt))
