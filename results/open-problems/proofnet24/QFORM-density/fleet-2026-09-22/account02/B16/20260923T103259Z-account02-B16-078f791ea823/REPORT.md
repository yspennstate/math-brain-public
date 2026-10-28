SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T10:32:59Z.
attacking: near-coloop fresh-square versus shared-bank geometry—aggregate a whole disjoint source bank before the curved pushforward and compare it quantitatively with every single-coordinate fresh-square certificate.

# account02/B16 — bank-aggregated fresh square inside the strict no-pivot near-coloop chamber

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Projection-product interaction / complementary constructions and source-valid counterexamples  
**Run:** `20260923T103259Z-account02-B16-078f791ea823`  
**Status:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Regularity:** absolute continuity and an essential `L^infinity` bound are proved for the family below; continuity is not claimed.

## 1. First unpaid implication

The exact-rank-three near-coloop debt is now more precise:

`QFORM-NEAR-COLOOP-FRESH-BANK-OR-SHARED-BANK-v1`.

A proof cannot require a single original coordinate carrying a fresh square with quantitative `|b det B|`. The family below lies arbitrarily deep in the chamber where every physical diagonal and every physical `2 x 2` principal determinant is tiny, and every individual fresh-square certificate from the completed account03/B16 sign-free theorem deteriorates like `m^(3/4)`. Nevertheless, aggregating one entire **disjoint original-coordinate rank-one bank** into a scalar projection gives a uniform density bound `4`.

Thus the structural compiler still has to prove one of two things for a general near-coloop frame: either extract a disjoint rank-one source bank whose aggregate scalar supplies quantitative fresh-square curvature, or handle the genuinely shared-bank endpoint where no such exact bank exists. The arbitrary-higher-rank extension remains separate.

## 2. Source construction

Let `m` be divisible by `4`. Partition `{1,...,m}` into four equal classes and choose signs `eps_j,tau_j in {+1,-1}` so that each pair

`(eps_j,tau_j)=(+,+),(+,-),(-,+),(-,-)`

occurs exactly `m/4` times. Hence

`sum eps_j = sum tau_j = sum eps_j tau_j = 0`.

Let

`X_0, X_1,...,X_m, Z_1,...,Z_m`

be arbitrary independent real random variables whose densities are bounded by `1`. Define the three normalized projections of the first leaf bank

`L = m^(-1/2) sum_j X_j`,
`U = m^(-1/2) sum_j eps_j X_j`,
`T = m^(-1/2) sum_j tau_j X_j`,

and the disjoint fresh-bank projection

`V = m^(-1/2) sum_j Z_j`.

Fix parameters

`0 <= rho <= 1`,
`eta > 0`,
`eta^2(1+rho^2) < 1/63`,
`0 < delta <= 1/16`,

and put

`H = eta(L+rho T)`,
`Y = X_0 + H`.

Finally set

`Q = 4 delta Y^2 + 8 Y U + 4 V^2`.                         (2.1)

The source objects

`X_0`, `(H,U)`, `V`

are mutually independent because they use three disjoint original-coordinate banks. No independence between `H` and `U` is assumed or needed.

## 3. Projection-product interface

The coefficient vectors of `L,U,T` are orthonormal. Consequently the one-dimensional bounded-density projection theorem gives

`||p_U||_infinity <= sqrt(2)`,
`||p_V||_infinity <= sqrt(2)`.                               (3.1)

The required pinned continuation source at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

also records the checked two-dimensional product-marginal theorem used in its ruled-hyperboloid argument. Applying it here to

`W := H/(eta sqrt(1+rho^2))`

and `U` gives

`||p_(W,U)||_infinity <= 2`,                                  (3.2)

because the coefficient vectors of `W` and `U` are orthonormal. Equivalently,

`||p_(H,U)||_infinity <= 2/(eta sqrt(1+rho^2))`.              (3.3)

Equation (3.2) is a genuine two-dimensional marginal statement, not projected independence. The curved argument below does not factor `p_(H,U)`; it keeps the pair dependent and uses only the unconditional one-dimensional marginal of `U` plus the original source-bank independence.

## 4. Designated partner theorem gives a uniform curved bound

Write (2.1) as

`Q = (Y,U,V)^T B_delta (Y,U,V)`,

where

`B_delta = 4 [[delta,1,0],[1,0,0],[0,0,1]]`.                 (4.1)

The latest completed designated partner result account03/B16 r27, theorem

`QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SIGNFREE-v1`,

allows `(H,U)` to be arbitrarily dependent while `X_0`, `(H,U)`, and `V` are mutually independent. It gives

`||p_Q||_infinity
 <= 2^(13/4) L_V sqrt(L_X L_U/|gamma|)
    (|b det B_delta|)^(-1/4)`.                                (4.2)

Here

`L_X=1`, `L_U<=sqrt(2)`, `L_V<=sqrt(2)`, `gamma=1`,
`b=4`, `det B_delta=-64`,

so `|b det B_delta|=256` and (4.2) simplifies exactly to

`boxed: ||p_Q||_infinity <= 4`.                               (4.3)

This proves absolute continuity and a dimension-free essential density bound for the whole family, uniformly in `m,eta,rho,delta` in the stated range. No conditional projection-density cap or post-rotation independence appears.

## 5. The family is genuinely in the three-large-eigenvalue target class

Let `y,u,v` be the physical coefficient vectors of `Y,U,V`. They are pairwise orthogonal and

`||y||^2 = s^2 := 1+eta^2(1+rho^2) < 64/63`,
`||u||=||v||=1`.                                               (5.1)

Therefore the nonzero spectrum of the physical quadratic matrix is the spectrum of

`4 [[delta s^2,s,0],[s,0,0],[0,0,1]]`.                       (5.2)

