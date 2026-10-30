SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T04:36:53Z.
attacking: aggregate ALL physical three-volume packets before reciprocal-minor payment by lifting the disjoint-row-basis entropy construction to the full row/column minor law; classify the small-disjointness failure as three-row volume concentration.

# Global three-volume disjointness before reciprocal-minor inversion

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Logical worker: `fleet03/B02` (Integrated Fourier estimate).  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The full universal conjecture is **not** proved here. This report proves a new supporting integrated-Fourier theorem for an arbitrary original-coordinate cross block, with every row-marginal gate enforced through an explicit entropy reweighting. It also gives an exact structural certificate when that reweighting becomes expensive. No moment, Gaussian, log-concavity, compact-support, connected-support, post-rotation independence, or law-uniform scalar pointwise Fresnel estimate is used.

## 1. Sources actually used

1. Newest volume theorem and sharp q-dependent constants:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   I use its original-coordinate decoupling, determinant expansion, endpoint-safe Brascamp--Lieb treatment, and sharp Hausdorff--Young normalization.

2. Determinant-weighted entropy basis law:
   `yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`, theorem `QFORM-PLUCKER-ENTROPY-BL-v1`.
   I use its conditioned-disjoint-basis entropy construction, but lift it to the **full row/column three-volume law** rather than a single rank-three frame or selected column triple.

3. Previous B02 fixed-three-column packet:
   `yspennstate/math-open-problems@f445f3dd7e2b845f96ac58cc4bd96f12ec7a839c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T040049Z-fleet03-B02-qform-r19/REPORT.md`.
   The present theorem removes the fixed-column-triple selection from that mechanism.

