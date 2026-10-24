SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T15:04:43Z.
attacking: the heavy-transverse null-hub survivor; reroot exact-null heavy anchors, pay nonzero anchors by a source-valid rank-two half-Riesz Schur identity, and construct a target-valid diffuse stress family against fixed-minor shortcuts.

# account02/B18 — heavy-anchor reroot compiler and diffuse-null stress family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING EXACT-RANK3 COMPILER / SOURCE-VALID SHORTCUT COUNTEREXAMPLE / FULL QFORM OPEN`  
**Continuity:** proved only on the exact-null reroot-diffuse branch; not claimed on the nonzero-pivot branch or globally.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and live correction boundary

The owner target remains: arbitrary dimension, independent original real coordinates with one-dimensional probability densities bounded by one, and a real symmetric physical matrix with at least three eigenvalues of modulus at least one. Prove a universal essential-density bound for `X^T A X` or give a valid counterexample.

This report adds no moments, support bounds, log-concavity, symmetry, centering, iid hypothesis, diagonal-basis assumption, or post-rotation independence. It explicitly retains the live corrections: arbitrary bounded three-dimensional joint density is not enough for the indefinite/two-sheet problem; conditional density caps are not independence; a fixed good principal minor cannot be assumed; and a small nonzero coefficient cannot be deleted by an unsupported continuity argument on unbounded inputs.

The incoming account02/B18 r29 state is the exact-rank-three null-hub Schur packet. In its high/moderate-shear branch, either the account03/B18 transverse compiler already pays the form or some ORIGINAL residual coordinate `i` has transverse leverage `q_i>1/2`. The exact determinant ledger from r29 then gives a fixed aggregate hub-triple star but not a fixed large leaf minor. The first debt was to spend that heavy original coordinate without violating provenance.

## 2. Completed e5f theorem actually applied

From the pinned interactive source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`RESULTS.md` / `FOURIER_ROUTE_REPORT.md`, the completed scalar square peel says: if an ORIGINAL physical scalar pivot has coefficient `a!=0`, completing that square gives

`Dens(Q) <= |a|^(-1/2) H_(1/2)(R)`,                              (2.1)

where `R` is the Schur residual and

`H_(1/2)(R)=sup_s E|R-s|^(-1/2)`.

This is used below at a literal inequality. It is not a heuristic stationary-phase step.

The second completed input is the orientation-free theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`,

canonical `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, which states that for a rank-two quadratic form in independent cap-one ORIGINAL coordinates, with arbitrary affine term,

`H_(1/2)(R) <=128 |pdet_2 R|^(-1/4)`.                           (2.2)

The arbitrary-affine clause is important: it permits conditioning or ambient linear terms without silently assuming that the affine part lies in the spectral two-plane.

## 3. New theorem I — every nonzero heavy anchor is a rank-two Schur payment

### `QFORM-HEAVY-ANCHOR-NONZERO-PIVOT-v1`

Let

`A=R M R^T`, `R^T R=I_3`,

be an exact-rank-three physical matrix. Let `u_j` denote the `j`-th row of `R`, put

`D=|det M|=|pdet A|`, `c_i=||u_i||^2`, `a=A_ii=u_i^T M u_i`.

If `a!=0`, then for arbitrary independent cap-one original-coordinate laws,

`boxed: ||p_Q||_infinity <=128 [c_i D |a|]^(-1/4).`              (3.1)

Absolute continuity / essential boundedness follows. Continuity is not asserted by this route.

### Proof

Complete the square in the ORIGINAL coordinate `X_i`. Let

`S=A/A_ii`

be the scalar Schur complement on the remaining physical coordinates. By (2.1),

`||p_Q||_infinity <=|a|^(-1/2) H_(1/2)(S)`.                    (3.2)

The key exact identity is

`boxed: |pdet_2 S|=c_i D/|a|.`                                  (3.3)

For every pair `p<q`, `p,q!=i`, scalar Schur determinant factorization gives

`det A[{i,p,q}] = a det S[{p,q}]`.                              (3.4)

Because `A=RMR^T` has rank three,

`det A[{i,p,q}]=det(M) det(u_i,u_p,u_q)^2`.                     (3.5)

Rotate only the three-dimensional coefficient basis, not the random variables, so that

`u_i=sqrt(c_i)e_1`.

