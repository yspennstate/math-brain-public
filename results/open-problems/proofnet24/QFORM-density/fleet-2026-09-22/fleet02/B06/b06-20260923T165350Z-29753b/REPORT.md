SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T16:53:50Z.
attacking: turn failure of the one-Fresnel/one-cross weighted-volume marginal gate into an exact at-most-two-physical-coordinate concentration certificate, then spend partner r39's rank-two floor before any local inverse-minor extraction.

# fleet02/B06 — fused-volume heavy-row transfer

**Run:** `b06-20260923T165350Z-29753b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN: for arbitrary independent ORIGINAL-coordinate densities bounded by one and real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^TAX`, or give a valid counterexample. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is used below. Continuity remains separate.

## 1. Source-valid inputs

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no B06 stop. The same-hour canonical login already existed and was preserved rather than overwritten.

The immediate B06 premise is the preceding fleet02/B06 theorem at

`yspennstate/math-open-problems@3f715005422309e2d831f45fb3c9d577e340af74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T162549Z-a11cf/REPORT.md`.

Its `r=1,k=1` Fresnel-volume case says the following. If, in ORIGINAL coordinates,

`Q = X^T(D + lambda vv^T)X + 2 X^T M Y + R(Y) + affine`,              (1.1)

where `D` is diagonal, `||v||=1`, `lambda != 0`, the `X,Y` coordinates retain their product laws, and `R` is arbitrary, define

`Z = ||(I-vv^T)M||_F^2`

and sample physical row pairs and a physical cross column with weight proportional to

`(v_p M_{qt}-v_q M_{pt})^2`.

If every sampled-row marginal is at most `1/2`, then

`||p_Q||_infinity <= C_F (|lambda| Z)^(-1/3),`

where

`C_F = 3*2^(4/3)*e^(1/3) = 10.550168831164775...`.                   (1.2)

The fresh designated partner fleet03/B06 r39 is source-pinned at

`yspennstate/math-open-problems@9ac8f055fe86ee993b00125fdcfbc1d528147632`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T161847Z-fleet03-B06-qform-r39/REPORT.md`.

In its true near-rank-two physical cross tube, with squared singular values `x_1>=x_2>=...` and `E=||N||_F^2`, it proves

`E > 11907/16384,`
`x_2 >= E/64,`
`sum_{j>=3} x_j < E/64`.                                             (1.3)

The pinned newest-Claude package required by the owner was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The specific completed statements applied below are its fractional-potential lemma

`H_{1/2}(S) <= 8 B^(1/2)/sqrt(2 pi)` when `|phi_S(t)|<=min(1,B/|t|)`,  (1.4)

and its square peel

`D(aZ^2+S) <= |a|^(-1/2) H_{1/2}(S)`                                (1.5)

for a genuinely independent physical scalar `Z` of density at most one. The current grouped-projection continuation

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

is used only at its proved exact-rank-two crossing scope in Section 6.

## 2. Exact fused-row identity

Let

`C=(I-vv^T)M`, `Z=||C||_F^2>0`,                                      (2.1)

and define

`w_{pq,t}=(v_pM_{qt}-v_qM_{pt})^2/Z`, `p<q`,                          (2.2)

with row marginal

`alpha_i = P_w(i in {p,q})`.                                         (2.3)

### Lemma 2.1 — `QFORM-FUSED-ROW-MARGINAL-IDENTITY-v1`

For every ORIGINAL physical row `i`,

`boxed: alpha_i = v_i^2 + ||C_{i,*}||_2^2/Z.`                         (2.4)

**Proof.** Replace each column `M_t` by

`c_t=(I-vv^T)M_t`.

The determinant with first column `v` is unchanged because adding a multiple of `v` to the second column changes no two-by-two minor. Since `<v,c_t>=0` and `||v||=1`,

`sum_{j != i}(v_i c_{jt}-v_j c_{it})^2`
` = v_i^2 sum_j c_{jt}^2 + c_{it}^2 sum_j v_j^2 - 2v_i c_{it}<v,c_t>`
` = v_i^2 ||c_t||^2 + c_{it}^2.`                                     (2.5)

Sum over `t` and divide by `Z`. QED.

This is an exact localization identity, not a norm inequality. In particular `sum_i alpha_i=2` and a failed marginal gate identifies a physical coordinate carrying either rank-one spectral mass, transverse cross mass, or both.

## 3. Exact heavy-row transfer

The crucial point is that a heavy row can be moved from the structured Fresnel bank to the arbitrary bank without paying a worst fiber and without rotating the product law.

Fix one physical coordinate `h`. Let

`s^2=1-v_h^2`.                                                        (3.1)

If `s=0`, then `v` is supported on `h` and every nonzero fused minor contains `h`, already the fully concentrated endpoint. Assume `s>0`, put

`v'=v_{-h}/s`, `lambda'=lambda s^2`.                                 (3.2)

Move the ORIGINAL scalar `X_h` from the `X` bank to the `Y` bank. The remaining structured block is still diagonal plus rank one,

`D_{-h} + lambda' v'v'^T`,                                            (3.3)

