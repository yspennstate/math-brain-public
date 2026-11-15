#!/usr/bin/env python3
"""Exact checks of the per-radius largest repair ratios, including single circuits."""
import csv
import json
import os
from pathlib import Path
import resource
import signal
import time
from audit_peeling import exact_sample

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
resource.setrlimit(resource.RLIMIT_CPU,(1100,1100)); signal.alarm(1180)
start = time.monotonic()
output = []
for prefix in ['pilot','ensemble']:
    rows = list(csv.DictReader(open(prefix+'_samples.csv')))
    selected = {}
    for radius in {int(r['radius']) for r in rows}:
        group = [r for r in rows if int(r['radius'])==radius and int(r['circuits'])>0]
        row = max(group,key=lambda r:float(r['C_over_A']))
        selected[row['sample_id']] = row
    for line in Path(prefix+'_configurations.jsonl').open():
        config = json.loads(line)
        if config['sample_id'] in selected:
            result = exact_sample(config,selected[config['sample_id']])
            output.append(dict(ensemble=prefix,**result))
            print(prefix,result['sample_id'],'circuits',result['circuits'],'exact outlier passed',flush=True)
result = dict(samples=output,effective_nice=os.getpriority(os.PRIO_PROCESS,0),
              peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              elapsed_seconds=time.monotonic()-start)
assert result['peak_RSS_bytes']<1024**3
Path('outlier_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print('elapsed',result['elapsed_seconds'],'RSS',result['peak_RSS_bytes'])
