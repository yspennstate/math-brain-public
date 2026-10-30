SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T12:12:07Z.
attacking: the product-provenance exact-null endpoint: isolate a physical source coordinate and pay the remaining rotated hyperbolic plane by the affine half-Riesz theorem.

# fleet03/B11 r31 — exact-null two-plane boundary and physical-pivot compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures; quantitative inequalities and rigorous computations  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and correction boundary

The full conjecture remains OPEN. This run returns to the exact two-plane geometry isolated in fleet03/B11 r29/r30. It does **not** use arbitrary planar joint-density caps as a sufficient invariant; r30 disproved that. It also consumes the live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`: exact zero can be controlled, but a merely small Schur diagonal cannot be treated by a naive perturbation of the half-Riesz endpoint.

The exact-rank-three geometry is

`A = R M R^T`, `R^T R = I_3`, `M=M^T` invertible and indefinite,

with a disjoint original-coordinate partition `S sqcup T` and, in a spectral orthonormal basis,

`G_S := R_S^T R_S = diag(1,rho,0)`,
`G_T := R_T^T R_T = diag(0,1-rho,1)`,                       (1.1)

where `0<rho<1`. Write rows in the two banks as

`r_i=(x_i,y_i,0)` for `i in S`,
`r_j=(0,u_j,v_j)` for `j in T`.                              (1.2)

The null-sum endpoint is

`m_22=0`.                                                     (1.3)

The rank-two affine half-Riesz theorem used below is the source-pinned result

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:

for an orthonormal two-dimensional projection and an invertible symmetric `2x2` quadratic matrix `Lambda`, arbitrary original-coordinate affine terms are allowed and

`sup_t E |q-t|^(-1/2) <= 128 |det Lambda|^(-1/4)`.            (1.4)

The designated fleet04/B11 partner theorem used below is the completed null-scalar theorem in

`yspennstate/math-open-problems@master`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T222040Z-fleet04-B11-cone-envelope-r3/REPORT.md`.

Its quantitative statement is: if `Z` is independent of a planar pair `(V,W)`, `||p_Z||_infinity<=L`, `||p_(V,W)||_infinity<=K`, and

`T=2 alpha ZW + beta V^2 +2 gamma VW + delta W^2 + affine`,

then

`||p_T||_infinity <= 3*2^(2/3) (LK)^(2/3) |alpha|^(-2/3)|beta|^(-1/3)`.  (1.5)

No Gaussianity, moments, support assumptions, post-rotation independence, or pointwise Fresnel decay are used here.

## 2. A scale-sensitive physical-pivot compiler inside the exact-null chamber

Fix `j in T` and write

`r_j=(0,u,v)`, `a=A_jj=r_j^T M r_j`.                           (2.1)

Assume `v != 0` and `a != 0`. Let `I=S union {j}`. Its spectral Gram matrix is

`G_I = G_S + r_j r_j^T`

`= [[1,0,0],[0,rho+u^2,uv],[0,uv,v^2]]`,                      (2.2)

hence

`det G_I = rho v^2`.                                           (2.3)

Because `v!=0`, the principal block `A[I,I]` has exact rank three. Orthogonalize the frame by

`V_I = R_I G_I^(-1/2)`, `M_I=G_I^(1/2) M G_I^(1/2)`.           (2.4)

Then `V_I^T V_I=I_3` and

`det M_I = det G_I det M = rho v^2 det M`.                     (2.5)

The pivot row has leverage exactly one in this orthogonalized block:

`c_j = r_j^T G_I^(-1) r_j = 1`.                               (2.6)

Indeed the lower `2x2` block of `G_I^(-1)` is

`(rho v^2)^(-1) [[v^2,-uv],[-uv,rho+u^2]]`,

and direct substitution gives (2.6).

Now apply the full-ambient rank-three Schur consequence of (1.4). Conditioning on every original coordinate outside `I` creates only affine terms, which (1.4) explicitly allows. Therefore

`boxed:
 ||p_Q||_infinity
 <= 128 [rho v^2 |a| |det M|]^(-1/4).`                         (2.7)

Equivalently, with the physical-pivot certificate

`theta_j := rho v_j^2 |A_jj|`,                                 (2.8)

one has

`||p_Q||_infinity <=128 theta_j^(-1/4)|det M|^(-1/4)`.          (2.9)

If `s=min_k |lambda_k(M)|`, then `|det M|>=s^3`, so

