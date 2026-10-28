# account01/B12 — adaptive thresholded orthogonalized spectral-shield absorption

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T131905Z-account01-B12-QFORM-auto11`  
Assignment: additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / PARTNER ACTUALLY APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T13:19:05Z.

attacking: adaptive thresholded orthogonalized spectral-shield absorption for arbitrary signed added eigenvalues.

## 1. Target and point of this run

The target is unchanged. For independent real `X_i` with probability densities bounded by one, and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a counterexample. No moments, support assumptions, log-concavity, or independence after a spectral rotation may be introduced.

The preceding account01/B12 run controlled the singular tail of an added spectral matrix through bilateral physical `|E|` energy and a nuclear norm estimate. This run changes mechanism. It works at the level of the **final high-spectral projector** and proves an adaptive compiler: arbitrarily large positive or negative added eigenmodes are absorbed into a physical shield and cost only the leverage of the *orthogonalized union subspace*; all remaining modes, regardless of rank, cost only one spectral threshold in operator norm.

The full conjecture remains open because the bare hypothesis `s_3(A)>=1` does not itself force the adaptive shield score below to be small.

## 2. Completed sources used

### 2.1 Designated partner account02/B12

Read the immutable partner report

`yspennstate/math-open-problems@82f8bc73589e3b6f61b4f11d9cb2df1941cd5565`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T125143Z-account02-B12-QFORM-auto11/REPORT.md`.

The result used is its outer-projector leakage theorem. If `B=B^T`, `P` is an orthogonal projection reducing `B`, `Q=I-P`,

`||Q B Q||_op <= beta < a`,

`A=B+T`, `||T||_op<=delta`, and

`Pi=1_{|A|>=a}`,

then

`||Q Pi||_op <= sqrt(2) delta/(a-beta)`.                                      (2.1)

No norm bound is imposed on the `PBP` block.

### 2.2 Completed ridge-window receiver

Read the immutable report

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

at

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

The receiver used here is: if the final symmetric matrix `A` has at least three eigenvalues of modulus at least one and its spectral projection

`Pi=1_{|A|>=1/64}`

satisfies

`max_i Pi_ii <= 1/32`,

then for every independent cap-one product input the law of `X^T A X` has a continuous `C_0` density and

`||p||_infinity <= 288 sqrt(3e)/13 < 64`.                                   (2.2)

The present proof uses (2.1) only as a deterministic matrix statement and then (2.2) on the actual final matrix. It never interprets a matrix remainder as independent random noise.

## 3. A sharper physical-coordinate consequence of the partner theorem

### Proposition 3.1 (`QFORM-APPROXIMATE-REDUCING-SHIELD-v1`)

Let `A=A^T` be a final target matrix, so `s_3(A)>=1`. Let `P` be any orthogonal projection in the ORIGINAL coordinate space and put `Q=I-P`. Fix

`a=1/64`,

and define

`mu_i=P_ii`,
`beta=||Q A Q||_op`,
`c=||Q A P||_op`.

Assume `beta<a`. If

`max_i [ sqrt(mu_i) + (sqrt(2)c/(a-beta)) sqrt(1-mu_i) ]^2 <= 1/32`,          (3.1)

then `X^T A X` has a continuous `C_0` density satisfying (2.2).

A coarser sufficient condition is

`sqrt(mu) + sqrt(2)c/(a-beta) <= 1/sqrt(32)`,

where `mu=max_i P_ii`.                                                       (3.2)

#### Proof

Relative to `Ran P direct_sum Ran Q`, write

`A = B + T`,

where

`B=PAP+QAQ`,
`T=PAQ+QAP`.

The projection `P` reduces `B`; moreover

`||Q B Q||_op=beta`.

The off-diagonal self-adjoint block

`T = [[0,(QAP)^*],[QAP,0]]`

has operator norm exactly

`||T||_op=c`.

Apply the completed account02/B12 theorem (2.1). For the final outer spectral projection `Pi=1_{|A|>=a}`,

`||Q Pi||_op <= epsilon := sqrt(2)c/(a-beta)`.                              (3.3)

For every original coordinate vector `e_i`,

`sqrt(Pi_ii)=||Pi e_i||`

`<= ||Pi P e_i|| + ||Pi Q e_i||`

`<= sqrt(mu_i) + ||Pi Q||_op sqrt(1-mu_i)`

`= sqrt(mu_i) + ||Q Pi||_op sqrt(1-mu_i)`

`<= sqrt(mu_i)+epsilon sqrt(1-mu_i)`.                                      (3.4)

