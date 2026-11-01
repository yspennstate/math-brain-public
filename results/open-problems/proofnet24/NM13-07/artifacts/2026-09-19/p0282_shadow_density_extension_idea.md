# P0282 idea before production validation — shadow-set density and extension fractions

Date: 2026-09-19 UTC

## Translation

Let `j=n-k` and let `F_j(n)=ell_{n,n-j}`. Rhoades's Viennot-shadow model identifies `F_j(n)` with the number of size-`j` shadow sets, which are size-`j` nonattacking rook placements in `[n]x[n]` satisfying the shadow-set criterion. The total number of size-`j` rook placements is

`R_j(n)=j! * binom(n,j)^2`.

Define the normalized shadow density

`rho_j(n)=F_j(n)/R_j(n)`.

Then Chen's ratio factors exactly as

`F_j(n)^2/(F_{j-1}(n)F_{j+1}(n))`

`= ((j+1)/j)*((n-j+1)/(n-j))^2 * rho_j(n)^2/(rho_{j-1}(n)rho_{j+1}(n))`.

So the stronger statement `rho_j(n)^2 >= rho_{j-1}(n)rho_{j+1}(n)` would imply Chen strictly.

In the stable long-LIS range this `rho_j(n)` is exactly the predecessor's Plancherel correction `A_j(n)`, because `(n)_j^2/j! = j! binom(n,j)^2`.

## Extension-count formulation

Shadow sets are the squarefree standard monomials of Rhoades's quotient, hence form a downward-closed family inside the matching complex of `K_{n,n}`. For a valid rank-`r` shadow set `S`, let

`e(S)=#{one-rook extensions S union {p} that are again shadow sets}`.

Every rank-`r+1` shadow set has exactly `r+1` rank-`r` subfaces, while every rank-`r` rook placement has `(n-r)^2` ambient one-rook extensions. Therefore

`rho_{r+1}(n)/rho_r(n) = E_{S uniform in Delta_r}[ e(S)/(n-r)^2 ]`.

Thus log-concavity of `rho_j` is equivalent to monotonicity in `r` of the average normalized valid-extension fraction.

A first exact consequence needing no conjecture is normalized rank monotonicity `rho_{r+1}<=rho_r`, by double-counting incidence edges between consecutive ranks.

## Falsification-first test

Before trying to prove averaged monotonicity, test the tempting pointwise strengthening along every valid inclusion `S subset T` with `|T|=|S|+1`:

`e(T)/(n-|T|)^2 <= e(S)/(n-|S|)^2`.

If this is false, archive the smallest exact counterexample and do not build a proof around it. Then inspect what averaged inequality survives. If it holds in small cases, seek a direct proof from Rhoades's two ballot-word criteria.

Section-B routes for this run, all RECYCLED because all 30 have already genuinely been used on P0282 and different from the preceding triple #5/#21/#4:

- #18 SAY IT IN ANOTHER LANGUAGE — recast the Plancherel correction as density in the matching complex;
- #19 MAKE IT AN ALGORITHM — expose the ratio as an average one-rook extension probability;
- #20 FIND WHY THE ALGORITHM FAILS — falsify the pointwise extension monotonicity before attempting the averaged theorem.

This note records an idea and test plan, not a proved theorem or a claim of novelty.