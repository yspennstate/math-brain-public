# Four-type strictly non-Volterra QSO paper

Author: Yitzchak Shmalo. Prepared 15 September 2026.

`QSO_four_types.pdf` is the full manuscript. `QSO_four_types.tex` is its standalone LaTeX source. Build with `pdflatex QSO_four_types.tex` twice. The manuscript includes complete proofs of uniqueness, averaged contraction, stability, local analytic dependence, continuous dynamics, and exact polynomial-bit-complexity approximation.

Run `python3 qso_exact_solver.py` to reproduce `example_results.json`. The implementation uses exact integers and fractions only. Its residual is checked independently by direct Fraction evaluation in the example runner. The code illustrates and applies the mathematical theorem; it is not a formal verification of the general theorem.

## Mathematical scope and prior work

Every nonnegative four-type coefficient tensor satisfying parent symmetry, stochasticity and strict parental exclusion has a unique simplex fixed point. Allowed coefficients may vanish. This addresses the four-type uniqueness clause of Ganikhodzhaev--Rozikov (2009), Problem 11. It does not claim the entire multi-clause source problem has been solved. Jamilov (2016), DOI 10.5890/DNC.2016.09.006, reports a four-type uniqueness result for a symmetric class. The theorem here is stated for the full coefficient class, with no priority claim over that result. Jamilov's five-type counterexample is credited as prior work.

