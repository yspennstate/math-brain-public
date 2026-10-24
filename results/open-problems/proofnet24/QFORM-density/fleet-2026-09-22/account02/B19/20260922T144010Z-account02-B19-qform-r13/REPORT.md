# account02/B19 — universal proof assembly: two-sided scalar-curvature repair of the 2x2 mixed endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T144010Z-account02-B19-qform-r13`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Source-valid conditional assembly

The full target remains open: for arbitrary independent real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`.

The newest designated partner result actually applied is `account03/B19`, canonical package `yspennstate/math-open-problems@a22b97b292c1e3d313e0c8c79edff61d5b0d22cb`. It proves that a counterexample must lie in the residual

`||A-diag(A)||_op > 1/4`, `sr(A-diag(A)) < 32`,

because the near-diagonal branch and the high-stable-rank off-diagonal branch are already paid.

The newest compatible synthesis result actually applied is `account01/B19`, canonical package `yspennstate/math-open-problems@1620f286923bde59e02467ff11ed662d2a18514f`. It proves a one-sided `1 self + 2 cross` theorem: a scalar square plus an invertible physical `2x2` mixed block is enough when the scalar coordinate couples to only one side. Its stated first analytic obstruction is the genuinely two-sided case, where the scalar coordinate couples to both mixed blocks.

The mixed-Hessian input used below is `account03/B09`, canonical package `yspennstate/math-open-problems@446d0a33ef626b11ed5da529f2cec821732e97e9`. For a two-by-two invertible mixed block `C` and arbitrary same-side phases, its Plancherel calculation gives the exact endpoint

`|phi_S(t)| <= min(1, pi |t|^{-1} |det C|^{-1/2})`

for cap-one product blocks. More generally, if the two independent two-dimensional blocks have joint density caps `M_U,M_V`, the same proof gives

`|phi_S(t)| <= min(1, pi |t|^{-1} |det C|^{-1/2} (M_U M_V)^{1/2})`.

This run removes the one-sided coupling restriction whenever the Schur-corrected cross block is nonsingular.

## 2. Main theorem: two-sided Schur-cross repair

### Theorem `QFORM-TWOSIDED-SCHUR-2PLUS1-v1`

Let `X` be a real random variable, and let `U=(U_1,U_2)`, `V=(V_1,V_2)` be real two-dimensional random vectors. Assume `X,U,V` are mutually independent, with

`||p_X||_infinity <= M_X`, `||p_U||_infinity <= M_U`, `||p_V||_infinity <= M_V`.

Let

`T = a X^2 + 2 X (beta + r^T U + s^T V)
     + F(U) + 2 U^T B V + G(V) + c`,

where `a != 0`, `B` is a real `2x2` matrix, `r,s in R^2`, and `F,G` are arbitrary real quadratic-affine functions. Put

`C = B - a^{-1} r s^T`.

If `det C != 0`, then `T` has an essentially bounded density and

`||p_T||_infinity
 <= C_0 M_X (M_U M_V)^{1/4} |a|^{-1/2} |det C|^{-1/4}`,

where

`C_0 = 3 * 2^(1/3) * sqrt(6) < 9.259`.

For five distinct original coordinates with one-dimensional density caps one, `M_X=M_U=M_V=1`, so

`||p_T||_infinity <= C_0 |a|^{-1/2}|det C|^{-1/4}`.       (2.1)

No sign assumption is used. The scalar coordinate may couple to **both** mixed sides.

### Equivalent overlapping-minor form

Define the `3x3` overlapping mixed matrix

`M = [[a, s^T],
      [r, B  ]]`.

By the Schur determinant identity,

`det M = a det(B-a^{-1}rs^T) = a det C`.

Hence in the original cap-one case (2.1) is equivalently

`||p_T||_infinity <= C_0 |a det M|^{-1/4}`.              (2.2)

Thus the paid resource is a scalar curvature together with one nondegenerate **overlapping** three-by-three mixed determinant; it need not be a disjoint three-by-three cross block and it need not obey the one-sided coupling restriction.

## 3. Proof

Write

`L(U,V)=beta+r^T U+s^T V`.

Completing the square only in the original scalar coordinate gives the exact identity

`aX^2+2XL = a(X+L/a)^2 - L^2/a`.

Therefore

`T = a(X+L/a)^2 + S(U,V)`,

where

`S(U,V)=F(U)+G(V)+2U^T C V + (arbitrary same-side quadratic/linear terms) + c'`.

