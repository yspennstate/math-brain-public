#!/usr/bin/env python3
"""Report tables derived from the saved, independently audited CSV files."""
import csv
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import signal
import statistics

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
resource.setrlimit(resource.RLIMIT_CPU,(30,30)); signal.alarm(60)

for prefix in ['pilot','ensemble']:
    result = json.loads(Path(prefix+'_results.json').read_text())
    rows = list(csv.DictReader(open(prefix+'_samples.csv')))
    details = list(csv.DictReader(open(prefix+'_circuits.csv')))
    print(prefix,'samples',len(rows),'circuits',len(details))
    for radius in result['radii']:
        group = [r for r in rows if int(r['radius'])==radius]
        counts = [sum(int(r['circuits'])==k for r in group) for k in range(1+max(int(r['circuits']) for r in group))]
        active = [r for r in group if int(r['circuits'])>0]
        multi = [r for r in group if int(r['circuits'])>=2]
        print('R',radius,'counts',counts,'C/A active median/max',
              statistics.median(float(r['C_over_A']) for r in active),max(float(r['C_over_A']) for r in active),
              'multi',len(multi),
              'multi median/max',statistics.median(float(r['C_over_A']) for r in multi) if multi else None,
              max((float(r['C_over_A']) for r in multi),default=None))
    print('length range',min(int(d['length']) for d in details),max(int(d['length']) for d in details))
    print('min radius <=2',sum(int(d['min_radius'])<=2 for d in details),'/',len(details),
          'max radius median',statistics.median(int(d['max_radius']) for d in details))
    audit = json.loads(Path(prefix+'_audit.json').read_text())
    for x in audit['exact_multi_interface_samples']:
        r,a,c = (F(x[k]) for k in ['R','A','C'])
        assert 0<=r-a<=c
        print('exact',x['sample_id'],'interfaces',x['circuits'],'R,A,C',float(r),float(a),float(c),
              'C/A',float(c/a),'D/C',float((r-a)/c))
    print('resources production',result['elapsed_seconds'],result['peak_RSS_bytes'],
          'audit',audit['elapsed_seconds'],audit['peak_RSS_bytes'])

result = json.loads(Path('survey_results.json').read_text())
audit = json.loads(Path('survey_audit.json').read_text())
rows = list(csv.DictReader(open('survey_samples.csv')))
details = list(csv.DictReader(open('survey_circuits.csv')))
print('survey','samples',result['samples'],'proposals',result['proposals'],'counts',result['circuit_counts'])
for key in ['C_over_A','R_over_A','D_over_C']:
    vals = [float(r[key]) for r in rows if r[key]]
    print(key,min(vals) if vals else None,statistics.median(vals) if vals else None,max(vals) if vals else None)
print('measured circuits',len(details),'length range',min(int(d['length']) for d in details),max(int(d['length']) for d in details))
for group in ['all','multiple']:
    min_counts = {int(k):v for k,v in audit['scale_counts'][group+'_min'].items()}
    max_counts = {int(k):v for k,v in audit['scale_counts'][group+'_max'].items()}
    expanded = [k for k,v in max_counts.items() for _ in range(v)]
    print(group,'minradius<=2',sum(v for k,v in min_counts.items() if k<=2),'/',sum(min_counts.values()),
          'minradius range',min(min_counts),max(min_counts),'maxradius median',statistics.median(expanded),
          'maxradius range',min(max_counts),max(max_counts))
for x in audit['exact_samples']:
    r,a,c = (F(x[k]) for k in ['R','A','C'])
    assert 0<=r-a<=c
    print('survey exact',x['sample_id'],'interfaces',x['circuits'],'R,A,C',float(r),float(a),float(c),
          'C/A',float(c/a),'D/C',float((r-a)/c))
print('resources survey',result['elapsed_seconds'],result['peak_RSS_bytes'],
      'audit',audit['elapsed_seconds'],audit['peak_RSS_bytes'])
print('AO check',F(91,48)/2,F(91,48)+F(91,96),2*F(91,48)/(F(91,48)+F(91,96)))
