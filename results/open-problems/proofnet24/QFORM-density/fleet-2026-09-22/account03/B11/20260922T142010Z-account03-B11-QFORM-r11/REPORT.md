# account03/B11 — zero-diagonal three-variable smoothing for indefinite signatures

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T142010Z-account03-B11-QFORM-r11`  
**Assignment:** Indefinite signatures  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full target remains: for every dimension, every independent real input coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample. Continuity is a separate stronger conclusion.

This report retains the original-coordinate product law. It does not use the refuted law-uniform pointwise van-der-Corput/Fresnel decay, does not rotate to eigen-coordinates and retain false independence, does not use a naive fiber supremum, and does not infer a global good principal minor from the spectral hypothesis.

The previous account03/B11 run proved a determinant-scale half-potential estimate for arbitrary binary indefinite quadratics and, with a completed square in a nonzero physical scalar pivot, obtained the majority-sign estimate

`||p_Q||_infinity <= 8 / |c det B|^(1/4)`

for a physical invertible indefinite `3x3` block `B` when the pivot `c` has the majority sign. The completed account04/B18 result gives the complementary definite-Schur/minority-sign bound

`||p_Q||_infinity <= 2 sqrt(pi) / |c det B|^(1/4)`.

Both estimates become useless when the selected physical diagonal pivot tends to zero. The exact zero-pivot geometry is not singular, however: a fully off-diagonal block such as the triangle matrix has eigenvalues `2,-1,-1`. This run attacks that missing local implication directly.

## 2. Completed compatible peer result actually applied

The designated partner is `account04/B11`. At both fresh-main checks in this run there was still no completed QFORM handoff or canonical report from that exact slot, so none is invented.

A completed compatible other-account result is applied in the local branch synthesis below:

- `account04/B18`, canonical scientific source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its proved physical-triple inequality is

`||p_Q||_infinity <= 2 sqrt(pi) / |c det B|^(1/4)`

when a nonzero scalar pivot `c` has definite `2x2` Schur complement. Section 8 combines this exact inequality with the new zero-pivot theorem and the previous B11 majority-sign theorem.

## 3. A concentration lemma for a square under an unnormalized cap

Let `w` be a nonnegative integrable function on `R` with

`||w||_infinity <= M`.

Let `mu` be the pushforward of the finite measure `w(y)dy` under

`y -> kappa (y-y0)^2 + tau`,

where `kappa != 0`. For every measurable `E subset R` of finite Lebesgue measure `|E|`,

`mu(E) <= 2 M sqrt(|E|/|kappa|)`.                                      (3.1)

**Proof.** Translations of `y` and of the output do not matter, and reflection handles negative `kappa`. For `s=kappa y^2`, the total Lebesgue measure of the preimage of a measurable positive-output set `E` is

`|kappa|^(-1/2) integral_E s^(-1/2) ds`.

By decreasing rearrangement, among sets of length `L` this is maximized by `[0,L]`, giving `2 sqrt(L/|kappa|)`. Multiplication by the cap `M` proves (3.1). QED.

This lemma is deliberately about arbitrary measurable sets, not intervals; fragmented input supports are therefore retained.

## 4. Square plus an independent linear coordinate

Let the finite measure in Lemma 3.1 have total mass `m`, and let `Z` have a probability density `h<=1`, independent of the square variable. For `ell != 0`, let `r_ell` be the density of

`kappa (Y-y0)^2 + 2 ell Z`

under the product measure `w(y)dy h(z)dz`.

Then

`||r_ell||_infinity <= min( m/(2|ell|), sqrt(2) M/(sqrt(|kappa|) sqrt(|ell|)) ).`     (4.1)

**Proof.** The pushforward of `Z` under `z -> 2 ell z` has a probability density `k_ell` satisfying

`0 <= k_ell <= K := 1/(2|ell|)`.

The trivial convolution estimate gives `||r_ell||_infinity <= K m`.

For the second estimate, write by layer cake, for fixed output level `t`,

`r_ell(t) = integral_0^K mu({s : k_ell(t-s)>q}) dq`.

Using (3.1), then Cauchy-Schwarz in `q`,

`r_ell(t)
 <= (2M/sqrt(|kappa|)) integral_0^K |{k_ell>q}|^(1/2) dq
 <= (2M/sqrt(|kappa|)) [ K integral_0^K |{k_ell>q}| dq ]^(1/2)`.

The layer-cake identity for `k_ell` gives

`integral_0^K |{k_ell>q}| dq = integral k_ell = 1`.

Therefore

`r_ell(t) <= 2M sqrt(K/|kappa|)
             = sqrt(2) M/(sqrt(|kappa|) sqrt(|ell|))`.

This proves (4.1). QED.

The key point is the gain from `|ell|^-1` to the integrable singularity `|ell|^-1/2` near the hyperbolic coefficient `ell=0`.

## 5. Main theorem: an invertible physical triple with a zero diagonal pivot

Consider a real symmetric matrix

`B = [[a,b,u],
      [b,d,v],
      [u,v,0]]`

with `det B != 0`. Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Allow arbitrary affine terms as well:

`Q = [X,Y,Z] B [X,Y,Z]^T + rX+sY+hZ+k`.                     (5.1)

### Theorem 5.1 — `QFORM-ZERO-PIVOT-DET-SMOOTHING-v1`

The law of `Q` has a **continuous** density satisfying

`boxed( ||p_Q||_infinity <= 3 * 2^(2/3) * |det B|^(-1/3) ).`             (5.2)

No sign condition on `B` is needed beyond invertibility. In particular it applies to the genuinely indefinite signatures `(2,1)` and `(1,2)`.

### Proof

Because `det B != 0`, at least one of `u,v` is nonzero. Interchanging `X` and `Y` if needed, assume `u != 0`.

Define the physical linear coefficient of `Z`

`ell = u x + v y + h/2`.

Use `(ell,y,z)` as coordinates, so

`x = (ell-h/2-vy)/u`,     `dx dy dz = |u|^(-1) d ell dy dz`.

The product density becomes

`w_ell(y) h_Z(z)`,

where

`w_ell(y) = |u|^(-1) f_X((ell-h/2-vy)/u) f_Y(y)`.

Thus, for every `ell`,

`0 <= w_ell <= M := 1/|u|`,

and if

`m(ell)=integral w_ell(y)dy`,

then `m` is the density of `uX+vY+h/2`, hence

`integral_R m(ell) d ell = 1`.                                          (5.3)

Substituting `x=(ell-h/2-vy)/u` into (5.1), all terms not containing `z` form a quadratic polynomial in `y` whose quadratic coefficient is

`kappa = d - 2bv/u + a v^2/u^2
       = - det(B)/u^2`.                                                   (5.4)

Since `det B != 0`, `kappa != 0`. For each fixed `ell`, completing the square in `y` gives

`Q = 2 ell z + kappa (y-y_ell)^2 + tau(ell)`,                            (5.5)

for deterministic functions `y_ell,tau(ell)`; their explicit lower-order forms are irrelevant. Translating `y` by `y_ell` preserves the cap `M` and the mass `m(ell)` of the unnormalized `y`-density.

For every `ell != 0`, Lemma 4.1 therefore gives a continuous conditional pushforward density `r_ell` with

`r_ell(t) <= min( m(ell)/(2|ell|),
                  sqrt(2)/( |u| sqrt(|kappa|) sqrt(|ell|) ) ).`          (5.6)

By (5.4),

`|u| sqrt(|kappa|) = sqrt(|det B|)`.                                     (5.7)

Consequently, for every `L>0`, Tonelli and (5.3) give

`p_Q(t)
 <= integral_{|ell|<=L} sqrt(2)/(sqrt(|det B|) sqrt(|ell|)) d ell
    + integral_{|ell|>L} m(ell)/(2|ell|) d ell`

`<= 4 sqrt(2) |det B|^(-1/2) sqrt(L) + 1/(2L).`                         (5.8)

Set

`A0 = 4 sqrt(2) |det B|^(-1/2)`.

The right side of (5.8) is `A0 sqrt(L)+1/(2L)`. Its minimum occurs at

`L=A0^(-2/3)`,

and equals

`(3/2) A0^(2/3)
 = 3 * 2^(2/3) |det B|^(-1/3)`,

which proves (5.2).

It remains to justify the claimed continuity. For each `ell != 0`, the square pushforward of the absolutely continuous finite measure `w_ell(y)dy` has an `L^1` density, and the pushforward of `Z` under `2ell Z` has an `L^1` density. Their convolution `r_ell` is therefore continuous. Fix the optimizing `L`; the right side of (5.6), using the first term outside `[-L,L]` and the second term inside, is an integrable dominating function of `ell`, with integral bounded by (5.8). Hence dominated convergence in (5.5) shows that `p_Q(t)=integral r_ell(t-tau(ell))dell` is continuous in `t`. QED.

## 6. Ambient conditional version

Let an arbitrary-dimensional symmetric matrix `A` have a physical principal `3x3` block `B` of the form in Theorem 5.1. Condition every original coordinate outside that triple. Outside variables add only affine and constant terms to the triple polynomial, while the quadratic block remains exactly `B`. Theorem 5.1 is uniform in all affine terms. Therefore every conditional output law has a continuous density bounded by the same constant in (5.2).

Averaging the conditional densities gives

`||p_{X^T A X}||_infinity <= 3*2^(2/3)|det B|^(-1/3)`.                  (6.1)

Since the conditional representatives are continuous and uniformly bounded, dominated convergence in the outside conditioning variable also gives a continuous representative for the full output density.

Thus a single invertible physical principal triple with a zero scalar diagonal is a complete bounded-and-continuous-density branch, with no assumption on any other coordinates, eigenvalues, or outside couplings.

## 7. Genuinely rotated indefinite example

Take the fully off-diagonal triangle matrix

`B_triangle = [[0,1,1],
               [1,0,1],
               [1,1,0]].`

Its eigenvalues are exactly `2,-1,-1`, so it satisfies the owner's three-large-eigenvalue threshold and has signature `(1,2)`. It is not diagonal in the physical independent coordinates, and every diagonal pivot is exactly zero. Also

`det B_triangle = 2`.

Theorem 5.1 therefore gives, for every independent input law with marginal densities at most one,

`||p_{2(XY+XZ+YZ)}||_infinity
 <= 3*2^(2/3)*2^(-1/3)
 = 3*2^(1/3)
 < 3.780.`                                                              (7.1)

The density is continuous.

This is a strict target-level three-eigenvalue, rotated, indefinite example that neither the nonzero-scalar-pivot estimate nor a diagonal argument covers directly.

## 8. Applying the completed account04/B18 inequality: local branch synthesis

Let `B` be any invertible physical indefinite `3x3` block.

1. If a chosen nonzero diagonal pivot `c` has **definite** Schur complement, the completed account04/B18 result applies directly and gives

   `||p_Q||_infinity <= 2 sqrt(pi) / |c det B|^(1/4)`.                  (8.1)

   In inertia `(2,1)` or `(1,2)`, this is the minority-sign scalar-pivot branch.

2. If a chosen nonzero diagonal pivot has **indefinite** Schur complement, the previous account03/B11 half-potential theorem gives

   `||p_Q||_infinity <= 8 / |c det B|^(1/4)`.                           (8.2)

   This is the majority-sign scalar-pivot branch.

3. If all available scalar pivots in the desired coordinate position vanish, Theorem 5.1 supplies the missing exact-zero branch

   `||p_Q||_infinity <= 3*2^(2/3)|det B|^(-1/3)`.                       (8.3)

Hence the local three-variable analytic mechanism no longer fails *because the physical pivot is exactly zero*. The remaining obstruction is quantitative and global: (8.1)-(8.2) are not uniform as a nonzero physical diagonal tends to zero, and the global three-large-eigenvalue hypothesis does not force a single well-conditioned physical principal triple. No claim of full closure is made.

## 9. How the third direction removes the rank-two logarithmic singularity

The rank-two opposite-sign control is retained. For example, with independent unit-density uniforms near zero, a product/hyperbolic form such as `XY` has a logarithmically divergent density at zero. A bound based only on the affine `Z`-fiber would produce the nonintegrable factor `1/|ell|` when its coefficient `ell=uX+vY` is small.

The third nondegenerate direction contributes the residual square coefficient

`kappa = -det B/u^2`.

Near `ell=0`, concentration of that square over arbitrary fragmented sets replaces the bad `1/|ell|` fiber cap by

`1/(sqrt(|det B|) sqrt(|ell|))`,

which is integrable. Away from zero, the original linear fiber cap contributes an integrable tail after weighting by the actual density `m(ell)`. Optimizing the crossover produces the determinant scale `|det B|^(-1/3)`.

If `det B` collapses to zero, then `kappa` vanishes and this repair disappears, consistently recovering the rank-two logarithmic obstruction. Thus the theorem identifies an exact real-space mechanism, rather than a false pointwise Fourier decay, by which the third direction removes the singularity.

## 10. Verification and scope

A standard-library checker accompanying this report verifies the algebraic identity

`kappa=-det(B)/u^2`,

the transformed polynomial for random integer coefficients and points, the optimization constant in (5.8), and the triangle certificate `spec(B_triangle)={2,-1,-1}`, `det=2` via its characteristic polynomial.

The theorem itself is analytic; finite checks are regression evidence, not proof.

### What is proved

- exact zero-diagonal physical-pivot branch for every invertible `3x3` quadratic block;
- arbitrary independent input densities bounded by one;
- arbitrary affine terms from conditioning outside the block;
- explicit dimension-free conditional bound `3*2^(2/3)|det B|^(-1/3)`;
- continuous density in this branch;
- a strict fully rotated target example with eigenvalues `2,-1,-1` and bound `<3.780`;
- an explicit synthesis with the completed account04/B18 definite-Schur inequality.

### What is not proved

- the full universal conjecture for arbitrary `A`;
- a uniform passage through *small but nonzero* physical diagonal pivots;
- a dimension-free extraction/aggregation theorem producing a quantitatively usable physical block from merely three spectral eigenvalues;
- a completed result from designated partner `account04/B11`, which was absent from fresh main during this run.

The next B11 implication should attack the small-nonzero-pivot transition without discarding the fixed `Z`-density translation information. The discriminant-only half-potential estimate loses precisely that information and blows like `|c|^-1/4`; the zero-pivot theorem shows the endpoint itself is finite, so a successful bridge must average the moving quadratic stationary point against the *same fixed independent* `Z` law rather than maximize separately in every fiber.
