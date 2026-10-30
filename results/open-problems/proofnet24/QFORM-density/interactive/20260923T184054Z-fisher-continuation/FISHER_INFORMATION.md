# Dimension-free quadratic-form bounds from projected Fisher information

Programme QFORM-DENSITY-3EIG-20260922. Interactive continuation 20260923T184054Z-fisher-continuation. Full unrestricted conjecture: OPEN.

Status: a complete supporting proof is supplied here. Finite symbolic and numerical checks were executed separately; they are not independent proof reviews. The additional information hypothesis must not be removed. This is new work in this continuation, not a claim of literature-wide priority.

## 1. Statement

Let X have independent real coordinates with probability densities f_i and sqrt(f_i) in H^1(R). Put I_i=4 integral |(sqrt(f_i))'|^2=integral_{f_i>0} |f_i'|^2/f_i. Let A be symmetric and let U be an n-by-r orthonormal-column matrix, r>=3, with AU=U Lambda and Lambda diagonal, min_j |lambda_j|>=s>0. Define ell_i=(UU^T)_ii and J_E=sum_i ell_i I_i.

For every b,c, the full form Q=X^TAX+b^TX+c has a bounded density satisfying

    ||p_Q||_infinity <= (r-1) J_E / [2s(r-2)^2].                 (1)

No moments, support bounds, sign condition, rank bound, or constraint on the remaining spectrum is required. A density cap is not needed for (1).

When additionally f_i<=1, write v_r=pi^(r/2)/Gamma(r/2+1), D_r=2r v_r^(2/r)/(r-2), and d_E=min(D_r,J_E/(r-2)^2). Then

    ||p_Q||_infinity <= [r d_E + sqrt(J_E d_E)]/(4s).           (2)

In particular, I_i<=J and s3(A)>0 imply

    ||p_Q||_infinity <= 3J/s3(A),                              (3)

and with the cap-one condition there is also the bound

    ||p_Q||_infinity <= [11.694+1.710 sqrt(J)]/s3(A).           (4)

The constants in (4) are rounded upward. All conclusions include arbitrary affine terms, even outside the range of A.

## 2. Score identity and inverse-distance bound

Write F=prod_i f_i. Since sqrt(f_i) is in H^1, f_i is in W^{1,1}, f_i'=2sqrt(f_i)(sqrt(f_i))', and integral f_i'=0. Define S_i=f_i'/f_i on {f_i>0} and zero elsewhere. Then partial_i F=F S_i, E S_i=0, E S_i^2=I_i, and independence gives

    E |U^T S(X)|^2=J_E.                                      (5)

Set z=U^T x-z0, z0=-(1/2)Lambda^(-1)U^T b, and R=|z(X)|. The projection U^T X is absolutely continuous; in particular P(R=0)=0. For delta>0 let W_delta=Uz/(|z|^2+delta). Direct differentiation gives

    div W_delta = r/(R^2+delta)-2R^2/(R^2+delta)^2
                >=(r-2)/(R^2+delta),
    |W_delta|^2 <=1/(R^2+delta).

Integration by parts and Cauchy--Schwarz therefore imply, for K_delta=E(R^2+delta)^(-1),

    (r-2)K_delta <= -E [z dot U^T S/(R^2+delta)]
                  <=sqrt(J_E K_delta).

Consequently K_delta<=J_E/(r-2)^2. By monotone convergence,

    D:=E R^(-2) <= J_E/(r-2)^2.                              (6)

This is uniform in the center z0. It is a projected Hardy-type estimate, proved directly rather than taken as an unverified regularity assertion about conditional distributions.

For every integration by parts here, insert first a smooth cutoff chi_N supported on the ball of radius 2N, equal to one on the ball of radius N, and with gradient bounded by C/N. For fixed delta the vector fields and their divergences are bounded; the scores are integrable against F. The cutoff error is bounded by C||W_delta||_infinity/N and tends to zero. No moment of X is needed. The product W^{1,1} derivative identity supplies the weak integration by parts even when the densities vanish.

