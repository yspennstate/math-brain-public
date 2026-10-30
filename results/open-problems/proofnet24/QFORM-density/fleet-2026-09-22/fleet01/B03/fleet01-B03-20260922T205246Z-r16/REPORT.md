SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-22T20:52:46Z.
attacking: the zero-diagonal physical-triple branch via an exact product-preserving linear/square interpolation, using the latest fleet02/B03 square L3 estimate.

# fleet01/B03 r16 — zero-diagonal physical triple by product-preserving L3 interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  

## 1. Exact target and correction boundary

The full owner target is unchanged: for arbitrary independent original-coordinate real inputs with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free essential bound for the density of `Q=X^TAX`, or give a valid target counterexample. Continuity is a separate desired conclusion.

This report does **not** use law-uniform pointwise Fresnel decay, post-rotation independence, the false arbitrary-joint rank-three coarea lemma, a positive conditional projection-density moment, a worst-fiber scalar bound, or the refuted assertion that one uniformly good physical minor must exist. It also respects `QFORM-SEMIPRODUCT-CAP-ONLY-FALSE-v1`: the proof below uses the exact algebraic image of the original product density, not merely an arbitrary two-dimensional cap.

The designated partner result actually applied is fleet02/B03 run `20260922T201216Z-fleet02-B03-QFORM-r12`, canonical mathematics

`yspennstate/math-open-problems@d205dc643b8d2439efdbbe986f93ea8b4f2933f5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T201216Z-fleet02-B03-QFORM-r12/REPORT.md`.

I use its proved Lemma 2.1: if a scalar random variable `S` has a probability density bounded by `M`, then for every nonzero `kappa`, the density of `kappa S^2` satisfies

`||p_(kappa S^2)||_(3/2) <= 2 M^(2/3) |kappa|^(-1/3)`.              (1.1)

This is a genuine use below, not a citation-only dependency.

## 2. New local theorem

### Theorem 2.1 — `QFORM-ZERO-DIAGONAL-TRIPLE-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let `b,c,d` be nonzero and let arbitrary affine terms be allowed. Define

`Q = 2bXY + 2cXZ + 2dYZ + ell_1 X + ell_2 Y + ell_3 Z + q_0`.       (2.1)

Put

`M = max{|b|,|c|,|d|}`.                                               (2.2)

Then `Q` has an essentially bounded density and

`boxed{
 ||p_Q||_infinity <= 4 sqrt(2) ( |b c d| M )^(-1/4).
}`                                                                       (2.3)

No compact support, connected support, moments, symmetry, log-concavity, or regularity of the input densities is assumed.

### Corollary 2.2 — well-conditioned zero-diagonal physical triple

Let

`B = [[0,b,c],[b,0,d],[c,d,0]]`                                      (2.4)

and suppose `sigma_min(B)>=s>0`. Then for arbitrary independent cap-one inputs and arbitrary affine terms,

`boxed{
 ||p_(x^T B x + ell^T x + q_0)||_infinity
 <= 4 * 2^(7/8) / s
 < 7.337 / s.
}`                                                                       (2.5)

Consequently, if an ambient quadratic form has an ORIGINAL-coordinate principal triple `I` whose physical block is zero-diagonal and satisfies `sigma_min(A[I,I])>=s`, then conditioning on all coordinates outside `I` proves the same ambient bound (2.5). Outside quadratic terms and outside couplings merely generate an affine perturbation in the conditioned triple.

This is an essential-density statement. **Continuity is not claimed.**

## 3. Affine terms are harmless here

Because `b c d !=0`, the matrix `B` in (2.4) is invertible with

`det B = 2 b c d`.                                                     (3.1)

For the affine form `x^T B x + ell^T x + q_0`, put

`h = (1/2) B^(-1) ell`.

Then

`x^T B x + ell^T x + q_0 = (x+h)^T B (x+h) + constant`.              (3.2)

The coordinatewise translation `x_i -> x_i+h_i` preserves independence and every density cap. Hence it suffices to prove Theorem 2.1 with all affine terms zero.

## 4. Exact product-preserving coordinates

Fix the `X` coordinate and define

`L = bY + cZ`,
`S = bY - cZ`,
`kappa = d/(2bc)`.                                                     (4.1)

Then

`Y = (L+S)/(2b)`, `Z=(L-S)/(2c)`,                                    (4.2)

