#!/usr/bin/env python3
"""Independent replay, planar dual, exact arithmetic and summary audits."""
from collections import defaultdict, deque
import csv
import json
import os
from pathlib import Path
import random
import resource
import signal
import statistics
import time

from sample_percolation import (DIRS,ball,norm,edges_of,location,decompose,
                                select_circuit,circuit_cost)
from recheck_previous import exact_flow,cycle_cost


def edge_key(u,v):
    return tuple(sorted((u,v)))


def closed_crossing(sites,lo,hi):
    closed = {v for v in ball(hi) if lo <= norm(v) and v not in sites}
    seen = {v for v in closed if norm(v) == lo}
    todo = list(seen)
    while todo:
        a,b = todo.pop()
        for da,db in DIRS:
            v = (a+da,b+db)
            if v in closed and v not in seen:
                seen.add(v)
                todo.append(v)
    return any(norm(v) == hi for v in seen)


def triangulation(radius):
    vs = set(ball(radius))
    faces = []
    # The anchor of a downward triangle can lie outside the hexagonal ball
    # even when all three vertices of that triangle lie inside it.
    for a,b in ball(radius+1):
        for tri in [((a,b),(a+1,b),(a,b+1)),
                    ((a+1,b),(a,b+1),(a+1,b+1))]:
            if all(v in vs for v in tri):
                faces.append(tri)
    edge_faces = defaultdict(list)
    vertex_faces = defaultdict(list)
    for j,tri in enumerate(faces):
        for v in tri:
            vertex_faces[v].append(j)
        for u,v in zip(tri,tri[1:]+tri[:1]):
            edge_faces[edge_key(u,v)].append(j)
    assert all(len(fs) in (1,2) for fs in edge_faces.values())
    return faces,edge_faces,vertex_faces


def check_geometric_split(radius,cycle,sites,edges,mesh):
    faces,edge_faces,vertex_faces = mesh
    barrier = {edge_key(u,v) for u,v in zip(cycle,cycle[1:]+cycle[:1])}
    adj = [[] for _ in faces]
    outside = set()
    for edge,fs in edge_faces.items():
        if edge in barrier:
            continue
        if len(fs) == 1:
            outside.add(fs[0])
        else:
            u,v = fs
            adj[u].append(v)
            adj[v].append(u)
    todo = list(outside)
    for u in todo:
        for v in adj[u]:
            if v not in outside:
                outside.add(v)
                todo.append(v)
    for v in sites-set(cycle):
        statuses = {j in outside for j in vertex_faces[v]}
        assert len(statuses) == 1
        assert (location(v,cycle) == -1) == statuses.pop()
    twice = [(2*a,2*b) for a,b in cycle]
    for u,v in edges:
        key = edge_key(u,v)
        midpoint = (u[0]+v[0],u[1]+v[1])
        if key in barrier:
            assert location(midpoint,twice) == 0
        else:
            statuses = {j in outside for j in edge_faces[key]}
            assert len(statuses) == 1, (radius,key,edge_faces[key],statuses)
            assert (location(midpoint,twice) == -1) == statuses.pop()


def brute_circuit_exists(sites):
    """Independent simple-cycle DFS for small annuli only."""
    adj = {v:[] for v in sites}
    for u,v in edges_of(sites):
        adj[u].append(v)
        adj[v].append(u)
    for start in sorted(sites):
        path,seen = [start],{start}
        def walk(u):
            for v in adj[u]:
                if v == start and len(path) >= 3 and location((0,0),path) == 1:
                    return True
                if v > start and v not in seen:
                    path.append(v)
                    seen.add(v)
                    if walk(v):
                        return True
                    path.pop()
                    seen.remove(v)
            return False
        if walk(start):
            return True
    return False


