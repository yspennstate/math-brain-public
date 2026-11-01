# P0282 idea before validation — fourth-order Plancherel centering toward an `n^(5/6)` defect window

Date: 2026-09-19 UTC

The predecessor proved an `n^(4/5)` fixed-defect boundary window by expanding the residual hook factor `log R_mu(n,j)` through order `n^-3`, centering the Plancherel statistics `C(mu)` and `S_2(mu)`, and bounding everything else by `O(j^4/n^4)`.

The next route is to keep the fourth-order term instead of treating it as error. For column heights `h_c=mu'_c` and `a_c=j+c-1`, the formal fourth coefficient is

`B_4(mu) = -sum h_c a_c^3 + (3/2)sum h_c^2 a_c^2 - sum h_c^3 a_c + (1/4)sum h_c^4`.

Writing cell content `x=c-r`, the per-cell contribution appears to collapse to a cubic polynomial in `x`, so `B_4` should be expressible using only `C(mu)=sum x`, `S_2(mu)=sum x^2`, and `S_3(mu)=sum x^3`. Conjugation should kill the odd-content means. The new complication is that `log A_j = log E[exp(2 log R_mu)]`: at order `n^-4`, the variance of the already-centered `-2 C(mu)/n^2` term contributes deterministically. The same central Jucys--Murphy element `T=sum_i X_i=sum_{a<b}(ab)` should give the exact Plancherel second moment `E[C(mu)^2]=binom(j,2)` by reading the identity coefficient of `T^2` in the regular representation.

If these identities are exact, the order-`n^-4` deterministic approximation to `log A_j` should have a fourth coefficient whose discrete curvature is positive, while the residual should be bounded by `O(j^5/n^5)`. That would yield a source-facing sufficient condition of the form

`n^5 >= C (j+1)^6`,

hence a `Theta(n^(5/6))` long-LIS boundary window. The constants must be proved explicitly; no theorem is claimed until the complete remainder and cumulant bounds are checked.

Actual Section-B routes for this invocation, all RECYCLED because all thirty have already been genuinely used on P0282, and chosen as a different triple from the predecessor's #5/#14/#3:

- **#7 TAKE THE LIMIT** — retain one more term in the exact `1/n` expansion instead of stopping at the `n^-3` approximation;
- **#25 COUNT THE SAME THING TWICE** — compute `E[C^2]` both as a Plancherel spectral moment and as the identity coefficient of the square of the transposition class sum;
- **#18 SAY IT IN ANOTHER LANGUAGE** — rewrite the Plancherel average as a small centered cumulant/mgf problem so the variance correction is separated from the pointwise hook remainder.

Validation plan: (1) symbolically derive the exact `B_4` content identity; (2) prove the two required Plancherel moments by group-algebra traces; (3) bound the fifth-order pointwise remainder and the centered-mgf error with explicit constants; (4) exact-rational partition enumeration for small `j`; only then, as a secondary metric check, advance the finite row frontier if warranted.
