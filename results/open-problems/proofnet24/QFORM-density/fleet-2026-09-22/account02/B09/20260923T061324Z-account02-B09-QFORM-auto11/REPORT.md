SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T06:13:24Z.
attacking: pay the partner rank-split k=2 branch: two physical core directions plus a disjoint outside line, retaining arbitrary dense within-bank curvature via source-coordinate conditional linear anti-concentration.

# account02/B09 auto11 — k=2 physical core-pair extraction, a paid semidefinite endpoint, and the cancellation obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED + REFUTED_INTERMEDIATE_EXTENSION / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This run does not claim an exhaustive payment of the partner `k=2` rank-split survivor. It proves a quantitative original-coordinate extraction from that survivor, pays a genuine target-valid exact endpoint, applies the required newest-Claude mixed-hub theorem to a distinct dense same-side star, and gives an exact source-law obstruction showing why arbitrary within-bank residual curvature cannot simply be placed behind the favorable coefficient decomposition.

No moments, compact support, connected support, log-concavity, identical-law hypothesis, Gaussianity, post-rotation independence, arbitrary-joint coarea, worst conditional-density supremum, pointwise law-uniform stationary phase, or small-random-error argument is used.

## 1. First unpaid implication

The newest completed designated-partner input is account03/B09 r24,

`QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1`,

canonical source

`yspennstate/math-open-problems@9fcac412f233f09c6ee5e8a1140207d596cce8a2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T045157Z-account03-B09-QFORM-r24/REPORT.md`.

For an orthonormal three-frame `U` in original physical coordinates and determinant-weighted disjoint-basis mass `rho`, the partner proves that for every `eta in (0,1)` either `rho>=eta^3/2`, or a Pluecker subfamily of total weight at least `1/6` has one of three literal physical-bank rank splits. In its `k=2` case a physical triple `S` carries two coefficient-space directions with singular values at least `sqrt(1-eta)`, while the disjoint physical bank `T=S^c` carries the complementary line with singular value greater than `sqrt(eta)`.

The first unpaid B09 implication is therefore not to rediscover the rank split. It is:

`QFORM-K2-ACTUALCORE-OR-EXTERNAL-SMOOTHER-v1`:

> convert the partner `k=2` coefficient geometry into an actual density payment after arbitrary same-bank curvature has been included in the total matrix, without paying a vanishing individual coefficient and without treating a small matrix term as a small random quadratic perturbation.

This report advances that implication and isolates its exact cancellation gate.

## 2. Required newest-Claude package actually used

I used the owner-required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed results from that exact source are applied below at equations, not merely cited:

1. `COUNTEREXAMPLE_SEARCH.md` proves that a rank-two positive-semidefinite form with nonzero eigenvalues `lambda_1,lambda_2>0`, formed from a two-dimensional orthogonal projection of a cap-one product law, has

`||p||_infinity <=2 pi/sqrt(lambda_1 lambda_2)`.                (2.1)

2. `RESULTS.md`, Theorem H, gives the mixed-hub Fresnel/Brascamp--Lieb estimate for one or more original physical hub coordinates and an exact leaf block

`A_II=D+sum_k lambda_k v_kv_k^T`,                              (2.2)

where `D` is diagonal. It keeps `A_HH,A_HJ,A_IJ,A_JJ` arbitrary after conditioning and works entirely in the original product coordinates. I apply it to a target-valid indefinite dense leaf star in Section 6.

The source itself states that these are supporting tools and the unrestricted conjecture remains open.

## 3. New extraction theorem: a `k=2` rank split contains a quantitative physical core pair and an aggregate outside line

Let `U in R^(N x 3)` have orthonormal columns and rows `u_i^T`. Suppose a physical triple `S` belongs to the partner `k=2` branch at scale `eta`. Thus there is an orthogonal decomposition

`R^3=F direct_sum span(f)`, `dim F=2`, `|f|=1`,                 (3.1)

such that

`singular_min(P_S U|_F) >= sqrt(1-eta)`,                       (3.2)

and, with `T=S^c`,

`||P_T U f||_2 > sqrt(eta)`.                                   (3.3)

### Theorem `QFORM-K2-COREPAIR-LINE-EXTRACTION-v1`

There are distinct original physical coordinates `i,j in S` such that, with `a_l=P_F u_l`,

`boxed: |det_F(a_i,a_j)| >= (1-eta)/sqrt(3)`,                  (3.4)

and the corresponding two-row map from `F` obeys

`boxed: singular_min([a_i^T;a_j^T]|_F) >=(1-eta)/sqrt(6)`.     (3.5)

At the same time the disjoint original-coordinate bank `T` carries the coefficient vector

`r=(<u_t,f>)_(t in T)`                                        (3.6)

with

`boxed: ||r||_2>sqrt(eta)`.                                   (3.7)

Consequently the aggregate scalar `Z=r^T X_T` has the source-valid one-dimensional product-marginal cap

`||p_Z||_infinity <=sqrt(2)/||r||_2 <sqrt(2/eta)`.             (3.8)

