SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T02:24:30Z.
attacking: change mechanism after the coloop-interpolation sequence; compile exact rank three into a diffuse-light exit, a finite heavy physical exit, or one explicit finite near-null core while applying the account04/B16 Pluecker endpoint theorem at inequality level.

# account03/B16 — finite-heavy-core projection-product compiler

**Run:** `20260923T022430Z-account03-B16-QFORM-r22`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `PROVED SUPPORTING STRUCTURAL THEOREM / FULL QFORM OPEN`  
**Continuity:** proved in two Fourier/ridge exits below; not proved in the remaining exits or globally.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated private-repository transport was used; no native learned-memory receiver use was verified).

## 1. Target, mechanism change, and source-valid inputs

The full target is unchanged: for every dimension, independent real coordinates with one-dimensional densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a single dimension-free essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, log-concavity, Gaussianity, or post-rotation independence hypothesis is used here.

The preceding B16 runs treated the null/nonzero-coloop interpolation. This run changes mechanism as required: instead of refining another scalar coloop kernel, it performs an **original-coordinate heavy/light spectral-frame decomposition** and uses product-preserving projection results before the nonlinear quadratic payment.

Fresh control was read from `yspennstate/math-research-brain@6c3241b8679d0d42516cbdb68d2051b3838f4c2d`, OWNER CONTROL revision `2026-09-22.15`. Live corrections consumed include the failure of arbitrary-joint rank-three coarea, positive conditional projection-height moments, post-rotation independence, receiver-only fiber suprema, and law-uniform pointwise quadratic-phase decay. None is used below.

The completed inputs actually used are:

