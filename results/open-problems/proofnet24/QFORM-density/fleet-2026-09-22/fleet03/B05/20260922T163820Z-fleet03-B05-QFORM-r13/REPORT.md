# fleet03/B05 — base-packing endpoint and coloop coarea closure

**Run:** `20260922T163820Z-fleet03-B05-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.6` at `yspennstate/math-research-brain@144f57f486c0d7caf6356876dbc4ea62686e44cf`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW ENDPOINT CLASSIFICATION + TWO COAREA CLOSURES / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and mechanism change

The sole target is the full owner conjecture: for every dimension, independent real physical coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential density of `Q=X^TAX`, or give a target-valid counterexample. The separate continuity request remains distinct.

The previous B05 mechanism aggregated pair Pluecker mass and then attempted curved-trace payment in the exact-rank-three heavy-isotropic normal form. It exposed nonzero triple defect as the next obstruction but did not close it. This run deliberately changes mechanism: instead of another reciprocal-minor or local pair estimate, it studies the rank-three vector matroid of the physical spectral rows and classifies the exact **zero disjoint-basis-mass endpoint**. One of the resulting terminal geometries is then paid by a product-preserving coarea argument.

The mandatory corrections are respected. No law-uniform pointwise Fresnel decay is used; no independence is asserted after a general spectral rotation; no unrestricted fiber supremum is integrated; no one-good-minor dichotomy is assumed; and no conditional density cap is substituted for genuine independence where the cited hyperbolic theorem needs independence.

The assigned partner is `fleet04/B05`. Fresh source checks found no completed current-QFORM artifact at either its canonical math-open-problems root or its shared handoff root, so no theorem is fabricated for that slot. A completed compatible fleet04 theorem is nevertheless applied at an actual inequality below: fleet04/B18, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Two other completed dependencies are used at their stated scopes:

1. fleet02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical report
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`: every orthogonal two-dimensional projection of a cap-one product law has joint density at most `e`.
2. fleet02/B10, scaled dependent-pair hyperbolic-square theorem, canonical report
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`: if `W` is genuinely independent of a possibly dependent pair `(Y,Z)`, with caps `K,H`, then
   `2aWY+F(Y)+b(Z+theta(Y))^2` has density at most
   `3*2^(2/3) H^(2/3) K^(2/3)|a|^(-2/3)|b|^(-1/3)`.

All new statements below are for the exact-rank-three spectral core. Arbitrary additional spectral directions remain a separate interaction debt.

## 2. Disjoint spectral bases and the exact zero-mass endpoint

Let

`A=U Lambda U^T`, `U^T U=I_3`,

where `Lambda` is an invertible symmetric `3 x 3` matrix with all three eigenvalues of modulus at least one. Write the physical rows of `U` as `u_i in R^3`. Ignore zero rows and let `E` be the finite set of nonzero rows. For every three-set `I subset E`, put

`w_I = det(U_I)^2`.

By Cauchy--Binet,

`sum_{|I|=3} w_I = det(U^T U)=1`.                                      (2.1)

Thus the positive `w_I` are exactly the bases of the rank-three vector matroid of the rows. Define the ordered disjoint-basis mass

`D_0 = sum_{I cap J = empty} w_I w_J`.                                 (2.2)

Then `D_0=0` if and only if this vector matroid has no two disjoint bases.

### Theorem 2.1 — `QFORM-RANK3-ZERO-DISJOINT-BASE-CLASSIFICATION-v1`

If `D_0=0`, at least one of the following holds:

1. at most five physical spectral rows are nonzero;
2. a one-dimensional spectral line contains all but at most three nonzero rows;
3. a two-dimensional spectral plane contains all but exactly one nonzero row.

#### Proof

Use the classical Edmonds--Fulkerson matroid base-packing theorem for `k=2`: a rank-`r` finite matroid on `E` contains two disjoint bases iff

`2 r(S) + |E\S| >= 2r`                                                 (2.3)

for every `S subset E`. Here `r=3`. Since two disjoint bases do not exist, there is an `S` with

`2 r(S)+|E\S| <=5`.                                                     (2.4)

The rank of `S` can only be `0,1,2`; rank `3` would make the left side at least six. If `r(S)=0`, then because `E` contains only nonzero rows, `S` is empty and `|E|<=5`. If `r(S)=1`, all rows of `S` lie on a line and `|E\S|<=3`. If `r(S)=2`, all rows of `S` lie in a plane and `|E\S|<=1`. Since the full row configuration has rank three, the last complement cannot be empty, hence it consists of exactly one row. QED.

