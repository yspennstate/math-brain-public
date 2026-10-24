SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-22T23:32:47Z.
attacking: the singular/near-isotropic scalar-pair endpoint in the one-rank-two/two-rank-one bank geometry; preserve the original product law and eliminate the reciprocal smallest-singular-value loss at exact scalar-pair rank one.

# account01/B05 QFORM r23 — exact rank-one scalar-pair closure by two-regime coarea

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Control observed before the mathematical write:** owner revision `2026-09-22.15`, QFORM only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository retrieval is not native brain ingestion).  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED`.  
**Full conjecture:** `OPEN_NOT_PROVED`.  
**Continuity:** not proved here; the theorem below asserts essential boundedness only.

## 1. Source-valid starting point

Use the exact-rank-three three-bank geometry from account03/B05 r19. The active original-coordinate set is partitioned into disjoint banks `G1,G2,G3`. Bank `G1` has spectral rank two, while `G2,G3` have spectral rank one. Writing

`A_S = R_S M R_S^T`, with `M` invertible symmetric `3 x 3`,

factor

`R_G1 = C T1^T`, `C^T C=I_2`,

and define the genuine product-origin two-dimensional projection

`L=C^T X_G1`.

The two rank-one banks compress to scalar aggregates `Y,Z`, independent of each other and of the whole first bank, with

`||p_Y||_infinity, ||p_Z||_infinity <= sqrt(2)`.

Let `t2,t3` be their normalized spectral columns. In variables `(L1,L2,Y,Z)` the quadratic matrix is

`K = [[C0,p,q],[p^T,a,c],[q^T,c,d]]`,

where `C0` is `2 x 2`, `p,q in R^2`, and

`B=[[a,c],[c,d]] = [t2,t3]^T M [t2,t3]`.

The four compressed columns span the three-dimensional spectral space, hence `rank K=3`.

The aggregate physical principal-triple determinant mass is

`mu = sum_(i in G1,j in G2,k in G3) |det A_{ijk}|`.

This is the same `mu` as in account03/B05 r19; no individual physical triple is selected.

The live correction stream is respected: no arbitrary-joint coarea bound, no conditional projection-density cap, no post-rotation independence, and no law-uniform pointwise oscillatory decay are used.

## 2. Exact rank-one scalar-pair geometry

Assume the scalar-pair block `B` has rank exactly one. It is nonzero. Choose the scalar labels so that

`|a| >= |d|` and hence `a !=0`.

Since `det B=ad-c^2=0`,

`d=c^2/a`, and `|eta|:=|c/a|=sqrt(|d/a|)<=1`.

Set

`theta = q-(c/a)p`, `r=||theta||_2`.

### Lemma 2.1 — aggregate singular-pair identity

`boxed(mu = |a| r^2.)`

#### Proof

For each of the two orthonormal compressed first-bank coordinates `L_ell`, take the compressed principal triple `(L_ell,Y,Z)`. Its determinant is

`det [[(C0)_{ell ell}, p_ell, q_ell],
      [p_ell,              a,     c],
      [q_ell,              c,     d]]
 = -a (q_ell-(c/a)p_ell)^2
 = -a theta_ell^2`,

because `d=c^2/a`.

For exact rank three, every physical principal triple has determinant

`det(M) det(r_i,r_j,r_k)^2`,

so all nonzero triple determinants have one common sign. The Cauchy--Binet compression used in account03/B05 r19 therefore identifies the sum of the absolute values of the two compressed triple determinants with the full bank packet `mu`. Summing the display over `ell=1,2` gives

`mu=|a|(theta_1^2+theta_2^2)=|a|r^2`. QED.

In particular, `mu>0` forces `theta !=0`. Also, if `B=0` then every `(one G1 coordinate,G2,G3)` principal triple is zero, hence `mu=0`. Therefore the positive-packet branch can never have scalar-pair rank zero: its only singular case is exactly rank one.

### Lemma 2.2 — common-factor residual normal form

After completing the `Y` square, the quadratic residual on `(L,Z)` is

`S0 = [[C0-pp^T/a, theta],[theta^T,0]]`.

Since `rank K=3` and the pivot `a` has rank one, `rank S0=2`. Rotate only the two-dimensional notation for `L` so that `theta=r e1`, and write the first-bank coordinates in that notation as `(U,V)`. Then

`S0 = [[alpha,beta,r],[beta,0,0],[r,0,0]]`

for some `alpha,beta`. Indeed, if the lower-right entry of the transformed `2 x 2` first-bank block were `gamma`, then

`det S0 = -r^2 gamma`;

rank two and `r>0` force `gamma=0`. Thus the entire residual quadratic phase factors as

`boxed(alpha U^2+2 beta U V+2r U Z = U(alpha U+2 beta V+2rZ).)`

This identity is useful structural information: at the singular scalar-pair endpoint the internal rank-two-bank curvature is not an arbitrary leaking quadratic form; it has one common linear factor.

## 3. A two-variable affine rank-one coarea lemma

The key estimate is elementary and keeps the original independent scalar variables.

### Lemma 3.1 — sheared-square plus null-linear coarea

Let `Y,Z` be independent probability variables with density caps `L_Y,L_Z`. Let `a h !=0`, `|eta|<=1`, and let `delta,k` be arbitrary real numbers. Put

`F=a(Y+eta Z+delta)^2+hZ+k`.

Then `F` is absolutely continuous and, for every density representative obtained by the coarea formula,

`p_F(q) <= min{ (4L_Y+2L_Z)/|h|,
                 2 sqrt(2) L_Y sqrt(L_Z) / sqrt(|a h|) }`.          (3.1)

#### Proof of the first bound

Use the unit-Jacobian shear

`s=Y+eta Z+delta`, `z=Z`.

On the level `q=a s^2+h z+k`,

`z_q(s)=(q-k-a s^2)/h`,
`y_q(s)=s-eta z_q(s)-delta`.

Therefore

`p_F(q)=|h|^{-1} integral f_Y(y_q(s)) f_Z(z_q(s)) ds`                 (3.2)

for a.e. `q`.

Write `tau=2as/h`. Then

`z_q'(s)=-tau`, `y_q'(s)=1+eta tau`.

Split the real line into

`A={|tau|>=1/2}`, `B0={|tau|<1/2}`.

On each of the two monotone components of `A`, `|z_q'|>=1/2`. Hence, using `f_Y<=L_Y` and `integral f_Z=1`,

