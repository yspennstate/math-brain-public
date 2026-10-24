Two counterexamples for Markov-modulated Poisson processes
Research note and reproducible exact checks - 2 October 2026

The model is a 16-state rate-one directed cycle with strictly positive,
rational arrival rates. It disproves the stochastic-dominance assertion
in Asanjarani and Nazarathy, ANZIAM Journal 64 (2022), Conjecture 3.9.
It also disproves the proposed time-stationary squared-coefficient-of-
variation bound in Qi-Ming He, Journal of Applied Probability 58 (2021),
Section 4.3. The event-stationary SCV bound proved by He remains respected.

These are specialized applied-probability problems first posed in
2019-2021. This work does not claim a solution to a famous major conjecture.
No earlier published disproof was located in the searches performed on
2 October 2026; this is not an exhaustive literature or priority determination.

Contents:
  mmpp_counterexamples.pdf         Complete proof note.
  mmpp_note.tex                    Editable LaTeX source.
  mmpp_conjecture39_check.py        Main exact verifier, Python standard library.
  mmpp_exact_checks.json           Output of the main verifier.
  mmpp_independent_audit.py         Independent dense exponential-series check.
  mmpp_independent_checks.json     Output of the independent check.

Run the exact verifier:
  python3 mmpp_conjecture39_check.py

The mathematical certificate uses fractions.Fraction and integer comparisons.
The decimal strings in the JSON are displays, not inputs to the certificate.
The survival-series tail is bounded explicitly. The SCV moments are computed
by exact linear solves whose residuals are checked.

Results:
  (pi-alpha) exp(12C) 1 < -13/5314410 < 0.
  0 < time-stationary SCV < 199999/200000 < 1.

Sources:
  https://doi.org/10.1017/S1446181122000013
  https://doi.org/10.1017/jpr.2021.18
