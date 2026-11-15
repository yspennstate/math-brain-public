#!/usr/bin/env python3
"""Finite conditioned triangular percolation and circuit-current measurements.

Standard library only. All outputs are relative to this script's directory.
No infinite-IIC or asymptotic-exponent inference is made.
"""
import argparse
from collections import deque
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

ROOT = Path(__file__).resolve().parent
DIRS = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
DIR_INDEX = {v:i for i,v in enumerate(DIRS)}


def norm(v):
    a,b = v
    return max(abs(a),abs(b),abs(a+b))


def ball(radius):
    return [(a,b) for a in range(-radius,radius+1)
            for b in range(-radius,radius+1) if norm((a,b)) <= radius]


def edges_of(sites):
    return [(u,v) for u in sorted(sites) for da,db in DIRS
            if (v := (u[0]+da,u[1]+db)) in sites and u < v]


def connected_to_boundary(sites, radius):
    seen = {(0,0)}
    todo = [(0,0)]
    while todo:
        a,b = todo.pop()
        if norm((a,b)) == radius:
            return True
        for da,db in DIRS:
            v = (a+da,b+db)
            if v in sites and v not in seen:
                seen.add(v)
                todo.append(v)
    return False


def location(p, polygon):
    """-1 outside, 0 boundary, 1 inside; exact integer winding test."""
    winding = 0
    for u,v in zip(polygon,polygon[1:]+polygon[:1]):
        cross = (v[0]-u[0])*(p[1]-u[1])-(v[1]-u[1])*(p[0]-u[0])
        if cross == 0 and min(u[0],v[0]) <= p[0] <= max(u[0],v[0]) and min(u[1],v[1]) <= p[1] <= max(u[1],v[1]):
            return 0
        if u[1] <= p[1] < v[1] and cross > 0:
            winding += 1
        elif v[1] <= p[1] < u[1] and cross < 0:
            winding -= 1
    return 1 if winding else -1


def canonical(cycle):
    j = cycle.index(min(cycle))
    x = cycle[j:]+cycle[:j]
    return min(tuple(x),tuple([x[0]]+x[:0:-1]))


def select_circuit(sites, low, high):
    vertices = {v for v in sites if low <= norm(v) <= high}
    adj = {v:[] for v in vertices}
    for u,v in edges_of(vertices):
        adj[u].append(v)
        adj[v].append(u)
    for v in adj:
        adj[v].sort(key=lambda u: DIR_INDEX[(u[0]-v[0],u[1]-v[1])])
    unseen = {(u,v) for u in adj for v in adj[u]}
    candidates = set()
    while unseen:
        first = min(unseen)
        arc = first
        walk = []
        while True:
            assert arc in unseen
            unseen.remove(arc)
            u,v = arc
            walk.append(u)
            neighbors = adj[v]
            w = neighbors[(neighbors.index(u)-1) % len(neighbors)]
            arc = (v,w)
            if arc == first:
                break
        # Split repeated vertices, retaining simple closed subwalks only.
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
    return list(min(candidates,key=lambda c:(len(c),c))) if candidates else None


def divergence(edges, flow, extra=()):
    d = {v:0.0 for v in extra}
    for (u,v),f in zip(edges,flow):
        d[u] = d.get(u,0.0)+f
        d[v] = d.get(v,0.0)-f
    return d


