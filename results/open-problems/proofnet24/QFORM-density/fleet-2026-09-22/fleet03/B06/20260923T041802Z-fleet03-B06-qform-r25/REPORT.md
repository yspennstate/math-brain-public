SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T04:18:02Z.
attacking: aggregate-before-reciprocal curved-fiber packet inequality in the double-wedge-diffuse near-rank-two tube.

# fleet03/B06 r25 — leverage-free third-volume L3 receiver plus dependence-safe outer square

**Run:** `20260923T041802Z-fleet03-B06-qform-r25`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** new supporting target-relevant theorem proved; full conjecture remains OPEN; continuity is NOT proved by the outer-square endpoint.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and the first missing implication attacked

The owner target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample.

The preceding B06 run left a full retained cross block `B` after a genuine original-coordinate square pivot. It had an aggregate two-volume receiver when a range/ridge leverage gate holds and a separate `sigma_3` receiver when a third cross singular value is quantitatively large. The first missing implication was to avoid choosing a weak physical minor or deleting a nonzero cross tail in the near-rank-two chamber.

This run changes the mechanism: aggregate **all physical 3x3 cross minors first**, use the fractional three-volume Brascamp--Lieb calculation only up to `L^(3/2)` Fourier integrability, and spend that `L3` residual through the dependence-safe original-coordinate square. The key observation is that the leverage restriction disappears at the fractional exponent `q=2`: every third-volume inclusion marginal is automatically at most one.

No rotation of the independent random coordinates, law-uniform pointwise Fresnel decay, unrestricted fiber supremum, arbitrary-joint coarea estimate, conditional projection-height moment, moment/support regularity, Gaussianity, log-concavity, or one-minor selection is used.

## 2. Source-valid inputs and why the extension is new

### 2.1 Fractional three-volume decoupling before inversion

The complete source

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,

proves the following pre-inversion inequalities for an ORIGINAL-coordinate cross block `B` between disjoint coordinate banks. Put

`Z = Delta_3(B) = e_3(BB^T) = sum_(|S|=|T|=3) det(B[S,T])^2`.

Normalize the squared third minors to a probability law and let `alpha_i` be the row inclusion marginals. For any `q>=1` for which `alpha_i<=q/2`, its Sections 5.1--5.3 give, before the final `L1` inversion,

`|phi_R(t)|^2 <= E_D F_t(D)`,

`E_D F_t <= (E_D F_t^q)^(1/q)`,

and

`E_D F_t^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2).`             (2.1)

The published theorem there states `q<3/2` only because it next requires `phi_R in L1` to obtain a continuous bounded density directly. The derivation of (2.1) itself uses only Jensen, the physical-coordinate volume-sampling Brascamp--Lieb datum, and sharp Hausdorff--Young with output exponent `q/alpha_i>=2`. At `q=2`, every `alpha_i<=1=q/2` automatically, including endpoint marginals equal to one. Thus the pre-inversion argument is valid at `q=2`; we do **not** invoke the source's `L1` conclusion outside its stated range.

The source explicitly retains arbitrary same-bank measurable phases, affine terms, outside couplings, and all additional cross singular directions. Product provenance stays in the original coordinates.

### 2.2 Dependence-safe square kernel

The completed fleet04/B18 result

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,
`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`,

proves, after completing a square in one ORIGINAL independent coordinate with coefficient `a!=0`, the pointwise domination

`p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du.`      (2.2)

No independence between `R` and the translated square variable is asserted or needed. The designated partner `fleet04/B06` still has no completed current-QFORM canonical handoff at the fresh lookup, so no partner result is fabricated; the compatible completed fleet04/B18 theorem is applied at (2.2).

## 3. Leverage-free third-volume L3 theorem

### Theorem 3.1 — `QFORM-THIRD-VOLUME-L3-NOLEVERAGE-v1`

Let `R` be an arbitrary real quadratic-plus-affine form in independent cap-one ORIGINAL coordinates. Suppose it contains an original-coordinate cross block `B` between disjoint coordinate banks and

`Z=Delta_3(B)>0`.

Then `R` has an `L3` density and

`boxed(
 ||p_R||_3 <= [3^(3/2) e^(2/3) / 2^(2/3)] Z^(-1/9).
)`                                                                    (3.1)

