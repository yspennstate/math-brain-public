SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T13:37:27Z.
attacking: the true near-coloop shared-bank/null-Rayleigh endpoint by isolating the pivot interpolation hidden in the latest account02/B16 bank-aggregate family and retaining the original source banks through the nonlinear quadratic pushforward.

# account01/B16 r34 — bank aggregation removes the null-pivot singularity on a true near-coloop gate-failure family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: projection-product interaction  
Status: **NEW TARGET-VALID ONE-PARAMETER THEOREM / COMPLETED PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Continuity: **global continuity is not proved by this run.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh control and correction-aware scope

Fresh `math-research-brain` control was read before work and again before publication. OWNER CONTROL remained revision `2026-09-22.15`; programme revision remained `2026-09-22.5`; QFORM is the sole mathematical target and there is no later B16 stop.

The full target remains open: for independent real original-coordinate inputs with one-dimensional density caps at most one, and any real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite density bound for `X^T A X`.

This report explicitly preserves the live corrections:

- a bounded joint projection density alone does **not** bound an arbitrary indefinite quadratic level-set integral;
- arbitrary-joint rank-three coarea bounds of the previously proposed form are false;
- positive moments of worst conditional projection-density caps can diverge;
- orthogonal projection preserves a joint density cap but does not create independence;
- one physical triple need not have a uniformly good determinant, so diffuse source banks must sometimes be aggregated before reciprocal determinant payment.

The argument below never conditions on a rotated spectral complement and never asserts independence of projected coordinates. The source-bank sums are functions of disjoint original-coordinate groups, hence their independence is genuine.

## 2. Source-pinned inputs actually used

### 2.1 Completed designated partner account02/B16

The newest completed designated-partner theorem used here is

`QFORM-GATEFAIL-NEARCOLOOP-BANK-AGGREGATE-v1`,

canonical source

`yspennstate/math-open-problems@7dc1a1fb738f263d7fe021dcf3ce5c37223ced4e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T112849Z-account02-B16-QFORM-6a31b2a7/REPORT.md`.

It constructs an exact-rank-three family in the true near-coloop collar `c>63/64` where a one-physical-coordinate determinant certificate deteriorates like `m^(2/3)`, but aggregating two complete original-coordinate banks gives the uniform bound

`||p_Q||_infinity < 210.080 < 211`.                                  (2.1)

The exact source objects and coefficients from that theorem are retained below.

### 2.2 Physical-triple determinant theorem

The completed theorem

`QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`,

canonical source

`yspennstate/math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T202347Z-account03-B16-QFORM-r15/REPORT.md`,

states that for three independent cap-one real variables, every invertible symmetric quadratic block `B` with arbitrary affine term has

`||p||_infinity <= C3 |det B|^(-1/3)`,                               (2.2)

where

`C3=16 sqrt(30) 2^(1/4)=104.21688998922089...`.                      (2.3)

This is used only after genuine original-source aggregation and normalization.

### 2.3 Actual two-dimensional product projection theorem and ruled integration

The pinned ruled theorem package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For every exact-rank-three signature `(+,+,-)` form with all three absolute eigenvalues at least one, its one-sheet side satisfies

`p_Q(s) <= pi sqrt(2)` for a.e. `s>=0`.                               (2.4)

The proof uses the actual two-dimensional product-projection marginal bound `<=2` along hyperboloid rulings; it does not require the two projected coordinates to be independent. This is exactly the valid projection-to-curvature interface on that side.

### 2.4 Same-bank discriminant theorem as context

The fresh account03/B06 theorem

`QFORM-SAMEBANK-TRANSLATED-SQUARE-DISCRIMINANT-v1`,

canonical source

`yspennstate/math-open-problems@71c369d883ef5211a624f1e943e53dcfbcc3dcdd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T131910Z-account03-B06-qform-r36/REPORT.md`,

shows how a nonzero effective scalar pivot can be paid while preserving an arbitrary same-bank translation, but its generic determinant currency degenerates when that effective pivot tends to zero. The theorem below exhibits a true near-coloop source geometry in which that apparent null-pivot singularity disappears after the **correct bank aggregation**.

## 3. The partner near-coloop frame

Fix

`0<a<1/64`, `c=1-a`, `h=1/128`.                                      (3.1)

Set

`q=sqrt(a) h`,
`t1^2=a(1-h)(1-2h^2)`,
`t2=-t1 sqrt(h/(1-h))`,                                               (3.2)

with `t1>0`. In spectral coordinates take