1. **Designated partner account04/B16**, `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical source  
   `yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd:proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`.  
   For an exact-rank-three indefinite matrix `A=R Lambda R^T`, with Pluecker law `w_S=det(R_S)^2` and `d=P(S cap T=emptyset)`, it proves
   `||p_Q||_infinity <=12 |det Lambda|^(-1/3)d^(-1/6)` when `d>0`, and, independently of `d`, the majority-sign one-sheet side is bounded by `pi sqrt(2)`. The first estimate has a continuous density through its cross-cut Fourier proof.

2. **One-scale ridge/spectral-window theorem**, canonical source  
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.  
   If a symmetric matrix has at least three eigenvalues of modulus at least one and the projection `P` onto *all* eigenspaces with `|lambda|>=1/64` obeys `max_i P_ii<=1/32`, then the quadratic form, even with arbitrary coordinate-separable real additions, has a continuous density `<64`.

3. **Orientation-free exact-rank-three scalar-pivot estimate**, source  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.  
   If `A=R Lambda R^T` has exact rank three, `c_i=||r_i||^2`, and `a=A_ii!=0`, then
   `||p_Q||_infinity <=128 [c_i |a| |det Lambda|]^(-1/4)`.

4. **Physical-triple determinant theorem**, B16 source  
   `yspennstate/math-open-problems@e8effa5a58b9788063a3f4b4b7829330f000d478:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T202347Z-account03-B16-QFORM-r15/REPORT.md`.  
   Every invertible original-coordinate principal triple `B=A[S,S]` gives
   `||p_Q||_infinity <= C3 |det B|^(-1/3)`, where
   `C3=16 sqrt(30) 2^(1/4)=104.216889989...`, with arbitrary outside coordinates/couplings retained.

The account04/B16 theorem is applied below to explicit inequalities; it is not used as a receiver-only projection cap.

## 2. Main theorem — `QFORM-EXACT-R3-FINITE-HEAVY-CORE-v1`

Let the **entire** matrix have exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,

with all three eigenvalues of `Lambda` satisfying `|lambda_j|>=1`. Let `r_i^T` be row `i` of `R`, and put

`c_i=||r_i||^2`.

Let `w_S=det(R_S)^2` for physical triples `S`, let `S,T` be independent with law `w`, and put

`d=P(S cap T=emptyset)`.

Define the fixed heavy/light split

`H={i:c_i>1/64}`, `L=H^c`,

and the spectral Gram matrices

`G_H=sum_(i in H) r_i r_i^T`, `G_L=sum_(i in L) r_i r_i^T=I_3-G_H`.

Then at least one of the following five alternatives holds.

### Exit A — disjoint Pluecker mass

If

`d>=1/64`,

then the designated account04/B16 theorem gives the actual two-sided inequality

`boxed: ||p_Q||_infinity <=12 (1/64)^(-1/6)=24.`

This exit has a continuous density.

### Exit B — diffuse light coordinates

If

`lambda_min(G_L)>=1/2`,

then

`boxed: ||p_Q||_infinity <128.`

This exit also has a continuous density.

### Exit C — a heavy physical scalar pivot

If there is an `i in H` with

`|A_ii|>=1/4096`,

then

`boxed: ||p_Q||_infinity <2897.`

### Exit D — a volumetric heavy physical triple

If

`det G_H>=1/64`,

then

`boxed: ||p_Q||_infinity <43818.`

### Residual chamber E — finite near-null, nearly low-rank heavy core

If none of A--D holds, then all of the following are simultaneously true:

1. `d<1/64`;
2. `|H|<=192`;
3. `lambda_max(G_H)>1/2`;
4. `det G_H<1/64`;
5. every `i in H`, after normalization `u_i=r_i/sqrt(c_i)`, satisfies
   `|u_i^T Lambda u_i|<1/64`;
6. the signature is indefinite;
7. writing the eigenvalues of `G_H` as `h_1>=h_2>=h_3>=0`, either
   `h_2<1/4` (a near-line heavy core) or `h_3<1/8` (a near-plane heavy core).

Moreover the designated account04/B16 ruled theorem still pays one entire output side in this residual chamber: for signature `(2,1)`,

`boxed: ess sup_(s>=0) p_Q(s) <= pi sqrt(2),`

and for signature `(1,2)` the same bound holds on `s<=0`. Thus the only exact-rank-three density debt left by this theorem is the **minority-sign two-sheet side** of the finite near-null near-line/near-plane chamber E.

This is a fixed-cardinality compiler: no number depending on the ambient dimension remains in chamber E.

## 3. Proof of Exit B: diffuse light coordinates

This is the key product-preserving step.

Assume `G_L>= (1/2)I_3`. Condition on all original heavy coordinates `X_H`. The remaining variables `X_L` are still independent with their original density caps at most one. The conditional quadratic form is

`Q | X_H = X_L^T A_LL X_L + ell(X_H)^T X_L + const(X_H)`,

where

`A_LL=R_L Lambda R_L^T`.

The linear term is coordinate-separable; no rotation of the input law has occurred.

Because `G_L=R_L^T R_L` is positive definite, the three nonzero eigenvalues of `A_LL` are the eigenvalues of the symmetric congruence

`B_L=G_L^(1/2) Lambda G_L^(1/2)`.

Indeed the nonzero spectra of `R_L Lambda R_L^T` and `Lambda G_L` agree, and `Lambda G_L` is similar to `B_L`. Since

`s_min(B_L)>=s_min(G_L^(1/2))^2 s_min(Lambda)
             >=(1/2)*1=1/2`,

all three nonzero eigenvalues of `A_LL` have modulus at least `1/2`.

The orthogonal projector onto `range(A_LL)=range(R_L)` is

`P_L=R_L G_L^(-1) R_L^T`.

For every light coordinate `i in L`,

`(P_L)_ii=r_i^T G_L^(-1)r_i
          <=||G_L^(-1)|| c_i
          <=2*(1/64)=1/32`.

Now multiply the whole conditional scalar output by `2`. The matrix `2A_LL` has three eigenvalues of modulus at least one, and its projection onto all eigenspaces with eigenvalue modulus at least `1/64` is exactly `P_L` (the only other eigenvalues are zero). Therefore the completed spectral-window theorem applies, including the arbitrary conditional linear term, and gives

`||p_(2Q | X_H)||_infinity <64`.

Scaling a scalar density back by a factor two gives

`||p_(Q | X_H)||_infinity <128`,

uniformly in the value of `X_H`. Averaging the conditional densities proves Exit B.

Each conditional density supplied by the spectral-window theorem is continuous and uniformly bounded by `128`; dominated convergence over the heavy-coordinate law therefore gives a continuous unconditional representative in this exit.

## 4. Proof of Exit C: a heavy scalar pivot

For `i in H`, `c_i>1/64`. If also `|A_ii|>=1/4096`, the exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity
 <=128 [c_i |A_ii| |det Lambda|]^(-1/4)`

`<128 [(1/64)(1/4096)]^(-1/4)`

`=128*2^(18/4)`

`=2896.309375740099... <2897`.

No projection-density substitution is made: the half-Riesz estimate retains the original product source through the Schur remainder.

## 5. Proof of Exit D: a heavy physical triple

First, because `sum_i c_i=tr(R^TR)=3`, the heavy set has fixed cardinality

`|H|*(1/64)<sum_(i in H)c_i<=3`,

so

`|H|<=192`.

Cauchy--Binet applied to `R_H` gives

`det G_H
 =sum_(S subset H, |S|=3) det(R_S)^2`.

If `det G_H>=1/64`, some heavy triple `S` obeys

