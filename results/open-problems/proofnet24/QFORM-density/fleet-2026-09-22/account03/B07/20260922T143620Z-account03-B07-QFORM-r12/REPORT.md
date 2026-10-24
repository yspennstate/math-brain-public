# account03/B07 — conditional volume-sampling star/triangle stability

**Run:** `20260922T143620Z-account03-B07-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Status:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source discipline

The full target remains open: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with a universal `L^infinity` bound, or give a valid counterexample. Continuity is tracked separately and is not proved here.

Fresh control was read from `yspennstate/math-research-brain` main and remained owner revision `2026-09-22.5`. The final pre-publication correction refresh was through brain main `51c58a07a652459ee99b08ffa6bad2f11437070f`, correction blob `7a8e97b4c64376d251852264100ffc8502eebea1`. In particular, this report does not use pointwise law-uniform Fresnel decay, receiver-only conditional caps, one tiny minor, bounded fragment count, or post-rotation independence.

The exact assigned partner `account04/B07` still had no completed current-QFORM handoff at the fresh pre-publication source check. No result is fabricated or attributed to it. The compatible completed account04/B18 theorem actually applied below is:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

It proves, for a physical `3x3` block with scalar pivot `a!=0` and definite Schur complement,

`||p_Q||_infinity <= 2 sqrt(pi) (|a det B|)^(-1/4)`,                    (1.1)

with arbitrary outside couplings after conditioning on original coordinates.

I also consume account03/B13's newest completed nested-heavy theorem, canonical source

`yspennstate/math-open-problems@dd421029601cf5663685c49f225af55567332fb6`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/b13-20260922T143428Z-qform11/REPORT.md`,

which pays every rank-three nested-heavy state except a simultaneous final-bank/covariance-saturation limit described precisely in Section 6 below.

## 2. Rank-three volume sampling and exact conditioning

First isolate the rank-exactly-three core

`A=U Lambda U^T`, `U^T U=I_3`, `det Lambda !=0`.

For every triple `S`, define the Pluecker weight

`W_S = det(U_S)^2`.

Cauchy--Binet gives

`sum_{|S|=3} W_S=1`.                                                   (2.1)

For a coordinate `i`, put

`c_i=||u_i||^2`.

The standard inclusion identity, also immediate by expanding the determinant along row `i`, is

`c_i = sum_{S: i in S} W_S`.                                          (2.2)

Whenever `c_i>0`, condition the size-three volume-sampling law on inclusion of `i`. This gives a probability distribution on residual edges `{j,k}`:

`w_{jk}=W_{ijk}/c_i`,                                                   (2.3)

with

`sum_{j<k, j,k!=i} w_{jk}=1`.                                         (2.4)

Let

`q_j = sum_{k!=i,j} w_{jk}`                                            (2.5)

be the conditional inclusion probability of residual coordinate `j`. In the whitened residual two-frame this is exactly the residual row leverage. Thus this conditioning is source-valid geometry, not a choice of a single minor.

Finally define the ordered disjoint-edge mass

`rho = sum_{e,f: e cap f = empty} w_e w_f
     = P(E cap F = empty)`                                             (2.6)

for iid residual edges `E,F~w`. This is the same disjoint two-basis resource that appears in the rank-two cross-block aggregation route.

## 3. An exact identity for the residual disjoint resource

### Lemma 3.1 — `QFORM-RANK2-DPP-DISJOINT-IDENTITY-v1`

For any probability distribution `w` on two-element subsets, with vertex inclusion probabilities `q_j`,

`rho = 1 - sum_j q_j^2 + sum_e w_e^2`.                                 (3.1)

### Proof

Let `E,F` be iid with law `w`. Since both are edges, `|E cap F|` is `0,1,2`. The event `|E cap F|=0` has probability `rho`, while `|E cap F|=2` is exactly `E=F` and has probability `sum_e w_e^2`. Therefore

`E|E cap F| = 1-rho+sum_e w_e^2`.

On the other hand, by indicators,

`E|E cap F| = sum_j P(j in E,j in F)=sum_j q_j^2`.

Equating the two expressions proves (3.1). QED.

This identity separates genuine near-coloop structure (`sum q_j^2` large) from atom concentration (`sum w_e^2` large). It is dimension-free.

## 4. New quantitative star-or-triangle theorem

### Theorem 4.1 — `QFORM-RANK2-DPP-STAR-TRIANGLE-v1`

Let `w` be any probability distribution on edges of an arbitrary finite vertex set and let `rho=P(E cap F=empty)` for iid `E,F~w`. For every `tau>0`, at least one of the following holds:

1. **star:** some vertex `v` has

   `q_v >= 1-rho-tau`;                                                 (4.1)

