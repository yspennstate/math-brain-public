# Repairs

No new repair proposed.

C02 is independently regression-tested in this run. Minimal insertion after the conditional bound and before (4.5):

\[
|\mathbb E_{X_{I'}}F(X_{I'})|^2\le \mathbb E_{X_{I'}}|F(X_{I'})|^2.
\]

This repairs L319-L322 without changing any constant. The complex-measure domination, scaled Plancherel coefficient, mollification, and downstream Step 3 were independently checked.
