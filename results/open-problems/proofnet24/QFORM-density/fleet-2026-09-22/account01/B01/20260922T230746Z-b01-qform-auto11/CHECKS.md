# Exact/symbolic checks

The run's symbolic check used the bank-level matrices directly.

For the prior five-bank completion-defect family, the three-row Gram matrix is

`G=[[3,1,1],[1,2,0],[1,0,2]]`,

with characteristic polynomial

`(lambda-4)(lambda-2)(lambda-1)`

and eigenvalues `{4,2,1}`.

Its scalar three-bank core

`M=[[2,1,1],[1,2,1],[1,1,1]]`

has characteristic polynomial

`(lambda-1)(lambda^2-4lambda+1)`

and eigenvalues `{1,2-sqrt(3),2+sqrt(3)}`.

For the new four-bilinear-banks plus square aggregate matrix

`B_13=B_31=B_24=B_42=1`, `B_55=1`, all other entries zero,

the characteristic polynomial is

`(lambda-1)^3(lambda+1)^2`,

so the bank-level spectrum is exactly `{1,1,1,-1,-1}`.

With the Livshyts--Paouris--Pivovarov one-dimensional projection cap `sqrt(2)`, the grouped-square same-sign bound is exactly

`pi*(sqrt(2))^2=2pi`,

and the account02/B01 r29 four-bank two-slope bound is

`2*sqrt((sqrt(2))^4)=4`.

All identities were checked symbolically with exact arithmetic. `STATUS=PASS`.
