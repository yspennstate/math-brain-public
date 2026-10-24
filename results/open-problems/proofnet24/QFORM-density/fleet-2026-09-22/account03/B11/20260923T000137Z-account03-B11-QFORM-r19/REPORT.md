SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T00:01:37Z.
attacking: small-positive disjoint-Pluecker stability; after reading the new designated-partner result, changed mechanism to close the exact null-coloop stability gap uniformly before returning to near-coloop aggregation.

# account03/B11 QFORM r19 — exact null-coloop branch closes uniformly by the partner null-scalar theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B11` — Indefinite signatures  
Run: `20260923T000137Z-account03-B11-QFORM-r19`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a new product-preserving null-coloop bank theorem for exact-rank-three indefinite forms and, as a strict corollary, removes the logarithmic `D downarrow 0` instability that remained in the completed account04/B19 physical-null-coloop analysis. The proof uses the newest completed designated-partner account04/B11 theorem at an actual inequality.

No step uses post-rotation independence, arbitrary-joint coarea, conditional-density caps as independence, a fiber supremum, pointwise Fresnel decay, moments, compact support, connected support, or deletion of small coefficients.

## 1. Source-pinned completed inputs

### 1.1 Designated partner account04/B11: null-scalar smoothing

Completed source:

`yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.

If `Z` is independent of `(V,W)`, `||p_Z||_infinity<=L`, `(V,W)` has joint-density cap `M_2`, and

`T=2 alpha Z W + beta V^2 + 2 gamma V W + delta W^2 + affine`,

with `alpha beta !=0`, then

`||p_T||_infinity <= 3*2^(2/3)*(L M_2)^(2/3)
                      *|alpha|^(-2/3)|beta|^(-1/3)`.             (1.1)

For the associated symmetric matrix

`H=[[0,0,alpha],[0,beta,gamma],[alpha,gamma,delta]]`,

`det H=-alpha^2 beta`, so (1.1) is determinant-homogeneous. The proof keeps the rank-two saddle singularity honest: the far region costs `r^(-1)`, while transverse square curvature changes the near kernel from `|w|^(-1)` to `|w|^(-1/2)`, yielding `sqrt(r)` and a finite optimized balance.

### 1.2 Product projection bounds before spectral curvature

The completed weighted affine-fiber Brascamp--Lieb theorem is at

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an orthonormal two-dimensional projection of independent cap-one coordinates it gives joint-density cap at most `e`. The completed account03/B19 source also records the one-dimensional Rogozin--Ball product-projection bound `sqrt(2)` for a normalized scalar linear form:

`yspennstate/math-open-problems@39b2d7a6fc503f2abbeee3b50c30ed64886de365`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T223200Z-account03-B19-QFORM-r19/REPORT.md`.

Both estimates are taken before applying the indefinite quadratic pushforward; no independence is asserted after an arbitrary spectral rotation.

### 1.3 The exact physical null-coloop gap to be closed

Completed account04/B19 source:

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

In its exact physical null-coloop residual-diffuse normal form,

`Q=2s X_i Y_1+dY_1^2+2gY_1Y_2+fY_2^2`,                         (1.2)

with `s>=1` and

`det M=-s^2 f`.                                                   (1.3)

That report proved continuous density with a `34 sqrt(log(e/D))` bound when the residual determinant `D>0`, and a uniform bound at `D=0`, leaving uniformity through `D downarrow0` open. Equation (1.2) is exactly within the designated partner's theorem and does not require `D` at all.

## 2. New theorem: a full-leverage null ray can be compressed before the saddle

### Theorem 2.1 — `QFORM-NULL-COLOOP-BANK-CLOSURE-v1`

Let

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

where `M` is real symmetric, invertible and indefinite. Suppose a nonempty bank `H` of ORIGINAL coordinates has collinear spectral rows

`r_i=c_i r`, `i in H`, `||r||=1`,                               (2.2)

along an `M`-null direction

`r^T M r=0`,                                                      (2.3)

and that this bank has full leverage on its projective ray,

`sum_(i in H)c_i^2=1`.                                           (2.4)

