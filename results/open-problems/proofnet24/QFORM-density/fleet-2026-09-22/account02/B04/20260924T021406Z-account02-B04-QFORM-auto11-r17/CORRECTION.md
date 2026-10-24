# Immutable notation/numerical correction

In `REPORT.md`, Section 4, the sentence describing the uniform `0<epsilon<=1/16` ambient D/D' family says the bound stays between `5.0597` and `5.0662`. The exact endpoint computed and used everywhere else is

`5.059613126870304...` at `epsilon=1/16`,

so the correctly rounded interval is

`5.0596 <= B_D(epsilon) < 5.0662`

(with the upper endpoint approached as `epsilon->0`). No theorem, hypothesis, proof step, comparison order, or remaining implication changes.
