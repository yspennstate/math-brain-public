SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T22:47:30Z.
attacking: route rough clean-bank curvature by conditioning a physical quadratic vertex cover, retain the grouped top-two crossing norm, and upgrade the clean-bank rearrangement branch to a continuous C0 density.

# fleet01/B04 — curvature-cover product rearrangement

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Execution status: `WITHOUT_VERIFIED_BRAIN`.
Mathematical status: `NEW SUPPORTING THEOREM / PARTNER APPLIED / C0 REGULARITY PROVED IN BRANCH / FULL TARGET OPEN`.

The unrestricted conjecture is **not** proved here. No moment, support, centering, Gaussian, log-concavity, connected-support, or post-rotation independence assumption is used. All conditioning is on original independent coordinates.

## 1. Pinned completed input

The designated partner result used here is fleet02/B04's completed theorem

`QFORM-CLEANBANK-TOPTWO-REARRANGEMENT-v1`

at

`yspennstate/math-open-problems@dfe442ee899867f5677e5ced85a196eca922fe64`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T211520Z-fleet02-B04-qform/REPORT.md`.

For disjoint original-coordinate product banks `X,Y`,

`Q=F(X)+2 X^T M Y+b^T Y+c`,

with arbitrary measurable `F(X)` and no `Y-Y` quadratic term, if the top two singular values of `M` are `s1>=s2>0`, then

`||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2)`.                     (1.1)

The partner proof conditions on the original X-bank, uses the product linear-form density bound

`||p_(Q|X=x)||_infinity <=1/[sqrt(2)||M^T x+b/2||_2]`,               (1.2)

projects only the deterministic coefficient norm onto the top-two left singular frame, uses the joint density cap `<=2` for that projection, and applies decreasing rearrangement to `|w|^(-1)` in `R^2`.

I also use the exact parameter version already checked in the preceding B04 run: if the top-two left projection `U_2^T X` has density cap `L_X`, then the same proof gives

`||p_Q||_infinity <= sqrt(2 pi L_X) (s1s2)^(-1/2)`.                  (1.3)

For an X-bank consisting of exactly two original coordinates, `U_2` is a two-dimensional orthogonal matrix, hence the transformed joint density is at most one and `L_X<=1`.

## 2. New theorem: condition a quadratic vertex cover

### Theorem 2.1 — `QFORM-CURVATURE-VERTEX-COVER-REARRANGEMENT-v1`

Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` be disjoint banks of original independent real random variables, every scalar density bounded by one. Let

`Q=F(X)+2X^T M Y+Y^T C Y+b^T Y+c`,                                  (2.1)

where `F` is arbitrary measurable and `C=C^T` is arbitrary.

Let `R subset J` and put `L=J\R`. Assume

`C[L,L]=0`.                                                           (2.2)

Equivalently, every nonzero physical quadratic coefficient inside the Y-bank is incident to at least one coordinate of `R`; diagonal coefficients count as loops and force that coordinate into `R`.

Let

`s1=s1(M[:,L]) >= s2=s2(M[:,L]) >0`.                                (2.3)

Then `Q` has a density with a continuous representative vanishing at infinity, and

`boxed:
 ||p_Q||_infinity <=2 sqrt(pi) (s1 s2)^(-1/2),
 p_Q in C_0(R).`                                                      (2.4)

More generally, if the top-two left projection of the original X-bank has joint density cap `L_X`, then

`boxed:
 ||p_Q||_infinity <=sqrt(2 pi L_X) (s1s2)^(-1/2).`                    (2.5)

In particular, if the X-bank consists of exactly two original physical coordinates,

`boxed:
 ||p_Q||_infinity <=sqrt(2 pi) (s1s2)^(-1/2).`                        (2.6)

### Proof of the density bound

Condition only on the original coordinates `Y_R=r`. Since `C[L,L]=0`, the remaining Y_L dependence is exactly linear:

`Q=F_r(X)+2X^T M_L Y_L+beta_r^T Y_L+c_r`,                            (2.7)

where

`M_L=M[:,L]`,
`beta_r=b_L+2C[L,R]r`,

and every term involving only `X` and `r` has been absorbed into `F_r,c_r`.

For every fixed `r`, (2.7) is exactly within the completed fleet02/B04 theorem. Its constant is translation-uniform in `beta_r`; hence

`||p_(Q|Y_R=r)||_infinity
 <=2 sqrt(pi)(s1s2)^(-1/2)`                                          (2.8)

for almost every `r`. Averaging the conditional densities proves existence of an unconditional density and (2.4)'s height bound. The same argument with the exact projection cap `L_X` gives (2.5).

### New regularity step: the same branch is actually C0

The partner theorem did not claim continuity. Here it can be recovered without any extra hypothesis.

Fix `r`. Given also `X=x`, the random Y_L part is the linear form

`a(x,r)^T Y_L`,
`a(x,r)=2M_L^T x+beta_r`.                                             (2.9)

Because `rank(M_L)>=2`, for almost every `x` the coefficient vector `a(x,r)` has at least two nonzero physical coordinates. Indeed, for a fixed coordinate `j`, the set on which every coefficient except possibly the j-th vanishes is the solution of

