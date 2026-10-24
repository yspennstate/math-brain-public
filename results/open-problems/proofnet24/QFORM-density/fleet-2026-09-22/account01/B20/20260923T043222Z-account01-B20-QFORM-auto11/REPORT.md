SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T04:32:22Z.
attacking: account02/B20 r24's unresolved aggregate W wedge branch by product-preserving random disjointization, followed by an E2-to-third-volume/rank-two compiler.

# QFORM B20 proof-closure report

Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / CONTINUITY_OPEN / WITHOUT_VERIFIED_BRAIN`.

## Control and source provenance

Fresh owner control on `yspennstate/math-research-brain/main` is revision `2026-09-22.15`; QFORM remains the sole research target. The full target is still OPEN and the global continuity claim is still OPEN. Live corrections were reread before this argument; in particular this report does not use law-uniform pointwise quadratic oscillatory decay, post-rotation independence, arbitrary-joint coarea, one-good-minor extraction, or a conditional spectral-density cap.

Designated partner actually consumed: completed `account02/B20` run `20260923T035847Z-account02-B20-QFORM-r24`, canonical mathematics `yspennstate/math-open-problems@0da7f3ef78f89efa33d2014211323fcda3d3214b`. In its physical star block

`C = [[a,m^T],[m,B]]`, `r=||m||>0`, `gamma=s3(C)>0`,

it defines

`W_j = sum_{k<l, k,l != j} (m_k B_{jl}-m_l B_{jk})^2`,
`E_j = sum_{k != j} (m_j B_{jk}-B_{jj}m_k)^2`,
`W=sum_j W_j`, `E=sum_j E_j`,

and proves the exact aggregate lower bound

`W+E >= r^2 gamma^2/2`.

On its actual source survivor `gamma>1/6`, `r>1/48`, hence

`W+E>1/165888`,

so at least one of

`W>1/331776` or `E>1/331776`

holds. The partner had paid a single large `W_j` by a two-gradient theorem but left diffuse `W` and aggregate `E` open.

The reviewed diffuse third-volume receiver used below is Theorem D' source-pinned in the prior B20 handoff to `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, with subsequent review. At row- or column-third-volume marginals at most `2/3`, it gives for a physical original-coordinate cross block `N`

`||p_Q||_inf <= 9 sqrt(3e) e3(NN^T)^(-1/6)`,

retaining arbitrary same-side quadratic blocks and outside couplings.

## New theorem 1: aggregate wedge disjointization

**Claim `QFORM-O3-WEDGE-DISJOINTIZATION-v1`.** For the partner's physical star block, there is a deterministic partition of the leaf coordinates into disjoint original-coordinate banks `J sqcup R` such that, for the physical cross block

`N=C[{hub} union J, R]`,

one has

`e2(NN^T) >= (4/27) W`.

### Proof

Independently place each leaf into `R` with probability `p=2/3` and into `J` otherwise. Fix one summand

`w_{jkl}=(m_k B_{jl}-m_l B_{jk})^2`, `j,k,l` distinct,

appearing in `W`. It is captured by the partition exactly when `j in J` and `k,l in R`, an event of probability

`(1-p)p^2=(1/3)(4/9)=4/27`.

Therefore, for

`T(J,R)=sum_{j in J} sum_{k<l; k,l in R}(m_k B_{jl}-m_l B_{jk})^2`,

we have `E_partition T=(4/27)W`. Hence some deterministic physical partition satisfies

`T >= (4/27)W`.

Now apply Cauchy--Binet to the actual original-coordinate cross block `N=C[{hub} union J,R]`:

`e2(NN^T)=sum_{|S|=|T|=2} det(N[S,T])^2`.

For `S={hub,j}` and `T={k,l}` the determinant is exactly

`det N[{hub,j},{k,l}] = m_k B_{jl}-m_l B_{jk}`.

All terms are nonnegative, so restricting the Cauchy--Binet sum to these captured minors gives

`e2(NN^T)>=T>=(4/27)W`.

This proves the claim. No random rotation is performed; the randomization is only an existence proof for a partition of the original physical coordinates.

## Actual account02/B20 inequality

On the partner's unresolved `W` branch,

`W>1/331776`.

The preceding theorem therefore gives a disjoint physical cross block `N` with

`boxed: e2(NN^T)>4/(27*331776)=1/2239488.`

Thus *all* aggregate `W`, including completely diffuse `W`, has been converted to fixed-scale exterior-two currency on honest disjoint product banks. The previous need to extract one large `W_j` is eliminated.

## New theorem 2: rank-two tube versus third-volume compiler

Let `lambda_1>=lambda_2>=...>=0` be the squared singular values of any matrix `N`, and set

`E2=e2(lambda)`, `E3=e3(lambda)`,
`T2=sum_{r>=3}lambda_r=dist_F(N,{rank<=2})^2`.

Then

`boxed: 3 E3 >= E2 T2.`

