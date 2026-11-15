#!/usr/bin/env python3
"""Measure a supplied local calculation through its JSON serialization."""
import json
import os
from pathlib import Path
import resource
import runpy
import signal
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(180,180))
signal.alarm(900)
assert os.environ.get('OMP_NUM_THREADS')=='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15
target=Path(sys.argv[1])
assert target.name in ('twelve.py','audit_twelve.py') and target.parent==Path('.')
sys.argv=sys.argv[1:]
start=time.monotonic()
runpy.run_path(str(target),run_name='__main__')
peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert peak<1_000_000_000
result=dict(target=str(target),arguments=sys.argv[1:],
            elapsed_seconds_including_serialization=time.monotonic()-start,
            peak_rss_bytes_including_serialization=peak,
            priority=os.getpriority(os.PRIO_PROCESS,0))
Path(target.stem+'_resources.json').write_text(json.dumps(result,indent=2)+'\n')
print('FULL RUN RESOURCES: '+str(result),flush=True)
