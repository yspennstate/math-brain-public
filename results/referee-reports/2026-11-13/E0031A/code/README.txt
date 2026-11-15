E0031 reproduction

Run from the task root directory. The shell must already have nice >= 10;
all numerical scripts assert it. The supplied launch.sh starts Codex at nice 10.
Set OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, VECLIB_MAXIMUM_THREADS=1.
No package installation or global file changes are needed in this environment.

1. python3 code/build_solver.py
2. python3 code/verify_solver.py
3. python3 code/proof_audit.py
4. python3 code/check_d1.py
5. python3 code/simulate.py
6. python3 code/analyze.py
7. python3 code/audit_artifacts.py

The simulation is serial and flushes samples.csv after every result. It skips
sample keys already present when restarted. Seeds are independent per (d,n,rep)
and saved, together with a hash of each input point array. Input generation uses
NumPy 2.2.3 default_rng (PCG64); see run_metadata.json. Example configurations
and matching partners are saved in compressed NumPy files.

Blossom V 2.05, by Vladimir Kolmogorov, is retained under its original private
research licence in vendor/. Source URL, archive checksum and local changes are
recorded in vendor/PROVENANCE.txt. The driver uses every complete-graph edge.
Its local changes use 64-bit integer costs, not floating-point dual arithmetic.
Every solve runs the integral complementary-slackness/feasibility checker at
zero tolerance. Independent exhaustive and NetworkX comparisons are in
verify_solver.py.

Distances are rounded to 10^-12 for optimization, and the returned matching's
ordinary Euclidean length is recorded. If real distances were evaluated without
rounding, the selected cost is within n/(2*10^12) of the real optimum, in addition
to floating-point distance-evaluation error. Thus this is an exact matching
algorithm for discretized weights, not symbolic algebraic optimization of square
roots. No nearest-neighbour truncation, Delaunay restriction, heuristic matching,
Poisson sample-size approximation, periodic metric, or bipartite relaxation is
used.

Theorem and page notes are in REPORT.md and sources/SEARCH.txt. Numerical
results and fitted slopes are evidence only. analyze.py uses 4,000 stratified
nonparametric bootstrap replicates for variance intervals and finite-size slope
intervals. The unweighted log-log regressions are exploratory summaries, not
estimates with guaranteed asymptotic bias control.

get_source.py downloads a source PDF into memory, converts it to page-labelled
plain text, and discards its bytes. It never writes a PDF or page image.
