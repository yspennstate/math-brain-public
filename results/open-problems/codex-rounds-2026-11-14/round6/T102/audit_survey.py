#!/usr/bin/env python3
"""Streaming independent audit of geometry census and multi-interface solves."""
from collections import Counter,defaultdict
import csv
import gzip
import json
import os
from pathlib import Path
import random
import resource
import signal
import statistics
import time
from sample_percolation import ball,connected_to_boundary,norm,edges_of,location
from peel_circuits import peel
from audit_samples import triangulation,check_geometric_split
from audit_peeling import dual_cycle_exists,exact_sample,validate_circuit_records


def main():
    start = time.monotonic()
    result = json.loads(Path('survey_results.json').read_text())
    rows = list(csv.DictReader(open('survey_samples.csv')))
    census = list(csv.DictReader(open('survey_census.csv')))
    by_id = {r['sample_id']:r for r in rows}
    details = defaultdict(list)
    for detail in csv.DictReader(open('survey_circuits.csv')):
        details[detail['sample_id']].append(detail)
    exact_ids = {r['sample_id'] for r in rows[:2]}
    exact_ids.add(max(rows,key=lambda r:float(r['C_over_A']))['sample_id'])
    exact_ids.add(max(rows,key=lambda r:int(r['circuits']))['sample_id'])
    rng = random.Random(result['seed'])
    radius = result['radius']; vertices = ball(radius); mesh = triangulation(radius)
    proposals = checked = geometry = 0
    counts = Counter(); scales = defaultdict(Counter); exact = []
    with gzip.open('survey_configurations.jsonl.gz','rt') as cf:
        for config,entry in zip(map(json.loads,cf),census,strict=True):
            checked += 1
            sites = set(map(tuple,config['open_sites']))
            while True:
                proposals += 1
                fresh = {v for v in vertices if v == (0,0) or rng.getrandbits(1)}
                if connected_to_boundary(fresh,radius):
                    break
            assert fresh == sites
            assert config['proposal'] == proposals == int(entry['proposal'])
            assert config['sample_id'] == entry['sample_id']
            selected,trace = peel(sites,radius)
            assert selected == [list(map(tuple,c)) for c in config['cycles']]
            assert trace == config['peeling_trace']
            k = len(selected); counts[k] += 1
            assert int(entry['circuits']) == k
            assert (config['sample_id'] in by_id) == (k>=2) == bool(int(entry['electrically_measured']))
            if k>=2:
                validate_circuit_records(config,by_id[config['sample_id']],details[config['sample_id']])
            remaining = {v for v in sites if 1 <= norm(v) < radius}
            for cycle in selected+[None]:
                assert dual_cycle_exists(remaining,mesh) == (cycle is not None)
                geometry += 1
                if cycle is not None:
                    check_geometric_split(radius,cycle,sites,edges_of(sites),mesh)
                    lo,hi = min(map(norm,cycle)),max(map(norm,cycle))
                    scales['all_min'][lo] += 1; scales['all_max'][hi] += 1
                    if k>=2:
                        scales['multiple_min'][lo] += 1; scales['multiple_max'][hi] += 1
                    remaining = {v for v in remaining if location(v,cycle) == -1}
            if config['sample_id'] in exact_ids:
                exact.append(exact_sample(config,by_id[config['sample_id']]))
                print('exact',config['sample_id'],flush=True)
            if checked%200 == 0:
                print('survey audit',checked,'/',len(census),flush=True)
    assert checked == result['samples'] and proposals == result['proposals']
    assert {str(k):counts[k] for k in range(max(counts)+1)} == result['circuit_counts']
    assert len(rows) == result['electrically_measured'] == sum(n for k,n in counts.items() if k>=2)
    summary = result['measured_summary'][0]['multiple_circuits']
    for key in ['C_over_A','R_over_A','D_over_C']:
        vals = sorted(float(r[key]) for r in rows if r[key]); n = len(vals)
        stats = dict(min=vals[0],max=vals[-1],median=vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2) if vals else None
        assert summary[key] == stats
    out = dict(configurations_reproduced=checked,proposals_reproduced=proposals,
               dual_existence_and_termination_checks=geometry,
               exact_samples=exact,scale_counts={k:dict(sorted(v.items())) for k,v in scales.items()},
               effective_nice=os.getpriority(os.PRIO_PROCESS,0),
               peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               elapsed_seconds=time.monotonic()-start)
    assert out['peak_RSS_bytes'] < 1024**3
    Path('survey_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['exact_samples','scale_counts']},indent=2),flush=True)


if __name__ == '__main__':
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100)); signal.alarm(1180)
    main()