This classification is a structural endpoint theorem, not a density theorem. Its point is that failure of all disjoint spectral-basis aggregation is not arbitrary: it collapses to finite support, a line-plus-three-exceptions geometry, or a plane-plus-one-exception geometry.

## 3. Plane-plus-one-exception is an exact physical coloop

The third endpoint is substantially more rigid because `U^TU=I_3`.

### Lemma 3.1 — `QFORM-PLANE-SINGLETON-COLOOP-RIGIDITY-v1`

Assume all nonzero rows except one row `u_0` lie in a two-dimensional plane `H`. Let `n` be a unit normal to `H`. Then

`u_0 = +/- n`, `||u_0||=1`,                                           (3.1)

and the remaining rows form a Parseval frame of `H`. Consequently, after changing only the spectral bookkeeping basis, the spectral coordinate in direction `n` is exactly `+/- X_0`, while the other two spectral coordinates depend only on the original coordinates different from `X_0` and are therefore independent of `X_0`.

#### Proof

The Parseval identity is

`sum_i u_i u_i^T=I_3`.                                                 (3.2)

Taking the quadratic form against `n` gives

`1=sum_i <u_i,n>^2=<u_0,n>^2`,                                        (3.3)

because all other rows lie in `H`. Every row leverage is at most one since `UU^T` is an orthogonal projection, so

`1=|<u_0,n>|^2 <= ||u_0||^2 <=1`.

Equality forces `u_0=+/- n`. Subtracting `u_0u_0^T=nn^T` from (3.2) leaves the identity on `H`. QED.

This is exactly the product provenance needed by coarea: the exceptional spectral direction is not merely a bounded-density projection; it is one untouched original independent coordinate.

## 4. A coloop coarea theorem: isotropic pivot

Choose the orthonormal spectral basis `n,e_1,e_2`. In the coloop geometry write

`Lambda = [[a,b^T],[b,C]]`,                                            (4.1)

where `a` is scalar, `b in R^2`, and `C` is symmetric. Let

`Y=(Y_1,Y_2)`

be the spectral projection of the remaining original coordinates to `H`. By fleet02/B06's completed weighted affine-fiber theorem,

`||p_Y||_infinity <= e`.                                               (4.2)

Also `X_0` is independent of `Y` and has density cap one.

### Theorem 4.1 — `QFORM-COLOOP-ISOTROPIC-COAREA-v1`

If the coloop pivot is isotropic, `a=0`, then

`boxed(
 ||p_Q||_infinity
 <= 3 (2e)^(2/3) |det Lambda|^(-1/3)
 <= 3(2e)^(2/3)
 < 9.276.
)`                                                                    (4.3)

#### Proof

Invertibility of `Lambda` forces `b!=0`. Rotate only the two-dimensional spectral bookkeeping plane `H` so that `b=(B,0)` with `B=||b||>0`. This does not rotate the original independent coordinates; it only chooses coordinates for the already dependent pair `Y`. Write

`C=[[r,s],[s,tau]]`.

Then

`det Lambda = -B^2 tau`,                                               (4.4)

so `tau!=0`. The quadratic is exactly

`Q=2B X_0 Y_1 + rY_1^2+2sY_1Y_2+tau Y_2^2`

` =2B X_0Y_1 +(r-s^2/tau)Y_1^2
   +tau(Y_2+(s/tau)Y_1)^2`.                                           (4.5)

Now apply fleet02/B10's completed scaled dependent-pair hyperbolic-square theorem with

`W=X_0`, `K=1`, `H=e`, `a_hyp=B`, `b_hyp=tau`.

It yields

`||p_Q||_infinity
 <=3*2^(2/3)e^(2/3)|B|^(-2/3)|tau|^(-1/3)`
` =3(2e)^(2/3)(B^2|tau|)^(-1/3)`
` =3(2e)^(2/3)|det Lambda|^(-1/3)`.                                   (4.6)

Since every eigenvalue of `Lambda` has modulus at least one, `|det Lambda|>=1`. QED.

This is a genuinely dimension-free coarea closure of one terminal zero-disjoint-basis geometry. It retains arbitrary input laws and all signs allowed by the displayed invertible block. It proves an essentially bounded density in this branch; continuity is not claimed from this argument.

## 5. A coloop coarea theorem: minority-sign pivot

The nonzero coloop pivot has another paid region. Suppose `Lambda` has indefinite inertia `(2,1)` or `(1,2)` and `a` has the minority sign. Then the Schur complement

`S=C-bb^T/a`                                                           (5.1)

is definite of the majority sign by Sylvester inertia additivity. Complete the square only in the untouched original coordinate `X_0`:

`Q=a(X_0+a^(-1)b^TY)^2+Y^T S Y`.                                      (5.2)

