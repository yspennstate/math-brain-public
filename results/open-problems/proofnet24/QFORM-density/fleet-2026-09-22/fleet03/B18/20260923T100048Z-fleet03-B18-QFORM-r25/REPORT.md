SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T10:00:48Z.

attacking: non-source-separated high-shear exact-rank-three branch via source-valid projection/decoupling inequalities and an actual fleet04/B18 splice.

# fleet03/B18 — Edmonds zero-collision reduction and the exact plane-plus-one receiver

**Run:** `20260923T100048Z-fleet03-B18-QFORM-r25`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `NEW STRUCTURAL REDUCTION + TWO PARTNER-PAID PLANE ENDPOINTS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope

Work in the exact-rank-three Schur-isotropic packet

`Q=(Y+r n X_0)^T D (Y+r n X_0)`,                                (1.1)

where

- `X_0,X_1,...,X_m` are independent real random variables with probability densities bounded by one;
- `D` is a real symmetric invertible `3x3` matrix;
- `n in S^2`, `r>0`, and `n^T D n=0`;
- `Y=sum_j v_j X_j`, with residual Parseval frame

`sum_j v_j v_j^T=I_3`.                                          (1.2)

The physical coefficient map is `L=[r n,v_1,...,v_m]`, so

`L L^T=I_3+r^2 n n^T`,                                          (1.3)

and, if the three nonzero eigenvalues of the physical matrix all have modulus at least one,

`|det D|(1+r^2)>=1`.                                             (1.4)

This report treats the exact **zero-disjoint-residual-basis endpoint** of the aggregate two-bank method and then pays two pieces of the only surviving geometry. It does not absorb arbitrary extra spectrum and does not prove the unrestricted conjecture.

No step below uses post-rotation independence, arbitrary-joint coarea, a conditional-density cap as a substitute for independence, a positive moment of a worst conditional projection density, a fixed good physical minor, deletion of small coefficients, or pointwise law-uniform van-der-Corput decay.

## 2. Primary literature transfer

### 2.1 Edmonds matroid union/base packing

The deterministic source is Jack Edmonds' matroid-union/partition theorem. A convenient primary citation is:

Jack Edmonds, *Submodular functions, matroids, and certain polyhedra*, in **Combinatorial Structures and Their Applications**, Gordon and Breach (1970), pp. 69--87.

The 1965 precursor is Jack Edmonds, *Minimum partition of a matroid into independent subsets*, J. Res. Natl. Bur. Standards B **69B** (1965), 67--72, DOI 10.6028/jres.069B.004.

For a rank-`rho` matroid `M=(E,r_M)`, the matroid-union formula for the maximum size of a union of `k` independent sets is

`min_(U subset E) [ |E\U| + k r_M(U) ]`.                         (2.1)

Hence `M` has `k` pairwise disjoint bases iff

`|E\U| >= k(rho-r_M(U))` for every `U subset E`.                 (2.2)

We use only `rho=3`, `k=2`.

### 2.2 Livshyts--Paouris--Pivovarov

The probabilistic source is

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. **216** (2016), 877--889; arXiv:1507.07949.

For a product probability density with every one-dimensional factor bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. No moment, Gaussian, log-concave, bounded-support, connected-support, smoothness, symmetry, centering, or iid hypothesis is present.

In particular, if `a` is a unit coefficient vector then

`||p_(sum a_i X_i)||_infinity <= sqrt(2)`.                       (2.3)

For a full-rank linear map `B^T X` into `R^2`, whitening gives

`||p_(B^T X)||_infinity <= 2/sqrt(det(B^T B))`.                  (2.4)

## 3. New theorem: zero residual base-collision reduces to one exact geometry

Let `M_v` be the rank-three vector matroid of the nonzero residual frame vectors `{v_j}`.

### Theorem 3.1 — `QFORM-EDMONDS-ZEROCOLLISION-REDUCTION-v1`

Assume `M_v` has **no two disjoint bases**. Then at least one of the following holds.

1. `Q` already has an essentially bounded density with

`||p_Q||_infinity <= 4 sqrt(30 pi) = 38.8325182511...`;          (3.1)

2. there is a plane `P` with unit normal `m` such that, after relabeling, exactly one residual frame vector lies outside `P`, that vector is `v_*=+m` or `-m`, and the remaining plane bank is exactly Parseval on `P`:

`sum_(j != *) v_j v_j^T = P_P = I-mm^T`.                         (3.2)

Thus the entire exact zero-collision endpoint reduces, modulo a universal finite-dimensional bound, to an **exact plane-plus-one** residual frame.

The bound in (3.1) proves absolute continuity and essential boundedness. Continuity is not claimed from the projected-gradient theorem used there.

### Proof

Apply Edmonds' criterion (2.2) with `rho=3`, `k=2`. Since there are no two disjoint bases, some subset `U` obeys

`|E\U| < 2(3-r_M(U))`.                                           (3.3)

Because all quantities are integers, only three ranks can occur.

#### Rank two witness

If `r_M(U)=2`, then `|E\U|<=1`. Let `P=span{v_j:j in U}`. Every residual vector except possibly one lies in `P`.

Parseval rank three rules out zero exceptional vectors, so there is exactly one exceptional vector `q`. Let `m` be a unit normal to `P`. From

`G_P + qq^T=I`, `Ran(G_P) subset P`,                              (3.4)

we get by evaluating on `m`

`(m^T q)^2=1`.                                                    (3.5)

Every Parseval row satisfies `||q||^2<=1`, so (3.5) forces `q=+m` or `-m`. Substituting back into (3.4) gives `G_P=I-mm^T`. This is exactly alternative 2.

#### Rank one witness

If `r_M(U)=1`, all but at most three residual vectors lie on one line. Write the line as `span{e}` and the collinear rows as

`v_j=a_j e`, `j in C`,

with

`alpha=sum_(j in C) a_j^2 in [0,1]`.                             (3.6)

If `alpha=0`, there are at most three nonzero residual physical coordinates, so together with `X_0` the form uses at most four original cap-one variables; the finite-dimensional theorem quoted below gives a smaller bound than (3.1).

Assume `alpha>0` and define

`W=alpha^(-1/2) sum_(j in C) a_j X_j`.                            (3.7)

The coefficients of `W` have Euclidean norm one, so (2.3) gives `||p_W||_infinity<=sqrt(2)`. Put `W'=sqrt(2)W`; then `W'` has density cap at most one and is independent of `X_0` and all exceptional residual coordinates.

The original line-bank contribution is exactly

`sum_(j in C) v_j X_j = sqrt(alpha/2) e W'`.                     (3.8)