def wired_flow(edges, left, right, tolerance=2e-12):
    """PCG plus spanning-tree residual repair and primal/dual bounds."""
    left,right = set(left),set(right)
    assert left and right and left.isdisjoint(right)
    def name(v):
        return -1 if v in left else -2 if v in right else v
    quotient = [(name(u),name(v)) for u,v in edges]
    adj = {-1:[],-2:[]}
    for u,v in quotient:
        if u != v:
            adj.setdefault(u,[]).append(v)
            adj.setdefault(v,[]).append(u)
    # Grounded tree includes all components touching either wired terminal;
    # other components have zero flow and remain in the physical edge list.
    parent = {-2:None}
    order = [-2]
    for u in order:
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                order.append(v)
    assert -1 in parent
    free = order[1:]
    ix = {v:i for i,v in enumerate(free)}
    neighbors = [[ix[v] for v in adj[u] if v != -2] for u in free]
    diag = [len(adj[u]) for u in free]
    def multiply(x):
        return [degree*x[i]-sum(x[j] for j in neighbors[i]) for i,degree in enumerate(diag)]
    rhs = [float(u == -1) for u in free]
    x = [0.0]*len(free)
    residual = rhs[:]
    z = [r/d for r,d in zip(residual,diag)]
    direction = z[:]
    rz = sum(r*t for r,t in zip(residual,z))
    for iteration in range(1, max(100,8*len(free))+1):
        ad = multiply(direction)
        alpha = rz/sum(p*q for p,q in zip(direction,ad))
        x = [v+alpha*p for v,p in zip(x,direction)]
        residual = [r-alpha*q for r,q in zip(residual,ad)]
        if max(map(abs,residual),default=0.0) <= tolerance:
            break
        z = [r/d for r,d in zip(residual,diag)]
        new_rz = sum(r*t for r,t in zip(residual,z))
        beta = new_rz/rz
        direction = [s+beta*p for s,p in zip(z,direction)]
        rz = new_rz
    else:
        raise AssertionError('PCG did not converge')
    potential = {-2:0.0} | dict(zip(free,x))
    gradient = [potential.get(u,0.0)-potential.get(v,0.0) for u,v in quotient]
    div = divergence(quotient,gradient,order)
    defect = {u:float(u == -1)-float(u == -2)-div[u] for u in order}
    corrections = {}
    for u in reversed(free):
        p = parent[u]
        q = defect[u]
        corrections[u,p] = q
        defect[p] += q
    repaired = [f+corrections.get((u,v),0.0)-corrections.get((v,u),0.0)
                for (u,v),f in zip(quotient,gradient)]
    # Quotient can have parallel physical edges. Put the tree correction on
    # one such edge, rather than counting it once per parallel edge.
    used = set()
    for j,(u,v) in enumerate(quotient):
        key = frozenset((u,v))
        if (u,v) in corrections or (v,u) in corrections:
            if key in used:
                repaired[j] = gradient[j]
            else:
                used.add(key)
    div_q = divergence(quotient,repaired,order)
    conservation = max(abs(div_q[u]-float(u == -1)+float(u == -2)) for u in order)
    eg = math.fsum(f*f for f in gradient)
    upper = math.fsum(f*f for f in repaired)
    lower = potential[-1]**2/eg
    # Floating evaluations of the two certificates may cross by roundoff.
    slack = 5e-12*max(1.0,upper)
    assert lower <= upper+slack
    assert conservation < 2e-9
    assert upper-lower < 1e-7*upper
    return dict(flow=repaired, lower=lower, upper=upper,
                gap=max(0.0,upper-lower), iterations=iteration,
                conservation=conservation)


def decompose(sites, edges, cycles, radius):
    doubled = [[(2*a,2*b) for a,b in cycle] for cycle in cycles]
    pieces = [[] for _ in range(len(cycles)+1)]
    vertex_sets = [set() for _ in pieces]
    for v in sites:
        p = (2*v[0],2*v[1])
        j = sum(location(p,c) == -1 for c in doubled)
        vertex_sets[j].add(v)
    for u,v in edges:
        midpoint = (u[0]+v[0],u[1]+v[1])
        j = sum(location(midpoint,c) == -1 for c in doubled)
        pieces[j].append((u,v))
        vertex_sets[j].update((u,v))
    boundaries = [[(0,0)]]+cycles+[[v for v in sorted(sites) if norm(v) == radius]]
    for j in range(len(pieces)):
        vertex_sets[j].update(boundaries[j]+boundaries[j+1])
    for j,cycle in enumerate(cycles):
        assert all(location(v,cycles[j+1]) == 1 for v in cycle) if j+1 < len(cycles) else True
    for i in range(len(pieces)):
        for j in range(i):
            expected = set(boundaries[i]) if i == j+1 else set()
            assert vertex_sets[i] & vertex_sets[j] == expected
    assert set.union(*vertex_sets) == sites
    assert sum(map(len,pieces)) == len(edges)
    return pieces,boundaries,vertex_sets


def circuit_cost(demand):
    cumulative,acc = [],0.0
    for value in demand:
        acc += value
        cumulative.append(acc)
    assert abs(acc) < 1e-8
    # Remove the tiny total-divergence roundoff at the final coordinate.
    mean = math.fsum(cumulative)/len(cumulative)
    flow = [z-mean for z in cumulative]
    q = math.fsum(f*f for f in flow)
    pairwise = math.fsum((x-y)**2 for i,x in enumerate(cumulative) for y in cumulative[:i])/len(cumulative)
    assert abs(q-pairwise) < 2e-10*max(1.0,q)
    tv = math.fsum(abs(z) for z in demand)/2
    coarse = len(demand)*tv*tv/4
    assert q <= coarse+1e-8
    return dict(Q=q, TV=tv, variance=q/len(demand),
                coarse=coarse, repair=flow, total_defect=acc)