`M_{L\{j}}^T x = -beta_{r,L\{j}}/2`.                                 (2.10)

The matrix on the left is not identically zero, because otherwise all columns except the j-th would vanish and `rank(M_L)<=1`. Thus (2.10) lies in an affine hyperplane (or is empty), hence has Lebesgue measure zero. A finite union over `j` is still null. The X-law is absolutely continuous, so the bad set has probability zero.

Whenever at least two coefficients are nonzero, the density of `a(x,r)^T Y_L` is a convolution of two scaled L1 densities, followed by convolution with probability measures from the remaining coordinates. Therefore that conditional density lies in `C_0(R)`.

Moreover the partner proof supplies the pointwise majorant

`||p_(Q|X=x,Y_R=r)||_infinity
 <= 1/[sqrt(2)||M_L^T x+beta_r/2||_2]`.                              (2.11)

The decreasing-rearrangement calculation shows that its X-expectation is bounded uniformly in `r` by the right side of (2.4), or by (2.5) when `L_X` is retained. Thus dominated convergence, first over X and then over Y_R, gives both continuity and vanishing at infinity of the unconditional density. This proves the C0 assertion.

No continuity of any input density is used; only their L1 property and independence are needed for the two-factor convolution.

## 3. Exact structural currency: removing the curvature cover

Write the crossing columns as

`M=[M_R M_L]`.

Then there is the exact positive-semidefinite identity

`M_L M_L^T = M M^T - M_R M_R^T`.                                    (3.1)

Let

`delta=||M_R||_op` and `sigma=s2(M)`.

Since `M_R M_R^T <= delta^2 I`, Loewner monotonicity gives

`boxed:
 s2(M_L)^2 >= sigma^2-delta^2.`                                      (3.2)

