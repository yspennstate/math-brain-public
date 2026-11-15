"""Independent finite-grid referee experiments; no submitted code is imported.

Sites have equal mass h**d and centres quota alpha/h**d. Euclidean distances
give strict preferences (checked). Both directions of deferred acceptance are
implemented separately. Verification enumerates every possible blocking pair.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import collections
import csv
import heapq
import json
import pathlib
import resource
import time
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'data'

def site_proposing(cost, quota):
    ns, nc = cost.shape
    preferences = np.argsort(cost, axis=1)
    next_choice = np.zeros(ns, dtype=np.int64)
    assignment = np.full(ns, -1, dtype=np.int64)
    held = [[] for _ in range(nc)]
    free = collections.deque(range(ns))
    proposals = 0
    while free:
        site = free.popleft()
        if next_choice[site] == nc:
            continue
        centre = int(preferences[site, next_choice[site]])
        next_choice[site] += 1
        proposals += 1
        heap = held[centre]
        pair = (-float(cost[site, centre]), -site)
        if len(heap) < quota[centre]:
            heapq.heappush(heap, pair)
            assignment[site] = centre
        elif pair > heap[0]:
            _, evicted_negative = heapq.heapreplace(heap, pair)
            evicted = -evicted_negative
            assignment[evicted] = -1
            free.append(evicted)
            assignment[site] = centre
        else:
            free.append(site)
    return assignment, proposals

def centre_proposing(cost, quota):
    ns, nc = cost.shape
    preferences = np.argsort(cost, axis=0)
    next_choice = np.zeros(nc, dtype=np.int64)
    counts = np.zeros(nc, dtype=np.int64)
    assignment = np.full(ns, -1, dtype=np.int64)
    free = collections.deque(range(nc))
    proposals = 0
    while free:
        centre = free.popleft()
        while counts[centre] < quota[centre] and next_choice[centre] < ns:
            site = int(preferences[next_choice[centre], centre])
            next_choice[centre] += 1
            proposals += 1
            old = int(assignment[site])
            if old == -1 or cost[site, centre] < cost[site, old]:
                assignment[site] = centre
                counts[centre] += 1
                if old != -1:
                    was_full = counts[old] == quota[old]
                    counts[old] -= 1
                    if was_full:
                        free.append(old)
    return assignment, proposals

def verify(cost, assignment, quota):
    ns, nc = cost.shape
    counts = np.bincount(assignment[assignment >= 0], minlength=nc)
    assert np.all(counts <= quota)
    current = np.full(ns, np.inf)
    claimed = assignment >= 0
    current[claimed] = cost[np.flatnonzero(claimed), assignment[claimed]]
    blocking = 0
    for centre in range(nc):
        worst = np.inf if counts[centre] < quota[centre] else np.max(cost[assignment == centre, centre])
        blocking += int(np.count_nonzero((cost[:, centre] < current) & (cost[:, centre] < worst)))
    assert blocking == 0, blocking
    return int(np.sum(claimed)), blocking

def clusters(d, layers):
    # Nested prefixes of an infinite locally finite configuration with N(r)=Theta(r^3).
    centres = [np.array([.137*np.sqrt(2)] if d == 1 else [.137*np.sqrt(2), -.193*np.sqrt(3)])]
    for layer in range(1, layers+1):
        rng = np.random.default_rng(1000*d + layer)
        for direction in range(2*d):
            anchor = np.zeros(d)
            anchor[direction//2] = (-1 if direction % 2 else 1)*layer
            for _ in range(layer**2):
                centres.append(anchor + rng.uniform(-.035, .035, size=d) + np.sqrt(np.arange(2, d+2))*.001)
    return np.array(centres)

def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    OUT.mkdir(exist_ok=True)
    # Random shared-cost controls test quota handling and stability.
    rng = np.random.default_rng(83583)
    for trial in range(80):
        ns, nc = int(rng.integers(2, 35)), int(rng.integers(2, 15))
        cost = rng.random((ns, nc))
        quotas = rng.integers(1, 8, size=nc)
        s, _ = site_proposing(cost, quotas)
        c, _ = centre_proposing(cost, quotas)
        verify(cost, s, quotas)
        verify(cost, c, quotas)
        assert np.array_equal(s, c)
    records = []
    for d, layer_options, denominators in [(1, [4, 8, 12], [16, 32, 64]), (2, [3, 5, 7], [2, 4, 8])]:
        for denominator in denominators:
            previous_core = None
            for layers in layer_options:
                start = time.monotonic()
                half = layers + 1
                h = 1/denominator
                axis = (np.arange(2*half*denominator)+.5)*h-half
                sites = np.stack(np.meshgrid(*([axis]*d), indexing='ij'), axis=-1).reshape(-1,d)
                centres = clusters(d, layers)
                cost = np.zeros((len(sites), len(centres)))
                for coordinate in range(d):
                    cost += (sites[:, None, coordinate]-centres[None, :, coordinate])**2
                site_gap = float(np.min(np.diff(np.sort(cost, axis=1), axis=1)))
                centre_gap = float(np.min(np.diff(np.sort(cost, axis=0), axis=0)))
                assert site_gap > 1e-11 and centre_gap > 1e-11
                quotas = np.full(len(centres), denominator**d, dtype=np.int64)
                s, sp = site_proposing(cost, quotas)
                c, cp = centre_proposing(cost, quotas)
                claimed, bs = verify(cost, s, quotas)
                _, bc = verify(cost, c, quotas)
                core = np.all(np.abs(sites)<1, axis=1)
                core_changes = None if previous_core is None else int(np.count_nonzero(previous_core != s[core]))
                previous_core = s[core].copy()
                name = f'd{d}_n{layers}_h{denominator}'
                np.savetxt(OUT/(name+'_sites.csv'), np.column_stack([sites, s, c]), delimiter=',', header=','.join([f'x{i}' for i in range(d)]+['site_optimal','centre_optimal']), comments='', fmt='%.17g')
                np.savetxt(OUT/(name+'_centres.csv'), centres, delimiter=',', header=','.join([f'x{i}' for i in range(d)]), comments='', fmt='%.17g')
                record = dict(name=name, dimension=d, layers=layers, h=h, alpha=1, centres=len(centres), sites=len(sites), claimed=claimed, disagreement=int(np.count_nonzero(s!=c)), disagreement_volume=float(np.count_nonzero(s!=c)*h**d), core_changes=core_changes, site_proposals=sp, centre_proposals=cp, blocking_site=bs, blocking_centre=bc, min_site_gap=site_gap, min_centre_gap=centre_gap, seconds=time.monotonic()-start)
                print(json.dumps(record), flush=True)
                records.append(record)
                del cost
    metadata = dict(records=records, random_controls=80, nice=os.getpriority(os.PRIO_PROCESS, 0), thread_limit=1, peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (OUT/'independent_grid_results.json').write_text(json.dumps(metadata, indent=2)+'\n')
    with (OUT/'independent_grid_results.csv').open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

if __name__ == '__main__':
    main()
