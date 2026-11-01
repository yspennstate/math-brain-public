SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T11:53:28Z.
attacking: the exact two-planar null-sum endpoint: test whether planar density caps alone can pay the third-direction singularity.

# fleet03/B11 r30 — anisotropic planar-cap obstruction at the null-sum endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures; quantitative inequalities and rigorous computations  
**Status:** `REFUTED_INTERMEDIATE_RECEIVER / PROVED_EXPLICIT_COUNTEREXAMPLE / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The full quadratic-form conjecture remains OPEN. This run tests the first unpaid implication left by fleet03/B11 r29, not the conjecture itself.

The r29 addendum proposed the following receiver. Let `(U,Z)` and `(V,W)` be independent planar random vectors with bounded joint densities and consider

`T = beta U^2 + 2 alpha V(Z+W) + 2 gamma U V + delta V^2 + affine`,

with `alpha beta != 0`. The hope was for a dimension-free density bound depending only on the two planar density caps and the determinant-scale parameters such as `|alpha^2 beta|`.

That statement is false even with both planar joint-density caps equal to one, `alpha=beta=1`, and `gamma=delta=0`. The obstruction is anisotropic compression inside each planar bank. This does NOT refute the original QFORM conjecture because the resulting physical four-variable form has only two eigenvalues of magnitude at least one.

No pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea theorem, conditional-density-cap-as-independence step, or fixed-good-minor implication is used below.

## 2. Explicit planar-cap counterexample

Fix `0 < eps <= 1`. Let the two independent planar banks `(U,Z)` and `(V,W)` have densities

`f_eps(u,z) = 1_{|u| <= eps/2} 1_{|z| <= 1/(2 eps)}`,

`g_eps(v,w) = 1_{|v| <= eps/2} 1_{|w| <= 1/(2 eps)}`.

Each support rectangle has area

`eps * (1/eps) = 1`,

so each is a probability density and

`||f_eps||_infinity = ||g_eps||_infinity = 1`.                 (2.1)

Take

`T_eps = U^2 + 2 V(Z+W)`.                                      (2.2)

This is exactly the proposed null-sum normal form with

`alpha = beta = 1`, `gamma = delta = 0`.                       (2.3)

Introduce independent random variables

`A,B,C,D ~ Uniform[-1/2,1/2]`

and write

`U = eps A`, `Z = C/eps`, `V = eps B`, `W = D/eps`.             (2.4)

The two planar changes of variables have determinant one, so (2.1) is unchanged. Equation (2.2) becomes

`T_eps = eps^2 A^2 + 2 B(C+D)`.                                (2.5)

Because the chosen rectangular planar laws are themselves products, `A` is independent of

`Y := 2 B(C+D)`.                                                (2.6)

Thus the density of `T_eps` is the convolution of the square term `eps^2 A^2` with the density of `Y`.

## 3. Exact logarithmic density of the hyperbolic part

Let

`S = C+D`.

Since `C,D` are independent centered unit uniforms, `S` has the triangular density

`h(s) = 1-|s|`, `|s| <= 1`.                                    (3.1)

For `0<|y|<1`, conditioning on `B=b` gives

`p_Y(y)
 = integral_{-1/2}^{1/2} [1/(2|b|)] h(y/(2b))
     1_{|y| <= 2|b|} db`.

By symmetry this equals

`integral_{|y|/2}^{1/2} [1/b] [1-|y|/(2b)] db`

and therefore

`boxed:
 p_Y(y) = log(1/|y|) - 1 + |y|,
 0<|y|<1.`                                                     (3.2)

So the opposite-sign rank-two logarithm is present exactly. The extra square `eps^2 A^2` smooths it only on the collapsing scale `eps^2`.

## 4. Exact output density at zero

For fixed `eps>0`, both summands in (2.5) have `L^1` densities, so their convolution is continuous. In particular its point value at zero is an essential-height lower bound.

Since `Y` is symmetric and `0 <= eps^2 A^2 <= eps^2/4 < 1`, (3.2) gives

`p_{T_eps}(0)
 = E p_Y(-eps^2 A^2)
 = E [log(1/(eps^2 A^2)) - 1 + eps^2 A^2].`                    (4.1)

For `A ~ Uniform[-1/2,1/2]`,

`E A^2 = 1/12`,                                                 (4.2)

and

`E[-log |A|]
 = 2 integral_0^{1/2} -log a da
 = 1 + log 2`.                                                  (4.3)

Substituting (4.2)-(4.3) into (4.1) yields the exact formula

`boxed:
 p_{T_eps}(0)
 = 2 log(1/eps) + 1 + 2 log 2 + eps^2/12.`                      (4.4)

Hence

`boxed:
 ||p_{T_eps}||_infinity >=
 2 log(1/eps) + 1 + 2 log 2 + eps^2/12
 -> infinity as eps downarrow 0.`                               (4.5)

This disproves every proposed bound for (2.2) depending only on fixed values of

`||f_eps||_infinity`, `||g_eps||_infinity`, `|alpha|`, and `|beta|`.

### Theorem 4.1 — `QFORM-TWOPLANAR-JOINTCAP-NULLSUM-FALSE-v1`

There is no finite function `C(M_L,M_R,|alpha|,|beta|)` which bounds the density supremum of

`beta U^2 + 2 alpha V(Z+W)`

for all independent planar banks with joint density caps `M_L,M_R`, even at the fixed parameter point

`M_L=M_R=|alpha|=|beta|=1`.

The family above is an exact counterexample.

## 5. Why this is not a counterexample to the full QFORM conjecture

In the original independent cap-one coordinates `(A,B,C,D)`, (2.5) is the quadratic form

`Q_eps(A,B,C,D) = eps^2 A^2 + 2BC + 2BD`.                       (5.1)

Its symmetric matrix is

`[[eps^2,0,0,0],
  [0,0,1,1],
  [0,1,0,0],
  [0,1,0,0]]`.                                                  (5.2)

The lower `3 x 3` block has eigenvalues `sqrt(2), -sqrt(2), 0`, so the full spectrum is

`{sqrt(2), -sqrt(2), eps^2, 0}`.                                (5.3)

For `eps<1`, only TWO eigenvalues have absolute value at least one. Thus the family exactly reproduces the permitted rank-two logarithmic obstruction rather than violating the three-large-eigenvalue target.

This exposes the missing invariant in the r29 receiver: a bounded planar joint density is unchanged by determinant-one anisotropic maps

`(u,z) -> (eps u, z/eps)`,

but that map can collapse the actual third quadratic eigenvalue from order one to `eps^2`. A correct endpoint theorem must retain enough product-projection geometry to prevent this hidden spectral collapse.

In the r28/r29 application the normalized planar banks arise as genuine two-dimensional orthogonal projections of cap-one product measures, with quantitative bank Gram data `rho,1-rho >= 1/1024`. Those banks carry stronger one-dimensional/X-ray information than an arbitrary planar density cap. That provenance, or an equivalent original-coordinate volume certificate, must enter the null-sum receiver.

## 6. Designated fleet04/B11 partner result applied to an actual inequality

The newest completed fleet04/B11 result is

`QFORM-DISJOINT-VOLUME-COMPILER`,

canonical source `yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`, path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T111608Z-fleet04-B11-disjoint-volume-compiler-r5/REPORT.md`.

