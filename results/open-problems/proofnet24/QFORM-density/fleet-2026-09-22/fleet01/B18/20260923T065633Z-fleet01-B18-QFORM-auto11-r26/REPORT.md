SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T06:56:33Z.
attacking: literature-to-proof transfer for the fresh tilted two-plane Schur-isotropic bank; replace the weaker zero-pivot payment by the completed fleet02/B18 scalar/dependent-pair theorem and track continuity separately.

# fleet01/B18 r26 — sharp tilted-two-plane bank transfer via fleet02/B18

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_SHARPENING / DESIGNATED_PARTNER_APPLIED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** established for this branch by the already-completed fleet03/B18 theorem; the new fleet02/B18 payment sharpens the essential bound, and therefore also the continuous representative pointwise.

## 1. Exact target and correction boundary

The owner target remains the unrestricted statement: for arbitrary independent real ORIGINAL coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite density bound for `X^T A X`. No moment, bounded-support, iid, log-concavity, Gaussian, smoothness, connected-support, or post-rotation-independence hypothesis may be added.

This run preserves the live corrections. In particular it does not use arbitrary-joint rank-three coarea, a positive moment/supremum of conditional projection densities, independence after spectral rotation, a law-uniform pointwise Fresnel estimate, coefficient deletion, or a universal good physical minor. Independence below comes only from conditioning complementary ORIGINAL coordinates and retaining the original scalar `X_0` versus an original-coordinate bank.


## 2. Primary theorem matched at its exact hypotheses

The external input is the primary theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1.

If `X=(X_1,...,X_m)` has product probability density `prod_i f_i`, with every `f_i` a probability density and `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. No moments, support restriction, iid hypothesis, log-concavity, or smoothness is assumed.

A consequence used below is the exact nonorthonormal two-dimensional version. Let `B` be an `m x 2` full-column-rank coefficient matrix and set `G=B^T B`. Factor `B=Q G^(1/2)` with `Q^TQ=I_2`. Then

`boxed: ||p_(B^T X)||_infinity <= 2 / sqrt(det G).`               (2.1)

This is only a joint density cap; no independence between the two image coordinates is asserted.

## 3. Completed designated partner theorem

The completed fleet02/B18 theorem is `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

Let `S` have density cap `K`, let `(C,D)` be genuinely independent of `S` and have an arbitrary joint density cap `M`, and let

`T=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`,             (3.1)

with `beta,gamma!=0`. Then

`boxed:
 ||p_T||_infinity
 <=3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`                       (3.2)

The pair coordinates may be dependent.

For later use, (3.2) has an equivalent coordinate-free zero-pivot form. If

`H=[[0,b^T],[b,C_2]]`                                             (3.3)

is an invertible symmetric `3 x 3` matrix, rotate only inside the two-dimensional pair so that `b=(beta,0)`. The pair density cap and scalar/pair independence are unchanged. In these coordinates

`det H=-beta^2 gamma`,                                            (3.4)

where `gamma` is the lower-right pair coefficient. Hence

`boxed:
 ||p_((S,Y)^T H(S,Y))||_infinity
 <=3(2MK)^(2/3)|det H|^(-1/3).`                                  (3.5)

Arbitrary deterministic affine terms cost nothing when `H` is invertible: translate the full active vector by `(1/2)H^(-1)ell`. This translates the scalar and the pair separately, preserving their density caps and their genuine independence, while leaving the quadratic matrix unchanged.

## 4. Fresh peer input: tilted two-plane Schur-isotropic bank