The projected pair `Y` has joint density cap `e`. Therefore direct two-dimensional elliptic coarea gives

`||p_{Y^T S Y}||_infinity <= pi e / sqrt(|det S|)`.                    (5.3)

The translation of `X_0` depends on `Y`, so ordinary convolution independence is not available. This is exactly where the completed compatible fleet04/B18 theorem is applied.

### Theorem 5.1 — `QFORM-COLOOP-MINORITY-SQUARE-SMOOTHING-v1`

Under the minority-sign hypothesis,

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(pi e) (|a| |det Lambda|)^(-1/4).
)`                                                                    (5.4)

In particular, if `|a|>=eta>0`, then

`||p_Q||_infinity <= 2 sqrt(pi e) eta^(-1/4) < 5.845 eta^(-1/4)`.      (5.5)

#### Proof

Let `R=Y^T S Y`. Equation (5.3) gives its density cap

`M=pi e |det S|^(-1/2)`.                                              (5.6)

Disintegrate over `R=r`. Because `X_0` is independent of all remaining original coordinates, the conditional law of

`V_r=X_0+a^(-1)b^T Y`

is a mixture of translates of the original density of `X_0`, and hence has conditional density cap one. Apply fleet04/B18's `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` to

`Q=R+aV_R^2`.

It gives

`||p_Q||_infinity <=2 sqrt(M/|a|)`
` =2 sqrt(pi e)|a|^(-1/2)|det S|^(-1/4)`.                             (5.7)

Since `det Lambda=a det S`, (5.7) is exactly (5.4). QED.

This is an actual application of completed fleet04 mathematics to the current B05 inequality. The designated fleet04/B05 slot itself still has no completed current-QFORM artifact visible in the authorized repositories, so no result is attributed to it.

## 6. What this eliminates, and what remains

The exact endpoint `D_0=0` is now reduced to three rigid structural types. In the plane-plus-singleton type, the singleton is automatically a physical spectral coloop, and two important subbranches are completely paid:

- isotropic coloop pivot `a=0`: universal bound `<9.276`;
- indefinite minority-sign coloop pivot: determinant-scale square-smoothing bound (5.4), universal whenever the pivot is bounded away from zero.

The first unpaid implication inside the **same plane-plus-singleton endpoint** is the majority-sign nonzero coloop pivot (equivalently, an indefinite Schur complement in (5.2)) together with the possibility `a->0` through that majority-sign side. A bounded joint density of `Y` alone cannot pay an indefinite quadratic pushforward; the current correction set already rules out collapsing product provenance to only such a cap. The next coarea attack should therefore use the full weighted affine-fiber representation of `Y`, not merely (4.2), before the hyperbolic trace is taken.

The other two exact base-packing endpoints also remain:

- at most five nonzero spectral rows;
- a line containing all but at most three nonzero rows.

These are finite-bank / grouped-bank configurations and are candidates for an original-coordinate grouped reduction. A local reciprocal-minor argument is not sufficient by itself.

Finally, `D_0=0` is an exact endpoint. A full rank-three proof also needs a **quantitative stability theorem** when `D_0` is small but nonzero, unless one directly uses the already completed disjoint-basis density theorem in the region where `D_0` is bounded below. Arbitrary extra nonzero spectral directions remain a separate full-target debt.

Thus the full owner QFORM conjecture is still **OPEN / NOT PROVED**, and continuity for the full target is still **OPEN**.

## 7. New source-valid claim cards

1. `QFORM-RANK3-ZERO-DISJOINT-BASE-CLASSIFICATION-v1` — **PROVED SUPPORTING STRUCTURAL THEOREM**.
2. `QFORM-PLANE-SINGLETON-COLOOP-RIGIDITY-v1` — **PROVED SUPPORTING STRUCTURAL THEOREM**.
3. `QFORM-COLOOP-ISOTROPIC-COAREA-v1` — **PROVED SUPPORTING DENSITY THEOREM**, bound `3(2e)^(2/3)|det Lambda|^(-1/3)`.
4. `QFORM-COLOOP-MINORITY-SQUARE-SMOOTHING-v1` — **PROVED SUPPORTING DENSITY THEOREM**, bound `2sqrt(pi e)(|a||det Lambda|)^(-1/4)`.
5. Full QFORM — **OPEN**.
6. Full continuity — **OPEN**.

## 8. External theorem used in Section 2

The only external combinatorial theorem invoked is the classical Edmonds--Fulkerson matroid base-packing theorem. Its use is finite, rank three, and exactly equation (2.3). No probabilistic, analytic, or quadratic-form conclusion is imported from that source.
