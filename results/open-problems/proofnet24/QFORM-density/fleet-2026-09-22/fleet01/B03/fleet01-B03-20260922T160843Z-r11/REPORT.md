# QFORM B03 — Schur-balanced half-Riesz bridge

Run: `fleet01-B03-20260922T160843Z-r11`
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 0. Exact target and source pins

Target: for independent real coordinates with probability densities bounded by one and a real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a dimension-free L-infinity density bound for `X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion.

Control source read coherently at `math-research-brain@2c421dda3573fe3a1872350b4751a3b0dd1aa2f1`, revision `2026-09-22.5`; refreshed before publication at a descendant with the same owner control. Corrections consumed include `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`, and `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`.

Named partner result actually used: fleet02/B03, `math-open-problems@f40d5d4f5013b0a6af275a19aa3dc0fa2d76c347`, which proves for independent cap-one `U,V`

`||p_{UV}||_3 <= 2 sqrt(3)`.

No conditional sum/difference density cap is used.

## 1. One-dimensional quadratic section lemma

For every `c != 0`, `s in R`, `eps>0`, and every probability density `g<=1`,

`P(|c(Z-h)^2+s| <= eps) <= 4 eps / (sqrt(|c|) sqrt(|s|+eps)).`  (1)

Proof. After scaling, it is enough to bound the Lebesgue length of

`{u: |u^2-r|<=eta}`.

If `r>eta`, its length is

`2(sqrt(r+eta)-sqrt(r-eta)) = 4 eta/(sqrt(r+eta)+sqrt(r-eta)) <= 4 eta/sqrt(r+eta)`.

If `|r|<=eta`, the length is at most `2 sqrt(r+eta)<=2 sqrt(2 eta)<=4 eta/sqrt(|r|+eta)`. If `r<-eta` the set is empty. Multiplying by the density cap proves (1).

## 2. Uniform regularized square-potential estimate

Define

`J(s)= integral_R ( ||u^2-s|+1 )^(-3/4) du.`

Then

`sup_s J(s) <= 16.`  (2)

A direct proof uses three cases. If `s<=0`, split at `|u|=1` and compare the tail to `|u|^(-3/2)`, giving less than 6. If `0<s<=4`, split at `|u|=3`; the compact part contributes at most 6 and the tail less than 4. If `s>4`, let `r=sqrt(s)>2` and on the positive half-line split `[0,r/2]`, `[r/2,3r/2]`, `[3r/2,infinity)`. The first and third pieces are `O(r^(-1/2))`; on the middle interval use `|u^2-r^2|>=r|u-r|` and integrate `(1+r|u-r|)^(-3/4)`. The positive-half contribution is less than 7, hence the full integral is less than 14. The round constant 16 is retained.

Consequently, if `Y` has density `f<=1`, `delta!=0`, then for all `r in R` and `eps>0`,

`E ( |delta(Y-h)^2-r| + eps )^(-1/2)
 <= 16^(2/3) |delta|^(-1/3) eps^(-1/6).`  (3)

Indeed `||f||_3<=1`, while after the scaling `u=sqrt(|delta|/eps)(y-h)`, the `L^(3/2)` norm of the kernel in (3) is at most the right side.

## 3. New two-coordinate small-ball theorem

Let `Y,Z` be independent, each with density bounded by one, and let

`R(Y,Z)=aY^2+2bYZ+cZ^2+l_1Y+l_2Z+r_0`,

with

`D=|ac-b^2|>0`.

If `c!=0`, then for every target `t` and every `eps>0`,

`P(|R-t|<=eps)
 <= K0 |c|^(-1/6) D^(-1/3) eps^(5/6),`  (4)

where

`K0=4*16^(2/3)<25.4`.

Proof. Because the Hessian block is nonsingular, translate `Y,Z` by constants to remove the linear terms; translations preserve independence and the density caps. Completing the square in `Z` gives

`R-t = c(Z+alpha Y+beta)^2 + delta(Y-gamma)^2-tau`,

with `delta=(ac-b^2)/c`, hence `|delta|=D/|c|`. Condition on `Y`. By (1),

`P(|R-t|<=eps | Y)
 <= 4 eps |c|^(-1/2)
    ( |delta(Y-gamma)^2-tau|+eps )^(-1/2).`

Average and apply (3). This is exactly (4).

The same statement holds with `a` in place of `c` by reversing the coordinates.

## 4. New half-Riesz theorem for a nonsingular 2D quadratic

If a nonnegative random variable `W=|R-t|` satisfies

`P(W<=eps)<=min(1,K eps^(5/6))`,

then layer cake gives

`E W^(-1/2) <= (5/2) K^(3/5)`.

Applying (4) yields

`sup_t E |R-t|^(-1/2)
 <= C0 |c|^(-1/10) D^(-1/5),`  (5)

with

`C0=(5/2)(4*16^(2/3))^(3/5)<17.5`.

Taking the larger nonzero diagonal coefficient `m=max(|a|,|c|)` gives the best version of (5). In particular, if for some `kappa in (0,1]`

`m >= kappa sqrt(D)`,

then

`boxed{ sup_t E |R-t|^(-1/2)
        <= 17.5 kappa^(-1/10) D^(-1/4). }`  (6)

Thus the determinant-optimal half-Riesz scaling is proved whenever the two-dimensional Schur block is not extremely cross-dominant.

More generally, the same proof with any Holder exponent `p in (1,2)` gives a tunable family

`P(|R-t|<=eps)
 <= C_p |c|^{-(p-1)/(2p)} D^{-1/(2p)}
    eps^{(p+1)/(2p)}`,

and hence

`sup_t E|R-t|^(-1/2)
 <= C'_p |c|^{-(p-1)/(2(p+1))}D^{-1/(2(p+1))}.`