Thus (3.1) implies `max_i Pi_ii<=1/32`, and (2.2) applies to the actual final matrix. QED.

**Interpretation.** The entire `PAP` block is free: its rank, signs, multiplicities and eigenvalue magnitudes may be arbitrary. Only leakage of the final matrix from the shield, measured by `QAP`, and the complement spectral size `QAQ`, are charged.

## 4. Whole-tail form: arbitrary matrix on a shield is magnitude-free

### Corollary 4.1

Suppose

`A=F+R`,

where `F=PFP` for an orthogonal projection `P`. No restriction is imposed on `F`. Let

`sigma=||R||_op`.

Let `Pi=1_{|A|>=a}`, `a=1/64`. Applying (2.1) directly with `B=F`, `T=R`, and `beta=0` gives

`||Q Pi||_op <= sqrt(2) sigma/a = 64 sqrt(2) sigma`.                         (4.1)

Hence, if `s_3(A)>=1` and

`max_i [sqrt(P_ii)+64sqrt(2)sigma sqrt(1-P_ii)]^2 <= 1/32`,                 (4.2)

then the final quadratic form has a continuous `C_0` density satisfying (2.2). In particular it is enough that

`sqrt(mu)+64sqrt(2)sigma <= 1/sqrt(32)`.                                   (4.3)

Again, `F` may have arbitrarily large positive and negative eigenvalues and arbitrary rank.

There are therefore two valid deterministic leakage channels. If `A=F+R`, `F=PFP`, one may either use the whole-tail estimate (4.1), or absorb the final `PAP` and `QAQ` diagonal blocks and use Proposition 3.1. The better one can be chosen:

`||Q Pi||_op <= sqrt(2) min{ ||R||_op/a, ||QAP||_op/(a-||QAQ||_op) }`,       (4.4)

where the second term is used only when `||QAQ||_op<a`. This minimum is an exact consequence of two applications of the same completed partner theorem.

## 5. New adaptive spectral-threshold compiler

### Theorem 5.1 (`QFORM-ADAPTIVE-THRESHOLDED-ORTHOGONALIZED-SHIELD-v1`)

Let

`A=A_0+E+T`,                                                               (5.1)

with all three matrices symmetric. Assume a baseline decomposition

`A_0=F_0+R_0`,
`F_0=P_0 F_0 P_0`,
`||R_0||_op<=eta`,                                                         (5.2)

where `P_0` is an orthogonal projection in the ORIGINAL coordinate space. Let

`E = sum_k theta_k v_k v_k^T`                                              (5.3)

be an orthonormal spectral decomposition of the added matrix. There is no sign or magnitude restriction on the `theta_k`. Let

`delta=||T||_op`.

For a threshold `h>=0`, define

`E_>(h)=sum_{|theta_k|>h} theta_k v_k v_k^T`,
`E_<=(h)=E-E_>(h)`,                                                        (5.4)

so

`||E_<=(h)||_op<=h`.                                                       (5.5)

Let `W_h=Ran E_>(h)` and let `P_h` be the orthogonal projector onto

`Ran P_0 + W_h`.                                                           (5.6)

Put

`p_i(h)=(P_h)_ii`,
`sigma_h=eta+h+delta`.                                                     (5.7)

Assume the **actual final matrix** `A` satisfies the owner hypothesis

`s_3(A)>=1`.                                                               (5.8)

If for at least one threshold `h`

`max_i [ sqrt(p_i(h)) + 64sqrt(2) sigma_h sqrt(1-p_i(h)) ] <= 1/sqrt(32)`,  (5.9)

then the law of `X^T A X` has a continuous `C_0` density and

`boxed: ||p_{X^T A X}||_infinity <= 288 sqrt(3e)/13 < 64.`                 (5.10)

The coarser but simpler sufficient condition is

`sqrt(mu_h)+64sqrt(2)(eta+h+delta) <= 1/sqrt(32)`,                         (5.11)

where `mu_h=max_i(P_h)_ii`.

Equivalently, one can optimize the one-parameter score

`Phi := inf_{h>=0} [ sqrt(mu_h)+64sqrt(2)(eta+delta+h) ]`.                 (5.12)

The condition `Phi<=1/sqrt(32)` proves (5.10).

#### Proof

Set

`F_h=F_0+E_>(h)`,
`R_h=R_0+E_<=(h)+T`.                                                       (5.13)

Every summand of `F_0` has range in `Ran P_0`, and every summand of `E_>(h)` has range in `W_h`. Therefore