`det(R_S)^2
 >= [1/64]/binom(192,3)`.

Here

`binom(192,3)=1,161,280`.

For exact rank three,

`det A[S,S]=det(Lambda) det(R_S)^2`,

so `|det A[S,S]|` is at least the same lower bound because `|det Lambda|>=1`. Apply the completed ambient physical-triple determinant theorem:

`||p_Q||_infinity
 <= C3 [64*binom(192,3)]^(1/3)`

`=43817.11194162648... <43818`.

The huge numerical constant is immaterial here: the point is that a *fixed* heavy original-coordinate core with genuine three-dimensional volume is completely paid without any dimension loss.

## 6. Proof of the residual geometry

Assume A--D all fail.

The failure of B gives `lambda_min(G_L)<1/2`. Since `G_H=I-G_L`, the two matrices have the same eigenvectors and

`lambda_max(G_H)=1-lambda_min(G_L)>1/2`.

The failure of D gives `det G_H<1/64`.

The cardinality `|H|<=192` was already proved above.

For every heavy row, failure of C gives `|A_ii|<1/4096`. Since

`A_ii=r_i^T Lambda r_i
     =c_i u_i^T Lambda u_i`

and `c_i>1/64`,

`|u_i^T Lambda u_i|
 <(1/4096)/(1/64)=1/64`.

Thus every member of the finite heavy core lies in the fixed `1/64` Rayleigh neighborhood of the spectral null cone.

The residual chamber cannot have a definite signature. If all eigenvalues of `Lambda` had the same sign, `|lambda_j|>=1` would imply

`|A_ii|=|r_i^T Lambda r_i|>=||r_i||^2=c_i>1/64`

for every heavy row, contradicting failure of C.

Finally let `h_1>=h_2>=h_3` be the eigenvalues of `G_H`. We know `h_1>1/2` and `h_1h_2h_3<1/64`. If `h_2<1/4` we are in the near-line alternative. Otherwise `h_2>=1/4`, so

`h_3 < (1/64)/[(1/2)(1/4)] =1/8`.

This proves the near-line/near-plane dichotomy.

Because A failed, `d<1/64`; but the account04/B16 one-sheet estimate does not require `d>0`. Since the residual signature is indefinite, it yields `pi sqrt(2)` on the majority-sign side exactly as stated in chamber E. This is a second equation-level application of the designated partner result.

## 7. Why this is useful and what is still unpaid

This theorem changes the shape of the exact-rank-three problem. A dimension-dependent diffuse Pluecker cloud is no longer the generic unresolved object. Either:

* disjoint Pluecker mass is quantitatively present and account04/B16 pays it;
* the light original-coordinate subsystem is sufficiently isotropic and the spectral-window theorem pays it after conditioning;
* a heavy scalar pivot pays the curvature;
* the finite heavy core contains true three-dimensional volume and a physical triple pays it; or
* all remaining difficulty is confined to at most `192` heavy original coordinates whose normalized spectral rows are uniformly near the indefinite null cone and whose Gram matrix is quantitatively near rank one or rank two. One whole output side is already paid by account04/B16.

The natural successor is therefore not another receiver-only projection cap. It is

`QFORM-FINITE-NEAR-NULL-CORE-PLUS-LIGHT-STABILITY-v1`:

> In chamber E, aggregate the at-most-192 heavy original coordinates into a bounded number of near-null angular banks, keep the light coordinates as a genuine product-projection/transverse resource, and prove the minority-sign density bound without deleting tangent leakage or taking worst conditional slices.

The completed account01/B11 five-null-ray compiler pays the zero-width endpoint of precisely this kind of geometry; the remaining task is tangent/light stability. A successful theorem here would close the **exact-rank-three** case. It would still not by itself close arbitrary additional spectrum.

For the full QFORM target, arbitrary extra spectral components remain a separate global interface: selecting three large eigenvectors and discarding the complement is not permitted, because the complement changes the same physical quadratic and cross blocks.

## 8. Continuity and final status

* Exit A: bounded **continuous** density, `<=24`.
* Exit B: bounded **continuous** density, `<128`.
* Exits C and D: essential boundedness; continuity not supplied by the cited arguments.
* Chamber E: minority-sign side still open; majority-sign side `<=pi sqrt(2)`.
* Exact rank three: still **OPEN**, but reduced to the explicit chamber E.
* Full arbitrary-rank QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
* Global continuous-density conclusion: **OPEN**.

No Monte Carlo argument, post-rotation independence, arbitrary-joint coarea, conditional projection-height moment, receiver-only fiber supremum, or law-uniform pointwise van der Corput estimate is used.