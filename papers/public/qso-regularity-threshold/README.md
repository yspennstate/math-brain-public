# On the regularity threshold of uniformly positive quadratic stochastic operators

Yitzchak Shmalo

This repository contains a paper on quadratic stochastic operators on the simplex whose heredity coefficients are
all bounded below, together with the programs behind its exact and numerical checks.

Paper: [paper/main.pdf](paper/main.pdf) (source [paper/main.tex](paper/main.tex)).

## Summary

A quadratic stochastic operator V on the simplex of probability vectors in R^m is regular if every trajectory
converges to one point. Write lambda_m for the least number such that every operator whose heredity coefficients are
all at least lambda_m is regular. Ganikhodzhaev and Rozikov ask for this threshold in their survey of open problems
(arXiv:0902.4207). The paper proves

* lambda_2 = (3 - sqrt 7)/4,
* (1 - 1/sqrt(m+1))/(2m) <= lambda_m <= 2/(3m + 2 + sqrt(m^2 + 12m + 4)) < 1/(2m) for every m >= 3,

so that 2m lambda_m tends to 1. The upper bound comes from a contraction of V in the Fisher-Rao distance; the lower
bound comes from an explicit family of positive operators with a two-cycle. The exact value of lambda_m for m >= 3
remains open.

## Code

Python 3 with NumPy, SciPy and SymPy (the runs here used Python 3.14.3, NumPy 2.4.3, SciPy 1.17.1, SymPy 1.14.0).
Run the scripts from the repository root.

* `code/exact_checks.py` checks in exact arithmetic the binary identities of Section 3, the contraction condition of
  Section 4, the two-cycle of Section 5 for m = 3, ..., 8, and the examples of Section 5 with the spectral radius of
  the derivative of V^2. It writes `data/exact_checks.json`.
* `code/search.py cycles` maximizes the least coefficient of an operator with a two-cycle, or with two distinct fixed
  points, for m = 3, 4 and two lower bounds on the separation (Table 2 of the paper). It writes
  `data/search_cycles.json`.
* `code/search.py random` iterates 4,320 random operators with least coefficient between L_m + 10^-4 and
  C_m + 10^-4 for m = 3, 4. It writes `data/search_random.json`.

`SHA256SUMS` lists the SHA-256 hash of every other file in the repository.

## License

The code is released under the MIT License (see `LICENSE`). The paper is the author's work; please cite it if you
use the results.
