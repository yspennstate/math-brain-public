SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T21:37:43Z.
attacking: diffuse deletion geometry — force a macroscopic star component transverse to the top-two child eigenspace, then spend it with the completed fleet02/B08 balanced physical half-cut.

# fleet01/B08 r36 — transverse-star amplification after deleting a diffuse spectral coordinate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING STRUCTURAL THEOREM + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

The unrestricted conjecture remains **OPEN**. Continuity for the unrestricted conjecture remains **OPEN**. The paid branch below has a continuous `C_0` density. No moment, support, log-concavity, iid, post-rotation independence, or small-random-perturbation assumption is used.

## 1. The first missing implication attacked

The previous B08 run left, after deleting a physical coordinate of a diffuse selected three-eigenvector frame, a star-plus-two-child state

`A = [[a,b^T],[b,C]]`,

with selected-frame leverage `p<=1/48`, two child singular directions at scale nearly `L`, and a possible small third child singular value. The old dual half-cut estimate treated the literal star only at the weak scale inherited from a spectral-window localization argument. It therefore paid the transverse branch only when

`s_3(C) <= 2.16e-5 L`.

The key observation of this run is that this misses the selected eigenvector equation. If the deleted selected coordinate has small leverage and the child has only two substantial singular directions, then the part of the star **orthogonal to those two child directions must itself be huge**. This is an exact deterministic consequence of `AR=R Lambda`; it does not use a probabilistic tail estimate.

The resulting theorem raises the transverse paid threshold from about `2.16e-5 L` to the clean scale

`s_3(C) <= L/130`,

and gives a continuous density `<183/L` whenever the actual transverse angle is at least `1/2` and the associated physical three-frame is diffuse.

## 2. Source-pinned inputs

### 2.1 Exact owner target and corrections

The source owner target is the full arbitrary-product-law QFORM conjecture. The live source state used here records the full target as OPEN. In particular, the following false interfaces are not used: law-uniform pointwise van-der-Corput decay, arbitrary-joint three-dimensional coarea, positive moments of worst conditional projection caps, post-rotation independence, and naive fiber-sup integration.

### 2.2 Completed designated partner: fleet02/B08 r28

The completed partner result used at an actual inequality is

`yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T153836Z-fleet02-B08-qform-r28/REPORT.md`.

Its Lemma 3.1 is the following balanced physical half-cut. If `W` is an `m x 3` matrix with orthonormal columns and

`max_j ||W_{j,*}||^2 <= 1/48`,

then there is an ORIGINAL-coordinate partition `S disjoint_union T` such that

`(1/4)I_3 <= W_S^T W_S <= (3/4)I_3`,
`(1/4)I_3 <= W_T^T W_T <= (3/4)I_3`.                    (2.1)

The proof is the exact second-moment Rademacher argument in that report. This is the designated partner input applied below.

### 2.3 Literal-cross receiver

The completed volume-stability theorem is at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a literal ORIGINAL-coordinate cross block `M=M_0+E`, if

`s_3(M_0)>=kappa>0`,
`max_j (P_range(M_0))_{jj}<=1/2`,
`||E||_op<=kappa/16`,                                      (2.2)

then the full ambient quadratic-plus-affine form, including arbitrary same-bank curvature and outside couplings, has a continuous `C_0` density satisfying

`||p_Q||_infinity <= (24 sqrt(3) e)/(5 kappa) < 23/kappa`.   (2.3)

No random perturbation is removed in this theorem; the actual cross block is retained.

## 3. New exact theorem: transverse-star amplification

Let `A` be real symmetric. Let `R in R^{n x 3}` have orthonormal columns and

`A R = R Lambda`,
`Lambda=diag(lambda_1,lambda_2,lambda_3)`,
`min_j |lambda_j| >= L >0`.                                  (3.1)

Fix an ORIGINAL coordinate `i`, move it to the first position, and write

`A = [[a,b^T],[b,C]]`.                                        (3.2)

Write the selected row as `v=R_{i,*}` and the remaining rows as `Z=R_{-i,*}`. Put

`p=||v||^2`, so `Z^T Z=I_3-v^T v`.                            (3.3)

Let `U` be the two-dimensional eigenspace spanned by eigenvectors of `C` corresponding to its two largest singular values. Let `P=UU^T`, and put

`C_tail=(I-P)C(I-P)`,
`x=s_3(C)/L=||C_tail||_op/L`,
`r=(I-P)b`, `tau=||r||`.                                      (3.4)

### Theorem 3.1 — `QFORM-DELETE1-TRANSVERSE-STAR-AMPLIFICATION-v1`

If `x<1`, then `p>0` and

`boxed{
 tau >= (1-x) L sqrt((1-p)/p).
}`                                                              (3.5)

Equivalently, if a selected three-frame has very little mass on the deleted physical coordinate and the child matrix is close in operator norm to rank two at scale `L`, then the **actual physical star has a large component transverse to the top-two child eigenspace**.

### Proof

The lower block of the exact eigenvector equation is

