SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-22T21:25:42Z.
attacking: literature-to-proof transfer: close the quantitative physical-pair alternative in account02/B18's two-stage window/star/pair reduction by a two-pivot fractional-smoothing argument, leaving only the genuine star obstruction.

# account01/B18 — two physical pivots convert quarter-small-ball control into a bounded density

**Run:** `20260922T212542Z-qform-B18-a01-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET_LEVEL_REDUCTION`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result in one line

The completed account02/B18 reduction had five alternatives: two diffuse branches already paid, two heavy-star branches unpaid, and a quantitative physical-pair branch. This report pays the **entire quantitative pair branch, with no sign or condition-number restriction**, by proving that two quantitative sequential physical scalar pivots plus `s_3(A)>=1` already imply a universal density bound. Therefore, after combining the two reports, every still-unpaid target matrix is forced into one of the two product-provenance heavy-star branches.

The explicit bound on the newly paid pair branch is

`||p_(X^T A X)||_infinity < 6039`.

Continuity is not claimed by this argument.

## 2. Exact partner result consumed

Designated partner `account02/B18`, canonical report:

`yspennstate/math-open-problems@6cda809756c61201f08cdee2dd7e07f20e5d5596`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T203852Z-b18-qform-lit-r12/REPORT.md`.

Its theorem `QFORM-TWO-STAGE-WINDOW-STARPAIR-v1`, for every symmetric `A` with `s_3(A)>=1`, fixes

`delta=2^-9=1/512`

and gives five exhaustive alternatives. Alternatives 1 and 3 have density bounds `<64` and `<576`. Alternatives 2 and 5 are heavy-star alternatives. Alternative 4 is produced as follows: one first has an original coordinate pivot

`a=A_ii`, `|a|>=delta`,

and its physical Schur residual

`S=C-b b^T/a`

has a residual physical coordinate `j` with

`d=S_jj`, `|d|>=delta`.

The original pair determinant obeys the exact identity

`det A[{i,j},{i,j}] = a d`,

so `|det|>=delta^2=2^-18`. The construction, not merely the determinant lower bound, is what is used below.

The partner also applies the primary Livshyts--Paouris--Pivovarov theorem to the two remaining star branches: a normalized one-dimensional bank `Y=u^T X_rest` has

`||p_Y||_infinity<=sqrt(2)`

while the distinguished original scalar is independent of the **entire original source** generating `(Y,R)`. This is source-valid but does not make `Y` independent of `R`.

## 3. Source-valid analytic dependency

The second dependency is the completed arbitrary-rank small-ball lemma from

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

For every nonzero symmetric matrix `T`, every affine perturbation, and independent cap-one coordinates `W`, it proves

`sup_u P(|W^T T W + ell^T W + c-u|<rho)`
` <= min(1, 5 (rho/||T||)^(1/4)).`                         (3.1)

No moment, support, centering, iid, log-concavity or smoothness assumption is present.

## 4. New scalar-square smoothing lemma

### Lemma 4.1 — quarter-small-ball to three-quarter-small-ball

Let `X` have a probability density bounded by one and be independent of a random source `W`. Let `m=m(W)` and `R=R(W)` be arbitrary measurable functions. Assume, for some `H>0`,

`sup_u P(|R-u|<rho) <= H rho^(1/4)` for every `rho>0`.       (4.1)

For `d!=0`, put

`Y=d (X+m)^2+R`.

Then for every `t` and `h>0`,

`P(|Y-t|<h)`
` <= [Gamma(1/4)^2/sqrt(pi)] H |d|^(-1/2) h^(3/4).`          (4.2)

Consequently

`sup_t E|Y-t|^(-1/2)`
` <= 3 [Gamma(1/4)^2 H/sqrt(pi)]^(2/3) |d|^(-1/3).`          (4.3)

#### Proof

Condition on `W`. Translation by `m(W)` is harmless. After scaling by `sqrt(|d|)`, the relevant one-dimensional sublevel set is

`E(z,h)={x: |x^2-z|<h}`,

where the sign of `d` is absorbed into `z`. Directly from the two square-root endpoints,

`|E(z,h)| <= 4h/sqrt(h+|z|)`                               (4.4)

for all real `z` and `h>0`:

- if `z<=-h`, the set is empty;
- if `-h<z<h`, its length is `2 sqrt(z+h)` and the displayed bound follows from `z<=h` (the negative-`z` case is even smaller);
- if `z>=h`, its length is
  `2(sqrt(z+h)-sqrt(z-h))=4h/(sqrt(z+h)+sqrt(z-h))`.

Since the density of `X` is at most one, (4.4) gives

`P(|Y-t|<h | W)`
` <= 4h |d|^(-1/2) (h+|R-t|)^(-1/2).`                       (4.5)

Set `Z=|R-t|`. By layer cake,

`E(h+Z)^(-1/2)`
` = (1/2) integral_0^infinity (h+r)^(-3/2) P(Z<=r) dr`
` <= (H/2) integral_0^infinity (h+r)^(-3/2) r^(1/4) dr`
` = (H/2) h^(-1/4) B(5/4,1/4)`
` = H Gamma(1/4)^2/(4 sqrt(pi)) h^(-1/4).`                  (4.6)

Here `Gamma(5/4)=Gamma(1/4)/4` and `Gamma(3/2)=sqrt(pi)/2`. Averaging (4.5) and using (4.6) proves (4.2).

Let

`L=[Gamma(1/4)^2/sqrt(pi)] H |d|^(-1/2)`.

Then `P(|Y-t|<h)<=min(1,L h^(3/4))`. Another layer-cake identity gives

`E|Y-t|^(-1/2)`
` = (1/2) integral_0^infinity h^(-3/2) P(|Y-t|<=h) dh`.

Split at `h_0=L^(-4/3)`. The two integrals are exact:

`(1/2)[ L integral_0^h0 h^(-3/4) dh + integral_h0^infinity h^(-3/2) dh ]`
` = (1/2)[4 L h_0^(1/4)+2 h_0^(-1/2)]`
` =3 L^(2/3).`

This proves (4.3). QED.

## 5. New two-pivot theorem

### Theorem 5.1 — `QFORM-TWO-PIVOT-QUARTER-TO-DENSITY-v1`

Let `A` be real symmetric with

`s_3(A)>=s>0`,

and let the coordinates of `X` be independent with probability densities bounded by one. Choose an original coordinate `i` with

`a=A_ii !=0`

and form its physical Schur residual

`S=C-bb^T/a`.

Choose a residual original coordinate `j` with

`d=S_jj !=0`

and form the second Schur residual `T`. Then `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity`
` <= 3 [5 Gamma(1/4)^2/sqrt(pi)]^(2/3)`
`       * |a|^(-1/2) |d|^(-1/3) s^(-1/6).`                 (5.1)

No sign assumption on `a` or `d` is needed. No conditioning number of the original physical `2x2` pair occurs.

#### Proof

Two rank-one completion identities give the singular-value inequalities

`s_3(A)<=s_2(S)<=||T||`.                                    (5.2)

Indeed `A` is the sum of a rank-one completed-square matrix and `0 direct_sum S`, and `S` is the sum of a rank-one completed-square matrix and `0 direct_sum T`; the standard singular-value rank inequality gives each step. Thus

`||T||>=s`.

Complete the second square in the original coordinate `X_j`:

`Q_1=d (X_j+m_2(W))^2+R(W)`,                                (5.3)

where `W` consists of all remaining original coordinates. The scalar `X_j` is genuinely independent of `W`. The quadratic matrix of `R` is exactly `T`, with any induced affine term allowed. By (3.1) and (5.2),

`sup_u P(|R-u|<rho)<=5 s^(-1/4) rho^(1/4).`                 (5.4)

Apply Lemma 4.1 with `H=5s^(-1/4)` to obtain

`sup_t E|Q_1-t|^(-1/2)`
` <=3 [5 Gamma(1/4)^2/sqrt(pi)]^(2/3)`
`      |d|^(-1/3) s^(-1/6).`                                (5.5)

Now complete the first square in the original coordinate `X_i`:

`Q=a (X_i+m_1(X_{-i}))^2+Q_1(X_{-i}).`                      (5.6)

Again `X_i` is independent of the entire remaining source. For fixed `X_{-i}`, the pushforward density of `a(X_i+m_1)^2` is bounded by

`|a|^(-1/2) |u|^(-1/2)`

on its sign-compatible half-line: the two inverse branches each contribute at most `1/(2 sqrt(|a||u|))`. Tonelli and (5.5) therefore give (5.1). This also proves absolute continuity and essential boundedness. No continuity statement follows from this argument for arbitrary merely bounded input densities. QED.

## 6. Application to account02/B18 Alternative 4

In the partner construction, Alternative 4 is reached with sequential pivots satisfying

`|a|>=delta`, `|d|>=delta`, `delta=2^-9`,

and `s_3(A)>=1`. Theorem 5.1 therefore gives

`||p_Q||_infinity`
` <= C_2p delta^(-5/6)`,

where

`C_2p=3 [5 Gamma(1/4)^2/sqrt(pi)]^(2/3)`
`    =33.3600019053431...`.

Since `delta^(-5/6)=2^(15/2)=181.019335983756...`,

`||p_Q||_infinity <=6038.80539332206... <6039.`              (6.1)

This pays **all signs** of Alternative 4. In particular there is no need to split the physical pair into definite versus indefinite cases, and no `sigma_min(B)` lower bound is required.

## 7. Combined reduction after the new payment

Applying Theorem 5.1 to the exact account02/B18 reduction yields the following source-pinned consequence.

For every target matrix `A` with `s_3(A)>=1`, at least one of the following now holds:

1. the overall diffuse spectral-window theorem gives `||p_Q||_infinity<64`;
2. there is an **outer heavy star**
   `|A_ii|<1/512`, `||A_{i,-i}||_2>1/512`;
3. a nonzero pivot has diffuse two-eigenvalue Schur residual and `||p_Q||_infinity<576`;
4. two sequential physical pivots have magnitudes at least `1/512`, and Theorem 5.1 gives `||p_Q||_infinity<6039`;
5. there is a **Schur heavy star**
   `|S_jj|<1/512`, `||S_{j,-j}||_2>1/512`.

Thus the only still-unpaid matrices in this entire two-stage structural reduction are the two near-zero/heavy-star mechanisms. This is strictly sharper than the partner reduction, whose quantitative pair alternative was still unpaid.

The Livshyts--Paouris--Pivovarov primary theorem applies exactly to either remaining star after normalizing its cross row: the bank `Y=u^T X_rest` has density cap `sqrt(2)`. No moments, support, centering, iid, log-concavity or smoothness are added. The unresolved point is that `Y` can remain dependent on the same-side quadratic remainder `R`; the live correction archive rules out treating a marginal cap as conditional independence.

## 8. Literature audit

Primary theorem checked: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1. For a product probability density `prod f_i` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`; for `k=1` this is `sqrt(2)`. This matches the remaining normalized star bank exactly.

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, IMRN 2015, supplies the broader source family behind these marginal estimates, but its stable-rank theorem is not needed to assert the new two-pivot bound.

A targeted search did not locate a primary theorem that directly matches the unrestricted owner target with only the cap-one product assumption and `s_3(A)>=1`. This is a search outcome, not a novelty claim.

## 9. Corrections respected and first unpaid implication

This argument does **not** use law-uniform pointwise Fresnel decay, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional projection-density moments, a fixed principal minor, a single Schur rank-two extraction, or conditional-cap-as-independence. It keeps all square completions on original physical coordinates and retains every induced affine term through the arbitrary-rank small-ball lemma.

The first unpaid implication is now unified and narrower:

> Prove a dimension-free density bound for the product-provenance star
> `Q=aX^2+2 beta X Y+R(W)`, where `|a|<1/512`, `beta>1/512`, `X` is an original cap-one scalar independent of the entire original-coordinate source `W`, `Y=u^T W` with `||u||_2=1` and `||p_Y||_infinity<=sqrt(2)`, while `R(W)` is an arbitrary quadratic remainder constrained only through the original full target's third large singular value; or derive an equivalent product-preserving grouped-coordinate payment.

The marginal cap on `Y` alone is not enough; the dependence between `Y` and `R(W)` must be used rather than discarded.