Equation (3.8) is a marginal-density statement only. No independence between `Z` and any other projection of the same `X_T` is asserted.

### Proof

Use an orthonormal basis of `F`. The `3 x 2` matrix `P_S U|_F` has both singular values at least `sqrt(1-eta)`. Cauchy--Binet therefore gives

`sum_(i<j in S) det_F(a_i,a_j)^2
 =det[(P_S U|_F)^T(P_S U|_F)]
 >=(1-eta)^2`.                                                 (3.9)

There are exactly three physical pairs in `S`, so one pair satisfies (3.4). Each row of `U` has norm at most one; hence the selected `2 x 2` map has operator norm at most its Frobenius norm, at most `sqrt(2)`. Its two singular values multiply to the determinant magnitude in (3.4), proving (3.5).

Finally

`||r||_2^2=f^T U_T^T U_T f=||P_T U f||_2^2>eta`,               (3.10)

which is (3.7). The standard product-marginal theorem for a linear combination of independent cap-one coordinates gives (3.8). QED.

At the partner's concrete scale `eta=1/16`, this produces

`|det_F(a_i,a_j)| >=15/(16sqrt(3))>0.5412`,                    (3.11)

`singular_min >=15/(16sqrt(6))>0.3827`,                        (3.12)

and

`||r||_2>1/4`.                                                  (3.13)

The point is the order of operations: all three physical pair minors on the core triple are summed before one pair is selected, and the third direction remains an entire disjoint original-coordinate bank before any reciprocal payment.

## 4. A genuine paid `rho=0`, `k=2` target endpoint

The source theorem (2.1) pays an exact semidefinite physical-core branch with arbitrary dense curvature on the disjoint remainder.

### Theorem `QFORM-K2-BLOCKSEPARATED-SEMIDEFINITE-v1`

Partition the original coordinates as `S union K`. Suppose

`A_SK=0`,                                                       (4.1)

and the actual physical principal block `B=A_SS` is rank two and semidefinite, with its two nonzero eigenvalues of the same sign and magnitudes at least `s>0`. The complementary block `A_KK` is completely arbitrary. Then for arbitrary independent cap-one inputs,

`boxed: ||p_(X^TAX)||_infinity <=2 pi/s`,                       (4.2)

and every interval `L` satisfies

`boxed: P{X^TAX in L} <=(2 pi/s)|L|`.                           (4.3)

### Proof

Reflect the output if necessary, so the two nonzero eigenvalues of `B` are positive. The source rank-two theorem (2.1) gives

`||p_(X_S^T B X_S)||_infinity
 <=2 pi/sqrt(lambda_1lambda_2)
 <=2 pi/s`.                                                     (4.4)

Because (4.1) makes `X_S^T B X_S` independent of the full arbitrary complementary quadratic variable `X_K^T A_KK X_K`, the total law is their convolution, and convolution with a probability measure cannot raise the essential supremum. This proves (4.2)-(4.3). QED.

### Exact target packet in the partner `k=2` geometry

Let `S={1,2,3}`, `e=(1,1,1)/sqrt(3)`, and let `v_1,v_2` be an orthonormal basis of `e^perp`. Then

`P_F=v_1v_1^T+v_2v_2^T=I-ee^T`                                (4.5)

is a genuinely dense physical `3 x 3` same-side block with spectrum `{1,1,0}`. On a disjoint physical hub `h` and disjoint bank `T`, choose a unit vector `c` and put

`Q=X_S^T P_F X_S+2X_h<c,X_T>+H(X_R)`,                          (4.6)

where `R` is any further disjoint original-coordinate bank and `H` is an arbitrary quadratic form there.

The first term is independent of the remainder and (4.2) gives

`boxed: ||p_Q||_infinity <=2 pi <6.284`.                        (4.7)

The matrix has eigenvalues `1,1` from (4.5) and the star eigenvalues `+1,-1`; hence it has at least four eigenvalues of modulus at least one and is a literal target instance. The arbitrary `H` may itself be a dense same-side quadratic operator and does not change (4.7).

Moreover, the mixed frame

`U=[v_1,v_2,c]`                                                 (4.8)

is exactly a partner `rho=0`, `k=2` endpoint: every nonzero three-row Pluecker basis uses two rows from the three-coordinate core `S`, so two such bases must intersect. The core carries `F` isometrically and the disjoint bank `T` carries the complementary line isometrically. Thus the partner's structural endpoint is not merely formal: a nontrivial target family in it has a direct linear small-ball bound.

## 5. Exact obstruction: a favorable `k=2` component can be canceled by arbitrary same-bank curvature

The preceding payment cannot be generalized by simply exhibiting a favorable rank-two component and allowing an arbitrary residual quadratic operator on the same bank.

Keep the exact mixed frame (4.8), but start from the displayed favorable rank-two component

`v_1v_1^T+v_2v_2^T=P_F`                                       (5.1)

and add the same-bank dense residual

`R_S=-P_F`.                                                     (5.2)

The actual total core curvature is then zero. Take the outside line to be one physical coordinate `t`, so `c=1`, and take iid