For an exact-rank-three factorization `A=RMR^T`, disjoint physical triples `S,T`,

`||p_Q||_infinity <= (3/s) (v_S v_T)^(-1/6)`,                  (6.1)

where `s=min |lambda(M)|` and

`v_S=det(R_S R_S^T)`, `v_T=det(R_T R_T^T)`.

Apply (6.1) to the concrete six-coordinate genuinely indefinite frame

`R = (1/sqrt(2)) [I_3 ; I_3]`,
`M = diag(1,1,-1)`,                                             (6.2)

with `S={1,2,3}`, `T={4,5,6}`. Then `R^T R=I_3`, `s=1`, and

`v_S=v_T=det((1/2)I_3)=1/8`.                                   (6.3)

The corresponding original-coordinate form is

`Q = (1/2)[(X1+X4)^2 + (X2+X5)^2 - (X3+X6)^2]`,                (6.4)

whose nonzero spectrum is exactly `{1,1,-1}`. Substituting (6.3) into (6.1),

`boxed:
 ||p_Q||_infinity
 <= 3 (1/64)^(-1/6)
 = 6.`                                                          (6.5)

This is an actual target-scope inequality using the designated partner's completed result. It also demonstrates the repaired principle: quantitative original-coordinate third volume prevents the anisotropic collapse exploited by Theorem 4.1.

## 7. Third-direction mechanism, corrected

The mandatory rank-two control remains, for independent `X,Y ~ Uniform[-1/2,1/2]`,

`p_{2XY}(t)=log(1/(2|t|))`, `0<|t|<1/2`.                        (7.1)

The counterexample above shows that merely appending a formal square term in arbitrary planar coordinates is not enough: if its physical scale is allowed to collapse through an area-preserving anisotropy, its smoothing window shrinks and the logarithmic height grows like `2 log(1/eps)`.

The useful third direction must therefore be paid in a metric tied to the original product source: a lower singular value/Gram eigenvalue, disjoint triple volume, physical pair determinant plus Schur curvature, or another product-preserving certificate. In the partner example (6.4), both disjoint triple volumes equal `1/8`, and the logarithmic endpoint is uniformly removed with bound `6`.

## 8. Corrected next implication

The r29 proposed receiver should be replaced by the stronger endpoint:

`QFORM-TWOPLANAR-NULLSUM-PRODUCTPROVENANCE-v2`:

> In the exact two-plane r28 geometry, use the actual normalized orthogonal-projection provenance of the two disjoint original-coordinate banks, together with `rho,1-rho >= 1/1024`, to bound the null-sum endpoint `m_22=0`; arbitrary planar joint-density caps alone are insufficient.

Equivalently, prove that this provenance yields either:

1. a quantitative disjoint-volume/pair-area certificate already paid by fleet04/B11 r5 or earlier pair compilers; or
2. an overlap-safe null-sum estimate using the bank's one-dimensional/X-ray projection bounds in addition to its two-dimensional density cap.

The full arbitrary-matrix bridge with extra nonseparable spectrum remains separate. Continuity for the full target also remains open.

## 9. Verification scope

The accompanying checker verifies the exact hyperbolic density formula by symbolic integration, the expectation identities in (4.2)-(4.4), the four-variable spectrum (5.3), and the partner-frame volumes and constant (6.5). These are algebraic checks only; they are not a proof of the full conjecture.

Changed-file fallback privacy review: this run writes only mathematical statements, public-formula constants, repository source pins, and nonsecret operational metadata under the authorized worker paths. No credentials, account secrets, private unrelated data, signed URLs, or machine paths are included. No installation or remote workflow was used.
