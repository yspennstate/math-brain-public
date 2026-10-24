# r15 addendum — cross-pair stability forces one residual planar atom

**Parent report:** `REPORT.md` in this run.  
**Classification:** `ESSENTIAL_STEP_APPLIED / STRICT STRENGTHENING / FULL QFORM OPEN`.

This addendum pushes the account02/B13 pair-incidence mechanism one step further. It proves that the `1/2` planar-concentration threshold in the partner report is not the asymptotic endpoint: when the two normalized residual planar directions align and the transverse direction is diffuse, small disjoint Pluecker mass forces **one original residual coordinate to carry asymptotically all planar energy**.

## 1. Setup from the assigned partner

Use the notation of the completed assigned-partner result

`yspennstate/math-open-problems@93bed74b07afe996a4aa08eaeb88f35060653134`.

Thus `x,y,z` are unit vectors in the residual coordinate space, with

`x perpendicular z`, `y perpendicular z`,

where `x=b/sqrt(B)`, `y=u/sqrt(U)`, and

`d=max_k z_k^2=d_*`.

For unordered residual pairs `e={k,l}`, define the normalized rank-two Pluecker laws

`P_e=(x_k z_l-z_k x_l)^2`,

`Q_e=(y_k z_l-z_k y_l)^2`.

Because each pair `(x,z)` and `(y,z)` is orthonormal,

`sum_e P_e=sum_e Q_e=1`.

The partner's unnormalized pair measures are `p_e=alpha P_e` and `q_e=beta Q_e`, and if

`delta_cross=sum_{e cap f=empty} P_e Q_f`,

then its cross-incidence mass `M` is `M=alpha beta delta_cross`. Since the partner proves `D0>=2M`,

`delta_cross <= D0/(2 alpha beta)`.                         (1.1)

After choosing the harmless global sign of `y` so `<x,y>>=0`, the partner also proves

`||x-y||_2^2 <= 2 theta`,

where

`theta=h Delta/(B beta)`.                                  (1.2)

## 2. Total-variation stability of the two Pluecker laws

Let the exterior-coordinate amplitudes be

`xi_e=(x wedge z)_e`, `eta_e=(y wedge z)_e`.

Then `P_e=xi_e^2`, `Q_e=eta_e^2`, and

`||xi||_2=||eta||_2=1`.

Moreover, since `(x-y) perpendicular z`,

`||xi-eta||_2=||(x-y) wedge z||_2=||x-y||_2`.

Therefore

`sum_e |P_e-Q_e|`
` <= ||xi-eta||_2 ||xi+eta||_2`
` <=2||x-y||_2`,

so

`boxed(||P-Q||_TV <= ||x-y||_2 <= sqrt(2 theta))`.          (2.1)

This step uses the common source coordinates of the two pair laws; no post-rotation independence or density approximation is involved.

## 3. Self-disjoint probability and rank-two leverage

Let

`delta_P=sum_{e cap f=empty} P_e P_f`.

For the rank-two Parseval frame with rows `(x_k,z_k)`, the exact one-coordinate basis-incidence identity is

`sum_{e: k in e} P_e = x_k^2+z_k^2=:p_k`.                  (3.1)

It follows either by the same row-scaling/Cauchy--Binet proof as in the parent report or directly from the two-vector Lagrange identity.

Two independent `P`-edges are disjoint unless they collide at a vertex. Hence the union bound gives

`delta_P >=1-sum_k p_k^2`.                                  (3.2)

Put

`m=max_k x_k^2`.

Because `max z_k^2=d`,

`sum_k p_k^2`
` =sum_k x_k^4+2sum_k x_k^2 z_k^2+sum_k z_k^4`
` <=m+2d+d`
` =m+3d`.                                                    (3.3)

Consequently

`boxed(delta_P >=1-m-3d)`.                                  (3.4)

## 4. Cross-to-self transfer

For a fixed second edge `f`, define

`F(f)=sum_{e: e cap f=empty}P_e`,

so `0<=F<=1`. Then

`delta_P=E_P F`, `delta_cross=E_Q F`.

By (2.1),

`delta_P <= delta_cross+||P-Q||_TV`
` <= D0/(2 alpha beta)+sqrt(2 theta)`.                       (4.1)

Combining (3.4) and (4.1) proves the main quantitative statement:

### Theorem `QFORM-RESIDUAL-PAIR-DPP-STABILITY-v1`

`boxed(max_k x_k^2`
` >=1-3d_*-D0/(2 alpha beta)-sqrt(2 theta))`,                (4.2)

with `theta=h Delta/(B beta)`.

In particular, whenever `d_*->0`, `D0/(alpha beta)->0`, and `theta->0`,

