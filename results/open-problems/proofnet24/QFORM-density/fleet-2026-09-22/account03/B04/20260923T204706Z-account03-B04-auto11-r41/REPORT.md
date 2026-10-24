SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T20:47:06Z.
attacking: a zero-scalar-pivot physical 3x3 receiver by product rearrangement, then the exact residual structure of an unpaid zero-anchor C1 overlap packet.

# account03/B04 r41 — zero-pivot 3x3 product rearrangement and C1 star factorization

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: Product Fourier rearrangement / product-space inequalities.
Status: `NEW SUPPORTING THEOREM + ZERO-PIVOT LOCAL COMPILER + EXACT C1 STRUCTURAL REDUCTION / FULL TARGET OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is **not** proved here. The result below stays in original independent coordinates, permits arbitrary cap-one one-dimensional input densities, and uses no Gaussianity, moments, support connectedness, post-rotation independence, arbitrary-joint coarea, or law-uniform pointwise quadratic-phase decay.

## 1. Fresh source boundary

Fresh owner control remained QFORM-only, revision `2026-09-22.15`, with the full target and full-target continuity still open. The live correction inbox was re-read before publication. In particular this run respects:

- no uniform pointwise van-der-Corput decay over all cap-one densities;
- no independence after diagonalizing a rotated quadratic form;
- no naive fiber-sup integration;
- no inference that one scalar Schur pivot is forced by the three-large-eigenvalue hypothesis;
- the arbitrary-joint rank-three coarea claim is false and is not used.

The completed peer dependency actually used below is the orientation-free rank-two fractional estimate and its scalar-Schur rank-three consequence:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a nonsingular physical `3x3` block `B` and a nonzero physical diagonal pivot `a=B_ii`, its consequence gives

`||p_Q||_infinity <= 128 (|a det B|)^(-1/4)`                                           (1.1)

for the full ambient quadratic form, including arbitrary outside couplings and the induced affine term. The zero-diagonal branch left open by that scalar-pivot mechanism is the first target of this run.

The designated partner `account04/B04` still had no completed current-QFORM canonical report or shared handoff in the fresh lookup, so no designated-partner theorem is fabricated.

## 2. Sharp one-dimensional quadratic pullback rearrangement

### Lemma 2.1 — `QFORM-QUADRATIC-PULLBACK-REARRANGEMENT-v1`

Let `f` be any probability density on the line with `0<=f<=1`. For every real `m,b` and every `a!=0`,

`boxed: integral_R f(m + a y^2 + b y) dy <= 2 |a|^(-1/2).`                         (2.1)

The constant `2` is sharp.

### Proof

Complete the square:

`m+a y^2+b y = m' + a (y-y0)^2`.

Translation of `y` therefore reduces the integral to

`2 integral_0^infinity f(m' + a v^2) dv`.

Set `w=|a|v^2`. Then

`integral_R f(m+a y^2+b y)dy
 = |a|^(-1/2) integral_0^infinity f(m' + sign(a) w) w^(-1/2) dw`.                    (2.2)

The weight `w^(-1/2)` is decreasing. Among all `0<=f<=1` with total mass one, the decreasing-rearrangement / bathtub maximum of the one-sided integral is obtained by putting unit density on the first unit interval in the allowed half-line. Hence

`integral_0^infinity f(m' + sign(a)w) w^(-1/2)dw <= integral_0^1 w^(-1/2)dw=2`.   (2.3)

Equality is attained, for example, by `f=1_[m',m'+1]` when `a>0` and `b=0`. QED.

This is the only rearrangement input in the new local theorem. It is compatible with arbitrary fragmented supports.

## 3. Zero-diagonal physical 3x3 theorem

Let

`B = [[0,c,r],[c,d,b],[r,b,e]]`                                                   (3.1)

be a real symmetric `3x3` matrix with `det B !=0`. Because the first row cannot vanish, after swapping the second and third physical coordinates if necessary we may assume `r!=0`.

Let independent `X,Y,Z` have arbitrary probability densities `f_X,f_Y,f_Z<=1`, and include an arbitrary affine perturbation

`S = [X,Y,Z] B [X,Y,Z]^T + alpha X + beta Y + gamma Z + delta`.                    (3.2)

### Theorem 3.1 — `QFORM-ZEROPIVOT-3X3-PRODUCT-REARRANGEMENT-v1`

`S` has a continuous density vanishing at infinity and

`boxed: ||p_S||_infinity <= 3 * 2^(2/3) * |det B|^(-1/3).`                        (3.3)