`C Z + b v = Z Lambda`.                                        (3.6)

Let `Y=(I-P)Z`. Since `P` is a spectral projection of the symmetric matrix `C`, it commutes with `C`, and projecting (3.6) onto `U^perp` gives

`C_tail Y + r v = Y Lambda`.                                  (3.7)

Column by column,

`(lambda_j I-C_tail)y_j = r v_j`.                              (3.8)

Because `|lambda_j|>=L` and `||C_tail||=xL<L`,

`||(lambda_j I-C_tail)^(-1)|| <= 1/((1-x)L)`.                  (3.9)

Consequently

`||Y||_F^2
 <= tau^2 ||v||^2 / ((1-x)^2 L^2)
 = tau^2 p / ((1-x)^2 L^2).`                                  (3.10)

On the other hand `PZ` has rank at most two. Therefore Eckart--Young gives

`s_3(Z) <= ||Z-PZ||_op = ||Y||_op <= ||Y||_F`.                 (3.11)

From (3.3), the singular values of `Z` are exactly

`1, 1, sqrt(1-p)`,                                             (3.12)

so `s_3(Z)=sqrt(1-p)`. Combining (3.10)--(3.12) proves (3.5).

If `p=0`, then (3.7) reads `C_tail Y=Y Lambda`. Since `Z` has three orthonormal columns while `PZ` has rank at most two, `Y` is nonzero in a third singular direction; this is impossible when `||C_tail||<L`. Thus `x<1` indeed forces `p>0`. QED.

### 3.2 Companion two-child rigidity

The earlier deletion identity can be reproved in one line here. Since

`(A^2)_{-i,-i}=C^2+bb^T >= L^2 Z Z^T`,                         (3.13)

the third eigenvalue of the right side is `(1-p)L^2`. Weyl and the rank-one matrix `bb^T` imply

`boxed{ s_2(C) >= sqrt(1-p)L. }`                               (3.14)

Thus at `p<=1/48`, the top two child singular values are at least

`sigma L`, `sigma=sqrt(47/48)=0.989528507253...`.               (3.15)

## 4. Apply the partner half-cut to an actual density inequality

Assume now

`p<=1/48`,
`x=s_3(C)/L<=1/130`.                                            (4.1)

By Theorem 3.1,

`tau/L >= (1-x)sqrt((1-p)/p)
         >= (129/130)sqrt(47)
         =:tau_0
         =6.802918795782... .`                                  (4.2)

Let `s=b/||b||`, and write its sine-angle from the top-two child plane as

`d=||(I-P)s||=tau/||b||`.                                      (4.3)

Assume the transverse branch

`d>=1/2`.                                                       (4.4)

Set `w=r/tau` and let

`W=[w,U]`.                                                       (4.5)

This is an orthonormal physical three-frame. Assume its actual row leverage is diffuse:

`nu:=max_j ||W_{j,*}||^2 <=1/48`.                              (4.6)

Apply the completed fleet02/B08 r28 balanced-half-cut lemma to this `W`. We obtain an ORIGINAL-coordinate split of the child coordinates,

`{1,...,n-1}=S disjoint_union T`,

with both restricted Gram matrices between `I_3/4` and `3I_3/4`, as in (2.1).

Let `C_2=U D U^T` be the top-two spectral part of `C`; then

`||C-C_2||_op=s_3(C)=xL`.                                      (4.7)

Put the deleted hub coordinate on the `T` side and consider the literal physical cross block

`M=[ C[S,T], b_S ]`.                                            (4.8)

Its structured reference is

`M_0=[ C_2[S,T], b_S ]`.                                       (4.9)

In coefficient coordinates `[w,U]`, write the unit star direction as `z=(d,a_1,a_2)^T`. If `B=||b||/L`, then

`M_0 M_0^T = W_S K W_S^T`,                                    (4.10)

where, using `G_T=W_T^T W_T>=I_3/4`,

`K >= (sigma^2 L^2/4) P_U + B^2 L^2 z z^T`.                    (4.11)

The one-dimensional direction in the `U`-plane orthogonal to the `U`-component of `z` has eigenvalue at least `sigma^2L^2/4`. On the remaining two-plane, determinant divided by trace gives

`lambda_min(K)
 >= B^2 sigma^2 d^2 L^2/(4B^2+sigma^2).`                       (4.12)

Since `G_S>=I_3/4`,

`s_3(M_0)
 >= [B sigma d/(2 sqrt(4B^2+sigma^2))] L.`                     (4.13)

Now `Bd=tau/L`. From `d>=1/2`, `B<=2(tau/L)`. Hence

`s_3(M_0)
 >= [ t sigma/(2 sqrt(16t^2+sigma^2)) ] L`,
`t=tau/L`.                                                       (4.14)

The right side is increasing in both `t` and `sigma`. By (4.2) and (3.15),

`s_3(M_0)>=kappa_0 L`,                                         (4.15)

where

