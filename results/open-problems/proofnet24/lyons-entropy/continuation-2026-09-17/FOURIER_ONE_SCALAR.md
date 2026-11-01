# One fixed pair mean suffices; the remaining Fourier question is scalar

17 September 2026. **PARTIAL; unrestricted Lyons conjecture OPEN.** This further strengthens the restricted results in `FOURIER_ALL_MEANS.md`. The global three-site quantity `B_Phi` remains UNMEASURED. The scalar introduced here is a separate four-site commuting-family reduction, not a replacement for that frozen milestone. Model and reasoning settings are not independently exposed. No independent audits have occurred.

## 1. A larger complete three-parameter theorem

Keep the notation

    K(a,b,x,y)=F diag(a+x,b+y,a-x,b-y) F*,
    F[j,k]=i^(jk)/2.

**Theorem.** For every fixed `b in [0,1]`, the configuration entropy is jointly concave in the three variables `(a,x,y)` on the entire closed convex domain

    0<=a<=1,
    |x|<=min(a,1-a),
    |y|<=min(b,1-b).

The corresponding statement holds with `a` fixed and `(b,x,y)` varying. In the strict contraction interior, each of these three-variable Hessians is negative definite whenever `x^2+y^2>0`.

Thus fixing both pair means, as in Theorem A of `FOURIER_ALL_MEANS.md`, was unnecessarily restrictive. One pair mean can move freely together with both coupling coordinates. The common-mean theorem and the fixed-diagonal cone theorem remain additional, different affine families.

## 2. Recall the exact curvature identity

Use the six orbit masses `f_0,c_1,P,O,c_3,f_4`, and the count sequences `f,g,h` from `FOURIER_ALL_MEANS.md`. Along a direction

    w=(c,d,u,v)=(a',b',x',y'),
    lambda'=(c+u,d+v,c-u,d-v),

put

    ell=log(O/P),
    alpha_0=log[c_1^2/(f_0 P)],
    alpha_1=log[PO/(c_1c_3)],
    alpha_2=log[c_3^2/(f_4 P)].

The full negative entropy curvature is exactly

    Q[w]=-H''=R[w]+4cd ell,                          (1)

where the quadratic form

    R[w]=I_excess+g_0^2/f_1+g_3^2/f_3
                         +sum_(k=0)^2(Q_k-h_k alpha_k) (2)

is positive semidefinite. This follows from the all-sign local Hillion-Johnson inequality and the exact measured-atom bounds `0<=alpha_k<=L_k`, with `beta_k=L_k-alpha_k>=log 2`. In particular,

    Q_k-h_k alpha_k >= h_k^+ beta_k+h_k^- alpha_k.   (3)

All terms in (1), including the signed atom acceleration, are retained.

For `b` fixed, `d=0`, so (1) immediately proves the interior Hessian inequality. The rest of this note proves strictness and derives the scalar criterion for arbitrary `c,d`.

## 3. The first atom ratio is strictly positive off the decoupled locus

Let `q_i=lambda_i/(1-lambda_i)>0` be the four spectral odds, and set

    X=q_0+q_2, Y=q_1+q_3,
    U=q_0q_2, V=q_1q_3,
    D=product_i(1+q_i), C=XY+2U+2V.

The atom formulas become

    f_0=1/D, c_1=(X+Y)/(4D),
    P=C/(8D), O=XY/(4D).

Therefore

    exp(alpha_0)=(X+Y)^2/(2C),
    (X+Y)^2-2C=(q_0-q_2)^2+(q_1-q_3)^2.           (4)

The scalar odds map is strictly increasing on `(0,1)`. Thus `alpha_0>0` exactly when `x^2+y^2>0`. This proves the strict statement needed below without relying on a generic strictness assertion for a determinant inequality.

For reference, the middle ratio also has a sum-of-squares numerator:

    exp(alpha_1)=CXY/[2(X+Y)(UY+VX)],
    CXY-2(X+Y)(UY+VX)
      =[(X^2-4U)Y^2+(Y^2-4V)X^2]/2.

Occupation complementation gives the corresponding strictness of `alpha_2`. Only (4) is needed for the theorem.

## 4. A coercive bound for the entire positive part R

Write the four eigenvalue slopes as `v_i=lambda_i'` and define

    S=sum_i v_i/(1-lambda_i),
    T=sum_i v_i^2/(1-lambda_i)^2.

Direct differentiation of `f_0=product_i(1-lambda_i)` gives

    g_0=f_0 S,
    h_0=f_0(S^2-T).                                (5)

