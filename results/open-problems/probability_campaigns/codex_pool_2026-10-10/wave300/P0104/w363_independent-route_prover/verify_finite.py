"""Bounded exact controls for L2/L3; never an asymptotic proof receipt."""
import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument('--gate-seconds', type=float, required=True)
parser.add_argument('--max-configurations', type=int, required=True)
args = parser.parse_args()
if not 0 < args.gate_seconds <= 60 or not 16 <= args.max_configurations <= 128:
    raise SystemExit('Fresh compute gate rejected: require <=60 seconds, <=128 configurations.')
start = time.monotonic()
deadline = start + args.gate_seconds
counts = {'variance_identities': 0, 'gradient_correlations': 0,
          'forcing_sandwiches': 0, 'energy_sandwiches': 0,
          'harmonic_identities': 0, 'negative_controls_rejected': 0}

def gate():
    if time.monotonic() > deadline:
        raise TimeoutError('Fresh compute gate expired')

def configurations(m):
    if 2 ** m > args.max_configurations:
        raise ValueError('Configuration budget exceeded')
    return list(product((0, 1), repeat=m))

def probability(x, p):
    return p ** sum(x) * (1-p) ** (len(x)-sum(x))

def simple_paths(edges, source, target):
    adjacency = {}
    for i, (u, v) in enumerate(edges):
        adjacency.setdefault(u, []).append((v, i))
        adjacency.setdefault(v, []).append((u, i))
    paths = []
    def visit(v, seen, path):
        if v == target:
            paths.append(tuple(path))
            return
        for w, i in adjacency[v]:
            if w not in seen:
                visit(w, seen | {w}, path + [i])
    visit(source, {source}, [])
    return sorted(paths)

def graph_controls(name, edges, source, target, p, direct_noise):
    gate()
    m = len(edges)
    xs = configurations(m)
    probs = {x: probability(x, p) for x in xs}
    paths = simple_paths(edges, source, target)
    chosen = {x: min(paths, key=lambda path: (sum(1+x[i] for i in path), path)) for x in xs}
    values = {x: F(sum(1+x[i] for i in chosen[x])) for x in xs}
    mean = sum(probs[x]*values[x] for x in xs)
    variance = sum(probs[x]*(values[x]-mean)**2 for x in xs)
    pq = p*(1-p)
    # Orthogonal centered product basis avoids irrational normalization.
    spectral = {}
    for mask in range(1, 1 << m):
        gate()
        subset = [i for i in range(m) if mask & (1 << i)]
        moment = F(0)
        for x in xs:
            basis = F(1)
            for i in subset:
                basis *= x[i]-p
            moment += probs[x]*values[x]*basis
        spectral[mask] = moment**2 / pq**len(subset)
    assert sum(spectral.values()) == variance
    counts['variance_identities'] += 1
    energy_spectral = sum(mask.bit_count()*v for mask, v in spectral.items())
    gradients = {}
    for i in range(m):
        zs = configurations(m-1)
        gradients[i] = {}
        for z in zs:
            gate()
            low = tuple(list(z[:i])+[0]+list(z[i:]))
            high = tuple(list(z[:i])+[1]+list(z[i:]))
            delta = values[high]-values[low]
            assert F(i in chosen[high]) <= delta <= F(i in chosen[low])
            counts['forcing_sandwiches'] += 1
            gradients[i][z] = delta
    energy_direct = pq * sum(probability(z, p)*d*d for g in gradients.values() for z,d in g.items())
    assert energy_direct == energy_spectral
    high_count = sum(probs[x]*sum(x[i] for i in chosen[x]) for x in xs)
    low_count = sum(probs[x]*sum(1-x[i] for i in chosen[x]) for x in xs)
    assert (1-p)*high_count <= energy_direct <= p*low_count
    counts['energy_sandwiches'] += 1
    if energy_direct:
        harmonic = sum(v/energy_direct for v in spectral.values())
        assert variance == energy_direct*harmonic
        counts['harmonic_identities'] += 1
    if direct_noise:
        for rho in [F(0), F(1,4), F(1,2), F(3,4), F(1)]:
            correlation = F(0)
            for gradient in gradients.values():
                for x, dx in gradient.items():
                    for y, dy in gradient.items():
                        gate()
                        if not dx or not dy:
                            continue
                        joint = F(1)
                        for u,v in zip(x,y):
                            pu = p if u else 1-p
                            pv = p if v else 1-p
                            joint *= pu * (rho*int(u == v)+(1-rho)*pv)
                        correlation += pq*joint*dx*dy
            expected = sum(mask.bit_count()*rho**(mask.bit_count()-1)*v for mask,v in spectral.items())
            assert correlation == expected
            counts['gradient_correlations'] += 1
    return {'model': name, 'p': str(p), 'configurations': len(xs),
            'variance': str(variance), 'energy': str(energy_direct),
            'variance_over_energy': str(variance/energy_direct)}

receipt = {'gate': {'wall_seconds': args.gate_seconds,
                    'max_configurations_per_model': args.max_configurations,
                    'local_cpu_only': True},
           'proof_scope': 'Exact finite rational arithmetic controls only; G1 unproved; no formal theorem checker.'}
try:
    diamond = [(0,1), (1,3), (0,2), (2,3)]
    models = [graph_controls('two-path-diamond', diamond, 0, 3, p, True)
              for p in [F(1,2), F(3,4), F(99,100)]]
    ladder = [(0,1), (1,2), (3,4), (4,5), (0,3), (1,4), (2,5)]
    if args.max_configurations >= 128:
        models.append(graph_controls('two-by-three-ladder', ladder, 0, 2, F(1,2), False))
    # Incorrect replacement of the integral by its endpoint must fail.
    assert F(models[0]['variance']) != F(models[0]['energy'])
    counts['negative_controls_rejected'] += 1
    # A typical spectral scale can coexist with dominant small-degree leakage.
    n = 4096
    epsilon = F(1,8)  # n^(-1/4)
    typical_k = 16  # n^(1/3)
    actual_harmonic = epsilon+(1-epsilon)/typical_k
    naive_harmonic = F(1, typical_k)
    assert actual_harmonic > naive_harmonic
    counts['negative_controls_rejected'] += 1
    # Establish the elementary constant in L4 without numerical square roots.
    assert 3**2 < 10  # r=3/(5 sqrt(10)) < 1/5
    assert F(4,3)*F(1,5)/(1-F(1,5)) == F(1,3)
    receipt.update(status='PASS', models=models, counts=counts,
                   endpoint_shortcut={'wrong': models[0]['energy'], 'actual': models[0]['variance']},
                   typical_scale_shortcut={'wrong': str(naive_harmonic), 'actual': str(actual_harmonic)})
except Exception as exc:
    receipt.update(status='FAIL', error=f'{type(exc).__name__}: {exc}', counts=counts)
receipt['elapsed_seconds'] = round(time.monotonic()-start, 6)
Path(__file__).with_name('MEASUREMENTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt, indent=2))
if receipt['status'] != 'PASS':
    raise SystemExit(1)