## 3. Inverse spectral vector field and the factor one-half

Define

    V_delta=U Lambda^(-1)z/[2(|z|^2+delta)].

Because AU=U Lambda,

    grad Q dot V_delta=|z|^2/(|z|^2+delta).                    (7)

All other eigenvalues and the affine component orthogonal to E cancel in this identity, without being removed from the actual random quadratic form. Also

    div V_delta=tr[Lambda^(-1)(I-2zz^T/(R^2+delta))]
                              /[2(R^2+delta)].

The matrix in parentheses has operator norm at most one. Thus

    |div V_delta| <= r/(2sR^2),
    |V_delta dot S| <= |U^T S|/(2sR).                         (8)

These are integrable by (5)--(6).

Let psi be a nonnegative smooth compactly supported function, m=integral psi, and Phi(t)=integral_{-infinity}^t psi(u)du-m/2. Then ||Phi||_infinity<=m/2. Integration by parts gives

    E[psi(Q)R^2/(R^2+delta)]
      =-E[Phi(Q)(div V_delta+V_delta dot S)].

For fixed delta the same cutoff argument is valid: the contracted derivative in (7) is bounded, even though the coordinates have no moments. Sending delta to zero gives

    E psi(Q) <= m [rD+sqrt(J_E D)]/(4s).                      (9)

Domination on all such test functions implies domination of the pushforward measure by this multiple of Lebesgue measure. In particular, a density exists and has the stated essential bound. The factor 1/4 in (9) includes the centered-primitive factor 1/2; no density or pointwise coarea formula was assumed in proving it. Substituting (6) yields (1).

A more precise version replaces r/s by T_E=sum_j |lambda_j|^(-1) and J_E/s^2 by J_{E,2}=sum_i I_i |Lambda^(-1)U^T e_i|^2:

    ||p_Q||_infinity <= [T_E D+sqrt(J_{E,2}D)]/4.              (10)

This follows from exactly the same two estimates in (8). One may minimize over admissible invariant subspaces. No coordinate leverage upper bound is required.

## 4. Improvement under the original density cap

The Livshyts--Paouris--Pivovarov marginal-density theorem bounds the density of U^T X by 2^(r/2). When r=n the product bound one is stronger and the same displayed estimate remains valid. Hence P(R<t)<=min(1,2^(r/2)v_r t^r). Layer cake gives

    E R^(-2) <= integral_0^infinity min(1,2^(r/2)v_r u^(-r/2))du
              =r(2^(r/2)v_r)^(2/r)/(r-2)=D_r.                (11)

Use the smaller of (6) and (11) in (9); this proves (2). For r=3, J_E<=3J, D3=6(4pi/3)^(2/3)=15.591108358883012, 3D3/4=11.69333126916226, and sqrt(3D3)/4=1.7097756628547982. This proves (3)--(4).

External input: G. Livshyts, G. Paouris and P. Pivovarov, On sharp bounds for marginal densities of product measures, Israel J. Math. 216 (2016), 877--889, Theorem 1.1, arXiv:1507.07949. The other calculations above are provided in full.

## 5. A non-Gaussian compact-kernel class, including arbitrary heavy-tailed locations

Let g(x)=cos^2(pi x/2) on [-1,1] and zero elsewhere. It has mass one, cap one, sqrt(g) in H^1, and

    I(g)=pi^2 integral_{-1}^1 sin^2(pi x/2)dx=pi^2.

For an arbitrary probability measure nu, f=g*nu has cap one and I(f)<=I(g). Indeed the weak derivative is g'*nu and pointwise Cauchy--Schwarz gives

    |integral g'(x-y)nu(dy)|^2 / integral g(x-y)nu(dy)
      <= integral_{g(x-y)>0} |g'(x-y)|^2/g(x-y) nu(dy).

Integrate and use Tonelli. Membership sqrt(f) in H^1 follows by applying the weak chain rule to sqrt(f+eta) locally, using this uniform derivative bound, and sending eta to zero; the square roots have global squared L2 norm one. No moments or support condition on nu is involved.