As `p downarrow 1`, the exponents approach the determinant-optimal `D^(-1/4)` endpoint; only the endpoint constant/tail summation remains unpaid.

## 5. Partner result closes the exact pure-saddle endpoint

Now suppose the centered residual is the exact saddle

`R=cUV+r_0`,

where translated `U,V` remain independent and cap one. Fleet02/B03 proves

`||p_{UV}||_3 <= 2 sqrt(3)`.

After scaling,

`||p_R||_3 <= 2 sqrt(3) |c|^(-2/3).`

For any radius `rho>0`, Holder on `|s-t|<=rho` gives

`integral_{|s-t|<=rho} p_R(s)|s-t|^(-1/2) ds
 <= 4 ||p_R||_3 rho^(1/6),`

while the complement contributes at most `rho^(-1/2)`. Optimizing in `rho` gives

`boxed{ sup_t E|R-t|^(-1/2)
 <= 4(8 sqrt(3)/3)^(3/4) |c|^(-1/2)
 < 12.61 |c|^(-1/2). }`  (7)

For a matrix block `[[0,b],[b,0]]`, `c=2b`, so (7) is less than

`8.92 |b|^(-1/2) = 8.92 D^(-1/4)`.

This is an actual application of the named fleet02/B03 result. It also shows that the apparent blow-up of (5) as a diagonal coefficient tends to zero is not intrinsic at the exact saddle endpoint.

## 6. New physical-principal-triple certificate for the full form

Let `A` be arbitrary symmetric in any dimension. Choose three ORIGINAL coordinates `(i,j,k)` and condition on all other coordinates `W`. Write the physical principal triple as

`T=A[{i,j,k},{i,j,k}]`.

Assume the physical pivot

`d=A_ii !=0`.

After completing the square only in the original variable `X_i`, the conditional form is

`d(X_i+h(Y,Z,W))^2 + R_W(Y,Z)+const(W)`,

where the quadratic Hessian of `R_W` is the 2x2 Schur block

`S=T[{j,k},{j,k}] - d^(-1) T[{j,k},i] T[i,{j,k}].`

Outside couplings affect only linear terms and translations, so Sections 3-5 apply uniformly in `W`.

For fixed `Y,Z,W`, the transformed square has conditional density bounded by

`|d|^(-1/2)|u|^(-1/2)`

on the appropriate half-line. Therefore (5) gives the unconditional density certificate

`boxed{ ||p_Q||_infinity
 <= 17.5 |d|^(-1/2) m^(-1/10) |det S|^(-1/5), }`  (8)

where `m=max(|S_jj|,|S_kk|)>0`.

If `m>=kappa sqrt(|det S|)`, then

`boxed{ ||p_Q||_infinity
 <= 17.5 kappa^(-1/10)
    |d|^(-1/4)|det T|^(-1/4). }`  (9)

Here `det T=d det S` exactly.

If instead the Schur block is the exact pure saddle `[[0,b],[b,0]]`, the partner-assisted endpoint (7) gives

`boxed{ ||p_Q||_infinity
 < 8.92 |d|^(-1/4)|det T|^(-1/4). }`  (10)

All statements (8)-(10) allow arbitrary additional coordinates, arbitrary outside couplings, arbitrary signs, and arbitrary cap-one input densities. They use no rotation of the product law and no false conditional cap after sum/difference symmetrization.

These arguments prove existence of an essentially bounded density in the stated certificate branches. They do NOT prove continuity of that density.

## 7. What changed and what remains unpaid

This is a different mechanism from the preceding B03 cross-rank/Fourier and conditional-L2-packet runs: it is a direct product-preserving sublevel/half-Riesz estimate for a 2D Schur residual.

The new useful reduction is that a physical scalar pivot no longer needs a rank-two disjoint cross block. A nonsingular 2D Schur residual is enough whenever one of its physical diagonal entries is at least a fixed fraction of `sqrt(|det S|)`, and the exact zero-diagonal saddle endpoint is also paid by the partner collision theorem.

The first unpaid local implication is now narrow and explicit:

> remove the mild cross-dominance loss in (5), uniformly in the regime
> `0 < max(|S_11|,|S_22|) << sqrt(|det S|)`, or produce a product-preserving aggregate certificate that bypasses a single Schur triple there.

A tunable `p downarrow1` estimate shows that the loss can be made arbitrarily small in exponent; the obstruction is the endpoint tail constant, not the quadratic section algebra. Separately, the full spectral hypothesis still does not force one dimension-free principal triple, as recorded by the live corrections. Hence this is a supporting theorem, not a full solution.

## 8. Integrity statement

Full QFORM remains OPEN. No Gaussianity, moments, compact support, connected support, log-concavity, diagonal eigenbasis independence, or pointwise van-der-Corput claim is used. The result is source-compatible with all corrections available at publication time.
