#!/usr/bin/env python3
"""Geometry-only nested circuit peeling; finite conditioned measurements."""
import argparse
from collections import Counter
import csv
import json
import os
from pathlib import Path
import random
import resource
import signal
import statistics
import time
from sample_percolation import (DIRS, DIR_INDEX, ball, norm, edges_of, location,
                               canonical, connected_to_boundary, measure)

ROOT = Path(__file__).resolve().parent


def enclosing_candidates(vertices):
    adj = {v: [] for v in vertices}
    for u,v in edges_of(vertices):
        adj[u].append(v)
        adj[v].append(u)
    for v in adj:
        adj[v].sort(key=lambda u: DIR_INDEX[(u[0]-v[0],u[1]-v[1])])
    unseen = {(u,v) for u in adj for v in adj[u]}
    candidates = set()
    for first in sorted(unseen):
        if first not in unseen:
            continue
        arc,walk = first,[]
        while True:
            unseen.remove(arc)
            u,v = arc
            walk.append(u)
            ns = adj[v]
            arc = (v,ns[(ns.index(u)-1) % len(ns)])
            if arc == first:
                break
        stack,positions = [],{}
        for v in walk+[walk[0]]:
            if v in positions:
                j = positions[v]
                cycle = stack[j:]
                if len(cycle) >= 3 and location((0,0),cycle) == 1:
                    candidates.add(canonical(cycle))
                for w in stack[j+1:]:
                    del positions[w]
                stack = stack[:j+1]
            else:
                positions[v] = len(stack)
                stack.append(v)
    return candidates


def twice_area(cycle):
    return abs(sum(u[0]*v[1]-u[1]*v[0]
                   for u,v in zip(cycle,cycle[1:]+cycle[:1])))


def peel(sites, radius):
    remaining = {v for v in sites if 1 <= norm(v) < radius}
    cycles,trace = [],[]
    while True:
        candidates = enclosing_candidates(remaining)
        trace.append(dict(remaining_vertices=len(remaining),candidates=len(candidates)))
        if not candidates:
            break
        cycle = list(min(candidates,key=lambda c:(twice_area(c),c)))
        assert len(cycle) == len(set(cycle))
        if cycles:
            assert all(location(v,cycle) == 1 for v in cycles[-1])
        cycles.append(cycle)
        remaining = {v for v in remaining if location(v,cycle) == -1}
    return cycles,trace


def summarize(rows):
    output = []
    for radius in sorted({r['radius'] for r in rows}):
        group = [r for r in rows if r['radius'] == radius]
        counts = Counter(r['circuits'] for r in group)
        entry = dict(radius=radius,samples=len(group),
                     circuit_counts={str(k):counts[k] for k in range(max(counts)+1)})
        for name,subset in [('with_circuits',[r for r in group if r['circuits']]),
                            ('multiple_circuits',[r for r in group if r['circuits']>=2])]:
            entry[name] = dict(samples=len(subset))
            for key in ['C_over_A','R_over_A','D_over_C']:
                vals = [r[key] for r in subset if r[key] is not None]
                entry[name][key] = dict(min=min(vals),median=statistics.median(vals),max=max(vals)) if vals else None
        output.append(entry)
    return output


def main(args):
    start = time.monotonic()
    # Full disk has all concentric hexagonal rings under this rule.
    for r in range(2,8):
        cycles,_ = peel(set(ball(r)),r)
        assert [len(c) for c in cycles] == [6*k for k in range(1,r)]
        assert [twice_area(c) for c in cycles] == [6*k*k for k in range(1,r)]
    rng = random.Random(args.seed)
    saved = [json.loads(s) for s in Path(args.replay).read_text().splitlines()] if args.replay else None
    records = iter(saved) if saved is not None else None
    rows,details,attempts = [],[],{}
    prefix = ROOT/args.prefix
    with Path(str(prefix)+'_configurations.jsonl').open('w') as cf, Path(str(prefix)+'_samples.csv').open('w',newline='') as sf, Path(str(prefix)+'_circuits.csv').open('w',newline='') as df:
        sw = dw = None
        for radius in args.radii:
            vertices = ball(radius)
            proposals = 0
            for index in range(args.samples):
                if records is not None:
                    record = next(records)
                    assert record['radius'] == radius
                    sites = set(map(tuple,record['open_sites']))
                    proposals = record['proposal']
                else:
                    while True:
                        proposals += 1
                        sites = {v for v in vertices if v == (0,0) or rng.getrandbits(1)}
                        if connected_to_boundary(sites,radius):
                            break
                assert connected_to_boundary(sites,radius)
                cycles,trace = peel(sites,radius)
                sample_id = f'{radius}-{index:03}'
                config = dict(sample_id=sample_id,radius=radius,proposal=proposals,
                              open_sites=sorted(sites),cycles=cycles,peeling_trace=trace)
                cf.write(json.dumps(config,separators=(',',':'))+'\n')
                cf.flush()
                row,circuit_data = measure(sites,cycles,radius)
                row = dict(sample_id=sample_id,proposal=proposals,**row)
                if sw is None:
                    sw = csv.DictWriter(sf,fieldnames=list(row)); sw.writeheader()
                sw.writerow(row); sf.flush(); rows.append(row)
                for j,(cycle,detail) in enumerate(zip(cycles,circuit_data)):
                    detail = dict(sample_id=sample_id,circuit_index=j,twice_coordinate_area=twice_area(cycle),**detail)
                    if dw is None:
                        dw = csv.DictWriter(df,fieldnames=list(detail)); dw.writeheader()
                    dw.writerow(detail); details.append(detail)
                df.flush()
                assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1024**3
                if (index+1)%10 == 0:
                    print(f'R={radius} {index+1}/{args.samples}; multiple={sum(r["circuits"]>=2 for r in rows)}; elapsed={time.monotonic()-start:.2f}s',flush=True)
            attempts[radius] = proposals
    if records is not None:
        assert next(records,None) is None
    output = dict(seed=None if saved is not None else args.seed,replay=args.replay,
                  samples_per_radius=args.samples,radii=args.radii,proposals=attempts,
                  summary=summarize(rows),total_circuits=len(details),
                  multiple_circuit_samples=sum(r['circuits']>=2 for r in rows),
                  max_relative_solve_gap=max(r['max_solve_relative_gap'] for r in rows),
                  max_conservation_error=max(r['max_conservation_error'] for r in rows),
                  max_layer_components=max(r['max_layer_components'] for r in rows),
                  circuit_radius_ranges=[dict(radius=r,count=sum(row['min_radius']==r for row in details))
                                         for r in sorted({row['min_radius'] for row in details})],
                  effective_nice=os.getpriority(os.PRIO_PROCESS,0),
                  elapsed_seconds=time.monotonic()-start,
                  peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path(str(prefix)+'_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples',type=int,default=40)
    parser.add_argument('--radii',type=int,nargs='+',default=[12,24,48])
    parser.add_argument('--seed',type=int,default=202611150652)
    parser.add_argument('--replay')
    parser.add_argument('--prefix',default='pilot')
    args = parser.parse_args()
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100))
    signal.alarm(1180)
    main(args)
