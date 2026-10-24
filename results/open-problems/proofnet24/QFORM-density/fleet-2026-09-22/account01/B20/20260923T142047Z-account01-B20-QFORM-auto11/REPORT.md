SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T14:20:47Z.
attacking: the first unpaid N3 double-anchor packet; splice the newest account02/B20 two-by-two anchor into the completed double-anchor E5/Schur bridge and force either a continuous density payment or an explicit low-effective-rank/two-star survivor.

# account01/B20 — double-anchor Schur payment at a universal N3 scale

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T142047Z-account01-B20-QFORM-auto11`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

## 1. Scope and source pins

The target is the unrestricted statement: independent original-coordinate real variables `X_i` with probability densities `0<=f_i<=1`, an arbitrary real symmetric matrix `A`, and at least three eigenvalues of `A` of absolute value at least one. The goal is a single universal finite essential-supremum bound for the density of `Q=X^TAX`, or a target-valid counterexample. No Gaussian, moment, iid, compact-support, log-concavity, diagonal-basis or post-rotation independence hypothesis is introduced here.

Fresh owner control remains revision `2026-09-22.15`, QFORM-only. The live correction set was retained: no law-uniform pointwise quadratic Fresnel decay; no post-rotation independence; no arbitrary-joint rank-three coarea shortcut; no worst-fiber conditional cap; no deletion of a small random tail on unbounded inputs; and no inference that aggregate determinant mass by itself supplies one uniformly good physical minor.

The newest completed designated partner actually consumed is account02/B20 run `20260923T135926Z-account02-B20-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@a71dd6ede2dbff2508586f8cd3cdef0cf624b592`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T135926Z-account02-B20-QFORM-auto11/REPORT.md`.

It starts from the account01/B20 leverage-free N3 cross-cut. Put

`c_*=(63/128)^2=3969/16384`.

For its concentrated nested branch there is an actual original-coordinate cross block `N=A[J,K]`, with

`E=||N||_F^2>c_*`,

and fixed distinct physical row anchors `i,r in J` and fixed distinct physical column anchors `j,s in K` such that the selected double-anchor third-minor mass satisfies

`Z_22 > E^3/M`,

`M=3538944000`.                                                   (1.1)

The same partner proves this after first paying the one-anchor diffuse branch by its new Jensen extension; hence (1.1) is a genuine residual packet, not an unjustified large-minor selection.

The analytic transport input is account03/B02 r28, canonical mathematics

