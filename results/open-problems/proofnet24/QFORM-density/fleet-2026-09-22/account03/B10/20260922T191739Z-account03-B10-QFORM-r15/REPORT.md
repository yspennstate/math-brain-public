SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-22T19:17:39Z.
attacking: the exact-rank-three partial-null-bank endpoint; compress the whole null bank into one genuine independent cap-one coordinate and remove the apparent rho->0 spectral degeneration before paying the remaining overlap bank.

# account03/B10 r15 — null-bank compression removes the near-endpoint spectral loss

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Fresh owner control before publication:** revision `2026-09-22.14`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW_PRODUCT-PRESERVING_REDUCTION / FULL_TARGET_OPEN`

The full target remains the universal essential-density bound for `Q=X^T A X` when the physical coordinates are independent with densities at most one and `A` has at least three eigenvalues of modulus at least one. This report works in the exact-rank-three core and does not claim the full theorem. Continuity is tracked separately and is not proved by the new reduction.

## 1. Correction discipline and the first unpaid implication

Fresh `CURRENT_RESEARCH.md` still marks the arbitrary-joint rank-three coarea cap and the positive conditional-projection-density moment as false. I therefore do not use the newer owner-message assertions that unrestricted rank-three has already been closed by a bounded three-dimensional projected density. I also do not assume independence after a spectral rotation, do not take a vector-fiber supremum, and do not use law-uniform pointwise quadratic-phase decay.

The preceding B10 run, canonical source

`yspennstate/math-open-problems@d41decf403b7b6a6761096fa35fbd4427c24ffe7`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T181253Z-account03-B10-QFORM-r14/REPORT.md`,

proved a uniform bound when the whitened complement of a partial null-ray bank is diffuse, but its bound was

`3 e (rho |det Lambda|)^(-1/3)`

and therefore deteriorated as the complement mass `rho=1-L` tended to zero, even though the exact endpoint `rho=0` had already been paid uniformly. The first target here is that apparent near-endpoint singularity.

## 2. Setup inherited from the exact null-ray bank theorem

Let

`A=U Lambda U^T`, `U^T U=I_3`,

where `Lambda` is real symmetric, invertible, and all its eigenvalues have modulus at least one. Let a nonempty physical-row bank `S` lie on a unit spectral null ray `r`:

`u_i=alpha_i r`, `r^T Lambda r=0`, `i in S`.

Set

`L=sum_(i in S) alpha_i^2`, `0<L<=1`,

and let

`W=sum_(i in S) alpha_i X_i`.

The bank variable is genuinely independent of the complementary original coordinates. The completed scalar projection bound used in the preceding B10 report gives

`||p_W||_infinity <= sqrt(2/L)`.                                    (2.1)

Write `C=S^c`. Parseval gives

`sum_(j in C) u_j u_j^T = I-L r r^T`.                              (2.2)

Put

`s=||Lambda r||`.

Since the least singular value of `Lambda` is at least one,

`s>=1`.                                                            (2.3)

## 3. New theorem: compress the entire null bank before whitening

### Theorem 3.1 — `QFORM-NULL-BANK-CAPONE-COMPRESSION-v1`

In the setup above define

`c=sqrt(2/L)`, `X_0=c W`, `beta=1/c=sqrt(L/2)`.

Then `X_0` is independent of every complementary original coordinate and has density at most one. Moreover the law of the same quadratic form `Q` can be represented as an exact-rank-three quadratic form in the independent cap-one variables

`(X_0,(X_j)_(j in C))`

with a Parseval spectral frame `U_hat` and symmetric spectral matrix `Lambda_hat` satisfying all of the following exact statements.

Let

`q=1-L/2`.

Then

`1/2 <= q <1`,                                                     (3.1)

`|det Lambda_hat| = q |det Lambda|`,                              (3.2)

`sigma_min(Lambda_hat) >= q sigma_min(Lambda) >= q >=1/2`,        (3.3)

and the synthetic physical row corresponding to `X_0` is a null pivot with leverage

`ell_0=L/(2-L)`.                                                    (3.4)

Furthermore its complete physical two-coordinate determinant bank obeys

`sum_(j in C) |det (A_hat)_{ {0,j} }|
 = (L/2) ||Lambda r||^2
 >= L/2`.                                                          (3.5)

Here `A_hat` denotes the coefficient matrix of the reduced independent-coordinate representation; it generates exactly the same random variable `Q`.

### Proof

By (2.1), scaling by `c=sqrt(2/L)` gives

`||p_(X_0)||_infinity
 =c^(-1)||p_W||_infinity
 <=sqrt(L/2)sqrt(2/L)=1`.

Because `W` only uses the coordinates in `S`, `X_0` remains genuinely independent of the complement.

