SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T05:13:53Z.
attacking: fragment-mass localization before cap normalization; prove the sharp exponent criterion and apply account02/B14's k-volume branch to a target-valid remote-fragment family.

# Early substantive checkpoint

Let each cap-one extreme marginal be `1_{E_i}` with a finite disjoint interval decomposition `E_i=\bigsqcup_j I_{ij}`, lengths `ell_{ij}=|I_{ij}|`, `\sum_j ell_{ij}=1`. For a component tuple `a=(a_1,...,a_m)`, the unnormalized product piece has mass `w_a=\prod_i ell_{i,a_i}`.

If a componentwise estimate has the unnormalized form

`mu_a{F in J} <= C |J| prod_i ell_{i,a_i}^{gamma_i}`

with every `gamma_i>=1`, then summing components gives

`mu{F in J} <= C|J| prod_i sum_j ell_{ij}^{gamma_i} <= C|J|`.

This is zero-loss and completely independent of fragment positions, support diameter, moments or translations. The threshold is sharp for this summation mechanism: if some `gamma_i<1`, split that coordinate into N equal fragments, so `sum_j ell_{ij}^{gamma_i}=N^{1-gamma_i}`.

Equivalently, if after normalizing a component rectangle the analytic certificate grows like `prod_i M_i^{beta_i}` in marginal caps `M_i=ell_i^{-1}`, then the unnormalized exponent is `gamma_i=1-beta_i`. Arbitrary-fragment uniformity by normalize-then-average therefore requires `beta_i<=0` coordinatewise. Any positive cap homogeneity is unsafe without additional cancellation/aggregation.

Target-valid application planned for the completed account02/B14 r24 `D_k` branch: for `k>=5`, `Q=2 sum_{i=1}^k X_i X_{k+i}` has spectrum `+1` and `-1`, each multiplicity k, and direct whole-law `D_k` gives `||p_Q||_inf<=C_k`. If every marginal is `1_{E_N}` with N remote intervals of length `1/N`, then conditioning on all `2k` fragment labels and rescaling each normalized interval law to cap one shrinks the cross block to `N^{-2} I_k`; hence `Z_k=N^{-4k}` and the same theorem yields only `C_k N^2` on every normalized component. Averaging cannot repair the factor. Thus whole-law localization preserves the constant, while component-normalization loses `N^2` even on an exact target matrix.

Full QFORM remains open. This checkpoint does not use pointwise quadratic Fourier decay, post-rotation independence, bounded support, or moment assumptions.
