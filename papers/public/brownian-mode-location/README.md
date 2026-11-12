# The mode of classical and free Brownian motion with an initial distribution at large time

Yitzchak Shmalo

Let mu be a probability measure on the real line with mean m and finite variance v. The law at time t of a Brownian
motion started from mu is mu * N(0,t); the law at time t of a free Brownian motion started from mu is the free
convolution of mu with the semicircle law S(0,t) of variance t. Hasebe and Ueda (*Large time unimodality for
classical and free Brownian motions with initial distributions*, ALEA Lat. Am. J. Probab. Math. Stat. 15 (2018),
353-374, Problem 4.6) asked for an estimate of the position of the mode of these laws at large time.

The paper proves

- the density of mu * N(0,t) has a unique global maximizer for t >= 600 v, within sqrt(2) v / sqrt(t) of m, and
  within E|X-m|^3 / t of m when the third absolute moment is finite;
- the density of the free convolution has a unique global maximizer for t > 7 (7 + 4 sqrt 2) v, within
  4 (7 + 4 sqrt 2) v / sqrt(t) of m, and within 26 ((2 + sqrt 2)^3 v^(3/2) + E|X-m|^3) / t of m when the third
  absolute moment is finite;
- with a finite third moment the maximizers are m - mu_3/(2t) + o(1/t) and m - 3 mu_3/t + o(1/t), and with a finite
  seventh moment and central moments mu_k they are

      m - mu_3/(2t) + (mu_5 - 6 v mu_3)/(8 t^2) + O(t^-3)        (classical),
      m - 3 mu_3/t + (5 mu_5 - 22 v mu_3)/t^2 + O(t^-3)          (free);

- explicit versions under the exponential moment condition of Hasebe and Ueda and for compactly supported mu.

The free part uses Biane's description of the free convolution with a semicircle law.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/mode_checks.py`: symbolic derivation of the coefficients of the two expansions, the maximizers of several
  initial laws at large t against the expansions, and a scan of the two densities at the thresholds of the theorems.
  Output in `code/mode_checks.json`.
- `code/checks.py`: for four finitely supported laws, finds both global modes by grid search and Newton's method at
  40-digit precision (the free mode through Biane's parametrization) and compares them with the two-term expansions
  for t = 100, ..., 1600. Output in `code/checks_out.txt` and `code/checks.json`.
- `lean/Algebra.lean`: the polynomial identity used for concavity in the free case and coefficient arithmetic of the
  free expansion, checked with Lean 4 and Mathlib. The analysis is not formalized.

## Running

    python code/mode_checks.py code/mode_checks.json
    cd code && python checks.py > checks_out.txt

The first program needs SymPy and mpmath, the second mpmath; each takes several minutes. The Lean file compiles
inside any Lean 4 project with Mathlib (`lake env lean Algebra.lean`).

An archived copy of the paper is at https://doi.org/10.5281/zenodo.24064373.

## License

Paper: CC BY 4.0. Code: MIT.
