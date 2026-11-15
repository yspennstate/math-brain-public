import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
groups=defaultdict(list)
for r in csv.DictReader((ROOT/'data'/'simulation.csv').open()):
    groups[(int(r['n']),float(r['alpha']))].append(r)
output=[]
for (n,alpha),rows in sorted(groups.items()):
    vals=[float(r['local_over_log2']) for r in rows]
    rad=[float(r['radius_log_exponent']) for r in rows]
    output.append(dict(n=n,alpha=alpha,reps=len(rows),
        max_local_mean=statistics.mean(vals),max_local_median=statistics.median(vals),
        max_local_standard_error=statistics.stdev(vals)/math.sqrt(len(vals)),
        max_local_limit=4*alpha**2/math.pi,
        disc_exponent_mean=statistics.mean(rad),disc_exponent_prediction=alpha/2))
with (ROOT/'data'/'summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(output[0]));w.writeheader();w.writerows(output)
text=['| n | α | paths | mean M/log²n | standard error | limit | mean log R/log n | predicted exponent |',
      '|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in output:
    text.append('| {n} | {alpha:g} | {reps} | {max_local_mean:.4f} | {max_local_standard_error:.4f} | {max_local_limit:.4f} | {disc_exponent_mean:.4f} | {disc_exponent_prediction:.3f} |'.format(**r))
(ROOT/'data'/'SUMMARY.md').write_text('\n'.join(text)+'\n')
