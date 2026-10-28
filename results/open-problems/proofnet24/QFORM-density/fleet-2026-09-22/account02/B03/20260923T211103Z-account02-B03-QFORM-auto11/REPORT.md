SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T21:11:03Z.
attacking: remove the last two-volume row-marginal gate at the half-Riesz endpoint, then splice one genuine physical square to obtain one-copy linear small-ball scale.

# account02/B03 — marginal-free two-volume half-Riesz theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Decoupled time integral / complementary constructions and source-valid counterexamples  
**Status:** `NEW SUPPORTING THEOREM / Z2 HALF-RIESZ MARGINAL GATE REMOVED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. Continuity is not asserted by the square-peel conclusion below. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced.

## 1. Sources and live corrections used


Pinned package actually used: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `FOURIER_ROUTE_REPORT.md` Section 1.2. Its volume-sampling decoupling proof is valid for general volume degree `k`; at `k=2`, under two-volume row marginals `alpha_i<=1/2`, it gives the critical one-copy envelope used in Branch A below. The square peel from the same package is used in Corollary 4.1.

Fresh crossing source actually used: `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` at the fresh source commit. I use (i) the grouped projected-crossing theorem at `(k,ell)=(1,1)` and (ii) its exact-rank-two arbitrary-internal-functions crossing theorem.

Designated partner consumed: account03/B03 latest completed report visible at this invocation, `20260923T181128Z-account03-B03-QFORM-r36/REPORT.md`. Its proved effective-dimension squared-time compiler is applied in Section 5 below to an actual target-valid residual, giving a quantitative collision inequality.

## 2. Statement

Let

`Q(X)=X^T A X+b^T X+c`,

where the scalar coordinates of `X` are independent and each density is bounded by one. Let `I,J` be disjoint sets of genuine original coordinates, condition freely on every coordinate outside `I union J`, and put

`M=A[I,J]`,

`Z_2=e_2(MM^T)=sum_{|S|=|T|=2} det(M_{S,T})^2`.

Assume `Z_2>0`. Define

`H_{1/2}(Q)=sup_s E|Q-s|^{-1/2}`.

### Theorem 2.1 — `QFORM-Z2-HALFRIESZ-MARGINAL-FREE-v1`

Without **any** two-volume row-marginal hypothesis,

`boxed:
 H_{1/2}(Q) <= 8 e^(1/4) Z_2^(-1/8).
}`

Numerically the outer constant is

`8 e^(1/4)=10.2722033335019...`.

All same-side quadratic blocks, all diagonal terms, all affine terms, and all conditioned outside-coordinate contributions are arbitrary.

For an independent copy `Q'`, the same theorem immediately gives

`E|Q-Q'|^(-1/2) <= 8 e^(1/4) Z_2^(-1/8)`

by conditioning on `Q'`. The partner's sharper squared-time compiler improves the collision constant to

`boxed:
 E|Q-Q'|^(-1/2) <= (16/3)e^(1/4) Z_2^(-1/8),
}`