`||p_Q||_infinity <=128 theta_j^(-1/4)s^(-3/4)`.                (2.10)

The reflected statement for a pivot in `S` is obtained by swapping spectral axes `1<->3`, banks `S<->T`, and `rho<->1-rho`.

This is deliberately scale-sensitive. The live correction forbids turning an arbitrarily small nonzero `theta_j` into an exact-zero statement by a naive continuity argument.

## 3. Main new theorem: the exact zero-pivot boundary is uniformly paid

### Theorem 3.1 — `QFORM-EXACT-NULL-ZERO-BANK-SPLIT-v1`

Assume (1.1)-(1.3), and suppose

`A_jj=0 for every j in T`.                                     (3.1)

Then the law of `Q=X^TAX` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity <= 6 e^(2/3) |det M|^(-1/3).`                (3.2)

In particular, if `s=min |lambda(M)|`,

`boxed:
 ||p_Q||_infinity <= 6 e^(2/3)/s
 = 11.6864042464.../s.`                                        (3.3)

The same statement holds if all physical diagonals vanish on `S`, by exchanging the two unique spectral axes.

### Proof

For `j in T`, using `m_22=0`,

`A_jj = r_j^T M r_j
       = v_j(2 m_23 u_j + m_33 v_j)`.                          (3.4)

First `m_23 !=0`. Otherwise (3.1), together with `sum_j v_j^2=1`, forces `m_33=0`; with `m_22=m_23=m_33=0`, the last two rows of `M` are linearly dependent and `det M=0`, contradicting invertibility.

For every row with `v_j!=0`, (3.1) therefore gives

`u_j = -(m_33/(2m_23)) v_j`.                                  (3.5)

But the off-diagonal Gram entry of `G_T` vanishes:

`0=(G_T)_(23)=sum_j u_j v_j`.                                  (3.6)

Rows with `v_j=0` contribute nothing, while `sum_j v_j^2=1`; substituting (3.5) into (3.6) yields

`m_33=0`.                                                       (3.7)

Hence (3.5) sharpens to

`v_j!=0  =>  u_j=0`.                                           (3.8)

Thus the `T` bank splits **in the original product coordinates** into two disjoint subbanks:

`T_2={j:v_j=0}` carrying only the shared `e_2` direction,
`T_3={j:v_j!=0}` carrying only the unique `e_3` direction.     (3.9)

Let

`U = sum_(i in S) x_i X_i`,
`H = sum_(i in S) y_i X_i + sum_(j in T_2) u_j X_j`,
`Z = sum_(j in T_3) v_j X_j`.                                 (3.10)

By the Gram identities,

`||coeff(U)||_2=1`, `||coeff(H)||_2=1`, `coeff(U) perp coeff(H)`,
`||coeff(Z)||_2=1`.                                             (3.11)

Moreover `Z` uses a coordinate set disjoint from the one used by `(U,H)`, so `Z` is genuinely independent of the planar pair `(U,H)`.

The Rogozin-Ball scalar projection theorem gives

`||p_Z||_infinity <= sqrt(2)`.                                 (3.12)

The standard two-dimensional product-projection theorem gives

`||p_(U,H)||_infinity <= e`.                                   (3.13)

Since `m_22=m_33=0`, the quadratic form is exactly

`Q = m_11 U^2 +2m_12 U H +2m_13 UZ +2m_23 HZ`.                 (3.14)

Set

`V=U`, `W=m_13 U + m_23 H`.                                   (3.15)

The linear map `(U,H)->(V,W)` has determinant `m_23`, so

`||p_(V,W)||_infinity <= e/|m_23|`.                            (3.16)

Also

`Q = 2 ZW + beta V^2 +2 gamma VW`,                             (3.17)

where

`beta = m_11 - 2m_12 m_13/m_23`,
`gamma = m_12/m_23`.                                           (3.18)

A direct determinant expansion gives

`det M = -m_23^2 beta`.                                        (3.19)

Since `M` is invertible, `beta!=0`. We may therefore apply the completed fleet04/B11 theorem (1.5) with

`L=sqrt(2)`, `K=e/|m_23|`, `alpha=1`.                          (3.20)

It yields

`||p_Q||_infinity
 <= 3*2^(2/3) (sqrt(2)e/|m_23|)^(2/3)|beta|^(-1/3)`

` = 6 e^(2/3) |m_23|^(-2/3)|beta|^(-1/3)`

` = 6 e^(2/3)|det M|^(-1/3)`,                                 (3.21)

which is (3.2). Finally `|det M|>=s^3` gives (3.3). QED.

### Interpretation

This is the product-provenance fact missing from the arbitrary-planar-cap counterexample of r30. Exact vanishing of every transverse physical pivot does **not** permit an anisotropic hidden collapse: Parseval orthogonality forces the bank to split into two disjoint original-coordinate rulings. That split restores genuine independence between the null scalar `Z` and the transverse pair `(V,W)`, exactly the hypothesis needed by the partner theorem.

## 4. Actual partner inequality on a genuine rotated target instance

The newest completed fleet04/B11 disjoint-volume compiler is

`yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T111608Z-fleet04-B11-disjoint-volume-compiler-r5/REPORT.md`.

For two disjoint physical triples `S_0,T_0`, it gives

`||p_Q||_infinity <= (3/s)(v_(S_0)v_(T_0))^(-1/6)`.            (4.1)

Apply it to the six-row Parseval frame

`r1=r2=(1/sqrt(2),0,0)`,
`r3=r4=(0,1/sqrt(2),0)`,
`r5=r6=(0,0,1/sqrt(2))`,                                      (4.2)

with

`M=[[1,0,0],[0,0,1],[0,1,0]]`.                               (4.3)

Then `spec(M)={1,1,-1}`, the shared `e_2` line is null, and the entire `T={4,5,6}` bank has zero physical diagonal. The corresponding form is

`Q = (X1+X2)^2/2 + (X3+X4)(X5+X6)`.                           (4.4)

Take disjoint triples

`S_0={1,3,5}`, `T_0={2,4,6}`.                                 (4.5)

Each has spectral volume

`v_(S_0)=v_(T_0)=1/8`.                                        (4.6)

Therefore the partner theorem gives the concrete target-scope inequality

`boxed:
 ||p_Q||_infinity <= 3(1/64)^(-1/6)=6.`                        (4.7)

The new zero-bank theorem (3.2) independently gives `<=6e^(2/3)=11.6864...` on the same instance. The disjoint-volume compiler is sharper here; Theorem 3.1 is useful precisely because it does not require two individually large disjoint triples.

## 5. Opposite-sign rank two and the third-direction mechanism

For independent `X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                      (5.1)