`r0=(sqrt(c),0,0)`,
`u1=(t1,sqrt(h),0)`,
`u2=(t2,sqrt(1-h),0)`,
`u3=(q,0,1/sqrt(2))`,
`u4=(-q,0,1/sqrt(2))`.                                                (3.3)

The partner proves the exact Parseval identity

`r0 r0^T + sum_(nu=1)^4 u_nu u_nu^T = I_3`.                         (3.4)

Keep `u1` as one physical row and diffuse each of `u2,u3,u4` into `m>=64` equal rows `u_nu/sqrt(m)`. For the three disjoint diffuse source banks define

`Y_nu=m^(-1/2) sum_(k=1)^m X_(nu,k)`, `nu=2,3,4`.                    (3.5)

Then

`X0, X1, Y2, Y3, Y4`                                                 (3.6)

are genuinely independent source objects, and the one-dimensional product-projection theorem gives

`||p_Y2||_infinity, ||p_Y3||_infinity, ||p_Y4||_infinity <=sqrt(2)`. (3.7)

Define the three spectral aggregate coordinates

`S=sqrt(c)X0+t1X1+t2Y2+qY3-qY4`,
`T=sqrt(h)X1+sqrt(1-h)Y2`,
`V=(Y3+Y4)/sqrt(2)`.                                                  (3.8)

The partner's original null-pivot member is `2ST+V^2`.

## 4. New target-valid pivot interpolation

For every real `delta`, define

`g_delta = sqrt(1+|delta|)`                                          (4.1)

and the spectral core

`Lambda_delta = [[delta,g_delta,0],
                 [g_delta,0,0],
                 [0,0,1]]`.                                         (4.2)

Let

`Q_delta = delta S^2 + 2 g_delta S T + V^2`.                         (4.3)

### Lemma 4.1 — every member remains inside the exact QFORM target

If `delta>=0`, then the two eigenvalues of the upper-left block in (4.2) are

`delta+1` and `-1`.                                                   (4.4)

If `delta<0`, writing `d=|delta|`, they are

`1` and `-(d+1)`.                                                     (4.5)

The third eigenvalue is `1`. Hence for every `delta in R`,

`spec(Lambda_delta)` is either `{delta+1,-1,1}` or `{1,-(1+|delta|),1}`,

and therefore all three eigenvalues have modulus at least one. Because the physical frame has orthonormal columns, `A_delta=R Lambda_delta R^T` has those same three nonzero eigenvalues. Thus (4.3) is an exact-rank-three instance of the original conjecture for every real `delta`.

The normalization `g_delta^2=1+|delta|` is essential here. Keeping the cross coefficient equal to one would make one hyperbolic eigenvalue have modulus below one whenever `delta!=0`.

## 5. Projection theorem: the entire one-sheet side is uniformly paid

The matrix `Lambda_delta` has signature `(+,+,-)` for every real `delta`, with all three absolute eigenvalues at least one. Therefore the pinned ruled theorem (2.4) applies directly:

`boxed: p_(Q_delta)(s) <= pi sqrt(2),  for a.e. s>=0.`                (5.1)

This is a direct nonlinear use of the actual bounded-density projection theorem. In the partner source, the relevant planar marginal is built from the original product banks and has density cap at most two. The ruled parametrization converts the quadratic coarea integral into line integrals of that marginal, which are exactly the quantities controlled by the projection theorem.

Nothing in (5.1) says the projected coordinates are independent. The opposite/two-sheet side cannot be paid merely from the same joint cap; the live corrections rule out that shortcut. The next section keeps the source decomposition and aggregates before curvature.

## 6. Main theorem: the bank-aggregate determinant is uniform through the null pivot

### Theorem 6.1 — `QFORM-GATEFAIL-PIVOT-INTERPOLATION-v1`

For the family (3.1)--(4.3), every `m>=64`, every real `delta`, and every collection of independent original-coordinate input laws with density caps at most one,

`boxed:
 ||p_(Q_delta)||_infinity
 < 210.079333 (1+|delta|)^(-1/3)
 <=210.079333<211.`                                                   (6.1)

In particular, the bound is uniform as `delta->0`, exactly where a generic scalar-pivot half-Riesz estimate would diverge.

### Proof

Condition on the genuinely independent source objects `X1,Y4`. In the remaining independent triple

`Z=(X0,Y2,Y3)`                                                       (6.2)

write the affine parts of `(S,T,V)` as constants and their linear coefficient vectors as

`s=(sqrt(c),t2,q)^T`,
`t=(0,sqrt(1-h),0)^T`,
`v=(0,0,1/sqrt(2))^T`.                                               (6.3)

