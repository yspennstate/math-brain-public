SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T17:54:46Z.
attacking: the punctured tiny-edge heavy null-hub collar 0<|g_i|<1/64; transfer the owner-pinned pure-hub/transverse-square theorem through an exact rank-one partner identity, without deleting the nonzero edge.

# account03/B18 r32 — exact rank-one partner closure inside the tiny-edge heavy null-hub collar

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW SUPPORTING THEOREM + DESIGNATED PARTNER SPLICE / FULL QFORM OPEN / CONTINUITY NOT PROVED FOR THE NEW BRANCH**.

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and live debt

The exact-rank-three null-hub normal form used by the live compiler is

`Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2`,          (1.1)

with

`||beta||_2=1`, `beta dot g=0`, `gamma=||g||_2>0`.                    (1.2)

For a leaf `i`, write

`epsilon=g_i`, `b=beta_i`, `q_i=b^2+epsilon^2/gamma^2`.               (1.3)

The completed account04/B18 r4 theorem pays every heavy witness `q_i>1/2` with `|epsilon|>=1/64` by

`||p_Q||_infinity <64.1795826152`,                                   (1.4)

while account03/B18 r31 pays the exact endpoint `epsilon=0` by a continuous `C_0` density bound `<9.263` in the target-normalized moderate/high-shear regime. Thus the live local debt contains the genuinely punctured state

`q_i>1/2`, `0<|epsilon|<1/64`.                                       (1.5)

This report closes a concrete source-valid portion of (1.5): the exact **rank-one partner** subgeometry, quantitatively through `q_i<=3/4`, and separately the exact coloop endpoint `q_i=1`.

No small nonzero coefficient is replaced by zero.

## 2. Exact rank-one partner condition

Delete coordinate `i` from the leaf block and set

`G=g_{-i}`, `B=beta_{-i}`, `E=ell_{-i}`.                              (2.1)

The two physical rows from the original coordinates `{0,i}` into the remaining original leaves are

`G`,

`ell_i G + epsilon E + d b B`.                                      (2.2)

Hence their cross block has rank one precisely when

`epsilon E+d b B in span{G}`.                                       (2.3)

Assume throughout Sections 2--5 that `epsilon!=0` and (2.3) holds. Write

`epsilon E+d b B=tau G`, `alpha=tau/epsilon`,                        (2.4)

so that

`E=alpha G-(d b/epsilon) B`.                                        (2.5)

This is an exact algebraic condition on ORIGINAL-coordinate coefficient rows. It is not a probabilistic rotation or an independence assertion.

## 3. Exact reduction to a pure hub plus transverse square

Let

`Z=X_{L\{i}}`, `H=G dot Z`, `K=B dot Z`, `U=X_0`, `V=X_i`, `l=ell_i`. (3.1)

Substituting (2.5) into (1.1) gives

`Q=2(U+lV+alpha H-(db/epsilon)K)(epsilon V+H)+d(bV+K)^2`.            (3.2)

Condition on the ORIGINAL coordinate `V=x`. Define

`D_0=K-(b/epsilon)H`.                                                (3.3)

A direct expansion, with no approximation, gives

`Q = 2U(H+epsilon x)+d D_0^2+F_x(H)`,                               (3.4)

where `F_x` is a real quadratic polynomial depending on the fixed value `x`. In particular, every residual dependence on `K` outside the single square `D_0^2` cancels exactly.

For reference, one explicit form is obtained by subtracting the first two displayed terms from (3.2):

`F_x(H)= - (H+epsilon x)[-2 alpha epsilon^2 H+b^2 d H-b^2 d epsilon x-2 epsilon^2 l x]/epsilon^2`.  (3.5)

Thus the nonzero edge `epsilon` has been retained exactly.

## 4. Orthogonalization in coefficient space only

Put

`rho=epsilon/gamma`, `q=q_i=b^2+rho^2`.                             (4.1)

Assume first `q<1`. Since `||g||=gamma`,

`s:=||G||=gamma sqrt(1-rho^2)>0`.                                  (4.2)

Let

`w=G/s`, `L=w dot Z`.                                               (4.3)

From `beta dot g=0`,

`G dot B=-epsilon b`.                                               (4.4)

Write `B_perp=P_{G^perp}B` and `t=||B_perp||`. A one-line Gram computation gives

`t^2 = ||B||^2-(G dot B)^2/||G||^2`
`    = (1-q)/(1-rho^2)`.                                           (4.5)