The bank spectral contribution `W r` is now `beta X_0 r`. Therefore the reduced (not yet Parseval) spectral row matrix consists of the synthetic row `beta r` and all rows `u_j`, `j in C`. Its Gram matrix is, using (2.2),

`H=beta^2 r r^T + I-L r r^T
  =I-(L/2) r r^T`.                                                 (3.6)

Thus `H` has eigenvalues `(q,1,1)` with `q=1-L/2`. Define

`U_hat=U_red H^(-1/2)`,
`Lambda_hat=H^(1/2) Lambda H^(1/2)`.                               (3.7)

Then `U_hat^T U_hat=I_3` and

`U_red Lambda U_red^T = U_hat Lambda_hat U_hat^T`,                 (3.8)

so this is a law-preserving representation in the reduced independent cap-one coordinates.

Since `det H=q`, (3.2) follows. Also `lambda_min(H)=q`, hence for every vector `x`,

`||H^(1/2) x||>=sqrt(q)||x||`.

Applying this on both sides of `Lambda` gives

`sigma_min(H^(1/2)Lambda H^(1/2))
 >=q sigma_min(Lambda)`,                                           (3.9)

which proves (3.3).

The synthetic Parseval row is

`u_hat_0=beta H^(-1/2)r=(beta/sqrt(q))r`,

so its leverage is

`ell_0=beta^2/q=(L/2)/(1-L/2)=L/(2-L)`,                            (3.10)

and its physical pivot remains exactly zero:

`(A_hat)_{00}=beta^2 r^T Lambda r=0`.                              (3.11)

For a complement coordinate `j`, the physical cross coefficient is invariant under the simultaneous whitening:

`(A_hat)_{0j}=beta r^T Lambda u_j`.                                (3.12)

Since the 2x2 principal block on `{0,j}` has zero first diagonal,

`|det(A_hat)_{ {0,j} }|=|(A_hat)_{0j}|^2`.                         (3.13)

Summing and using (2.2),

`sum_j |(A_hat)_{0j}|^2
 =beta^2 (Lambda r)^T (I-Lrr^T)(Lambda r)`
`=beta^2 ||Lambda r||^2`                                          (3.14)

because `r^T Lambda r=0`. Since `beta^2=L/2`, this is exactly (3.5). QED.

### Interpretation

The small parameter `rho=1-L` from complement-only whitening was not an intrinsic spectral degeneration. Compressing the genuine independent bank **before** whitening leaves a uniformly invertible rank-three spectral matrix: its least eigenvalue magnitude is at least `1/2` for every `L>0`. The cost is one distinguished null physical coordinate whose leverage is explicitly known.

This is product-preserving. No projected coordinate has been declared independent; the only new independent coordinate is the actual bank aggregate `X_0`, which is independent because the original bank and complement have disjoint coordinate supports.

## 4. Near-endpoint corollary: a uniformly conditioned heavy null pivot

Assume the previously troublesome near endpoint

`rho=1-L <=1/8`, equivalently `L>=7/8`.

Then Theorem 3.1 gives

`ell_0=L/(2-L)>=7/9`,                                               (4.1)

`sigma_min(Lambda_hat)>=1/2`,                                     (4.2)

and

`sum_(j in C)|det(A_hat)_{ {0,j} }|
 >=7/16`.                                                         (4.3)

Thus the near-endpoint problem is converted into a **uniformly conditioned heavy-null-row problem carrying constant total indefinite-pair curvature**. In particular no estimate in the surviving branch needs to pay a power of `rho^{-1}` merely because the original null bank nearly exhausted the spectral ray.

The exact partner-like high-null normal form from account03/B11 can also now be applied without a vanishing spectral scale: its separated-leakage theorem has bound

`6 e^(2/3) s_0^(-1)`

when the heavy null row's leakage support is disjoint from the two transverse spectral forms. Here `s_0=sigma_min(Lambda_hat)>=1/2`, so that branch is uniformly bounded by

`12 e^(2/3)<23.373`.                                                (4.4)

Hence, after compression, the genuinely unresolved near-endpoint case is the **overlapping leakage** case, not spectral degeneration.

## 5. Completed compatible account04 mathematics applied to an actual inequality

The exact named partner `account04/B10` still has no completed current-QFORM run/handoff in the fresh source tree; the latest visible B10 work there is earlier POS3 work, so no partner result is fabricated.

I apply the completed compatible account04/B16 theorem

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

Its exact fixed-pair determinant identity says that for a Parseval rank-three frame, if a row has leverage `c` and a second row has residual leverage `h` after removing the first row's direction, then

`sum_k |det A_{ {i,j,k} }|=|det Lambda| c h`.                       (5.1)