`integral_A f_Y(y_q(s))f_Z(z_q(s)) ds <=4L_Y`.                       (3.3)

On `B0`, because `|eta|<=1`,

`y_q'(s)>=1-|eta||tau|>=1/2`.

This is one monotone interval. Using `f_Z<=L_Z` and `integral f_Y=1`,

`integral_B0 f_Y(y_q(s))f_Z(z_q(s)) ds <=2L_Z`.                      (3.4)

Substitution in (3.2) proves the first term in (3.1).

#### Proof of the second bound

Condition on `Z=z`. A translated square of a variable with density cap `L_Y` has density bounded by

`L_Y / sqrt(|a| |u|)`

at displacement `u` from its translated vertex. Hence

`p_F(q) <= L_Y |a|^{-1/2}
           integral f_Z(z)|q-k-hz|^{-1/2} dz`.                       (3.5)

The law of `hZ` has density cap `L_Z/|h|`. For any probability density `g<=M`, the one-dimensional bathtub inequality gives

`sup_x integral |x-u|^{-1/2} g(u)du <=2 sqrt(2M)`.                   (3.6)

Apply (3.6) with `M=L_Z/|h|` to obtain the second term in (3.1). QED.

The two terms in (3.1) are deliberately both retained. The square-kernel term is integrable at `h=0`; the direct null-linear coarea term is stronger away from zero. Their crossover is what removes the singular pivot loss below.

## 4. Main theorem: exact singular scalar-pair closure

### Theorem 4.1 — `QFORM-RANK2BANK-RANK1-SCALARPAIR-COAREA-v1`

In the exact-rank-three three-bank geometry of Section 1, assume the scalar-pair block `B` has rank exactly one and `mu>0`. Arbitrary affine terms in all active variables are allowed, including those produced by conditioning every original coordinate outside the active banks. Then

`boxed(||p_Q||_infinity <= 16 mu^(-1/3).)`                            (4.1)

Only essential boundedness is asserted.

#### Proof

Include arbitrary affine terms and complete the `Y` square. With

`eta=c/a`, `theta=q-(c/a)p`,

