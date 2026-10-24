from pathlib import Path
import datetime
import hashlib
import subprocess
import time

root = Path(__file__).resolve().parent
source = root / 'FiniteAlgebra.lean'
data = source.read_bytes()
assert not data.startswith(b'\xef\xbb\xbf'), 'Remove BOM before running Lean'
command = ['lake', 'env', 'lean', '-M', '900', str(source)]
start = time.monotonic()
with (root / 'lean_check.log').open('w', encoding='utf8') as output:
    output.write('Start UTC: ' + datetime.datetime.now(datetime.timezone.utc).isoformat() + '\n')
    output.write('Command: ' + ' '.join(command) + '\n')
    output.write('Source SHA256: ' + hashlib.sha256(data).hexdigest() + '\n')
    output.write('Timeout seconds: 3600; Lean memory limit MiB: 900\n')
    output.flush()
    print('Started single local Lean check; incremental log: lean_check.log', flush=True)
    try:
        result = subprocess.run(command, cwd=r'~/lean_verify',
                                stdout=output, stderr=subprocess.STDOUT, timeout=3600)
        output.write('\nExit: ' + str(result.returncode) + '\n')
    except Exception as exc:
        output.write('\nRun did not complete: ' + repr(exc) + '\n')
    output.write('Elapsed seconds: ' + str(time.monotonic() - start) + '\n')
print((root / 'lean_check.log').read_text(encoding='utf8'), flush=True)
