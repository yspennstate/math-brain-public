# Independent audit of `CONDITIONAL_LAW.md`

**Disposition.** The conditional thinning law, its Lévy density, and the fine/coarse multiplier limits are correct under the selected mixed-cone theorem in `../agents/f03_cone.md`. The stable endpoint Laplace exponent has coefficient `c_alpha Gamma(1-alpha/2) p`, **without** an extra factor `1/2`. The current draft explicitly recognizes this correction; the earlier displayed half-coefficient should be removed from the final theorem statement and kept only in the failed-routes record if desired. No external priority claim is made.

## Conditional Poisson law

The marked PPP has intensity `alpha c_alpha |z|^{-1-alpha} dz nu(dv)`, with `nu=Law(XU)`. Its positive- and negative-`z` restrictions are independent and independent of `(R,C)`. On `R_1<0<R_2`, `P_2` is measurable only from the positive restriction and uses `p_2(gamma z |R_1|)`, whereas `P_1` is measurable only from the negative restriction and uses `p_1(gamma |z| R_2)`. Conditional independence given `(R,C)` follows immediately. Since `nu` has positive density, the zero-threshold sets of the selector have zero intensity.

For `w=z^2` on either half-line,

\[
\alpha c_\alpha z^{-1-\alpha}dz
=\frac{\alpha c_\alpha}{2}w^{-1-\alpha/2}dw.
\]

Thus the displayed Lévy measures and the equivalent positive-`z` Laplace integral in `CONDITIONAL_LAW.md` agree. Near zero, `(1-e^{-lambda w})w^{-1-alpha/2}=O(w^{-alpha/2})` is integrable because `alpha<2`; at infinity the `w^{-1-alpha/2}` tail is integrable. The selected masses are finite almost surely, though their means need not be finite.

For a constant thinning probability `p` (the fine and infinite-multiplier endpoints), set `q=alpha/2`. The exact integral is

\[
\frac{\alpha c_\alpha}{2}p
\int_0^\infty (1-e^{-\lambda w})w^{-1-q}dw
=\frac{\alpha c_\alpha}{2}p\frac{\Gamma(1-q)}q\lambda^q
=c_\alpha p\Gamma(1-\alpha/2)\lambda^{\alpha/2}.
\]

The `1/2` from the Jacobian is canceled by `alpha/q=2` in the integral. This validates the draft's correction and rejects its earlier half-coefficient.

## Multiplier limits and ordering

For `x>0`, `x<=a ceil(x/a)<x+a`. At generic marks this implies the selector converges to the continuous race as `a↓0`, and every continuously escaping mark escapes at every positive discrete step size. A cell `x in ((n-1)a,na)` has an open, positive-measure overshoot strip `-cna<y<-cx`, proving `p_j(a)>p_j(0)` for every `a>0`. At `a→infinity`, every fixed `x>0` is handled in a single step and the other coordinate eventually crosses; the selected set tends to `{v_1>0 or v_2>0}`. Because `sum_N z^2<infinity` almost surely, dominated convergence applies to `P_j^gamma` for both multiplier limits. It also gives uniform finite-horizon convergence of `e^{-Q_gamma t}R` via continuity of the matrix exponential.

If a coarse multiplier is an integer multiple of a fine one, its first grid time after a threshold is no earlier. The selected sets and masses are ordered atomwise. The example in `../agents/f01_entrance.md` shows that this fails for nonnested multipliers. That example proves nonmonotonicity of individual atom selection; it does **not** by itself prove nonmonotonicity of the averaged probability `p_j(a)`, and the draft does not need that stronger assertion.

The finite-multiplier Lévy density is genuinely nonhomogeneous: `p_j(a)` has distinct limits `p_j(0)` and `p_infinity`, since the positive density `nu` charges marks with an opposing positive coordinate but continuous-race failure. Thus an exact positive-stable law is confined to the two endpoint thinning limits, even though every finite-multiplier mass remains positive and infinitely divisible.

Final root verification: the displayed endpoint coefficients in CONDITIONAL_LAW.md have now been corrected; the requested correction is complete.
