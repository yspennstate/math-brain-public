# account01/B16 — zero-pivot conditional trace and heavy-isotropic exact-rank-three closure

**Run:** `account01-B16-20260922T1705Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh pre-publication control:** `yspennstate/math-research-brain@b434387d05c04e23238e8fc27efa4eb395f75bba`; owner control revision `2026-09-22.8`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREM`; full QFORM target remains **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and live constraints

The full target remains: for every dimension, every independent real input vector `X=(X_1,...,X_n)` whose scalar densities are bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential supremum of the density of `X^T A X`. Continuity is a separate desired conclusion and is not asserted here.

This run preserves the live corrections: no independence is inferred after rotation; a bounded projected density is not by itself substituted for an indefinite level-set integral; no conditional density cap is inferred after a sum/difference transform; and no fixed good principal triple is assumed to follow from the three-large-eigenvalue hypothesis.

Fresh completed dependencies actually used:

1. **Designated partner account02/B16**, run `20260922T163840Z-account02-B16-qform-r13`, canonical mathematics `yspennstate/math-open-problems@d2e3dd1587a3fa93707631ea847c48279f3dc6dc`. Its source-valid triangular representation of a two-dimensional orthogonal projection gives, for a physical projection row of leverage `eta=r^2`, a joint projection-density bound `sqrt(2)/r = sqrt(2) eta^(-1/2)` without claiming independence of the two projected coordinates.
2. **account02/B06**, canonical mathematics `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`: every two-dimensional orthogonal projection of a cap-one product law has joint density at most `e`.
3. **account03/B06**, canonical mathematics `yspennstate/math-open-problems@5aec7529c2a065de05a62a95c6462ce90f12c521`, which identified the heavy isotropic exact-rank-three frontier `ell_i>1/2, A_ii=0` as unpaid. Section 5 below closes precisely that frontier.

## 2. One-dimensional quadratic pullback lemma

### Lemma 2.1

Let `f` be a probability density on `R` with `0<=f<=K`. For every `lambda!=0` and all real `A,mu`,

`int_R f(A-lambda v^2-mu v) dv <= 2 sqrt(K/|lambda|).`             (2.1)

### Proof

Complete the square in `v`; translation does not change the integral, so it is enough to treat `mu=0`. For `lambda>0`, the two branches of `y=A-lambda v^2` give

`int_R f(A-lambda v^2)dv
 =lambda^(-1/2) int_0^infinity f(A-s)s^(-1/2)ds.`

The function `s^(-1/2)` is decreasing. Subject to `0<=f(A-s)<=K` and total mass at most one on this half-line, the integral is maximized by the bathtub profile `K 1_[0,1/K]`. Its value is `2 sqrt(K)`. The case `lambda<0` is identical after reflection. QED.

The mass-one constraint is essential: this is not a pointwise oscillatory estimate.

## 3. Zero-pivot conditional curved-trace theorem

The next theorem is the main new analytic step. Its hypothesis is deliberately **conditional density**, not independence.

### Theorem 3.1 — `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1`

Let `(X,Z_1,Z_2)` be a real random vector. Assume:

- `Z=(Z_1,Z_2)` has a joint density `g` with `||g||_infinity<=M`;
- for almost every `z`, the conditional law of `X|Z=z` has a density bounded by `K`.

Let `B` be a real symmetric nonsingular `3x3` matrix with

`B_11=0`.

For arbitrary affine terms `ell in R^3` and `c in R`, set

