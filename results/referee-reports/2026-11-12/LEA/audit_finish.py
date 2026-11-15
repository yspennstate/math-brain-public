"""Additional sequential checks; invokes the same bounded runner utilities."""
from pathlib import Path
import subprocess
import time


def run(args, output):
    t = time.monotonic()
    with open(output, 'w') as f:
        p = subprocess.run(args, stdout=f, stderr=subprocess.STDOUT, timeout=230)
    print(f'{output}: exit={p.returncode}, elapsed={time.monotonic()-t:.3f}s', flush=True)
    assert p.returncode == 0, Path(output).read_text()


run(['python3','audit_symbolic.py'],'audit_symbolic.out')
for ell in [1,2,3]:
    run(['./audit_sim_ants','run',str(ell),'100000000','1'], f'audit_run_l{ell}_s1_1e8.out')
