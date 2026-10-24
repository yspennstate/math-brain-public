# Post-write peer refresh: the weighted scalar replacement is globally finite on the B15 source

After the immutable main report was written, fresh main exposed the independent concurrent account02/B01 run `20260922T180441Z-account02-B01-qform-r26`, canonical `yspennstate/math-open-problems@bda6ef89066f27778833b0f725b011d4ff64d8c8`. It independently refutes the same scalar-residual worst-level supremum on a different Hadamard four-cube target and identifies the weighted expectation as the surviving interface. This supplement records the corresponding exact global weighted bound for the B15 simple-spectrum source; no novelty or priority claim is made.

Keep the B15 source from REPORT.md: iid `Uniform[0,1]`, Hadamard coordinates, eigenvalues `(1,2,-3,1/2)`, `Q'=(1/2)Y4^2`, and `Y4 in [0,2]`. Let `h(y)=p_{Y4}(y)`.

Because the orthogonal change of variables preserves four-dimensional Lebesgue density and the physical cube density equals one, the conditional law of `(Y1,Y2,Y3)` given `Y4=y` is uniform on the corresponding three-dimensional cube section. Its conditional density norm is therefore exactly

`||rho_{123|Y4=y}||_infinity = 1/h(y)`

for almost every `y` with `h(y)>0`.

Since `Q'=(1/2)Y4^2` is one-to-one on `[0,2]`, conditioning on `Q'` is equivalent to conditioning on `Y4`, and hence

`E ||rho_{123|Q'}||_infinity^(2/3)
 = integral_0^2 h(y) [1/h(y)]^(2/3) dy
 = integral_0^2 h(y)^(1/3) dy.`

Now `h` is a probability density supported on an interval of length two. Hölder gives

`integral_0^2 h(y)^(1/3) dy
 <= (integral_0^2 h(y) dy)^(1/3) 2^(2/3)
 = 2^(2/3).`

Thus the exact rank-three coarea interface gives, on this source,

`boxed( E ||rho_{123|Q'}||_infinity^(2/3) <= 2^(2/3) )`

although

`sup_b ||rho_{123|Q'=b}||_infinity^(2/3)=infinity`.

This makes the discarded scalar-level weight quantitative on the whole residual support, not only near the corner endpoint.

The concurrent B01 source proves the same qualitative separation with a different spectral choice `(1,1,-1,1/128)` and also verifies its full quadratic output independently by a physical-triple theorem. The two constructions therefore converge on the correction: the revision-.11 worst-level scalar conditioning gate is false, while the scalar-weighted expectation remains viable and is exactly finite on both four-cube controls.

Full QFORM remains OPEN. The next universal statement is to bound the weighted scalar conditional coarea cost for arbitrary target matrices and arbitrary cap-one product laws, not to take a supremum over residual levels.