The conditional quadratic block is

`B_delta = delta s s^T
          +g_delta(s t^T+t s^T)
          +v v^T`.                                                    (6.4)

Let

`P=[s t v]`.                                                         (6.5)

Then, exactly,

`B_delta = P Lambda_delta P^T`.                                     (6.6)

The determinant therefore factors without any reciprocal small-pivot term:

`det B_delta = (det P)^2 det Lambda_delta`.                          (6.7)

From (6.3),

`det P = sqrt(c) sqrt(1-h)/sqrt(2)`,                                (6.8)

while

`det Lambda_delta = -g_delta^2 = -(1+|delta|)`.                     (6.9)

Consequently

`boxed:
 |det B_delta| = (1+|delta|) c(1-h)/2.`                              (6.10)

This is the key interpolation identity. The longitudinal leakage coefficients `t2` and `q` completely disappear from the determinant. More conceptually, adding the `delta S^2` pivot does not produce a small determinant because the companion hyperbolic coefficient has been scaled so that `det Lambda_delta=-(1+|delta|)`.

Now normalize the aggregate variables to cap-one sources:

`Z2=sqrt(2)Y2`, `Z3=sqrt(2)Y3`.                                     (6.11)

By (3.7), `X0,Z2,Z3` are independent and each has density cap at most one. The congruence from `(X0,Z2,Z3)` to `(X0,Y2,Y3)` is

`D=diag(1,1/sqrt(2),1/sqrt(2))`.                                    (6.12)

Hence the cap-one conditional block is

`B'_delta=D B_delta D`                                               (6.13)

and

`|det B'_delta|
 =(det D)^2 |det B_delta|
 =(1+|delta|) c(1-h)/8`.                                             (6.14)

The conditioning on `X1,Y4` produces only affine and constant terms in this triple, and the physical-triple determinant theorem (2.2) is uniform over arbitrary affine translations. Therefore

`||p_(Q_delta)||_infinity
 <= C3 [8/((1+|delta|)c(1-h))]^(1/3)`.                              (6.15)

Since `c>63/64` and `1-h=127/128`,

`c(1-h) > 8001/8192`,                                               (6.16)

so

`8/[c(1-h)] <65536/8001`.                                           (6.17)

Using (2.3),

`C3 (65536/8001)^(1/3)
 =210.07933258236775...`.                                            (6.18)

Substituting (6.18) into (6.15) proves (6.1). QED.

### Why the null pivot is harmless here

At `delta=0`, (6.10) reduces to the determinant used in the completed account02/B16 theorem. For nonzero `delta`, a direct scalar-square completion can create a factor `|delta|^(-1/4)` and falsely suggest a singular transition. The source-bank computation (6.6)--(6.10) shows that this is not an intrinsic singularity of this family: the full conditioned three-variable curvature stays uniformly nondegenerate through `delta=0`.

This is exactly an aggregate-before-inversion phenomenon. The partner proved that selecting one physical coordinate from each diffuse bank gives determinant of order `m^(-2)` and therefore a certificate growing like `m^(2/3)`. By contrast, the whole-bank variables `Y2,Y3` give the fixed determinant (6.14), uniformly in both `m` and `delta`.

## 7. The completed partner result applied to actual inequalities

The mandatory designated-partner application is now explicit.

At `delta=0`, Theorem 6.1 reduces to the completed account02/B16 family and reproduces its quantitative bound

`||p_(2ST+V^2)||_infinity<211`.                                     (7.1)

Therefore, for any independent random variable `W` generated by additional disjoint original coordinates,

`p_(2ST+V^2+W)=p_(2ST+V^2)*mu_W`,

so Young's inequality gives the actual higher-rank inequality

`boxed:
 ||p_(2ST+V^2+W)||_infinity<211.`                                   (7.2)

For example, for arbitrary independent cap-one `Z_1,...,Z_N` and arbitrary symmetric `C`, taking

`W=Z^T C Z`                                                         (7.3)

gives (7.2) with no sign, rank, or dimension restriction on `C`. The block-direct-sum coefficient matrix retains the partner's three eigenvalues `{1,-1,1}` and is therefore a genuine arbitrary-rank QFORM target family.

The new theorem strengthens this endpoint application to the entire target-valid pivot deformation:

`boxed:
 ||p_(delta S^2+2sqrt(1+|delta|)ST+V^2+W)||_infinity
 <210.079333(1+|delta|)^(-1/3)`                                     (7.4)

for every `delta in R` and every independent additive block `W`.