Apply (5.1) to the compressed form with the synthetic row `i=0`. If a complementary row `j` has residual leverage `h_j>1/2`, then, using (3.2), (3.4), and the exact cancellation

`q ell_0=L/2`,                                                      (5.2)

we obtain

`sum_k |det(A_hat)_{ {0,j,k} }|
 =|det Lambda_hat| ell_0 h_j`
` =(L/2)|det Lambda| h_j`
` > (L/4)|det Lambda|`.                                             (5.3)

In the near endpoint `L>=7/8` and `|det Lambda|>=1`, this becomes the constant-scale determinant-bank payment

`boxed:  sum_k |det(A_hat)_{ {0,j,k} }| > 7/32.`                    (5.4)

This is a direct application of completed account04 mathematics to the newly compressed geometry; unlike the r14 bound, it has **no `rho` loss**.

The same account04/B16 source supplies a target-level zero-diagonal atom theorem. Write its normalized determinant-bank weights as `w_k`. If, in addition,

`(A_hat)_{00}=(A_hat)_{jj}=(A_hat)_{kk}=0`

and one eligible atom has `w_k>=tau`, then (5.3) gives

`|det(A_hat)_{ {0,j,k} }| > (L/4)|det Lambda| tau`.                 (5.5)

For `L>=7/8`, `|det Lambda|>=1`, and `tau>=1/8`,

`|det(A_hat)_{ {0,j,k} }|>7/256`.                                  (5.6)

The account04 zero-diagonal triple density theorem therefore gives the actual target inequality

`||p_Q||_infinity
 <= C_off (256/7)^(1/3)
 <15.972`,                                                         (5.7)

where

`C_off=2^(4/3)[log 3+2 log(3/2)]
      =4.8117455951457755...`.

Thus an eligible heavy atom in the nested-heavy near-endpoint state is completely paid at a universal constant, again without `rho^{-1/3}`.

If every positive determinant-bank atom is eligible but none has weight at least `1/8`, there are at least nine positive atoms. The surviving branch is genuinely a **diffuse cubic determinant bank**, exactly the aggregation problem identified by account04/B16, now with total mass bounded below by `7/32` rather than a quantity vanishing with `rho`.

## 6. The first unpaid implication is now smaller

The first unpaid B10 implication after this run is:

**`QFORM-HEAVY-NULL-OVERLAP-AGGREGATION-v1`.** Prove a universal density bound for an exact-rank-three Parseval form with

1. one original independent cap-one coordinate having physical pivot zero and leverage at least `7/9`;
2. spectral least singular value at least `1/2`;
3. total two-coordinate determinant mass from that null row at least `7/16`;
4. in the nested-heavy subbranch, a fixed-pair triple determinant bank of total mass `>7/32`;
5. no eligible heavy zero-diagonal determinant atom and no support-separated leakage shortcut.

The required step is to aggregate the overlapping original-coordinate leakage / diffuse determinant bank **before** taking reciprocal local-minor constants. A bounded conditional density cannot replace the missing independence; the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` correction remains binding.

This is strictly narrower than the previous `rho->0` bridge: after Theorem 3.1 there is no small spectral eigenvalue or vanishing total determinant resource left to explain the difficulty.

## 7. Computation and algebra checks

A 20,000-sample numerical stress check was run on random symmetric Witt-form matrices

`[[0,s,0],[s,a,b],[0,b,kappa]]`

rescaled so that their least singular value is at least one, with `L` sampled in `[7/8,1)`. It checked

`det Lambda_hat=q det Lambda`

and the simple Parseval-frame realization of

`sum_j |(A_hat)_{0j}|^2=(L/2)||Lambda r||^2`.

The maximum relative errors were respectively

`3.65e-15` and `7.43e-16`.

The minimum observed ratio

`sigma_min(Lambda_hat)/(q sigma_min(Lambda))`

was `1.0048...`, consistent with the exact inequality (3.9). These are diagnostics only; the proof above is algebraic.

## 8. Status and regularity

Proved in this run:

- a law-preserving compression of an arbitrary exact null-ray bank to one genuine independent cap-one coordinate;
- uniform spectral conditioning `sigma_min(Lambda_hat)>=1/2` after that compression;
- exact synthetic null-row leverage and pair-determinant mass identities;
- removal of the `rho` loss from the nested-heavy determinant-bank inequality;
- the explicit `<15.972` density bound in the account04/B16 eligible-heavy-atom branch.

Not proved: the overlapping-leakage diffuse-bank aggregation, arbitrary exact-rank-three closure, the extension from exact rank three to arbitrary additional spectrum, or the full owner conjecture. The new general compression theorem is structural; it does not itself prove a continuous density. The explicit density branch (5.7) proves essential boundedness, not continuity.

**Full QFORM conjecture: OPEN / NOT PROVED.**