Thus the law of `Q` is represented **exactly** as a quadratic form in at most five independent cap-one scalar variables: `X_0`, `W'`, and at most three exceptional original coordinates.

Let

`G=I+r^2 n n^T`                                                  (3.9)

be the active Gram before the normalization (3.8), and let `G'` be the active Gram after replacing the whole line bank by the cap-one variable `W'`. Then

`G'=G-(alpha/2) e e^T`.                                         (3.10)

Since `alpha e e^T` is one component of the residual Parseval sum, `alpha e e^T<=I<=G`. Hence

`G/2 <= G' <= G`.                                                (3.11)

Let

`B=G^(1/2) D G^(1/2)`, `B'=G'^(1/2) D G'^(1/2)`.                 (3.12)

The eigenvalues of `B` are exactly the three nonzero physical eigenvalues, so the target gives `s_min(B)>=1`. Set

`T=G^(-1/2)G'^(1/2)`.                                            (3.13)

Then

`B'=T^T B T`,                                                    (3.14)

and (3.11) implies `s_min(T)^2>=1/2`. Therefore

`s_min(B') >= s_min(T)^2 s_min(B) >=1/2`.                        (3.15)

So the exact effective quadratic matrix in at most five independent cap-one variables has three eigenvalues of modulus at least `1/2`.

Use the completed projected-gradient finite-dimensional theorem

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1:

an `m`-variable cap-one quadratic-plus-affine form with three eigenvalues of modulus at least `sigma` has

`||p||_infinity <= 2 sqrt(6 pi m)/sigma`.                        (3.16)

With `m<=5`, `sigma=1/2`, this gives

`||p_Q||_infinity <=4 sqrt(30 pi)`.                              (3.17)

#### Rank zero witness

If `r_M(U)=0`, then (3.3) gives at most five nonzero residual vectors. Together with `X_0`, the form uses at most six actual original cap-one variables. No aggregation is needed, and the target gives `sigma=1`. Equation (3.16) yields

`||p_Q||_infinity <=2 sqrt(36 pi)=12 sqrt(pi)<4 sqrt(30 pi)`.    (3.18)

This proves the theorem. QED.

### Why the line aggregation is safe

