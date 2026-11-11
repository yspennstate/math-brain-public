# The dimension of harmonic measure on Galton-Watson trees increases at small bias

Yitzchak Shmalo, November 2026

Let T be a Galton-Watson tree without leaves whose offspring number N is not constant and has finite mean m, and
let d(λ) be the Hausdorff dimension of the harmonic measure of the λ-biased random walk on T, for 0 ≤ λ < m.
Lyons, Pemantle and Peres asked whether d(λ) increases with λ (Question 17.29 in Lyons and Peres, *Probability on
Trees and Networks*). The paper proves that d is continuously differentiable on [0, k0), where k0 is the smallest
value taken by N, and that

    d'(0) = -(1 - E[1/N]) Cov(log N, 1/N) > 0,

so d is strictly increasing on an interval [0, ε]. The question on the whole interval [0, m) remains open.

## Contents

- `paper/harmonic_dimension_slope.pdf`, `paper/harmonic_dimension_slope.tex`: the paper.
- `code/dim_check.py`: Monte Carlo evaluation of d(λ) and of its derivative from the formula of Lin and Rousselin,
  for four offspring laws.
- `code/make_tables.py`: builds the tables of Section 4 from the output.
- `data/dim_200k.json`: the output used in the paper (pool 200000, 300 iterations, 6 seeds).

## Running the code

Python 3 with numpy.

    python code/dim_check.py 200000 300 6 data/dim_200k.json
    python code/make_tables.py data/dim_200k.json tables.tex

The first command takes about fifteen minutes on one core.
