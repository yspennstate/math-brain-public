SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-22T22:13:10Z.
attacking: near-unit null heavy-row overlap: exhaustive product-preserving reduction combining residual high leverage, pair-log, and diffuse-bank wedge aggregation.

# QFORM B11 report — balanced-bank regression endpoint and finite-spike reduction

Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. Source state and conditional end-to-end map

Fresh pre-publication control: `yspennstate/math-research-brain@ab37e417299f19c541938cb54ab8ad46b085ea5d`, OWNER CONTROL revision `2026-09-22.15`; QFORM remains the sole target. The live corrections were reread. In particular this proof does not use arbitrary-joint rank-three coarea, a conditional-density cap as independence, a fixed good physical triple, perturbative deletion of small coefficients under unbounded supports, or pointwise law-uniform van-der-Corput decay.

Named assigned partner actually consumed: account02/B11 run `20260922T211715Z-account02-B11-QFORM-5f4a9c7d`, canonical proof `yspennstate/math-open-problems@08587fcda4f590bb64d655cdaa8b8dd98fa8af45`, theorem `QFORM-DIFFUSE-TRANSVERSE-WEDGE-PARTITION-v1`. Its hypotheses and conclusion used below are exact: in the exact-rank-three heavy-null normalization, if each residual transverse row has squared norm at most `1/16`, it produces disjoint ORIGINAL-coordinate banks `S,T` with

`(1/4)I_2 <= G_S,G_T <= (3/4)I_2`

and cross wedge mass at least `3/8`.

The compact conditional end-to-end map for this angularly diffuse heavy-null chamber is now:

1. partner partition `S,T`;
2. regress each bank's longitudinal spectral coordinate on its transverse two-plane;
3. if either bank is an exact graph (`delta_B=0`), the whole form is paid after conditioning on the opposite bank, with an explicit `<29.448/s` bound;
4. if a bank has `delta_B>0` and no longitudinal spike, the earlier B11 diffuse-deletion theorem applies to that conditioned bank with an exact determinant formula;
5. if diffuse deletion fails, at most three longitudinal spike coordinates occur in that bank, and removing the spike sets from both banks still leaves at least `3/32` of the partner's transverse cross-wedge mass and transverse covariance at least `I_2/16` on each side.

Thus the previous two-bank wedge debt is sharpened to a near-graph finite-spike wedge-trace problem. The derivation follows.

## 2. Setup

Let

`A=R M R^T`,  `R^T R=I_3`,  `sigma_min(M)>=s>0`,

with inertia `(2,1)` or `(1,2)`. Choose the heavy null original coordinate `0` and rotate only spectral coordinates so

`r_0=(sqrt(c),0,0)`,  `c>=1/2`,  `r_0^T M r_0=0`.

For each residual original coordinate write

`r_i=(a_i,z_i)`,  `z_i in R^2`.

Parseval gives

`sum_i a_i^2=1-c`,  `sum_i a_i z_i=0`,  `sum_i z_i z_i^T=I_2`.       (2.1)

Assume the partner diffuse hypothesis `max_i ||z_i||^2<=1/16`, and let `S,T` be the partner partition. For a bank `B in {S,T}` define

`G_B = sum_{i in B} z_i z_i^T`,
`v_B = sum_{i in B} a_i z_i`,
`u_B = sum_{i in B} a_i^2`,
`q_B = G_B^{-1}v_B`,
`e_i = a_i-q_B^T z_i`,
`delta_B = sum_{i in B}e_i^2`.

Because `G_B>=I_2/4`, all quantities are well-defined. The normal equations give

`sum_{i in B} e_i z_i=0`,
`delta_B=u_B-v_B^T G_B^{-1}v_B >=0`.                                  (2.2)

Thus `delta_B` is exactly the longitudinal energy not linearly explained by the transverse two-plane.

## 3. Exact Gram and leverage identities

Let

`K_B = sum_{i in B} r_i r_i^T = [[u_B,v_B^T],[v_B,G_B]]`,
`H_B = r_0 r_0^T + K_B = [[c+u_B,v_B^T],[v_B,G_B]]`.

Schur complementation gives the exact determinant identities

`det K_B = delta_B det G_B`,                                           (3.1)
`det H_B = (c+delta_B) det G_B`.                                      (3.2)

The heavy-row leverage in the normalized subframe `{0} union B` is

`h_B := r_0^T H_B^{-1}r_0 = c/(c+delta_B)`.                           (3.3)

If `delta_B>0`, then `K_B` is invertible and block inversion yields, for every `i in B`,

`r_i^T K_B^{-1} r_i = e_i^2/delta_B + z_i^T G_B^{-1}z_i`.             (3.4)

