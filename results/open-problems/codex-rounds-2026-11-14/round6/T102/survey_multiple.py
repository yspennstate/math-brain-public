#!/usr/bin/env python3
"""Keep a full geometry census; electrically measure every multi-circuit case."""
import csv
import gzip
import json
import os
from pathlib import Path
import random
import resource
import signal
import time
from collections import Counter
from sample_percolation import ball,connected_to_boundary,measure
from peel_circuits import peel,summarize,twice_area


def main():
    start = time.monotonic()
    radius,samples,seed = 48,2000,202611150700
    rng = random.Random(seed)
    vertices = ball(radius)
    proposals = 0
    counts = Counter()
    measured = []
    with gzip.open('survey_configurations.jsonl.gz','wt') as cf, open('survey_census.csv','w',newline='') as gf, open('survey_samples.csv','w',newline='') as sf, open('survey_circuits.csv','w',newline='') as df:
        gw = csv.DictWriter(gf,fieldnames=['sample_id','radius','proposal','circuits','electrically_measured']); gw.writeheader()
        sw = dw = None
        for index in range(samples):
            while True:
                proposals += 1
                sites = {v for v in vertices if v == (0,0) or rng.getrandbits(1)}
                if connected_to_boundary(sites,radius):
                    break
            cycles,trace = peel(sites,radius)
            sample_id = f'{radius}-{index:04}'
            config = dict(sample_id=sample_id,radius=radius,proposal=proposals,open_sites=sorted(sites),cycles=cycles,peeling_trace=trace)
            cf.write(json.dumps(config,separators=(',',':'))+'\n'); cf.flush()
            counts[len(cycles)] += 1
            gw.writerow(dict(sample_id=sample_id,radius=radius,proposal=proposals,circuits=len(cycles),electrically_measured=int(len(cycles)>=2))); gf.flush()
            if len(cycles)>=2:
                row,details = measure(sites,cycles,radius)
                row = dict(sample_id=sample_id,proposal=proposals,**row)
                if sw is None:
                    sw = csv.DictWriter(sf,fieldnames=list(row)); sw.writeheader()
                sw.writerow(row); sf.flush(); measured.append(row)
                for j,(cycle,detail) in enumerate(zip(cycles,details)):
                    detail = dict(sample_id=sample_id,circuit_index=j,twice_coordinate_area=twice_area(cycle),**detail)
                    if dw is None:
                        dw = csv.DictWriter(df,fieldnames=list(detail)); dw.writeheader()
                    dw.writerow(detail)
                df.flush()
                print('measured',sample_id,'circuits',len(cycles),'C/A',row['C_over_A'],flush=True)
            assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1024**3
            if (index+1)%100 == 0:
                print(f'census {index+1}/{samples}; multi={len(measured)}; elapsed={time.monotonic()-start:.2f}s',flush=True)
    output = dict(radius=radius,samples=samples,seed=seed,proposals=proposals,
                  circuit_counts={str(k):counts[k] for k in range(max(counts)+1)},
                  electrically_measured=len(measured),measurement_rule='every case with at least two selected circuits',
                  measured_summary=summarize(measured),
                  effective_nice=os.getpriority(os.PRIO_PROCESS,0),
                  peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  elapsed_seconds=time.monotonic()-start)
    Path('survey_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2),flush=True)


if __name__ == '__main__':
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100)); signal.alarm(1180)
    main()