The third eigenvalue is `4`. If `lambda_+>0>lambda_-` are the two eigenvalues of

`[[delta s^2,s],[s,0]]`,

then

`lambda_+ >= s >=1`,
`|lambda_-| = s^2/lambda_+`.

Using

`sqrt(delta^2 s^4+4s^2) <= delta s^2+2s`

gives

`lambda_+ <= s+delta s^2`,
`|lambda_-| >= s/(1+delta s)`.

Hence

`4 lambda_+ >=4`,
`4|lambda_-| >= 4s/(1+delta s) > 1`.                          (5.3)

Thus all three nonzero eigenvalues have modulus at least `1` (in fact much larger).

The physical hub coordinate `X_0` has leverage

`c = 1/s^2 > 63/64`.                                          (5.4)

So this lies in the genuine near-coloop collar left by the exact-rank-three reductions.

## 6. It can lie arbitrarily deep in the physical no-pivot chamber

For a shared-bank coordinate `j`, write

`h_j = eta(1+rho tau_j)/sqrt(m)`,
`u_j = eps_j/sqrt(m)`.

For a fresh-bank coordinate `k`, its `V` coefficient is `v_k=1/sqrt(m)`. Relative to the aggregate coordinates `(Y,U,V)`, the source rows are

`q_0=(1,0,0)`,
`q_j=(h_j,u_j,0)`,
`q_k=(0,0,v_k)`.

Since physical coefficients are `A_ab=q_a^T B_delta q_b`, one gets

`A_00 = 4 delta`,                                              (6.1)

`A_jj = 4 delta h_j^2 + 8 h_j u_j`,                           (6.2)

`A_kk = 4/m`.                                                  (6.3)

Under the parameter restrictions,

`|A_jj| < 3/m`.                                                (6.4)

The principal pair determinants are equally explicit. For hub/shared,

`det A_{0j} = (4delta)(4delta h_j^2+8h_ju_j)
              -(4delta h_j+4u_j)^2
            = -16 u_j^2
            = -16/m`.                                         (6.5)

For hub/fresh,

`|det A_{0k}|=16 delta/m`.                                    (6.6)

For two shared rows,

`det A_{j ell}
 = -16(h_j u_ell-u_j h_ell)^2`,                               (6.7)

so

`|det A_{j ell}| <= 256 eta^2/m^2 < 5/m^2`.                   (6.8)

For shared/fresh,

`|det A_{jk}| = |A_jj| 4/m < 12/m^2`,                         (6.9)

and fresh/fresh determinants vanish.

Consequently

`max_i |A_ii| <= max(4delta,4/m)`,
`max_{i<j} |det A_{ij}| <= 16/m`.                              (6.10)

For every threshold `tau_*>0`, choose

`delta < min(1/16,tau_*/4)`

and then choose a sufficiently large multiple of four with `m>16/tau_*`. All physical diagonals and all physical `2 x 2` principal determinants then have modulus `<tau_*`, while (5.3) still supplies three eigenvalues of modulus at least one and (4.3) still gives `||p_Q||_infinity<=4`.

This is therefore a strict target-valid family arbitrarily deep in the no-scalar/no-pair-pivot region.

## 7. Why aggregation has to precede the curved payment

Take one shared coordinate `j` and one fresh coordinate `k`. The exact principal-triple determinant is

`det A_{0jk}
 = det(B_delta) det[q_0;q_j;q_k]^2
 = -64/m^2`,                                                   (7.1)

because `|u_j|=|v_k|=m^(-1/2)`. Together with `A_kk=4/m`,

`|A_kk det A_{0jk}| = 256/m^3`.                               (7.2)

If one conditions on all other original coordinates and applies the same completed account03/B16 sign-free theorem to this single physical triple, all three remaining source densities have cap one and the certificate is

`2^(13/4) (256/m^3)^(-1/4)
 = 2^(5/4) m^(3/4)`,                                          (7.3)

which diverges.

By contrast, aggregating the **whole fresh original-coordinate bank first** gives the normalized scalar `V` with density cap `sqrt(2)`, turns its quadratic coefficient from `4/m` into `4`, retains independence from the dependent shared-bank pair `(H,U)`, and yields the dimension-free value `4` in (4.3).

Thus the local atom certificate loses a factor of order `m^(3/4)` on a family whose true source-valid certificate is constant. This is an explicit aggregation-before-curvature phenomenon, not a counterexample to the QFORM conjecture.

## 8. Relation to the previous B16 obstruction

The first leaf bank contains three overlapping orthogonal projections `L,U,T`. The previous account02/B16 run showed that adding an arbitrarily weak same-bank transverse coordinate can make a proposed slice-Wiener norm infinite even while the relevant two-dimensional product marginal remains bounded. The present family shows the positive complementary fact: once a disjoint rank-one source bank supplies the fresh square, the completed partner transducer carries an arbitrarily dependent `(H,U)` pair through the curved integral with a uniform constant. No conditional height of `U|H` and no slice-Wiener norm is needed.

The remaining structural debt is therefore not an analytic Schur-sign problem and not a two-dimensional marginal theorem. It is to produce a suitable disjoint rank-one bank from a general near-coloop frame, or replace it by a genuinely shared-bank source-first transducer.

## 9. Source pins and scope


Required pinned continuation source actually used:
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially the checked product-marginal theorem behind its ruled-hyperboloid argument.

Designated partner actually used:
account03/B16 r27,
`yspennstate/math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`,
theorem `QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SIGNFREE-v1`.

**Full target change: none.** The unrestricted QFORM theorem and global continuity remain open. The present result is a quantitative supporting theorem and a source-valid obstruction to any compiler that insists on paying fresh-square curvature one physical coordinate at a time.
