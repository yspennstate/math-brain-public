# r26 notation correction

In `REPORT.md`, every global bordered-currency sum of the form

`sum_{j,S} det A[S,U union {j}]^2`

is over the same admissible index set as (2.2): `j in T`, `S subset T\{j}`, `|S|=3`. In particular, in (6.3) the intended definition is

`H_H = sum_{j in T} sum_{S subset T\{j}, |S|=3, S cap H != empty} det A[S,U union {j}]^2`.

Thus every term has disjoint row and column coordinate labels. No overlapping-coordinate minor is included. The proofs and numerical constants are unchanged.
