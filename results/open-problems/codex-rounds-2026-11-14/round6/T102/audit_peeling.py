#!/usr/bin/env python3
"""Independent planar-dual and sparse rational audits of peeled samples."""
from collections import Counter, defaultdict
from fractions import Fraction as F
import argparse
import csv
import json
import math
import os
from pathlib import Path
import random
import resource
import signal
import statistics
import time
from sample_percolation import ball,norm,edges_of,location,decompose,DIRS
from peel_circuits import peel,enclosing_candidates,twice_area
from audit_samples import triangulation,check_geometric_split,brute_circuit_exists
from recheck_previous import cycle_cost,exact_flow


def exact_sparse(edges,left,right):
    """Prescribed-current grounded Laplacian, exact sparse Schur elimination."""
    left,right = set(left),set(right)
    def name(v):
        return -1 if v in left else -2 if v in right else v
    adj = defaultdict(dict)
    for u,v in edges:
        u,v = name(u),name(v)
        if u != v:
            adj[u][v] = adj[u].get(v,F(0))+1
            adj[v][u] = adj[v].get(u,F(0))+1
    active,queue = {-2},[-2]
    for u in queue:
        for v in adj[u]:
            if v not in active:
                active.add(v); queue.append(v)
    assert -1 in active
    free = active-{-2}
    matrix = {v:{u:-g for u,g in adj[v].items() if u != -2} for v in free}
    for v in free:
        matrix[v][v] = sum(adj[v].values())
    rhs = {v:F(v == -1) for v in free}
    history = []
    while matrix:
        v = min(matrix,key=lambda u:(len(matrix[u]),repr(u)))
        row = matrix[v]
        d = row[v]
        assert d > 0
        ns = {u:a for u,a in row.items() if u != v}
        history.append((v,d,rhs[v],ns))
        for u,a in ns.items():
            rhs[u] -= a*rhs[v]/d
            for w,b in ns.items():
                value = matrix[u].get(w,F(0))-a*b/d
                if value:
                    matrix[u][w] = value
                else:
                    matrix[u].pop(w,None)
            del matrix[u][v]
        del matrix[v],rhs[v]
    potential = {-2:F(0)}
    for v,d,b,ns in reversed(history):
        potential[v] = (b-sum(a*potential[u] for u,a in ns.items()))/d
    div = {v:F(0) for v in left|right|{v for e in edges for v in e}}
    flow = []
    for u,v in edges:
        f = potential.get(name(u),F(0))-potential.get(name(v),F(0))
        flow.append(f); div[u] += f; div[v] -= f
    assert sum(div[v] for v in left) == 1
    assert sum(div[v] for v in right) == -1
    assert all(d == 0 for v,d in div.items() if v not in left|right)
    energy = sum(f*f for f in flow)
    assert energy == potential[-1]
    return energy,flow,div


def dual_cycle_exists(remaining,mesh):
    """Origin face is separated from exterior iff active edges enclose it."""
    faces,edge_faces,vertex_faces = mesh
    barrier = {tuple(sorted(e)) for e in edges_of(remaining)}
    adj = [[] for _ in faces]
    outside = set()
    for edge,fs in edge_faces.items():
        if edge in barrier:
            continue
        if len(fs) == 1:
            outside.add(fs[0])
        else:
            a,b = fs; adj[a].append(b); adj[b].append(a)
    queue = list(outside)
    for u in queue:
        for v in adj[u]:
            if v not in outside:
                outside.add(v); queue.append(v)
    origin = vertex_faces[(0,0)]
    assert len({f in outside for f in origin}) == 1
    return origin[0] not in outside


