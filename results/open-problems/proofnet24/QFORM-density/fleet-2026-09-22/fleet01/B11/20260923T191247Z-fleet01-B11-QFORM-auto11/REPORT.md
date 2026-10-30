SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T19:12:47Z.
attacking: the nonzero-hub continuation of the exact-graph near-coloop endpoint; extend the three-variable four-region receiver to every subcritical hub ratio and use the exact graph energy budget to stay uniformly subcritical.

# fleet01/B11 — subcritical-hub coarea and exact-graph completion

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** essential boundedness is proved on the new branches; continuity is not claimed here.

The unrestricted conjecture remains OPEN. No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, or perturbative deletion of an unbounded random quadratic term is used.

## 1. Fresh source and the mechanism change

The fresh owner control remains revision `2026-09-22.15`, QFORM only. I reread the live correction set before starting. In particular, bounded conditional density is not treated as independence, and a small matrix coefficient is not treated as a uniformly small random perturbation on unbounded supports.

Two fresh source results materially change the right endpoint to attack.

1. `proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md` proves a three-variable receiver when a physical scalar hub is independent of a planar vector of joint density cap `M`, the three-dimensional Hessian has least singular value at least one, and the normalized hub diagonal is `<1/64`.
2. `proofnet24/QFORM-density/interactive/20260923T193000Z-quantitative-dpp-near-coloop/EXACT_COLOOP_TRUNCATION.md` isolates the exact physical-coloop model but correctly warns that its small rank-two matrix leakage cannot be discarded on unbounded supports.

The present run does **not** perturb across that leakage. Instead it first extends the coarea receiver to every hub ratio strictly below one, then applies it to the existing B11 one-exact-graph bank endpoint after genuine original-coordinate conditioning. This removes the previously separate `small nonzero hub pivot` obstruction from that exact-graph endpoint.

The designated partner fleet02/B11 result actually used below is

`QFORM-INDEFINITE-SQUARE-INDEPENDENT-SHEAR-v1`,

canonical report `math-open-problems@d618ae04de4d2366b3dc6cd9a67c36dc1bdb9fcf`, which gives the full-line bound `8*2^(1/4)` for `2 X1 X2 + Z^2 + 2 kappa ZW`, uniformly in `kappa`.

## 2. New analytic theorem: the four-region receiver at every subcritical hub ratio

### Theorem `QFORM-SUBCRITICAL-HUB-PLANAR-CORE-v1`

Let `H` be a real random variable with density at most one. Let `(L0,V0)` be independent of `H` and have an arbitrary joint probability density bounded by `M`. Let `T` be a real symmetric invertible `3 x 3` matrix acting on `(H,L0,V0)`, and suppose

`σ_min(T) >= sigma > 0`,

and, for a fixed `0 <= r < 1`,

`|T_HH| <= r sigma`.

Arbitrary deterministic affine terms and a constant are allowed. Then the resulting quadratic polynomial `Q` has an essentially bounded density and

`||p_Q||_infinity <= B(r,M)/sigma`,                                      (2.1)

where

`G0 = (2*pi)^(3/2) exp(1/2) Gamma(1/4)/(4 sqrt(pi) Gamma(3/4))`,

`R(r) = sqrt( 5 + (1+2r)^2/(1-r^2) )`,

and

`B(r,M) = 1 + M [ 2/sqrt(1-r^2) + 2 + G0 R(r) ].`                       (2.2)

Numerically `G0 = 10.8362594669...`.

This extends the cited small-hub receiver from the convenient ratio `1/64` to every fixed ratio below one. The blow-up as `r -> 1` is explicit and expected; no statement is made at `r=1`.

### Proof

Scale by `sigma`, so it suffices to prove the result for `σ_min(T)>=1` and `|T_HH|<=r`. Orthogonally rotate only the deterministic two-dimensional light coordinates so that the hub row is `(a,t,0)`:

`T = [[a,t,0],[t,b,gamma],[0,gamma,lambda]],   |a|<=r.`

This rotation preserves the planar joint density cap and does not assert independence of the two rotated light coordinates. Since `||T e_H||>=1`,

`|t| >= sqrt(1-a^2) >= t0 := sqrt(1-r^2).`                             (2.3)

Reverse the first light coordinate if necessary so `t>0`. As in `GENERAL_3D_CORE.md`, take `z=(-gamma/t,0,1)`. The inequality `||Tz||>=||z||` implies `|lambda|>=1`. Shear

`V = V0 + (gamma/lambda)L0`, `L=L0`.

The shear has determinant one, so the planar density cap remains `M`. The quadratic Hessian becomes `K direct_sum [lambda]`,

`K = [[a,t],[t,b-gamma^2/lambda]].`

