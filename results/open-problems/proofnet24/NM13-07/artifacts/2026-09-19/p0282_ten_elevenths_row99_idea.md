# P0282 idea before production validation — shadow-complex obstruction and finite ninth-coefficient recovery

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Source: P0282, Chen fixed-size LIS log-concavity

The predecessor reached the rigorous growing-defect window `j+1 <= n^(9/10)/8` and explicitly said not to automate the next Taylor coefficient before trying a whole-series explanation. This note records that attempt before any new production checker or row-99 certificate.

All thirty Section-B methods have already genuinely appeared on P0282, so the methods below are **RECYCLED** rather than falsely called unused. They differ from the predecessor's `#11/#25/#3` triple.

## #1 CHANGE THE CATEGORY — shadow sets as a simplicial complex

Rhoades's Toeplitz standard-monomial basis identifies the degree-`j` standard monomials with Viennot shadow sets of size `j`. Since divisors of standard monomials are standard, the shadow sets form a simplicial complex `Delta_n` inside the rook-placement complex on `[n] x [n]`.

Its normalized rank density is exactly the retained Plancherel correction

`A_j(n) = F_j(n) / (j! * binom(n,j)^2)`,

where `F_j(n)=ell_{n,n-j}` and the denominator is the number of size-`j` rook placements. Thus the previously proved fixed-defect ULC statements are exactly log-concavity statements for this normalized shadow density.

A natural hope is that `Delta_n` is a matroid independence complex, which would open a direct Hodge/Mason route to all-rank log-concavity.

## #20 FIND WHY THE ALGORITHM FAILS — exact matroid augmentation obstruction

The matroid route fails immediately, for a source-internal reason rather than a numerical accident. For `n=3`, the shadow criterion (equivalently RSK followed by adding the unused row/column labels as the first row) gives the valid shadow sets

`A = {(2,2)}`

and

`B = {(2,3),(3,2)}`.

Both are valid shadow sets. But neither element of `B\A` augments `A`: adding `(2,3)` repeats row 2, while adding `(3,2)` repeats column 2. Hence `Delta_3` violates the matroid augmentation axiom. The same obstruction is inherited from the ambient rook/matching geometry. Therefore a direct application of matroid Hodge theory to `Delta_n` cannot be the missing whole-series proof.

This does **not** disprove normalized shadow-density log-concavity; exact tests continue to support that stronger inequality. It only kills the naive matroid explanation.

## #8 GO THE OTHER WAY AND DISCRETIZE — finite recovery of the ninth Taylor coefficient

Return to the retained Plancherel factorization

`F_j(n)=((n)_j^2/j!) A_j(n)`,

`G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`, `t=1/n`.

Instead of deriving a long list of ninth-order content moments individually, prove once that for every fixed `m`, `D_m(j)` is a polynomial in `j` of degree at most `m`.

Reason: the exact cell formula

`B_s(mu)=-(1/s) sum_{box in mu}[(j+c(box))^s-(j+c(box)-1)^s]`

expresses each coefficient of `exp(2 sum B_s t^s)` as a finite linear combination of explicit powers of `j` times products of content power sums. Under Plancherel measure, a product of content power sums is the identity coefficient of a product of Jucys--Murphy power sums. For total transposition-word length `L`, group the words by equality/support pattern. Any identity word has no vertex appearing exactly once, hence uses at most `L` vertices; each pattern contributes a falling-factorial polynomial in `j` of degree at most its support size. Tracking the explicit powers of `j` in the cell formula gives total degree at most the Taylor order. The logarithm recurrence preserves this degree bound.

Therefore `D_9(j)` is determined by ten exact values, say `j=0,...,9`. Exact partition/hook enumeration can recover those ten values, interpolate the unique degree-9 polynomial, and then independently verify it at extra values. If its Chen discrete curvature is positive for all `j>=1`, the retained Cauchy-tail argument immediately lifts the growing-defect exponent from `9/10` to `10/11` without any unproved moment identity.

This finite-interpolation argument is intended as a rigorous theorem proof with an exact finite core, not curve fitting: the degree bound is the proof that ten exact evaluations determine the coefficient globally.

Only if the ninth curvature is favorable will a production exact checker and row-99 finite seam be archived.