This left side is exactly the deletion-normalized residual leverage appearing in `QFORM-HEAVY-DELETE-DIFFUSE-v1`: normalize the full subframe by `H_B^{-1/2}`, delete the heavy row, and then renormalize the residual Gram. Congruence cancels the intermediate normalization and leaves `r_i^T K_B^{-1}r_i`.

Since `G_B>=I_2/4` and `||z_i||^2<=1/16`,

`z_i^T G_B^{-1}z_i <= 1/4`.                                          (3.5)

Therefore

`e_i^2<=delta_B/4 for all i in B  ==>  r_i^T K_B^{-1}r_i<=1/2`.       (3.6)

These are exact structural identities, not asymptotics.

## 4. New theorem: exact graph-bank endpoint is uniformly paid

### Theorem `QFORM-BALANCED-GRAPH-BANK-ENDPOINT-v1`

Under the setup above, if `delta_B=0` for either partner bank `B`, then the full quadratic form, including arbitrary coordinates in the opposite bank and arbitrary affine terms created by conditioning them, has an essentially bounded density satisfying

`||p_Q||_infinity <= C0 * 32^(1/3) / s < 29.448/s`,                   (4.1)

where

`C0=3*2^(2/3)*e^(2/3)<9.276`.

This statement is sign-dual and applies equally to `(2,1)` and `(1,2)`.

### Proof

Condition on every original coordinate outside `{0} union B`. This preserves independence of the variables that remain and turns all outside couplings into affine terms.

Because `delta_B=0`, (3.1) says `K_B` has rank two. Since `G_B` is positive definite, the residual rows in `B` span exactly the two-dimensional graph plane

`{(q_B^Tz,z):z in R^2}`.

Adding `r_0=(sqrt(c),0,0)` gives full rank three. Normalize the retained frame by `H_B^{-1/2}`. Equation (3.3) gives heavy-row leverage `h_B=1`; its physical quadratic coefficient remains zero under the congruence because it is the same original physical entry `A_00=0`. Therefore the previous B11 unit-leverage null-scalar theorem applies to every conditional form, uniformly in all affine terms.

Its determinant parameter is the normalized spectral matrix

`M_B = H_B^(1/2) M H_B^(1/2)`,

so

`|det M_B|=det(H_B)|det M|`.

At the graph endpoint, (3.2) gives `det H_B=c det G_B`. The partner covariance bounds imply

`det G_B>=1/16`,  `c>=1/2`,

hence

`|det M_B| >= (1/32)s^3`.                                              (4.2)

The unit-leverage theorem gives

`||p_(Q | outside)||_infinity <= C0 |det M_B|^(-1/3)
                              <= C0 32^(1/3)/s <29.448/s`.

Averaging the conditional densities preserves the same essential-supremum bound, proving (4.1). QED.

This strictly enlarges the exact-ray degeneration previously paid by the three-ray compiler: the rows of `B` may fill an arbitrary two-dimensional graph plane; they need not lie on one projective ray.

## 5. Positive residual energy: exact diffuse-deletion payment

Suppose `delta_B>0` and the no-spike condition in (3.6) holds. Apply `QFORM-HEAVY-DELETE-DIFFUSE-v1` to the normalized retained subframe `{0} union B`. Its bound is

`3e[(1-h_B)|det M_B|]^(-1/3)`.

Using (3.2)-(3.3), the apparent singular factors cancel exactly:

`(1-h_B)|det M_B|
 = [delta_B/(c+delta_B)] [(c+delta_B)det G_B |det M|]
 = delta_B det G_B |det M|`.                                         (5.1)

Therefore

`||p_Q||_infinity
 <=3e[delta_B det G_B |det M|]^(-1/3)
 <=3e(16/delta_B)^(1/3)s^(-1)`.                                      (5.2)

For example, if `delta_B>=1/64`, this is `<82.196/s`. The prior diffuse theorem supplies a common integrable Fourier envelope uniform in the affine conditioning parameters, so in this scoped branch the full averaged density is continuous.

The point of (5.1) is diagnostic: the only remaining loss is the genuinely new near-graph parameter `delta_B`; no hidden factor `1-c` remains.

## 6. New theorem: failure of diffuse deletion localizes to at most six spikes without destroying wedge mass

For each bank with `delta_B>0`, define the static longitudinal spike set

`H_B={i in B: e_i^2>delta_B/4}`.                                      (6.1)

Since `sum e_i^2=delta_B`, necessarily

`|H_B|<=3`.                                                           (6.2)

Moreover partner diffuseness gives, in Loewner order,