while the enlarged cross block consists of the old rows `M_{-h,*}` plus the new column

`lambda v_h v_{-h}`                                                   (3.4)

coming from the physical same-bank coupling to `X_h`. That new column is parallel to `v'`, so its transverse fused contribution is exactly zero.

Let `Z'` be the `r=1,k=1` fused currency of the transferred form. Then

`s^2 Z'`
` = sum_{p<q, p,q != h} sum_t (v_pM_{qt}-v_qM_{pt})^2`
` = Z(1-alpha_h)`.                                                     (3.5)

Therefore

`boxed: |lambda'| Z' = |lambda| Z (1-alpha_h).`                       (3.6)

Moreover the new squared-minor probability is exactly the old law conditioned on the event that the sampled physical row pair avoids `h`. No independence has been manufactured: only an ORIGINAL coordinate has been reassigned to the arbitrary side of the proof.

This is **`QFORM-FUSED-HEAVY-ROW-TRANSFER-v1`**.

## 4. Two-transfer compiler: diffuse payment or at most two physical hubs

### Theorem 4.1 — `QFORM-FUSION-GATE-OR-2HUB-CONCENTRATION-v1`

For every form (1.1) with `Z>0`, exactly one of the following useful exits occurs:

1. **weighted diffuse payment:** after moving at most one physical row to the arbitrary bank, the surviving fused-minor law has every row marginal at most `1/2`, retains at least one quarter of the original fused mass, and

   `boxed: ||p_Q||_infinity`
   ` <= C_F 4^(1/3) (|lambda|Z)^(-1/3).`                              (4.1)

2. **two-coordinate concentration:** there is a set `H` of at most two ORIGINAL coordinates such that

   `boxed: P_w({p,q} intersects H) > 3/4,`                            (4.2)

   equivalently

   `sum_{t,p<q: {p,q} intersect H != empty}`
   `  (v_pM_{qt}-v_qM_{pt})^2 > 3Z/4.`                               (4.3)

**Proof.** If the original marginals satisfy `max alpha_i<=1/2`, use (1.2) and we are in exit 1 with retained mass one. Otherwise choose `h_1` with `alpha_{h_1}>1/2`. The mass of fused minors avoiding it is

`p_1=1-alpha_{h_1}<1/2`.                                               (4.4)

If `p_1<1/4`, then `H={h_1}` gives (4.2). If `p_1>=1/4`, perform the exact transfer of Section 3. If the conditional fused law is diffuse, (3.6) and (1.2) give

`D(Q)<=C_F(|lambda|Z p_1)^(-1/3)`
`    <=C_F 4^(1/3)(|lambda|Z)^(-1/3)`,                                (4.5)

which is exit 1. Otherwise choose a second physical row `h_2` whose conditional marginal is greater than `1/2`. The mass avoiding both rows is

`p_2=p_1(1-alpha'_{h_2}) < p_1/2 < 1/4`.                              (4.6)

Hence more than three quarters of the original fused mass meets `H={h_1,h_2}`. QED.

This is the requested weighted product-structure replacement for the dimension-losing fiber supremum in this subbranch: a marginal failure does not trigger a supremum, a single-minor extraction, or a rotated conditional law. It is compiled into at most two ORIGINAL coordinates.

## 5. Real application to partner r39

Take partner r39's physical cross block `N` satisfying (1.3), and let `v` be any unit vector used by a diagonal-plus-rank-one same-bank representation. By the best rank-one approximation theorem,

`Z=||(I-vv^T)N||_F^2`
` >= sum_{j>=2}x_j`
` >= x_2`
` > 11907/1048576`
` = 0.011355400085449219... .`                                       (5.1)

Thus, whenever the rank-one coefficient obeys `|lambda|>=1`, Theorem 4.1 gives an unconditional dichotomy inside this structured nonnull-bank branch.

In the weighted diffuse exit,

`||p_Q||_infinity`
` < C_F 4^(1/3) (11907/1048576)^(-1/3)`
` = 74.50954761179284... .`                                           (5.2)

No part of the small nonzero cross tail has been deleted: `N` is the complete partner block.

Otherwise there are at most two physical coordinates `H` carrying more than three quarters of the fused determinant mass, quantitatively