Indeed,

`3E3 = sum_{p<q} lambda_p lambda_q sum_{r != p,q} lambda_r`.

Because `lambda_1,lambda_2` are the two largest terms, for every pair `p<q`,

`sum_{r != p,q}lambda_r >= sum_r lambda_r-lambda_1-lambda_2=T2`.

Multiplication by the nonnegative `lambda_p lambda_q` and summation gives the assertion.

Apply this to the disjointized `N`, where `E2>delta:=1/2239488`. Choose

`epsilon := delta/12288 = 1/27518828544`.

Then the entire partner `W` branch has the following exhaustive trichotomy.

### (W1) Small third volume: explicit rank-two tube

If `E3<epsilon`, then

`T2 <= 3E3/E2 < 3 epsilon/delta = 1/4096`,

hence

`boxed: dist_F(N,{rank<=2})<1/64.`

The nonzero tail is retained; it is not deleted or treated as exactly zero.

### (W2) Substantial diffuse third volume: paid

If `E3>=epsilon` and either the row or column third-volume determinant-squared law has every inclusion marginal at most `2/3`, reviewed Theorem D' gives

`||p_Q||_inf <= 9 sqrt(3e) E3^(-1/6)`
`             <= 9 sqrt(3e) epsilon^(-1/6)`
`             = 1412.175593909552...`

and therefore

`boxed: ||p_Q||_inf < 1412.176.`

This is a full ambient quadratic-form payment in the reviewed theorem's scope; same-side blocks and outside couplings remain present.

### (W3) Substantial concentrated third volume: nested two-anchor packet

Otherwise there is a physical row `u` and physical column `v` with third-volume inclusion marginals

`alpha_u>2/3`, `beta_v>2/3`.

Under the same determinant-squared volume law,

`P(u included and v included) >= alpha_u+beta_v-1 >1/3`.

Therefore the total squared third-minor mass simultaneously containing both physical anchors obeys

`boxed: Z_uv > E3/3 >= epsilon/3 = 1/82556485632.`

Conditioned on such an anchored minor, exactly two residual rows and two residual columns remain. Independently two-colour residual row coordinates into `J1,J2` and residual column coordinates into `R1,R2`. A fixed residual row pair is separated with probability `1/2`, and the residual column pair likewise; hence a fixed anchored third minor is captured with probability `1/4`. Averaging yields deterministic disjoint physical banks with nested anchored packet mass

`boxed: P_nested > Z_uv/4 > epsilon/12 = 1/330225942528.`

Again this is an aggregate packet, not a claim that one minor or one edge is large.

## Closure consequence

`QFORM-O3-W-BRANCH-COMPILER-v1` is therefore proved, conditional only on the already completed partner r24 theorem and the already reviewed D' receiver:

From the actual account02/B20 branch `W>1/331776`, one obtains one of:

1. the full ambient density is paid by `||p_Q||_inf<1412.176`;
2. an honest disjoint physical cross block satisfies both `e2>1/2239488` and `dist_F(rank<=2)<1/64`;
3. an honest physical row+column anchored third-volume four-bank packet has mass `>1/330225942528`.

Thus *diffuse W is no longer an independent proof debt*. This is stronger than the partner's single-`W_j` extraction because it spends all `W` before any reciprocal or localization.

The first partner-specific unpaid implication is now the complementary aggregate branch `E>1/331776`, together with the two explicit W survivors (rank-two tube or nested anchor). A natural next attack on `E` is to split

`E <= 2 sum_j m_j^2 ||B_{j,-j}||_2^2 + 2 sum_j B_jj^2 (r^2-m_j^2)`

before reciprocals: the first term is physical hub--leaf--leaf chain energy, the second is diagonal-weighted hub energy. This inequality is recorded only as a router, not as a paid branch.

## Correction discipline

No uniform pointwise quadratic oscillatory decay is used. No rotated coordinate is declared independent. No arbitrary-joint density cap or coarea bound is used. No individual minor is extracted from aggregate volume. All random partitions act on original coordinate labels only, and the resulting analytic receivers are applied only to disjoint original-coordinate banks.

## Keeper state

A fresh native scheduler inventory for account01 showed the same twenty B01--B20 QFORM tasks, all enabled, hourly-valid and quiet, with no managed duplicate, B21/B22, or owner-paused slot to repair. No scheduler mutation was made. Native assignment state remains separate from worker login/check-in state; a missing login is not an outage.

The current actual-hour B20 login and unique start record already existed for run `20260923T043222Z-account01-B20-QFORM-auto11`; they were preserved rather than duplicated. The active QFORM sign-in/check-in request is acknowledged by this run. A unique finish record and source-pinned handoff are to be written after final control refresh.

Model self-report: GPT-5.6 Sol. Configured reasoning effort and provider reasoning-token/thinking-time counters are not exposed and remain `UNKNOWN/null`, not zero.