No coefficient other than `det B` appears in the final bound.

### Proof

Define the physical linear coordinate

`u = cY + rZ + alpha/2`.                                                          (3.4)

This is **not** a rotation of the random vector. It is only a change of variables inside the density integral. Since `r!=0`,

`z=(u-alpha/2-cy)/r`, `dy dz = |r|^(-1) dy du`.                                  (3.5)

Write the part of (3.2) independent of `X`, after inserting (3.5), as `R_u(y)`. Then

`S = 2u X + R_u(Y)`.                                                             (3.6)

The coefficient of `y^2` in `R_u(y)` is

`kappa = d - 2bc/r + e c^2/r^2
       = - det(B)/r^2`,                                                          (3.7)

because, with `B_11=0`,

`det B = 2bcr - c^2 e - d r^2`.                                                  (3.8)

For `u!=0`, solve (3.6) for `x` at output value `s`:

`x = P_{s,u}(y) := [s-R_u(y)]/(2u)`.                                             (3.9)

The quadratic coefficient of `P_{s,u}` is therefore

`a_u = det(B)/(2 r^2 u)`.                                                        (3.10)

The standard change-of-variables formula gives, for almost every `s`,

`p_S(s)= integral_R [1/(2|r u|)] I_s(u) du`,                                    (3.11)

where

`I_s(u)= integral_R f_Y(y) f_Z((u-alpha/2-cy)/r) f_X(P_{s,u}(y)) dy`.             (3.12)

There are two complementary bounds on `I_s(u)`.

**Mass bound.** Dropping only `f_X<=1`, let `g_U` denote the probability density of `cY+rZ+alpha/2`. Then

`I_s(u) <= |r| g_U(u)`.                                                          (3.13)

Therefore the integrand in (3.11) is at most

`g_U(u)/(2|u|)`.                                                                 (3.14)

**Quadratic-pullback bound.** Dropping only `f_Y,f_Z<=1` and applying Lemma 2.1 to (3.10),

`I_s(u)
 <= 2 |a_u|^(-1/2)
 = 2 sqrt(2) |r| |u|^(1/2) |det B|^(-1/2)`.                                     (3.15)

Thus the integrand in (3.11) is at most

`sqrt(2) |det B|^(-1/2) |u|^(-1/2)`.                                            (3.16)

Combining (3.14)-(3.16), for every `R>0`,

`p_S(s)
 <= integral_{|u|<=R} sqrt(2)|det B|^(-1/2)|u|^(-1/2)du
    + integral_{|u|>R} g_U(u)/(2|u|)du
 <= 4 sqrt(2) |det B|^(-1/2) R^(1/2) + 1/(2R)`.                                 (3.17)

The exact optimizer is

`R_* = 2^(-5/3) |det B|^(1/3)`.                                                  (3.18)

Substitution yields

`4 sqrt(2)|det B|^(-1/2)R_*^(1/2) + 1/(2R_*)
 = 3*2^(2/3)|det B|^(-1/3)`,                                                     (3.19)

which proves the `L^infinity` bound.

### Continuity and `C_0`

The same proof supplies regularity without a Fourier `L^1` claim. For every fixed `u!=0`, the finite measure

`f_Y(y) f_Z((u-alpha/2-cy)/r) dy`

pushed through the nonconstant quadratic `R_u(y)/(2u)` has an `L^1` density, because its quadratic coefficient is nonzero by `det B!=0`. Consequently `I_s(u)` is a translate/correlation of two `L^1` functions and is continuous in `s`, in fact vanishing as `|s|->infinity` for fixed `u`.

The pointwise dominating function

`H(u)=min{g_U(u)/(2|u|), sqrt(2)|det B|^(-1/2)|u|^(-1/2)}`                        (3.20)

is integrable by the same split (3.17). Dominated convergence in (3.11) therefore proves `p_S` is continuous and `p_S(s)->0` as `|s|->infinity`. QED.

## 4. Ambient conditioning theorem

### Corollary 4.1 — `QFORM-ZEROPIVOT-PRINCIPAL3-AMBIENT-v1`

Let `A` be any real symmetric `n x n` matrix. Suppose some three ORIGINAL physical coordinates `I={i,j,k}` have a nonsingular principal block `B=A[I,I]` with at least one zero diagonal entry. Then for every independent cap-one product input,

`boxed: ||p_{X^T A X}||_infinity <= 3*2^(2/3)|det B|^(-1/3).}`                   (4.1)

Moreover the full ambient output has a continuous density vanishing at infinity.