one obtains exactly

`Q = a[Y+eta Z+delta(L)]^2 + H(L) Z + K0(L)`,                         (4.2)

where

`H(L)=2 theta dot L+h0`                                                (4.3)

for a constant `h0`; `delta(L)` and `K0(L)` may be arbitrary affine/quadratic functions generated by the algebra. No independence between the two coordinates of `L` is asserted or needed.

Condition on the whole first bank, equivalently on `L` together with any unused first-bank information. The scalar variables `Y,Z` are still independent, with caps `sqrt(2)`. Lemma 3.1 therefore gives

`p_(Q|L)(q) <= F(|H(L)|)`,                                            (4.4)

where

`F(h)=min{ 6sqrt(2)/h, 2^(9/4)/sqrt(|a|h) }`, `h>0`.                  (4.5)

Now use the product origin of `H`. The normalized linear projection

`(theta/r) dot L`

is a unit Euclidean linear form in the original independent coordinates of `G1`; the source-pinned product-marginal theorem gives density at most `sqrt(2)`. Therefore the affine variable `H=2 theta dot L+h0` has density cap

`M_H <= 1/(sqrt(2) r)`.                                               (4.6)

The function `F` is decreasing. Among all probability densities bounded by `M_H`, the symmetric bathtub bound yields

`E F(|H|) <= 2 M_H integral_0^R F(h) dh`,
`R=1/(2M_H)=r/sqrt(2)`.                                               (4.7)

The two terms of (4.5) cross at

`h_* = (9/(2sqrt(2))) |a|`.                                          (4.8)

If `h_*<=R`, then direct integration gives

`E F(|H|)
 <= (12/r)[2+log(2r/(9|a|))]`.                                       (4.9)

If `h_*>R`, then the square-kernel branch on the whole bathtub interval gives

`E F(|H|) <=8sqrt(2) |a|^{-1/2} r^{-1/2}`.                           (4.10)

Use the exact identity `mu=|a|r^2`. Write

`|a|=mu^(1/3) z`, `r=mu^(1/3) z^{-1/2}`.

The first case is `z<=(2/9)^(2/3)` and (4.9) becomes

`12 mu^(-1/3) z^(1/2)
 [2+log(2/(9z^(3/2)))]`.                                              (4.11)

Its maximum occurs at

`z^(1/2)=(2/(9e))^(1/3)`

and equals

`36(2/(9e))^(1/3) mu^(-1/3)
 <15.625 mu^(-1/3)`.                                                   (4.12)

In the second case (4.10) is

`8sqrt(2) mu^(-1/3) z^(-1/4)`,                                       (4.13)

which decreases with `z`; at the boundary `z=(2/9)^(2/3)` it is

`8sqrt(2)(9/2)^(1/6) mu^(-1/3)
 <14.537 mu^(-1/3)`.                                                   (4.14)

Thus both cases are bounded by `16 mu^(-1/3)`, proving (4.1). QED.

### Concrete packet consequence

Account03/B10 r20 supplies a tripartite packet with

`mu>=1/512`.

Whenever two packet banks are spectral rank one, the third is spectral rank two, and the compressed scalar-pair block is singular, positivity of `mu` rules out `B=0`, so `rank B=1` and Theorem 4.1 applies. Hence

`boxed(||p_Q||_infinity <=16*(512)^(1/3)=128.)`                       (4.15)

This closes the **exact singular scalar-pair endpoint** without selecting a small physical principal triple and without a reciprocal `sigma_min(B)` factor.

## 5. Named partner result consumed and applied

The designated partner account02/B05 completed run `20260922T225232Z-account02-B05-QFORM-37473ccc`, canonical mathematics

`yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T225232Z-account02-B05-QFORM-37473ccc/REPORT.md`.

Its theorem `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1` says that if `X` has density cap `L_X`, an independent environment supplies a random slope `T` of density cap `L_T`, and `R=K(E)+2XT(E)`, then

`sup_q E|q-R|^(-1/2) <=4 sqrt(2L_XL_T)`,                              (5.1)

and a further independent cap-one translated square of coefficient `b` converts this to a density bound after multiplication by `|b|^{-1/2}`.

Apply it to (4.2) before the new two-regime improvement. Put `X=Z` and `T=H/2`. From (4.6),