`yspennstate/math-open-problems@3dc52765d1ebb50341bba6a4fea5ca8d68f97372`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T105738Z-account03-B02-qform-r28/REPORT.md`.

Its theorem `QFORM-DOUBLEANCHOR-E5-SCHUR-BRIDGE-v1` says that for a physical cross block

`B=[[P,R],[C,M0]]`

with invertible `2x2` anchor `P`, `D=|det P|`, and true cross-Schur residual

`S=M0-C P^{-1}R`,

if

`G=||det(P)M0-C adj(P)R||_F^2=D^2||S||_F^2`

and `rho=sr(S)=||S||_F^2/||S||_op^2>3`, then the full ambient form has an integrable characteristic function and

`||p_Q||_infinity
 <= C5 [6rho/(rho-3)]^(1/10) D^(2/5) G^(-3/10)`,               (1.2)

where

`C5=(e/20) B(1/10,1/40)=6.770121056043999...`.

This theorem retains arbitrary same-bank quadratic curvature, all outside coordinates and couplings, and every affine term created by conditioning.

## 2. The account02/B20 double-anchor mass is exactly a Schur-Frobenius packet

Restrict `N` to the two fixed anchor rows and columns from (1.1) together with precisely the residual row and column banks used by the partner's selected family. Reorder the anchors first and write this genuine physical cross block as

`B=[[P,R],[C,M0]]`,                                               (2.1)

where `P=N[{i,r},{j,s}]` is `2x2`.

For every residual physical row `b` and residual physical column `c`, Laplace/Schur expansion gives the exact identity

`det B[{i,r,b},{j,s,c}]
 = det(P) (M0)_{bc} - C[b,:] adj(P) R[:,c]`.                    (2.2)

The account02/B20 selected family contains all admissible residual `(b,c)` pairs inside its two remaining nested banks. Therefore summing (2.2)^2 gives

`boxed:
 G:=||det(P)M0-C adj(P)R||_F^2 = Z_22.
}`                                                                 (2.3)

Combining (1.1) and `E>c_*` yields the absolute dimension-free floor

`boxed:
 G > g0 := c_*^3/M
          =4.0170735956385206...e-12.
}`                                                                 (2.4)

This is the required equation-level consumption of the completed account02/B20 result.

## 3. N3 supplies a universal upper bound on the anchor determinant

The current global compiler is inside `N3(1/64)`. Thus for every physical coordinate `u`,

`|A_uu|<1/64`,

and for every distinct `u,v`,

`|A_uu A_vv-A_uv^2|<1/64`.

Hence every off-diagonal physical coefficient obeys

`A_uv^2
 <= |A_uu A_vv|+|A_uu A_vv-A_uv^2|
 <1/4096+1/64
 =65/4096`.                                                      (3.1)

Every entry of the cross anchor `P` is such an off-diagonal coefficient. Therefore

`D=|det P|
 <= |P_11P_22|+|P_12P_21|
 <2*(65/4096)
 =65/2048`.                                                       (3.2)

The point is important: the E5/Schur density bound (1.2) contains the *positive* power `D^(2/5)`, so an upper bound on the physical anchor determinant is exactly what is needed. No reciprocal tiny-pivot loss occurs on this branch.

## 4. New payment theorem at stable rank only 3+1/64

Assume first that `det P !=0` and put

`rho=sr(S)`.

Take the fixed universal threshold

`rho0=3+1/64=193/64`.                                             (4.1)

If `rho>=rho0`, then

`6rho/(rho-3) <= 6rho0/(rho0-3)=1158`,                          (4.2)

because `rho/(rho-3)` is decreasing for `rho>3`.

Substitute (2.4), (3.2) and (4.2) into (1.2):

`||p_Q||_infinity
 < C5 * 1158^(1/10)
      * (65/2048)^(2/5)
      * (M/c_*^3)^(3/10)`.                                      (4.3)

The right side is

`9045.39872498047...`.

Thus:

### `QFORM-N3-2X2ANCHOR-HIGHSR-SCHUR-PAYMENT-v1`

On the newest account02/B20 double-anchor branch, if the physical `2x2` cross anchor is invertible and the true cross-Schur residual satisfies

`sr(S)>=193/64`,

then the complete ambient quadratic form has a bounded continuous density with

`boxed: ||p_Q||_infinity <9046.`                                (4.4)

The characteristic function is in `L1`, so the density has a continuous representative vanishing at infinity on this branch.

This is a strict strengthening of the earlier `sr(S)>=4` payment: the unpaid invertible-anchor packet is now confined to a stable-rank collar of width only `1/64` above the critical value three.

## 5. Exact structural meaning of failure

Suppose `det P !=0` but the payment gate fails:

`sr(S)<193/64`.

Since `G=D^2||S||_F^2`,

`||D S||_op^2
 =D^2||S||_op^2
 > (64/193)D^2||S||_F^2
 =(64/193)G`.                                                    (5.1)

Together with (2.4),

`boxed:
 ||det(P)M0-C adj(P)R||_op
 > (8/sqrt(193)) sqrt(g0)
 =1.15416055249...e-6.
}`                                                                 (5.2)

So failure is no longer an arbitrary Frobenius double-anchor packet. It is an explicit low-effective-rank compound-Schur matrix with a fixed operator-norm direction. This is structural currency only; the matrix in (5.2) is a determinant/deshear matrix and is not silently treated as a new independent-coordinate cross coefficient matrix.

Now suppose instead that `det P=0`. Since `G>0`, `P` cannot be the zero matrix. Thus `rank P=1`. Let

`sigma=||P||_op>0`

and factor

`adj(P)=sigma u v^T`

with unit vectors `u,v`. Equation (2.3) becomes exactly

`G=sigma^2 ||C u||_2^2 ||R^T v||_2^2`.                          (5.3)

Moreover (3.1) gives

`sigma<=||P||_F<2 sqrt(65)/64=sqrt(65)/32`.                     (5.4)

Hence the singular-anchor survivor obeys the genuine inverse-free two-star lower bound

`boxed:
 ||C u||_2 ||R^T v||_2
 > sqrt(g0)/sigma
 > 32 sqrt(g0)/sqrt(65)
 =7.95514672488...e-6.
}`                                                                 (5.5)

Again this is a structural packet, not yet a density theorem.

## 6. What this closes and the first remaining implication

The newest account02/B20 double-anchor packet has therefore been reduced exhaustively to three cases:

1. `det P!=0` and `sr(S)>=193/64`: **PAID**, continuously, by (4.4), with `||p_Q||_infinity<9046`;
2. `det P!=0` and `sr(S)<193/64`: explicit low-effective-rank deshear packet (5.2);
3. `det P=0`: explicit inverse-free two-star packet (5.5).

Thus the high-effective-rank double-anchor geometry is no longer an open branch. The first remaining implication inside this packet is

`QFORM-N3-2X2ANCHOR-LOWRANK-OR-SINGULAR-PAYMENT-v1`:

> Starting from either the fixed compound-Schur operator reserve (5.2) with `sr(S)<193/64`, or the singular-anchor two-star product (5.5), route the state to an existing grouped-hub / physical-pair / mixed-volume receiver while retaining arbitrary opposite-bank curvature and without deleting any random tail.

The separate account01/B20 near-rank-one and near-rank-two cross-cut tubes remain open full-target debts. The exact-rank-three finite-core branch has additional paid subcases, but those are not promoted to arbitrary rank here.

## 7. Corrections and scope audit

The proof above never uses:

- uniform pointwise decay for one-dimensional quadratic phases;
- independence after rotating the random vector;
- an arbitrary-joint coarea bound;
- a worst-fiber conditional density cap;
- deletion of a small cross tail;
- a claim that aggregate volume forces one large coordinate minor.

Only original-coordinate physical cross banks are used probabilistically. Singular values and stable rank enter solely as deterministic algebraic summaries of the true Schur residual after the two physical anchors have already been fixed.

Full QFORM remains **OPEN**. No target-valid counterexample was found. Global continuity remains **OPEN**; continuity is proved only on the paid branch (4.4).
