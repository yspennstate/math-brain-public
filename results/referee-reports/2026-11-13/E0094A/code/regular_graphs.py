"""Enumerate unlabelled regular graphs with nauty; optimize every nonedge/matching.

All optimizations are exhaustive. Eigenvalues are double precision, not exact
algebraic certificates. The report separately certifies a counterexample in Q[x].
"""
import os
for name in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
             'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']:
    os.environ[name] = '1'
import csv
import itertools
import json
from pathlib import Path
import subprocess
import networkx as nx
import numpy as np
from scipy.linalg import eigh
from exact_spectra import certify_optimizer

GENG = Path('sources/nauty2_8_9/geng')


def gap(a, normalized=True):
    d = a.sum(axis=1)
    lap = np.diag(d) - a
    return float(eigh(lap, np.diag(d) if normalized else None,
                      subset_by_index=[1, 1], eigvals_only=True)[0])


def matchings(vertices, a):
    if not vertices:
        yield []
        return
    u = vertices[0]
    for k, v in enumerate(vertices[1:], start=1):
        if not a[u, v]:
            for rest in matchings(vertices[1:k]+vertices[k+1:], a):
                yield [(u, v)] + rest


def main():
    fields = ['n', 'd', 'index', 'graph6', 'gap', 'multiplicity',
              'nonedges', 'best_edge', 'best_gap', 'worst_gap',
              'extremal_pairs', 'extremal_best_gap', 'fiedler_heuristic_fails',
              'matchings', 'best_matching', 'best_matching_gap']
    counts = []
    counterexamples = []
    certificates = []
    with open('data/regular_graphs.csv', 'w') as out:
        writer = csv.DictWriter(out, fields)
        writer.writeheader()
        for n in [2, 4, 6, 8, 10]:
            for d in range(1, n):
                if d == 1 and n > 2:
                    continue
                if n*d % 2:
                    continue
                run = subprocess.run([str(GENG), '-cq', f'-d{d}', f'-D{d}', str(n)],
                                     capture_output=True, check=True)
                lines = run.stdout.splitlines()
                if not lines:
                    continue
                Path(f'data/regular_n{n}_d{d}.g6').write_bytes(run.stdout)
                failures = 0
                for idx, line in enumerate(lines):
                    g = nx.from_graph6_bytes(line)
                    a = nx.to_numpy_array(g)
                    vals, vecs = eigh(np.diag(a.sum(axis=1))-a)
                    g0 = vals[1]/d
                    mult = int(np.sum(np.abs(vals-vals[1]) < 1e-8))
                    f = vecs[:, 1]
                    pairs = list(nx.non_edges(g))
                    edgevals = []
                    edge_candidates = []
                    for u, v in pairs:
                        b = a.copy(); b[u, v] = b[v, u] = 1
                        edgevals.append(gap(b))
                        edge_candidates.append(([u,v], b.astype(int).tolist(), edgevals[-1]))
                    best = max(edgevals, default=float('nan'))
                    bi = int(np.argmax(edgevals)) if edgevals else None
                    extrema = [(u, v) for u, v in pairs
                               if (abs(f[u]-f.min()) < 1e-8 and abs(f[v]-f.max()) < 1e-8)
                               or (abs(f[v]-f.min()) < 1e-8 and abs(f[u]-f.max()) < 1e-8)]
                    heurbest = max((edgevals[pairs.index(e)] for e in extrema), default=float('nan'))
                    failure = mult == 1 and extrema and heurbest < best - 1e-8
                    failures += int(bool(failure))
                    if failure:
                        counterexamples.append(dict(n=n, d=d, graph6=line.decode(), index=idx,
                            edges=sorted(g.edges()), f=f.tolist(), original_gap=g0,
                            best_edge=pairs[bi], best_gap=best, extrema=extrema,
                            heuristic_gap=heurbest, lap_eigenvalues=vals.tolist(),
                            all_edges=[dict(edge=e, gap=x) for e, x in zip(pairs,edgevals)]))
                    bestm, bestmg, nm = None, -1.0, 0
                    matching_candidates = []
                    for matching in matchings(list(range(n)), a):
                        nm += 1
                        b = a.copy()
                        for u, v in matching:
                            b[u, v] = b[v, u] = 1
                        z = gap(b)
                        matching_candidates.append((matching,b.astype(int).tolist(),z))
                        if z > bestmg + 1e-12:
                            bestm, bestmg = matching, z
                    cert = dict(n=n,d=d,index=idx,graph6=line.decode())
                    if edge_candidates:
                        brackets, opts = certify_optimizer(edge_candidates,bi)
                        cert['edges']=[dict(edge=e,bracket=br) for (e,_,_),br in zip(edge_candidates,brackets)]
                        cert['optimal_edges']=[edge_candidates[i][0] for i in opts]
                    if matching_candidates:
                        bmi=int(np.argmax([z for _,_,z in matching_candidates]))
                        brackets,opts=certify_optimizer(matching_candidates,bmi)
                        cert['matchings']=[dict(edges=e,bracket=br) for (e,_,_),br in zip(matching_candidates,brackets)]
                        cert['optimal_matchings']=[matching_candidates[i][0] for i in opts]
                    certificates.append(cert)
                    row = dict(n=n, d=d, index=idx, graph6=line.decode(), gap=g0,
                        multiplicity=mult, nonedges=len(pairs),
                        best_edge=pairs[bi] if bi is not None else None,
                        best_gap=best, worst_gap=min(edgevals,default=float('nan')),
                        extremal_pairs=extrema, extremal_best_gap=heurbest,
                        fiedler_heuristic_fails=bool(failure), matchings=nm,
                        best_matching=bestm, best_matching_gap=bestmg if nm else float('nan'))
                    writer.writerow(row)
                counts.append(dict(n=n,d=d,graphs=len(lines),simple_fiedler_failures=failures))
                out.flush()
                print(counts[-1],flush=True)
                Path('data/regular_exact_certificates.json').write_text(json.dumps(certificates,indent=2)+'\n')
    Path('data/regular_counts.json').write_text(json.dumps(counts, indent=2)+'\n')
    Path('data/fiedler_counterexamples.json').write_text(json.dumps(counterexamples,indent=2)+'\n')


if __name__ == '__main__':
    main()
