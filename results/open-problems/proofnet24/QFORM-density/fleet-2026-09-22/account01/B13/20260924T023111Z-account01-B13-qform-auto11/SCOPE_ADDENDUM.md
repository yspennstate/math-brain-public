# Scope addendum — extremal-product reduction

This addendum narrows one presentation point in `REPORT.md`; it does **not** change the new coefficient/Pluecker theorems `QFORM-HIGHSCORE-INTERSECTING-58-v1` or `QFORM-LOWSCORE-TO-HUBSTRIP-18-v1`.

The report's one-coordinate threshold proof of an **exact zero-loss** indicator replacement implicitly assumes the existence of a finite-measure quantile threshold satisfying

`|{h>t}|<=1<=|{h>=t}|`.

On the noncompact line this particular threshold need not exist (for example a bounded `h` may approach its supremum at infinity while every strict superlevel below the supremum has infinite measure). I am therefore **not using the exact zero-loss assertion as a proved premise in this run** until a separate purification proof repairs that noncompact attainment issue.

The safe reduction needed for QFORM remains the optimizer-free approximation/finite-mixture statement already established in the programme and explicitly retained by account02/B13 r39:

> For every strict slab witness under cap-one mass-one product densities and every `epsilon>0`, one can find bounded finite-union unit-measure sets `E_i` such that the product-indicator slab probability is at least the original slab probability minus `epsilon`.

One implementation is: truncate and approximate each marginal in `L^1` by a compactly supported simple cap-one density; on the finite partition, the vector of cell masses lies in a finite hypersimplex and is a convex combination of incidence vectors corresponding to unit-measure indicator sets; tensor the finite marginal mixtures and select one product component whose slab integral is at least the mixture average. The product telescoping estimate

`||prod_i f_i-prod_i g_i||_1 <= sum_i ||f_i-g_i||_1`

controls the approximation loss. Refining the partition gives bounded finite unions. No common support diameter or uniform fragment-count bound is obtained.

Thus every strict violation of any proposed universal density bound transfers with arbitrarily small loss to bounded-finite-union product indicators, which is sufficient for contradiction/compactness-free QFORM arguments.

All new structural inequalities in `REPORT.md` are coefficient-only consequences of the source-pinned account02/B13 r39 theorem and remain unchanged. In the final handoff, interpret the product-set formulation with arbitrarily small strict-witness loss rather than relying on exact attainment.