There is **no row- or column-leverage hypothesis**. All same-side quadratic terms, affine terms, outside couplings and every extra cross singular direction are retained.

#### Proof

Take `q=2` in the source-valid pre-inversion calculation (2.1). Since every third-volume inclusion marginal obeys `0<=alpha_i<=1=q/2`, the sharp Hausdorff--Young step is admissible for every active row, including `alpha_i=1`, where its output exponent is exactly two. Thus

`E F_t^2 <= e^3 2^(-3/2) (pi/|t|)^3 Z^(-1/2).`               (3.2)

From `|phi_R(t)|^2<=E F_t` and Cauchy--Schwarz/Jensen,

`|phi_R(t)| <= min(1, K |t|^(-3/4)),`                         (3.3)

where

`K = [e^3 2^(-3/2) pi^3 Z^(-1/2)]^(1/4).`

Let

`t0=K^(4/3)=[e^3 2^(-3/2) pi^3 Z^(-1/2)]^(1/3)
           = (pi e/sqrt(2)) Z^(-1/6).`                        (3.4)

Raise (3.3) to the `3/2` power. Since the tail exponent becomes `9/8>1`,

`int_R |phi_R(t)|^(3/2) dt
 <= 2[t0 + K^(3/2) int_(t0)^infinity t^(-9/8)dt]
 = 2[t0+8t0]
 = 18t0
 = 9sqrt(2) pi e Z^(-1/6).`                                  (3.5)

With Fourier convention `hat f(t)=int e^(itx)f(x)dx`, sharp inverse Hausdorff--Young at exponents `(3/2,3)` gives

`||p_R||_3 <= [3^(1/6)/(2 pi^(2/3))]
               ||phi_R||_(3/2).`                              (3.6)

Substituting (3.5) into (3.6) yields exactly

`[3^(1/6)/(2 pi^(2/3))]
 [9sqrt(2) pi e]^(2/3) Z^(-1/9)
 = 3^(3/2)e^(2/3)2^(-2/3) Z^(-1/9),`

which is (3.1). Since the characteristic measure has an inverse Fourier transform in `L3`, uniqueness of Fourier transforms identifies this `L3` function as the density of `R`. QED.

### Why this is a curved-fiber aggregation theorem

`Delta_3(B)` is the Cauchy--Binet sum of squares of **all** physical third minors. The reciprocal power `Z^(-1/9)` is taken only after the complete volume bank has been summed. No individual curved intersection or fiber maximum is selected. The argument therefore directly implements the B06 assignment's required aggregate-before-reciprocal replacement.

## 4. Actual fleet04 square application: an endpoint with no cross leverage

The B18 pointwise kernel (2.2) combines with any `L3` base. The preceding B06 run proved the elementary half-Riesz estimate

`sup_t int_0^infinity p(t-u)u^(-1/2)du
 <= [8/3^(3/4)] ||p||_3^(3/4)`                             (4.1)

for every probability density `p in L3`, by splitting at `U`, applying Holder on `[0,U]`, using total mass on `[U,infinity)`, and optimizing `U`.

Insert (3.1) into (2.2) and (4.1).

### Theorem 4.1 — `QFORM-THIRD-VOLUME-OUTER-SQUARE-v1`

