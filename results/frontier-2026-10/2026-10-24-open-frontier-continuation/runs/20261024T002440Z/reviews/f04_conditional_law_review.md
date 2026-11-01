# Independent audit of `CONDITIONAL_LAW.md`

**Verdict.** Conditional on `R_1<0<R_2` and on the selected mixed-cone theorem in `agents/f03_cone.md`, the Poisson thinning formula, multiplier limits, and non-stability conclusion are correct. The displayed stable Laplace exponent now has the correct coefficient; an earlier factor-of-two error was repaired during review.

For `z>0`, the mark selector uses the scale `a=gamma z|R_1|`. Its acceptance probability is exactly

`p_2(a)=nu{v2>0}+nu{v1>0,v2<=0,v2+c a ceil(v1/a)>0}`,

where `c=-rho`. The first term handles initial `-+` and `++`, and the second handles initial `+-`. Disjointness is immediate. The negative-`z` selector is its coordinate-exchanged counterpart under the same projected-mark law `nu`. Given `(R,C)`, the two accepted atom sets are independent restrictions of the positive and negative halves of `N`; `P1` and `P2` are consequently conditionally independent.

The positive-`z` intensity is `alpha c_alpha z^(-1-alpha) dz nu(dv)`. With `w=z^2`, this becomes `(alpha c_alpha/2) w^(-1-alpha/2)dw`, so the stated Levy measures are correct. For a constant thinning probability `p`, writing `beta=alpha/2`, the exponent is

`(alpha c_alpha/2) p integral_0^infinity (1-e^(-lambda w)) w^(-1-beta)dw`

`= (alpha c_alpha/2) p [Gamma(1-beta)/beta] lambda^beta`

`= c_alpha Gamma(1-beta) p lambda^beta`.

There is **no factor `1/2`** in this final coefficient. The source now displays only this corrected formula.

For each fixed atom, `a ceil(v1/a)` tends to `v1` as `a↓0`; the exceptional equality surface has zero mark probability. As `a↑infinity`, every finite positive `v1` lies in the first coarse cell and a `+-` atom escapes. The square-weighted Poisson measure is finite almost surely, so dominated convergence proves the almost-sure mass limits, and matrix-exponential continuity proves uniform finite-horizon output convergence. These are iterated multiplier limits **after** `m→infinity`; the note correctly avoids a simultaneous `gamma_m` claim.

For any fixed `a>0`, the overshoot strip in a cell `((n-1)a,na)` has strictly positive `nu` mass, so `p_j(a)>p_j(0)`. The continuous and infinite-multiplier acceptance probabilities satisfy `p_j(0)<p_infinity` by a positive-density dead-corner region. For finite `gamma`, the thinning factor varies with `w`, and uniqueness of the Levy measure rules out an exact positive stable law. The note's nested-grid inequality is valid only when one grid is a subset of the other; its warning about nonnested multipliers is necessary.
