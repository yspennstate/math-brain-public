# Reproducing the work

Run from this worker directory with Python 3, NumPy, SciPy, mpmath and clang++. The inherited process nice value in this fleet is 10; the resource verifier records it. Keep OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and VECLIB_MAXIMUM_THREADS=1. Run at most two computations concurrently. No network or shared filesystem writes are needed for the saved numerical checks.

The short record replay is:

```sh
clang++ -O3 -std=c++17 engine.cpp -o engine
python3 checks.py
python3 audit_pm.py
python3 pm_isomorphism.py
python3 mixed_audit.py
python3 periodic_audit.py
python3 interval_witness.py
```

The broad numerical suite is:

```sh
python3 enumerate.py
python3 tower_census.py
python3 census_audit.py
python3 search.py
python3 search.py other
python3 tower_search.py
python3 group_catalog.py
python3 other_groups.py
python3 group_audit.py
python3 towers.py
python3 bent_census.py
python3 balance_pm.py
python3 mixed_search.py
python3 mixed_audit.py
python3 periodic_towers.py
python3 periodic_audit.py
python3 interval_witness.py
python3 subclass_checks.py
python3 hod_reconstruct.py
python3 ot_tower_dp.py
python3 verify.py
python3 make_report.py
```

The source-reference files are already saved locally. Group enumeration regenerates each `.orbits` file and saves every retained function. The six-variable reconstruction uses Hod's corrected balanced formula. The failed literal reconstruction scripts are diagnostics, not required to verify any record. The supplied PM helper is read from the path named in BRIEF.md by audit_pm.py; the record, isomorphism and interval scripts construct their own nine-variable base locally.

`engine.cpp` stores G in `.balanced.json` as a balanced-base tower limit, in `.tower.json` as a self-tower residual lower approximation, and under `tower_search/` as that search objective. In ordinary finite-search files it is the base function's erasure ratio. The independently recomputed base statistics and tower values are separated in `verification.json`, `census_audit.json` and `group_audit.json`. Actual total evaluation counts are taken from the run logs; a witness file's evaluation field is the time of its last improvement.