Suppose `Q` is obtained after completing one genuine original-coordinate square of coefficient `a!=0`, leaving a residual `R` with an ORIGINAL cross block `B` satisfying `Delta_3(B)>0`. Then

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(2e) 3^(3/8)
    |a|^(-1/2) Delta_3(B)^(-1/12).
)`                                                                    (4.2)

Numerically the universal coefficient is

`4 sqrt(2e) 3^(3/8) = 14.08129836146... <14.082.`             (4.3)

#### Proof

Equation (2.2), followed by (4.1) and (3.1), gives

`||p_Q||inf
 <= [8/3^(3/4)] |a|^(-1/2)
    [3^(3/2)e^(2/3)2^(-2/3) Z^(-1/9)]^(3/4).`

The powers simplify to `Z^(-1/12)` and the coefficient to

`8 * 3^(9/8-6/8) * e^(1/2) * 2^(-1/2)
 =4sqrt(2e)3^(3/8).`

QED.

This is an essential-density conclusion. The proof does not establish continuity of the final density: `phi_R in L^(3/2)` is insufficient for a continuous representative, and the dependence-safe square step is used only at the `L3 -> Linfinity` level.

## 5. Concrete splice into the current B06 transverse chamber

In the inherited B06 transverse notation, let the retained residual cross block have singular values

`h1>=h2>=h3>=...>=0`

and suppose

`h1 h2 > (4/5) G^2.`                                         (5.1)

Then

`Delta_3(B)
 >= h1^2 h2^2 h3^2
 > (16/25) G^4 h3^2.`                                        (5.2)

Therefore the old third-singular-value collar `h3>=G/64` implies

`Delta_3(B)>G^6/6400.`                                       (5.3)

Theorem 4.1 now gives the strengthened paid branch

`boxed(
 h3>=G/64
 => ||p_Q||infinity
 < 29.230 / sqrt(|a|G).
)`                                                                    (5.4)

Indeed

`14.08129836146 * 6400^(1/12)
 =29.22970048094...`.

The previous B06 ridge proof paid the same `h3>=G/64` branch by `<200/sqrt(|a|G)`. The new argument improves the constant by more than a factor six and, more importantly, uses the aggregate third-volume invariant rather than a worst single singular direction. The contrapositive remains honest: failure of the stronger volume payment `Delta_3>=G^6/6400` forces `h3<G/64` by (5.2), so the same explicit rank-two operator-norm tube survives with no tail deletion.

## 6. Application to the newest B08 third-volume packet

The fresh fleet03/B08 r27 proof begins from the diffuse compiler currency

`Delta_3(B) >= L^6/2304`

for an ORIGINAL-coordinate cross block `B`; canonical report:

`yspennstate/math-open-problems@e875d54d4a946d399466cb6afa1fc37da12a11d2`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T042303Z-fleet03-B08-qform-diffuse-r27/REPORT.md`.

B08 needs extra routing because it does not assume a separate square pivot. In the **B06 outer-pivot context**, however, Theorem 4.1 consumes that same third-volume packet immediately, without asking whether the normalized third-volume law has diffuse inclusion marginals and without routing through an anchored hub:

`boxed(
 ||p_Q||infinity
 <= 4sqrt(2e)3^(3/8) 2304^(1/12) / sqrt(|a|L)
 < 26.845 / sqrt(|a|L).
)`                                                                    (6.1)

The coefficient is `26.84414484630...`. This is an actual application to a live fleet currency. It does not claim that B08's no-outer-pivot branch is solved.

## 7. What this eliminates and what it does not

This run eliminates a broad higher-cross-rank obstruction **after a nonzero original-coordinate square pivot**:

* any residual cross block with positive aggregate third volume has an `L3` density without a leverage hypothesis;
* a dimension-free third-volume lower bound can be spent directly through the genuine square;
* in the transverse chamber, the prior `sigma_3` paid branch improves from `<200` to `<29.230` at the same collar;
* the aggregate is taken before every reciprocal power, consistent with the live local-minor/fiber-sup corrections.

It does **not** prove that an arbitrary three-large-eigenvalue matrix supplies a nonzero physical square `a` with a universally paid product `|a| Delta_3(B)^(1/6)`. Exact-rank-three forms typically leave only rank two after a scalar Schur pivot, so `Delta_3` of the residual may vanish; those branches require the already-developed rank-two/curved-pair mechanisms. Zero or near-zero outer physical pivots therefore remain a global debt.

The next exact B06 implication is sharpened to:

`QFORM-RANK2-TUBE-OR-ZERO-PIVOT-PRODUCT-PAYMENT-v1`:

inside the surviving `Delta_3<G^6/6400` / `h3<G/64` tube, combine the two-sided diffuse exterior information and original product structure to obtain either a rank-two aggregate `Delta_2` receiver with a fractional leverage/ridge gate, a grouped coordinate packet, or a paid nonzero scalar pivot. The tail must remain present until a source-valid stability estimate absorbs it.

## 8. Correction discipline and status

Consumed live corrections include: law-uniform pointwise quadratic-phase decay false; arbitrary-joint rank-three coarea false; conditional projection positive moments false; post-rotation independence false; unrestricted fiber sup dimension loss; one-good-minor / local-minor-before-aggregation failures; and small nonzero tails may not simply be discarded.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The universal continuous-density conclusion remains **OPEN**. Theorem 3.1 gives an `L3` density in its scope; Theorem 4.1 gives an essentially bounded density in its scope, not a proved continuous representative.