Consequently, for independent X_i of densities g*nu_i and every symmetric A with s3(A)>0,

    ||p_(X^TAX+b^TX+c)||_infinity
      <=17.065/s3(A) <18/s3(A).                              (12)

The unrounded constant from (2) is 17.06474993087351. The nu_i may have widely separated atoms, unbounded support, or no finite moments. This class includes g itself, so it is not merely a positive-variance Gaussian-mixture class: such Gaussian mixtures are positive on the entire real line, whereas g is compactly supported.

## 6. Uniformity through the difficult small coupling, inside this class

For orthonormal light statistics L,V,P and an independent original coordinate X_h, consider

    Q_e=2X_h L+V^2+2e L P.

On the span of (X_h,L,V,P), its matrix is

    [[0,1,0,0],[1,0,0,e],[0,0,1,0],[0,e,0,0]].

Its characteristic polynomial is t(t-1)(t^2-1-e^2); thus s3=1 for every real e. Equations (3) and (12) give bounds uniform in e, including e->0. L,V,P are not asserted independent. The original X_i, including the hub, must obey the information hypothesis or compact-kernel hypothesis. Unlike restricted block estimates, Theorem 1 also permits every additional matrix term as long as the actual s3 remains bounded below.

This removes leakage dependence for an additional input class, not for arbitrary rough cap-one inputs.

## 7. The smoothing shortcut still fails

Let u=1_[0,1] and h_delta=u*phi_delta, where phi_delta is the Gaussian density of standard deviation delta. Then h_delta<=1 and h_delta->u in L1. Writing Phi and phi for the standard Gaussian cdf and density,

    h_delta(x)=Phi(x/delta)-Phi((x-1)/delta).

For delta<=1/4 and -delta<=x<=0,

    h_delta'(x)>=[phi(1)-phi(4)]/delta.

Since h_delta<=1,

    I(h_delta)>=integral_{-delta}^0 |h_delta'|^2
                >=[phi(1)-phi(4)]^2/delta ->infinity.          (13)

Thus cap-preserving smooth approximation cannot remove the information hypothesis from the bound just proved. This is an obstruction to a proof interface, not a counterexample to the original conjecture.

For a possible full-target continuation, the divergence part of (8) is already cap-controlled by (11). The remaining question is whether the signed score term E[Phi(Q)(Lambda^(-1)z) dot U^T S/(2(R^2+delta))] admits a uniform bound without replacing it by the diverging information norm. Such cancellation would be a new theorem; it is not assumed here.

## 8. Relation to existing results and review request

The anonymous consolidated manuscript at math commit d2f970d33fa7084f8de55412189402ac609e4da6, directory 20260923T164118Z-full-proof-paper, supplies the earlier semidefinite, Gaussian-mixture, physical-pair, projected-crossing, and rough-law partial results. This continuation retains those results and their exact hypotheses. It adds the argument above rather than presenting the existing 125-page release as newly created in this invocation.

Relevant nearby methods include R. Herry, D. Malicet and G. Poly, Regularity of laws via Dirichlet forms--Application to quadratic forms in independent and identically distributed random variables, arXiv:2303.09488, and M. Aizenman, R. Peled, J. Schenker, M. Shamis and S. Sodin, Matrix regularizing effects of Gaussian perturbations, Comm. Contemp. Math. 19 (2017), 1750028, especially Lemma 2.1. Their assumptions and conclusions should not be identified with the unrestricted bounded-product-density conjecture. No new priority claim is made from a search miss.

Requested existing-worker reviews: fleet02/B02 checks the weak integration by parts, cutoff limits, inverse-distance inequality and density-domination factor; fleet03/B04 checks spectral invariance, constants, the compact-kernel convolution class and the failure of uniform smoothing. These are requests, not completed or independent reviews. Other workers continue their differentiated full-QFORM proof tasks and apply only the scope actually proved. The full rough-input target remains OPEN.
