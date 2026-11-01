# B04 checkpoint — delocalized-square splice

Programme: `QFORM-DENSITY-3EIG-20260922`; fleet02/B04. Full target remains OPEN.

First substantive calculation. Let `Z_K` be a disjoint original-coordinate product bank, `c!=0`, and let `R` be a quadratic polynomial in the remaining independent original coordinates. Suppose a disjoint physical cross block `M` of `R` has `E2=e2(M^T M)>0`. Fleet01/B01 `QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`, source `yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`, gives

`sup_s E|R-s|^(-1/2) <= C_E2 E2^(-1/8)`,

`C_E2 <= 12*2^(5/6)*e^(5/24)=26.3340461808...`,

with arbitrary two-sided self curvature. The product-projection bound source-pinned by fleet03/B04 r20/r27 gives

`||p_(c^T Z)||_inf <= sqrt(2)/||c||_2`.

Hence, for arbitrary residual-dependent shift `m`,

`Q=a[c^T Z+m]^2+R`

has conditional square kernel at most

`(sqrt(2)/||c||) |a|^(-1/2)|u|^(-1/2)`.

Therefore

`||p_Q||_inf <= 12*2^(4/3)*e^(5/24) (|a| ||c||^2)^(-1/2) E2^(-1/8)`

`=37.24196526099... (|a| ||c||^2)^(-1/2) E2^(-1/8)`.

This removes the `sqrt(m)` loss from selecting one physical coordinate in a flat `m`-coordinate rank-one square.

Stress family to finish: even `m`, `c=m^(-1/2)1`, `delta=1/4`, `M=[[5/4,3/4],[3/4,5/4]]`,

`Q_m=(c^T Z)^2 + delta||X||^2 - delta||Y||^2 + 2 X^T M Y`.

Here `spec(M)={2,1/2}`, `E2(M)=1`, and the full symmetric matrix spectrum is

`{1, +-sqrt(65)/4, +-sqrt(5)/4, 0^(m-1)}`,

so it is genuinely rotated, indefinite, and target-valid. The new bound is `<37.242`, uniformly in `m`. The same form written using one physical `Z_i` square has pivot `1/m`; the partner-source physical-square splice costs `26.3340461808 sqrt(m)`.

Next in this run: on the same matrix split the flat square bank in half. The natural cross cut has singular values `{2,1/2,1/2}` and `E3=1/4`, but every nonzero 3x3 minor contains both residual X rows, so all admissible e5 third-volume weights fail their row-marginal gate. Compute the direct ridge gate exactly and publish the comparison.
