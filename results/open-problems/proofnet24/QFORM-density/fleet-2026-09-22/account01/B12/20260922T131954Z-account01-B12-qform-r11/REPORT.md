# account01/B12 — additional-eigenvalue control by low-leverage vertex-cover absorption

**Run:** `20260922T131954Z-account01-B12-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 1. Full target and source state

The full conjecture remains OPEN: for independent real coordinates with densities bounded by one and a real symmetric matrix having at least three eigenvalues of absolute value at least one, prove one dimension-independent bound on the output density of `X^T A X` (and separately determine whether a continuous representative always exists).

This run used the current source state from `yspennstate/math-research-brain@0f7fa82fc244a9777494310295edbce82f9d5c45`, after an initial coherent read at `38452179b0badfe9fe8774e103bf62bbb5453ad2`. The live correction inbox still contains the pointwise-decay, fiber-supremum, cross-minor, conditional-cap, single-Schur-extraction, absolute-ambiguity/Hölder and bounded-diameter-localization failures. None is used below.

Two source theorems are applied exactly:

1. **Diffuse separable-phase theorem**: `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`. If `U^T U=I_r`, `r>=3`, every row leverage is at most `1/2`, and `Lambda` is invertible symmetric, then

   `T=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`

   has a bounded continuous density and

   `||p_T||_infinity <= [r/(r-2)] B(U)^(2/r) |det Lambda|^(-1/r) <= [e r/(r-2)] |det Lambda|^(-1/r)`.

   The proof is uniform in arbitrary measurable coordinate-separable phases `V_i`, and its characteristic-function envelope is integrable.

2. **Partner account02/B12 codimension-one same-sign theorem**: `yspennstate/math-open-problems@5924039504a3f27bdfa9079c4d054422a26baaf2:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/account02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`. A symmetric `m x m` matrix (`m>=4`) with at least `m-1` eigenvalues all `>=L` or all `<=-L`, the last eigenvalue arbitrary, gives under independent density-`<=1` inputs and arbitrary affine tilt

   `||p||_infinity <= C_same/L`,

   where

   `C_same=max{pi sqrt(1000/17), (2000/949)(2 pi+3 sqrt(3))}<24.193`.

The second theorem is applied in Section 5, not merely cited.

## 2. New theorem: arbitrary nonseparable perturbations with a low-leverage vertex cover

### Theorem A — `QFORM-LOW-LEVERAGE-VERTEX-COVER-ABSORPTION-v1`

Let `U` be an `n x r` real matrix with `U^T U=I_r`, `r>=3`, and let `Lambda` be an invertible real symmetric `r x r` matrix. Write the rows of `U` as `u_i^T`.

Choose a set of original coordinate indices `S subset [n]`, put `T=S^c`, and define

`H = U_S^T U_S`,  `G = I_r-H = U_T^T U_T`.

Assume `G` is positive definite and

`u_i^T G^{-1} u_i <= 1/2` for every `i in T`.                    (2.1)

Let `R` be an arbitrary real symmetric `n x n` matrix satisfying

`R_{T,T}` is diagonal.                                            (2.2)

Equivalently, `S` is a vertex cover of the off-diagonal support graph of `R`: every nonzero off-diagonal entry of `R` touches at least one coordinate in `S`.

For independent real `X_i` with probability densities `0<=f_i<=1`, set

`Q = X^T (U Lambda U^T + R) X`.

Then `Q` has a bounded continuous density vanishing at infinity, and

`||p_Q||_infinity <= [r/(r-2)] B(U_T G^{-1/2})^(2/r)
                      * [det(G) |det Lambda|]^(-1/r)`             (2.3)

and therefore

`||p_Q||_infinity <= [e r/(r-2)] [det(G)|det Lambda|]^(-1/r)`.    (2.4)

If `rho=||H||_op<1`, then `det(G)>=(1-rho)^r`, hence

`||p_Q||_infinity <= [e r/((r-2)(1-rho))] |det Lambda|^(-1/r)`.   (2.5)

No bound at all is imposed on the size, rank, sign pattern or eigenvalues of `R`; only the structural condition (2.2) and the retained-frame condition (2.1) are required. In particular the added matrix may introduce arbitrarily many additional eigenvalues of either sign and arbitrarily large magnitude.

### Proof

Condition on the coordinates `X_S=z`. Write `y=X_T`. Because the original coordinates are independent, the conditional variables `y_i`, `i in T`, retain their original independent density-`<=1` laws.

Expand the low-rank core:

`U^T X = U_T^T y + U_S^T z`,

so

`(U^T X)^T Lambda(U^T X)
 = y^T U_T Lambda U_T^T y
   + 2 y^T U_T Lambda U_S^T z
   + z^T U_S Lambda U_S^T z`.                                    (2.6)

By (2.2), the `T x T` part of `R` is diagonal. Hence all remaining contributions of `R` after conditioning are a diagonal quadratic function of the individual `y_i`, an arbitrary linear tilt in `y`, and a scalar depending on `z`. Thus the conditional quadratic form has exactly the shape

`Q_z(y)= y^T U_T Lambda U_T^T y + sum_{i in T} V_{i,z}(y_i)+c(z)`, (2.7)

where every `V_{i,z}` is a one-coordinate real quadratic-plus-linear function. The coefficients may depend arbitrarily on `z`; this causes no loss because the source theorem is uniform over all separable phases.

Now whiten the retained frame. Since `G=U_T^T U_T` is positive definite, put

`U_tilde = U_T G^{-1/2}`,
`Lambda_tilde = G^{1/2} Lambda G^{1/2}`.                           (2.8)

Then

`U_tilde^T U_tilde = I_r`,                                        (2.9)

and

`U_T Lambda U_T^T = U_tilde Lambda_tilde U_tilde^T`.             (2.10)

For each retained coordinate,

`c_tilde_i = ||u_i^T G^{-1/2}||_2^2 = u_i^T G^{-1}u_i <= 1/2`    (2.11)

by assumption. Also

`|det Lambda_tilde| = det(G) |det Lambda|`.                        (2.12)

Therefore the diffuse separable-phase theorem applies to every conditional law `Q_z`, giving the uniform characteristic-function estimate

`|phi_z(t)| <= min{1,
  B(U_tilde) pi^(r/2)
  [det(G)|det Lambda|]^(-1/2) |t|^(-r/2)}`.                       (2.13)

The right-hand side is independent of `z` and integrable because `r>2`. Averaging the conditional characteristic functions yields the unconditional characteristic function `phi_Q`; hence the same integrable envelope holds for `phi_Q`. Fourier inversion therefore gives a bounded continuous density vanishing at infinity and yields (2.3). The bound `B(U_tilde)<=exp(r/2)` gives (2.4).

Finally, `0<=H<=rho I`, so `G=I-H >= (1-rho)I`. Thus `det G >= (1-rho)^r`, proving (2.5). QED.

## 3. Trace-leverage corollaries

Put `c_i=||u_i||_2^2` and

`tau_S = sum_{i in S} c_i = tr(H)`.

Because `H` is positive semidefinite,

`rho=||H||_op <= tr(H)=tau_S`.                                    (3.1)

Hence a convenient sufficient condition for (2.1) is

`tau_S<1` and `max_{i in T} c_i <= (1-tau_S)/2`.                  (3.2)

Indeed `G >= (1-tau_S)I`, so

`u_i^T G^{-1}u_i <= c_i/(1-tau_S) <= 1/2`.                       (3.3)

Under (3.2), Theorem A gives

`||p_Q||_infinity <= [e r/((r-2)(1-tau_S))]
                      |det Lambda|^(-1/r)`.                       (3.4)

For rank `r=3` and `|det Lambda|>=1`, this becomes

`||p_Q||_infinity <= 3e/(1-tau_S)`.                               (3.5)

A concrete diffuse-rank consequence uses the currently important leverage scale `c_i<=1/12`. If the off-diagonal support graph of the added remainder has a vertex cover `S` satisfying

`tau_S <= 5/6`,                                                    (3.6)

then every retained leverage obeys

`c_i/(1-tau_S) <= (1/12)/(1/6)=1/2`,

and therefore

`||p_Q||_infinity <= 18e |det Lambda|^(-1/3)`.                    (3.7)

If instead `tau_S<=1/2`, the sharper bound is

`||p_Q||_infinity <= 6e |det Lambda|^(-1/3)`.                     (3.8)

Thus the separable-phase theorem survives a genuinely nonseparable perturbation whenever all of its nonseparable interactions can be covered by coordinates carrying sufficiently little mass of the diffuse spectral frame.

## 4. What “additional eigenvalues” are actually controlled

The theorem does **not** assert that the eigenvalues of the perturbation are small. It allows:

- arbitrary diagonal entries on every coordinate;
- an arbitrary symmetric block on `S x S`;
- arbitrary cross-couplings `S x T`;
- hence arbitrarily many added eigenvalues, of either sign and of arbitrarily large magnitude.

The restriction is geometric rather than spectral: outside `S`, the perturbation must be coordinate-separable. This is exactly what conditioning on the original coordinates in `S` can absorb without destroying the product structure needed by the Brascamp-Lieb/Hausdorff-Young argument.

The whitening loss is explicit and only depends on the spectral mass of the diffuse frame removed by the conditioning set through `G=I-U_S^T U_S`.

## 5. Actual application of the named partner theorem

The account02/B12 theorem gives a complementary stability certificate that does not require a diffuse representation.

### Corollary B — physical-block codimension-one transfer

Let `I subset [n]`, `|I|=m>=4`. Suppose the physical principal block `A_{I,I}` has at least `m-1` eigenvalues all `>=L` or all `<=-L`; its remaining eigenvalue is arbitrary. Then for independent density-`<=1` coordinates,

`||p_{X^T A X}||_infinity <= C_same/L < 24.193/L`.                (5.1)

**Derivation.** Condition on every original coordinate outside `I`. The conditional form on `X_I` has quadratic matrix exactly `A_{I,I}`; every outside cross-coupling becomes an affine tilt. The partner theorem is uniform over affine tilts, so every conditional density has cap `C_same/L`. Averaging the conditional laws gives (5.1). This is a direct use of the partner theorem in the full matrix, not a spectral-rotation independence claim.

### Perturbative version

Suppose `B_{I,I}` has at least `m-1` same-sign eigenvalues with magnitude at least `L`, and let `F` be any symmetric perturbation with

`||F_{I,I}||_op <= delta L`, `0<=delta<1`.                         (5.2)

Set `A=B+F`, with **no restriction whatsoever** on `F` outside the `I x I` principal block. Weyl's inequality gives at least `m-1` eigenvalues of `A_{I,I}` of the same sign and magnitude at least `(1-delta)L`. Therefore Corollary B yields the explicit inequality

`||p_{X^T A X}||_infinity
   <= C_same/[(1-delta)L]
   < 24.193/[(1-delta)L]`.                                        (5.3)

All additional eigenvalues and all couplings outside the certified block may be smaller, larger, positive or negative. This is the requested partner result applied to an actual stability inequality.

The partner route proves an essentially bounded density at the scope stated in its source. The stronger continuous-density conclusion is established in Theorem A because there the characteristic function itself has a uniform integrable envelope.

## 6. Relation to the full conjecture and exact unpaid implication

These two mechanisms now control two broad kinds of spectral additions:

1. **localized nonseparable additions to a diffuse core** — Theorem A permits an arbitrary perturbation whose off-diagonal interaction graph has a sufficiently low-leverage vertex cover;
2. **arbitrary completions of a codimension-one same-sign physical block** — Corollary B and (5.3) permit every outside eigenvalue and coupling once one physical block has the partner spectral certificate.

Neither mechanism proves that every target matrix with merely three eigenvalues of absolute value at least one admits one of these decompositions. A generic dense nonseparable remainder may have no low-leverage vertex cover, while a rank-three delocalized core may have no uniformly curved fixed principal block. The full conjecture therefore remains OPEN.

The first essential missing implication for this assignment is now:

> Starting only from three large spectral directions, either produce a product-preserving decomposition whose nonseparable remainder has a low-leverage vertex cover (so Theorem A applies), or prove a genuinely nonseparable analogue of the diffuse Fourier/Brascamp-Lieb estimate that does not require coordinate-factorization after conditioning.

The present theorem makes the obstruction quantitative: conditioning on a set `S` costs exactly the whitening matrix `G=I-U_S^T U_S`, with an explicit sufficient loss `1/(1-tau_S)`. Any next reduction can therefore be judged against a concrete leverage budget rather than the vague requirement that the remainder be “small.”

## 7. Correction and integrity check

The proof never uses:

- a law-uniform pointwise van-der-Corput estimate;
- independence after rotating to an eigenbasis;
- a fiber-supremum bound;
- a bare cross-minor criterion;
- a conditional density cap as a substitute for independence;
- a single Schur pivot extraction;
- an interval/localization extremizer.

All conditioning is on original independent coordinates. All nonseparable terms remaining after conditioning are linear or scalar; the retained quadratic perturbation is genuinely coordinate-separable. The determinant and leverage losses are exact identities.

**Status:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`. No claim of a full solution or publication novelty is made.