The only probabilistic compression in the proof is (3.7), performed on a bank of **collinear physical rows**. The quadratic form depends on that entire bank only through the single scalar sum in (3.7), so no information relevant to `Q` is discarded. Independence is preserved because that bank is disjoint from the exceptional original coordinates and from `X_0`. The spectral loss in (3.15) is paid deterministically and is at most a factor two.

## 4. Exact plane-plus-one geometry: direct fleet04/B18 payment

Assume alternative 2 of Theorem 3.1. Let `P=m^perp`, let `X_*` be the exceptional original scalar with vector `v_*=m` (the sign can be absorbed into `X_*`), and put

`theta=|n^T m|`.                                                   (4.1)

The plane bank is exactly Parseval on `P` by (3.2).

The designated completed partner result is fleet04/B18:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

At its literal hypotheses, a cap-one scalar independent of a two-dimensional vector with joint density cap `M`, under a nonsingular symmetric zero scalar pivot, has a **continuous density** with

`||p||_infinity <=6 M^(2/3)|det K|^(-1/3).`                     (4.2)

The affine extension, needed only after conditioning, was proved by translating the dangerous fiber in fleet03/B18 run `20260923T062246Z-fleet03-B18-QFORM-r25`; no constant changes.

### Theorem 4.1 — tilted plane-plus-one branch

If `theta>0`, then after conditioning on `X_*`, the active scalar is `X_0` and the active pair is the two-dimensional plane-bank projection. LPP gives pair density cap `M<=2`. The active coefficient map from `(X_0, plane pair)` to `R^3` has determinant magnitude `r theta`, so the corresponding quadratic matrix `K` has

`|det K|=r^2 theta^2 |det D|`.                                   (4.3)

The scalar pivot is zero because `n^T D n=0`. Applying (4.2) gives the actual partner inequality

`boxed:
 ||p_Q||_infinity
 <=6*2^(2/3)[r^2 theta^2 |det D|]^(-1/3).
`                                                                    (4.4)

The conditional bound is uniform in the fixed value of `X_*`, so averaging preserves it. The density is continuous on this branch by the affine partner theorem and dominated convergence.

Under the target normalization (1.4), if `r>=1`,

`r^2 |det D| >= r^2/(1+r^2) >=1/2`,                              (4.5)

hence

`boxed: ||p_Q||_infinity <=12 theta^(-2/3).`                     (4.6)

This is not a universal bound as `theta ->0`; it is a source-valid quantitative payment for every fixed transverse angle.

### Theorem 4.2 — coplanar null-exception endpoint

Now suppose `theta=0`, so `n in P`, and assume additionally

`b:=m^T D m=0`.                                                   (4.7)

Keep `X_*` active as the partner scalar. The two-dimensional pair is now

`Z=P(Y+r n X_0)`                                                  (4.8)

inside `P`. It depends on the plane-bank original coordinates and `X_0`, all disjoint from `X_*`. Its coefficient Gram in an orthonormal basis of `P` is

`I_2+r^2 n n^T`,                                                  (4.9)

whose determinant is `1+r^2`. By whitening and LPP,

`||p_Z||_infinity <=2/sqrt(1+r^2)`.                              (4.10)

In the orthonormal basis `(m,P)`, the scalar pivot of `D` is exactly zero by (4.7), the scalar `X_*` is genuinely independent of the pair `Z`, and `|det K|=|det D|`. Applying the designated fleet04/B18 theorem gives

`||p_Q||_infinity
 <=6 [2/sqrt(1+r^2)]^(2/3)|det D|^(-1/3)`
`=6*2^(2/3)[|det D|(1+r^2)]^(-1/3)`
`<=6*2^(2/3)=9.52440631181...`.                                  (4.11)

This branch has a **continuous density**.

Equation (4.11) is a literal partner application with genuine scalar-versus-pair independence; no conditional-cap substitution is involved.

## 5. Additional exact payment at the coplanar endpoint when the exceptional pivot is bounded away from zero

The remaining coplanar geometry can also consume the newest sign-free fresh-square theorem from fleet03/B16:

`yspennstate/math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T095010Z-fleet03-B16-QFORM-r27/REPORT.md`.

Choose an orthonormal basis `(n,p,m)`. The plane bank gives a dependent pair `(H,U)`; `X_0`, `(H,U)`, and `X_*` are mutually independent source objects. The scalar `U` is a normalized one-dimensional projection of the Parseval plane bank, so LPP gives

`||p_U||_infinity <=sqrt(2)`.                                    (5.1)

