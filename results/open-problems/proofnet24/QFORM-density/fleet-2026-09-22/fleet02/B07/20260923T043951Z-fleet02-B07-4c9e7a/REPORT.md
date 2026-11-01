# fleet02/B07 — incident `E2` lifts to anchored third compound before localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Coordinate minor selection  
**Status:** `ESSENTIAL_STEP_APPLIED / CONCENTRATED INCIDENT-E2 BRANCH PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved or disproved here. The contribution is a deterministic matrix theorem that upgrades the *actual incident second-minor bank* in the current fleet03/B07 survivor to a quantitative anchored third-minor bank, before choosing any individual minor. Its fully concentrated branch is then paid by the already-completed physical-core receiver; its genuinely conditional-diffuse branch remains open with arbitrary same-bank curvature.

## 1. Fresh source state and first unpaid implication

Fresh owner control at the last pre-write refresh was revision `2026-09-22.15`, QFORM-only, with no B07 pause. The live correction ledger still includes the prohibitions against selecting a single tiny cross minor, deleting extra cross curvature, using arbitrary-joint coarea, or claiming independence after a physical rotation.

The designated partner result actually consumed is fleet03/B07 r23,

`yspennstate/math-open-problems@e24329a6a315b96a87b3efc608473ef0554f3b8d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T033734Z-fleet03-B07-qform-r23/REPORT.md`.

Its incoming r22 state has disjoint physical star norms `C,R`, a physical cross block `M`, `F=||M||_F`, and

`CRF>kappa`, `kappa=1/(256 sqrt(3))`.

On the non-low-tail branch

`T := dist_F(M, rank<=2)^2 = sum_{j>=3} s_j(M)^2 >= theta F^2`.

In the partner's actual row/column compiler, around physical row `i` and column `a`, write

`M = [[b,r^T],[c,D]]`

and

`Z_ia := sum_{k!=i,l!=a} det M[{i,k},{a,l}]^2 = ||bD-cr^T||_F^2`.

One partner alternative is a physical edge; the other gives, in particular,

`sqrt(Z_ia) > (11 theta/7200) F^2`.

The first unpaid implication after this run is therefore:

`QFORM-T4-EDGE-OR-CONDITIONAL-DIFFUSE-ANCHORED-E3-RECEIVER-v1` — pay either the partner's physical-edge branch, or an anchored third-volume packet whose residual pair/singleton inclusion law is genuinely diffuse, while retaining arbitrary same-bank quadratic curvature and all nonzero cross tails. The concentrated anchored-third-volume branch is paid below.

## 2. New theorem: incident `E2` forces anchored `E3` away from rank two

For a real `m x n` matrix `M`, fix a physical row `i` and physical column `a`. Permuting coordinates only in the notation, put these first and write

`M = [[b,r^T],[c,D]]`.

Define the complete incident second-minor mass

`Z_ia(M) = sum_{k!=i,l!=a} det M[{i,k},{a,l}]^2`

and the complete anchored third-minor mass

`W_ia(M) = sum_{k<m, k,m!=i; l<n, l,n!=a}
              det M[{i,k,m},{a,l,n}]^2`.

Let

`T_2(M)=dist_F(M,rank<=2)^2=sum_{j>=3}s_j(M)^2`.

### Theorem 2.1 — `QFORM-INCIDENT-E2-ANCHOR-LIFT-v1`

For every real matrix `M` and every physical row/column pair `(i,a)`,

`boxed( W_ia(M) >= (1/2) T_2(M) Z_ia(M). )`                 (2.1)

The constant `1/2` is sharp: equality holds for `M=I_3` with the first row and column anchored.

This is a determinant-weight statement. It does not infer a good individual minor.

### Proof for `b != 0`

Set the incident Schur numerator

`N = bD-cr^T`.

Every incident `2x2` determinant is an entry of `N`, hence

`Z_ia = ||N||_F^2`.                                           (2.2)

For residual row pairs `K` and column pairs `L`, ordinary determinant Schur expansion at the scalar cross entry `b` gives

`det M[{i} union K,{a} union L] = b det(D[K,L]-c_K r_L^T/b)
                                = det N[K,L]/b`.

Therefore, by Cauchy--Binet,

`W_ia = E_2(N)/b^2`,                                         (2.3)

where `E_2(N)=e_2(NN^T)` is the sum of squared physical `2x2` minors of `N`.

Let `N_1` be a best rank-one Frobenius approximation to `N`, and put

`U = ||N-N_1||_F^2 = sum_{j>=2} nu_j(N)^2`.

Define

`D_1=(cr^T+N_1)/b`,
`M_1=[[b,r^T],[c,D_1]]`.

The scalar Schur complement of `M_1` at `b` is `N_1/b`, of rank at most one, so `rank(M_1)<=2`. Hence

`T_2(M) <= ||M-M_1||_F^2 = U/b^2`,

or

`U >= b^2 T_2(M)`.                                           (2.4)

Write `x_j=nu_j(N)^2`, so `Z=sum_j x_j`, `x_1=Z-U`. Since every `x_j<=x_1`,

`sum_j x_j^2 <= x_1 sum_j x_j = (Z-U)Z`.

Thus

`E_2(N)=1/2[(sum_j x_j)^2-sum_j x_j^2]
          >= ZU/2`.                                          (2.5)

Combining (2.3)--(2.5),

`W_ia >= (ZU)/(2b^2) >= (1/2) Z_ia T_2(M)`.

### The case `b=0`

Replace only the `(i,a)` entry by `epsilon`. All four quantities in (2.1) are continuous functions of the matrix entries. The proved inequality holds for every `epsilon!=0`, and taking `epsilon -> 0` gives (2.1) at `b=0` without division or a hidden invertibility assumption.

### Sharpness

For `M=I_3`, anchored at `(1,1)`,

`T_2=1`, `Z_11=2`, `W_11=1`,

so equality holds in (2.1).

## 3. Apply the theorem to the designated partner r23 state

On the live non-low-tail branch, partner r23 supplies

`T_2(M)>=theta F^2`,

and on its incident alternative

`sqrt(Z_ia) > (11 theta/7200) F^2`.

Theorem 2.1 therefore gives the *same physical anchors* a third-minor packet of mass

`W_ia > (theta F^2/2) * (11 theta F^2/7200)^2`

so

`boxed( W_ia > omega(theta) F^6, )`                           (3.1)

with

`omega(theta)=121 theta^3/(2*7200^2)`.

For the convenient collar `theta=1/16`,

`omega=2.8492491922260804e-10`.

This is stronger structurally than merely knowing a global `E_3`: every determinant in `W_ia` passes through the *same actual physical row and column* produced by the partner compiler. No local reciprocal factor has been taken.

## 4. Required e5 result applied at a real inequality

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

proves D': if a physical cross block has third-volume `E_3` and one orientation of its determinant-volume law has all row inclusion marginals at most `h<3/4`, then

`||p_Q||_inf <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) E_3^(-1/6)`,

with arbitrary self blocks, affine terms and outside couplings retained.

The incoming r22 non-low-tail inequality already gives

`E_3(M) >= (theta^2/6) F^6`.

Therefore, **if the actual third-volume law of `M` has all marginals at most `2/3` on either physical side**, orient that side as the constrained D' side and obtain

`boxed( ||p_Q||_inf
        <= 9 sqrt(3e) (theta^2/6)^(-1/6) F^(-1). )`           (4.1)

If the preceding large-star branch failed, `CR<=Lambda` and `CRF>kappa`, hence `F>kappa/Lambda`. Thus (4.1) is universal:

`||p_Q||_inf < 9 sqrt(3e) (theta^2/6)^(-1/6) Lambda/kappa`.

At `theta=1/16`, `Lambda=1`, `kappa=1/(256sqrt(3))`, this is

`||p_Q||_inf < 38709.377`.

This is an actual use of the completed e5 theorem. It does not assume that the singular-vector range projection is diffuse; it tests the physical determinant-volume marginals themselves.

Hence an unpaid incident-E2 state may be assumed, in addition, to have a `>2/3` third-volume coordinate on both physical orientations.

## 5. Finite-depth anchored concentration tree

Normalize the packet (3.1) to a probability law on residual row pairs and residual column pairs:

`w(K,L)=det M[{i} union K,{a} union L]^2/W_ia`,

where `|K|=|L|=2` and neither contains an anchor.

Let

`gamma_k=P_w(k in K)`, `delta_l=P_w(l in L)`.

Both families sum to two.

### Level 1

If one orientation has every residual pair marginal at most `2/3`, stop and record a **pair-conditional-diffuse anchored packet**. No density conclusion is claimed from this condition alone.

Otherwise choose `k_*`,`l_*` with

`gamma_k*>2/3`, `delta_l*>2/3`.

By the union bound,

`P_w(k_* in K and l_* in L)>1/3`.

Thus the subpacket through the two row anchors `{i,k_*}` and two column anchors `{a,l_*}` has mass

`W_2>W_ia/3`.                                                (5.1)

Condition on these four anchors. Each remaining minor chooses exactly one further row and one further column. Let their singleton laws have marginals `rho_m`,`sigma_n`, each summing to one.

### Level 2

If one orientation has every singleton marginal at most `2/3`, stop and record a **singleton-conditional-diffuse anchored packet**.

Otherwise choose `m_*`,`n_*` with

`rho_m*>2/3`, `sigma_n*>2/3`.

Again the joint event has conditional probability `>1/3`. Consequently one actual physical `3x3` minor satisfies

`det M[{i,k_*,m_*},{a,l_*,n_*}]^2 > W_ia/9`.                 (5.2)

This terminal selection is not a blanket best-minor inference: it occurs only after two proved concentration failures, while the diffuse alternatives are retained explicitly.

## 6. The terminal concentrated branch is a paid six-coordinate spectral core

We are in the sufficient no-pivot class `N3(tau)` with `tau=1/128`. Hence every off-diagonal physical coefficient obeys

`|A_uv|^2 < tau+tau^2`.

For the terminal physical `3x3` cross block `C`,

`||C||_op^2 <= ||C||_F^2 < 9(tau+tau^2)`.

By (3.1) and (5.2),

`|det C| > (sqrt(omega(theta))/3) F^3`.                       (6.1)

Now apply this slot's already-completed determinant-marginal-tail physical-core receiver

`yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`.

With exactly three rows and three columns, it gives for the full ambient quadratic form, after conditioning only outside these original coordinates,

`||p_Q||_inf <= 2 sqrt(36 pi) ||C||_op^2/|det C|`

and therefore

`boxed( ||p_Q||_inf
        < 324 sqrt(pi) (tau+tau^2) omega(theta)^(-1/2) F^(-3). )`  (6.2)

On the inherited collar `F>kappa/Lambda`,

`||p_Q||_inf
 < 324 sqrt(pi)(tau+tau^2) omega(theta)^(-1/2)(Lambda/kappa)^3`.

At `theta=1/16`, `Lambda=1`, `tau=1/128`, this unoptimized universal cap is

`2.33522e13`.

The size of the constant is irrelevant here; the point is that the fully concentrated incident-E2 branch has now been converted into an **actual bounded physical spectral core and paid**, while determinant weights were carried until concentration itself justified localization.

## 7. Exact regression: conditional diffusion is genuine

The earlier target-valid B07 family remains the correct stress test. For even `N`, let

`u=v=N^(-1/2)(1,...,1)`,
`x=y=N^(-1/2)((-1)^j)_j`,

and

`M_N=[[0,u^T],[v,xy^T]]`,
`A_N=[[0,M_N],[M_N^T,0]]`.

The singular values of `M_N` are exactly `1,1,1`, so `A_N` has spectrum containing

`{1,1,1,-1,-1,-1}`.

With the fixed anchor row and column,

`Z_ia=1`, `T_2=1`, and all third-volume mass is anchored: `W_ia=E_3=1`.

Yet every residual pair inclusion marginal equals `2/N`. For `N>=4` the new concentration tree therefore stops immediately in its level-1 pair-conditional-diffuse branch, and every bounded-cardinality physical core still has norm tending to zero as `N->infinity`.

Thus Theorem 2.1 does **not** secretly revive the refuted claim that a constant aggregate packet must contain a uniformly good local minor.

This family is not a QFORM counterexample. The required e5 mixed-Fresnel theorem applies in its special low-rank light-curvature scope: taking the two anchors as heavy coordinates, the residual light quadratic block has rank two with eigenvalues `+1,-1`, the mixed Gram is `I_4`, and every generalized physical leverage is `2/N<=1/2`. Hence

`|phi_Q(t)| <= 16 pi^3 |t|^-3`

and

`||p_Q||_inf <= 3*2^(1/3) < 3.780`.

What remains open is exactly the source-valid version: the same conditional determinant diffusion with **arbitrary same-bank light curvature retained**.

## 8. What was and was not closed

Closed in this run:

1. The actual partner incident-`E2` packet plus non-rank-two tail now forces a quantitative anchored physical third-compound packet by the sharp inequality `W_ia >= T_2 Z_ia/2`.
2. Any current state whose *global* third-volume law is `2/3`-diffuse on one side is paid directly by e5 D'.
3. Within the incident branch, two successive failures of conditional diffusion force one determinant of certified weight and therefore a paid six-coordinate physical spectral core.

Still unpaid:

- the partner physical-edge branch;
- the level-1 pair-conditional-diffuse anchored packet;
- the level-2 singleton-conditional-diffuse anchored packet;
- arbitrary same-bank curvature in those diffuse anchored states.

These are strictly narrower than the preceding generic `incident-E2-plus-inner-stars` debt. The exact `M_N` regression shows why concentration alone cannot remove them.

## 9. Deterministic checks

`CHECKS.py` verifies:

- the exact identity `W_ia=E_2(bD-cr^T)/b^2` for nonzero `b` on 1000 seeded random rectangular matrices;
- `W_ia >= T_2 Z_ia/2` on all of those tests;
- the `b=0` limiting inequality on 750 additional seeded matrices;
- sharp equality for `M=I_3`;
- the displayed live-collar constants.

`CHECKS.txt` ends

`QFORM_INCIDENT_E2_ANCHOR_LIFT_CHECK_PASS`.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Global continuity remains separate and is not claimed here.