`X_h,X_t ~ Uniform[-1/2,1/2]`.                                 (5.3)

The actual form is

`Q=2X_hX_t`.                                                    (5.4)

Its density is exactly

`p_Q(q)=log(1/(2|q|)),    0<|q|<1/2`,                           (5.5)

and therefore diverges logarithmically at zero.

The coefficient frame still has a perfect `k=2` physical-core-plus-outside-line split, and one may still write the formal favorable component with coefficients `lambda_1=lambda_2=1`. What disappeared is the ACTUAL third quadratic direction after the arbitrary same-bank residual was included.

This is not a counterexample to the full conjecture: the matrix of (5.4) has only the two nonzero eigenvalues `+1,-1`. It is a source-valid refutation of the intermediate extension

> “partner `k=2` geometry plus a favorable displayed rank-two curvature component yields a density bound uniformly over arbitrary same-bank residual quadratic curvature.”

The correct payment must either certify the relevant curvature in the actual total principal block/form, or keep a genuine external third source-compatible smoother unconditioned through the cancellation. This is exactly why a small matrix coefficient cannot be dropped on arbitrary unbounded product inputs.

## 6. Required mixed-hub smoothing applied to an actual dense source-coordinate star

To apply the newest-Claude Theorem H directly, take an original-coordinate leaf bank `Y=(Y_1,...,Y_m)` with `m>=6`, a disjoint physical hub `X_h`, and choose three orthonormal flat vectors

`c,v_1,v_2 in R^m`,                                            (6.1)

for example Walsh vectors when `m` is an appropriate power of two. Every coordinate then has squared augmented-row leverage

`c_i^2+(v_1)_i^2+(v_2)_i^2=3/m<=1/2`.                          (6.2)

Consider the actual star

`F_m=2X_h<c,Y>+<v_1,Y>^2-<v_2,Y>^2`.                           (6.3)

The same-side leaf operator

`v_1v_1^T-v_2v_2^T`                                           (6.4)

is dense in physical coordinates and indefinite; it is retained exactly, not conditioned away. The augmented mixed-frame Gram matrix is `I_3`. With one hub and two Fresnel directions, Theorem H gives

`|phi_(F_m)(t)|
 <=(2|t|)^(-1)(4 pi |t|)^(-1)(4 pi)^3
 =8 pi^2 |t|^(-2)`.                                           (6.5)

Therefore

`int_R |phi_(F_m)(t)|dt
 <=int_R min(1,8 pi^2/t^2)dt
 =8sqrt(2) pi`,                                                (6.6)

and Fourier inversion yields

`boxed: ||p_(F_m)||_infinity <=4sqrt(2)<5.657`,                 (6.7)

`boxed: P{F_m in L}<=4sqrt(2)|L|`.                              (6.8)

The grouped orthonormal basis `(e_h,c,v_1,v_2)` shows that the nonzero spectrum of (6.3) is exactly

`{+1,-1,+1,-1}`.                                               (6.9)

Thus (6.7) is an actual target-valid inequality for a source-coordinate star with diffuse hub couplings and dense same-side indefinite curvature. No probability squaring occurs: the `|t|^-2` estimate is directly integrable, so the interval scale remains linear.

Theorem H in fact permits arbitrary diagonal leaf twists and arbitrary conditioned outside blocks/couplings at the analytic level. Section 5 explains why one cannot replace its diagonal-twist hypothesis by an arbitrary dense same-bank residual without additional actual-curvature information.

## 7. What changed and what remains

This run turns the partner `k=2` structural output into three precise pieces of proof currency:

- a universal-scale **physical pair** inside the three-coordinate core, with (3.4)-(3.5);
- a genuinely **disjoint aggregate original-coordinate line**, with (3.7)-(3.8);
- an exact diagnosis that the unresolved gate is **actual total curvature**, not lack of a coefficient-space rank split.

It also pays a nontrivial block-separated semidefinite endpoint and a distinct dense indefinite mixed-hub target family.

The first unpaid B09 implication is sharpened to

`QFORM-K2-COUPLED-ACTUALCORE-SMOOTHING-v1`:

> starting from the extracted physical core pair and the disjoint aggregate line, retain the full cross coupling and arbitrary same-bank residual operator, and prove a direct `O(|L|)` bound whenever the actual total matrix still carries the required third spectral direction; otherwise route quantitatively to the already-paid physical-pair / finite-core / zero-hubpair / cross-volume branches.

The cancellation example (5.1)-(5.5) is a mandatory regression test: a proof may not charge a low-rank component that is canceled in the actual total matrix.

## 8. Scope and review status

The full QFORM conjecture and its full-target continuity statement remain OPEN. The new extraction theorem is elementary and complete; the semidefinite endpoint uses the source-pinned completed rank-two theorem; the mixed-hub target application uses the source-pinned completed Theorem H. No independent end-to-end review of the present combined result is claimed.

Deterministic algebra and constants for the examples are recorded in `CHECKS.txt` in this run directory. No numerical histogram or Monte Carlo inference is used.