Since all the other contributions to (2) are nonnegative, (3) implies

    R[w] >= g_0^2/f_1 + (-h_0)^+ alpha_0.

Put

    mu=min(f_0^2/f_1, f_0 alpha_0).

If `S^2<=T`, the displayed bound is

    (f_0^2/f_1)S^2 + f_0 alpha_0(T-S^2) >= mu T.

If `S^2>=T`, the boundary term alone is at least `(f_0^2/f_1)T>=mu T`. Hence, in every direction,

    R[w] >= mu sum_i (lambda_i')^2/(1-lambda_i)^2.  (6)

At a strict contraction with `x^2+y^2>0`, equation (4) gives `mu>0`. The map from `w` to `lambda'` is invertible, so **R is positive definite**. This is a statement about all four parameters, even in the adverse sign cone where the sign of Q remains unresolved.

For a fixed pair mean, the final term of (1) vanishes. Thus (6) proves the strict three-variable assertion. To extend concavity to the full closed domain, contract every eigenvalue toward `1/2` by the same affine factor. The fixed pair mean becomes a fixed strict pair mean for each approximating segment. Integrate the interior Hessian inequality and pass to the original segment by entropy continuity.

The same argument also strengthens Theorem A of `FOURIER_ALL_MEANS.md`: its two-variable Hessian is negative definite for every strict `x^2+y^2>0`, with no imbalance-sign restriction.

## 5. At most one eigenvalue can have the wrong sign

Let bold `R` denote the symmetric 4-by-4 matrix of (2), in coordinate order `(a,b,x,y)`. Equation (1) says that the full negative entropy Hessian matrix is

    Q = R + 2ell(e_a e_b^T+e_b e_a^T).             (7)

At `x^2+y^2>0`, R is positive definite by (6). The correction in (7) has one positive and one negative eigenvalue when `ell!=0`, and is zero when `ell=0`. Adding its positive part to R leaves a positive definite matrix; subtracting its remaining rank-one part can make at most one eigenvalue nonpositive. Thus **Q has at least three strictly positive eigenvalues**.

This conclusion also follows from the positive definite three-variable restrictions established above and eigenvalue interlacing. It is stronger than simply listing nonnegative principal minors without controlling their strictness.

Consequently, throughout this nondegenerate domain,

    Q is positive semidefinite  if and only if det Q>=0.  (8)

In particular a zero determinant is allowed: the other three eigenvalues stay positive.

## 6. An explicit single scalar criterion

Expanding (7) in its two modified entries gives

    Phi_F := det R + 4ell adj(R)_(a,b)
                         -4ell^2 det R_{x,y} = det Q.     (9)

Here `R_{x,y}` is the principal 2-by-2 submatrix on the two coupling coordinates. Thus the full four-eigenvalue Fourier entropy-concavity problem away from `x=y=0` is exactly

    Phi_F(a,b,x,y) >= 0                               (10)

on the complete strict physical domain. Every entry in R is explicit from the six orbit probabilities and the count derivative sequences in (2). An equivalent dimensionless version is

    Phi_F/det R
       =1+4ell(R^(-1))_(a,b)
          -4ell^2[(R^(-1))_(a,a)(R^(-1))_(b,b)
                         -(R^(-1))_(a,b)^2].          (11)

The inverse form is legitimate because R is positive definite. Equations (9) and (11) are the determinant lemma and its complementary-minor form, rather than new estimates. The substantive gain is the strict positivity of the other three eigenvalues, which makes this one determinant sufficient as well as necessary.

At `x=y=0`, the measured kernel is the direct sum, after grouping opposite coordinates, of two identical two-site kernels with eigenvalues `a,b`. The means-only entropy is `2E_2(a,b)`, which is concave. Both coupling first derivatives vanish; (4), its complemented version, and the middle-ratio identity give all three alpha values zero. Equation (1) and the orbit formulas show that the coupling Hessian and mean-coupling cross terms vanish there. Thus the full four-variable Hessian is already nonpositive on this exceptional locus. No inverse R is used there.

## 7. Status

Theorem (1 fixed pair mean), coercivity (6), and the scalar equivalence (8)-(10) are analytic conclusions. They do **not** prove the global sign (10). No certified negative value of the actual Hessian has been found. A proof of (10) would settle the complete four-site Fourier family, still not the full Lyons conjecture or its unrestricted three-site milestone.

The finite polynomial identities behind (4)-(5), and the determinant update identity in (9), are checked exactly in `verify_fourier_scalar.py`. These are self-checks; no independent audit or broad novelty claim is asserted.