`sum_{t,p<q: {p,q} intersect H != empty}`
` (v_pN_{qt}-v_qN_{pt})^2`
` > (3/4)(11907/1048576)`
` = 0.008516550064086914... .`                                       (5.3)

This sharpens the first unpaid branch. The prior statement "the fused marginal gate may fail" is replaced by a bounded-cardinality physical certificate with a fixed aggregate currency.

## 6. Candidate refuted: concentrated fused mass does not imply a strong physical hub row

A tempting next inference is false.

Take three `X` coordinates, two `Y` coordinates,

`v=e_1`,

and

`M = [[0,0], [1,0], [0,1]].`                                         (6.1)

Then `Z=2`. The only nonzero fused minors are

`({1,2},1)` and `({1,3},2)`, each of squared size one. Hence

`alpha_1=1`, `alpha_2=alpha_3=1/2`,                                  (6.2)

so **all** fused mass touches the single physical coordinate `1`. But the actual physical cross row is

`M_{1,*}=0`.                                                          (6.3)

Therefore neither (4.2) nor even 100% concentration implies a nonzero hub-partner row, let alone a quantitatively strong one. This is **`QFORM-FUSED-CONCENTRATION-NOT-HUB-v1`**. It refutes an intermediate compiler step, not QFORM.

The reason is structural: the fused determinant can be large because a localized same-bank square direction `v` pairs with cross curvature living entirely on other rows.

## 7. The obstruction family is itself a genuine target and is paid by completed source results

Set `lambda=1`, all other same-bank coefficients to zero, and use (6.1). Then

`Q_* = X_1^2 + 2X_2Y_1 + 2X_3Y_2`.                                   (7.1)

Its symmetric coefficient matrix has spectrum

`{1,1,1,-1,-1}`,                                                      (7.2)

so this is an exact QFORM target, not merely a toy route obstruction.

Let

`R=2X_2Y_1+2X_3Y_2`.                                                   (7.3)

The current completed exact-rank crossing theorem in `NEW_PROJECTED_CROSSING.md`, applied to the two physical coordinate banks and `B=I_2`, gives

`|phi_R(t)| <= min(1, pi/|t|)`.                                       (7.4)

Here both two-dimensional projection densities are simply product densities bounded by one, so no rotated-independence claim is involved.

Now apply the pinned newest-Claude fractional-potential lemma (1.4) with `B=pi`:

`H_{1/2}(R)`
` <= 8 sqrt(pi)/sqrt(2pi)`
` = 4 sqrt(2).`                                                        (7.5)

Finally `X_1` is a genuinely independent ORIGINAL coordinate and (7.1) is an exact square peel. The pinned newest-Claude Lemma 4.2 therefore gives

`boxed: ||p_{Q_*}||_infinity <= 4 sqrt(2) = 5.656854249... .}`         (7.6)

Thus the counterexample only kills the inference "concentrated fused volume => strong physical hub row". It simultaneously shows the correct repair at this endpoint: when the rank-one direction localizes completely, move that physical scalar out and spend it as the independent square smoothing an exact rank-two crossing.

## 8. Deterministic check

`CHECK.py` tests 500 random `(v,M)` instances. It verifies (2.4), (3.5), and the conditional-marginal identification after transfer. The recorded maxima are

`max_alpha_identity_error = 3.33e-16`,
`max_transfer_identity_relative_error = 5.60e-16`,
`max_conditional_marginal_error = 1.10e-14`.

It also records the r39 floor and the constant in (5.2). Source SHA-256:

`bf21ccb4e90debfdb90ea895063decd3f3e967ca65a0f71ebe4edd1aeb859666`.

Output SHA-256:

`0f8862b3dfdfaaac6d81d8bf5fbe7aeb3113d219476d7737eb527c29a2802d2b`.

The check is diagnostic only; the identities above are proved algebraically.

## 9. First unpaid implication after this run

The live debt is now

**`QFORM-FUSED-2HUB-CONCENTRATION-ROUTING-v1`**:

> In partner r39's complete near-rank-two physical cross tube, when a diagonal-plus-rank-one same-bank direction with `|lambda|>=1` falls into the concentrated alternative (5.3), retain the complete cross tail and arbitrary opposite-bank curvature and route the at-most-two physical coordinates either into (i) the current two-hub + transverse-square / projected-crossing receivers, or (ii) a localized-square + rank-two crossing peel as in Section 7, with a uniform quantitative threshold. Do not infer a strong hub row from fused concentration alone.

The exact example (6.1) proves that the routing must distinguish "hub-partner concentration" from "localized-square concentration". That is the first unpaid implication; no full theorem is claimed.