The only cross coefficient changed by the completion is exactly

`B -> C=B-a^{-1}rs^T`.

### Step 1: the Schur residual has a uniform `L^4` density

Let `psi(t)=E exp(itS)`. The mixed-Hessian Plancherel estimate in dimension two gives

`|psi(t)| <= min(1, K/|t|)`,

with

`K = pi |det C|^{-1/2} ||p_U||_2 ||p_V||_2
   <= pi |det C|^{-1/2}(M_U M_V)^{1/2}`.

For exponent `4/3`,

`||psi||_(4/3)^(4/3)
 <= integral_R min(1,(K/|t|)^(4/3)) dt
 = 8K`.

For the Fourier convention `hat f(t)=integral exp(itx)f(x)dx`, inverse Hausdorff--Young gives

`||p_S||_4 <= (2pi)^(-3/4)||psi||_(4/3)`.

Consequently

`||p_S||_4
 <= (2pi)^(-3/4)(8K)^(3/4)
 <= 2^(3/2)(M_U M_V)^(3/8)|det C|^(-3/8)`.       (3.1)

This also proves absolute continuity of `S` at the exact two-cross endpoint, although an `L^infinity` bound for `S` need not hold.

### Step 2: conditional square singularity is only a one-half Riesz kernel

For fixed `u,v`, the shifted variable `X+L(u,v)/a` has density at most `M_X`. Hence the conditional density of

`a(X+L/a)^2`

is bounded pointwise by

`M_X |a|^{-1/2}|y|^{-1/2}`

(on its actual half-line support; the displayed symmetric kernel is merely an upper bound). Averaging over `S` therefore yields, for every `z`,

`p_T(z)
 <= M_X |a|^{-1/2}
    integral_R |z-s|^{-1/2} p_S(s) ds`.                (3.2)

This step does **not** assert independence between the completed square and `S`; it uses only the uniform conditional square-density bound before averaging.

### Step 3: `L^1 cap L^4` controls the half-order singular integral

Set `M=||p_S||_4`. For any `R>0`, split the integral in (3.2):

`integral |z-s|^{-1/2}p_S(s)ds`

`<= M (integral_{|y|<=R}|y|^{-2/3}dy)^(3/4) + R^{-1/2}`

`= 6^(3/4) M R^(1/4) + R^(-1/2)`.

Writing `A=6^(3/4)M`, the minimum of `A R^(1/4)+R^(-1/2)` is

`3 * 2^(-2/3) * sqrt(6) * M^(2/3)`.

Insert (3.1):

`M^(2/3)
 <= 2 (M_U M_V)^(1/4)|det C|^(-1/4)`.

Therefore

`||p_T||_infinity
 <= 3*2^(1/3)*sqrt(6)
    M_X (M_U M_V)^(1/4)
    |a|^(-1/2)|det C|^(-1/4)`.

This is the claimed bound.

## 4. Why this is not the refuted conditional-independence shortcut