2. **triangle:** some three vertices `{a,b,c}` have total internal edge mass

   `w_ab+w_ac+w_bc >= 1-rho-rho/tau^2`.                                (4.2)

In particular, taking `tau=rho^(1/3)` (for `rho>0`) gives a common threshold

`kappa(rho)=1-rho-rho^(1/3)`                                           (4.3)

such that either `max_v q_v>=kappa(rho)` or some triangle carries edge mass at least `kappa(rho)`.

### Proof

For an edge `e`, write

`d(e)=sum_{f disjoint e} w_f`.

Because `sum_e w_e d(e)=rho`, choose an edge `e0={a,b}` with `d(e0)<=rho`. Put `r=d(e0)`. Decompose all non-disjoint edge mass as

`z=w_ab`, `x_c=w_ac`, `y_c=w_bc`,
`X=sum_c x_c`, `Y=sum_c y_c`.

Then

`z+X+Y+r=1`.                                                           (4.4)

If `X<tau`, the star at `b` has mass

`q_b=z+Y=1-r-X >=1-rho-tau`.

The same argument with `X,Y` interchanged handles `Y<tau`.

Assume now `X,Y>=tau`. Every ordered pair `(ac,bd)` with `c!=d` is disjoint, hence

`2(XY-sum_c x_c y_c) <= rho`.                                         (4.5)

Normalize `p_c=x_c/X`, `s_c=y_c/Y`. Then

`sum_c p_c s_c >=1-epsilon`,
`epsilon:=rho/(2XY)<=rho/(2tau^2)`.                                   (4.6)

Let `c_*` maximize `s_c`. Since `sum p_c s_c<=max s_c`,

`s_{c_*}>=1-epsilon`.

Consequently the total `s`-mass away from `c_*` is at most `epsilon`, and

`1-epsilon <= sum p_c s_c <= p_{c_*}+sum_{c!=c_*}s_c
                         <= p_{c_*}+epsilon`,

so `p_{c_*}>=1-2epsilon`. Therefore

`(X-x_{c_*})+(Y-y_{c_*})
 <= 2epsilon X + epsilon Y
 <= 2epsilon(X+Y)
 <= 2epsilon
 <= rho/tau^2`.                                                        (4.7)

Using (4.4), the triangle `{a,b,c_*}` carries

`z+x_{c_*}+y_{c_*}
 =1-r-[(X-x_{c_*})+(Y-y_{c_*})]
 >=1-rho-rho/tau^2`.                                                   (4.8)

This proves the theorem. QED.

The conclusion is deliberately aggregate: it does not assert that a generic tiny principal minor is useful.

## 5. Consequence for conditional rank-three Pluecker mass

Apply Theorem 4.1 to (2.3). If the triangle branch occurs, at least one of its three edges has

`w_{jk} >= (1-rho-rho/tau^2)/3`.                                      (5.1)

Hence a genuine physical triple containing the original pivot `i` satisfies

`W_{ijk} >= c_i(1-rho-rho/tau^2)/3`.                                  (5.2)

If the star branch occurs, then for some `j`

`P(i,j both in the volume sample)
 = c_i q_j
 >= c_i(1-rho-tau)`.                                                   (5.3)

The left side of (5.3) is the determinant of the `2x2` Gram matrix of rows `u_i,u_j`; thus the star branch is quantitative **two-coordinate spectral-area localization**, not merely large individual leverage.

A particularly clean numerical collar is

`rho<=1/64`, `tau=1/4`.

Then

`kappa=1-1/64-1/4=47/64`.                                              (5.4)

If `c_i>1/2`, either

* some residual row has conditional leverage `q_j>=47/64>1/2`; or
* some physical triple has

  `W_{ijk} >= (1/2)(47/64)/3 = 47/384`.                                (5.5)

No dimension enters these constants.

## 6. Direct application of the newest nested-heavy theorem

The star outcome in (5.4) is exactly the hypothesis needed by account03/B13: the first row is heavy (`c_i>1/2`) and a second row has residual leverage

`h=q_j>=47/64>1/2`.

Therefore the completed B13 theorem applies without any new rotation of the input law. In its notation, let `d_*` be the largest squared coefficient in the final transverse physical direction and

`Delta=det(I-r_i r_i^T-r_j r_j^T)`

for the selected nested-heavy pair. Then:

* if `d_*>=1/6`, the density is bounded by `<275.505`;
* if `d_*<1/6` but `Delta>=1/16`, the density is bounded by `<26.940`;
* consequently, along any unbounded-density sequence inside this star branch one must have simultaneously

  `d_* ->0` and `Delta->0`.                                            (6.1)