4. Designated partner `fleet04/B02`:
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`, theorem `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`.
   Its genuine L2 Fourier estimate is applied in Section 7 below.

## 2. Setup

Let `I,J` be disjoint sets of ORIGINAL coordinates and let

`M=A[I,J]`.

Condition on all remaining original coordinates. The conditional quadratic-plus-affine form can be written

`Q=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` are arbitrary real measurable functions finite almost surely; in the actual quadratic form they are quadratic-plus-affine functions. The bound below is uniform in them, so averaging over the conditioned coordinates is harmless.

Assume

`Z:=E3(M):=e3(M^T M)=sum_{|R|=|T|=3} det(M[R,T])^2>0`.

Define the canonical full three-volume law

`w_{R,T}=det(M[R,T])^2/Z`.

Let its row-basis marginal be

`mu_R=sum_T w_{R,T}`,

and draw `R,S` independently from `mu`. Define the determinant-weighted disjointness mass

`delta=P(R cap S=empty)`.

No individual minor is assumed large.

## 3. Main theorem

### Theorem 3.1 (`QFORM-GLOBAL-VOLUME-DISJOINT-ENTROPY-L1-v1`)

If `delta>0`, then

`|phi_Q(t)| <= min(1, K |t|^(-3/2))`,

with

`K=e^(3/2) pi^(3/2) delta^(-1/4) Z^(-1/4)`.

Consequently `phi_Q in L1(R)`, the conditional and unconditional laws have continuous densities vanishing at infinity, and

`boxed{ ||p_Q||_infinity <= 3 e delta^(-1/6) Z^(-1/6). }`      (3.1)

All within-bank quadratic terms, outside spectrum/couplings, and affine terms are retained.

### Proof

Let `(R,S)` have law `mu x mu` conditioned on `R cap S=empty`, and let `nu` be the first marginal. Symmetry and disjointness give, for every physical row index `i`,

`2 P(i in R | R cap S=empty)
 =P(i in R | disjoint)+P(i in S | disjoint)<=1`.

Thus every row inclusion marginal of `nu` is at most `1/2`. This is exactly the Hausdorff--Young/Brascamp--Lieb gate; it is not dropped or approximated.

For every row basis with `mu_R>0`, retain the original conditional column law

`w(T|R)=w_{R,T}/mu_R`

and lift `nu` to a full minor law

`pi_{R,T}=nu_R w(T|R)`.

Then the row marginals of `pi` are those of `nu`, hence are at most `1/2`. Its column marginals may be arbitrary in `[0,1]`; the endpoint-safe diagonal-plus-PSD determinant expansion in the cited volume theorem permits this.

The KL cost is

`D(pi||w)=D(nu||mu)`.

By data processing from the conditioned pair to its first coordinate,

`D(nu||mu)
 <=D(Law(R,S | disjoint) || mu x mu)
 =log(1/delta)`.                                             (3.2)

Now apply the standard original-coordinate decoupling. If `X_J'` is an independent copy of `X_J` and `D=X_J-X_J'`, then the coordinates of `D` are independent, each has probability density

`g_j=f_j * tilde(f_j)`

with `||g_j||_infinity<=1`, and

`|phi_Q(t)|^2
 <= integral prod_{i in I}|psi_i(2t(Md)_i)| prod_{j in J} g_j(d_j) dd`.  (3.3)

No sum/difference independence beyond the genuinely independent coordinates of `D` is asserted.

Use the row exponents `alpha_i=P_pi(i in R)` and column exponents `1-beta_j`, where `beta_j=P_pi(j in T)`. They satisfy

`sum_i alpha_i=3`, `sum_j beta_j=3`,

so the Brascamp--Lieb scaling sum is `|J|`. Rows with `alpha_i=0` are dropped using `|psi_i|<=1`; columns with `beta_j=1` are dropped using `g_j<=1`.

For positive Gaussian BL parameters, the diagonal-plus-PSD expansion gives

`det(D_J+M^T D_I M)
 >= Z sum_{R,T} w_{R,T} prod_{i in R} d_i prod_{j notin T} e_j`.

Weighted AM--GM with the alternative law `pi` gives

`det(D_J+M^T D_I M)
 >= Z exp(-D(pi||w)) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j)`.   (3.4)

Hence the Gaussian BL constant is at most

`Z^(-1/2) exp(D/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2)`.                         (3.5)

Since `alpha_i<=1/2`, sharp Hausdorff--Young at output exponent `1/alpha_i>=2` gives, exactly in the normalization of the newest volume theorem,

`|| |psi_i(2t .)| ||_(1/alpha_i)
 <=(pi/|t|)^alpha_i alpha_i^(alpha_i/2)
   (1-alpha_i)^(-(1-alpha_i)/2)`.                            (3.6)

The `alpha_i` factors cancel those in (3.5). The column density norms are at most one. The elementary inequality

`-(1-x)log(1-x)<=x`, `0<=x<=1`,

and the sums of the row/column inclusion marginals yield one factor `e^(3/2)` from each side. Therefore (3.3)-(3.6) imply

`|phi_Q(t)|^2
 <=exp(D/2+3) (pi/|t|)^3 Z^(-1/2)`.                       (3.7)

With (3.2),

`|phi_Q(t)|
 <= e^(3/2) pi^(3/2) delta^(-1/4) Z^(-1/4)|t|^(-3/2)`.

Together with `|phi_Q|<=1`, this proves the pointwise **joint** tail in the theorem. It is not a law-uniform one-coordinate van-der-Corput estimate; all three-volume directions have already been aggregated before the bound is taken.

For `K>0`,

`integral_R min(1,K|t|^(-3/2)) dt =6 K^(2/3)`.

Fourier inversion then gives

`||p_Q||_infinity <=(1/(2pi)) 6K^(2/3)
 =3e delta^(-1/6) Z^(-1/6)`.

Since `phi_Q in L1`, the density is continuous and vanishes at infinity. QED.

## 4. Exact structural complement when delta is small

The same quantity `delta` has an exact residual-volume meaning. For a fixed row triple `R`,

`P(S cap R=empty | R)
 =sum_{S subset R^c} mu_S
 =E3(M[R^c,J])/Z`.                                            (4.1)

Indeed the final equality is just Cauchy--Binet, summed first over column triples and then over row triples contained in `R^c`. Averaging (4.1) over `R~mu` gives

`boxed{ delta=E_{R~mu}[E3(M[R^c,J])/E3(M)]. }`               (4.2)

Therefore some physical row triple `R` with positive `mu_R` obeys

`boxed{ E3(M[R^c,J]) <= delta E3(M). }`                       (4.3)

This is a genuine aggregate-before-inversion alternative: small determinant-weighted disjointness forces almost all three-volume to depend on one physical row triple.

Combining Sections 3-4 with any threshold `0<eta<1` gives the explicit dichotomy

* if `delta>=eta`, then
  `||p_Q||infinity <=3e eta^(-1/6) E3(M)^(-1/6)` and the density is continuous;
* if `delta<eta`, then some physical row triple `R` satisfies
  `E3(M[R^c,J])<eta E3(M)`.

No number of column triples appears in either conclusion.

## 5. Exact-rank-three localization consequence

Suppose additionally `rank(M)=3`, and write a compact SVD

`M=U Sigma V^T`,

where `U,V` have orthonormal columns and `Sigma` is invertible diagonal. Then

`E3(M)=det(Sigma)^2`.

For every row triple `R`,

`E3(M[R^c,J])/E3(M)=det(U_{R^c}^T U_{R^c})`.                 (5.1)

Thus the row triple supplied by (4.3) satisfies

`det(U_{R^c}^T U_{R^c})<=delta`.

All eigenvalues of `G=U_{R^c}^T U_{R^c}` lie in `[0,1]`. Hence its smallest eigenvalue is at most `delta^(1/3)`. For a corresponding unit vector `v in R^3`,

`||U_{R^c}v||_2^2<=delta^(1/3)`,

and therefore

`boxed{ ||U_R v||_2^2 >=1-delta^(1/3). }`                   (5.2)

So failure of the all-column-triple Fourier aggregate produces an actual nearly localized singular-frame direction on only three original coordinates.

Applying the same argument to `M^T` gives a two-sided statement: if both the row and column disjointness masses are below `eta`, then there is a three-row set and a three-column set, each carrying at least `1-eta^(1/3)` of some left/right singular-frame direction. If either side has disjointness mass at least `eta`, Theorem 3.1 (or its transposed proof) supplies the continuous density bound.

A useful numerical threshold is `eta=1/64`: either

`||p_Q||infinity <=6e E3(M)^(-1/6)`,

or one exact-rank-three singular-frame direction has at least `3/4` of its coordinate energy on three physical rows.

## 6. Application of the newest collective-tail source

The volume-stability peer extension records

`E3(M)>=s1(M)^2 s2(M)^2 T2`,

where

`T2=sum_{j>=3}s_j(M)^2`.

Therefore Theorem 3.1 yields, whenever `delta>=eta`,

`boxed{ ||p_Q||infinity
 <=3e eta^(-1/6)
   [s1(M)^2 s2(M)^2 T2]^(-1/6). }`                           (6.1)

Unlike the existing collective-tail exit, (6.1) does **not** require the top-two row-space projection to have coordinate diagonal at most `1/2` or the tail operator norm to be at most `sqrt(T2)/15`. The missing price is explicit and structural: if `delta` is small, (4.3) forces three-volume concentration on one physical row triple instead of pretending the diffuse gate holds.

This is an equation-level use of the newest tail input, not a reproof of it.

## 7. Designated partner fleet04/B02 applied to an actual inequality

On the overlap where there is a nonsingular physical principal `3x3` block `B` with at least one zero diagonal entry, the completed designated-partner theorem gives

`integral_R |phi_Q(t)|^2 dt
 <= A2:=6 pi 2^(2/3)|det B|^(-1/3)`.                         (7.1)

Combine (7.1) with the new high-frequency bound

`|phi_Q(t)|<=K|t|^(-3/2)`

from Theorem 3.1. For every `T>0`, Cauchy--Schwarz at low frequencies and direct integration at high frequencies give

`integral |phi_Q|
 <=sqrt(2T A2)+4K T^(-1/2)`.

Optimizing at `T=4K/sqrt(2A2)` yields

`||p_Q||infinity
 <=(2/pi) K^(1/2)(2A2)^(1/4)`

and therefore

`boxed{
||p_Q||infinity
 <=2^(5/3) 3^(1/4)e^(3/4)
   delta^(-1/8) Z^(-1/8)|det B|^(-1/12)
 <8.845408 delta^(-1/8) Z^(-1/8)|det B|^(-1/12).
}`                                                                   (7.2)

This is a genuine new inequality using the assigned partner result. The direct partner density theorem remains stronger in some parameter ranges; (7.2) is useful when the global three-volume resource is large relative to the single physical determinant.

## 8. Rigorous computation check

`check.py` and `CHECK_OUTPUT.txt` in this run directory perform seeded deterministic regressions for the algebraic identities only. They are not proof substitutes.

Forty random rectangular tests and forty exact-rank-three tests gave:

* max relative error in `E3=sum det^2`: `2.678e-15`;
* max error between the double-disjointness sum and residual-volume average (4.2): `5.551e-17`;
* `min_R E3(M[R^c])/E3(M)-delta` was always nonpositive (largest observed `-2.997e-03`);
* max error in the exact-rank-three residual Gram determinant identity (5.1): `2.776e-15`;
* partner hybrid constant: `8.845407281723`.

The checker ended `STATUS=PASS`.

## 9. What this pays and what remains

This run removes the **column-triple selection debt** from the previous B02 packet theorem: the Fourier/BL argument now pays all row and column three-minors simultaneously through `E3(M)` and a single determinant-weighted disjointness parameter `delta`.

It also gives a source-valid quantitative failure mode: small `delta` is not merely "the Fourier method failed"; it forces a physical three-row concentration of the entire residual three-volume, and in exact rank three it forces an actual singular-frame direction to localize on three original coordinates.

The full QFORM conjecture remains **OPEN** because the bare three-large-eigenvalue hypothesis does not yet provide an exhaustive original-coordinate cross block for which either `E3(M)` and `delta` are both uniformly paid, or the resulting three-row concentration is automatically covered by an existing hub/localized/pair theorem while arbitrary extra spectrum is retained. The next B02 implication is therefore:

`QFORM-THREEROW-VOLUME-CONCENTRATION-ROUTING-v1`:

> Starting from a cross block with `E3(M[R^c]) << E3(M)` for some physical row triple `R`, route the form, without a tiny-minor reciprocal and without dropping arbitrary self curvature/additional spectrum, to either a bounded-dimensional physical core, a mixed-hub/grouped-hyperbolic theorem, or a second cross block to which Theorem 3.1 has nontrivial disjointness.

For exact rank three, the local witness (5.2) makes this a concrete near-localized-direction problem rather than a generic diffuse one.

I did **not** find or claim a valid exact-target counterexample to the stronger universal unweighted `integral |phi_Q(t)| dt` criterion. The theorem above proves that criterion on the stated global-cross-volume branch. Target-wide `L1` Fourier control remains OPEN; full essential boundedness remains OPEN; full-target continuity remains OPEN.

No scheduler/task identity/cadence/enabled-state/notification/email/Drive/workflow/public-release/paid-model/API/Codex/cross-account state was changed.
