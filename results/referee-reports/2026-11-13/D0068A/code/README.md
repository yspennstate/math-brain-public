# Reproduction

All commands run from the task directory. The launcher already supplies nice
10; `enumerate` refuses to run at a higher priority. Each program is single
threaded; set OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1.

```
python3 code/fetch_sources.py
c++ -std=c++17 -O3 code/enumerate.cpp -o code/enumerate
mkdir -p data
code/enumerate data
python3 code/verify.py
```

The first command downloads PDF bytes into memory and saves only plain text
with page labels. No PDF file is created. Additional source retrievals and
their limitations are documented in sources/literature_audit.txt.

Each graph file stores one row per y from −128 to 128; within a row x runs
from −128 to 128, and two bits per vertex encode the right and upper edges.
Boundary-exiting edges have bit zero. mt19937_64 seeds, rejected sample
counts, exact root coordinates, nmax, runtimes, and nice are recorded.

The origin component must reach all four window faces. This is a finite
proxy for membership in the infinite cluster, not a certificate. The other
two roots are the nearest distinct component vertices to (8,0) and (0,8),
searched within [−16,16]² with row-major tie-breaking. The origin is the
first root. Rejection conditioning and root selection bias the sample;
there is no claim of unbiased infinite-cluster sampling.

DFS visits every simple path once, marking all current path vertices and
unmarking on return. Counts for all lengths up to nmax are accumulated as
unsigned 64-bit integers. The deterministic bound 4·3^(nmax−1), with
nmax≤28, is below 2^64. Every root is farther than nmax from the window
boundary, so its finite-n counts agree with any infinite completion of
the sampled edges. This removes enumeration-boundary error, but does not
certify the root's membership in the infinite cluster in that completion.