The leading `2 x 2` principal block of `T^{-1}` is `K^{-1}`, hence `||K^{-1}||<=1`. Write its lower-right coefficient again as `beta`, put

`D=t^2-a beta`, `u=a h+t l`.

Exactly as in the source four-region proof, `D>0`, `D>=t`, and `D>=|beta|`. Split the source space into four regions.

**Region 1: `|u|>=1`.** The derivative in `h` has modulus at least two. The total `h`-length mapping to an output interval of length `delta` is at most `delta`; contribution `<=delta`.

**Region 2: `|u|<1`, `|v|>=1`.** The derivative in `v` has modulus at least two. For fixed `h`, the `l`-strip has length at most `2/t <=2/t0`; contribution

`<= (2M/t0) delta`.                                                   (2.4)

**Region 3: `|u|<1`, `|v|<1`, `|h|>=2`.** Since `l=(u-ah)/t`,

`|partial_l Q|/2 = |(D/t)h+(beta/t)u| >= (D/t)(|h|-|u|) >=1`.

The eligible `v`-strip has length two, hence this contribution is `<=2M delta`.

**Region 4: `|u|<1`, `|v|<1`, `|h|<2`.** Here

`|l| <= (1+2r)/t0`,

so the entire remaining region is contained in the Euclidean ball of radius

`R(r)=sqrt(5+(1+2r)^2/(1-r^2)).`                                    (2.5)

The joint source density in `(h,l,v)` is at most `M`. Compare Lebesgue measure on this ball with the Gaussian `N(0,R(r)^2 I_3)`. Its density on the ball is at least `(2*pi*R^2)^(-3/2) exp(-1/2)`. Since all three eigenvalues of `K direct_sum [lambda]` have absolute value at least one, the standard Gaussian quadratic characteristic function gives a Gaussian output-density cap

`Gamma(1/4)/(4 sqrt(pi) Gamma(3/4) R^2)`.

Consequently the Lebesgue volume of the part of the ball mapping into an interval of length `delta` is at most

`G0 R(r) delta`,                                                     (2.6)

and Region 4 contributes at most `M G0 R(r) delta`.

Summing (2.4)--(2.6) with Region 1 proves the interval inequality `P(Q in J)<=B(r,M)|J|`. This gives (2.1). Because `T` is invertible, deterministic affine terms are removed by a deterministic translation of the three variables, preserving the hub density cap, the planar cap, and their independence. QED.

## 3. Exact-graph near-coloop endpoint: the nonzero pivot is now paid

Return to the exact-rank-three Parseval factorization

`A=R M R^T`, `R^T R=I_3`, `s=min_j |eig_j(M)|>=1`.

Use the inherited B11 true-near-coloop notation. There is an ORIGINAL hub row

`r_0=sqrt(c) e`, `c>63/64`,

and two disjoint sets of remaining ORIGINAL coordinates `S,T`. Write

`r_i=s_i e+w_i`, `w_i in e^perp`.

Assume bank `S` is an exact graph,

`s_i=q^T w_i` for every `i in S`,                                    (3.1)

and its transverse Gram matrix

`W=sum_(i in S) w_i w_i^T`

satisfies

`lambda_min(W)>=1/32`.                                               (3.2)

No graph, support, or boundedness condition is imposed on bank `T`; it will be conditioned on in the ORIGINAL product coordinates. Assume only the usual physical no-pivot inequality at the hub,

`|A_00|<1/64`.                                                        (3.3)

There is **no requirement that this pivot vanish**.

### Corollary `QFORM-ONEBANK-EXACTGRAPH-ALL-NOPIVOT-v1`

Under (3.1)--(3.3), for arbitrary independent input densities bounded by one,

`||p_(X^T A X)||_infinity < 3656/s`.                                (3.4)

The statement is invariant under `A -> -A`, so it covers both signatures `(+,+,-)` and `(+,-,-)`.

### Proof

Condition on all ORIGINAL coordinates in `T`. Define

`Y = W^(-1/2) sum_(i in S) w_i X_i`.

Its two coefficient columns are orthonormal in the ORIGINAL `S`-source space; therefore its joint density is at most two. It is independent of the untouched ORIGINAL hub coordinate `X_0`.

By the exact graph identity, after conditioning on `T` the spectral vector is an affine translate of

`sqrt(c)e X_0 + e q^T W^(1/2)Y + W^(1/2)Y`.

Thus the conditional three-variable Hessian is

`H=C^T M C`,

with

`C = [[sqrt(c), r^T],[0,W^(1/2)]],   r=W^(1/2)q.`                    (3.5)

Parseval in direction `e` gives the exact longitudinal energy budget

`q^T W q = sum_(i in S) s_i^2 <= 1-c =: eta <1/64.`                (3.6)

Factor

