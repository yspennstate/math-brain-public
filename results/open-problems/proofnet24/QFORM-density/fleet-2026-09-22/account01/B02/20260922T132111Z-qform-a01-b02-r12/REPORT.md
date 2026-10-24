# account01/B02 — half-order integrated Fourier closure for a unique heavy rank-three row

Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`.  
Run: `20260922T132111Z-qform-a01-b02-r12`.  
Assignment: integrated Fourier estimate.  
Classification: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**.  
Execution status: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval was used, but repository transport is not claimed as native learned-memory ingestion).

## 1. Compact conditional end-to-end route

For a rank-exactly-three target matrix write

`A = U Lambda U^T`, `U^T U = I_3`, `|det Lambda| >= 1`,

and let `c_i=||u_i||^2` be the row leverages. If every `c_i<=1/2`, the reviewed diffuse Fourier theorem gives a bounded continuous density (indeed `<=3e`). The first genuinely different branch is therefore a leverage-heavy row.

This run proves the following new closure: if there is exactly one heavy row `k`, so `c=||u_k||^2>1/2` and all other rows have leverage `<=1/2`, then every nonzero physical diagonal pivot `d=A_kk` yields

`||p_Q||_infinity <= 4 sqrt(2e) (c |d| |det Lambda|)^(-1/4)`.      (1.1)

In particular, if `|d|>=1/4`, then

`||p_Q||_infinity <= 2^(13/4) sqrt(e) < 15.69`.                    (1.2)

The proof is not a pointwise scalar van-der-Corput estimate. It is a **half-order integrated Fourier estimate** for a rank-two residual, followed by an exact square-pushforward kernel. This changes mechanism from the previous fixed-cross-minor/Fourier-tail route.

Applying the completed partner result account02/B02 (`QFORM-PHYSICAL-PIVOT-CROSSBLOCK-FOURIER-v1`, canonical report `yspennstate/math-open-problems@400f82c8b98fc5623f567581b6ccb0b4298974e8:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/B02-20260922T120900Z-qform-r11/REPORT.md`), its localized-row identity gives in the remaining `|d|<1/4` branch

`d^2+sigma^2 = ||A e_k||^2 >= c > 1/2`,

hence

`sigma > sqrt(7)/4`,                                                 (1.3)

and its exact averaged-linear estimate becomes

`|phi_Q(t)| <= (4 pi sqrt(2)/sqrt(7))^(1/2) |t|^(-1/2)`.            (1.4)

Thus the unique-heavy rank-three case is reduced to a sharply identified **cross-dominant zero/small-diagonal branch**, rather than an arbitrary heavy regime. Cases with at least two leverage-heavy rows also remain.

No continuity claim is made for (1.1); only existence of an essentially bounded density is proved. The full arbitrary-dimension target remains open.

## 2. Exact setup for the unique-heavy row

Fix the unique heavy row `u_k`. Put

`c=||u_k||^2>1/2`.

Choose an orthogonal change of basis only inside the three-dimensional spectral space so that

`u_k = sqrt(c) e_1`.

This does not rotate the independent physical coordinates. Write every other row as

`u_i=(alpha_i,v_i)`, `v_i in R^2`, `i!=k`.

Since `sum_i u_i u_i^T=I_3`,

`sum_{i!=k} v_i v_i^T=I_2`,
`sum_{i!=k} alpha_i v_i=0`,
`sum_{i!=k} alpha_i^2=1-c`.                                      (2.1)

Uniqueness of the heavy row gives

`||v_i||^2 <= ||u_i||^2 <= 1/2`, `i!=k`.                          (2.2)

Thus the transverse two-dimensional frame is exactly in the Hausdorff--Young/Brascamp--Lieb diffuse range.

In this spectral basis write

`Lambda = [[a,b^T],[b,C]]`,

where `a` is scalar and `C` is symmetric `2x2`. Since

`d=A_kk = c a`,                                                     (2.3)

the hypothesis `d!=0` is equivalent to `a!=0`.

Put, using only the light physical variables,

`W=sum_{i!=k} alpha_i X_i`,
`Z=sum_{i!=k} v_i X_i in R^2`.

Then

`Q = a(sqrt(c)X_k+W)^2 + 2(sqrt(c)X_k+W)b^T Z + Z^T C Z`

and exact completion of the square gives

`Q = a(sqrt(c)X_k + W + a^(-1)b^T Z)^2 + Z^T S Z`,                (2.4)

where

`S=C-bb^T/a`,
`det S = det Lambda / a`.                                         (2.5)

Since `Lambda` is invertible and `a!=0`, the transverse matrix `S` is invertible.

## 3. Rank-two diffuse endpoint: the weighted Fourier estimate

Let

`R=Z^T S Z`.

Define the transverse leverage values `gamma_i=||v_i||^2`. By (2.1)--(2.2),

`sum gamma_i w_i w_i^T=I_2`, `gamma_i<=1/2`,

where `w_i=v_i/sqrt(gamma_i)` for nonzero rows. The same geometric Brascamp--Lieb plus sharp Beckner Hausdorff--Young calculation used in the reviewed diffuse theorem applies in rank two through the pointwise-Fresnel step (only the final unweighted `L^1_t` integration fails at rank two). It gives

`|phi_R(t)| <= min(1, K/|t|)`,                                    (3.1)

with

`K = B(V) pi |det S|^(-1/2)`,
`B(V)=prod_{gamma_i>0}(1-gamma_i)^(-(1-gamma_i)/2) <= e`.          (3.2)

For completeness: geometric Brascamp--Lieb and sharp Hausdorff--Young give `||hat g||_1 <= (2pi)^2 B(V)` for the density `g` of `Z`; the two-dimensional Fresnel kernel has modulus at most `pi |t|^(-1)|det S|^(-1/2)`. Fourier inversion of `g` therefore gives (3.1). No law-uniform one-dimensional Fresnel estimate is used.

Now integrate with the half-order Riesz weight:

`int_R |t|^(-1/2)|phi_R(t)| dt`
` <= 2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]`
` = 8 sqrt(K)`
` <= 8 sqrt(e pi) |det S|^(-1/4)`.                                (3.3)

This is the integrated Fourier estimate supplied by this run.

The one-dimensional Riesz kernel satisfies, with the Fourier convention `hat h(t)=int exp(-itx)h(x)dx`, the standard identity

`widehat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2)`.

Because the right side of (3.3) is finite, the convolution with the probability law of `R` has a bounded representative and

`sup_s E |s-R|^(-1/2)`
` <= (2pi)^(-1/2) int |t|^(-1/2)|phi_R(t)|dt`
` <= 4 sqrt(2e) |det S|^(-1/4)`.                                  (3.4)

This can be justified by Gaussian regularization of the Riesz kernel and dominated convergence; the absolute integrability in (3.3) supplies the domination.

## 4. Exact square-pushforward mixture

Condition on all light variables. In (2.4), put

`h=W+a^(-1)b^T Z`, `r=Z^T S Z`.

The conditional random variable is

`a(sqrt(c)X_k+h)^2+r`.

For every fixed `h,r` its density at `s` is a sum over at most two roots. Since `f_k<=1`, the exact Jacobian gives

`p_{Q | light}(s)`
` <= [c |a|]^(-1/2) |s-r|^(-1/2)`.                                (4.1)

Indeed each root has derivative magnitude `2 sqrt(c|a|) sqrt(|s-r|)`, and the two density values sum to at most `2`.

Average (4.1) over the light variables and use (3.4):

`||p_Q||_infinity`
` <= 4 sqrt(2e) c^(-1/2)|a|^(-1/2)|det S|^(-1/4)`
` = 4 sqrt(2e) c^(-1/2)|a|^(-1/4)|det Lambda|^(-1/4)`
` = 4 sqrt(2e) (c |d| |det Lambda|)^(-1/4)`.                       (4.2)

The last equality uses `d=ca`. This proves (1.1).

If the three nonzero eigenvalues have absolute value at least one, then `|det Lambda|>=1`. If additionally `c>1/2` and `|d|>=1/4`,

`(c|d||det Lambda|)^(-1/4) <= (1/8)^(-1/4)=2^(3/4)`,

so

`||p_Q||_infinity <= 4 sqrt(2e) 2^(3/4)=2^(13/4)sqrt(e)<15.69`.

This proves (1.2).

Existence of a density requires no Fourier inversion of `phi_Q`: every conditional square law in (4.1) is absolutely continuous because `a!=0`, and the mixture is absolutely continuous. The estimate is on the essential supremum of that mixture density. This argument does **not** prove that the density has a continuous representative.

## 5. Actual application of the assigned partner result

The assigned partner account02/B02 proved, for a physical row of a selected three-large-eigenvalue subspace, the exact endpoint identity and averaged-linear estimate. In the present rank-exactly-three setting, the selected subspace is the whole range and

`d^2+sigma^2 = ||Ae_k||^2 = u_k^T Lambda^2 u_k >= ||u_k||^2 = c`.  (5.1)

Therefore the only unique-heavy branch not uniformly closed by (1.2) satisfies `|d|<1/4`, hence

`sigma^2 > c-1/16 > 7/16`,
`sigma > sqrt(7)/4`.                                               (5.2)

Substituting (5.2) into partner equation (2.6),

`|phi_Q(t)| <= (pi sqrt(2)/(sigma |t|))^(1/2)`,

yields the explicit residual inequality

`|phi_Q(t)| <= (4 pi sqrt(2)/sqrt(7))^(1/2)|t|^(-1/2)`.           (5.3)

Thus the partner result is used in an actual bound, not merely cited. The remaining obstruction is that the rank-one endpoint `|t|^-1/2` is not integrable and must be coupled with the two transverse spectral directions without taking a false conditional density cap.

## 6. Relation to current corrections and other workers

This proof respects all live corrections read before publication:

- `QFORM-POINTWISE-DECAY-FALSE`: no arbitrary-density scalar Fresnel decay is used.
- `QFORM-FIBER-SUP-DIMENSION-LOSS`: no unrestricted fiber supremum is integrated.
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: the only spectral rotation is deterministic inside the rank-three coefficient space; independence is used only for the original physical variables. `X_k` remains independent of the light physical variables.
- `QFORM-UV-CONDITIONAL-CAP-FALSE` and `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: no conditional cap after a sum/difference transform is assumed.
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: no claim is made that every target matrix admits a physical scalar pivot plus a physical rank-two Schur cross block.
- `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`: no fixed good rank-three physical minor/cut is asserted.
- `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`: the proof keeps an exact Riesz/Fourier identity rather than a coordinatewise absolute-value Holder majorant.