There is also a non-block-diagonal extension that still preserves the aggregation. Let `Z_out` be a disjoint independent outside vector and let `G` be any deterministic matrix coupling `Z_out` only to the three aggregate coordinates `(S,T,V)`. For

`Q_ext = Q_delta
       +2 Z_out^T G (S,T,V)^T
       +Z_out^T C Z_out`,                                           (7.5)

condition first on `Z_out` and then on `X1,Y4`. The cross term becomes an arbitrary affine term in the same cap-one triple `(X0,sqrt(2)Y2,sqrt(2)Y3)`, while the quadratic block remains exactly `B'_delta`. Hence the same physical-triple theorem gives

`boxed:
 ||p_(Q_ext)||_infinity
 <210.079333(1+|delta|)^(-1/3).`                                    (7.6)

The gate-family physical matrix is a principal block of the enlarged symmetric matrix. Since it has two eigenvalues at least `+1` and one at most `-1`, Cauchy interlacing guarantees that the enlarged cross-coupled matrix still has at least three eigenvalues of modulus at least one. Thus (7.6), not only (7.4), is a non-block-diagonal higher-dimensional target-valid family.

The restriction in (7.5) is important: arbitrary outside couplings to individual coordinates inside a diffuse bank need not factor through `(S,T,V)` and can destroy the exact bank compression. This report does not claim such couplings are covered.

## 8. Exact relation to the projection-product assignment

The result separates two legitimate uses of projection information.

1. **Ruled side.** The two-dimensional product-projection density cap is directly matched to the line rulings of the one-sheet hyperboloid, giving (5.1). Dependence inside the projected pair is harmless because the geometry asks only for a marginal line integral.

2. **Global/two-sheet side.** A bare joint projection cap is insufficient. Instead, the disjoint original source banks are aggregated first, normalized to cap-one scalar variables, and then the full three-variable nonlinear curvature is paid by the determinant theorem. The exact determinant (6.14) remains nondegenerate through the null pivot.

This is the source-valid interaction requested by B16: bounded projection density is used only where the level geometry genuinely matches it; elsewhere product provenance is retained until after the nonlinear integration.

## 9. Remaining gap to the full theorem

`QFORM-GATEFAIL-PIVOT-INTERPOLATION-v1` is a real target-valid extension of the latest partner family, but it does **not** prove the universal conjecture. The still-unpaid structural implication is

`QFORM-TRUE-NEAR-COLOOP-BANK-COMPILER-v2`:

> From an arbitrary surviving exact-rank-three near-coloop frame with `c>63/64`, prove that the residual original-coordinate rows can be compiled either into a bounded number of aggregate banks whose conditioned three-variable determinant is uniformly nondegenerate, or into one of the already-paid source-first same-bank / Fresnel / volume branches. Then connect that exact-rank-three compiler to arbitrary extra spectrum without losing product provenance.

The theorem here proves that **once** the two-bank aggregate geometry of the partner family is available, the full scalar-pivot interpolation is no longer a problem: the determinant currency is uniform at, near, and away from zero. What remains is to force such an aggregate geometry in every surviving frame, not to repair the null pivot inside this family.

Global continuity also remains open. The physical-triple determinant theorem used for the global estimate establishes essential boundedness but does not by itself supply a continuous representative. The one-sheet estimate (5.1) should therefore be recorded separately from any global regularity claim.

## 10. Algebra checks and constants

The two exact identities on which the new result depends are

`det Lambda_delta=-(1+|delta|)`                                      (10.1)

and

`(det P)^2=c(1-h)/2`.                                                (10.2)

They imply (6.10) immediately. The numerical constant in (6.18) is

`16 sqrt(30) 2^(1/4) (65536/8001)^(1/3)
 =210.07933258236775...`.                                            (10.3)

No numerical experiment is used as proof.

## 11. Source ledger

Fresh control before publication: `yspennstate/math-research-brain@4e181f930f8bfea18bceb4e0f09603669de52dea`, OWNER CONTROL revision `2026-09-22.15`.

Completed designated partner: `math-open-problems@7dc1a1fb738f263d7fe021dcf3ce5c37223ced4e`.

Physical-triple determinant theorem: `math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`.

Product-projection / ruled theorem: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Fresh same-bank discriminant theorem used as context: `math-open-problems@71c369d883ef5211a624f1e943e53dcfbcc3dcdd`.

Full QFORM status: `OPEN / NOT PROVED / NOT DISPROVED`.  
New theorem status: `PROVED SUPPORTING TARGET-VALID FAMILY`.  
Independent end-to-end review of this new theorem: `NOT YET COMPLETED`.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.
