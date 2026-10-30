SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T18:08:26Z.
attacking: the punctured zero-edge heavy null-hub collar; first isolate why arbitrary small-edge perturbation is false, then transfer the owner-pinned pure-hub theorem to the exact target geometry without the designated partner's rank-one cross-block assumption.

# fleet02/B18 — planar-twist closure beyond the rank-one partner condition

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW SUPPORTING THEOREM + SOURCE-VALID OBSTRUCTION + DESIGNATED-PARTNER STRENGTHENING / FULL QFORM OPEN / CONTINUITY NOT CLAIMED FOR THE NEW BRANCH**.

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Live debt and the early obstruction

Work in the exact-rank-three null-hub normal form

`Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2`,       (1.1)

where the original coordinates are independent with one-dimensional densities at most one,

`||beta||_2=1`, `beta dot g=0`, `gamma=||g||_2>0`, `d!=0`.         (1.2)

For a leaf `i`, put

`epsilon=g_i`, `b=beta_i`, `rho=epsilon/gamma`,
`q_i=b^2+rho^2`.                                                     (1.3)

The live heavy punctured regime has `q_i>1/2` and, after the already completed edge exits, potentially `0<|epsilon|<1/64`.

The early checkpoint in this same run constructs

`Q_c=2U(W+cV)+V^2-W^2/c^2=(V+W/c)(2cU+V-W/c)`                     (1.4)

for independent `U,V,W ~ Uniform[-1/2,1/2]`. Its coefficient matrix

`A_c=[[0,c,1],[c,1,0],[1,0,-c^(-2)]]`                              (1.5)

has rank two and exactly two eigenvalues of modulus greater than one, while the output density is unbounded at zero. More precisely, with `delta=c^2/16`, the joint density `rho` of the two linear factors in (1.4) satisfies `rho(s,t)>=c/8` on `[-delta,delta]^2`, hence

`p_Qc(z) >= (c/8) log(delta^2/|z|)` for `0<|z|<delta^2`.           (1.6)

This is **not** a counterexample to QFORM because only two eigenvalues are large. It is a source-valid obstruction to any argument saying that the exact-zero-edge receiver survives a small nonzero edge for an otherwise arbitrary residual quadratic function. The target must spend its third curvature/provenance structure.

## 2. Designated partner r32 and the stronger planar condition

The latest completed designated partner `fleet03/B18 r32`, source

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T175446Z-fleet03-B18-QFORM-r32/REPORT.md`,

uses the same normal form. Delete leaf `i` and write

`G=g_{-i}`, `B=beta_{-i}`, `E=ell_{-i}`.                            (2.1)

Its exact rank-one partner hypothesis is

`epsilon E + d b B in span{G}`.                                    (2.2)

For `epsilon!=0`, (2.2) implies `E in span{G,B}`, but the converse is false. The partner proves under (2.2), `q_i<1`,

`||p_Q||_infinity <= [192/(|d| gamma^2 (1-q_i))]^(1/3).`           (2.3)

The main result below shows that the physical rank-one partner condition is unnecessary: **planarity of the residual twist alone is enough**, and it permits a genuinely rank-two physical partner cross block.

## 3. Main theorem — `QFORM-NULLHUB-PLANAR-TWIST-CLOSURE-v1`

Assume (1.1)--(1.3), fix an original-coordinate leaf `i` with

`q_i<1`,                                                             (3.1)

and suppose only

`E=ell_{-i} in span{G,B}`.                                          (3.2)

Then the law of `Q` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= [192/(|d| gamma^2 (1-q_i))]^(1/3).`    (3.3)

No continuity assertion is made by this transfer.

### Proof

Condition on the **original coordinate** `X_i=x`. Let `Z=X_{L\{i}}`. Since `q_i<1`, the residual vectors `G` and `B` are linearly independent. Indeed

`||G||^2 = gamma^2(1-rho^2)`,                                      (3.4)

`||B||^2 = 1-b^2`, `G dot B = -epsilon b`,                         (3.5)

