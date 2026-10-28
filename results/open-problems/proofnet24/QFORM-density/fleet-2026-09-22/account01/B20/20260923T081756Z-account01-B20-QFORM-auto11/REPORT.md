SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T08:17:56Z.
attacking: account02/B20's near-coloop + high-leverage survivor by converting the high physical leverage row into either an already-paid diagonal/pair certificate or a quantitatively diffuse multi-arm physical star, while retaining the partner's near-coloop geometry.

# account01/B20 auto11 — high-leverage row compiler and near-coloop anchored volume

Programme: `QFORM-DENSITY-3EIG-20260922`.
Classification: `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING COMPILER / FULL TARGET OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Continuity: unchanged globally; the unrestricted target continuity statement remains OPEN.

## 1. Source boundary and completed account02/B20 result consumed


The completed designated-partner result consumed is:

`yspennstate/math-open-problems@4ef597fe9dea9c5b4a91d8ef5d87cb188fe59086`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T070214Z-account02-B20-QFORM-auto11/REPORT.md`.

In the exact-rank-three branch it writes

`A = R Lambda R^T`, `R^T R = I_3`, `min_j |lambda_j(Lambda)| >= 1`,

and proves that every still-unpaid rank-two-cross near-kernel survivor simultaneously has:

1. a physical coordinate `h` with leverage `c_h=||R_h||^2>1/2`; and
2. a spectral unit vector `v` whose squared physical mass on one of the two product banks exceeds

`1-delta_* = 0.977391781546...`,

where

`delta_*=(1-sqrt(1-1/(8sqrt(2))))/2=0.0226082184537...`.

Equivalently the other bank carries less than `delta_*` of the `v`-mass. In the favorable case where the high-leverage row lies on that small-mass bank, its component transverse to `v` is larger than

`sqrt(1/2-delta_*)=0.69093543949...`.

The same partner report obtains this through the exact bank-volume identity

`(s_1(C)s_2(C))^2 ||Br||^2 = |det Lambda|^2 det(G) pdet(I-G)`

and a preceding fixed-scale near-kernel theorem. The unrestricted QFORM theorem is not claimed there.

Two reviewed analytic receivers used below are:

