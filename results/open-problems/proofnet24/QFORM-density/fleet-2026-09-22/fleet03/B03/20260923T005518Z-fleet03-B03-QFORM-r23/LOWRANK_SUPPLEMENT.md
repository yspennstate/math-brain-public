# QFORM-HUB-LOWRANK-SCREEN-AMBIGUITY-v1

## Status

**SUPPORTING THEOREM PROVED / STRICT EXTENSION OF THE RANK-ONE REPORT / FULL QFORM OPEN.**

The main r23 report proves the rank-one screen case.  The same dependence-safe argument closes every finite screen rank `r>=1` with a clean invariant and better decay as `r` grows.  The point is that the rank-one proof never used one-dimensionality except in the physical projection caps; the Ball/Livshyts--Paouris--Pivovarov bounds scale exactly in the required way.

## 1. Statement

Keep the original-coordinate split

`{h} disjoint_union I disjoint_union J_V disjoint_union J_L disjoint_union K`,

condition on `K`, and write `w=(A_hj)_{j!=h}`, `a=A_hh`.

Assume

`A[I,J_L] = U V^T`,

where `U` is `|I| x r`, `V` is `|J_L| x r`, both have rank `r>=1`.  No restriction is placed on the other cross block `A[I,J_V]` or on any self block or affine term.

Define

`P_I=[w_I,U]`,           `G_I=P_I^T P_I`,

`G_V=V^T V`,

`P_J=[V,w_{J_L}]`,       `G_J=P_J^T P_J`.

Assume `G_I,G_J` are invertible and every physical row of `P_I` has leverage at most `1/2`:

`(P_I)_{i,*} G_I^{-1} (P_I)_{i,*}^T <= 1/2` for every `i in I`.

Set the factorization-invariant certificate

`Xi_r := det(G_I)^2 det(G_V) det(G_J)`.                              (1.1)

Then, for every nonzero `t`,

`boxed(
 |phi_Q(t)|^2
 <= 2^((6r+5)/4) pi^(r+3/2)
    Xi_r^(-1/4) |t|^(-(r+3/2))
 )`.                                                                  (1.2)

Consequently, with

`theta_r = 1/[2(2r+3)]`,

`boxed(
 ||p_Q||_infinity
 <= C_r Xi_r^(-theta_r),
 C_r = [(2r+3)/(2r-1)] 2^((6r+5)/(2(2r+3)))
 )`.                                                                  (1.3)

The characteristic function is in `L^1`, so this branch has a **continuous density vanishing at infinity**.  In particular every interval `B` obeys

`P(Q in B) <= C_r Xi_r^(-theta_r) |B|`.                              (1.4)

For `r=1`, (1.3) is exactly the main-report constant

`C_1=5*2^(11/10)=10.7177346253...`.

For `r=2`,

`C_2=(7/3)2^(17/14)=5.4139371354...`.

Thus the same mechanism becomes stronger, rather than weaker, on a genuinely rank-two physical screen.

## 2. Exact independent-copy input

Use Proposition 4.1 of

`yspennstate/math-open-problems@f68817886312b904e2cf86ccbfb14f4f130229f3:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`.

For the duplicated `J_0=J_V union J_L` coordinates put `W=X-X'`; its coordinates remain independent probability densities bounded by one.  For the hub difference `sigma=X_h-X_h'`, the source ambiguity function satisfies

`int_R |Fhat_sigma(s)|^2 ds <= 2 pi g_h(sigma) <= 2 pi`.             (2.1)

The exact source inequality is

`|phi_Q(t)|^2
 <= int d sigma E_W [
      |Psi_I(2t( sigma w_I + A[I,J_V]W_V + U V^T W_L ))|
      |Fhat_sigma(2t(<w_{J_V},W_V>+<w_{J_L},W_L>+a sigma))|
    ]`.                                                               (2.2)

No independence between a sum and difference of the same original coordinate is used.  All such dependence remains inside `Fhat_sigma`.

## 3. Joint physical projection estimate

Put

`Z=V^T W_L in R^r`,       `Y=<w_{J_L},W_L> in R`.

Because `W_L` has independent cap-one coordinates, the projection theorem used in the source report gives

`||p_Z||_infinity <= 2^(r/2) det(G_V)^(-1/2)`,                      (3.1)

and

`||p_(Z,Y)||_infinity <= 2^((r+1)/2) det(G_J)^(-1/2)`.              (3.2)

Fix `sigma,W_V,z`.  Cauchy--Schwarz in the **actual joint density** `p(z,y)` gives

`int p(z,y)|Fhat_sigma(2t(y+C))|dy
 <= p_Z(z)^(1/2)
    [int p(z,y)|Fhat_sigma(2t(y+C))|^2dy]^(1/2)`.

By (3.2), `s=2t(y+C)`, and (2.1),

`int p(z,y)|Fhat_sigma(2t(y+C))|^2dy
 <= 2^((r+1)/2) det(G_J)^(-1/2)
    * [1/(2|t|)] * [2pi g_h(sigma)]`.