`F_h=P_h F_h P_h`.                                                        (5.14)

This is a purely deterministic range identity and does not rotate the random variables.

By (5.2), (5.5), and the triangle inequality,

`||R_h||_op <= eta+h+delta=sigma_h`.                                      (5.15)

Thus (5.1) is the decomposition `A=F_h+R_h` to which Corollary 4.1 applies. The completed partner theorem gives

`|| (I-P_h) Pi ||_op <= 64sqrt(2) sigma_h`,                               (5.16)

where `Pi=1_{|A|>=1/64}` is the spectral projection of the **actual final matrix**. Formula (3.4) with `P=P_h` gives exactly (5.9) as a sufficient condition for `max_i Pi_ii<=1/32`. Then the completed ridge-window theorem proves (5.10), including continuity and vanishing at infinity. QED.

### What this theorem pays and what it does not pay

1. Every added eigenmode with `|theta_k|>h` is absorbed into `P_h`; its **magnitude and sign disappear completely** from the analytic bound.
2. There is no rank penalty by itself. A hundred or a million large modes are harmless if their orthogonalized union still has small coordinate leverage.
3. Every remaining mode satisfies `|theta_k|<=h`; there may be arbitrarily many, with either sign and arbitrary eigenvectors, but their entire matrix costs only `h` in operator norm.
4. The arbitrary symmetric remainder `T` can be fully nonseparable and dense. It costs only its deterministic matrix norm `delta`; `X^T T X` is never treated as small, independent, or convolved away.
5. The threshold can be chosen after seeing the added spectrum. Raising `h` reduces the high-mode subspace and hence tends to reduce `mu_h`, while increasing the norm charge linearly. Equation (5.12) makes this tradeoff explicit.

This is the requested larger/smaller eigenvalue control in a form compatible with original-coordinate product structure.

## 6. Exact orthogonalized-union leverage identity

The useful quantity in Theorem 5.1 is not the number of high modes but the physical leverage of their span *after removing the old shield*.

Let `Q_0=I-P_0`, and let `V_h` have orthonormal columns spanning `W_h`. Put

`G_h=V_h^T Q_0 V_h`.                                                      (6.1)

Then

`Ran P_0 + W_h = Ran P_0 direct_sum Ran(Q_0 V_h)`,                         (6.2)

an orthogonal sum. Therefore the projector has the exact formula

`boxed: P_h = P_0 + Q_0 V_h G_h^dagger V_h^T Q_0,`                        (6.3)

where `dagger` denotes the Moore-Penrose inverse. In particular, with

`z_i=V_h^T Q_0 e_i`,

`boxed: p_i(h)=(P_0)_ii + z_i^T G_h^dagger z_i.`                          (6.4)

#### Proof

Every `w in W_h` decomposes orthogonally as `w=P_0w+Q_0w`, so the sum of spaces in (6.2) is exact. The second summand is the column space of `Q_0V_h`; the standard projector onto the column space of a matrix `Z` is `Z(Z^TZ)^dagger Z^T`. Taking `Z=Q_0V_h` yields (6.3), and evaluation on `e_i` yields (6.4). QED.

There is also a sequential exact form. Order the high-mode directions as `v_1,...,v_r`. Let `P_j` project onto

`Ran P_0 + span(v_1,...,v_j)`.

If

`w_j=(I-P_{j-1})v_j`

is nonzero, set `u_j=w_j/||w_j||`. Then

`P_j=P_{j-1}+u_j u_j^T`,                                                  (6.5)

and hence

`boxed: (P_r)_ii=(P_0)_ii + sum_{j:w_j!=0} u_{j,i}^2.`                    (6.6)

Thus a new enormous eigenvalue costs **zero** leverage if its direction is already in the old shield, and otherwise costs precisely the squared coordinates of its normalized orthogonalized residual. No amplitude appears. This exact Gram-Schmidt accounting is important: a raw leverage bound on the unorthogonalized `v_j` cannot in general replace (6.4)/(6.6), because nearly dependent directions can have a concentrated normalized residual.

Special case: if `W_h` is orthogonal to `Ran P_0`, then

`P_h=P_0+P_{W_h}`

and the leverages add coordinatewise.

## 7. Actual inequality from the designated partner theorem

Here is a literal target-class family on which the partner theorem produces a nontrivial final inequality.

Let `d>=4`. Choose a Sylvester-Hadamard dimension `N` with

`N>=256 d`,

and let `u_1,...,u_N` be its normalized Hadamard basis. Thus every coordinate of every `u_k` has magnitude `N^{-1/2}`.