and therefore

`||G||^2 ||B||^2 - (G dot B)^2 = gamma^2(1-q_i)>0`.                (3.6)

Put

`s=||G||=gamma sqrt(1-rho^2)`, `w=G/s`,                            (3.7)

and let `v` be the unit vector in `span{G,B}` perpendicular to `w`. Write

`B=c w+t v`,                                                        (3.8)

where a Gram calculation gives

`t^2 = ||P_{G^perp}B||^2 = (1-q_i)/(1-rho^2)`.                     (3.9)

Because of (3.2), also write

`E=e_w w+e_v v`.                                                     (3.10)

Define the two (generally dependent) projections of the residual original product block

`L=w dot Z`, `V=v dot Z`.                                           (3.11)

Then

`g dot X_L=sL+epsilon x`,                                           (3.12)

`beta dot X_L=cL+tV+bx`,                                           (3.13)

`ell dot X_L=e_wL+e_vV+ell_i x`.                                   (3.14)

Substitute these identities into (1.1). Every term other than the independent-hub term is a quadratic polynomial in `(L,V)`, and the coefficient of `V^2` is exactly `d t^2`. Consequently, for functions `a_x`, `A_x(L)`, `F_x(L)`,

`Q = 2s X_0(L+a_x) + d t^2 V^2 + A_x(L)V + F_x(L)`.                (3.15)

Complete the square in `V` and divide the output by `s`:

`Q/s = 2 X_0(L+a_x) + lambda (V-v_x(L))^2 + F'_x(L)`,              (3.16)

where

`lambda=d t^2/s`, `mu=|lambda|>0`,                                 (3.17)

and `v_x,F'_x` are arbitrary real measurable functions for the purpose of the receiver theorem.

Now use the owner-pinned theorem **A transverse square with an independent hub**, canonical source

`math-open-problems@fad298c9bb0e96eae32c5a98861b42b50eec8568:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/hubs.tex`.

Its hypotheses match exactly: `X_0` is an original coordinate and is genuinely independent of the residual product vector `Z`; `w,v` are deterministic orthonormal coefficient vectors; the theorem explicitly allows dependence between `L` and `V` and arbitrary measurable square centre `v_x(L)` and remainder `F'_x(L)`. It gives, uniformly in `x`,

`||p_(Q | X_i=x)||_infinity <= s^(-1) B(mu)`,                      (3.18)

where

`B(mu)=2sqrt(2)+sqrt(2)log(1/3+4sqrt(2)/mu)` for `mu<=6sqrt(2)`,

`B(mu)=(192/mu)^(1/3)` for `mu>=6sqrt(2)`.                         (3.19)

The exact scalar optimization recorded in the completed designated-partner r32 proof is

`sup_(mu>0) mu^(1/3) B(mu)=192^(1/3)`.                             (3.20)

For completeness, on the first branch put `z=1/3+4sqrt(2)/mu>=1`; the derivative with respect to `log mu` has the sign of `log z+1/z-1>=0`, and the endpoint `mu=6sqrt(2)` equals the second branch.

Hence

`||p_(Q | X_i=x)||_infinity`
` <= 192^(1/3) s^(-1) mu^(-1/3)`
` = [192/(|d| t^2 s^2)]^(1/3)`.                                   (3.21)

Finally (3.7) and (3.9) give the exact invariant

`t^2 s^2 = gamma^2(1-q_i)`.                                       (3.22)

This proves (3.3), uniformly in the conditioned original coordinate. Averaging over `X_i` preserves the same essential-density cap. No independence of the rotated pair `(L,V)` has been used. QED.

## 4. Strictness: a target-valid rank-two partner family that r32 does not cover

The strengthening is strict even on an exact target family. Let the three residual original coordinates be `X_1,X_2,X_3` and define orthonormal coefficient vectors

`u=(sqrt(2/3), -1/sqrt(6), -1/sqrt(6))`,                            (4.1)

