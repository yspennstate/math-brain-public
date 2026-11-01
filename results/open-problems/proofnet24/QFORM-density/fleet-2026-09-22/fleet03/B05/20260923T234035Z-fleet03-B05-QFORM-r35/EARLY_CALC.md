SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-23T23:40:35Z.
attacking: QFORM-SCALAR-HEAVY-PIVOT-CROSSING-v1 — use one literal heavy scalar source coordinate, the other scalar bank, and an asymmetric Pluecker split of the first product-projection bank to retain a rank-three crossing.

# Early calculation

In the r34 ratio packet write

`H=[[C,P],[P^T,B]]`, `C-PB^{-1}P^T=lambda m e1 e1^T`, `mu=|det B||lambda|`,
`A=B^{-1}P^T`, and let the first-bank Parseval rows be `g_i=(xi_i,rho_i)`.
For a first-bank subset with Gram `G`, put `s=e1^T G e1` and `d=det G`. If the Y/Z source coefficient masses on the same side are `y2,z2`, the Schur-factor Gram from r34 satisfies the exact identity

`det F = s*y2*z2 + d*(A22^2*y2 + A12^2*z2)`.                 (E1)

This follows by Cauchy-Binet: one-first+Y+Z triples contribute `s y2 z2`, two-first+Y triples contribute `A22^2 d y2`, and two-first+Z triples contribute `A12^2 d z2`.

There is also an asymmetric first-bank split. If `q_xi=max_i xi_i^2`, a Bernoulli half split I/J obeys

`E[(sum_{i in I}xi_i^2) det G_J]
 = (1/8) sum_{j<k} det(g_j,g_k)^2 (1-xi_j^2-xi_k^2)
 >= (1-2q_xi)/8`.

Hence if `q_xi<1/4` some split has

`(sum_{i in I}xi_i^2) det G_J >= 1/16`.                       (E2)

Let `q_Y=max eta_j^2`, choose a literal Y coordinate attaining q_Y and put it on the left, put all other Y coordinates on the right, and split the Z source bank so that `z_L z_R >= (1/2)sqrt(1-q_Z)`. Combining (E1)-(E2) gives for the physical rank-three crossing volume

`Delta >= (mu*m/8) * sqrt(q_Y(1-q_Z))
                   * sqrt(A12^2 + A22^2(1-q_Y)).`             (E3)

The symmetric Z-pivot formula is

`Delta >= (mu*m/8) * sqrt(q_Z(1-q_Y))
                   * sqrt(A22^2 + A12^2(1-q_Z)).`             (E4)

Whenever either right-hand side is positive, the determinant-sensitive exact-cross theorem gives a bounded continuous density via `||p_Q||_inf <= 6 Delta^(-1/3)`.

Complementary first-bank branch: if `q_xi>=1/4`, then one literal first-bank coordinate has exact-slope mass at least `m/4`; the designated fleet04/B05 theorem gives

`||p_Q||_inf < 51.6 (mu*m/4)^(-1/3)`.

For the standard ratio packet `m>=3/20`, this is `<154.17 mu^(-1/3)`.

This is a scoped branch theorem, not a full QFORM solution. The remaining scalar-heavy endpoint includes simultaneous collapse of the two currencies in (E3)-(E4), in particular near-literal Y and Z carriers with the corresponding Schur-factor cross couplings small.