def exact_sample(config,row):
    sites = set(map(tuple,config['open_sites']))
    cycles = [list(map(tuple,c)) for c in config['cycles']]
    edges = edges_of(sites)
    pieces,boundaries,_ = decompose(sites,edges,cycles,config['radius'])
    local = [exact_sparse(e,l,r) for e,l,r in zip(pieces,boundaries,boundaries[1:])]
    r,_,_ = exact_sparse(edges,boundaries[0],boundaries[-1])
    a = sum(s[0] for s in local)
    costs = []
    for j,cycle in enumerate(cycles):
        delta = [-local[j][2][v]-local[j+1][2][v] for v in cycle]
        costs.append(cycle_cost([1]*len(cycle),delta))
    c = sum(costs)
    assert 0 <= r-a <= c
    for key,val in [('R',r),('A',a),('C',c)]:
        assert abs(float(val)-float(row[key])) < 1e-9
    return dict(sample_id=config['sample_id'],circuits=len(cycles),R=str(r),A=str(a),C=str(c),costs=list(map(str,costs)))


def validate_circuit_records(config,row,details):
    assert len(details) == len(config['cycles']) == int(row['circuits'])
    for j,(raw,detail) in enumerate(zip(config['cycles'],details)):
        cycle = list(map(tuple,raw)); anchor = cycle[0]
        # Fan-triangle area, independently of the cyclic shoelace expression.
        area = abs(sum((u[0]-anchor[0])*(v[1]-anchor[1])
                       -(v[0]-anchor[0])*(u[1]-anchor[1])
                       for u,v in zip(cycle[1:-1],cycle[2:])))
        assert int(detail['circuit_index']) == j
        assert int(detail['length']) == len(cycle)
        assert int(detail['twice_coordinate_area']) == area
        assert int(detail['min_radius']) == min(map(norm,cycle))
        assert int(detail['max_radius']) == max(map(norm,cycle))
        q,t,n = float(detail['Q']),float(detail['TV']),len(cycle)
        assert abs(q-n*float(detail['variance'])) < 1e-9
        assert abs(float(detail['coarse'])-n*t*t/4) < 1e-9
    assert abs(math.fsum(float(d['Q']) for d in details)-float(row['C'])) < 1e-9


