# Supplement — selected-three diffuse versus whole-window diffuse

This supplement adds a global diffuse-eigenvector router to the r34 physical-row result. It uses the completed ridge-window theorem exactly at its proved scope:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

That source proves: if a symmetric matrix has at least three eigenvalues of modulus at least one and the spectral projection `P` onto `|lambda|>=1/64` has `max_i P_ii<=1/32`, then every cap-one product input gives a continuous `C_0` density with

`||p_Q||_infinity <= 288 sqrt(3e)/13 <64`.

## Theorem — `QFORM-SELECTED3-OR-WINDOW-DIFFUSE-ROUTER-v1`

Let `A` be symmetric and choose any three orthonormal eigenvectors `R=[r1,r2,r3]` whose eigenvalues have modulus at least `L>0`. Put

`P3=RR^T`

and let `PH` be the full spectral projection of `A` onto all eigenspaces with `|lambda|>=L/64`. Then exactly the following exhaustive routing is available:

1. **selected-three localized:** `max_i (P3)_ii>1/48`; or
2. **whole high-window diffuse:** `max_i (PH)_ii<=1/32`, in which case the full quadratic form has a continuous `C_0` density satisfying

   `||p_Q||_infinity <64/L`; or
3. **complementary-window physical currency:** for some original coordinate `i`,

   `(PH-P3)_ii>1/96`,

   and if `A_extra=A(PH-P3)=(PH-P3)A`, then

   `||A_extra e_i||_2 > L/(64 sqrt(96)) = 0.001594719884624465... L`.

   Consequently the literal full row obeys the same lower bound,

   `||A e_i||_2 > L/(64 sqrt(96))`,

   and hence

   `max(|A_ii|,||A_{i,-i}||_2) > L/(64 sqrt(192))`

   `=0.001127637244510988... L`.

### Proof

The range of `P3` is contained in the range of `PH`, hence `PH-P3` is an orthogonal projection and its diagonal entries are nonnegative. If branch 1 fails and branch 2 fails, choose `i` with `(PH)_ii>1/32`. Then

`(PH-P3)_ii > 1/32-1/48 =1/96`,

which is branch 3's leverage statement.

Because `PH-P3` is a spectral projection commuting with `A`, expand in an orthonormal eigenbasis of `A`. Every eigenvalue on its range has modulus at least `L/64`, so

`||A_extra e_i||_2^2
 = sum_{j in extra window} lambda_j^2 |r_j(i)|^2
 >= (L/64)^2 (PH-P3)_ii
 > L^2/(64^2*96)`.

The spectral pieces of `Ae_i` are orthogonal, so `||Ae_i||>=||A_extra e_i||`. Finally

`||Ae_i||_2^2=A_ii^2+||A_{i,-i}||_2^2`,

forcing the last displayed alternative.

If branch 2 holds, apply the source ridge-window theorem to `A/L`; density scaling gives the factor `1/L`. QED.

## Significance for B08

This gives a genuine end-to-end estimate in the strongest natural diffuse regime: if the **entire** spectral window down to `L/64` is delocalized, the target is already paid by `<64/L`, with continuity, while arbitrary smaller eigenvalues and arbitrary signs remain present. If only the selected three large eigenvectors are diffuse, failure of the whole-window gate is not an amorphous obstruction: it forces quantitative physical currency coming from the complementary high spectral window.

Thus a selected-three diffuse state can now fail a complete diffuse theorem only by producing an additional localized high-window resource. This is deterministic coefficient information and does not delete the complementary spectrum or rotate the random variables.

The universal target is still OPEN because branch 1 and branch 3 require product-preserving localized receivers; one row norm alone is not promoted to a density theorem.
