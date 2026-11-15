"""Insert the saved simulation results into REPORT.md, without rerunning them."""
from pathlib import Path
import csv,json,statistics
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'REPORT.md';text=p.read_text()
with (ROOT/'data/summary.csv').open() as f: rows=list(csv.DictReader(f))
meta=json.loads((ROOT/'data/run_metadata.json').read_text())
obs=[json.loads(s) for s in (ROOT/'data/observations.jsonl').read_text().splitlines()]
section='''## 5. Computation (evidence only)

The final run used 16 independent nested Poisson realizations per dimension, with expected sample sizes 1,024, 4,096, 16,384 and 65,536. This is 48 independent realizations and 384 finite MSTs, because the four sizes are nested and the two boundary conditions are paired. The actual maximum sample count was MAXN. Points have intensity one; the side lengths at the largest scale are 40.3175, 16 and 9.1896 for d=3,4,5. Thus “65,536 points” in d=5 still gives a spatially modest box.

**Exact finite MST calculation.** Candidate edges are all pairs within a radius, found by cKDTree. Kruskal's algorithm (SciPy sparse MST) is run on this graph; the radius is enlarged if the graph is disconnected. Every accepted tree has n−1 edges and maximum edge length strictly below the candidate radius. Every omitted complete-metric edge is at least that radius, so it cannot improve the tree, by the cycle/cut property. This certifies the *complete* Euclidean MST for free boundaries and the complete minimum-image torus MST for periodic boundaries; it is not an uncertified k-nearest-neighbor approximation. The distance-to-exterior wired forest of Proposition E is also computed for each free box.

**Observables.** The whole finite MST connects every pair, and this tautological check passed in all 384 cases. The nontrivial primary statistic selects 64 distinct random pairs in the central cube of side L/2, each with Euclidean separation at least L/3, and tests connection after restricting the MST to that cube. The same pairs are used for free and periodic boundaries. These are deliberately far-apart *moving* pairs. Their separation and window both grow with L, so these statistics do not estimate the iterated fixed-root limit (4.2).

Separately, in each smallest box a maximally separated pair among its central-cube points is chosen once and held fixed across the four nested boxes. Its connection is recorded within the fixed inner cube of side 0.75 L_min, as well as in the wired certificate using the whole growing box. The root coordinates are recorded, and this selection from the smallest sample is dependent on that sample. No Palm or unbiased-pair interpretation is attached to it.

The following entries are mean fractions of far pairs connected in the central cube. The bounds are approximate 95% Student-t intervals calculated over the 16 **replicate fractions**. They are descriptive intervals, not rigorous confidence bounds or intervals based on treating the 1,024 pairs as independent.

| d | Expected n | Free interior connection fraction (interval) | Periodic interior connection fraction (interval) |
|---|---:|---:|---:|
'''
for d in (3,4,5):
 for n in (1024,4096,16384,65536):
  entries=[]
  for bc in ('free','periodic'):
   r=next(r for r in rows if int(r['d'])==d and int(r['expected_n'])==n and r['boundary']==bc)
   entries.append(f"{float(r['mean_far_core_fraction']):.4f} ({float(r['replicate_t95_low']):.4f}–{float(r['replicate_t95_high']):.4f})")
  section+=f'| {d} | {n:,} | {entries[0]} | {entries[1]} |\n'
section+='''
At the largest scale, the wired whole-box certificate connected the fixed pair in the following numbers of realizations. A success proves connection in the corresponding infinite Poisson forest under the exact-arithmetic model; a failure does not prove disconnection. Floating-point arithmetic is used in the actual numerical implementation.

| d | Fixed-pair wired successes, as expected n grows 1,024 → 4,096 → 16,384 → 65,536 | Final far-pair fraction connected in whole-box wired certificate |
|---|---|---:|
'''
for d in (3,4,5):
 group=[next(r for r in rows if int(r['d'])==d and int(r['expected_n'])==n and r['boundary']=='free') for n in (1024,4096,16384,65536)]
 sequence=' → '.join(r['wired_whole_box_fixed_connections']+'/16' for r in group)
 section+=f"| {d} | {sequence} | {float(group[-1]['wired_whole_box_far_fraction']):.4f} |\n"
section+='''
The fixed-inner-window brackets converge to 0/16, 0/16 and 0–1/16 (wired lower/free upper) in dimensions 3,4,5 respectively at the final scale. This concerns only that small fixed window: the d=3 whole-box wired successes above show directly why a zero in a small observation window must not be read as global disconnection. The interior connected-pair fractions generally fall as separation increases, especially in d=4,5. The limited scales, dependence, and path escape permit no conclusion that the infinite forest is disconnected, no estimate of its number of trees, and no fitted critical dimension.

**Checks and reproducibility.** `code/poisson_msf.py --validate-only` compares the sparse Kruskal trees against an independently implemented dense Prim algorithm on 120 points in each dimension with both metrics; all edges agree. It also compares the augmented wired MST with full Prim and checks the strict-sublevel finite-cut witness for every retained wired edge. During the final run the code checks that wired certificates are retained by both finite boundary conditions, periodic interior edges are a subset of free interior edges, the fixed-window free events decrease, and the wired events increase. All checks passed.

`code/audit_results.py` independently aggregates the 24,576 saved pair records, reconstructs all fractions, recalculates the t intervals using a tabulated critical value, checks the root geometry and nested monotonicity, and verifies the MST radius certificates from the saved records. It passed: `data/audit.json`. This audits the finite calculations, not the infinite-dimensional conjecture.

Run commands, from this directory:

    python3 code/poisson_msf.py --replicates 16
    python3 code/audit_results.py

The task launcher supplied nice 10; the simulation verifies it. There was one simulation process, with numerical thread environment variables set to one. NumPy NUMPY and SciPy SCIPY were used. Peak recorded resident memory was RSS bytes (RSSGB decimal GB), below 4 GB, and elapsed time was ELAPSED seconds. A candidate-edge cap guards the array sizes. The attempt to set a 3.2 GB data-segment limit was rejected by macOS; it was not an active hard limit. The reported memory bound is the measured peak RSS. No subagents or other model workers were started.

Raw data: `data/observations.jsonl` (384 graph records, seeds, sample hashes, root coordinates, graph certificates); `data/pair_observations.csv` (24,576 pair records); `data/summary.csv`; `data/run_metadata.json`; `data/simulation_run.log`; `data/audit.json`. The earlier smaller pilot is preserved separately under `data/pilot_16384/` and is not pooled with the final results. The sample hashes permit deterministic regeneration with the recorded NumPy version and seeds; the full coordinate arrays are not stored. Source PDFs and paper images were never saved.

'''
section=section.replace('MAXN',str(max(r['n'] for r in obs))).replace('NUMPY',meta['numpy']).replace('SCIPY',meta['scipy'])
section=section.replace('RSSGB',f"{meta['peak_rss_bytes']/1e9:.3f}").replace('RSS',f"{meta['peak_rss_bytes']:,}").replace('ELAPSED',f"{meta['elapsed_seconds']:.2f}")
a=text.index('## 5. Computation');b=text.index('## 6. Source record',a)
p.write_text(text[:a]+section+text[b:])
print('Computation section inserted')