Set

`A_0=4 sum_{k=1}^3 u_k u_k^T`.                                            (7.1)

For arbitrary real numbers

`tau_4,...,tau_d in R`,                                                    (7.2)

with no restrictions on signs or magnitudes, add

`E_tau=sum_{k=4}^d tau_k u_k u_k^T`.                                      (7.3)

Finally add **any** symmetric dense matrix `T` satisfying

`||T||_op<=1/8192`.                                                       (7.4)

Choose the threshold

`h=1/8192`.                                                               (7.5)

Let `L={k in {4,...,d}: |tau_k|>h}` and

`P=P_{span(u_1,u_2,u_3,(u_k)_{k in L})}`.                                (7.6)

Because this is a subset of a Hadamard basis, every diagonal of `P` is the same and

`P_ii=(3+|L|)/N <= d/N <=1/256`.                                         (7.7)

Define

`F=4 sum_{k=1}^3 u_k u_k^T + sum_{k in L} tau_k u_k u_k^T`,               (7.8)

`R=sum_{k notin L, 4<=k<=d} tau_k u_k u_k^T + T`.                         (7.9)

Then `F=PFP`, while orthogonality of the Hadamard basis gives

`||R||_op <= 1/8192+1/8192=1/4096`.                                     (7.10)

Now apply the completed account02/B12 theorem (2.1) with

`a=1/64`, `beta=0`, `delta=1/4096`.

For `Pi=1_{|A|>=1/64}` it gives the **actual inequality**

`boxed: ||(I-P)Pi||_op <= sqrt(2)*(1/4096)/(1/64)=sqrt(2)/64.`             (7.11)

Consequently, by (3.4) and (7.7),

`sqrt(Pi_ii) <= 1/16 + sqrt(2)/64`,                                      (7.12)

so

`boxed: max_i Pi_ii <= (1/16+sqrt(2)/64)^2`

`= (18+8sqrt(2))/4096`

`= 0.007156667114009951... < 1/32.`                                      (7.13)

The matrix `F` has three singular values exactly `4` on the protected directions, independently of all `tau_k`; therefore Weyl gives

`s_3(A)>=s_3(F)-||R||_op >= 4-1/4096 >1`.                                (7.14)

The family is consequently inside the exact owner target for **every** choice of all `tau_k`, including simultaneous arbitrarily large positive and negative values and arbitrarily small values. The dense `T` is fully nonseparable.

Applying the completed ridge-window receiver to the actual final matrix yields

`boxed: ||p_{X^T A X}||_infinity <= 288 sqrt(3e)/13`

`=63.26405187778285... <64,`                                              (7.15)

and the density is continuous and vanishes at infinity.

The point of thresholding is that the high-amplitude `tau_k` are paid only through the diffuse union leverage (7.7), while *all* coefficients with `|tau_k|<=1/8192`, however many and of either sign, are simultaneously paid by the single operator-norm charge `1/8192`. The full dense tail is paid once more by `1/8192`.

## 8. Why no forbidden probabilistic step occurs

All rotations in this report are matrix/spectral descriptions used only to identify deterministic subspaces and operator norms. The random vector remains in its original coordinates throughout. The only probabilistic theorem invoked, the ridge-window receiver, is explicitly a theorem for the actual original-coordinate product source. We never assert that the coordinates `u_k^T X` are independent. We never write the final law as a convolution with `X^T R X`. We do not use pointwise van-der-Corput decay, arbitrary-joint coarea, a conditional projection-density moment, or a fiber-supremum estimate.

## 9. Remaining implication to the full target

The new theorem does **not** prove that every symmetric `A` with `s_3(A)>=1` admits a baseline shield / spectral split with score (5.12) below `1/sqrt(32)`. The exact missing structural statement is now:

> From the bare three-large-eigenvalue hypothesis, force either an adaptive product-coordinate shield with sufficiently small orthogonalized union leverage and small residual threshold score, or force one of the already-paid cross-volume, ridge, grouped-bank/hub, localized-core, pair/triple, or Schur exits.

Known diffuse exact-rank-three and singleton-plus-bank examples rule out replacing this by a claim that one uniformly conditioned small principal core or one rank-three cross cut always exists.

Thus the full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The present scoped branch proves **continuous** density, not merely essential boundedness, whenever (5.9) holds.

## 10. Source / correction discipline


Repository transport and native learned-memory ingestion are distinct. This run is `WITHOUT_VERIFIED_BRAIN`.
