# Reproduce FEIB25

Run in this folder. Processes inherited nice 10 in this session. Before heavy work, check the governor state and use a shell already at nice 10 or lower priority. Each Python command below uses one numerical thread:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
python3 -c 'import os; print(os.getpriority(os.PRIO_PROCESS,0))'
clang++ -O3 -std=c++17 npn.cpp -o npn
for n in 1 2 3 4 5; do ./npn "$n"; done
python3 levels.py census
python3 levels.py audit
python3 levels.py families
python3 search.py
python3 towers.py
python3 towers_decimal.py --precision 40
python3 towers_decimal.py --precision 50
python3 analytic.py
python3 final_audit.py
python3 summarize.py
```

The families command imports only `build` from ~/fei_solve_agent/code/mono_hidden.py. The analytic coverage check reads the earlier ../FEIB13/npn*.bin files to compare their bytes with this folder's independently regenerated representatives. All writes target this folder. The brain/math recall calls and source web access are documented separately in PAPER.md and REPORT.md.

The NPN generator represents the truth table by a uint32, bit x=1 for f(x)=−1. Output negation is normalized to make f(0)=1; it enumerates permutations and all input XOR masks. A visited bitset marks the complete orbit, and the next unvisited even truth table starts the next orbit. This proves completeness and uniqueness. Burnside's lemma in analytic.py independently checks the expected number of classes. NPN preserves level edge costs; arbitrary linear input changes are not being identified.

Each census_n*.npz contains `tt`, `W_numerator`, a common `denominator` equal to 4^n, `A`, and `E`. To recover requested quantities:

```python
import numpy as np
z=np.load('census_n5.npz')
W=z['W_numerator']/int(z['denominator'])
d=np.arange(W.shape[1])
dW=d*W
previous_dW=np.c_[np.zeros(len(W)),d[:-1]*W[:,:-1]]
A=z['A']
```

The masses are exact dyadic rationals. A/E are numerical evaluations of explicitly determined logarithms, not exact real numbers stored symbolically. Truth tables allow reconstruction of every summand. For other families, level_profiles.csv.gz contains one row per d with A_d, W_d, dW_d and (d−1)W_{d−1}. The tower rows preserve tiny exponents as decimal strings. The primary tower JSON is towers_decimal_50.json; towers.json is superseded because binary64 underflows in its smallest tails.

Candidate denominators, always excluding d=1, are:

    L1         dW_d+(d−1)W_{d−1}
    L2         dW_d+W_{d−1}
    lower_all  dW_d+Σ_{k<d}W_k
    tail_linear dW_d+(d−1)W_{d−1}+Σ_{k>d}kW_k
    global_I   I

L1/L2 are tested with a common coefficient C; allowing separately chosen fixed lower-level coefficients does not evade the proved counterexample. The finite maxima are not universal bounds. Search uses randomized single/double truth-table flips, three starts per objective/dimension, fixed seed 251110 and bounded proposal counts. It is a short hill search, not an exhaustive search above five variables. The search stores each best Boolean truth table; final_audit.py recomputes all objective values from scratch.