Since `sum_j u_j u_j^T=I_3`, the two transverse components of the remaining rows form a Parseval frame of `R^2`. Cauchy--Binet therefore gives

`sum_(p<q;p,q!=i) det(u_i,u_p,u_q)^2=c_i`.                      (3.6)

The Schur complement has rank exactly two: (3.4)--(3.6) show that its second elementary symmetric function is nonzero. Summing (3.4), using that for rank two the sum of the principal `2x2` minors equals its pseudodeterminant, gives

`a pdet_2(S)=c_i det M`,

hence (3.3). Now apply (2.2):

`H_(1/2)(S)<=128 (c_iD/|a|)^(-1/4)`.                            (3.7)

Substitute (3.7) into (3.2) to obtain (3.1). QED.

### Live heavy-anchor consequence

In the r29 heavy-transverse branch, the anchor satisfies

`c_i>=q_i>1/2`.

For target-normalized exact rank three, `D>=1`. Hence for every fixed `eta>0`,

`|A_ii|>=eta  =>  ||p_Q||_infinity <128 (2/eta)^(1/4).`         (3.8)

Thus the aggregate-star debt is not a problem whenever the heavy original anchor has a genuinely nonzero pivot bounded away from zero. The remaining obstruction is the PUNCTURED near-null collar `0<|A_ii|<<1`; (3.1) deliberately exposes the loss instead of deleting it.

## 4. New theorem II — exact-null rerooting

### `QFORM-NULL-ANCHOR-REROOT-v1`

Retain the exact-rank-three Parseval representation above. Suppose for an ORIGINAL physical coordinate `i`

`A_ii=0`, `c_i=||u_i||^2>0`,

and put `n_i=u_i/sqrt(c_i)`. Suppose every other physical spectral row obeys the rerooted transverse gate

`max_(j!=i) ||P_(n_i^perp)u_j||^2 <=1/2`.                       (4.1)

Then

`boxed: ||p_Q||_infinity <=3*2^(4/3)(c_iD)^(-1/3),`              (4.2)

and `Q` has a continuous density vanishing at infinity.

### Exact rerooting proof

First assume `c_i<1`. The residual covariance is

`G=I_3-u_i u_i^T`.

It is positive definite with eigenvalue `1-c_i` along `n_i` and eigenvalue one on `n_i^perp`. Let

`H=G^(1/2)`, `v_j=H^(-1)u_j` for `j!=i`.

Then

`sum_(j!=i) v_jv_j^T=I_3`.                                      (4.3)

Set

`D_i=H M H`,
`u'=H^(-1)u_i=sqrt(c_i/(1-c_i)) n_i`.

The physical matrix has the exact Schur-isotropic representation with hub `i`

`A=[u',V^T]^T D_i [u',V^T]`,                                    (4.4)

where the residual rows of `V` are the `v_j`. This is an algebraic coefficient-space refactorization of the SAME physical matrix; no random variable is rotated.

Since `A_ii=0`,

`n_i^T D_i n_i=(1-c_i)n_i^T M n_i=0`.                           (4.5)

Because `H^(-1)` is the identity on `n_i^perp`,

`||P_(n_i^perp)v_j||^2=||P_(n_i^perp)u_j||^2`.                  (4.6)

Thus (4.1) is exactly the transverse gate in the compatible designated-partner theorem account03/B18 r28, `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1`. Its determinant currency is

`r_i^2 |det D_i|
 =[c_i/(1-c_i)] [(1-c_i)D]
 =c_iD`.                                                         (4.7)

Applying r28 gives (4.2) and the `C_0` density conclusion.

If `c_i=1`, the residual rows lie in `n_i^perp`, and the completed isometric null-hub theorem account03/B10 r24 applies directly with hub leverage `h=1`, yielding the same formula. QED.

### Heavy-anchor consequence

If `i` is the r29 heavy-transverse anchor, `c_i>=q_i>1/2`. In target normalization `D>=1`; therefore every exact-null heavy anchor satisfying (4.1) obeys

`boxed: ||p_Q||_infinity <3*2^(5/3)
       =9.5244063118092... .}`                                  (4.8)

This is a whole-line estimate, not a one-sheet result.

## 5. Why account03/B18 r30 is not the compatible theorem here

The newest account03/B18 handoff r30 proves an aligned rank-two Schur collar estimate under

`a!=0` and `a!=theta`.