Using (3.1) and `g_h<=1`,

`int p(z,y)|Fhat_sigma(2t(y+C))|dy
 <= 2^((2r+1)/4) pi^(1/2) |t|^(-1/2)
    det(G_V)^(-1/4) det(G_J)^(-1/4)`.                               (3.3)

This step is the multi-dimensional version of the rank-one screen estimate.  It never forms or bounds a conditional density `p_(Y|Z)`, so the live conditional-cap counterexample is irrelevant.

## 4. Translated `(r+1)`-dimensional Brascamp--Lieb integral

After (3.3), the remaining nonnegative integral is

`int d sigma int_R^r dz E_{W_V}
 |Psi_I(2t( sigma w_I + U z + A[I,J_V]W_V ))|`.

For each fixed `W_V`, `A[I,J_V]W_V` is only a translation of the scalar arguments.  The source translated Brascamp--Lieb theorem applied to the `(r+1)` columns `P_I=[w_I,U]` gives

`int_R^(r+1) |Psi_I(P_I xi + beta)| dxi
 <= (4pi)^(r+1) det(G_I)^(-1/2)`                                   (4.1)

uniformly in `beta`, because every row leverage is at most `1/2`.

Scaling `xi=2t(sigma,z)` yields

`int d sigma dz E_{W_V}|Psi_I(...)|
 <= (2|t|)^(-(r+1))(4pi)^(r+1)det(G_I)^(-1/2)`.                    (4.2)

Multiplying (3.3) and (4.2) proves (1.2), since

`2^(r+1) * 2^((2r+1)/4) = 2^((6r+5)/4)`

and

`det(G_I)^(-1/2)det(G_V)^(-1/4)det(G_J)^(-1/4)=Xi_r^(-1/4)`.

## 5. Fourier inversion

Taking square roots in (1.2),

`|phi_Q(t)| <= min(1,B_r |t|^(-b_r))`,

where

`b_r=(2r+3)/4 > 1`,

`B_r=2^((6r+5)/8) pi^((2r+3)/4) Xi_r^(-1/8)`.

For every `b>1`,

`int_R min(1,B|t|^-b)dt = [2b/(b-1)]B^(1/b)`.

Here `pi^((2r+3)/4)` becomes exactly one factor of `pi` after the `1/b_r` power, which cancels Fourier inversion.  Therefore

`||p_Q||_infinity
 <= [(2r+3)/(2r-1)]
    2^((6r+5)/(2(2r+3)))
    Xi_r^(-1/[2(2r+3)])`,

which is (1.3).

## 6. Factorization invariance

The rank-r factorization is nonunique.  For any invertible `S in GL(r)`, replace

`U -> U S`,       `V -> V S^(-T)`.

Then

`det G_I -> det(S)^2 det G_I`,

`det G_V -> det(S)^(-2) det G_V`,

`det G_J -> det(S)^(-2) det G_J`.

Thus `Xi_r=(det G_I)^2 det G_V det G_J` is unchanged.  The theorem depends on the physical rank-r screen, not on a chosen factorization.

## 7. L2 collision bound and designated partner

From (1.2), with `beta=r+3/2=(2r+3)/2`,

`int_R |phi_Q(t)|^2dt
 <= [2 beta/(beta-1)] C_2^(1/beta)`,

where `C_2` is the coefficient in (1.2).  Plancherel simplifies this to

`boxed(
 ||p_Q||_2^2
 <= L_r Xi_r^(-theta_r),
 L_r=[(2r+3)/(2r+1)]2^((6r+5)/(2(2r+3)))
 )`.                                                                  (7.1)

Apply the valid fleet04/B03 partner lemma

`P(|Y-Y'|<=epsilon)<=2epsilon||p_Y||_2^2`

from

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

This gives the actual new rank-r collision inequality

`boxed(
 P(|Q-Q'|<=epsilon)
 <= 2 L_r Xi_r^(-theta_r) epsilon
 )`.                                                                  (7.2)

Only this valid partner lemma is used; the partner report's refuted weighted-L2 compiler is not revived.

## 8. Relation to the remaining full-target gap

The theorem materially enlarges the r23 main report: the physical screen need not have rank one.  In particular a rank-two screen closes with one-copy decay `|phi(t)|=O(|t|^(-7/4))` and explicit constant `C_2=5.413937...` times the invariant power.

This is directly aimed at the current strict-N3/hub remainder, where fresh work shows that rank-three/five cross-volume certificates can vanish and that an aggregate bordered packet can survive while local triples become tiny.  The theorem does **not** prove that every such packet yields a screen factorization with both augmented Gram determinants and the shared-side leverage gate uniformly controlled.  Establishing that deterministic routing, or replacing the leverage gate by an aggregate volume marginal, is the next unpaid implication.

Full QFORM remains OPEN.  Continuity is proved in this theorem's stated low-rank-screen branch only.