`beta=(0, 1/sqrt(2), -1/sqrt(2))`.                                 (4.2)

Take

`g=4u`, `d=4`, `ell=beta`,                                         (4.3)

so

`Q=4[ 2(X_0+beta dot X)(u dot X) + (beta dot X)^2 ]`.              (4.4)

In the orthonormal active basis `(e_0,u,beta)`, the nonzero coefficient matrix is

`4 M`, `M=[[0,1,0],[1,0,1],[0,1,1]]`.                              (4.5)

We have `det M=-1` and `||M||_op<=2` from the maximum absolute row sum. If `a<=b<=c` are the absolute eigenvalues of `M`, then `abc=1` and `b,c<=2`, so `a>=1/4`. Therefore every nonzero eigenvalue of the physical matrix in (4.4) has modulus at least one. There is one additional kernel direction, so this is an **exact-rank-three owner-target family**.

Use leaf `i=1`. Then

`b=beta_1=0`, `rho^2=(g_1/gamma)^2=2/3`, `q_i=2/3`,                (4.6)

and on residual coordinates `{2,3}`,

`G=4(-1/sqrt(6),-1/sqrt(6))`,                                      (4.7)

`B=E=(1/sqrt(2),-1/sqrt(2))`.                                      (4.8)

Thus `G perp B`, so `E in span{G,B}` and the new theorem applies. But the designated-partner rank-one condition fails maximally:

`epsilon E+d b B=epsilon B notin span{G}`.                         (4.9)

Equivalently, the two physical cross rows from the original pair `{0,1}` into residual coordinates `{2,3}` are proportional to `G` and `B`, hence have rank two.

The new whole-line estimate is

`||p_Q||_infinity <= [192/(4*16*(1/3))]^(1/3)=9^(1/3)`
`                   =2.080083823051904...`.                        (4.10)

Using the exact branch rather than the uniform scalar envelope is slightly sharper. Here `s=4/sqrt(3)`, `t=1`, `mu=sqrt(3)`, so

`||p_Q||_infinity`
` <= (sqrt(3)/4)[2sqrt(2)+sqrt(2)log(1/3+4sqrt(2)/sqrt(3))]`
` =2.009037710678627...`.                                          (4.11)

This example is source-valid for arbitrary independent cap-one coordinate laws. The variables `u dot X` and `beta dot X` are not asserted independent.

## 5. Required e5f transfer on the same genuine target family

The pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` counterexample-search record proves the ruled one-sheet theorem: for an exact rank-three form with signature `(2+,1-)` and all three nonzero eigenvalue magnitudes at least one,

`p_Q(t)<=pi sqrt(2)` for a.e. `t>=0`.                               (5.1)

The matrix `M` in (4.5) has `det M<0` and positive trace, so it has signature `(2+,1-)`. Hence (5.1) applies literally to (4.4). This is a real inequality on the current target family, not a novelty inference from a search miss. The new planar-twist theorem is stronger here because it controls the whole real line by (4.10), including the two-sheet side.

## 6. Nonplanar quantitative companion from the current hub theorem

The same coefficient bookkeeping gives a useful exact interface when the residual twist is not planar. Decompose

`E=e_w w+e_v v+E_perp`, `kappa=||E_perp||`.                        (6.1)

For `kappa>0`, put `e=E_perp/kappa`, so `w,v,e` are orthonormal coefficient vectors. After conditioning on `X_i=x` and dividing by `s`, the form is in the manuscript's **Nonzero leakage** normal form with transverse square strength

`lambda=d t^2/s`                                                    (6.2)

and leakage coefficient exactly `kappa` in the term `2 kappa L P`, `P=e dot Z`. Therefore, whenever the residual three-frame satisfies the source-side spread hypothesis

`w_j^2+v_j^2+e_j^2<=1/2` for every remaining original coordinate `j`, (6.3)

the proved leakage theorem yields

`boxed: ||p_Q||_infinity <= 3*2^(5/3) [kappa |d| gamma^2(1-q_i)]^(-1/3).`  (6.4)

Indeed scaling back gives `s^(-1) 3*2^(5/3)(kappa |d|t^2/s)^(-1/3)`, and (3.22) collapses the denominator exactly. This does not interpolate uniformly through `kappa->0`; Section 1 shows why arbitrary small-coefficient perturbation arguments are dangerous. But the endpoint `kappa=0` is now paid by the stronger planar theorem (3.3), without any rank-one partner requirement.

## 7. Target-normalized payoff and the sharpened debt

In the live moderate/high-shear exact-null branch, the completed compiler gives

`|d| gamma^2 >= 1/5`.                                               (7.1)

Therefore every **planar residual twist** with

`1/2<q_i<=3/4`                                                       (7.2)

obeys

`||p_Q||_infinity <= 3840^(1/3)=15.659470564675454...`,            (7.3)

uniformly through `g_i=0` and through every punctured nonzero edge. This strictly enlarges designated-partner r32, because physical partner rank two is permitted (Section 4).

The first unpaid local implication is correspondingly sharpened. A still-dangerous heavy witness must satisfy at least one of:

1. `3/4<q_i<1`, where the exact transverse-square currency `1-q_i` is small; or
2. `E` has a genuinely nonplanar component `kappa>0` but either the residual three-frame is not diffuse enough for (6.3), or `kappa` is in the small punctured range where (6.4) deteriorates.

The exact endpoint `q_i=1` has a separate completed three-bank closure under the designated partner's rank-one geometry, but no uniform collar theorem follows from that endpoint alone. The unrestricted QFORM theorem remains OPEN.

## 8. Primary-source boundary

The only external projection theorem needed by the owner-pinned pure-hub receiver is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1. It assumes an actual product

`f(x)=prod_j f_j(x_j)`, `||f_j||_1=1`,                              (8.1)

and proves for every `k`-dimensional orthogonal marginal

`||pi_E f||_infinity`
` <= min{(n/(n-k))^((n-k)/2), 2^(k/2)} prod_j ||f_j||_infinity^(gamma_j)`, (8.2)

with `gamma_j in [0,1]` and `sum gamma_j=k`. For cap-one inputs, the two-dimensional marginal cap is therefore exactly at most `2`. No moment, bounded-support, log-concavity, iid, centering, symmetry, or smoothness assumption appears. Equation (8.2) controls the **joint projected density**; it does not assert independence between the projected coordinates.

This is precisely the use in (3.16): `(L,V)` may be dependent, while the hub `X_0` remains genuinely independent because it is an untouched original coordinate.

## 9. Corrections audit

- Full QFORM is still OPEN; no completion claim is made.
- No projected-coordinate independence is asserted.
- No small nonzero edge is deleted or replaced by zero.
- No moment/support/log-concavity/Gaussian/iid/symmetry assumption is introduced.
- The rank-two construction in Section 1 is explicitly only a counterexample to a proof shortcut, not to QFORM.
- The pinned e5f search miss is not used as novelty evidence.
- The later `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction is compatible with this report: no singleton `G_*` scale forcing is invoked.
- Continuity is kept separate and is not claimed for (3.3), (4.10), or (6.4).

## 10. Sources read this run

Owner/control: fresh `math-research-brain/main`, including `AGENTS.md`, `scheduled_tasks/README.md`, OWNER continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, QFORM `MANIFEST/CURRENT_RESEARCH/CLAIMS/DELTAS/CORRECTION_INBOX/PATHWAYS/MEMORY_PROTOCOL`, `QFORM-PROOF-FIRST-20260922T161801Z.md`, `QFORM-CLAUDE-LATEST-20260922T225732Z.md`, and `assignments/fleet02/B18.json`.

Pinned math snapshot `e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.

Designated partner: fleet03/B18 r32 report above.

Owner-pinned receiver theorem: `math-open-problems@fad298c9bb0e96eae32c5a98861b42b50eec8568:.../manuscript/hubs.tex`.

Primary external theorem: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.
