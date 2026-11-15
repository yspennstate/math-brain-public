# Reproducing C0092 calculations

The C++ program has no external library dependencies and uses one thread. Python analysis needs numpy; matplotlib is optional for the SVG plot. Source retrieval additionally needs requests and pdftotext. Every source PDF is held in RAM and piped to pdftotext; it is never saved.

Run from the project root, under nice 10. The original agent and all children inherited nice 10 from the launch script. Do not start multiple copies. The main numerical child used 3,604,480 bytes maximum resident memory as reported by macOS getrusage; Python analysis is larger but far below 4 GB.

Build:

~~~sh
c++ -O3 -std=c++17 code/fk.cpp -o code/fk
~~~

Exact histograms:

~~~sh
code/fk enum 2 2 data/exact_d2_L2.csv
code/fk enum 2 3 data/exact_d2_L3.csv
code/fk enum 3 2 data/exact_d3_L2.csv
python3 code/check_exact.py
~~~

Side-2 periodic tori have parallel bonds, both retained. A side-L, d-dimensional torus has L^d vertices and d L^d bonds.

Monte Carlo input rows are whitespace-separated:

~~~text
d L q p chain start seed burn_sweeps measurement_sweeps sample_stride
~~~

start=0 means empty and start=1 means full. One sweep makes |E| random edge choices with replacement. Seeds use C++ mt19937_64. Observables are taken after the indicated number of sweeps, not after individual updates.

Reproduce the original scan, extension, and final validation:

~~~sh
code/fk mc data/jobs.txt data/mc_samples.csv 2>data/compute_progress.log
code/fk mc data/extension_jobs.txt data/extension_samples.csv 2>data/extension_progress.log
code/fk mc data/validation_jobs.txt data/validation_samples.csv 2>data/validation_progress.log
python3 - <<'PY'
from pathlib import Path
with Path('data/mc_samples.csv').open('a') as out, Path('data/extension_samples.csv').open() as inp:
    next(inp)
    for line in inp:
        out.write(line)
PY
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MPLCONFIGDIR="$PWD/data/matplotlib_cache" XDG_CACHE_HOME="$PWD/data/cache" python3 code/analyze.py
~~~

The first command overwrites the combined scan with the original one. Append the extension exactly once. Main jobs: 486 chains. Extension: 102 chains. Total main-scan samples after extension: 235,200. Validation: 36 chains, including longer runs at d=3,L=2,q=.25,p=.6; 268,000 retained validation samples.

Main scan: 400 burn-in sweeps, 1600 measured sweeps, stride 4, two independent chains (empty and full) per parameter. The 2D original grid is centered on sqrt(q)/(1+sqrt(q)) as a heuristic reference only; this value is not assumed to be a theorem below one. The extension adds lower p-values. The 3D grid is .04,.06,...,.30.

Analysis uses batches of 20 and 40 observations for standard errors (the larger estimated error is retained), split R-hat, and Geyer's initial monotone positive-pair autocorrelation estimate for effective sample size. The ESS autocovariance is computed by zero-padded FFT. Five hundred block-bootstrap replications estimate finite-grid pseudocritical variability. Raw samples, all seeds, summaries and the initial rare-event diagnostic are retained.

There is no mixing proof. A constant observed winding indicator does not certify probability zero or one. A bootstrap interval covers sampling variability conditional on these chains; it does not cover finite-size bias or grid discretization. Full susceptibility, susceptibility excluding a largest component, and susceptibility restricted to nonwrapping components are different observables.
