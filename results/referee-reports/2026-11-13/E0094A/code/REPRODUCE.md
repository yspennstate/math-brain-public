# Reproduction

Run commands from the workspace root. Set numeric-library thread counts to one:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
```

All experiments can run sequentially. If the shell does not already have nice
level at least 10, start it under `nice -n 10`. On macOS, adding another ten
to an already positive nice value can fail; inspect `os.getpriority` first.

The source archive for nauty 2.8.9 is `sources/nauty2_8_9.tar.gz`, downloaded
from https://users.cecs.anu.edu.au/~bdm/nauty/nauty2_8_9.tar.gz.
To rebuild the enumerator:

```sh
tar -xzf sources/nauty2_8_9.tar.gz -C sources
cd sources/nauty2_8_9
./configure
make -j1 geng
cd ../..
```

Then follow the commands in REPORT.md. `run_walks.py` writes complete curves
for n=5,...,11; rerunning it overwrites those experiment outputs. Each walk
uses only one thread and less than 1.5 GB of principal arrays. The run stops
at total variation below 0.01, or at the explicit cap of 5000 steps.

The n=9 doubled curve was rerun after the resource-guard audit; its diagnostic
output is in `data/walk_n9_double.stderr`. All curves use the same propagation
kernel. macOS rejected RLIMIT_AS, so the final code checks its allocation plan
and samples its resident high-water mark instead. The rejected probe is
preserved in `data/memory_limit_probe.stderr`.

`regular_graphs.py` enumerates all connected regular graphs of even order at
most ten, all missing edges, and all perfect matchings of their complements.
It also certifies all optimizers using rational arithmetic. `cycles.py`
extends the cycle-only matching enumeration to fourteen vertices, using
floating point for those additional rows.

`audit_walk.py` is independent of the C++ ranking implementation: it uses
tuple dictionaries and integer path counts on the small state spaces.
`words.py` tests each word by exact permutation composition.