The newly completed fleet03/B18 r25 theorem is source

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T062246Z-fleet03-B18-QFORM-r25/REPORT.md`.

Its relevant exact setup is

`Q=(Y+r n X_0)^T D (Y+r n X_0)`,                                 (4.1)

where `D=D^T` is invertible, `||n||=1`,

`n^T D n=0`,                                                      (4.2)

`X_0` and all residual ORIGINAL coordinates are mutually independent and cap one, and

`Y=sum_j v_j X_j`, `sum_j v_j v_j^T=I_3`.                        (4.3)

Let `J` be a subset of residual ORIGINAL coordinates whose rows span exactly a two-plane `E`. Condition on all residual original coordinates outside `J`; this creates only deterministic affine terms in the active variables.

Let `U` be an orthonormal `3 x 2` basis of `E`, set

`G_J=U^T (sum_(j in J) v_j v_j^T) U`,
`g_J=det G_J>0`,                                                  (4.4)

let `m` be a unit normal to `E`, and put

`theta=|n^T m|>0`,
`Omega_J=g_J theta^2
       =sum_(i<j; i,j in J) det(n,v_i,v_j)^2.`                    (4.5)

Fleet03/B18 paid this branch with

`6*2^(2/3) [r^2 |det D| Omega_J]^(-1/3)`                         (4.6)

and proved continuity. The next section shows that the designated fleet02/B18 theorem gives the strictly sharper constant `3*4^(2/3)` at the same exact hypotheses.

## 5. New theorem — sharper tilted two-plane payment

### Theorem `QFORM-TILTED-TWOPLANE-FLEET02-SHARP-v1`

Under (4.1)--(4.5), including arbitrary affine terms generated by conditioning the complementary original-coordinate bank,

`boxed:
 ||p_Q||_infinity
 <=3*4^(2/3) [r^2 |det D| Omega_J]^(-1/3).`                       (5.1)

Numerically,

`3*4^(2/3)=7.559526299369239...`.                                 (5.2)

Moreover the density has a continuous representative, by the already-completed fleet03/B18 theorem on exactly the same branch; that representative obeys the sharper bound (5.1) pointwise.

### Proof

After conditioning the original coordinates outside `J`, write the active two-dimensional projection in the orthonormal basis `U` as

`Z=U^T sum_(j in J) v_j X_j`.                                    (5.3)

Its coefficient Gram matrix is `G_J`. By the primary LPP theorem in the form (2.1),

`M:=||p_Z||_infinity <=2/sqrt(g_J).`                              (5.4)

The scalar `X_0` is an untouched original coordinate, hence has density cap

`K<=1`,                                                           (5.5)

and is genuinely independent of the entire pair `Z`, because the pair uses only the disjoint original source block `J`.

The active spectral vector is

`r n X_0 + U Z + y_0`,                                           (5.6)

where `y_0` is fixed under the conditioning. Therefore the active quadratic matrix in coordinates `(X_0,Z_1,Z_2)` is

`H=R^T D R`, `R=[r n, U]`.                                       (5.7)

By (4.2),

`H_11=r^2 n^T D n=0`.                                            (5.8)

Because `theta>0`, the line `Rn` is transverse to `E`, so `R` is invertible. Hence `H` is invertible. Its determinant is exact:

`|det H|
 =|det D| det(R)^2
 =r^2 |det D| theta^2`.                                          (5.9)

All affine terms from `y_0` are removed by the invertible translation described after (3.5). We may therefore apply the designated fleet02/B18 theorem (3.5) with (5.4)--(5.5):

`||p_(Q | X_(J^c residual))||_infinity
 <=3 [2*(2/sqrt(g_J))*1]^(2/3)
      [r^2|det D|theta^2]^(-1/3)`
` =3*4^(2/3)
    [r^2 |det D| g_J theta^2]^(-1/3)`
` =3*4^(2/3)
    [r^2 |det D| Omega_J]^(-1/3).`                               (5.10)

The right side is independent of the conditioned values. Averaging the conditional densities proves (5.1). QED.

The improvement relative to (4.6) is exactly

`[3*4^(2/3)]/[6*2^(2/3)] = 2^(-1/3)
 =0.7937005259840998...`,                                        (5.11)

a `20.63%` reduction in the branch constant.

## 6. Target-normalized corollary

Suppose the complete matrix in (4.1) has exact rank three and its three nonzero eigenvalues all have modulus at least `s>0`. Since the coefficient map is `L=[r n,V^T]` and `V^T V=I_3`,

`LL^T=I+r^2 nn^T`,
`|pdet A|=|det D|(1+r^2)>=s^3`.                                  (6.1)

For `r>=1`,

`r^2 |det D|
 >= s^3 r^2/(1+r^2)
 >= s^3/2`.                                                       (6.2)

Substituting into (5.1),

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/3) s^(-1) Omega_J^(-1/3)
 =9.524406311809198... s^(-1) Omega_J^(-1/3).`                   (6.3)

Thus every target-normalized Schur-isotropic survivor with `r>=1` and an original-coordinate two-plane bank satisfying `Omega_J>=eta>0` is paid by

`||p_Q||_infinity <=9.525 eta^(-1/3)/s`.                         (6.4)

For the owner scale `s=1`, a bank with `Omega_J>=1/8`, for example, has the explicit universal bound

`||p_Q||_infinity <=19.049...`.                                  (6.5)

This is an actual target-level implication; the extra condition is the quantitative two-plane bank currency, not an unproved assertion that every target matrix has such a bank.

## 7. Continuity tracked separately

The new fleet02/B18 theorem is used here only for the sharper essential `L^infinity` estimate. The same hypotheses were already proved by fleet03/B18 r25 to yield a continuous density via its affine zero-pivot theorem. Therefore a continuous representative exists.

If a continuous representative exceeded the number on the right of (5.1) at one point, continuity would force it to exceed that number on an open interval of positive measure, contradicting the essential bound (5.1). Hence the continuous representative itself satisfies the sharper pointwise bound.

This separates the two logical issues as requested: the fleet02/B18 transfer sharpens the bound; continuity comes from the independently completed branch theorem.

## 8. Literature scope audit

The primary LPP theorem matches the input class exactly for the projection step. The sharp maximum-density/rearrangement theorem of Juškevičius--Lee can improve constants for special explicit sums, but is not needed for (5.1). Hanson--Wright requires subgaussian-type hypotheses absent here. The quadratic-form regularity results of Herry--Malicet--Poly impose substantially stronger iid/smooth Gaussian-functional assumptions. None of these latter results directly settles the owner's arbitrary non-iid cap-one target.

No exact prior theorem was located that matches all owner quantifiers. This search statement is not used as evidence of novelty.

## 9. Remaining implication

The full QFORM conjecture remains **OPEN / NOT PROVED**. The present run completely pays, with a sharper constant, every Schur-isotropic high-shear survivor that contains a quantitatively nondegenerate rank-two ORIGINAL-coordinate source bank as in (4.4)--(4.5).

The remaining local obstruction is the genuinely non-source-separated state in which every product-preserving bank carrying substantial transverse volume has latent rank three. A bounded two-dimensional marginal after an arbitrary spectral projection is not enough: the live conditional-cap and two-sheet X-ray counterexamples forbid replacing missing product provenance by a generic joint-density interface.

The next useful literature-to-proof transfer would have to exploit the linear-image-of-product structure of a full-rank three-dimensional residual bank before conditioning destroys it, or combine the current nested-volume routers with a theorem that extracts a genuine rank-two source bank of `Omega_J>=c` or forces an already-paid ridge/physical-pair exit.

## 10. Source pins

- Primary projection theorem: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.
- Designated partner theorem actually applied: fleet02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`.
- Fresh peer tilted-bank theorem sharpened here: fleet03/B18 r25, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T062246Z-fleet03-B18-QFORM-r25/REPORT.md`.
- Current full-target status remains OPEN; independent end-to-end review of the full theorem has not occurred.