* rank-two affine half-Riesz / rank-three physical-pivot consequence:
  `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
  `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`;
* physical indefinite-pair logarithmic smoothing:
  `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
  `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

## 2. New theorem — `QFORM-HIGHLEVERAGE-ROW-STAR-COMPILER-v1`

Let `A=R Lambda R^T` have exact rank three, `R^T R=I_3`, and `min |lambda_j(Lambda)|>=1`. Let `h` be an original physical coordinate with

`c:=||R_h||^2>1/2`.

Write

`a=A_hh`, `b_j=A_hj` for `j!=h`.

Then at least one of the following holds.

**(D) physical diagonal payment:** `|a|>=1/64`, and the full ambient quadratic form has an essentially bounded density with

`||p_Q||_infinity < 430.539`.

**(P) physical pair payment:** some `j!=h` has `|b_j|>=1/4`, and the full ambient quadratic form has an essentially bounded density with

`||p_Q||_infinity < 143.109`.

**(S) diffuse star survivor:**

`|a|<1/64`, `max_(j!=h)|b_j|<1/4`,

and

`sum_(j!=h) b_j^2 > 2047/4096`.

Moreover in (S) the leaves can be partitioned into two disjoint original-coordinate banks `U,V` with

`sum_(j in U)b_j^2 > 1791/8192`,
`sum_(j in V)b_j^2 > 1791/8192`,

hence

`||A[h,U]||_2, ||A[h,V]||_2 > sqrt(1791/8192)=0.4675766564...`.

They can also be partitioned into three disjoint original-coordinate banks `U_1,U_2,U_3` satisfying, for every `q`,

`sum_(j in U_q)b_j^2 > 1535/12288`,

hence

`||A[h,U_q]||_2 > sqrt(1535/12288)=0.3534382828...`.

### Proof

If `|a|>=1/64`, apply the rank-three physical-pivot consequence from the first reviewed receiver. In its notation, `c>1/2`, `|det Lambda|>=1`, so

`||p_Q||_infinity <=128[c |a| |det Lambda|]^(-1/4)`

`< 128[(1/2)(1/64)]^(-1/4)`

`=128*128^(1/4)=430.5389646...`.

This proves (D).

Assume now `|a|<1/64`. Parseval gives the exact star-energy identity

`sum_j A_hj^2`
`=R_h^T Lambda R^T R Lambda R_h`
`=||Lambda R_h||^2`.

Removing the diagonal term and using `sigma_min(Lambda)>=1`,

`sum_(j!=h)b_j^2`
`=||Lambda R_h||^2-a^2`
`>=||R_h||^2-a^2`
`>1/2-1/4096`
`=2047/4096`.                                             (2.1)

Suppose some `|b_j|>=1/4`, and put `d=A_jj` and

`B=[[a,b_j],[b_j,d]]`.

If `|d|>2`, the same rank-three physical-pivot corollary applied at `j` gives

`||p_Q||_infinity <=128/sqrt(|d|)<128/sqrt(2)<90.51`.

If `|d|<=2`, then

`det B = ad-b_j^2`

satisfies

`det B <= |a||d|-b_j^2 < 1/32-1/16=-1/32`.

Thus `B` is an invertible indefinite physical pair and

`D:=|det B|>1/32`.

We also have `kappa:=sigma_min(B)>1/128`. Indeed, if `|b_j|<=2`, then `||B||_op<=|b_j|+2<=4`, hence `kappa=D/||B||_op>1/128`. If `|b_j|>2`, then `||B||_op<=|b_j|+2<2|b_j|`, while `D>b_j^2-1/32`, and therefore

`kappa>(b_j^2-1/32)/(2|b_j|)>1/128`.

The reviewed physical-pair logarithmic theorem with rank-three spectral scale `s=1` now gives

`||p_Q||_infinity`
`<=8 sqrt(5)(D kappa)^(-1/4)`
`<8 sqrt(5)[(1/32)(1/128)]^(-1/4)`
`=64 sqrt(5)=143.1083505...`.

This proves (P). Hence any unpaid high-leverage row satisfies (S).

For the two-bank partition, set `w_j=b_j^2`. Every weight is `<1/16`. Process the leaves in any order, always assigning the next weight to the currently lighter of two bins. At the end the load difference is less than `1/16`; hence each load is larger than

`(T-1/16)/2`
`>(2047/4096-256/4096)/2`
`=1791/8192`,

where `T=sum w_j`.

For three banks, use the same greedy rule with three bins. The final largest bin was, immediately before its last addition, a currently lightest bin, so its final load exceeds the final smallest load by less than `w_max<1/16`. Consequently, if `m` is the final smallest load,

`T < 3m+2(1/16)`,

and therefore

`m>(T-1/8)/3>(2047/4096-512/4096)/3=1535/12288`.

All partitions are of original physical coordinates. No spectral coordinate is treated as an independent random variable. QED.

## 3. Actual application of the completed account02/B20 result

The partner's unpaid survivor contains a physical row with leverage `>1/2`. Theorem 2 therefore applies immediately at that row. Thus **every still-unpaid partner survivor** must obey the concrete source-coordinate packet

`|A_hh|<1/64`,
`max_(j!=h)|A_hj|<1/4`,
`sum_(j!=h)A_hj^2>2047/4096`,                                  (3.1)

and admits both the two-arm and three-arm balanced physical-star partitions above.

This is a genuine inequality-level use of the account02/B20 output: the abstract statement “some high-leverage coordinate exists” has been converted into a dimension-free original-coordinate star resource. In particular the remaining branch cannot hide the high spectral leverage in one weak physical interaction; after the already-paid diagonal and dominant-edge exits are removed, more than `0.49975` of squared physical star energy remains and no single leaf carries as much as `1/16` of it.

The partner simultaneously supplies the near-coloop vector `v`. Hence the first unpaid implication is no longer a generic near-coloop/high-leverage statement. It is the intersection of a `97.739%` near-coloop with the quantitative diffuse multi-arm physical star (3.1).

## 4. Favorable small-bank orientation — fixed-anchor exterior-volume packet

There is one further deterministic gain in the favorable orientation of the partner geometry.

Use the partner notation `I union J` and choose a spectral orthonormal basis `(q,v,w)` in which `q` is the exact coloop on `I` (`J` has zero `q`-component) and

`G=R_I^T R_I=diag(1,gamma,eta)`.

Suppose the near-coloop is `I`-heavy, so

`gamma>1-delta_*`,

and suppose the high-leverage physical row `h` lies in the small-mass bank `J`. Write that row as

`r_h=(0,y,z)`.

Because total `v`-mass on `J` is less than `delta_*`,

`y^2<delta_*`.

Since `||r_h||^2>1/2`,

`z^2>1/2-delta_*`.

Define the fixed-anchor spectral three-volume mass

`P_h=sum_(i<k; i,k in I) det[r_h;r_i;r_k]^2`.

Cauchy--Binet / the exterior-square cofactor identity gives exactly

`P_h=r_h^T adj(G) r_h`.

Since

`adj(G)=diag(gamma eta, eta, gamma)`,

we obtain

`P_h=eta y^2+gamma z^2`
`>(1-delta_*)(1/2-delta_*)`
`=0.466598803861... .`                                         (4.1)

Randomly two-colour the rows of `I`. Every unordered pair is separated with probability `1/2`, so there is a deterministic physical partition `I=I_1 union I_2` with

`sum_(i in I_1,k in I_2) det[r_h;r_i;r_k]^2`
`>0.233299401930... .`                                         (4.2)

This is a **structural currency**, not yet a density theorem. The spectral basis is used only to calculate matrix volumes; no rotated independence is asserted. The opposite near-coloop orientation is not claimed to follow by symmetry, because the partner's exact coloop is tied to one physical bank.

## 5. What is now unpaid

The full QFORM theorem remains OPEN. This run pays every account02/B20 near-coloop/high-leverage survivor having either

`|A_hh|>=1/64`

or a physical edge

`|A_hj|>=1/4`.

The first remaining implication is therefore:

`QFORM-NEARCOLOOP-DIFFUSE-MULTIARM-PAYMENT-v1` — OPEN.

One must pay the simultaneous state consisting of:

* the account02/B20 near-coloop (`>0.9773917815` of one spectral direction on one physical bank),
* a physical high-leverage row `h`,
* `|A_hh|<1/64`, every `|A_hj|<1/4`, but star energy `>2047/4096`, and
* two-bank arms each `>0.46757` in `l2`, equivalently three-bank arms each `>0.35343`.

The favorable small-bank orientation additionally carries the anchored exterior-volume packet (4.1)--(4.2). A viable next splice is to spend that anchored aggregate volume before reciprocal inversion; in the adverse orientation, use the exact-coloop bank asymmetry together with the three balanced star arms. Deleting the `2.26%` near-coloop leakage as a small perturbation is not permitted for arbitrary unbounded/fragmented cap-one inputs.

No full-target counterexample was found. No Gaussian, iid, moment, bounded-support, log-concavity, or post-rotation-independence assumption was added.
