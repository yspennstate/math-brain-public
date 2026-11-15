#!/usr/bin/env python3
"""Independent exact audit of the preceding circuit result."""
from fractions import Fraction as F
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import time


def solve(a, b):
    a = [[F(v) for v in row] + [F(z)] for row, z in zip(a, b)]
    for j in range(len(b)):
        k = next(k for k in range(j, len(b)) if a[k][j])
        a[j], a[k] = a[k], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for k in range(len(b)):
            if k != j and a[k][j]:
                scale = a[k][j]
                a[k] = [x - scale*y for x, y in zip(a[k], a[j])]
    return [row[-1] for row in a]


def exact_flow(edges, left, right):
    """Direct unit-voltage solve; zero-flow components are fixed separately."""
    left, right = set(left), set(right)
    adj = {v: set() for e in edges for v in e[:2]}
    for u, v, _ in edges:
        adj[u].add(v)
        adj[v].add(u)
    fixed = {v: F(v in left) for v in left | right}
    unseen = set(adj)
    while unseen:
        comp = {min(unseen)}
        todo = list(comp)
        while todo:
            for v in adj[todo.pop()] - comp:
                comp.add(v)
                todo.append(v)
        unseen -= comp
        if not comp & fixed.keys():
            fixed[min(comp)] = F(0)
    free = sorted(adj.keys() - fixed.keys())
    ix = {v: i for i, v in enumerate(free)}
    a = [[F(0) for _ in free] for _ in free]
    b = [F(0) for _ in free]
    for u, v, r in edges:
        for s, t in ((u, v), (v, u)):
            if s in ix:
                a[ix[s]][ix[s]] += 1/F(r)
                if t in ix:
                    a[ix[s]][ix[t]] -= 1/F(r)
                else:
                    b[ix[s]] += fixed[t]/F(r)
    pot = fixed | dict(zip(free, solve(a, b)))
    flow = [(pot[u]-pot[v])/r for u, v, r in edges]
    div = {v: F(0) for v in adj.keys() | left | right}
    for (u, v, _), z in zip(edges, flow):
        div[u] += z
        div[v] -= z
    total = sum(div[v] for v in left)
    assert total > 0
    return 1/total, [z/total for z in flow], {v: z/total for v,z in div.items()}


def cycle_cost(weights, demand):
    h = []
    acc = F(0)
    for z in demand:
        acc += z
        h.append(acc)
    assert acc == 0
    w = sum(weights)
    mean = sum(r*z for r,z in zip(weights,h))/w
    q = sum(r*(z-mean)**2 for r,z in zip(weights,h))
    other = sum(weights[i]*weights[j]*(h[i]-h[j])**2
                for i in range(len(h)) for j in range(i))/w
    assert q == other
    return q


def audit():
    start = time.monotonic()
    squares = equal = zero = 0
    for lm, rm, owners in product(range(1,16), range(1,16), product(range(2),repeat=4)):
        left = [(4,j,1) for j in range(4) if lm >> j & 1]
        right = [(j,5,1) for j in range(4) if rm >> j & 1]
        for j,owner in enumerate(owners):
            (left if owner == 0 else right).append((j,(j+1)%4,1))
        ra,fa,da = exact_flow(left,[4],range(4))
        rb,fb,db = exact_flow(right,range(4),[5])
        r,_,_ = exact_flow(left+right,[4],[5])
        delta = [-da.get(j,F(0))-db.get(j,F(0)) for j in range(4)]
        q = cycle_cost([1]*4,delta)
        assert 0 <= r-ra-rb <= q
        squares += 1
        equal += int(r-ra-rb == q)
        zero += int(r == ra+rb)
    assert (squares,equal,zero) == (3600,656,240)
    cycles = 0
    # Here verify the formula by solving potentials for arbitrary divergence,
    # independently of the unit-voltage square test.
    for n in range(3,8):
        for weights in ([1]*n,[1+j%3 for j in range(n)]):
            a = [[F(0) for _ in range(n-1)] for _ in range(n-1)]
            for j,r in enumerate(weights):
                u,v = j,(j+1)%n
                for s,t in ((u,v),(v,u)):
                    if s < n-1:
                        a[s][s] += 1/F(r)
                        if t < n-1:
                            a[s][t] -= 1/F(r)
            for h in product([-1,0,1],repeat=n):
                if sum(h):
                    continue
                v = solve(a,h[:-1])+[F(0)]
                q = sum((v[j]-v[(j+1)%n])**2/r for j,r in enumerate(weights))
                assert q == cycle_cost(weights,h)
                cycles += 1
    assert cycles == 1222
    # Weighted reduction of the two-circuit obstruction, independent of
    # the old subdivided-network solver.
    growth = []
    for length in [2,3,4,8,16]:
        edges = [(0,1,1),(1,2,length),(1,2,length),
                 (2,3,1),(3,4,length),(3,4,length),(4,5,1)]
        r,_,_ = exact_flow(edges,[0],[5])
        assert r == length+3
        growth.append({'L':length,'A':'3','R':str(r),'C':str(F(length))})
    old = json.loads(Path('~/codex_op_1114r4/briefs/T102/circuit_results.json').read_text())
    assert old['square_networks'] == squares
    assert old['square_equal_upper_bound'] == equal
    assert old['square_zero_correction'] == zero
    assert old['weighted_circuit_demand_cases'] == cycles
    out = dict(square_cases=squares, equality_cases=equal, zero_cases=zero,
               weighted_demand_cases=cycles, obstruction=growth,
               result='previous circuit result independently confirmed',
               effective_nice=os.getpriority(os.PRIO_PROCESS,0),
               peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               elapsed_seconds=time.monotonic()-start)
    assert out['peak_RSS_bytes'] < 1024**3
    Path('previous_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    signal.alarm(180)
    audit()
