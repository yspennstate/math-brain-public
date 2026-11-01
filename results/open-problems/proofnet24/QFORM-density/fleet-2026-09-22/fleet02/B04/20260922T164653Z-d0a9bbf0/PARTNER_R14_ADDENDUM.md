# fleet02/B04 — latest-partner r14 strengthening

A newer completed named-partner result appeared after the primary report and first correction addendum:

- fleet03/B04 `QFORM-RANK2-SCHUR-NOLEVERAGE-v1`, canonical `yspennstate/math-open-problems@2761bd3896c56a1f929761e69035ba7cb8ebc2bc`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T164839Z-r14/REPORT.md`, blob `fe77dd5ab13c1de27d93fc2ba0b8c9f637d4a523`.

It proves that for one original-coordinate pivot

`A=[[C,b],[b^T,a]]`, `a!=0`,

if the Schur complement `S=C-bb^T/a` has rank exactly two with nonzero eigenvalues `mu_1,mu_2`, then

`||p_(X^TAX)||_inf <= C_* |a|^(-1/2)|mu_1mu_2|^(-1/4)`,

where

`C_* = 8 sqrt(2) 3^(3/4) 5^(1/4)/sqrt(e)
     =23.390590510770124... .`

This theorem is compatible with the square-dominant spectral transfer proved in the primary B04 report and gives a strictly stronger closure on the exact-rank-three subbranch.

## Actual inequality obtained by combining r14 with this run

Assume the target hypothesis `s_3(A)>=1` and a physical coordinate satisfies

`|a|>=1/312`, `||b||_2<=|a|`,

and suppose its Schur complement has rank exactly two. The physical square-completion shear from the primary report gives

`A=T^T diag(a,S)T`,

with

`||T||^2 <= M_*=(3+sqrt(5))/2`.

Hence

`s_3(diag(a,S)) >= s_*:=1/M_*=(3-sqrt(5))/2`.

Because `S` has rank exactly two, `diag(a,S)` has exactly three nonzero singular values. Therefore both residual eigenvalues obey

`|mu_1|,|mu_2|>=s_*`,

so

`|mu_1mu_2|>=s_*^2`.

Substituting into the partner theorem gives

`||p_(X^TAX)||_inf
 <= C_*/sqrt(|a|s_*)
 <= C_* sqrt(312/s_*)
 =668.5072525903349... <669.`

Thus the square-dominant heavy-coordinate branch is completely closed whenever the Schur residual has rank two, **without any residual leverage or spectral-window condition**. This is an actual application of the newest fleet03/B04 theorem, not merely a citation.

## Explicit unit-scale rotated indefinite form

Let `R` be the first three columns of the normalized `4x4` Walsh-Hadamard matrix and let

`A=R diag(1,1,-1) R^T`.

Then `A` has spectrum `{1,1,-1,0}`. Every physical row of `R` has leverage `ell_i=3/4`, and every diagonal entry of `A` equals `a_i=1/4`. The partner exact-rank-three identity gives

`P_i=|det Lambda| ell_i=3/4`,

so

`|a_i|P_i=3/16`.

Its corollary therefore yields the explicit bound

`||p_(X^TAX)||_inf
 <= C_* (3/16)^(-1/4)
 =35.546010757093306... .`

This is a genuinely rotated indefinite target form and holds for every admissible independent cap-one input law.

The full arbitrary-rank conjecture remains open. The first B04 unpaid implication is unchanged in character but is narrower: `QFORM-TWO-STAGE-BANK-OPPOSITE-SIGN-AGGREGATION-v1` only needs to handle the bank/opposite-sign configurations and arbitrary-rank Schur residuals not covered by this exact-rank-two closure.