`kappa_0
 := tau_0 sqrt(47/48)
    / [2 sqrt(16 tau_0^2+47/48)]
 =0.12360936305311279... .`                                    (4.16)

This is the promised concrete application of the completed fleet02/B08 half-cut: it has produced an actual rank-three literal crossing at a fixed macroscopic scale.

The range of `M_0` is `range(W_S)`. Therefore

`max_j (P_range(M_0))_{jj}
 <= nu/lambda_min(G_S)
 <=4nu
 <=1/12`.                                                       (4.17)

The actual perturbation is only the literal coefficient block

`M-M_0=[(C-C_2)[S,T],0]`,                                      (4.18)

so

`||M-M_0||_op <= xL <= L/130`.                                 (4.19)

A direct constant check gives

`1/130=0.00769230769230769...
 < kappa_0/16
 =0.00772558519081955... .`                                    (4.20)

Thus (4.15), (4.17), and (4.20) satisfy the completed literal-cross volume-stability theorem (2.2). We conclude:

### Corollary 4.1 — `QFORM-DIFFUSE-TRANSVERSE-STAR-PAID-130-v1`

Under (3.1), if for some deleted original coordinate

`p<=1/48`,
`s_3(C)<=L/130`,
`d>=1/2`,
`max_j ||[w,U]_{j,*}||^2<=1/48`,                               (4.21)

then the **full ambient form**, with all complementary spectrum, same-bank curvature, outside couplings, and conditioning-generated affine terms retained, has a continuous `C_0` density and

`boxed{
 ||p_Q||_infinity
 <= (24 sqrt(3)e)/(5 kappa_0 L)
 =182.8289554729.../L
 <183/L.
}`                                                              (4.22)

This improves the preceding B08 transverse-tail cutoff by a factor greater than `356`: the old sufficient hypothesis was `s_3(C)<=2.15791e-5 L`, whereas (4.21) allows `s_3(C)<=L/130`.

## 5. General tail-angle tradeoff

The same proof gives a useful continuous router rather than only the numerical point `1/130`.

Fix `p_0<1`, `x<1`, and suppose `p<=p_0`. Put

`sigma_0=sqrt(1-p_0)`,
`tau_0(x)=(1-x)sqrt((1-p_0)/p_0)`.                              (5.1)

If the physical angle satisfies `d>=d_0>0` and the frame `[w,U]` has row leverage at most `1/48`, then the partner half-cut produces

`s_3(M_0)>=kappa(x,d_0)L`,                                     (5.2)

where

`kappa(x,d_0)
 = tau_0(x) sigma_0
   / [2 sqrt(4 tau_0(x)^2/d_0^2+sigma_0^2)].`                  (5.3)

Therefore the branch is paid whenever

`x <= kappa(x,d_0)/16`.                                        (5.4)

When `tau_0(x)>32x`, condition (5.4) is equivalent to

`d_0 >= d_crit(x)
 := 64 x tau_0(x)
    / [sigma_0 sqrt(tau_0(x)^2-1024x^2)].`                     (5.5)

For the actual diffuse leverage `p_0=1/48`,

`d_crit(1/130)=0.497843450180... <1/2`.                         (5.6)

More importantly, as `x downarrow0`,

`d_crit(x) = (64/sqrt(47/48)) x + O(x^2)`.                     (5.7)

Thus a low-third-child-singular-value state which escapes the volume receiver must become **proportionally aligned**: its star angle to the top-two child plane is `O(s_3(C)/L)`. This is a substantially narrower obstruction than an unquantified aligned branch.

## 6. What is now left

This run does not claim a full proof. In this deletion chamber, after the new theorem, an unpaid state must enter at least one of the following explicit exits:

1. `s_3(C)>L/130` (a genuine third child direction at a fixed scale);
2. the star is in the near-aligned regime `d<d_crit(x)` (in particular `<1/2` at `x<=1/130`);
3. the physical three-frame `[w,U]` has a row leverage `>1/48` (a localized original-coordinate resource);
4. the initially selected three-frame itself is not diffuse at the deleted coordinate.

The first next B08 implication is therefore

`QFORM-AMPLIFIED-NEARALIGNMENT-OR-HEAVYROW-COMPILER-v1`:

> exploit the fact that in the low-tail survivor the transverse star component is already at least `(1-x)sqrt(47)L`, while an unpaid angle must be `O(x)`, to route the resulting very large aligned star or a heavy physical three-frame row into an existing scalar/pair, grouped-crossing, or localized receiver without discarding the complementary spectrum.

A bare local star is not declared sufficient: the live correction set contains counterexamples to several such shortcuts. The full target and full-target continuity remain OPEN.

## 7. Finite sanity check

A deterministic-seed numerical check sampled 2,000 random symmetric matrices in dimensions `5,7,10,15`, selected the three largest-modulus eigenvectors, deleted one random original coordinate, and tested Theorem 3.1 whenever `x<1`. It found zero violations; the smallest numerical slack was positive. This finite check is only diagnostic. The proof is the exact eigenvector/rank argument in Section 3.