so opposite-sign rank two is genuinely unbounded.

At the exact-null three-direction boundary, (3.17) has the canonical form

`2ZW + beta V^2 +2gamma VW`.                                  (5.2)

The partner proof shows exactly what the third direction does. Integrating the independent scalar `Z` alone gives the bad hyperbolic `1/|W|` kernel. The transverse square curvature `beta V^2` changes the near-zero singularity to `|W|^(-1/2)`, which is locally integrable; the far region is paid by the scalar density cap. Optimizing the near/far split produces the determinant-homogeneous exponent `|det M|^(-1/3)`.

The key new structural point is that exact zero physical pivots force original-coordinate bank splitting before this analytic argument is invoked. No spectral rotation is treated as preserving independence.

## 6. What remains

This run resolves the **exact zero-pivot boundary** of the r29/r30 two-plane null-sum chamber and gives the scale-sensitive nonzero-pivot certificate (2.7). It does **not** close the near-zero regime uniformly.

The first remaining implication is:

`QFORM-NEAR-ZERO-PIVOT-BANK-AGGREGATION-v1`:

> In the exact two-plane geometry with `m_22=0`, when the physical-pivot quantities `rho v_j^2|A_jj|` (and their reflected `S`-bank analogues) are all small but not identically zero, aggregate the whole original-coordinate bank into either a paid disjoint-volume/pair-area/ridge certificate or a quantitative product-preserving approximation to the exact split of Theorem 3.1. Do not use the refuted near-zero half-Riesz perturbation shortcut.

Arbitrary additional nonseparable spectrum remains a separate bridge. The theorem above proves an **essentially bounded density** in its stated branch; continuity is **not proved here**.

## 7. Verification and privacy scope

The accompanying checker verifies:

1. the determinant identity `det M=-m_23^2 beta` in the zero-bank normal form;
2. the six-row Parseval Gram identity;
3. the two disjoint triple volumes `1/8`;
4. the partner constant `6` and zero-bank constant `6e^(2/3)`.

The changed-file review is limited to this mathematical report and its deterministic checker/output under the authorized worker path. It contains only source pins, mathematical formulas, constants, and nonsecret operational metadata. No credentials, unrelated private data, machine paths, signed URLs, or public-release action are present. No installation or remote workflow is used.