Its conclusion is valuable for nonzero scalar pivots but it literally excludes the exact-null point `a=0`. Therefore this run does NOT apply r30 to (4.1). The newest compatible completed designated-partner result for the exact-null reroot is r28. This is precisely the sort of hypothesis distinction required by the literature-to-proof role.

## 6. New construction — a diffuse-null target family defeating fixed-minor shortcuts

### `QFORM-DIFFUSE-NULL-ANCHOR-STRESS-v1`

For an integer `kappa>=2`, define

`M_kappa=[[0,kappa,0],[kappa,0,0],[0,0,1]]`.                     (6.1)

Its spectrum is

`{-kappa,1,kappa}`,

so every resulting isometric physical realization lies literally in the owner target. Put two ORIGINAL physical spectral rows

`u_0=kappa^(-1)e_1`,

`u_1=(-1/2, 1/(2kappa), 1/sqrt(2))`.                            (6.2)

Both are exact nulls:

`u_0^T M_kappa u_0=0`,
`u_1^T M_kappa u_1=-1/4-1/4+1/2=0`.                            (6.3)

Relative to the first null hub direction `e_1`, coordinate `1` is transverse-heavy:

`q_1=1/2+1/(4kappa^2)>1/2`,
`c_1=3/4+1/(4kappa^2)`.                                         (6.4)

The pair pivot nevertheless degenerates:

`A_01=1/(2kappa)`,
`|det A[{0,1}]|=1/(4kappa^2) ->0`.                              (6.5)

The covariance still required to complete a Parseval frame is

`G_kappa=I-u_0u_0^T-u_1u_1^T`

`=[[3/4-1/kappa^2, 1/(4kappa), sqrt(2)/4],`
`  [1/(4kappa), 1-1/(4kappa^2), -sqrt(2)/(4kappa)],`
`  [sqrt(2)/4, -sqrt(2)/(4kappa), 1/2]].`                       (6.6)

For `kappa>=2` it is positive definite. Its three `2x2` principal minors are respectively

`(3kappa^4-5kappa^2+1)/(4kappa^4)`,
`(kappa^2-2)/(4kappa^2)`,
`(2kappa^2-1)/(4kappa^2)`,

and

`det G_kappa=((kappa^2-kappa-1)(kappa^2+kappa-1))/(4kappa^4)>0`. (6.7)

Let `C_kappa=G_kappa^(1/2)`, with row vectors `c_1',c_2',c_3'`. For an integer `N>=2`, replace each row `c_a'` by `N` copies of

`c_a'/sqrt(N)`.

Together with `u_0,u_1`, these are the rows of a matrix `R_(kappa,N)` satisfying

`R_(kappa,N)^T R_(kappa,N)=I_3`.                                (6.8)

Therefore

`A_(kappa,N)=R_(kappa,N) M_kappa R_(kappa,N)^T`                 (6.9)

has nonzero spectrum EXACTLY

`{-kappa,1,kappa}`.                                              (6.10)

No distributional assumption beyond independent cap-one original inputs is used in constructing the matrix.

### 6.1 Aggregate curvature remains macroscopic while every leaf can vanish

The r29 determinant ledger at hub `0` gives

`sum_(j!=0,1)|det A[{0,1,j}]|
 =|det M_kappa| ||u_0||^2 q_1`
` =kappa^2 * kappa^(-2) * (1/2+1/(4kappa^2))`
` =1/2+1/(4kappa^2)>1/2.`                                      (6.11)

Yet each split residual row carries only `1/N` of its unsplit determinant-square mass, hence

`max_(j!=0,1)|det A[{0,1,j}]| <= q_1/N <1/N`.                  (6.12)

So aggregate fixed-anchor triple curvature does NOT force one uniformly large leaf minor.

The same family can make all simpler local physical pivots tiny. Every split residual row `w` has `||w||^2<=1/N`; therefore

`|A_jj|<=kappa/N`,                                               (6.13)

`|det A[{0,j}]|=A_0j^2<=1/N`,                                  (6.14)

and, because

`||M_kappa u_1||^2=(kappa^2+3)/4`,

`|det A[{1,j}]|=A_1j^2<=(kappa^2+3)/(4N)`.                     (6.15)

For two split residual coordinates,

`|det A[{j,l}]|<=2kappa^2/N^2`.                                (6.16)