Hence whenever `delta<sigma`, Theorem 2.1 applies and, using `s1(M_L)>=s2(M_L)`,

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi) / sqrt(sigma^2-delta^2),
 p_Q in C_0.`                                                        (3.3)

With an exact projection cap `L_X`, replace the numerator by `sqrt(2pi L_X)`.

A still more elementary sufficient condition is

`sum_{j in R} ||m_j||_2^2 < sigma^2`,                                (3.4)

because `delta^2<=||M_R||_F^2`.

Thus arbitrary rough Y-curvature is already harmless whenever its physical support admits a quadratic vertex cover whose crossing columns do not consume the entire second crossing singular direction. No coefficient of C enters the density constant: those variables are conditioned rather than perturbatively estimated.

This is important under the owner's no-moment assumptions. A small operator norm of a random quadratic remainder cannot be treated as a small random error, but exact conditioning on original coordinates is legal and costs no moments.

## 4. Direct application to the partner's rough-Z gap

The designated partner report quotes the zero-anchor factorization

`2(b^T Y_N)(X_h+p^T Y_N)
 +2Y_N^T E_NZ Y_Z
 +Y_Z^T E_ZZ Y_Z`.                                                    (4.1)

Its clean case `E_ZZ=0` was the partner's completed application. Theorem 2.1 strictly extends that branch.

Take the curved bank to be `X=Y_N` and the prospective clean bank to be `(X_h,Y_Z)`. Let `R subset Z` satisfy

`E[Z\R,Z\R]=0`.                                                       (4.2)

Condition the original coordinates `Y_R`. The surviving clean-bank crossing is

`K_R=[ b , E[N,Z\R] ]`.                                               (4.3)

If

`s2(K_R)>0`,                                                         (4.4)

then

`boxed:
 ||p_Q||_infinity
 <=2sqrt(pi)[s1(K_R)s2(K_R)]^(-1/2),
 p_Q in C_0.`                                                        (4.5)

Thus the first unpaid partner implication

`QFORM-C1-STAR-FACTOR-ROUGH-ZCURVATURE-RECEIVER-v1`

is paid whenever the rough residual curvature has a physical vertex cover that leaves two grouped crossing directions. The remaining C1 branch is correspondingly narrower: every such curvature cover must destroy the target-scale second crossing direction, or another completed pair/D5/ridge/projected-crossing/grouped-hub mechanism must fire.

## 5. Diffuse genuinely rotated indefinite family

The next family shows simultaneously that

1. the curvature conditioned away can have order-one operator norm;
2. every physical crossing coefficient can be nonzero;
3. every useful individual leaf-leaf 2x2 minor can tend to zero;
4. the grouped clean-bank currency remains constant;
5. the exact target spectral hypothesis still holds uniformly.

Let `m>=2` be even. The X-bank has two original coordinates. The Y-bank is

`Y=(Y_r,Y_1,...,Y_m)`.

Define the `2 x (m+1)` crossing matrix

`M_m=[c, L_m]`,
`c=(1/10,1/5)^T`,                                                     (5.1)

where the first `m/2` columns of `L_m` are

`a=(2/sqrt(m))(1,1)^T`

and the last `m/2` are

`d=(2/sqrt(m))(1,-1)^T`.                                              (5.2)

Every cross coefficient is nonzero. Directly,

`L_m L_m^T=4 I_2`,                                                    (5.3)

so its singular values are exactly

`s1(L_m)=s2(L_m)=2`,                                                  (5.4)

and

`det(L_m L_m^T)=16`.                                                  (5.5)

Binet-Cauchy makes the aggregate nature explicit. Same-type leaf pairs have determinant zero; opposite-type pairs have

`|det[a,d]|=8/m`.                                                     (5.6)

There are `m^2/4` opposite-type pairs, and therefore

`(m^2/4)(8/m)^2=16=det(L_mL_m^T)`.                                   (5.7)

So every nonzero individual two-minor tends to zero like `m^(-1)`, while the grouped two-volume is exactly constant.

Put arbitrary nonseparable curvature on the X-bank, for definiteness

`F=(1/10)[[1,1],[1,-1]]`,                                             (5.8)

and put an order-one Y-curvature star on the coordinate `r`:

`C_m[rr]=1/2`,
`C_m[r,j]=C_m[j,r]=1/(2sqrt(m))` for every leaf j,
`C_m[i,j]=0` for all leaf-leaf pairs.                                 (5.9)

Thus `R={r}` is a quadratic vertex cover and `C_m[L,L]=0` after deleting r.

The star is not a vanishing operator perturbation. On the span of `e_r` and the normalized all-ones leaf vector its matrix is

`[[1/2,1/2],[1/2,0]]`,                                                (5.10)

hence

`||C_m||_op=(1+sqrt(5))/4=0.8090169943...`                            (5.11)

for every m.

Let

`A_m=[[F,M_m],[M_m^T,C_m]]`.                                         (5.12)

To verify the owner's exact spectral target, first remove F and C_m. Since

`M_m M_m^T=4I_2+cc^T`,                                                (5.13)

the second singular value of `M_m` is exactly two. Therefore the zero-self-block matrix has two positive and two negative eigenvalues of modulus at least two. The self-block perturbation has norm

`max{sqrt(2)/10,(1+sqrt(5))/4}=(1+sqrt(5))/4`.                        (5.14)

Weyl's inequality leaves two positive and two negative eigenvalues of `A_m` with modulus at least

`2-(1+sqrt(5))/4=(7-sqrt(5))/4
 =1.1909830056250525... >1`.                                          (5.15)

Hence every `A_m` satisfies the exact target, with four eigenvalues of absolute value greater than one.

Now condition only on the original coordinate `Y_r`. The entire order-one Y-curvature star disappears into the conditioned shift, and the surviving clean-bank crossing is exactly `L_m`.

Applying the designated fleet02/B04 theorem **exactly as stated** gives

`boxed:
 ||p_(X^T A_m X)||_infinity <= sqrt(pi)
 =1.772453850905516...`                                               (5.16)

uniformly in m and in every admissible cap-one product input law.

Because the X-bank consists of exactly two physical coordinates, the exact top-two projection density cap is one. The sharpened parameter version (2.5) therefore gives

`boxed:
 ||p_(X^T A_m X)||_infinity <=sqrt(pi/2)
 =1.253314137315500...,
 p_(X^T A_m X) in C_0(R).`                                            (5.17)

By contrast, selecting only one opposite-type leaf pair before applying the same two-dimensional rearrangement would use `s1s2=8/m` and yield

`sqrt(2pi)(8/m)^(-1/2)=sqrt(pi m)/2`,                                 (5.18)

which diverges like `sqrt(m)`. The grouped theorem therefore removes an artificial single-minor loss while simultaneously allowing an order-one rough curvature bank through exact physical conditioning.

## 6. What this does and does not solve

This run closes a real subbranch of the designated partner's first unpaid rough-curvature implication:

- `E_ZZ=0` is no longer the endpoint of the grouped clean-bank mechanism;
- any exact physical quadratic vertex cover of `E_ZZ` can be conditioned;
- the only price is deletion of its crossing columns;
- the exact currency after deletion is the grouped top-two singular product, not one local minor;
- the branch actually has a continuous C0 density.

The full conjecture remains OPEN because a general rough `E_ZZ` can have dense support, and every curvature vertex cover may carry a target-scale fraction of the second crossing direction. No argument here converts that strongly intertwined case into a universal bound.

The first remaining implication for this mechanism is therefore

`QFORM-C1-ROUGH-CURVATURE-COVER-OR-INTERTWINED-ROUTING-v1`:

> Starting from the zero-anchor C1 factorization, either find a physical curvature vertex cover `R` for `E_ZZ` such that `[b,E_N,Z\R]` retains target-scale top-two singular product, or show that failure of every such cover forces a completed pair/D5/ridge/projected-crossing/grouped-hub receiver. The proof must retain original-coordinate product provenance and cannot treat a small matrix remainder as a small random quadratic error without moments.

The current correction `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1` is respected: this theorem never asks slope innovation to absorb an arbitrary completed remainder. It removes the covered curvature exactly by conditioning original coordinates.

## 7. Source and verification status


No source-matching published theorem was found or claimed for this exact curvature-cover splice. Independent review of the new theorem is pending; therefore its status is a supporting theorem, not a fleet-level proved claim and not a full solution.