`Q=(X,Z)^T B (X,Z)+ell^T(X,Z)+c.`

Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= 3*2^(2/3) (K M)^(2/3) |det B|^(-1/3).
)`                                                               (3.1)

No independence between `Z_1,Z_2` is required.

### Proof

Because `B` is nonsingular, a deterministic translation removes all affine terms. Such a translation preserves the stated joint and conditional density caps. Hence write

`B=[[0,l^T],[l,C]]`, `l=(a,b)!=0`.

Put

`u=a z_1+b z_2`,
`v=-b z_1+a z_2`,
`s=a^2+b^2`.

The change `z -> (u,v)` has determinant `s`, so the joint density `h` of `(u,v)` satisfies

`||h||_infinity<=M/s.`                                           (3.2)

In these coordinates the quadratic polynomial is

`Q=2uX+alpha u^2+2 beta uv+gamma v^2`.                           (3.3)

The transformed quadratic matrix is

`G=[[0,1,0],[1,alpha,beta],[0,beta,gamma]]`,

so `det G=-gamma`. The coordinate change from `(X,u,v)` back to `(X,z)` has determinant `1/s`; therefore

`|gamma|=|det B|/s^2.`                                           (3.4)

For fixed `(u,v)` with `u!=0`, the conditional density of `Q` at `t`, obtained by solving (3.3) for `X`, is bounded by

`K/(2|u|)`.

Let `p_U(u)=int h(u,v)dv`. Splitting the full density integrand at a parameter `R>0` gives two different source-valid estimates.

**Tail `|u|>R`.** Using only the conditional cap,

`int_{|u|>R} ... du
 <= int_{|u|>R} K p_U(u)/(2|u|)du
 <= K/(2R).`                                                     (3.5)

**Core `|u|<=R`.** Using the joint cap (3.2), then Lemma 2.1 with quadratic coefficient `gamma/(2u)`,

`int h(u,v) p_{X|u,v}((t-alpha u^2-2beta uv-gamma v^2)/(2u)) dv /(2|u|)
 <= (M/s) sqrt(2K/|gamma|) |u|^(-1/2).`                         (3.6)

Since `int_{-R}^R |u|^(-1/2)du=4 sqrt(R)`, (3.5)-(3.6) yield

`p_Q(t)
 <= 4 sqrt(2) (M/s) sqrt(K/|gamma|) sqrt(R)+K/(2R).`             (3.7)

Optimizing `A sqrt(R)+D/R` at `R=(2D/A)^(2/3)` gives

`p_Q(t)
 <=3*2^(2/3) (M/s)^(2/3)K^(2/3)|gamma|^(-1/3).`                 (3.8)

Finally (3.4) cancels the coordinate scale exactly:

`(M/s)^(2/3)|gamma|^(-1/3)=M^(2/3)|det B|^(-1/3)`.

This proves (3.1). The set `u=0` is null because `(u,v)` has a density, so the conditional pushforward formula also proves absolute continuity. QED.

### Interpretation

The logarithmic rank-two singularity is regularized by one additional quadratic transverse direction. The proof keeps the product/projection provenance at the point where it is needed: it uses a true conditional cap for the scalar source and a true two-dimensional density cap for the receiver. It does not replace those facts by independence.

## 4. Actual application of designated partner account02/B16

Let `Z` be a two-dimensional orthogonal projection of an independent cap-one physical bank, written in the row notation of account02/B16,

`Z=theta+sum_j b_j X_j`, `sum_j b_j b_j^T=I_2`.

Suppose one physical row has leverage

`eta=|b_i|^2>0`.

The designated partner's exact triangular construction writes `Z=b_i U+cW` with `det(b_i,c)=1`, while

`||p_{U|W=w}||_infinity<=1`,
`||p_W||_infinity<=sqrt(2)/sqrt(eta)`.

Therefore the **joint** density of `(U,W)`, and hence that of `Z` because the last linear map has determinant one, satisfies the actual inequality

`boxed( ||p_Z||_infinity <= sqrt(2) eta^(-1/2). )`                (4.1)

This is a completed partner result being spent directly, not merely cited.

If the scalar variable in Theorem 3.1 has conditional density cap one, (4.1) inserted into (3.1) gives

`boxed(
 ||p_Q||_infinity
 <=6 (eta |det B|)^(-1/3).
)`                                                               (4.2)

For comparison, the leverage-free weighted affine-fiber theorem of account02/B06 gives `M<=e`, hence

`boxed(
 ||p_Q||_infinity
 <=3*2^(2/3)e^(2/3)|det B|^(-1/3)
 <9.276 |det B|^(-1/3).
)`                                                               (4.3)

Thus one may use the better of (4.2) and (4.3). The important point is that projection control is consumed **inside** the nonlinear quadratic integration; a bounded receiver density alone is not asserted to bound an arbitrary indefinite level-set trace.

## 5. Heavy isotropic exact-rank-three branch is closed

This section applies Theorem 3.1 to the precise frontier left open by account03/B06.

### Theorem 5.1 — `QFORM-EXACT-RANK3-HEAVY-ISOTROPIC-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,