For `q<1`, put `v=B_perp/t` and `W=v dot Z`; then `w,v` are orthonormal deterministic coefficient vectors. Equation (3.3) becomes

`D_0=t(W-v_c(L))`                                                   (4.6)

for a linear function `v_c`. Therefore, conditionally on `V=x`,

`Q = 2s U(L+beta_x)+d t^2(W-v_c(L))^2+F_x(L)`                      (4.7)

for a deterministic shift `beta_x` and measurable `F_x`.

Crucially, `L` and `W` are NOT asserted independent. They are merely two orthonormal projections of the same ORIGINAL product block `Z`. The only independence used is the genuine original-coordinate independence `U=X_0 independent Z`.

## 5. Source-valid pure-hub transfer and exact invariant

The owner-pinned manuscript theorem `A transverse square with an independent hub` states the following. Let `U` have density at most one and be independent of a cap-one product vector `Z`. For orthonormal coefficient vectors `w,v`, arbitrary measurable `v_c,F_c`, and `mu=|lambda|>0`,

`T=2U(L+beta)+lambda(W-v_c(L))^2+F_c(L)`                            (5.1)

has an essentially bounded density satisfying

`||p_T||_infinity <= B(mu)`,                                       (5.2)

where

`B(mu)=2sqrt(2)+sqrt(2) log(1/3+4sqrt(2)/mu)` for `0<mu<=6sqrt(2)`,

and

`B(mu)=(192/mu)^(1/3)` for `mu>=6sqrt(2)`.                         (5.3)

Canonical source read for this run:

`yspennstate/math-open-problems@fad298c9bb0e96eae32c5a98861b42b50eec8568:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/hubs.tex`.

Its product-projection input is hypothesis-exact for the owner source class: Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, prove that if `f=prod_j f_j` and every one-dimensional probability density satisfies `||f_j||_infinity<=1`, then every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`. No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, centering, symmetry, or smoothness assumption is present. The theorem controls a joint projected density; it does not say its coordinates are independent.

Apply (5.2) to (4.7) after scaling the output by `s`. The effective transverse-square strength is

`mu=|d| t^2/s`.                                                      (5.4)

Uniformly in the conditioned value `x`,

`||p_{Q|V=x}||_infinity <= s^(-1) B(mu)`.                          (5.5)

Averaging over the original coordinate `V` preserves the same essential bound.

Now define

`A_*:=|d| gamma^2(1-q)`.                                           (5.6)

Equations (4.2), (4.5), and (5.4) give the exact cancellation

`mu s^3 = |d| t^2 s^2 = |d| gamma^2(1-q)=A_*`.                    (5.7)

Hence

`||p_Q||_infinity <= A_*^(-1/3) [mu^(1/3) B(mu)]`.                (5.8)

### Exact scalar optimization

For `mu>=6sqrt(2)`, (5.3) gives

`mu^(1/3)B(mu)=192^(1/3)`.                                        (5.9)

For `0<mu<=6sqrt(2)`, set `z=1/3+4sqrt(2)/mu>=1`. Then

`F(mu):=mu^(1/3)B(mu)=sqrt(2) mu^(1/3)(2+log z)`.                 (5.10)

Differentiating with respect to `log mu`, the sign of `F'` is the sign of

`log z+1/z-1`.                                                      (5.11)

This is nonnegative for `z>=1`, because it vanishes at `z=1` and its derivative is `(z-1)/z^2>=0`. Thus `F` increases through the first branch and reaches the second-branch value at `mu=6sqrt(2)`. Therefore

`sup_(mu>0) mu^(1/3) B(mu)=192^(1/3)`.                             (5.12)

Combining (5.8) and (5.12) proves the main theorem.

### Theorem — `QFORM-NULLHUB-RANKONE-PARTNER-CLOSURE-v1`

Under (1.1)--(1.3), suppose `epsilon=g_i!=0`, `q_i<1`, and the exact rank-one partner condition (2.3) holds. Then the full law of `Q` has an essentially bounded density with

`boxed: ||p_Q||_infinity <= [192/(|d| gamma^2 (1-q_i))]^(1/3).`    (5.13)

Continuity is **not** claimed by this transfer. The cited pure-hub theorem is used here at the level of its proved essential-density statement, and conditioning/averaging alone does not add a continuity theorem.

## 6. Target-normalized payoff in the punctured tiny-edge collar

In the live target-normalized moderate/high-shear null-hub compiler,

`|d| gamma^2=hD`, `h>=1/5`, `D>=1`.                               (6.1)