For arbitrary independent original-coordinate inputs with densities bounded by one, `Q=X^TAX` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= 6 e^(2/3) |det M|^(-1/3).`           (2.5)

Consequently, if all three nonzero eigenvalues of `M` have magnitude at least `sigma>0`, then

`boxed: ||p_Q||_infinity <= 6 e^(2/3)/sigma <11.687/sigma.`      (2.6)

The theorem holds for both inertia `(2,1)` and `(1,2)`.

### Proof

Define the normalized bank scalar

`Z=sum_(i in H)c_i X_i`.                                         (2.7)

The coefficient vector has Euclidean norm one by (2.4), so the one-dimensional product-projection theorem gives

`||p_Z||_infinity<=sqrt(2)`.                                    (2.8)

The variable `Z` uses only the original coordinates in `H`, hence is independent of all coordinates in `H^c`.

By Parseval,

`sum_i r_i r_i^T=I_3`.                                           (2.9)

The full-leverage condition (2.4) therefore gives

`sum_(j notin H) r_j r_j^T=I_3-r r^T`.                          (2.10)

Taking the quadratic form of (2.10) on `r` yields

`sum_(j notin H) <r_j,r>^2=0`,                                  (2.11)

so every residual row is orthogonal to `r` individually.

Because `M` is invertible and `r` is null, `Mr` is nonzero and orthogonal to `r`. Put

`s=||Mr||>0`, `e_1=Mr/s`,                                       (2.12)

and choose `e_2` so `(r,e_1,e_2)` is orthonormal. Define two residual product projections

`Y_a=sum_(j notin H)<r_j,e_a>X_j`, `a=1,2`.                    (2.13)

Equation (2.10) implies their two coefficient vectors are orthonormal:

`sum_(j notin H)<r_j,e_a><r_j,e_b>=delta_ab`.                   (2.14)

Thus `(Y_1,Y_2)` has joint-density cap at most `e` by the completed two-dimensional product-projection theorem, and it is independent of `Z` because it uses the disjoint original-coordinate bank `H^c`.

In the orthonormal basis `(r,e_1,e_2)`, the spectral matrix has the exact form

`M = [[0,s,0],[s,d,g],[0,g,f]]`.                                (2.15)

Therefore

`Q=2s ZY_1+dY_1^2+2gY_1Y_2+fY_2^2`.                            (2.16)

A direct determinant calculation gives

`det M=-s^2 f`.                                                   (2.17)

Since `M` is invertible, `f!=0`, so the designated partner theorem (1.1) applies with

`alpha=s`, `W=Y_1`, `beta=f`, `V=Y_2`, `L=sqrt(2)`, `M_2=e`.    (2.18)

Hence

`||p_Q||_infinity`
` <=3*2^(2/3)*(sqrt(2)e)^(2/3)|s|^(-2/3)|f|^(-1/3)`
` =6 e^(2/3)|s^2 f|^(-1/3)`
` =6 e^(2/3)|det M|^(-1/3)`,                                    (2.19)

which proves (2.5). If `sigma_min(M)>=sigma`, then `|det M|>=sigma^3`, proving (2.6). Negating `M` exchanges the two indefinite signatures and does not change the bound. QED.

## 3. Stronger singleton corollary: the exact physical null-coloop gap is completely uniform

If the full-leverage null bank consists of one physical coordinate `i`, then `r_i=+/-r` and `Z=+/-X_i`. Its density cap is `L=1`, so the same application of (1.1) improves (2.5) to

`boxed: ||p_Q||_infinity
 <=3(2e)^(2/3)|det M|^(-1/3).`                                  (3.1)

At target scale `sigma_min(M)>=1`,

`boxed: ||p_Q||_infinity <9.276.`                               (3.2)

Apply (3.1) to the exact normal form (1.2) from account04/B19. It gives, for every residual determinant `D>=0`,

`||p_Q||_infinity <=3(2e)^(2/3)|s^2 f|^(-1/3)
                    =3(2e)^(2/3)|det M|^(-1/3)
                    <=9.276`.                                    (3.3)

Thus the previous `34 sqrt(log(e/D))` punctured bound and its discontinuous-looking `D=0` endpoint can be replaced, on the exact physical-null-coloop branch, by one uniform determinant bound independent of `D`. This is a strict target-relevant closure, not a numerical improvement only: the first unpaid `D downarrow0` implication in that branch disappears.

The account04/B19 result separately proves a continuous density throughout the same exact physical-null-coloop branch (`D=0` and `D>0`). Combining that regularity result with (3.3) gives a **continuous density with uniform height <9.276** at target scale for this branch. The grouped-bank theorem 2.1 itself is asserted here only as an essential-density bound; no new universal continuity proof for the grouped bank is claimed.

## 4. Why the third direction removes the rank-two logarithm

For iid `X,Y ~ Uniform[-1/2,1/2]`, the opposite-sign rank-two control

`2XY`

has density

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                         (4.1)

so the logarithmic singularity is real.

In (2.16), if the `fY_2^2` direction is removed, conditioning on `Y_1=w` exposes the same `1/|w|` hyperbolic Jacobian responsible for (4.1). The designated partner theorem shows exactly what the third direction does: transverse square curvature changes the singular near contribution to `|w|^(-1/2)`, which is locally integrable. The determinant identity

`s^2 |f|=|det M|`                                                 (4.2)

then prevents the null coupling `s` and the transverse curvature `f` from degenerating simultaneously. This produces the determinant-homogeneous `|det M|^(-1/3)` bound.

## 5. Scope and remaining implication

This theorem closes a genuine singular branch but not the unrestricted conjecture. It requires a full-leverage null ray, equivalently an exact rank-one null coloop bank. When the null bank has leverage `lambda<1`, the complement still carries an `r` component. Writing that residual component as `U`, the form acquires the extra coupled term `2s UY_1`; the scalar `Z` and the transverse pair can no longer be separated by the same disjoint-bank theorem without a new product-preserving argument.

Thus the next B11 implication is sharpened to:

`QFORM-NEAR-COLOOP-OVERLAP-COMPILER-v1` — for a null ray of leverage `1-epsilon`, control the residual overlapping scalar `U` jointly with the third-direction smoothing, or force an already completed pair/ridge/grouped-bank certificate, without treating small coefficients perturbatively and without replacing product independence by a conditional density cap.

This is also the correct local target for the small-positive disjoint-Pluecker stability problem from r18. Arbitrary additional spectrum remains a separate full-target debt.

**Full QFORM:** OPEN / NOT PROVED.  
**Theorem 2.1:** essential boundedness proved.  
**Physical-null-coloop corollary:** uniform essential bound proved; continuity supplied independently by the completed account04/B19 result.  
**Opposite-sign rank-two logarithmic control:** retained exactly.

## 6. Exact checks

For

`M=[[0,s,0],[s,d,g],[0,g,f]]`,

symbolic expansion gives

`det M=-s^2 f`.

The constants are

`3(2e)^(2/3)=9.275505197173...`,

`6e^(2/3)=11.686404246328...`.

The accompanying checker records `QFORM_B11_NULL_COLOOP_BANK_CLOSURE_CHECK_PASS`.