and therefore, using the exact whole-copy Riesz identity,

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (16/3)sqrt(2pi)e^(1/4) Z_2^(-1/8).
}`

The constants here are about `6.84813555567` and `17.1657302123`, respectively.

## 3. Proof of Theorem 2.1

Let `w_{S,T}=det(M_{S,T})^2/Z_2` be the two-volume sampling law and let

`alpha_i=P_w(i in S)`

be its row marginals. Thus `sum_i alpha_i=2`.

A basic identity used repeatedly below is the one-copy Riesz representation. If

`|phi_Y(t)| <= min(1,K|t|^-1)`,

then the weighted Fourier integral is absolutely convergent and

`sup_s E|Y-s|^-1/2
 <= (2pi)^(-1/2) int |t|^-1/2 |phi_Y(t)|dt
 <= 8 (2pi)^(-1/2) K^(1/2).`                                      (3.1)

This uses only the distributional identity

`int_R |t|^-1/2 exp(itx)dt=sqrt(2pi)|x|^-1/2`

with a standard positive regularization. Near zero the weight is integrable; at infinity the displayed `1/|t|` envelope makes the absolute integral finite.

### Branch A: all two-volume row marginals are at most one half

The pinned arbitrary-`k` volume-sampling decoupling proof, specialized to `k=2,q=1`, gives

`|phi_Q(t)|^2 <= e(2pi)^2 |t|^-2 Z_2^-1/2`.

Equivalently,

`|phi_Q(t)| <= min{1, 2pi sqrt(e) Z_2^-1/4 |t|^-1}.`                (3.2)

Applying (3.1) with `K=2pi sqrt(e)Z_2^-1/4` gives

`H_{1/2}(Q) <= 8 e^(1/4) Z_2^-1/8.`                               (3.3)

This is the eventual worst branch.

### Branch B: one heavy physical row, projected remainder spread

Suppose some original row `m=M_i` has `alpha_i>1/2`. Let

`S=||m||_2`,

and for every remaining row `n_j` of `M` put

`c_j=n_j(I-P_m)`.

Set

`F^2=sum_j ||c_j||_2^2`.

The numerator of the volume marginal of row `i` is the sum of the squared areas of the pairs `(m,n_j)`. By Cauchy-Binet/Lagrange's identity,

`boxed:
 S^2 F^2 = alpha_i Z_2 > Z_2/2.
}`                                                                  (3.4)

Assume first that every projected one-volume row marginal satisfies

`||c_j||^2/F^2 <=1/2`.

Promote the genuine original coordinate `i` to a one-dimensional hub. The fresh grouped projected-crossing theorem with `(k,ell)=(1,1)`, hub-density cap `M_H<=1`, hub crossing singular value `S`, and projected one-volume `Z_1=F^2`, gives

`|phi_Q(t)| <= min{1,2pi(SF)^-1/2 |t|^-1}.`                        (3.5)

Equation (3.1) yields

`H_{1/2}(Q) <=8(SF)^-1/4
 <8*2^(1/8) Z_2^-1/8
 <8e^(1/4) Z_2^-1/8.`                                               (3.6)

The hub coordinate remains a physical original coordinate; no rotated coordinate is declared independent.

### Branch C: a second heavy projected physical row

Otherwise choose a remaining physical row `n_j` with

`||c_j||^2>F^2/2`.

Condition on all other coordinates on the `I` side. The two genuine original coordinates `i,j` then cross the `J` bank through the literal two-row matrix having rows `m,n_j`. It has exact rank two. If `Delta` denotes the product of its two nonzero singular values, then

`Delta^2=det Gram(m,n_j)=S^2||c_j||^2
 >S^2F^2/2
 =alpha_i Z_2/2
 >Z_2/4.`                                                           (3.7)

For the exact-rank-two crossing theorem, the two-dimensional projection on the physical two-coordinate side has density cap at most one (orthogonal change of variables in exactly two original coordinates), while the orthogonal two-dimensional projection of the product `J` bank has density cap at most two. Arbitrary internal functions on both sides are allowed. Hence

`|phi_Q(t)| <= min{1,pi sqrt(2) Delta^-1/2 |t|^-1}.`                (3.8)

Using (3.1),

`H_{1/2}(Q)
 <=8*2^-1/4 Delta^-1/4
 <8 Z_2^-1/8.`                                                       (3.9)

Branches A-C are exhaustive, proving Theorem 2.1. Notice that the heavy-row recursion terminates after at most two promotions because the target volume degree is two.

## 4. One physical square converts the theorem to linear one-copy small ball

Suppose an original coordinate `Z` has physical diagonal `d!=0`. Exact completion gives

`Q=d[Z+h(W)]^2+R(W)`,                                               (4.1)

where `Z` is still independent of the original-coordinate background `W`; the quadratic part of `R` is the physical Schur complement. The pinned square-peel inequality is

`||p_Q||_infinity <= |d|^-1/2 H_{1/2}(R).`                         (4.2)

Therefore:

### Corollary 4.1 — `QFORM-SQUARE-PLUS-Z2-MARGINAL-FREE-v1`

If some physical cut of the Schur residual has two-volume `Z_2>0`, then

`boxed:
 ||p_Q||_infinity
 <=8 e^(1/4)|d|^-1/2 Z_2^-1/8
 =8e^(1/4)(|d|^4 Z_2)^-1/8.
}`                                                                  (4.3)

Consequently every interval `B` satisfies the actual linear small-ball estimate

`boxed:
 P(Q in B) <=8 e^(1/4)(|d|^4 Z_2)^-1/8 |B|.
}`                                                                  (4.4)

This is an essential-density statement. Continuity is deliberately left separate.

The main analytic gain is that **there is no longer any row-marginal gate whatsoever at the two-volume half-Riesz level**. A future structural proof only has to produce quantitative `|d|^4 Z_2`, not also certify spread of the two-volume sampling law.

## 5. Designated-partner application to an actual target-valid no-pivot family

Take an integer `N>=2`, let `m=2N^6`, let `u,v in R^m` be flat orthonormal vectors, and put `w=(1,1)/sqrt(2)`. For independent cap-one coordinates define

`R_N=2N^2 X_h <u,Y> + 2N^2 <w,Z><v,Y>`,

`Q_N=R_N+N^-1 X_s^2.`                                               (5.1)

The physical matrix of `R_N` is bipartite with exactly two nonzero crossing singular values, both equal to `N^2`. Thus its nonzero eigenvalues are

`+N^2,-N^2,+N^2,-N^2`,

and `Q_N` has those four eigenvalues plus `N^-1`. Hence the family is inside the exact owner target for every `N`.

Because the crossing vectors are flat,

`max_i |A_ii|=N^-1`,

and every physical `2x2` principal determinant is `O(N^-2)`; explicitly the largest one from the first star is `1/(2N^2)`. Thus this family enters every fixed no-pivot regime as `N` grows.

For the Schur residual after peeling `X_s`,

`Z_2=N^8`,                                                            (5.2)

so Corollary 4.1 already gives

`||p_{Q_N}||_infinity <= 8e^(1/4) N^-1/2.`                          (5.3)

Now apply the designated partner account03/B03 r36 effective-dimension squared-time lemma to the **actual** exact-rank-two residual. The fresh exact-rank-two crossing theorem gives here

`|phi_{R_N}(t)| <= min{1, 2pi N^-2 |t|^-1}.`                        (5.4)

In the partner notation this has `d=2` and `K=2pi N^-2`. Their completed Lemma 2.1 therefore yields

`boxed:
 int_R |t|^-1/2 |phi_{R_N}(t)|^2 dt
 <= (16/3)sqrt(2pi) N^-1,
}`                                                                  (5.5)

and the whole-copy identity gives

`boxed:
 E|R_N-R_N'|^-1/2 <=16/(3N).
}`                                                                  (5.6)

Their `L2` consequence gives

`||p_{R_N}||_2^2 <=4/N^2`,

hence the actual linear collision small-ball estimate

`boxed:
 P(|R_N-R_N'|<=eps) <=8 eps/N^2.
}`                                                                  (5.7)

No sum/difference coordinate is detached from its conjugate partner anywhere in (5.5)-(5.7).

For this exact-rank-two family one can also use the absolutely convergent **one-copy** half-Riesz integral directly in (5.4), improving (5.3) to

`H_{1/2}(R_N)<=8/N`,

and hence

`boxed:
 ||p_{Q_N}||_infinity <=8/sqrt(N).
}`                                                                  (5.8)

Thus a vanishing physical square can be more than compensated by aggregate two-volume strength. The invariant visible to the marginal-free receiver is

`|d|^4 Z_2=N^4`.

## 6. Sharper collision version of the general theorem

The partner's effective-dimension compiler can be applied branch-by-branch in the proof of Theorem 2.1, rather than bounding the collision potential by the one-copy potential.

In Branch A, (3.2) has `d=2`, `K=2pi sqrt(e)Z_2^-1/4`; hence

`E|Q-Q'|^-1/2 <=(16/3)e^1/4 Z_2^-1/8.`                             (6.1)