def main():
    start = time.monotonic()
    configs = [json.loads(line) for line in Path('configurations.jsonl').read_text().splitlines()]
    thin = [json.loads(line) for line in Path('thin_configurations.jsonl').read_text().splitlines()]
    rows = list(csv.DictReader(open('samples.csv')))
    circuit_rows = list(csv.DictReader(open('circuits.csv')))
    result = json.loads(Path('sample_results.json').read_text())
    assert len(configs) == len(thin) == len(rows) == 120
    rng = random.Random(result['seed'])
    proposals = {}
    vertex_lists = {r:ball(r) for r in result['radii']}
    # Reproduce every random bit and every rejected proposal independently.
    from sample_percolation import connected_to_boundary
    for config,old in zip(configs,thin):
        r = config['radius']
        while True:
            proposals[r] = proposals.get(r,0)+1
            sites = {v for v in vertex_lists[r] if v == (0,0) or rng.getrandbits(1)}
            if connected_to_boundary(sites,r):
                break
        assert sorted(sites) == list(map(tuple,config['open_sites']))
        assert config['open_sites'] == old['open_sites']
        assert proposals[r] == config['proposal'] == old['proposal']
    diagnostics = defaultdict(lambda:[0,0])
    meshes = {r:triangulation(r) for r in result['radii']}
    geometries = 0
    for kind,records in [('thin',thin),('wide',configs)]:
        for config in records:
            r = config['radius']
            sites = set(map(tuple,config['open_sites']))
            for (lo,hi),selected in zip(config['annuli'],config['selected_cycles']):
                crossing = closed_crossing(sites,lo,hi)
                assert bool(selected) == (not crossing), (kind,config['sample_id'],lo,hi)
                diagnostics[kind,r][bool(selected)] += 1
                if selected:
                    cycle = list(map(tuple,selected))
                    assert len(cycle) == len(set(cycle))
                    assert all(v in sites and lo <= norm(v) <= hi for v in cycle)
                    assert location((0,0),cycle) == 1
                    assert all((v[0]-u[0],v[1]-u[1]) in DIRS
                               for u,v in zip(cycle,cycle[1:]+cycle[:1]))
                    if kind == 'wide':
                        check_geometric_split(r,cycle,sites,edges_of(sites),meshes[r])
                        geometries += 1
    # Compare face-walk selection to explicit simple-cycle enumeration on
    # small random annuli, including masks with many spurs and repeated walks.
    small_rng = random.Random(9813)
    annulus = [v for v in ball(2) if norm(v) >= 1]
    brute_count = 0
    for _ in range(256):
        sites = {v for v in annulus if small_rng.getrandbits(1)}
        selected = select_circuit(sites,1,2)
        assert bool(selected) == brute_circuit_exists(sites)
        assert bool(selected) == (not closed_crossing(sites,1,2))
        brute_count += bool(selected)
    print('Random replay and planar audits passed.',flush=True)
    # All nontrivial smallest-radius samples: exact fractions independently
    # recompute R, every local wired profile, A and the actual circuit cost.
    exact_rows = []
    for config,row in zip(configs,rows):
        if config['radius'] != 12 or int(row['circuits']) == 0:
            continue
        sites = set(map(tuple,config['open_sites']))
        cycles = [list(map(tuple,c)) for c in config['selected_cycles'] if c]
        edges = edges_of(sites)
        pieces,boundaries,_ = decompose(sites,edges,cycles,12)
        local = [exact_flow([(u,v,1) for u,v in e],l,r)
                 for e,l,r in zip(pieces,boundaries,boundaries[1:])]
        r,_,_ = exact_flow([(u,v,1) for u,v in edges],boundaries[0],boundaries[-1])
        a = sum(s[0] for s in local)
        c = 0
        for j,cycle in enumerate(cycles):
            da,db = local[j][2],local[j+1][2]
            delta = [-da[v]-db[v] for v in cycle]
            c += cycle_cost([1]*len(cycle),delta)
        assert 0 <= r-a <= c
        for key,value in [('R',r),('A',a),('C',c)]:
            assert abs(float(value)-float(row[key])) < 1e-9
        exact_rows.append(dict(sample_id=config['sample_id'],R=str(r),A=str(a),C=str(c)))
        print('Exact rational sample passed:',config['sample_id'],flush=True)
    # Recompute every reported statistic from CSV independently of aggregate().
    for group in result['summary']:
        data = [row for row in rows if int(row['radius']) == group['radius']]
        counts = [sum(int(row['circuits']) == k for row in data) for k in range(3)]
        assert counts == group['circuit_counts']
        for name,predicate in [('with_circuits',lambda k:k>0),('two_circuits',lambda k:k==2)]:
            selected = [row for row in data if predicate(int(row['circuits']))]
            for key,stats in group[name].items():
                vals = sorted(float(row[key]) for row in selected)
                n = len(vals)
                median = vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2
                assert stats == dict(min=vals[0],median=median,max=vals[-1])
    active_circuits = [{key:float(row[key]) for key in ['length','Q','TV','coarse','variance']}
                       for row in circuit_rows]
    ratios = [row['coarse']/row['Q'] for row in active_circuits if row['Q'] > 0]
    out = dict(configurations_reproduced=len(configs),
               closed_crossing_diagnostics={f'{kind}_{r}':counts for (kind,r),counts in diagnostics.items()},
               dual_face_geometric_checks=geometries,
               brute_force_annuli=256,brute_force_positive=brute_count,
               exact_nontrivial_samples=exact_rows,
               circuit_coarse_over_actual=dict(min=min(ratios),median=statistics.median(ratios),max=max(ratios)),
               max_shell_components=max(int(row['max_layer_components']) for row in rows),
               effective_nice=os.getpriority(os.PRIO_PROCESS,0),
               peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               elapsed_seconds=time.monotonic()-start)
    assert out['peak_RSS_bytes'] < 1024**3
    Path('sample_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'exact_nontrivial_samples'},indent=2))


if __name__ == '__main__':
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100))
    signal.alarm(1180)
    main()