`G_{B\H_B}=G_B-sum_{i in H_B}z_i z_i^T
           >=(1/4-|H_B|/16)I_2
           >= I_2/16`.                                                (6.3)

Now use the exact two-dimensional identity

`sum_{j in T} det(z_i,z_j)^2 = z_i^T adj(G_T) z_i`.                   (6.4)

Because every eigenvalue of `G_T` lies in `[1/4,3/4]`, the same is true after swapping the two eigenvalues in `adj(G_T)`, in particular

`adj(G_T)<= (3/4)I_2`.

Thus every one row `i` can carry at most

`sum_{j in T}det(z_i,z_j)^2 <=(3/4)||z_i||^2<=3/64`                  (6.5)

of the cross-bank wedge. Three spikes on one side therefore account for at most `9/64`. Applying the same estimate to both sides and using the partner total `W_ST>=3/8=24/64`,

`sum_{i in S\H_S, j in T\H_T} det(z_i,z_j)^2
 >=24/64-9/64-9/64
 =3/32`.                                                              (6.6)

Hence even simultaneous failure of the deletion-diffuse test on both sides can be isolated to at most **six original coordinates**, while the remaining two independent banks still have positive-definite transverse covariance at scale `1/16` and retain cross-wedge mass at least `3/32`.

No claim is made that deleting these spikes preserves the old regression residuals; that would be false in general because the least-squares slope changes. The theorem only states the source-valid static localization and the surviving product/wedge certificate.

## 7. Assigned partner applied to an actual inequality

The partner account02/B11 theorem is what produces the balanced bank `B` with `G_B>=I_2/4`. In its exact-graph subcase `delta_B=0`, the calculation above gives the actual target-law inequality

`||p_Q||_infinity <29.448/s`.                                         (7.1)

Thus the partner's `QFORM-TWO-BANK-WEDGE-TRACE-v1` debt is now paid on every exact graph-bank endpoint, not only on exact projective rays. In the non-graph case the same partner bounds are used quantitatively in (3.5), (4.2), (6.3), (6.5), and (6.6).

The late partner addendum is respected: I do not infer a uniformly conditioned rank-three physical cross block from nonzero longitudinal leakage, do not promote cross-Frobenius scale through arbitrary self blocks, and do not perturbatively discard small self curvature.

## 8. Rank-two logarithm and what the third direction is doing

The opposite-sign rank-two control remains genuine: for centered unit uniforms, a product saddle such as `2XY` has a logarithmically divergent density at zero. The present argument does not erase this example.

At the exact graph-bank endpoint the third direction is visible geometrically. The residual bank occupies a two-dimensional graph plane, while the heavy null original coordinate is a third independent source transverse to that plane. After normalizing the retained subframe, the heavy row has leverage exactly one, so the null-scalar determinant theorem converts the rank-two logarithmic kernel into the integrable square-root kernel and yields (4.1). For positive `delta_B`, the scalar `delta_B` is precisely the Gram-volume measuring the extra longitudinal contamination; equation (5.1) shows exactly where the unresolved interpolation enters.

## 9. First essential remaining implication

The previous broad near-unit overlap debt can now be replaced by the narrower statement

**`QFORM-NEAR-GRAPH-FINITE-SPIKE-WEDGE-TRACE-v1`.** In the partner heavy-null two-bank geometry, assume neither bank is an exact graph, and no already-paid pair/ridge/minority-pivot certificate fires. Use the original product coordinates to control the regime in which one or both `delta_B` tend to zero. After isolating the static sets `H_S,H_T` of at most three longitudinal spikes per bank, the complement still has transverse covariance at least `I_2/16` on each side and cross wedge at least `3/32`. Prove a dimension-free quadratic density bound that jointly uses this surviving wedge core and the finite spike variables, or construct a genuine target-valid counterexample.

The proof may not replace either residual bank by an arbitrary joint density, may not treat small `delta_B` as a bounded-support perturbation, and may not take a worst conditional density over a conjugate spectral variable. Extra nonzero spectrum remains a separate interface unless one of the completed full-matrix pair/ridge certificates fires.

## 10. Regularity and status

`QFORM-BALANCED-GRAPH-BANK-ENDPOINT-v1` proves essential boundedness. The positive-`delta` diffuse branch inherits continuity from `QFORM-HEAVY-DELETE-DIFFUSE-v1`; continuity at the exact graph endpoint is not claimed by the present unit-leverage argument. The unrestricted QFORM density conjecture and its global continuity strengthening remain OPEN.

A finite checker beside this report verifies the determinant, leverage, graph-endpoint, spike-count, and constant identities; it is algebraic support only, not a universal proof certificate.
