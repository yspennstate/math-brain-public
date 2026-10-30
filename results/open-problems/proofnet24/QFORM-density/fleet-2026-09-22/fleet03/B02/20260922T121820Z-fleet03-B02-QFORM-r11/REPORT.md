# fleet03/B02 — integrated Fourier 2+1 smoothing lemma

**Run:** `20260922T121820Z-fleet03-B02-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and live corrections

The full target is unchanged: for every dimension, independent real coordinates with probability densities bounded by 1, and every real symmetric matrix having at least three eigenvalues of absolute value at least 1, prove a universal linear small-ball estimate, equivalently an essentially bounded density with a universal bound. No moment, centering, compact-support, log-concavity, continuity, or eigen-coordinate independence hypothesis is available. A continuous representative is a stronger conclusion and is tracked separately.

This run does **not** use the refuted law-uniform pointwise Fresnel bound. It also respects the current corrections that a nonsingular rank-two cross minor alone is insufficient, that the universal constant is not pi, and that generic two-sheet/X-ray control alone is insufficient without product provenance.

The assigned partner is `fleet04/B02`; at the final pre-derivation check there was no completed `fleet04/B02` QFORM handoff in the shared handoff directory. I therefore did not wait or fabricate a partner result. I instead consumed the compatible completed other-account result `fleet02/B02`, run `B02-20260922T120900Z-qform-r11`, canonical report commit `400f82c8b98fc5623f567581b6ccb0b4298974e8`. I apply its exact Plancherel cross-block mechanism and its one-coordinate `L^{3/2}` square-pushforward estimate below, while re-deriving the rank-two endpoint because that peer's final L1 theorem was stated only for rank greater than two.

## 2. New theorem: a rank-two physical cross block plus one decoupled quadratic pivot closes the Fourier integral

### Theorem `QFORM-RANK2-PLUS-PIVOT-FOURIER-v1`

Let `I,J` be disjoint sets of original coordinates with `|I|=|J|=2`. Let

`B=A[I,J]`

be invertible, with singular values `s_1,s_2` and

`Delta=s_1 s_2=|det B|>0`.

Let `k` be a further original coordinate outside `I union J`, and assume

1. `d=A_kk != 0`, and
2. `A_{k ell}=0` for every `ell in I union J`.

There is **no restriction** on `A[I,I]`, `A[J,J]`, any couplings from `I union J union {k}` to the remaining coordinates, any part of the matrix on the remaining coordinates, the signs of the eigenvalues, the dimension, or the input laws beyond coordinate independence and density cap 1.

Then the characteristic function `phi_Q(t)=E exp(i t X^T A X)` belongs to `L^1(R)` and

`||phi_Q||_1 <= 4 * 3^(2/3) * pi * (Delta |d|)^(-1/3)`.   (2.1)

Consequently `Q` has a bounded **continuous** density, vanishing at infinity, with

`boxed( ||p_Q||_infinity <= 2 * 3^(2/3) * (Delta |d|)^(-1/3). )`   (2.2)

In particular, this is a genuine integrated-Fourier closure of a `2+1` smoothing configuration. Rank two by itself is exactly the nonintegrable `|t|^{-1}` endpoint; the independent quadratic pivot supplies the missing Hölder credit without any law-uniform pointwise quadratic decay.

### Proof

Let `R` be the complement of `I union J union {k}` and condition on all `X_R`. All terms involving `X_R` become fixed linear terms plus a constant. Because `k` has no matrix coupling to `I union J`, the remaining conditional quadratic form splits as

`Q = Q_IJ(X_I,X_J) + d X_k^2 + 2 ell X_k + c`,

where `ell,c` depend on the conditioned value but are deterministic after conditioning. Independence of the original coordinates therefore yields a factorization of the conditional characteristic function

`Phi_R(t)=Psi_R(t) Theta_ell(t)`.   (2.3)

The estimates below are uniform in all conditioned values and all induced linear terms.

#### 2.1 Rank-two cross block gives a uniform `L^{3/2}` Fourier credit

Take an SVD `B=P diag(s_1,s_2) S^T`, with `P,S` orthogonal `2 x 2` matrices, and put `Y=P^T X_I`, `Z=S^T X_J`. For fixed `t`, absorb every within-side quadratic and linear phase into complex densities `F_t(Y),G_t(Z)` exactly as in the consumed fleet02/B02 Plancherel mechanism.

Because each side consists of exactly two original coordinates, orthogonal change of variables preserves Lebesgue measure and the underlying two-dimensional product densities are pointwise at most 1 and have mass 1. Hence

`||F_t||_2 <= 1`, `||G_t||_2 <= 1`.

With the angular Fourier convention, Cauchy-Schwarz, the change of variables `xi=2t diag(s_1,s_2)y`, and Plancherel give for `t!=0`

`|Psi_R(t)| <= pi Delta^(-1/2) |t|^(-1)`.   (2.4)

Together with `|Psi_R(t)|<=1`, put `D=pi Delta^(-1/2)` and obtain

`||Psi_R||_(3/2)^(3/2)`
` <= 2 int_0^infinity min(1,D/t)^(3/2) dt`
` = 2 [ D + D^(3/2) int_D^infinity t^(-3/2) dt ]`
` = 6D`.

Therefore

`||Psi_R||_(3/2) <= (6 pi Delta^(-1/2))^(2/3)`.   (2.5)

This is the precise rank-two endpoint credit. It is consistent with the live correction `QFORM-CROSSMINOR-ALONE-FALSE`: `(2.4)` is not itself integrable.

#### 2.2 A single quadratic pivot gives a uniform `L^3` Fourier credit

Complete the square:

`d X_k^2+2 ell X_k = d (X_k+ell/d)^2 - ell^2/d`.

The constant phase is irrelevant. Let `f<=1` be the density of `X_k` and put `h=ell/d`. For `d>0` (reflection handles `d<0`), the density `g` of `d(X_k+h)^2` satisfies

`||g||_(3/2) <= 2 |d|^(-1/3)`.   (2.6)

For completeness, write `F(r)=f(r-h)+f(-r-h)` on `r>0`. Then `0<=F<=2` and `int_0^infinity F(r)dr=1`, while

`int g(y)^(3/2)dy`
` = (2|d|)^(-1/2) int_0^infinity F(r)^(3/2) r^(-1/2) dr`
` <= |d|^(-1/2) int_0^infinity F(r) r^(-1/2)dr`
` <= 2 sqrt(2) |d|^(-1/2)`.

The last step is the elementary bathtub maximization under `F<=2`, mass 1. Raising to the power `2/3` gives `(2.6)`.

Hausdorff-Young for the angular Fourier transform, interpolating the `L^1 -> L^infinity` norm 1 and Plancherel norm `(2pi)^(1/2)`, gives

`||Theta_ell||_3 <= (2pi)^(1/3) ||g||_(3/2)`
` <= 2 (2pi)^(1/3) |d|^(-1/3)`.   (2.7)

Crucially, this is an **integrated** estimate and is uniform in the translation `h`; no false pointwise `|t|^-1/2` claim is used.

#### 2.3 Exact Hölder closure

From `(2.3)`, `(2.5)`, `(2.7)`, and Hölder with exponents `3/2` and `3`,

`||Phi_R||_1`
` <= ||Psi_R||_(3/2) ||Theta_ell||_3`
` <= (6 pi Delta^(-1/2))^(2/3) * 2 (2pi)^(1/3) |d|^(-1/3)`
` = 4 * 3^(2/3) * pi * (Delta |d|)^(-1/3)`.

The right side is independent of the conditioned value `X_R`. Since

`phi_Q(t)=E_R Phi_R(t)`,

Minkowski/Tonelli gives the same global `L^1` bound `(2.1)`. Fourier inversion then gives `(2.2)`. Because `phi_Q in L^1`, the inverse Fourier representative is continuous and tends to zero at infinity. This proves the theorem.

## 3. Rectangular extension using the consumed product-marginal estimate

The same argument works if `|I|=2` and `J` is arbitrary, provided `B=A[I,J]` has rank two with nonzero singular values `s_1,s_2`. The fleet02/B02 proof uses the Livshyts-Paouris-Pivovarov product-marginal density bound on the projected `J` side, yielding

`|Psi_R(t)| <= sqrt(2) pi Delta^(-1/2) |t|^(-1)`.

Repeating the calculation gives

`||p_Q||_infinity <= 2^(4/3) 3^(2/3) (Delta |d|)^(-1/3)`.   (3.1)

The square `2x2` theorem above is stronger and self-contained because neither selected side pays a projection-density loss.

## 4. What this pays, and the first unpaid implication

This run turns a previously nonintegrable rank-two Fourier endpoint into a valid `L^1` characteristic-function bound by adding one genuinely independent quadratic pivot. It therefore verifies an exact `2+1` version of the three-direction heuristic without assuming post-rotation independence and without any moments or support regularity.

It does **not** solve the full conjecture. The target spectral hypothesis by itself does not currently provide the coordinate configuration assumed here. Dense matrices can have no exact zero couplings, and diffuse eigenvectors can make every fixed physical minor small. Therefore the first unpaid implication is a **spectral-to-coordinate Fourier-credit extraction** statement strong enough to cover the coupled case: from three eigenvalues `|lambda|>=1`, either produce a rank-three cross-block configuration already handled by the existing Plancherel theorem, or obtain a replacement for the decoupled `2+1` factorization that survives nonzero couplings of the third pivot. Exact isolation must not be silently inferred.

A particularly concrete next question is whether a vector-valued version of the rank-two Plancherel estimate can retain enough `L^{3/2}` control as a function of the third physical coordinate to combine with the scalar `L^3` square-pushforward estimate even when `A_{k,I union J}` is nonzero. A mere uniform pointwise rank-two bound cannot do this: it leaves the nonintegrable `1/|t|` tail and loses the third-pivot cancellation.

## 5. Quantifiers and status

- Arbitrary dimension: retained on the proved branch.
- Independent coordinate densities `<=1`: retained exactly.
- No moments/log-concavity/compact support/continuity of inputs: used nowhere.
- Extra eigenvalues and arbitrary outside matrix entries: allowed.
- Indefinite signs: allowed.
- Essential boundedness: proved on the stated `2+1` structural branch.
- Continuous density: also proved on that branch because the characteristic function is in `L^1`.
- Full three-large-eigenvalue target: **OPEN**.

An exact symbolic simplification in this run verified that the rectangular-branch Fourier-inversion constant reduces to `2^(4/3) 3^(2/3) (Delta |d|)^(-1/3)`; no numerical experiment is used as proof.
