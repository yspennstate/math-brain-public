SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T01:32:42Z.
attacking: the zero-diagonal rank-two Schur overlap branch; keep the full square-plus-hyperbola geometry on two product-derived planar banks and aggregate their section weights before any fiber or physical-triple supremum.

# fleet01/B06 r21 — two-bank curved convolution receiver for the overlap branch

**Run:** `20260923T013242Z-qform-r21-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / BALANCED_OVERLAP_BRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope and source-valid premises

The target is unchanged: for independent original real coordinates with one-dimensional probability densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or give a valid target counterexample. The separate continuity request remains open here.


The exact incoming branch is the preceding fleet01/B06 r20 report

`yspennstate/math-open-problems@1d431d262969f767c2bf451f0e7210f41fe42696`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T003549Z-qform-r20-b06/REPORT.md`.

The designated partner result actually used below is fleet02/B06

`QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a two-dimensional orthogonal projection of an original-coordinate cap-one product vector it gives the actual inequality

`||p_Y||_infinity <= e`.                                              (0.1)

The partner's later `QFORM-THIRD-SQUARE-HYPERBOLIC-ABSORPTION-v1`, canonical `math-open-problems@168ac7725f62401408f20ce18cbf8ff7055e9013`, is also consistent with the mechanism below; the new point here is that the square is a **sum of one coordinate from each of two planar product-derived banks**, so the two square coordinates are not separated from the two hyperbolic coordinates by independent banks.

## 1. A geometric kernel lemma

### Lemma 1.1 — hyperbolic half-kernel on finite-measure sets

For measurable sets `E,F subset R` of finite Lebesgue measures and every `t in R`, `d!=0`,

`int_E int_F |t-2 d u v|^(-1/2) dv du
 <= 4 sqrt(2) |d|^(-1/2) |E|^(1/2)|F|^(1/2).`                         (1.1)

### Proof

For fixed `u!=0`, symmetric decreasing rearrangement of the one-dimensional kernel gives

`int_F |t-2duv|^(-1/2) dv
 = |2du|^(-1/2) int_F |v-t/(2du)|^(-1/2)dv
 <= |2du|^(-1/2) 2 sqrt(2|F|)
 = 2 |d|^(-1/2)|u|^(-1/2)|F|^(1/2).`                                 (1.2)

Again by one-dimensional rearrangement,

`int_E |u|^(-1/2)du <=2sqrt(2|E|).`                                   (1.3)

Multiplying (1.2) and (1.3) proves (1.1). The point `u=0` is null. QED.

This lemma is deliberately an **integrated** curved estimate. It never takes the supremum of a hyperbolic fiber.

## 2. Main weighted curved-fiber theorem

Let `(U,Z)` and `(V,W)` be independent random vectors in `R^2`, with probability densities `f` and `g` satisfying

`0<=f<=M_L`, `0<=g<=M_R`.                                             (2.1)

No independence is assumed between `U,Z` or between `V,W`. Let `xi:R^2->R` be any measurable function of `(U,V)`. For `A d !=0`, define

`T=A (Z+W+xi(U,V))^2 + 2 d U V.`                                     (2.2)

### Theorem 2.1 — `QFORM-TWOBANK-CURVED-SQUARE-HYPERBOLA-v1`

The law of `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 4 sqrt(2) sqrt(M_L M_R) / sqrt(|A d|).`                           (2.3)

The theorem allows arbitrary dependence *inside* each planar bank. The only independence used is between the two original product banks that produced the two planar projections.

### Proof

Write the one-dimensional sections

`f_u(z)=f(u,z)`, `g_v(w)=g(v,w)`,

and their masses

`p_U(u)=int f_u(z)dz`, `p_V(v)=int g_v(w)dw`.                         (2.4)

For fixed `(u,v)`, the unnormalised density of `S=Z+W` is

`h_uv(s)=int f_u(z)g_v(s-z)dz`.                                      (2.5)

Two different uses of the probability weight give

`||h_uv||_infinity
 <= M_R p_U(u),`

and

`||h_uv||_infinity
 <= M_L p_V(v).`                                                       (2.6)

Hence

`||h_uv||_infinity
 <= H(u,v):=min(M_R p_U(u), M_L p_V(v)).`                             (2.7)

The measurable shift `xi(u,v)` merely translates `h_uv`, so it does not change (2.7). For fixed `(u,v)`, the map

`s -> A(s+xi(u,v))^2+2duv`

has at most two inverse points. The sum of the reciprocal Jacobians is at most

`1/[sqrt(|A|) sqrt(|t-2duv|)]`.                                      (2.8)

Consequently

`p_T(t)
 <= |A|^(-1/2)
    int_R int_R H(u,v)|t-2duv|^(-1/2) dv du.`                         (2.9)

Now use the exact layer-cake representation

`H(u,v)=int_0^infinity
  1_{M_R p_U(u)>s} 1_{M_L p_V(v)>s} ds.`                             (2.10)

Set

`E_s={u:M_Rp_U(u)>s}`, `F_s={v:M_Lp_V(v)>s}`.                        (2.11)

Applying Lemma 1.1 inside (2.10), then Cauchy--Schwarz in `s`, gives

`int int H(u,v)|t-2duv|^(-1/2)dudv
 <=4sqrt(2)|d|^(-1/2)
   int_0^infinity |E_s|^(1/2)|F_s|^(1/2)ds`

`<=4sqrt(2)|d|^(-1/2)
   [int_0^infinity |E_s|ds]^(1/2)
   [int_0^infinity |F_s|ds]^(1/2).`                                  (2.12)

But layer cake and the fact that `p_U,p_V` are probability densities give

`int_0^infinity |E_s|ds=M_R`,
`int_0^infinity |F_s|ds=M_L`.                                       (2.13)

Substitution into (2.9) proves (2.3). This argument keeps both product weights **inside** the curved reciprocal kernel until after the hyperbolic integration; no fiber maximum appears. QED.

### Structural meaning

A naive square-root kernel estimate would replace a two-dimensional section by its worst fiber and can lose with the number of original coordinates. Here the two section bounds in (2.6) are kept simultaneously via their minimum. The level-set identity (2.10) converts that minimum into a product of two finite-measure sets, and Lemma 1.1 spends the actual hyperbola geometry before Cauchy--Schwarz finally uses only total probability mass. This is precisely an aggregate-before-supremum replacement.

## 3. Exact application to the r20 zero-diagonal rank-two Schur branch

Recall the r20 notation. A physical pivot `i` has `a=A_ii!=0`; its exact rank-two zero-diagonal Schur complement is

`S=sigma(uv^T+vu^T)`,                                               (3.1)

where `u,v` are unit vectors with disjoint physical supports `L,R`. Write

`h=A_{-i,i}=alpha u+beta v+k`, `k in ker S`,                         (3.2)

and decompose

`k=k_L+k_R+k_K`,                                                     (3.3)

with the obvious physical support restrictions. Orthogonality `k perp u,v` implies

`k_L perp u`, `k_R perp v`.                                         (3.4)

Put

`rho^2=a^2+||k||^2`,
`gamma=rho^2/|a|`,
`w=(a,k)/rho`,
`x=||w_L||=||k_L||/rho`,
`y=||w_R||=||k_R||/rho`,
`kappa=||w_{ {i} union K}||^2`.                                     (3.5)

Thus

`x^2+y^2+kappa=1`.                                                   (3.6)

The r20 spectral identity is

`gamma sigma >= s_3(A)^2`.                                          (3.7)

Condition only on the original coordinates `{i} union K`. This preserves independence between the entire original banks `L` and `R`. The remaining quadratic part is exactly

`T=(1/a)(Z_L+Z_R+c)^2+2sigma U V`,                                  (3.8)

where

`U=u^T X_L`, `V=v^T X_R`,
`Z_L=h_L^T X_L=alpha U+k_L^T X_L`,
`Z_R=h_R^T X_R=beta V+k_R^T X_R`,                                  (3.9)

and `c` is fixed by the outside conditioning.

Assume first `m_L:=||k_L||>0` and `m_R:=||k_R||>0`. Let

`p=k_L/m_L`, `q=k_R/m_R`.                                           (3.10)

Then `(u,p)` and `(v,q)` are orthonormal pairs. Applying the designated partner theorem (0.1) gives the **actual inequalities**

`||p_(U,P)||_infinity<=e`, `P=p^TX_L`,
`||p_(V,Q)||_infinity<=e`, `Q=q^TX_R`.                              (3.11)

The shears

`(U,P) -> (U,Z_L=alpha U+m_L P)`,
`(V,Q) -> (V,Z_R=beta V+m_R Q)`                                     (3.12)

have Jacobians `m_L,m_R`. Therefore

`M_L:=||p_(U,Z_L)||_infinity <= e/m_L`,
`M_R:=||p_(V,Z_R)||_infinity <= e/m_R`.                             (3.13)

Theorem 2.1 applied to (3.8), uniformly in the outside conditioning, yields

`||p_Q||_infinity
 <=4sqrt(2)e sqrt(|a|/(sigma m_Lm_R)).`                              (3.14)

Since `m_L=rho x`, `m_R=rho y`,

`sigma m_Lm_R/|a| = gamma sigma x y >= s_3(A)^2 x y`.                (3.15)

Hence the clean invariant estimate

`boxed:
 ||p_Q||_infinity
 <= 4sqrt(2)e / [s_3(A) sqrt(xy)].`                                  (3.16)

This is a genuine full-density bound for this exact branch; it is not merely an `L^3` or half-Riesz statement.

## 4. Quantitative closure of the balanced-overlap survivor

The preceding r20 theorem already pays

`kappa>=1/3`

by

`||p_Q||_infinity <=4sqrt(6)e/s_3(A)<26.634/s_3(A).`                 (4.1)

Suppose now

`kappa<1/3`.                                                         (4.2)

Then `x^2+y^2>2/3`. If in addition

`x^2>=1/6`, `y^2>=1/6`,                                             (4.3)

then `xy>=1/6`; (3.16) gives

`boxed:
 ||p_Q||_infinity
 <=4sqrt(12)e/s_3(A)
 <37.666/s_3(A).`                                                    (4.4)

Under the target normalization `s_3(A)>=1`, this branch is therefore uniformly paid by `37.666`.

Consequently the entire zero-diagonal exact-rank-three Schur endpoint from r20 is reduced to the **one-sided overlap state**: after possibly interchanging `L,R`,

`boxed:
 kappa<1/3,
 x^2<1/6,
 y^2>1/2.`                                                           (4.5)

Indeed `y^2=1-kappa-x^2>1-1/3-1/6=1/2`.

The r20 Pluecker identity simultaneously sharpens from merely `>1/3` aggregate mass to

`sum_{j in L, k<ell in R}
 det F[{j,k,ell},:]^2 = y^2 >1/2.`                                  (4.6)

Thus the remaining obstruction is no longer a generic overlap: **more than half of the effective third-square direction lies on one hyperbolic physical bank, while less than one sixth lies on the other, and the corresponding one-L/two-R Pluecker class carries mass above one half.**

## 5. Exact cross-exterior identity in the overlap state

There is another useful identity which records what the new curved receiver is paying. The physical `L x R` cross block of the full matrix is

`C_LR
 =sigma u v^T +(1/a)h_L h_R^T`.                                  (5.1)

In the orthonormal bases `(u,p)` and `(v,q)`, its two-by-two coefficient matrix is

`[[sigma+alpha beta/a, alpha m_R/a],
  [m_L beta/a,         m_Lm_R/a]].`                                  (5.2)

Therefore

`det = sigma m_Lm_R/a`,                                              (5.3)

and, because the left/right basis maps are isometries,

`boxed:
 Pi_2(C_LR)=sigma m_Lm_R/|a|,
 E_2(C_LR)=sigma^2 m_L^2m_R^2/a^2.`                                 (5.4)

This is exactly the scale appearing in (3.14). It also explains why selecting one physical minor is the wrong operation: the whole exterior mass is the invariant currency, while it may be distributed over arbitrarily many physical pairs.

For comparison, the completed fleet03/B06 `QFORM-EXACT-RANK2-CROSSBANK-L3-v1` gives an `L^3` density bound from this same `Pi_2` currency. Theorem 2.1 is stronger on the present special square-plus-hyperbola geometry because it reaches `L^infinity` directly by retaining the square and hyperbolic curved fibers together rather than first collapsing to a generic rank-two cross-bank law.

## 6. What is still unpaid

The first unpaid implication is now

`QFORM-ZERODIAG-ONE-SIDED-OVERLAP-RECEIVER-v1`:

in the exact rank-three zero-diagonal Schur configuration, assume after swapping banks that

`kappa<1/3`, `||w_L||^2<1/6`, `||w_R||^2>1/2`,

and hence the one-L/two-R Pluecker class has aggregate mass `>1/2`. Consume that strongly one-sided Pluecker packet **before selecting a physical coordinate**, while retaining original product provenance. A valid receiver may use a product-preserving split of the heavy `(w_R,v)` plane, a one-sided half-Riesz/ridge theorem, or a finite-bank compound payment. It may not delete the small nonzero `w_L` component, replace a conditional projection by an unconditional density cap, or invert one tiny physical triple.

This is strictly narrower than the r20 debt: all disjoint-square cases and all genuinely two-sided overlap cases are now paid.

## 7. Status

The full arbitrary-dimensional QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. No target-valid counterexample is produced. The new theorem establishes essential boundedness in the stated two-bank curved branch and closes the balanced-overlap portion of the exact-rank-three zero-diagonal Schur endpoint. The separate continuous-density conclusion is not proved here.

Model self-report: `GPT-5.6 Sol`. Configured thinking level and provider reasoning-token/time counters: `UNKNOWN / NOT_EXPOSED`.
