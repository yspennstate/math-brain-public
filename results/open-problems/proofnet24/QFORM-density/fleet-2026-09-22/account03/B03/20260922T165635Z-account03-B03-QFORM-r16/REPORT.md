# account03/B03 — exact pair-law Plancherel identity and fragmentation obstruction

Run: `20260922T165635Z-account03-B03-QFORM-r16`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: decoupled time integral  
Status: **PROVED SUPPORTING LEMMA + SOURCE-VALID OBSTRUCTION TO A NATURAL TT* STEP; FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and scope

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_j<=1`, and let `A=A^T`. Put `Q=X^T A X` and `phi(t)=E exp(itQ)`. The full programme asks for a universal essential-density bound when `A` has at least three eigenvalues of modulus at least one. This report does not claim that full theorem. It proves an exact dependence-safe representation for `|phi|^2`, obtains the sharp one-coordinate conditional Plancherel cost allowed by only `f<=1`, and gives an explicit cap-one fragmented-support family showing that the obvious averaged conditional-L2 closure is not dimension free.

This directly respects the live correction that `U=X+X'` and `V=X-X'` are not independent after decoupling.

## 2. Exact one-coordinate pair law

Let `X,X'` be iid with density `f`, `0<=f<=1`, and set

`U=X+X'`, `V=X-X'`.

The change of variables `(x,x')->(u,v)` has inverse `x=(u+v)/2`, `x'=(u-v)/2` and Jacobian `1/2`. Hence the exact joint density is

`g(u,v) = (1/2) f((u+v)/2) f((u-v)/2)`.

For fixed `u`, write `h_u(v)=g(u,v)` and

`m(u)=int h_u(v) dv = (f*f)(u)`.

Because `0<=f<=1`,

`0<=h_u(v)<=1/2`, `0<=m(u)<=1`,

and, exactly,

`int h_u(v)^2 dv = (1/2) (f^2*f^2)(u) <= (1/2)(f*f)(u) = m(u)/2`.      (2.1)

The factor `1/2` is sharp: equality holds for every indicator density `f=1_E` of a measurable set `E` of measure one.

With Fourier convention `H_u(s)=int exp(isv)h_u(v)dv`, Plancherel gives, for every nonzero real `a`,

`int_R |H_u(a t)|^2 dt = (2 pi/|a|) int h_u(v)^2 dv <= (pi/|a|) m(u)`.      (2.2)

If `m(u)>0` and `chi_u=H_u/m(u)` is the conditional characteristic function of `V|U=u`, then

`m(u) int_R |chi_u(a t)|^2 dt = (2 pi/|a|) [int h_u^2/m(u)]`.              (2.3)

Thus the correct averaged conditional cost is governed by the ratio `int h_u^2/m(u)`, not by a false conditional density cap.

## 3. Exact n-dimensional independent-copy identity

Let `X'` be an independent copy of `X`, and define coordinatewise `U=X+X'`, `V=X-X'`. Since `A` is symmetric,

`Q(X)-Q(X') = U^T A V`.

The coordinate pairs `(U_j,V_j)` are independent across `j`, but `U_j` and `V_j` are generally dependent within each pair. If `h_{j,u}` and `H_{j,u}` are defined as above from `f_j`, then Fubini gives the exact identity

`|phi(t)|^2 = int_{R^n} prod_{j=1}^n H_{j,u_j}( t (A u)_j ) du`.           (3.1)

No rotated-coordinate independence and no `U_j`--`V_j` independence is used. Formula (3.1) is the correct starting point for a decoupled-time estimate.

## 4. A decisive fragmentation obstruction to the one-pair TT* closure

A tempting next step is to use (2.3) for one active coordinate and average in `u` under its actual sum density `m(u)`. This would require a universal bound on

`F(f) := int_{m(u)>0} [int h_u(v)^2 dv / m(u)] du`.                       (4.1)

No such bound exists, even for cap-one indicator densities.

### Proposition 4.1 (explicit fragmented-support blowup)

For every integer `N>=1` there is a probability density `f_N<=1` for which

`F(f_N)=(N+1)/2`.

### Proof

Fix a base `M>=10` and let

`I_k=[M^k, M^k+1/N]`, `k=1,...,N`,

`E_N=union_k I_k`, `f_N=1_{E_N}`.