and the exact quadratic identity is

`Q = 2 L X + kappa (L^2-S^2)`.                                      (4.3)

The joint density of `(L,S)` is not arbitrary. It is exactly

`rho(l,s)
 = [1/(2|bc|)]
   f_Y((l+s)/(2b)) f_Z((l-s)/(2c))`.                                 (4.4)

Therefore

`0<=rho<=K`, `K=(2|bc|)^(-1)`.                                      (4.5)

Let

`m(l)=int rho(l,s) ds = p_L(l)`.                                    (4.6)

Because `L=bY+cZ`, simple conditioning on `Z` and separately on `Y` gives

`m(l) <= min{|b|^(-1),|c|^(-1)}
       = P`,
`P = 1/max{|b|,|c|}`.                                                (4.7)

This extra exact marginal bound is where the original product provenance is retained. It is not available for an arbitrary two-dimensional cap-one law.

For almost every `l` with `m(l)>0`, the conditional density of `S` given `L=l` is

`g_l(s)=rho(l,s)/m(l)`, hence

`||g_l||_infinity <= K/m(l)`.                                        (4.8)

Since `X` is independent of `(Y,Z)`, it remains independent of `S` after conditioning on `L=l`, and its law is unchanged.

## 5. Two complementary conditional density bounds

Fix `l !=0`. Up to the additive shift `kappa l^2`, the conditional random variable is

`T_l = 2l X - kappa S^2`.                                            (5.1)

### 5.1 Linear cap

The density of `2lX` is bounded by

`||p_(2lX)||_infinity <= 1/(2|l|)`.                                  (5.2)

Convolution with the independent `-kappa S^2` cannot increase the `L^infinity` norm, so

`||p_(T_l)||_infinity <= 1/(2|l|)`.                                  (5.3)

### 5.2 Partner-assisted `L^{3/2} * L^3` bound

Apply fleet02/B03 Lemma 2.1 to the conditional density `g_l`, whose cap is `K/m(l)`. The density `v_l` of `-kappa S^2` obeys

`||v_l||_(3/2)
 <= 2 [K/m(l)]^(2/3) |kappa|^(-1/3)`.                               (5.4)

The density `h_l` of `2lX` satisfies, since `0<=f_X<=1` and `int f_X=1`,

`||h_l||_3
 = (2|l|)^(-2/3) ||f_X||_3
 <= (2|l|)^(-2/3)`.                                                   (5.5)

Young's sharp exponent relation `1/(3/2)+1/3=1` gives

`||p_(T_l)||_infinity
 <= ||v_l||_(3/2) ||h_l||_3`
` <= 2^(1/3) [K/m(l)]^(2/3)|kappa|^(-1/3)|l|^(-2/3)`.               (5.6)

Multiplying by the mixing density `m(l)` and using (4.5) and (4.1), the constants collapse exactly:

`2^(1/3) K^(2/3)|kappa|^(-1/3)
 = |bcd|^(-1/3)`.                                                     (5.7)

Thus the contribution at level `l` is bounded by the minimum of

`m(l)/(2|l|)`                                                        (5.8)

and

`|bcd|^(-1/3) m(l)^(1/3)|l|^(-2/3)`.                                (5.9)

This is the decisive gain: the first bound controls large `|l|`, while the partner-assisted second bound is locally integrable at `l=0`.

## 6. Integrate the moving linear coefficient

For every `R>0`, use (5.9) on `|l|<=R` and (5.8) outside. From `m(l)<=P`,

`||p_Q||_infinity`
` <= |bcd|^(-1/3) P^(1/3)
      int_{|l|<=R} |l|^(-2/3) dl
    + int_{|l|>R} m(l)/(2|l|) dl`
` <= 6 |bcd|^(-1/3) P^(1/3) R^(1/3) + 1/(2R)`.                     (6.1)

Write

`G=|bcd|^(-1/3) P^(1/3)`.                                           (6.2)

The exact minimizer of `6 G R^(1/3)+1/(2R)` is

`R_*=(1/(4G))^(3/4)`.                                                (6.3)

Substitution gives

`min_R [6 G R^(1/3)+1/(2R)]
 =4 sqrt(2) G^(3/4)`.                                                (6.4)

Since `P=1/max{|b|,|c|}`, this proves, for the chosen `X` coordinate,