In Branch B the constant is at most `(16/3)2^(1/8)`, and in Branch C it is at most `16/3`, both strictly smaller than the Branch-A constant. Therefore (6.1) is global, and multiplication by `sqrt(2pi)` gives the time integral stated in Theorem 2.1.

This is the requested dependence-safe decoupled-time output: the entire copy difference is retained until the final scalar Riesz identity.

## 7. What is still unpaid

This run removes an analytic condition, not the remaining structural debt. The next unpaid implication can now be stated more cleanly:

> Starting only from `s_3(A)>=1` in the no-pivot/hub survivor, prove a product-preserving quantitative alternative that either produces a physical pivot `d` and a Schur residual cut with `|d|^4 Z_2>=c>0`, or lands in one of the already-paid zero-diagonal/grouped-hub/rank-three-crossing/low-rank-carrier exits.

No claim is made that such a lower bound follows from the spectrum alone without alternatives. In particular the live correction forbidding a universal rank-three physical cut remains binding, and exact zero-diagonal target families force separate grouped-hub/crossing receivers.

The new theorem means that **two-volume concentration itself is no longer an obstruction**: if `Z_2` is present after a square peel, a heavy row is automatically promoted to a real hub, and if the projected one-volume is itself concentrated, a second physical row automatically forms an exact-rank-two crossing. No extra spread hypothesis survives.

## 8. Scope and audit

- full QFORM: OPEN;
- unrestricted continuity: OPEN;
- no counterexample claimed;
- arbitrary original-coordinate product laws with density caps one are allowed;
- no support/moment/log-concavity assumptions;
- no post-rotation probabilistic independence;
- no false pointwise quadratic Fourier estimate;
- no conditioning that turns a conjugate sum/difference into an independent cap-one variable;
- rotations are used only inside deterministic singular-value/projection-density statements;
- all outside coordinates are handled only by legitimate conditioning, which produces affine/internal terms allowed by the cited crossing theorems.

The first unpaid implication has changed: the previous two-volume row-marginal check is paid completely; only the structural extraction of a square-plus-two-volume invariant, or a complementary already-paid exit, remains.