def measure(sites, cycles, radius):
    edges = edges_of(sites)
    pieces,boundaries,vertex_sets = decompose(sites,edges,cycles,radius)
    local = [wired_flow(e,l,r) for e,l,r in zip(pieces,boundaries,boundaries[1:])]
    full = wired_flow(edges,boundaries[0],boundaries[-1])
    a = math.fsum(s['upper'] for s in local)
    a_lower = math.fsum(s['lower'] for s in local)
    circuit_rows,repairs = [],{}
    for j,cycle in enumerate(cycles):
        da = divergence(pieces[j],local[j]['flow'],cycle)
        db = divergence(pieces[j+1],local[j+1]['flow'],cycle)
        delta = [-da[v]-db[v] for v in cycle]
        result = circuit_cost(delta)
        for u,v,f in zip(cycle,cycle[1:]+cycle[:1],result.pop('repair')):
            repairs[u,v] = f
        circuit_rows.append(dict(length=len(cycle),min_radius=min(map(norm,cycle)),
                                 max_radius=max(map(norm,cycle)),**result))
    c = math.fsum(row['Q'] for row in circuit_rows)
    coarse = math.fsum(row['coarse'] for row in circuit_rows)
    all_piece_edges = sum(pieces,[])
    candidate = []
    for e,s in zip(pieces,local):
        for (u,v),f in zip(e,s['flow']):
            repair = repairs.get((u,v),-repairs.get((v,u),0.0))
            if (u,v) in repairs or (v,u) in repairs:
                assert f == 0.0
            candidate.append(f+repair)
    energy = math.fsum(f*f for f in candidate)
    div = divergence(all_piece_edges,candidate,sites)
    sink = set(boundaries[-1])
    defect = max(abs(z-float(v == (0,0))) for v,z in div.items() if v not in sink)
    assert defect < 2e-8
    assert abs(math.fsum(div[v] for v in sink)+1) < 2e-8
    assert abs(energy-(a+c)) < 2e-10*max(1.0,energy)
    assert a_lower <= full['upper']+1e-8
    assert full['lower'] <= a+c+1e-8
    r = (full['lower']+full['upper'])/2
    row = dict(radius=radius,vertices=len(sites),edges=len(edges),circuits=len(cycles),
               A=a,A_lower=a_lower,R=r,R_lower=full['lower'],R_upper=full['upper'],
               D=r-a,C=c,coarse=coarse,R_over_A=r/a,C_over_A=c/a,
               D_over_C=(r-a)/c if c > 1e-20 else None,
               max_solve_relative_gap=max(s['gap']/s['upper'] for s in local+[full]),
               max_conservation_error=max(defect,*(s['conservation'] for s in local+[full])),
               max_iterations=max(s['iterations'] for s in local+[full]),
               max_layer_components=max(component_count(e,vs) for e,vs in zip(pieces,vertex_sets)))
    return row,circuit_rows


def component_count(edges, vertices):
    parent = {v:v for v in vertices}
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u,v in edges:
        parent[root(u)] = root(v)
    return len({root(v) for v in vertices})


def self_test():
    from fractions import Fraction
    from recheck_previous import exact_flow,cycle_cost
    # All 64 site masks of the first ring: an enclosing circuit requires all 6.
    ring = [v for v in ball(1) if norm(v) == 1]
    found = 0
    for mask in range(64):
        sites = {v for j,v in enumerate(ring) if mask >> j & 1}
        cycle = select_circuit(sites,1,1)
        assert bool(cycle) == (mask == 63)
        found += bool(cycle)
    sites = set(ball(8))
    cycles = [select_circuit(sites,2,3),select_circuit(sites,4,6)]
    assert list(map(len,cycles)) == [12,24]
    row,details = measure(sites,cycles,8)
    rng = random.Random(11701)
    checked = 0
    while checked < 10:
        sites = {v for v in ball(3) if v == (0,0) or rng.getrandbits(1)}
        if not connected_to_boundary(sites,3):
            continue
        edges = edges_of(sites)
        right = [v for v in sites if norm(v) == 3]
        exact,_,_ = exact_flow([(u,v,1) for u,v in edges],[(0,0)],right)
        s = wired_flow(edges,[(0,0)],right)
        assert s['lower']-1e-10 <= float(exact) <= s['upper']+1e-10
        checked += 1
    # Demand indexing is checked over the rationals as well.
    h = [Fraction(1,3),Fraction(-1,2),Fraction(1,6),Fraction(0)]
    assert abs(circuit_cost(list(map(float,h)))['Q']-float(cycle_cost([1]*4,h))) < 1e-15
    return dict(ring_masks=64,enclosing_masks=found,fully_open_lengths=[12,24],
                exact_rational_resistance_checks=checked,fully_open_measurement=row)