`C = diag(sqrt(c),W^(1/2)) [[1,u^T],[0,I_2]],   u=r/sqrt(c).`

Because the inverse of the last shear has norm at most `1+||u||`, (3.2)--(3.6) imply

`sigma_min(C)^2 >= rho0`,                                           (3.7)

where

`rho0 := (1/32)/(1+1/sqrt(63))^2 = 0.02464803918... .`

Hence

`sigma_min(H) >= s sigma_min(C)^2 >= rho0 s`.                       (3.8)

The physical hub coefficient of `H` is exactly

`H_11 = c e^T M e = A_00`.                                         (3.9)

Combining (3.3), `s>=1`, and (3.8), its ratio to the conditional three-dimensional singular scale is at most

`r0 := 1/(64 rho0) = (1+1/sqrt(63))^2/2 = 0.6339246657... <1`.      (3.10)

Apply Theorem 2 with `M_planar=2`, `sigma=rho0 s`, and `r=r0`. All terms created by conditioning on `T` are deterministic affine terms and are explicitly permitted. A direct evaluation gives

`B(r0,2)=90.09208211...`,

and therefore

`B(r0,2)/(rho0 s)=3655.141954.../s <3656/s`,

proving (3.4). QED.

### What changed relative to the preceding B11 run

The preceding zero-pivot theorem paid this one-bank exact-graph endpoint only when `e^T M e=0`, with the sharper constant `<76.6/s`. The present argument is deliberately coarser but removes the equality assumption completely: every hub pivot that survives the source no-pivot gate is now paid on the same exact-graph endpoint. Thus, in this endpoint, `small but nonzero hub pivot` is no longer a separate obstruction.

The first genuine remaining collar here is now **geometric**: both bank regression residual variances are strictly positive (possibly arbitrarily small), so neither bank is an exact graph. The current source warning remains in force: those residual random terms cannot be deleted just because their coefficient matrices are small.

## 4. Designated partner result applied to an actual inequality

Take four independent cap-one original coordinates and, for arbitrary real `kappa`,

`Q_kappa = 2 X_1 X_2 + Z^2 + 2 kappa Z W`.                          (4.1)

The core `(X_1,X_2,Z)` has least singular value one, zero hub pivot, and planar cap `M=1`. Theorem 2 alone gives a uniform but coarse bound `B(0,1)<31.55` after conditioning on `W`.

Now apply the completed fleet02/B11 theorem `QFORM-INDEFINITE-SQUARE-INDEPENDENT-SHEAR-v1` to the same actual form with `a=b=1`. Its exact square completion and pair-log estimate sharpen this to

`||p_(Q_kappa)||_infinity <= 8*2^(1/4) = 9.513656920...`,            (4.2)

uniformly for every `kappa`.

This is a genuine target family: its spectrum contains `+1,-1` and one eigenvalue of the `(Z,W)` block with magnitude at least one. At `kappa=0` the nonzero spectrum is exactly `{1,1,-1}`.

## 5. The opposite-sign logarithmic endpoint remains visible

For independent centered unit uniforms,

`p_(2X_1X_2)(t)=log(1/(2|t|)),   0<|t|<1/2`.                        (5.1)

So the rank-two opposite-sign saddle is genuinely unbounded. In (4.1) the third direction `Z^2` removes the logarithm by its square-root small-ball law; the residual shear `2 kappa ZW` is absorbed by exact completion after conditioning on the genuinely independent source `W`.

In the new exact-graph compiler the same rank-three mechanism is encoded differently: conditioning the unrelated bank leaves a bona fide scalar-plus-planar three-dimensional Hessian whose least singular value remains a fixed fraction `rho0` of the spectral scale. The third direction is therefore not deleted or averaged away; it supplies the third nonzero curvature used in the central three-dimensional coarea region.

## 6. Verification

The companion checker in this run evaluates `rho0`, `r0`, the Gaussian constant `G0`, `R(r0)`, and the final constant. It also samples random positive-definite `W`, exact-graph slopes satisfying `q^T W q<=1-c`, and verifies the singular-value lower bound (3.7). The deterministic output ends `QFORM_B11_SUBCRITICAL_GRAPH_CHECK_PASS`.

## 7. Exact remaining B11 implication

`QFORM-NEARCOLOOP-TWO-POSITIVE-RESIDUAL-COMPILER-v2`:

> In the one-hub/two-bank exact-rank-three survivor, pay the case in which both bank regression residual variances are strictly positive but may tend to zero, without deleting either residual random term, conditioning on a same-bank projection as though it preserved a cap, or using a pointwise quadratic-phase decay estimate.

A second interface remains beyond exact rank three: arbitrary additional nonseparable spectrum. The full owner target and the global continuity request therefore remain OPEN.
