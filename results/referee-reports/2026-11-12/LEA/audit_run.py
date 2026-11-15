"""Sequential, bounded audit runner; no jobs overlap. Outputs stay in this folder."""
import os
from pathlib import Path
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
try:
    os.nice(10)
except PermissionError:
    print('Sandbox prohibits changing process niceness; jobs remain sequential and bounded.', flush=True)
# Inherited by every child, including the C simulator; <1 GiB per job.
for limit_name in ['RLIMIT_AS', 'RLIMIT_DATA']:
    try:
        resource.setrlimit(getattr(resource, limit_name), (768*1024**2, 768*1024**2))
        print(f'{limit_name}: 768 MiB limit applied', flush=True)
    except (ValueError, OSError) as exc:
        print(f'{limit_name}: unavailable ({exc}); workloads use small finite graphs and fixed-size C arrays.', flush=True)
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))


def run(args, output, timeout=230):
    start = time.monotonic()
    with open(output, 'w') as out:
        result = subprocess.run(args, stdout=out, stderr=subprocess.STDOUT, timeout=timeout)
    elapsed = time.monotonic()-start
    print(f'{output}: exit={result.returncode}, elapsed={elapsed:.3f}s', flush=True)
    if result.returncode:
        raise RuntimeError(Path(output).read_text())


run(['python3', 'audit_exact.py'], 'audit_exact.out')
run(['python3', 'code/check_path_law.py'], 'audit_author_check.out')
run(['cc', '-O2', 'code/sim_ants.c', '-o', 'audit_sim_ants'], 'audit_compile.out')
for ell in [1, 2, 3]:
    run(['./audit_sim_ants', 'run', str(ell), '10000000', '1'], f'audit_run_l{ell}_s1.out')
run(['./audit_sim_ants', 'freeze', '2', '2', '3', '1', '4', '2', '2000000', '1'], 'audit_freeze_l2.out')
run(['./audit_sim_ants', 'freeze', '3', '5', '2', '3', '4', '1', '2000000', '1'], 'audit_freeze_l3.out')