Take `N=kappa^4`. As `kappa->infinity`, every physical diagonal, every physical `2x2` principal determinant, and every individual anchored `3x3` leaf minor tends to zero, while (6.11) tends to `1/2` and the physical spectrum continues to contain `{-kappa,1,kappa}`.

This is NOT a counterexample to QFORM. It is a rigorous source-valid counterexample to the shortcut

`macroscopic anchor-star mass => one fixed good physical minor or a nonzero heavy-anchor pivot`.

## 7. Designated partner applied to the stress family

Reroot the exact same physical family at ORIGINAL coordinate `1`. It is null by (6.3). Its leverage is

`c_1=(3kappa^2+1)/(4kappa^2)>3/4`.                              (7.1)

The old hub row `u_0` has rerooted transverse leverage at most

`||u_0||^2=kappa^(-2)<=1/4`.                                   (7.2)

Every split residual row has norm squared at most `1/N<=1/2`, so its transverse leverage is also at most `1/2`. Thus the exact-null reroot theorem (equivalently, account03/B18 r28 after the exact algebra in Section 4) applies. Since

`D=|det M_kappa|=kappa^2`,

`c_1D=(3kappa^2+1)/4`,                                          (7.3)

we obtain the genuine whole-line target estimate

`boxed: ||p_(Q_(kappa,N))||_infinity
 <=3*2^(4/3) [(3kappa^2+1)/4]^(-1/3).}`                         (7.4)

For every `kappa>=2`, this is at most

`5.103484443395882...`,                                         (7.5)

and it decays like `kappa^(-2/3)`. The density is continuous and vanishes at infinity.

Thus the construction simultaneously shows why fixed-minor extraction is invalid and why exact-null rerooting is a useful product-preserving mechanism.

## 8. Primary-source audit

The rank-two half-Riesz report explicitly depends on the sharp Hausdorff--Young theorem of William Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182, and on normalized geometric Brascamp--Lieb.

For the latter, Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 3.3 states the normalized inequality for unit vectors `u_i`, positive weights `c_i` with `sum c_i u_i tensor u_i=I`, and nonnegative integrable one-dimensional functions. Their Theorem 1.1 separately assumes a genuine product `prod f_i` of bounded one-dimensional probability densities and proves

`||pi_E f||_infinity
 <=min{(n/(n-k))^((n-k)/2), 2^(k/2)} prod ||f_i||_infinity^(gamma_i)`,

with `sum gamma_i=k`. Thus cap-one inputs give the exact projection cap `2^(k/2)`. Neither statement supplies independence of projected coordinates. There is no moment, compact-support, log-concavity, smoothness, symmetry, centering or iid hypothesis.

Those are the source-matching inputs used by the completed internal Fourier theorem; no stronger published theorem is imported here.

## 9. Sharpened first unpaid implication

The former broad debt `QFORM-NULLHUB-ANCHOR-STAR-AGGREGATION-v1` is now reduced to a much narrower geometry.

For the heavy ORIGINAL anchor `i` with `q_i>1/2`:

- `|A_ii|>=eta`: paid by (3.8), for every fixed `eta>0`;
- `A_ii=0` and the rerooted transverse frame is diffuse: paid continuously by (4.8);
- exact-null aggregate-star/fixed-minor shortcuts are genuinely insufficient, by Section 6.

Therefore the first local debt is

### `QFORM-HEAVY-ANCHOR-PUNCTURED-NEARNULL-OR-DOUBLEHEAVY-v1`

Obtain a universal endpoint either for

`0<|A_ii|<<1`

without paying a negative power of that scalar pivot, or for the exact-null reroot state in which (4.1) fails and a SECOND original physical row is transverse-heavy relative to `n_i`.

A correct proof must spend the coupled product provenance before conditioning; it cannot pass from the exact-null theorem to the punctured collar by deleting `A_ii`, and it cannot replace the double-heavy source by an arbitrary bounded joint density.

Full exact-rank-three theorem remains OPEN. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.

## 10. Deterministic algebra checks

The stress-family identities were checked symbolically:

- `u_1^T M_kappa u_1=0`;
- `||M_kappa u_1||^2=(kappa^2+3)/4`;
- the three displayed principal minors and determinant of `G_kappa` agree exactly with direct expansion;
- the reroot currency is `c_1|det M_kappa|=(3kappa^2+1)/4`;
- the bound at `kappa=2` is `5.103484443395882...`.

The computation is a regression check only; all arguments above are exact algebra plus completed source-pinned theorems.
