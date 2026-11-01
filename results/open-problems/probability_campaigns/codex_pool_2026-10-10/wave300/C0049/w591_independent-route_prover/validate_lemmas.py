"""Bounded exact arithmetic controls; not a formal proof or a lattice-limit test."""
import datetime as dt
import itertools
import json
import math
import pathlib
import time
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parent
GATE = pathlib.Path(r'~/.claude/compute/compute_state.json')
start = time.perf_counter()
cpu_start = time.process_time()
state = json.loads(GATE.read_text(encoding='utf-8-sig'))
age = time.time() - GATE.stat().st_mtime
receipt = {k: state.get(k) for k in ('ts', 'status', 'mode', 'reasons', 'cpu_pct', 'mem_avail_mb', 'disk_free_gb')}
receipt['file_age_seconds'] = age
receipt['operation'] = 'single-process standard-library exact arithmetic, at most 2 CPU seconds; no GPU/network'
allowed = (-5 <= age <= 90 and state.get('status') in ('ok', 'warn')
           and float(state.get('mem_avail_mb', 0)) >= 512
           and float(state.get('cpu_pct', 100)) <= 85
           and float(state.get('disk_free_gb', 0)) >= 1)
receipt['decision'] = 'RUN' if allowed else 'DEFER'
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
if not allowed:
    print(json.dumps(receipt))
    raise SystemExit(75)

counts = {'edge_conditionals': 0, 'restricted_fusion_ratios': 0,
          'q1_derivative_histories': 0, 'generator_and_coefficient_pairs': 0,
          'one_observable_false_variances_accepted': 0,
          'two_observable_false_variances_rejected': 0}

def budget():
    if time.process_time()-cpu_start > 2:
        raise RuntimeError('2 CPU-second compute budget reached; no gate weakening')

def clusters(n, edges, bits, ident=()):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    def union(a, b):
        parent[find(a)] = find(b)
    for a, b in ident:
        union(a, b)
    for (a, b), opened in zip(edges, bits):
        if opened:
            union(a, b)
    roots = [find(v) for v in range(n)]
    return len(set(roots)), roots

def weight(n, edges, bits, p, q, ident=()):
    k, _ = clusters(n, edges, bits, ident)
    opened = sum(bits)
    return p**opened*(1-p)**(len(edges)-opened)*q**k

graphs = [(3, [(0,1),(1,2),(0,2)]),
          (4, [(0,1),(1,2),(2,3),(3,0)]),
          (4, [(0,1),(1,2),(2,0),(2,3)])]
q_values = [F(1,2), F(1), F(2), F(3), F(4)]
p_values = [F(1,3), F(1,2), F(2,3)]
for n, edges in graphs:
    m = len(edges)
    for ident in ((), ((0,1),)):
        fused = ident+((0,n-1),)
        for p in p_values:
            for q in q_values:
                budget()
                for e_index, (a,b) in enumerate(edges):
                    for other in itertools.product((0,1), repeat=m-1):
                        bits = list(other)
                        bits.insert(e_index, 0)
                        closed = tuple(bits)
                        bits[e_index] = 1
                        opened = tuple(bits)
                        _, roots = clusters(n, edges, closed, ident)
                        expected = p if roots[a] == roots[b] else p/(p+q*(1-p))
                        wc = weight(n,edges,closed,p,q,ident)
                        wo = weight(n,edges,opened,p,q,ident)
                        assert wo/(wc+wo) == expected
                        counts['edge_conditionals'] += 1
                for length in range(m+1):
                    for prefix in itertools.product((0,1), repeat=length):
                        z = zf = za = F(0)
                        z1 = zf1 = dz1 = dzf1 = za1 = F(0)
                        for suffix in itertools.product((0,1), repeat=m-length):
                            bits = prefix+suffix
                            k, roots = clusters(n,edges,bits,ident)
                            kf, _ = clusters(n,edges,bits,fused)
                            base = p**sum(bits)*(1-p)**(m-sum(bits))
                            connected = roots[0] == roots[n-1]
                            z += base*q**k
                            zf += base*q**kf
                            za += connected*base*q**k
                            if q == 1:
                                z1 += base
                                zf1 += base
                                dz1 += base*k
                                dzf1 += base*kf
                                za1 += connected*base
                        ratio = zf/z
                        assert ratio == 1/q+(1-1/q)*(za/z)
                        if q != 1:
                            assert (q*ratio-1)/(q-1) == za/z
                        counts['restricted_fusion_ratios'] += 1
                        if q == 1:
                            assert ratio == 1
                            derivative = (dzf1*z1-zf1*dz1)/(z1*z1)
                            assert 1+derivative == za1/z1
                            counts['q1_derivative_histories'] += 1

# Check the exact differential coefficients independently of simulating an SDE.
for kappa in [F(4), F(16,3), F(6), F(7), F(15,2)]:
    for u in [F(1,5), F(2,5), F(3,5), F(4,5)]:
        ell = -4/(kappa*u)+(2-8/kappa)/(1-u)
        drift = 2/u+(kappa-2)*u-kappa
        assert kappa*(1-u)**2*ell/2+drift == 0
        c = 1+(u-1)*ell/2
        assert c == 2*(1+1/u)/kappa
        counts['generator_and_coefficient_pairs'] += 1
    u1, u2, y = F(1,3), F(2,3), F(2)
    c1, c2 = 2*(1+1/u1)/kappa, 2*(1+1/u2)/kappa
    assert y*(c2-c1) != 0
    nu = kappa/2+1
    assert nu != kappa
    a = -2*(nu-kappa)*(1+1/u1)/(kappa*y)
    assert y*a+c1*(nu-kappa) == 0
    counts['one_observable_false_variances_accepted'] += 1
    assert y*a+c2*(nu-kappa) != 0
    counts['two_observable_false_variances_rejected'] += 1

# Non-tautological controls against two tempting but false finite-graph shortcuts.
n, edges = graphs[0]
states = list(itertools.product((0,1), repeat=3))
weights = [weight(n,edges,b,F(1,2),F(2)) for b in states]
total = sum(weights)
actual_edge = sum(w for b,w in zip(states,weights) if b[0])/total
naive_partial = F(1,3)
actual_all = weight(n,edges,(1,1,1),F(1,2),F(2))/total
assert actual_edge == F(5,14) and actual_edge != naive_partial
assert actual_all == F(1,14) and actual_all != actual_edge**3
arc_ratio = F(2)**1/F(2)**4
assert arc_ratio == F(1,8) and arc_ratio != F(1,2)
budget()
result = {'passed': True, 'time_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
          'counts': counts, 'wall_seconds': time.perf_counter()-start,
          'cpu_seconds': time.process_time()-cpu_start,
          'negative_controls': {'partial_edge_actual':str(actual_edge),
                                'partial_edge_naive':str(naive_partial),
                                'all_edges_actual':str(actual_all),
                                'all_edges_independent_guess':str(actual_edge**3),
                                'four_vertex_arc_fusion_actual':str(arc_ratio),
                                'incorrect_two_class_guess':'1/2'},
          'scope':'exact finite and algebraic checks only; no continuum proof, independent audit, formal kernel check, or measured live-brain improvement'}
(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