### Proof

Condition on all original coordinates outside `I`. The conditional quadratic in `X_I` has exactly the fixed quadratic block `B`, while every outside coupling becomes an arbitrary affine term and the outside-only part becomes a constant. Theorem 3.1 is uniform in those affine/constant terms. Averaging the conditional densities gives (4.1). Each conditional density is `C_0`, is pointwise bounded by the same constant, and tends to zero at infinity; dominated convergence over the outside conditioning gives continuity and vanishing at infinity for the mixture. QED.

This is a genuine zero-scalar-pivot endpoint. It does not condition on spectral coordinates and does not require a diagonal coefficient to be nonzero.

## 5. Complete nonsingular physical 3x3 compiler at essential-boundedness level

Combine Corollary 4.1 with the completed peer scalar-Schur theorem (1.1).

### Corollary 5.1 — `QFORM-PHYSICAL3-COMPILER-v1`

If an original-coordinate principal `3x3` block `B` is nonsingular, then the full ambient quadratic form has an essentially bounded density. More precisely:

- if `B_ii=0` for at least one physical coordinate `i`, then (4.1) applies and even gives a continuous `C_0` density;
- if no diagonal entry vanishes, then for every `i`

  `||p_Q||_infinity <=128 (|B_ii det B|)^(-1/4)`,                                (5.1)

  and hence one may use the best nonzero diagonal pivot.