`||p_Q||_infinity
 <= 4sqrt(2) [|bcd| max{|b|,|c|}]^(-1/4)`.                          (6.5)

Permute the three coordinates so that the selected row is incident to an edge of maximal magnitude `M=max{|b|,|c|,|d|}`. Then `max{|b|,|c|}=M`, proving (2.3).

Absolute continuity follows from the conditional mixture: `L` has an ordinary density, so `P(L=0)=0`; for every `l!=0`, `T_l` has an absolutely continuous law because of the nonzero linear `2lX` term. The integrable uniform majorant above yields the essential density bound.

## 7. Spectral scaling of the zero-diagonal triple

If `sigma_min(B)>=s`, then

`|det B| = 2|bcd| >= s^3`,                                          (7.1)

so

`|bcd| >= s^3/2`.                                                    (7.2)

Also every row of `B` has Euclidean norm at least `s`, because

`||B e_i|| >= s ||e_i|| =s`.                                        (7.3)

Every row contains two of `b,c,d`, hence the global maximum `M` satisfies

`M >= s/sqrt(2)`.                                                     (7.4)

Therefore

`|bcd| M >= s^4/(2sqrt(2))`.                                        (7.5)

Insert this into (2.3):

`||p_Q||_infinity
 <= 4sqrt(2) (2sqrt(2))^(1/4) s^(-1)
 =4*2^(7/8) s^(-1)
 <7.337 s^(-1)`.                                                      (7.6)

This proves Corollary 2.2.

## 8. Why this is not the refuted cap-only semiproduct route

The live correction `QFORM-SEMIPRODUCT-CAP-ONLY-FALSE-v1` shows that an arbitrary independent scalar times an arbitrary dependent pair with only generic density caps does not suffice for an indefinite quadratic pushforward. The proof above uses two additional exact facts that come specifically from the original product source and this physical zero-diagonal algebra:

1. `(L,S)` has the exact product-image density (4.4), not a generic joint law;
2. its `L` marginal obeys the separate cap `m(l)<=1/max{|b|,|c|}`, and the quadratic phase has the exact mixed form `2LX+kappa(L^2-S^2)`.

The final estimate depends on both the joint cap `K` and this moving marginal `m(l)`, rather than replacing the pair by a worst conditional density. Thus the cited counterexample does not instantiate the hypotheses or algebra of Theorem 2.1.

## 9. Relation to the decoupled-time assignment

Previous B03 runs showed that an abstract rank-one endpoint splice from collision energies alone is false. This run therefore changes mechanism on the same target while retaining the integrated `L^3` ingredient supplied by fleet02/B03. The singular linear coefficient `L` is not bounded away from zero; instead the proof integrates it exactly. Near `L=0` it spends the square `L^{3/2}` budget from the partner result, while away from zero it spends the linear `L^infinity` budget. This is the physical-space dual of a mixed time-integrability argument and gives true linear small-ball scaling.

No pointwise law-uniform oscillatory decay is asserted.

## 10. Exact scope and remaining implication

Proved here:

- every invertible zero-diagonal physical `3 x 3` quadratic block with arbitrary affine perturbation has a universal density bound (2.3);
- if that block has `sigma_min>=s`, the clean constant is `<7.337/s`;
- the theorem persists inside an arbitrary ambient form after conditioning outside that original-coordinate triple;
- arbitrary fragmented cap-one input densities are allowed;
- only essential boundedness/absolute continuity is claimed, not continuity.

This does **not** prove the full conjecture. The first unpaid local implication is the **near-zero-diagonal bridge**: obtain a constant stable as the three physical diagonal entries tend to zero, rather than paying a reciprocal scalar pivot, or prove a product-preserving structural alternative that sends every three-large-eigenvalue matrix either to an already-paid pivot/ridge/cross-bank branch or to a quantitatively zero-diagonal triple of the type above. The bare three-large-eigenvalue hypothesis is not known to force a uniformly conditioned physical triple.

## 11. Status

- `QFORM-ZERO-DIAGONAL-TRIPLE-v1`: **PROVED**.
- ambient conditioned zero-diagonal-triple corollary: **PROVED**.
- continuous density for this branch: **NOT PROVED**.
- full QFORM universal theorem: **OPEN**.

The accompanying arithmetic checker verifies the exact constant simplification and the spectral scaling only; it is not used as a proof substitute.