The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` forbids replacing genuine independence by a bounded conditional density after a nonlinear/conjugate change of variables. The present proof does nothing of that kind.

- `X`, `U`, and `V` are genuinely independent before any manipulation.
- The two-sided coupling is removed algebraically by completing the square in the **single original scalar coordinate**.
- The remaining `U,V` law is still the original independent block product.
- The completed square is allowed to be dependent on `S`; equation (3.2) uses a pointwise conditional-density bound and then averages.

Thus the argument respects original product provenance throughout.

## 5. Exact target-level example beyond the one-sided theorem

Take five independent admissible coordinates `(x,u_1,u_2,v_1,v_2)` and

`Q = x^2 + 2x u_1 + 2x v_1 + 4u_1v_1 + 2u_2v_2`.

Here

`a=1`, `r=s=(1,0)^T`, `B=diag(2,1)`,

so

`C=B-rs^T=I_2`.

The physical symmetric matrix is

`[[1,1,0,1,0],
  [1,0,0,2,0],
  [0,0,0,0,1],
  [1,2,0,0,0],
  [0,0,1,0,0]]`.

Its characteristic polynomial factors exactly as

`lambda(lambda-3)(lambda-1)(lambda+1)(lambda+2)`,

so it has four eigenvalues of modulus at least one. The scalar coordinate couples to both mixed sides, so the one-sided theorem does not apply. The present theorem gives for **every** admissible product input law

`||p_Q||_infinity <= C_0 < 9.259`.

This is a literal target-class example, not a diagonal or post-rotation special case.

## 6. Application to the current proof architecture

The designated partner `account03/B19` reduces every hypothetical counterexample to the low-stable-rank off-diagonal regime. The newest `account01/B19` synthesis result had left the two-sided `1 self + 2 cross` endpoint as an analytic obstruction. The theorem above closes that endpoint whenever the Schur-corrected two-cross packet remains nonsingular.

The remaining obstruction is therefore no longer “two-sided scalar coupling” by itself. It is the **structural Schur-cancellation / aggregate extraction problem**: the full spectral hypotheses must force a product-compatible packet with a quantitatively nonnegligible overlapping determinant, or route the matrix to one of the already-paid diffuse/localized/regularized-determinant/hyperbolic-square branches.

### First unpaid implication, with exact quantifiers

`QFORM-SCHUR-MIXED-OR-AGGREGATE-v1` (OPEN): prove that there exist universal constants `c_0>0` and `M_0<infinity` such that every target matrix in the residual

`||A-diag(A)||_op > 1/4`, `sr(A-diag(A)) < 32`,

unless already covered by a source-valid near-diagonal, diffuse-range, localized diffuse-Schur, regularized-determinant, or hyperbolic-square theorem, admits one of the following:

1. five disjoint original coordinates `(x,I,J)`, `|I|=|J|=2`, for which `a=A_xx !=0` and
   `|a det A[{x} union I,{x} union J]| >= c_0`; or
2. three mutually independent original-coordinate banks producing a scalar block and two two-dimensional aggregate blocks with joint density caps at most `M_0`, for which the same Schur-corrected determinant resource is at least `c_0`; or
3. a quantitative descent to one of the already-paid branches.

By the theorem above, alternatives 1 and 2 immediately give a universal density bound. The missing work is purely structural/aggregate: it must rule out persistent near-singularity of every product-compatible Schur-corrected mixed packet without selecting and inverting one diffuse tiny minor.

This is narrower than the preceding `two-heavy + one-diffuse` formulation: two-sided scalar coupling itself is now paid; only Schur cancellation and aggregate resource extraction remain.

## 7. Status and nonclaims

**Proved here:** `QFORM-TWOSIDED-SCHUR-2PLUS1-v1`, including a block-density extension and a concrete target-class example.

**Applied peer result:** newest designated partner `account03/B19` low-stable-rank off-diagonal reduction; newest compatible `account01/B19` one-sided mixed endpoint; `account03/B09` exact two-cross Plancherel estimate.

**Not proved:** the structural extraction implication in Section 6, the full low-stable-rank residual, the full arbitrary-matrix theorem, or a universal continuous representative in every branch.

No full-proof claim is made.

## 8. Correction discipline

Consumed and respected live corrections include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

No refuted interface is used as a premise.