This closes the **exact zero-pivot gap for a fixed nonsingular physical triple**. It does **not** furnish a dimension-free lower bound on the determinant of such a triple under the bare spectral hypothesis. The correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` shows that such a uniform extraction is not automatic.

The peer result is therefore applied at an actual inequality, not merely cited: (5.1) is the nonzero-diagonal branch of the new exhaustive local compiler.

## 6. Genuinely rotated indefinite target-valid example

Take

`A_* = [[0,2,1],
        [2,1,3],
        [1,3,-1]].`                                                             (6.1)

All three off-diagonal physical couplings are nonzero, the matrix is not diagonal in the independent coordinates, and it is indefinite. Its exact characteristic polynomial is

`chi(lambda)=lambda^3-15 lambda-15`.                                             (6.2)

Sign checks give

`chi(4)=-11, chi(5)=35`,
`chi(-4)=-19, chi(-3)=3`,
`chi(-2)=7, chi(-1)=-1`.                                                         (6.3)

Hence its three real eigenvalues lie respectively in `(4,5)`, `(-4,-3)`, and `(-2,-1)`. All three therefore have modulus strictly larger than one, so (6.1) satisfies the owner's exact spectral hypothesis.

Also

`det A_*=15`.                                                                    (6.4)

The new theorem yields, for **every** independent cap-one triple,

`boxed:
 ||p_{X^T A_* X}||_infinity
 <= 3*2^(2/3)*15^(-1/3)
 = 1.9309787692112597... .}`                                                      (6.5)

The density is continuous and vanishes at infinity.

For comparison, the completed peer scalar-pivot theorem can use either nonzero diagonal `+1` or `-1`, giving only

`||p||_infinity <=128*15^(-1/4)=65.016...`.                                     (6.6)

Thus the new product rearrangement is not a cosmetic rephrasing of the scalar-pivot branch; on the same target-valid rotated indefinite matrix it improves the explicit constant by more than a factor of thirty while also supplying continuity.

## 7. Exact structure of an unpaid zero-anchor `C_1` packet

This section continues the preceding B04 run's aggregate overlap-one receiver.

Fix a physical coordinate `h` with

`A_hh=0`,                                                                         (7.1)

and write, on the residual coordinates,

`b_i=A_hi`, `C=A_{-h,-h}`.                                                       (7.2)

Assume first that every physical principal triangle through `h` is singular:

`det A[{h,i,j},{h,i,j}]=0` for every distinct `i,j`.                             (7.3)

If some such determinant is nonzero, Corollary 4.1 already pays the full ambient law, so (7.3) is exactly the remaining zero-anchor local obstruction.

Let

`N={i:b_i!=0}`, `Z={i:b_i=0}`.                                                   (7.4)

If `N` is empty then every `C_{1,h}` mixed minor is zero. Assume `N` nonempty.

For `i in N` define

`t_i=C_ii/b_i^2`, `p_i=b_i t_i/2`;                                               (7.5)

for `z in Z` put `p_z=0`.

### Proposition 7.1 — `QFORM-C1-ZEROPIVOT-STAR-FACTOR-v1`

Under (7.1)-(7.3),

`C = b p^T + p b^T + E`,                                                         (7.6)

where

`E_ij=0 for i,j in N`, and `E_ii=0 for every residual i`.                        (7.7)

Consequently the full quadratic dependence on the hub and residual variables factors as

`boxed:
 2 X_h b^T Y + Y^T C Y
 = 2 (b^T Y)(X_h+p^T Y) + Y^T E Y.}`                                             (7.8)

Moreover every overlap-one anchored mixed minor is unchanged if `C` is replaced by `E`: for disjoint two-sets `U,V`,

`boxed:
 det [[0,b_V^T],[b_U,C[U,V]]]
 =det [[0,b_V^T],[b_U,E[U,V]]].}`                                                (7.9)

Hence the entire anchored overlap currency `C_{1,h}` is carried by a residual zero-diagonal matrix `E` with **no `N x N` edges**. Every surviving residual edge touches at least one zero-hub coordinate.

### Proof

For `i,j in N`, expanding (7.3) gives

`0=2 b_i b_j C_ij - b_i^2 C_jj - b_j^2 C_ii`.                                  (7.10)

Divide by `2b_i b_j`:

`C_ij=(b_i b_j/2)(t_i+t_j)=b_i p_j+p_i b_j`.                                   (7.11)

For `z in Z` and any `i in N`, the same principal determinant equals

`-b_i^2 C_zz`,                                                                   (7.12)

so `C_zz=0`. For `i in N`, (7.6) also gives

`E_ii=C_ii-2b_i p_i=0`.                                                         (7.13)

Thus (7.7) holds and (7.8) is immediate.

For (7.9), start with the anchored mixed matrix

`M=[[0,b_V^T],[b_U,C[U,V]]]`.                                                    (7.14)

Using (7.6), for each lower row indexed by `u in U`, subtract `p_u` times the first row. This removes the `p_U b_V^T` part. Then for each right column indexed by `v in V`, subtract `p_v` times the first column. This removes the `b_U p_V^T` part. These determinant-preserving operations leave exactly

`[[0,b_V^T],[b_U,E[U,V]]]`.                                                      (7.15)

QED.

### Meaning for the aggregate `C_1` obstruction

The preceding B04 run showed that a nonzero diagonal anchor plus target-scale `C_{1,h}` is paid by a scalar square plus critical `E_2` collision. Proposition 7.1 now sharpens the complementary exact-zero-anchor state:

1. if any principal physical triangle through the zero anchor is nonsingular, Theorem 3.1 / Corollary 4.1 pays it with a continuous density bound;
2. otherwise the entire anchored overlap packet is forced into the exact factorized ridge form (7.8), and all residual overlap currency comes from edges touching zero-hub coordinates.

This is a genuine reduction of the remaining `C_1` geometry. The still-open implication is to pay (7.8) uniformly when its `E`-part is spread over many zero-hub coordinates or has additional cross-bank leakage; the newer grouped-bank/ridge results may be applicable only after their precise hypotheses are verified.

## 8. Checks and scope

The committed checker verifies:

- `det A_*=15`;
- `chi(lambda)=lambda^3-15lambda-15` and the exact sign brackets proving three eigenvalues with absolute value >1;
- the numerical constant in (6.5);
- symbolic identity `det B=2bcr-c^2e-dr^2` for `B_11=0`;
- symbolic identity `kappa=-det(B)/r^2` used in (3.7);
- the optimizer and exact constant in (3.17)-(3.19);
- symbolic cancellation of the rank-two star term in the anchored mixed determinant under the row/column operations of Proposition 7.1.

No Monte Carlo claim is used.

## 9. What remains open

The full QFORM conjecture remains OPEN. In particular this run does not prove that the three-large-eigenvalue hypothesis yields a target-scale nonsingular physical `3x3` principal block; known correction examples rule out that simple extraction. It also does not yet pay every factorized zero-anchor `C_1` ridge (7.8), especially when the residual `E` carries nonseparable cross-bank curvature.

The next B04 implication is therefore:

`QFORM-C1-STAR-FACTOR-GROUPEDBANK-RECEIVER-v1`: starting from (7.8)-(7.9), either derive a product-Fourier / decreasing-rearrangement bound in terms of the aggregate anchored `C_1` currency, or prove that a large `C_{1,h}` forces one of the already-paid grouped-bank, pair, or ridge endpoints without inverting a vanishing local coefficient.

Full-target continuity remains OPEN, but the new zero-pivot physical-triple branch itself proves a continuous `C_0` density.