The fresh regularized-determinant theorem (`math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`) is compatible: it closes an entire-range diffuse branch with arbitrary additional small eigenvalues. The theorem here attacks the opposite rank-exactly-three **unique-heavy** geometry and does not duplicate the requested independent reviews assigned to account02/B02 and account03/B04.

Account03/B02 independently supplied a physical scalar-pivot plus physical `2x2` Schur-cross-block potential theorem. The present result is different: the transverse smoothing is aggregated over a two-dimensional diffuse spectral frame and requires no fixed `2x2` physical cross minor.

## 7. Exact remaining implication

For rank-exactly-three matrices, the current branch picture is now:

1. all row leverages `<=1/2`: reviewed diffuse theorem gives a bounded continuous density;
2. exactly one leverage-heavy row and `|A_kk|>=1/4`: (1.2) gives an essentially bounded density `<15.69`;
3. exactly one leverage-heavy row and `|A_kk|<1/4`: partner inequality (5.3) gives uniform `|t|^-1/2` decay from a genuinely random independent linear aggregate, but the second half-order gain is unpaid;
4. at least two leverage-heavy rows: also unpaid.

The first essential missing implication for this worker is therefore:

**QFORM-UNIQUE-HEAVY-CROSS-CLOSURE-v1.** In case 3, exploit the two-dimensional transverse frame together with the large physical off-diagonal aggregate `sigma>sqrt(7)/4` to obtain either an integrable combined Fourier estimate or a direct small-ball bound. The proof must preserve original-coordinate product structure; conditioning on a conjugate aggregate and assigning it a uniform density cap is forbidden by the live corrections.

A successful form would upgrade the partner `|t|^-1/2` credit by another integrable half-order coming from the transverse frame, without selecting a uniformly large fixed physical minor. After that, at-least-two-heavy-row geometry remains the next structural branch.

## 8. Status

`ESSENTIAL_STEP_APPLIED`. The new theorem is a rigorous supporting branch under the stated rank-exactly-three and unique-heavy hypotheses. It does not match all quantifiers of the owner target, does not settle arbitrary additional eigendirections, and has not undergone two independent end-to-end reviews. The universal conjecture remains OPEN. Continuous density is **not proved** in the new heavy-pivot branch; only an essentially bounded density is proved.