The intervals are disjoint and `|E_N|=1`, so `f_N` is an admissible probability density. The unordered pair sums `M^k+M^ell` are all distinct by uniqueness of their base-`M` digit patterns. Their mutual separations exceed `2/N`; hence the intervals `I_k+I_ell`, `1<=k<=ell<=N`, are pairwise disjoint. Each has length `2/N`, so

`|E_N+E_N| = [N(N+1)/2] (2/N) = N+1`.                                   (4.2)

Because `f_N^2=f_N`, equality holds in (2.1): whenever `m_N(u)>0`,

`int h_{N,u}^2 dv / m_N(u) = 1/2`.                                      (4.3)

The positivity set of `m_N=f_N*f_N` agrees up to endpoints with `E_N+E_N`. Therefore (4.2)--(4.3) give

`F(f_N)=(1/2)|E_N+E_N|=(N+1)/2 -> infinity`.                             (4.4)

This proves the proposition. QED.

### Consequence

The exact conditional Plancherel estimate is useful only before the fragmentation cost is separated from the remaining coordinates. In particular, the route

`independent-copy identity -> condition on U_j -> one-coordinate Plancherel -> integrate the normalized conditional L2 cost in u_j`

cannot yield a law-uniform constant under the sole assumption `f_j<=1`. The failure is not the previously refuted pointwise van-der-Corput statement; it is a different, exact TT* obstruction caused by arbitrarily large sumset support. Any successful decoupled-time proof must retain cancellation/coupling among at least two original coordinate pairs, or aggregate a bank before paying this normalization.

A finite-support version remains true: if the positivity set of `f*f` has measure `L`, then (2.1) gives `F(f)<=L/2`, and Proposition 4.1 shows this dependence on `L` is sharp for indicator laws. Such an `L` is not controlled in the owner problem.

## 5. Completed account04 mathematics applied to an actual linear-small-ball branch

The designated partner `account04/B03` had no completed current-QFORM handoff or canonical QFORM run available at the fresh scan, so no partner result is invented. I instead apply the completed compatible account04 result from `account04/B16`, run `20260922T161909Z-account04-B16-QFORM-r2`, canonical mathematics `yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`.

That theorem concerns an exact-rank-three frame in its nested-heavy branch. If physical row `i` has leverage `c>1/2` and row `j` has residual leverage `h>1/2`, then its fixed-pair determinant-bank mass satisfies

`P_ij = |det Lambda| c h > |det Lambda|/4`.

If an eligible normalized bank atom has weight `w_k>=tau`, its completed zero-diagonal triple estimate yields

`||p_Q||_infinity <= C_off (4/tau)^(1/3)`,

where `C_off=4.8117455951457755...`, using `|det Lambda|>=1` in the exact-rank-three target. Taking `tau=1/8` gives the explicit numerical inequality

`||p_Q||_infinity <= 4.8117455951457755 * 32^(1/3)`

`                      = 15.276340039075507...`.                         (5.1)

Consequently every interval `I` obeys

`P(Q in I) <= 15.276340039075507... |I|`                                (5.2)

on that large-eligible-atom branch. This is a genuine linear small-ball estimate. It also isolates the only unpaid part of this nested-heavy exact-rank-three mechanism: the diffuse bank with all eligible atom weights below `1/8` (plus, for the full owner theorem, arbitrary additional spectral components).

The obstruction in Section 4 explains why this diffuse branch cannot be closed merely by normalizing and separately Plancherel-estimating one sum/difference coordinate pair: the resulting average can pay an unbounded sumset-support factor even for the simplest cap-one product laws.

## 6. First unpaid implication and next mechanism

The assignment-level first unpaid implication is now:

> Prove a genuinely multi-pair/bank decoupled-time estimate that controls the diffuse determinant-bank branch before dividing by any one-coordinate sum density, ideally at the aggregate scale `P_ij^(-1/3)` or another dimension-free invariant, while preserving arbitrary fragmented cap-one inputs and arbitrary outside couplings.

The exact identity (3.1) suggests that the averaging must be performed jointly in two or more pair variables `u_j` before Cauchy--Schwarz/Plancherel normalization. A one-pair TT* closure is source-validly ruled out by Proposition 4.1.

Full QFORM conjecture: **OPEN / NOT PROVED**. Continuity: **NOT PROVED by this report**.