def main(prefix):
    start = time.monotonic()
    configs = [json.loads(s) for s in Path(prefix+'_configurations.jsonl').read_text().splitlines()]
    rows = list(csv.DictReader(open(prefix+'_samples.csv')))
    details = list(csv.DictReader(open(prefix+'_circuits.csv')))
    results = json.loads(Path(prefix+'_results.json').read_text())
    by_id = defaultdict(list)
    for detail in details:
        by_id[detail['sample_id']].append(detail)
    assert len(configs) == len(rows)
    meshes = {r:triangulation(r) for r in results['radii']}
    checks = geometries = 0
    rng = random.Random(results['seed']) if results['seed'] is not None else None
    proposals = Counter()
    old = [json.loads(s) for s in Path(results['replay']).read_text().splitlines()] if rng is None else None
    for index,(config,row) in enumerate(zip(configs,rows)):
        radius = config['radius']
        sites = set(map(tuple,config['open_sites']))
        if rng is not None:
            from sample_percolation import connected_to_boundary
            while True:
                proposals[radius] += 1
                fresh = {v for v in ball(radius) if v == (0,0) or rng.getrandbits(1)}
                if connected_to_boundary(fresh,radius):
                    break
            assert fresh == sites and proposals[radius] == config['proposal']
        else:
            assert config['open_sites'] == old[index]['open_sites']
            assert config['proposal'] == old[index]['proposal']
        cycles = [list(map(tuple,c)) for c in config['cycles']]
        validate_circuit_records(config,row,by_id[config['sample_id']])
        selected,trace = peel(sites,radius)
        assert cycles == selected and trace == config['peeling_trace']
        assert len(cycles) == int(row['circuits'])
        remaining = {v for v in sites if 1 <= norm(v) < radius}
        for cycle in cycles+[None]:
            assert dual_cycle_exists(remaining,meshes[radius]) == (cycle is not None)
            checks += 1
            if cycle is None:
                continue
            assert set(cycle) <= remaining and len(cycle) == len(set(cycle))
            assert all((v[0]-u[0],v[1]-u[1]) in DIRS for u,v in zip(cycle,cycle[1:]+cycle[:1]))
            check_geometric_split(radius,cycle,sites,edges_of(sites),meshes[radius])
            geometries += 1
            remaining = {v for v in remaining if location(v,cycle) == -1}
        if (index+1)%40 == 0:
            print(f'geometry and random replay {index+1}/{len(rows)}',flush=True)
    small_rng = random.Random(617041)
    for _ in range(256):
        vertices = {v for v in ball(2) if norm(v)>=1 and small_rng.getrandbits(1)}
        assert bool(enclosing_candidates(vertices)) == brute_circuit_exists(vertices)
    # Compare the fresh sparse solver with dense Dirichlet on ten small graphs.
    for index in range(10):
        sites = set(ball(2))-{v for v in ball(2) if norm(v)==2 and (v[0]+2*v[1]+index)%3==0}
        edges = edges_of(sites); sink = [v for v in sites if norm(v)==2]
        r,_,_ = exact_sparse(edges,[(0,0)],sink)
        other,_,_ = exact_flow([(u,v,1) for u,v in edges],[(0,0)],sink)
        assert r == other
    # Audit all multiple-circuit R=12 samples, first three at R=24,
    # and the largest C/A among multiple-circuit cases at any radius.
    exact = []
    chosen24 = 0
    multi = [r for r in rows if int(r['circuits'])>=2]
    maximum_id = max(multi,key=lambda r:float(r['C_over_A']))['sample_id'] if multi else None
    for config,row in zip(configs,rows):
        if len(config['cycles']) < 2:
            continue
        radius = config['radius']
        if radius == 12 or (radius == 24 and chosen24<3) or config['sample_id'] == maximum_id:
            exact.append(exact_sample(config,row))
            chosen24 += int(radius == 24)
            print('exact multi-interface sample',config['sample_id'],flush=True)
    # Recompute all summary quantiles from saved CSV values.
    for summary in results['summary']:
        group = [r for r in rows if int(r['radius']) == summary['radius']]
        counts = Counter(int(r['circuits']) for r in group)
        assert summary['circuit_counts'] == {str(k):counts[k] for k in range(max(counts)+1)}
        for name,minimum in [('with_circuits',1),('multiple_circuits',2)]:
            subset = [r for r in group if int(r['circuits'])>=minimum]
            assert summary[name]['samples'] == len(subset)
            for key in ['C_over_A','R_over_A','D_over_C']:
                vals = sorted(float(r[key]) for r in subset if r[key])
                n = len(vals)
                stats = dict(min=vals[0],max=vals[-1],median=(vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2)) if vals else None
                assert summary[name][key] == stats
    scale_counts = defaultdict(Counter)
    for detail in details:
        radius = int(detail['sample_id'].split('-')[0])
        lo,hi = int(detail['min_radius']),int(detail['max_radius'])
        scale_counts[radius][f'{2**(lo.bit_length()-1)}-{2**lo.bit_length()-1}'] += 1
        assert abs(float(detail['variance'])*int(detail['length'])-float(detail['Q'])) < 1e-9
        assert 0 <= float(detail['TV']) <= 1+1e-9
    out = dict(samples=len(rows),random_replay=True,dual_existence_checks=checks,
               dual_circuit_splits=geometries,brute_force_annuli=256,
               sparse_vs_dense_exact_checks=10,exact_multi_interface_samples=exact,
               min_radius_dyadic_bins={r:dict(v) for r,v in scale_counts.items()},
               effective_nice=os.getpriority(os.PRIO_PROCESS,0),
               peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               elapsed_seconds=time.monotonic()-start)
    assert out['peak_RSS_bytes'] < 1024**3
    Path(prefix+'_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exact_multi_interface_samples'},indent=2),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('prefix'); args = parser.parse_args()
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100)); signal.alarm(1180)
    main(args.prefix)
