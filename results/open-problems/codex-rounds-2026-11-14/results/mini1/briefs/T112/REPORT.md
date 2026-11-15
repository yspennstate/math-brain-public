VERDICT: COMPUTED exact balance census of 364392 cyclically joined three-chain presentations through 24 elements

For three chains of a common length m, add A_a<B_b, B_c<C_d, C_e<A_f,
with all six coordinates between 1 and m. Every acyclic nonchain
presentation for m=1,...,8 has a balanced pair. This counts parameter
presentations, not isomorphism classes or all posets on 24 elements.

There are 446,964 presentations: 82,488 cyclic, 84 chains, and 364,392
nonchains. Of the nonchains, 347,718 have width three and 317,730 have
width three and are ordinal-indecomposable.

The exact minimum balance over the width-three members is 137/344,
attained at m=3 with gates (1,1,3,3,1,3). This poset has 344 extensions
and Pr(A_3<B_3)=137/344. Over all nonchain members the minimum is 1/3.
The separate minima for each m are in PROOF.md and summary.csv.

The general conjecture remains open in the primary sources checked.
SOLVED_ELSEWHERE.md records the literature search and an unverified newer
partial-result lead. No external theorem is needed for this finite result.

Reproduction commands, run from this directory:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py /usr/bin/clang++ -std=c++17 -O2 -Wall -Wextra census.cpp -o census
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py ./census 8 > census.out
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py /usr/bin/clang++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py ./verify 8 > verify.out
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py python3 brute_small.py > brute_small.out
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py python3 audit_data.py > audit_data.out
```

The lattice-path census took 2.514 seconds and 1.969 MiB peak resident
memory. A separate predecessor-subset recurrence verified every saved
certificate in 11.035 seconds and 2.828 MiB. It also counted all 2,532
unordered pairs in 19 extremal presentations, confirming all reported
minima. Direct permutation enumeration independently checked every pair
in all 65 presentations at m=1,2 and the standard tight three-element
example. It also checked every pair in the width-three minimizer by
enumerating all 1,680 unrestricted three-chain shuffles, retaining 344
extensions and finding exactly 137 with A3 before B3.
Aggregate counts and the largest possible extension count were
rederived independently. Full outputs and intermediate failures are in
LOG.md. Data are certificates.csv, summary.csv and extrema_pairs.csv;
manifest.json records their hashes and aggregate counts.

What failed: the pilot exposed a reversed inequality in the cycle
rejection cross-check; it was corrected before the full run. The search
found no counterexample. The sandbox rejected priority and memory-limit
changes. Children already inherited nice 20; explicit small state spaces
and measured memory stayed far below 1 GB. CPU and wall-time guards were
retained. The linked PDF for the newer partial-result lead could not be
opened, so its claims were not adopted.

Limits: this does not prove an infinite-family theorem or settle arbitrary
width three. The chain lengths are equal and there are exactly three
specified generating cross-relations. Novelty relative to every existing
structural result has not been established. The two counting algorithms
share the family definition and arithmetic type, but use different states
and recurrences; permutation checks provide a third small-case audit.

Next: add unequal chain lengths or a fourth joining relation. Preserve
the independent subset verifier and save every pair certificate. An
analytic lower bound for the three-relation family would be more useful
than merely raising the equal-chain cutoff: no width-three member in this
census comes close to 1/3.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:16 Asia/Tbilisi.