Thus the previous vague residual-near-coloop branch has been reduced further: when `rho<=1/64`, the only unhandled star configurations are the simultaneous final-direction diffuse / two-row covariance-saturation limit (6.1).

This is a direct source-bound application of a completed peer theorem, not a restatement of its conclusion.

## 7. Exact Schur pseudo-determinant bookkeeping

The same conditioning has a useful signed determinant identity.

### Lemma 7.1 — `QFORM-RANK3-SCHUR-PSEUDODET-v1`

Let `d=A_ii!=0` and let

`S=A[-i,-i]-A[-i,i]A[i,-i]/d`

be the physical scalar Schur complement. Since `rank A=3`, `rank S=2`. Then

`e_2(S)=det(Lambda)c_i/d`,                                             (7.1)

where `e_2(S)` is the product of the two nonzero eigenvalues of `S`.

### Proof

For every residual pair `{j,k}`, Schur's determinant identity gives

`d det S[{j,k}] = det A[{i,j,k}]`.

Sum over all pairs. Since `rank S=2`, the sum of its principal `2x2` minors is `e_2(S)`. Since

`det A[{i,j,k}]=det(Lambda) W_{ijk}`,                                  (7.2)

(2.2) yields

`d e_2(S)=det(Lambda) sum_{j<k}W_{ijk}=det(Lambda)c_i`.

QED.

Thus a small physical scalar pivot is not loss of spectral determinant: the residual rank-two pseudo-determinant grows reciprocally. Any future analytic payment should preserve (7.1), rather than pay `|d|^{-1}` and the residual determinant separately.

There is an exact second-stage version. If `b=S_jj!=0`, let `T` be the next scalar Schur complement; it has rank one, with its unique nonzero eigenvalue `theta`. Then

`d b theta = det(Lambda)c_i q_j.                                       (7.3)`

Indeed, apply (7.1) in rank two to `S`: `b theta=e_2(S)q_j`, then substitute (7.1). Equation (7.3) is the determinant-weighted two-pivot chain corresponding to the star outcome (5.3).

## 8. Actual application of compatible account04 mathematics

The triangle outcome gives a selected physical triple `B=A[{i,j,k}]` with

`|det B|=|det Lambda|W_{ijk}`.                                         (8.1)

Under the clean collar (5.4)-(5.5), `|det B|>=47/384` because `|det Lambda|>=1`.

If this triple admits a scalar pivot `a` with `|a|>=1/2` whose Schur complement is definite, the completed account04/B18 theorem (1.1) gives the concrete source-valid bound

`||p_Q||_infinity
 <=2 sqrt(pi) (|a det B|)^(-1/4)
 <=2 sqrt(pi) (768/47)^(1/4)
 <7.128`.                                                              (8.2)

Outside coordinates and couplings are allowed by that theorem because the conditioning is on original independent coordinates. This is an actual inequality application of the completed account04 result. If the selected triple has indefinite Schur complement, account03/B16 instead supplies the unified `16 sqrt(15)(|a det B|)^(-1/4)` payment. If all usable scalar pivots are near zero, this becomes a separate near-light-cone branch rather than an excuse to discard the large determinant mass.

## 9. What this run changes

The previous B07 state reduced rank exactly three to diffuse payment, minority-pivot payment, or a bounded-depth heavy-coordinate exception. The new theorem resolves an important ambiguity in the heavy exception:

* **residual disjoint mass not tiny:** retain the existing rank-two cross aggregation route;
* **residual disjoint mass `rho<=1/64`:** there is no amorphous near-coloop case. One gets either a quantitatively large physical triple `(W>=47/384)` or a genuine nested-heavy second row `(h>=47/64)`;
* **nested-heavy second row:** the newest B13 theorem pays it unless both its final-bank parameter and covariance determinant simultaneously collapse;
* **large triple:** completed local product-trace theorems pay it whenever a scalar pivot is not near the light cone, with (8.2) as the definite-Schur account04 application.

Accordingly the first rank-three structural debt is now the joint limit

`rho small`, `d_* small`, `Delta small`, and no selected large triple has a quantitatively usable scalar pivot.                              (9.1)

This is substantially narrower than arbitrary diffuse determinant mass.

For the **full owner target**, arbitrary additional spectral components remain a separate debt: they can change actual physical Schur complements even when three selected eigenvectors have the geometry above. The balanced self/cross resource theorem from account01/B19 is the current compatible route for that cancellation problem. No full-target closure is claimed.

## 10. Regularity and claim status

The new results here are finite-dimensional algebra/combinatorics plus source-valid applications of completed analytic theorems. They prove supporting density bounds on the stated branches. They do **not** prove the unrestricted QFORM conjecture and do not prove a continuous density representative for the new local branches.
