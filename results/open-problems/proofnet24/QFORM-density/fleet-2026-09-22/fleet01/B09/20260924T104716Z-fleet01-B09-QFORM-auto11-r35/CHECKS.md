# fleet01/B09 r35 deterministic checks

These finite computations are regression checks only; the universal statements are proved analytically in `REPORT.md`.

## 1. Block-Schur identities

For 100 random trials:

- draw a random symmetric indefinite invertible `2x2` matrix `B`;
- draw random `M` and symmetric `C`;
- set `A=[[B,M],[M.T,C]]`, `S=C-M.T@inv(B)@M`;
- set `A0=[[B,M],[M.T,M.T@inv(B)@M]]`.

Verified numerically in every trial:

`rank(A0)<=2`,

`s_3(A)<=||S||op`,

and for every complementary pair `i,j`,

`det A[H union {i}, H union {j}] = det(B) S_ij`.

Maximum absolute error in the bordered-minor identity: `1.0658141036401503e-14`.

## 2. Cut lemma finite stress test

For 100 random symmetric `6x6` matrices `S`, rescaled to `||S||op=1`, with `eta=1/2`, brute-force all nontrivial coordinate cuts. Whenever `max_i|S_ii|<eta`, verify

`max_(I union J=[6]) ||S[I,J]||op >= (1-eta)/2 = 1/4`.

Smallest observed slack over the finite sample:

`max_cut ||S[I,J]||op - 1/4 = 0.28735... >0`.

The proof in `REPORT.md` is exact and does not depend on this finite test.

## 3. Constants

`8*2^(1/4) = 9.513656920021768...`

`8*sqrt(2) = 11.313708498984761...`

For the required partner application with zero two-hub core and `Delta=1`,

`2*sqrt(2) = 2.8284271247461903...`.

No Monte Carlo output-density histogram is used.