have exact rank three, with all three nonzero eigenvalues satisfying `|lambda_j|>=1`. Let `r_i` denote physical row `i` of `R` and

`ell_i=||r_i||^2`.

If

`A_ii=r_i^T Lambda r_i=0`,                                      (5.1)

then for every `ell_i>0`,

`boxed(
 ||p_{X^TAX}||_infinity
 <=3*2^(2/3)e^(2/3)
   (ell_i |det Lambda|)^(-1/3).
)`                                                               (5.2)

In particular, throughout the previously unpaid heavy-isotropic branch `ell_i>1/2`,

`boxed(
 ||p_{X^TAX}||_infinity
 <=6 e^(2/3)
 =11.6864042463... .
)`                                                               (5.3)

The bound allows arbitrary independent cap-one input laws and does not rotate those laws into independent spectral variables.

### Proof

Make only a deterministic orthogonal change of basis in the three-dimensional **spectral coefficient space**, not in the physical random vector, so that

`r_i=sqrt(ell_i) e_1`.

Write the transformed spectral matrix as

`M=[[0,a^T],[a,H]]`,                                             (5.4)

where the upper-left entry is zero by (5.1). Because `M` is nonsingular, `a!=0`.

For the remaining physical rows, the Parseval identity gives

`sum_{k!=i} r_k r_k^T=I_3-ell_i e_1e_1^T.`                     (5.5)

Set `d=sqrt(1-ell_i)` (the case `ell_i=1` is interpreted with the first residual coordinate absent). From (5.5) the residual spectral projection can be written as

`(d W_1,Z_2,Z_3)`,                                               (5.6)

where `(Z_2,Z_3)` is a two-dimensional orthogonal projection of the independent coordinates `X_{k!=i}`. Hence account02/B06 gives

`||p_(Z_2,Z_3)||_infinity<=e.`                                  (5.7)

The full spectral vector is

`Y=(sqrt(ell_i)X_i+dW_1,Z_2,Z_3)`.

Using (5.4), the absence of the first square term gives exactly

`Y^T M Y
 =2 sqrt(ell_i) [X_i+(d/sqrt(ell_i))W_1] a^T Z
  + Z^T H Z,`                                                    (5.8)

where `Z=(Z_2,Z_3)`.

Define

`X'=X_i+(d/sqrt(ell_i))W_1.`

Although `W_1` can be correlated with `Z`, conditional on `Z=z` the variable `X'` is a mixture of translates of the **independent original physical coordinate** `X_i`. Therefore

`||p_{X'|Z=z}||_infinity<=1`                                    (5.9)

for almost every `z`. This is the crucial product-provenance step; no false independence after rotation is used.

Now (5.8) is exactly Theorem 3.1 with the `3x3` coefficient matrix

`B_ell=diag(sqrt(ell_i),1,1) M diag(sqrt(ell_i),1,1)`,

so

`|det B_ell|=ell_i |det M|=ell_i |det Lambda|.`                  (5.10)

Combining (5.7), (5.9), (5.10) and (3.1) proves (5.2). Since `|det Lambda|>=1` and `ell_i>1/2`, (5.3) follows. QED.