`L_X=sqrt(2)`, `L_T<=sqrt(2)/r`.

Therefore (5.1) gives

`sup_q E|q-[H(L)Z+K0(L)]|^(-1/2) <=8/sqrt(r)`.                        (5.2)

Since `Y` has density cap `sqrt(2)`, normalize `S=sqrt(2)Y`, which has cap one; the coefficient of its translated square is `a/2`. The partner theorem then yields the actual inequality

`||p_Q||_infinity
 <=8sqrt(2) |a|^{-1/2} r^{-1/2}
 =8sqrt(2) |a|^{-1/4} mu^{-1/4}.`                                    (5.3)

Thus the newest partner theorem identifies exactly the residual loss in a one-regime fractional argument: `|a|^{-1/4}`. Theorem 4.1 removes that loss by adding the direct `1/|H|` coarea estimate away from the small-slope region and optimizing the crossover. This is a genuine application, not merely a citation.

The partner's reverse-conditioned leakage theorem is consistent with the same principle: condition product banks before paying reciprocal Jacobians. The present proof uses that ordering at the singular three-bank endpoint and then uses a two-scale rather than one-scale Jacobian payment.

## 6. Conditional end-to-end position and first unpaid implication

The current aggregate-bank architecture now has the following exact improvement.

- The diffuse selected core is paid by account03/B10 r20.
- The three-rank-one-bank grouped-star endpoint is paid by account03/B10 r20.
- One rank-two bank plus two rank-one banks with an invertible indefinite scalar-pair block is paid quantitatively by account03/B05 r19 away from its reciprocal `kappa` loss.
- **New here:** if that scalar-pair block is exactly singular and the determinant packet is positive, then it is automatically rank one and is paid by (4.1), with the concrete packet bound `128`.

The first essential missing implication is therefore no longer the exact singular endpoint. It is the **stable near-singular crossover**:

`QFORM-NEAR-RANK1-SCALARPAIR-STABLE-COAREA-v1`:

> For the same one-rank-two/two-rank-one packet with `mu>=1/512`, control an invertible scalar-pair block whose smallest singular value tends to zero, uniformly through both definite and indefinite approaches, without reverting to `kappa^{-1/4}`. Equivalently, extend the two-regime argument above to the nonzero post-pivot `Z^2` coefficient while retaining the exact aggregate Schur identity and original-coordinate product structure.

The exact rank-one formula shows why this should be a crossover problem rather than a genuine singular obstruction: at the endpoint the dangerous reciprocal Jacobian has two complementary integrable regimes and the packet identity supplies exactly the scaling `mu=|a|r^2` needed to optimize them to `mu^{-1/3}`.

Configurations with two or three internally rank-two resource banks, arbitrary additional spectral directions, and the global routing from the bare three-large-eigenvalue hypothesis remain outside this theorem. Therefore the full QFORM conjecture remains open.

## 7. Audit notes

1. No rotation of the original `X_i` is declared independent. `Y,Z` are scalar aggregates of disjoint rank-one original-coordinate banks; `L` remains a whole product-origin two-dimensional projection block.
2. The only marginal-density input is the source-pinned one-dimensional product projection bound `sqrt(2)`.
3. Arbitrary affine terms survive: they only alter `delta(L)`, `h0`, and `K0(L)` and therefore do not change any estimate.
4. The proof never invokes the refuted arbitrary-joint rank-three coarea claim or any positive conditional-density-moment bound.
5. The numerical constants in (4.12)--(4.14) are optional slack; `16` is used as the clean theorem constant.
6. Essential boundedness is established in this branch. Continuity is not established.

## 8. Source pins

- account03/B05 aggregate rank-two-bank theorem and determinant packet identity: `yspennstate/math-open-problems@70f181cf738aa51ee6fb7043a329ac9e8b22c4ec:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T223741Z-account03-B05-QFORM-r19/REPORT.md`.
- account03/B10 tripartite packet `mu>=1/512`: `yspennstate/math-open-problems@7acd371ee2ee83a7fae12d7bedb38bc99c051b6d:proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T221548Z-account03-B10-QFORM-r20/REPORT.md`.
- designated partner account02/B05 reverse-conditioned leakage + random-slope half-Riesz: `yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T225232Z-account02-B05-QFORM-37473ccc/REPORT.md`.
