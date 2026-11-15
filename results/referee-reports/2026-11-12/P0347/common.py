"""Local resource limits and timestamped research log."""
import os
for _v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[_v] = '1'
import resource
# macOS may reject RLIMIT_AS below its large reserved address space. RSS is
# checked during each loop instead; all algorithms also have explicit bounds.
try:
    resource.setrlimit(resource.RLIMIT_RSS,(3_800_000_000,3_800_000_000))
except (ValueError,OSError):
    pass
from datetime import datetime
def log(s):
    line = datetime.now().astimezone().isoformat(timespec='seconds')+' — '+s
    with open('LOG.md','a') as f: f.write('\n'+line+'\n')
    print(line, flush=True)
def memory_check():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>3_700_000_000:
        raise MemoryError('3.7 GB RSS ceiling')
