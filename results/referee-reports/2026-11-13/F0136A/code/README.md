# F0136 computation

From the task directory, `python3 code/run.py` rebuilds the C++ simulation and
recreates the numerical outputs. It overwrites the numeric files in `data/`.
It runs one worker at absolute niceness at least 10 and limits numerical-library
threads to one. Python needs requests for source retrieval and matplotlib for plots.
The simulation itself needs only a C++17 compiler and the C++ standard library.

`python3 code/analyze.py` recomputes summaries and the figure from the saved CSVs
without rerunning trajectories. `python3 code/audit_artifacts.py` checks saved
source-text hashes, trajectory counts, seeds, and summary arithmetic.

Each trajectory samples one Dirichlet transition row the first time a site is
departed, then reuses that row on every return. Separate replicas have independent
seeds and environments. Coordinates are unbounded lattice coordinates stored in
a hash table; no torus or reflecting boundary is used in the simulations.
The ordered directions are +x,+y,-x,-y. Gamma variables are normalized to obtain
Dirichlet rows. Finite precision is used; this is numerical evidence.

The fresh-pair experiment samples two independent endpoint rows. If r and s are
their escape probabilities from the pair, q=r+s-r*s. The number K of complete
survived cycles has P(K=k)=(1-q)^k q. Conditional on escape, it occurs on the
first half-cycle with probability r/q, otherwise on the second. Thus
T=2K+1 or 2K+2. This avoids stepping through enormous holding times. The analysis
compares its output to an independently evaluated exact Beta moment formula.

Path trap records are a different observable: maximal consecutive traversals of
the same unordered lattice edge. Completed runs are counted at thresholds. The
last run at a checkpoint is recorded separately as right-censored. Encounters
are selected by the walk and need not follow the fresh-pair law independently.

Source retrieval:

```
python3 code/get_source.py https://arxiv.org/pdf/1601.08219v1 sabot_tournier_1601.08219v1.txt
```

PDF bytes are held in memory and passed to pdftotext through stdin. Only text
and plain-text hash metadata are written in `sources/`. A form feed separates
PDF pages. No paper PDF or page image is saved.
