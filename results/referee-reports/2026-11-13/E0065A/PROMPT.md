Open problem E0065. Source: R. Ganikhodzhaev, F. Mukhamedov and U. Rozikov, "Quadratic stochastic operators and processes:
results and open problems" (Infin. Dimens. Anal. Quantum Probab. Relat. Top. 14 (2011); arXiv version 2009/2010, find it by
title), Problem 12, PDF p. 7. For a quadratic stochastic operator V on the simplex S^{m-1},
(V x)_k = sum_{i,j} P_{ij,k} x_i x_j with P_{ij,k} = P_{ji,k} >= 0 and sum_k P_{ij,k} = 1, let lambda_m be the smallest number
such that P_{ij,k} > lambda_m for all i,j,k implies V is regular (every trajectory converges to a single fixed point). Theorem 7
of the source gives lambda_m <= 1/(2m) and lambda_2 = (3 - sqrt 7)/2. Find the exact value of lambda_m for every m >= 3.
Read the source for the exact definition (strict versus non-strict inequality, whether regularity means convergence for every
initial point to one common fixed point) and the proof of Theorem 7 and of lambda_2.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Theorem 7, its proof and Problem 12 exactly. Find
   the original paper where lambda_2 = (3 - sqrt 7)/2 was computed and the 1/(2m) bound (Ganikhodzhaev, Kesten "Quadratic
   transformations: a model for population growth", Lyubich's book "Mathematical structures in population genetics"), and
   search 2009-2026 work on regularity of QSOs with positive coefficients, "contractive" QSOs, Zhamilov / Jamilov, Mukhamedov-
   Saburov, Rozikov-Zhamilov "F-quadratic stochastic operators", Saburov "regularity of positive QSOs", "lambda_m", and later
   surveys (Mukhamedov-Ganikhodzhaev book 2015). If lambda_m is determined in print for all m >= 3, give the exact reference and
   theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand lambda_2. Re-derive lambda_2 = (3 - sqrt 7)/2 completely: the extremal operator, why below the threshold a
   2-cycle (or a non-convergent orbit) exists, why above it V is a contraction or has a Lyapunov function. Explain why the
   argument does not extend directly to m >= 3.
3. Prove what you can, with complete proofs: the exact lambda_3; or an improved upper bound lambda_m <= c_m < 1/(2m) for all m;
   or a lower bound by an explicit non-regular operator with all coefficients above a value (for instance a symmetric operator
   with a period-2 orbit or an attracting cycle), giving matching bounds for some m or the asymptotics of lambda_m as m grows.
   Note that sum_k P_{ij,k} = 1 forces lambda_m < 1/m, so the scale is 1/m.
4. Compute. For m = 3, 4 search numerically (optimisation over P with all entries >= lambda, symmetric families first) for
   non-regular operators: period-2 points of V (solve V(V x) = x, x not fixed), and stability of fixed points; locate the
   largest lambda at which non-regularity occurs, then certify the candidate exactly (algebraic numbers, interval arithmetic)
   if possible.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