def aggregate(rows):
    result = []
    for radius in sorted({r['radius'] for r in rows}):
        group = [r for r in rows if r['radius'] == radius]
        active = [r for r in group if r['circuits'] > 0]
        two = [r for r in group if r['circuits'] == 2]
        item = dict(radius=radius,samples=len(group),
                    circuit_counts=[sum(r['circuits'] == k for r in group) for k in range(3)])
        for name,subset in [('with_circuits',active),('two_circuits',two)]:
            item[name] = {key:dict(min=min(r[key] for r in subset),
                                  median=statistics.median(r[key] for r in subset),
                                  max=max(r[key] for r in subset))
                          for key in ['R_over_A','C_over_A','D_over_C']} if subset else {}
        result.append(item)
    return result


def run(samples, radii, seed, replay=None, thin=False):
    start = time.monotonic()
    checks = self_test()
    print('Self-tests passed.',flush=True)
    rng = random.Random(seed)
    saved = iter(json.loads(line) for line in Path(replay).read_text().splitlines()) if replay else None
    rows,circuit_rows,attempts = [],[],{}
    config_path = ROOT/'configurations.jsonl'
    with config_path.open('w') as configs, (ROOT/'samples.csv').open('w',newline='') as sf, (ROOT/'circuits.csv').open('w',newline='') as cf:
        sw = cw = None
        for radius in radii:
            vertices = ball(radius)
            annuli = ([(max(2,radius//8),radius//4),(radius//2,5*radius//6)] if thin
                      else [(1,radius//4),(radius//4+1,radius-1)])
            count = proposals = 0
            while count < samples:
                if saved is None:
                    proposals += 1
                    assert proposals < 100000
                    sites = {v for v in vertices if v == (0,0) or rng.getrandbits(1)}
                    if not connected_to_boundary(sites,radius):
                        continue
                else:
                    record = next(saved)
                    assert record['radius'] == radius
                    proposals = record['proposal']
                    sites = set(map(tuple,record['open_sites']))
                    assert connected_to_boundary(sites,radius)
                selected = [select_circuit(sites,lo,hi) for lo,hi in annuli]
                cycles = [cycle for cycle in selected if cycle]
                sample_id = f'{radius}-{count:03}'
                config = dict(sample_id=sample_id,radius=radius,proposal=proposals,
                              annuli=annuli,open_sites=sorted(sites),selected_cycles=selected)
                configs.write(json.dumps(config,separators=(',',':'))+'\n')
                configs.flush()
                row,details = measure(sites,cycles,radius)
                row = dict(sample_id=sample_id,proposal=proposals,**row)
                if sw is None:
                    sw = csv.DictWriter(sf,fieldnames=list(row))
                    sw.writeheader()
                sw.writerow(row)
                sf.flush()
                rows.append(row)
                for j,detail in enumerate(details):
                    detail = dict(sample_id=sample_id,circuit_index=j,**detail)
                    if cw is None:
                        cw = csv.DictWriter(cf,fieldnames=list(detail))
                        cw.writeheader()
                    cw.writerow(detail)
                    circuit_rows.append(detail)
                cf.flush()
                count += 1
                if count % 10 == 0:
                    print(f'R={radius}: {count}/{samples} accepted, {proposals} proposals, {time.monotonic()-start:.1f}s',flush=True)
            attempts[radius] = proposals
    if saved is not None:
        assert next(saved,None) is None
    output = dict(seed=seed,per_radius=samples,radii=radii,proposals=attempts,
                  replay_source=replay,annulus_rule='thin' if thin else 'wide',
                  self_tests=checks,summary=aggregate(rows),
                  circuit_count=len(circuit_rows),
                  max_relative_solve_gap=max(r['max_solve_relative_gap'] for r in rows),
                  max_conservation_error=max(r['max_conservation_error'] for r in rows),
                  max_iterations=max(r['max_iterations'] for r in rows),
                  effective_nice=os.getpriority(os.PRIO_PROCESS,0),
                  peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  elapsed_seconds=time.monotonic()-start)
    assert output['peak_RSS_bytes'] < 1024**3
    (ROOT/'sample_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples',type=int,default=40)
    parser.add_argument('--radii',type=int,nargs='+',default=[12,24,48])
    parser.add_argument('--seed',type=int,default=202611150821)
    parser.add_argument('--replay')
    parser.add_argument('--thin',action='store_true')
    args = parser.parse_args()
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(1100,1100))
    signal.alarm(1180)
    run(args.samples,args.radii,args.seed,args.replay,args.thin)