The first active coordinate is `rX_0+H`; the fresh square scalar is `X_*`; the coefficient matrix is `D` in this basis, with fresh-square diagonal `b=m^T Dm`.

If `b!=0`, the sign-free theorem yields

`||p_Q||_infinity
 <=2^(13/4) sqrt(sqrt(2)/r) (|b det D|)^(-1/4)`
`=2^(7/2) r^(-1/2)(|b det D|)^(-1/4).`                           (5.2)

Using (1.4), for `r>=1`,

`boxed:
 ||p_Q||_infinity <=2^(15/4)|b|^(-1/4)
 =13.4543426441... |b|^(-1/4).
`                                                                    (5.3)

This proves absolute continuity and an essential bound; continuity is not claimed from this theorem.

Thus, at the exact plane-plus-one obstruction and `r>=1`, every region with either

`theta >= theta_0>0`                                             (5.4)

or, on the coplanar slice, `|m^TDm|>=b_0>0`, is quantitatively paid. The exact corner `theta=0`, `m^TDm=0` is also paid continuously by (4.11).

The remaining analytic collar is therefore sharply localized to

`theta ->0`, `m^T Dm ->0`,                                      (5.5)

with both nonzero at finite scale, where current source-preserving interfaces have a discontinuous certificate even though the exact corner is benign.

## 6. Relation to the high-shear obstruction

Fleet03/B18 r24 closed **source-separated** high shear. Fleet01/B18 r20 showed that two disjoint full-rank residual banks close exact rank three by LPP plus Plancherel. Theorem 3.1 addresses the opposite exact endpoint: when the residual vector matroid has no two disjoint bases at all, every zero-collision configuration except exact plane-plus-one is already universally bounded by a finite-dimensional reduction.

Hence the no-disjoint-basis endpoint is no longer a generic high-dimensional obstruction. Its only unresolved exact geometry is:

- a Parseval two-plane residual bank;
- one unit residual normal coordinate;
- a nearly coplanar high-shear direction `n`;
- a nearly null but nonzero exceptional quadratic pivot `m^T Dm`.

This is a much narrower shared-source receiver problem than arbitrary non-source-separated high shear.

## 7. Source-hypothesis audit and non-transfer

1. Edmonds is used only for deterministic support geometry of the residual vector matroid. It adds no probability assumption.
2. LPP is applied only to genuine linear marginals of disjoint original-coordinate product banks. It gives joint density caps, never independence of projected coordinates.
3. The fleet04/B18 zero-pivot theorem is used only where the scalar source and the entire two-dimensional pair use disjoint original-coordinate source sets.
4. The finite-dimensional projected-gradient theorem is applied after an **exact** collinear-bank aggregation; it is not applied after an arbitrary spectral rotation of random variables.
5. No coefficient tending to zero is replaced by zero. In particular, (4.11) treats the exact `b=0` endpoint separately, while (5.2) keeps every nonzero `b` exactly.

A focused literature check again found no published theorem matching the unrestricted QFORM statement; this is not a novelty claim from search absence.

## 8. Status and next implication

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full-target continuity:** OPEN.

Proved this run:

- `QFORM-EDMONDS-ZEROCOLLISION-REDUCTION-v1`: zero residual base-collision reduces to exact plane-plus-one, with every line-plus-three or finite-support alternative universally paid by `4 sqrt(30 pi)`.
- exact tilted plane-plus-one partner bound (4.4), continuous;
- exact coplanar/null-exception partner bound (4.11), continuous;
- coplanar/nonzero-exception sign-free bound (5.2)--(5.3), essential `L^infinity`.

The first local unpaid implication is now:

`QFORM-PLANEPLUSONE-NEAR-CORNER-v1`:

> in the exact plane-plus-one Schur packet, obtain one source-preserving bound uniform as both `theta=|n^Tm|` and `b=m^TDm` tend to zero through nonzero values, or route this collar to an already-paid hub/ridge/physical-pair mechanism.

A separate global compiler is still needed to absorb arbitrary additional spectrum.

## 9. Source pins

- Edmonds 1965 primary paper: https://doi.org/10.6028/jres.069B.004
- Edmonds 1970 primary matroid-union source: *Submodular functions, matroids, and certain polyhedra*, pp. 69--87.
- LPP primary source: https://arxiv.org/abs/1507.07949
- designated fleet04/B18 zero-pivot theorem: `math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`.
- projected-gradient finite-dimensional theorem: `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`.
- sign-free fresh-square receiver: `math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`.

Repository retrieval is not native mathematical-brain ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
