"""Run a foreground command with a wall/CPU limit; never starts model workers."""
import os
import resource
import subprocess
import sys
import time

os.environ['OMP_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    raise SystemExit(f'Refusing compute at nice {priority}; require >=15')
resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
try:
    resource.setrlimit(resource.RLIMIT_DATA, (512 * 1024**2, 512 * 1024**2))
    memory_guard = 'data_limit=512MiB'
except (OSError, ValueError) as exc:
    # Darwin may reject DATA limits even below an inherited infinite limit.
    # RSS is advisory there; these programs also have bounded small arrays.
    memory_guard = f'memory bounded by program construction; DATA limit unavailable: {exc}'
start = time.monotonic()
print(f'priority={priority}; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; {memory_guard}', flush=True)
result = subprocess.run(sys.argv[1:], timeout=1140, check=False)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
rss_mib = usage.ru_maxrss / (1024**2 if sys.platform == 'darwin' else 1024)
print(f'exit={result.returncode}; wall_seconds={time.monotonic()-start:.3f}; child_peak_rss_mib={rss_mib:.3f}', flush=True)
raise SystemExit(result.returncode)