If

`1/2<q_i<=3/4`,                                                     (6.2)

then `1-q_i>=1/4`, and (5.13) gives

`||p_Q||_infinity <= (192*20)^(1/3)`
`                   =3840^(1/3)`
`                   =15.659470564675454...`.                       (6.3)

This is uniform as `epsilon ->0` through nonzero values. No perturbative passage to the zero-edge theorem is made.

## 7. Exact coloop endpoint q_i=1 under the same rank-one-partner geometry

The formula (5.13) necessarily degenerates as `q_i ->1`, but the exact endpoint is separately payable.

Suppose `q_i=1` and `epsilon!=0`. The two coefficient rows `g/gamma` and `beta` are orthonormal. Their residual Gram determinant after deleting coordinate `i` is exactly

`det [[1-rho^2,-rho b],[-rho b,1-b^2]]=1-q_i=0`.                  (7.1)

Thus `G` and `B` are collinear. Under the exact rank-one partner condition (2.3), `E` is collinear with the same residual direction as well. Consequently the entire quadratic form depends only on three genuinely independent scalar source banks:

`X_0`, `X_i`, and one normalized residual projection `w dot Z`.     (7.2)

The third bank has density cap at most `sqrt(2)` by the primary Livshyts--Paouris--Pivovarov theorem. The physical active subspace `span{e_0,e_i,w}` is orthonormal, so its effective symmetric `3x3` matrix has exactly the three nonzero eigenvalues of the physical exact-rank-three matrix.

Therefore the already completed account03/B18 theorem `QFORM-THREE-DISJOINT-BANKS-ALLPIVOTS-v1`, source

`yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f:proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T112422Z-account03-B18-QFORM-r27/REPORT.md`,

applies. In target normalization it gives

`||p_Q||_infinity <296`.                                          (7.3)

This endpoint is asserted as essential boundedness; continuity is not supplied by the all-pivot theorem in general.

## 8. Required designated-partner splice at an actual inequality

The latest completed designated partner is account04/B18 r4:

`yspennstate/math-open-problems@afbdba9c6b0624552a6725568d3eb883b999d1e1:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T162049Z-account04-B18-QFORM-r4/REPORT.md`.

For every heavy witness `q_i>1/2` with `|g_i|>=1/64`, it proves (1.4).

Combine it with the present theorem and the completed account03/B18 r31 exact-zero theorem. In the exact rank-one-partner geometry, for every heavy witness with

`1/2<q_i<=3/4`,                                                     (8.1)

we now have the explicit trichotomy

* `g_i=0`: account03/B18 r31 gives `<9.263` and a continuous `C_0` density;
* `0<|g_i|<1/64`: the present theorem gives `<15.660`;
* `|g_i|>=1/64`: account04/B18 r4 gives `<64.180`.

Thus this entire edge-size axis is paid on (8.1), with the uniform essential-density bound

`boxed: ||p_Q||_infinity <64.18.`                                  (8.2)

The middle line is the new implication: the previously punctured tiny-edge interval is bounded without setting `g_i` to zero.

## 9. What remains open

This is not a proof of the unrestricted conjecture. Even inside the null-hub heavy branch, (5.13) loses as `q_i ->1`, and the exact endpoint `q_i=1` is paid separately rather than by a uniform collar argument. The exact rank-one-partner survivor

`3/4<q_i<1`, `0<|g_i|<1/64`                                       (9.1)

therefore remains quantitatively open by this mechanism. More importantly, a general source-entangled heavy witness need not satisfy (2.3); the two-anchor partner cross block may have genuine rank two. Arbitrary additional spectrum is also a separate global compiler debt.

The unrestricted owner QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open.

## 10. Correction audit

This proof obeys the current correction set:

- no independence is asserted after a spectral or coefficient rotation;
- the projected pair `(L,W)` is explicitly allowed to be dependent;
- a bounded projection density is used only inside the source-pinned pure-hub theorem, not as an arbitrary indefinite pushforward theorem;
- no conditional density cap is substituted for independence;
- no law-uniform pointwise quadratic-phase decay is used;
- no fixed good physical minor is selected;
- no small nonzero coefficient is deleted or replaced by zero;
- no moment, support, log-concavity, Gaussian, symmetry, or iid assumption is introduced;
- no Monte Carlo or interval-extremality assertion enters the argument.

Primary source checked this run:
G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949.

The report makes no claim of literature-wide novelty. It is a programme-internal supporting theorem pending independent end-to-end review.