`boxed(max_k x_k^2 ->1)`.                                   (4.3)

Because `||x-y||_2->0`, the same maximizing coordinate also satisfies `y_k^2->1`; because `z_k^2<=d_*`, it has `z_k^2->0`.

This is much stronger than the earlier consequence `max x_k^2>=1/2-o(1)`.

## 5. Explicit strengthening in the non-boundary chamber

Retain the parent report's fixed `eta` hypotheses

`1/2<c,h<=1-eta`,

`d_*<=1/16`, `D0<=eta^2/64`, `Delta<=eta^2/256`.

As proved there,

`alpha beta>=eta^2/4`,

`theta<=1/128`.

Thus (4.2) gives

`max_k x_k^2 >=1-3/16-1/32-1/8=21/32`.                     (5.1)

Choose `k` attaining this maximum. Since `B>=eta`,

`boxed(b_k^2=B x_k^2 >=21 eta/32)`.                         (5.2)

Also `||x-y||_2<=1/8`, so

`|y_k|>=sqrt(21/32)-1/8`,

and

`y_k^2 >= (sqrt(21/32)-1/8)^2`
`       =(sqrt(42)-1)^2/64`
`       >7/16`.                                             (5.3)

Since `U=beta/s>=eta/2`,

`boxed(u_k^2>7 eta/32)`.                                    (5.4)

Finally `z_k^2<=d_*<=1/16`. Hence the same single residual physical coordinate carries a macroscopic fraction of both surviving planar coefficient vectors while remaining transverse-small.

Its leverage satisfies

`ell_k>=b_k^2>=21 eta/32`.                                  (5.5)

Using the universal half-Riesz/Schur pivot estimate from `account03/B05@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`, the determinant-normalized physical pivot therefore obeys

`|A_kk| |det Lambda|`
` <= [32/(21 eta)] 2^19 M^(-4)`
` < 2^20/(eta M^4)`,                                       (5.6)

where `M=||p_Q||_infinity`.

## 6. Asymptotic source geometry becomes an approximate four-bank frame

Assume now a putative unbounded nested-heavy sequence stays away from the leverage-one boundary, so some fixed `eta>0` works after passing to a subsequence. The completed dependencies imply

`d_*->0`, `D0->0`, `Delta->0`,

while `alpha beta` stays bounded below. By (4.3), choose `k` with

`x_k^2->1`, `y_k^2->1`, `z_k^2->0`.                        (6.1)

Thus

`sum_{l!=k} b_l^2=B(1-x_k^2)->0`,                           (6.2)

and, because `U<=1`,

`sum_{l!=k} u_l^2=U(1-y_k^2)->0`.                           (6.3)

The original first planar residual coefficients satisfy

`a_l=(sqrt(s)u_l+rho b_l)/sqrt(h)`.

Since `h>1/2`, `s<=1`, and `rho^2<=1`, (6.2)--(6.3) imply

`sum_{l!=k} a_l^2->0`.                                      (6.4)

At the same time

`sum_l z_l^2=1`, `max_l z_l^2->0`, and `z_k^2->0`.          (6.5)

Therefore the residual spectral frame asymptotically splits, in the original-coordinate coefficient geometry, into:

- one physical row `k` carrying essentially all residual heavy-plane energy; and
- a high-cardinality bank of the remaining original coordinates carrying essentially all transverse `e3` energy and vanishing total planar energy.

Together with the two original heavy rows `i,j`, the only possible non-boundary unbounded rank-three sequence is therefore an **approximate four-bank geometry**: three concentrated physical planar rows plus one diffuse transverse bank. This conclusion is coefficient-space structural; it does not perturb the random variables or assume moments, so it is compatible with the live no-bounded-support corrections.

## 7. New unpaid implication

The first remaining rank-three implication is sharpened again:

> **`QFORM-RANK3-ROBUST-FOUR-BANK-CLOSURE-v1` (OPEN).** Starting from three original physical rows carrying asymptotically all heavy-plane coefficient energy and a disjoint residual coordinate bank carrying asymptotically all transverse coefficient energy, prove a density bound uniform under the vanishing planar leakage of that residual bank and the vanishing transverse leakage of the third physical row, without perturbing `X^TAX` in value and without any moment/support assumptions.

The exact zero-leakage four-bank limit is already covered by the finite-projective-bank theorem. The unresolved point is a **source-valid robustification** of that aggregation theorem. A raw small operator-norm perturbation of `A` is not sufficient because the input laws have no moment bounds. The appropriate next mechanism should absorb the leakage inside a regularized determinant, half-Riesz, or hyperbolic-square inequality before evaluating the quadratic form.

Full QFORM remains OPEN, and arbitrary additional spectrum remains a separate debt after rank three.