### Partner refinement on the transverse projection

If the transverse two-dimensional projection in (5.6) has a physical row of leverage `eta>0`, applying account02/B16's completed triangular projection estimate (4.1) instead of (5.7) gives the sharper companion bound

`boxed(
 ||p_Q||_infinity
 <=6 (ell_i eta |det Lambda|)^(-1/3).
)`                                                               (5.11)

This is the designated partner theorem applied to the exact heavy-isotropic geometry.

## 6. Principal-triple corollary with arbitrary ambient couplings

Let `I={i,j,k}` be three original physical coordinates. Suppose the principal block `B=A_{I,I}` is nonsingular and one of its diagonal entries, say `A_ii`, is zero. Condition on all coordinates outside `I`. The remaining quadratic in `(X_i,X_j,X_k)` has quadratic matrix exactly `B`; all outside cross couplings become affine terms. Since the three physical coordinates are independent and cap one, Theorem 3.1 with `K=M=1` gives

`boxed(
 ||p_{X^TAX}||_infinity
 <=3*2^(2/3)|det A_{I,I}|^(-1/3).
)`                                                               (6.1)

Thus a zero-diagonal nonsingular physical packet can be used inside an arbitrary ambient matrix without discarding outside dependence.

For the pure zero-diagonal triangle

`B=[[0,a,b],[a,0,c],[b,c,0]]`,

`det B=2abc`, and (6.1) becomes

`||p_Q||_infinity <=3*2^(1/3)|abc|^(-1/3).`                      (6.2)

## 7. Exact determinant-mass identity and the remaining implication

For exact rank three, every physical principal triple `I` satisfies

`det A_I=det Lambda (det R_I)^2.`                                (7.1)

Cauchy--Binet with one prescribed row gives the exact volume-sampling identity

`sum_{j<k; j,k!=i} (det R_{ {i,j,k} })^2=ell_i.`                 (7.2)

Consequently

`boxed(
 sum_{j<k; j,k!=i} |det A_{ {i,j,k} }|
 =|det Lambda| ell_i.
)`                                                               (7.3)

When `A_ii=0`, every triple in (7.3) is a zero-pivot packet to which (6.1) applies whenever its determinant is nonzero. For the heavy-isotropic branch the total determinant mass is at least `1/2`.

However, (6.1) pays a reciprocal cube root **after selecting a triple**. The mass in (7.3) can be spread over arbitrarily many triples, so taking the largest individual determinant would reintroduce dimension loss. The direct spectral proof in Section 5 avoids that loss for exact rank three by aggregating the transverse projection before nonlinear integration.

The next first unpaid implication for this B16 route is therefore:

**`QFORM-ZERO-NEAR-ISOTROPIC-HIGHER-RANK-AGGREGATE-v1`** — retain the conditional-cap mechanism of Theorem 3.1 when additional correlated spectral directions are present, or prove an original-coordinate grouped-coordinate reduction that aggregates determinant mass before reciprocal payment. The completed ridge-window theorem pays an important low-leverage spectral-window branch, but the bare three-large-eigenvalue hypothesis does not yet imply the required decomposition.

A natural local next extension is also the near-isotropic case `|A_ii|` small but nonzero: interpolate the zero-pivot trace above with the rank-two affine half-Riesz/nonzero-pivot machinery without a constant blowing up as `A_ii ->0`.

## 8. Status

- New theorem 3.1 is analytic, dimension-free, and keeps conditional product provenance.
- It closes the **entire heavy isotropic exact-rank-three branch** identified by account03/B06, with explicit constant `<11.687`.
- It applies the completed designated partner account02/B16 at the actual inequality (4.2)/(5.11).
- It does **not** prove the full arbitrary-rank QFORM conjecture.
- Continuity is not proved here; only absolute continuity and essential boundedness in the stated branches are established.
