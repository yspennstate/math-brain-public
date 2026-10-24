# Continue here: Lyons entropy, 17 September 2026

**Full conjecture: OPEN.** No complete proof or certified DPP counterexample was obtained in this session.

**Resume here:** [FISHER_CONTINUATION.md](FISHER_CONTINUATION.md) states the last unproved count-information inequality and reduces it to one explicit nuisance variance. Its six polynomial identities and five rational sample checks pass (`python verify_fourier_fisher.py`); the global inequality is not proved. Numerical search scripts and outputs are retained separately.

**Latest and strongest:** [FOURIER_POSITIVE_IMBALANCE.md](FOURIER_POSITIVE_IMBALANCE.md) proves the full four-variable Fourier Hessian sign whenever `Var(N) log(P/O)<=8/5`, including every kernel with `O/P>=1/4`. [FOURIER_ONE_SCALAR.md](FOURIER_ONE_SCALAR.md) strengthens the affine-family theorem to one fixed pair mean and reduces the remaining four-variable question to one explicit determinant, with the other three eigenvalues proved positive. Run `python verify_fourier_positive.py` and `python verify_fourier_scalar.py`. The remaining Fourier directions have `Var(N) log(P/O)>8/5` and same-sign pair-mean motion; the general Lyons conjecture remains open.

**Newest result:** [FOURIER_ALL_MEANS.md](FOURIER_ALL_MEANS.md) proves joint coupling concavity for every fixed pair of spectral means, and full three-parameter concavity when the pair means move together. It isolates one signed term for the remaining four-parameter Fourier problem. Run `python verify_fourier_all_means.py`; its 21 coefficientwise identities and 36 rational curvature checks pass. The global conjecture and unrestricted three-site milestone remain open.

[FOURIER_NEXT_STEPS.md](FOURIER_NEXT_STEPS.md) adds concavity on two convex cones with fixed diagonal and three varying couplings, an exact bivariate count reduction, two certified failures of stronger proof shortcuts, and an earlier remaining bound. Run `python verify_fourier_barriers.py`. The new Fourier work now has 75 coefficientwise polynomial identities in total; numerical optimizer scans are explicitly separate from these exact self-checks.

**Further continuation:** [FOURIER_EXTENSION.md](FOURIER_EXTENSION.md) proves the full fixed-mean four-site Fourier square for every mean, closing the central gap left by X088. It also extends the fixed-pair-mean region with nonnegative imbalance. This is a restricted theorem with exact self-checks; the unrestricted conjecture remains open. Run `python verify_fourier_extension.py` for its certificate. The original `MANIFEST.json` records the earlier checkpoint, before these added files.

Read [RESEARCH.md](RESEARCH.md), then [ADDENDUM.md](ADDENDUM.md). They contain the actual derivations, proved route obstructions, failed ideas, numerical scope, source checks, and remaining obligations. The three exact certificates disprove stronger *proof steps*, not Lyons's statement.

Run the exact self-checks with Python 3 and its standard library:

```bash
python verify_shuffle_obstruction.py
python verify_resolvent_obstruction.py
python verify_cumulative_obstruction.py
```

Each writes a JSON certificate. Natural logarithms are enclosed with exact rational arithmetic. No third-party package is needed for the three verifiers.

Exploratory scripts require numpy and scipy:

```bash
OPENBLAS_NUM_THREADS=1 python search_hessian.py --n 4 --count 6000 --output search_n4.json
OPENBLAS_NUM_THREADS=1 python search_hessian.py --n 5 --count 4000 --seed 170927 --output search_n5.json
OPENBLAS_NUM_THREADS=1 python search_hessian.py --n 6 --count 1000 --seed 170928 --output search_n6.json
OPENBLAS_NUM_THREADS=1 python search_real_transverse.py
OPENBLAS_NUM_THREADS=1 python search_multiscale.py
OPENBLAS_NUM_THREADS=1 python search_shuffle.py
OPENBLAS_NUM_THREADS=1 python search_swap_network.py
OPENBLAS_NUM_THREADS=1 python search_resolvents.py
```

The numerical JSON files record worst candidates and seeds through their source scripts. They are not proof certificates. The exact independently specified rational examples are deliberately separate from those searches.

The next mathematical task is still a full-sign proof or a certified negative value of the actual entropy Hessian. The independently randomized swap-network comparison and full compensated resolvent remain unproved routes. Do not assume arbitrary shuffles, pointwise resolvent positivity, or positivity of every partial integral: this session proves those substitutions false.

Earlier history: X095 three-site reduction; C074/C075 count-uniform envelope; X088 nonuniform four-site Fourier reduction; X094 weak block gluing. No old track files or scheduled tasks were changed.
