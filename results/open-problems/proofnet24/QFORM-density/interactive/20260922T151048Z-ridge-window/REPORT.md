# Quadratic-form densities from ridge leverage and a spectral window

Programme: QFORM-DENSITY-3EIG-20260922. Interactive record: 20260922T151048Z-ridge-window.

**Status:** complete analytic arguments for the supporting theorems below; independent end-to-end review pending. The unrestricted three-large-eigenvalue conjecture remains unproved. No literature-wide novelty claim is made.

## 1. Exact advance and remaining scope

The original target assumes independent real coordinates with probability densities bounded by one and a symmetric matrix with at least three eigenvalues of absolute value at least one. It asks for a single dimension-independent density bound, without sign, moment, regularity or support assumptions.

The previous regularized-determinant argument required a leverage bound on the entire range of a cross block. Its spectral application required the entire range of A to be diffuse, excluding every invertible A. Here the regularization scale is left free and then made frequency-dependent. The resulting criterion requires only a bound on a ridge projection at ONE fixed spectral scale. It can apply to a full-rank cross block whose ordinary range projection is the identity.

The application is the following theorem. Let P be the spectral projection of A onto the eigenspaces with |lambda| >= 1/64. If A satisfies the original three-large-eigenvalue condition and every P_ii <= 1/32, then X^T A X has a continuous density vanishing at infinity and

    ||p||_infinity <= 288 sqrt(3e)/13 < 64.

The remaining eigenvalues can be arbitrarily numerous, nonzero, small and of either sign, with arbitrary eigenvectors. In particular this includes full-rank indefinite matrices and genuinely nonseparable small perturbations. The spectral-window leverage assumption is additional and is NOT implied by the original conjecture. Thus this is not the full solution.

## 2. Sources and conventions

Use hat f(s) = integral exp(isx) f(x) dx. All matrix norms below are Euclidean operator norms; logarithms are natural. I denotes an identity of the required size when used in a matrix expression.

Classical analytic inputs:

1. W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159-182, DOI 10.2307/1970980. Sharp Hausdorff-Young and sharp Young convolution inequalities. Publisher: https://annals.math.princeton.edu/1975/102-1/p11 . For 1 <= p <= 2, p'=p/(p-1),

       ||hat f||_(p') <= (2pi)^(1/p') C_p ||f||_p,
       C_p = p^(1/(2p)) / (p')^(1/(2p')).

   For 1/p+1/q=1+1/r, sharp Young is ||f*g||_r <= (C_p C_q/C_r)||f||_p||g||_q. Endpoint constants are interpreted by limits.

2. Rank-one geometric Brascamp-Lieb: for unit vectors v_j and positive weights c_j with sum c_j v_j v_j^T=I,

       integral prod F_j(v_j dot z)^(c_j) dz <= prod (integral F_j)^(c_j).

   The normalized statement used here is Theorem 3.3 in G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, https://arxiv.org/pdf/1507.07949 .

3. A. W. Marcus, D. A. Spielman and N. Srivastava, *Interlacing families II: Mixed characteristic polynomials and the Kadison-Singer problem*, Annals of Mathematics 182 (2015), 327-350, Corollary 1.5, https://arxiv.org/pdf/1306.3969 . Its two-part frame-partition statement is specified in Section 7. This is a published input, not a theorem proved by this project.

The starting graph argument is in the private archive at yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a, path proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md, blob 080253f929411bfa9c7aa3254a2bdaf37be72ebb. Its Sections 3-6 have a passing scoped review recorded by account02/B02 at brain handoff 20260922T140817Z-account02-B02-qform-r11.md, blob 72a94fec2ea0dd275892cfd62267b7e6d4225e18. That review is not a review of this extension. All steps needed here are supplied below.

## 3. Scalar estimates

Let f be a probability density, 0 <= f <= 1. Then ||f||_p <= 1 for every p >= 1. If g=f*tilde(f), with tilde(f)(x)=f(-x), then for 0<c<=1, sharp Young with inputs p=2/(1+c) and output r=1/c gives

    ||g||_(1/c) <= 2^c c^(c/2) (1+c)^(-(1+c)/2).               (3.1)

This follows by substituting in C_p^2/C_r. It includes c=1, where both sides equal one as an upper bound.

For 1<=q<=2 and 0<d<=q/2, put h=|hat f|^q. Sharp Hausdorff-Young at Fourier exponent q/d>=2 gives

    ||h||_(1/d) <= (2pi)^d q^(q/2-d)
                       (q-d)^(-(q-d)/2) d^(d/2).              (3.2)

Indeed the conjugate input exponent is q/(q-d) in [1,2], and raising Hausdorff-Young to the qth power gives exactly (3.2). This explicitly explains why d<=q/2 is required.

Define G(c)=2^c(1+c)^(-(1+c)/2) and H_q(d)=q^(q/2-d)(q-d)^(-(q-d)/2). Their logarithms are concave, with second derivatives -1/[2(1+c)] and -1/[2(q-d)], respectively. Taking the tangent to log G at c=1 and the tangent to log H_q at d=0 yields

    log G(c) <= (1-log 2)(1-c)/2,
    log H_q(d) <= (1-log q)d/2.                               (3.3)

Both follow directly from the displayed derivatives and endpoint values log G(1)=log H_q(0)=0.

## 4. A graph inequality with a free regularizer

Let R be a real m-by-k matrix with columns r_j. Let D_i be independent differences of two independent copies of real variables with probability densities bounded by one, so their densities g_i satisfy (3.1). Let f_j be any further one-dimensional probability densities bounded by one; the two lists need not have the same laws.

Fix alpha>0, a real a, and q in [1,2]. Define

    M = alpha I_m + a^2 R R^T,
    c_i = alpha e_i^T M^(-1)e_i,
    d_j = a^2 r_j^T M^(-1)r_j,
    theta = sum_j d_j = sum_i (1-c_i),
    L_q = pi e sqrt(2/q).

Assume d_j<=q/2 for every j. Then

    E prod_j |hat f_j(a r_j dot D)|^q
      <= det(I_m+a^2RR^T/alpha)^(-1/2)
                  (L_q/sqrt(alpha))^theta.                   (4.1)

Unlike the earlier fixed-regularizer estimate, alpha is arbitrary: the multiplier on the right must be retained, even when it exceeds one.

### Proof

If a=0, the left side equals one and theta=0, so the assertion holds. For a!=0, put

    v_i=sqrt(alpha) M^(-1/2)e_i,   w_j=a M^(-1/2)r_j.

Their outer products sum to I_m; their squared lengths are c_i and d_j. In particular 0<c_i<=1 and 0<=d_j<=1. Ignore zero w_j, whose Fourier factors are one.

After the change of variables x=M^(-1/2)z, normalize each nonzero vector to unit length and apply geometric Brascamp-Lieb to g_i and h_j=|hat f_j|^q, with the powers absorbed into the scalar functions. The resulting bound is

    det(M)^(-1/2)
      prod_i [alpha^(c_i/2)c_i^(-c_i/2)||g_i||_(1/c_i)]
      prod_j [d_j^(-d_j/2)||h_j||_(1/d_j)].                    (4.2)

For example, the g_i argument is sqrt(c_i/alpha) times a unit linear form; its scalar change of variables contributes alpha^(c_i/2)c_i^(-c_i/2). This scale factor is essential.

Substitution of (3.1)-(3.2) cancels the c_i and d_j powers in (4.2). Since sum_i c_i=m-theta, the remaining expression is

    det(M)^(-1/2) alpha^((m-theta)/2) (2pi)^theta
                    prod_i G(c_i) prod_j H_q(d_j).

By (3.3), the last product is at most exp([1-log(2q)/2]theta). Factor alpha^m from det M. The remaining scalar multiplier is

    [2pi exp(1-log(2q)/2)/sqrt(alpha)]^theta
      = (L_q/sqrt(alpha))^theta.

This proves (4.1). All scalar integrals needed for Brascamp-Lieb are finite by (3.1)-(3.2). No smoothness, moment or support condition is used. QED.

## 5. Ridge-leverage density criterion for arbitrary cross blocks

Let I,J be disjoint sets of ORIGINAL coordinates of the quadratic form, and put B=A[I,J]. Fix gamma>0 and define the positive semidefinite ridge operator on R^I

    K_gamma = BB^T (gamma^2 I+BB^T)^(-1),
    theta_gamma = tr K_gamma,
    D_gamma = det(I+BB^T/gamma^2).

Suppose, for some q in [1,2],

    max_i (K_gamma)_ii <= q/2,     theta_gamma > 2q.           (5.1)

Then Q=X^TAX has a bounded continuous density vanishing at infinity, and

    ||p_Q||_infinity
      <= e/[sqrt(2q) gamma] * theta_gamma/(theta_gamma-2q)
                                      * D_gamma^(-1/(2theta_gamma))
      <= sqrt(e)/[sqrt(2q) gamma]
                                      * theta_gamma/(theta_gamma-2q). (5.2)

All self blocks, outside coordinates and outside couplings are unrestricted. The same statement holds after adding any sum of real measurable coordinate-separable terms, finite almost surely. One can interchange I and J to use the other side's ridge leverage.

### Proof

Condition on all original coordinates outside I union J. The remaining law is still a product law with its original caps. The conditional form is

    q_I(X_I)+q_J(X_J)+2 X_I^T B X_J+c.

The self functions may in fact be arbitrary real measurable functions, finite almost surely; induced linear terms and separable perturbations are included in them.

Let Y,Y' be independent copies of X_J. Cauchy-Schwarz in the law of X_I, expansion of the square, and the triangle inequality give

    |phi(t)|^2 <= E_(Y,Y') prod_(i in I)
                      |hat f_i(2t[B(Y-Y')]_i)|.

Jensen for q>=1 therefore gives

    |phi(t)|^(2q) <= E_(Y,Y') prod_(i in I)
                      |hat f_i(2t[B(Y-Y')]_i)|^q.             (5.3)

For each t!=0, apply (4.1) with R=B^T, a=2t and

    alpha=(2gamma|t|)^2.

The graph weights d_i are now exactly (K_gamma)_ii, independent of t, and their sum is theta_gamma. Thus (5.1) makes the graph bound admissible at every nonzero frequency. Taking the (2q)th root in (5.3) gives

    |phi(t)| <= D_gamma^(-1/(4q))
              [L_q/(2gamma|t|)]^(theta_gamma/(2q)).           (5.4)

The bound is uniform in all outside conditioning values, hence also bounds the unconditional characteristic function. Combine it with |phi(t)|<=1. Set

    beta=theta_gamma/(2q)>1,
    t_0=L_q/(2gamma) * D_gamma^(-1/(2theta_gamma)).

Then |phi(t)|<=min(1,(t_0/|t|)^beta), whose integral is

    2t_0 beta/(beta-1)=2t_0 theta_gamma/(theta_gamma-2q).

Fourier inversion gives a continuous C_0 density and the first inequality in (5.2), because L_q/(2pi)=e/sqrt(2q).

For the second, if x_j=s_j(B)^2/gamma^2, then theta_gamma=sum x_j/(1+x_j) and log D_gamma=sum log(1+x_j). The elementary inequality

    log(1+x) >= x/(1+x),  x>=0,

has zero difference at x=0 and derivative x/(1+x)^2. Therefore log D_gamma>=theta_gamma, so D_gamma^(-1/(2theta_gamma))<=e^(-1/2). This proves (5.2). QED.

The strict condition theta_gamma>2q is essential for this Fourier argument. At equality its envelope has a nonintegrable |t|^(-1) tail; no endpoint density theorem follows from this proof.

### Three substantial cross singular values

If B has at least three singular values >=sigma>0, set gamma=sigma/sqrt(6). Then

    theta_gamma >= 3 sigma^2/(gamma^2+sigma^2)=18/7.

If also max_i (K_gamma)_ii<=1/2, use q=1 in (5.2). Since theta/(theta-2) decreases for theta>2,

    ||p_Q||_infinity <= 9 sqrt(3e)/(2sigma).                  (5.5)

There is no cost depending on the number or minimum size of the other singular values. For a full-rank B its ordinary range leverage can be one, while (5.1) still holds.

## 6. Stability of ridge leverage under a small nonseparable perturbation

Let B=B_0+F, ||F||<=eta, and let S=range(B_0). Suppose the diagonal of its orthogonal projection satisfies (P_S)_ii<=ell. Then for every gamma>0,

    (K_gamma)_ii <= [sqrt(ell)+eta/gamma]^2.                 (6.1)

A slightly sharper coordinate-specific upper bound is

    [sqrt((P_S)_ii)+(eta/gamma)sqrt(1-(P_S)_ii)]^2.

### Proof

The identity

    K_gamma=B(gamma^2 I+B^TB)^(-1)B^T

shows 0<=K_gamma<=I. If v is perpendicular to S, B_0^Tv=0 and therefore

    v^T K_gamma v
      = ||(gamma^2 I+B^TB)^(-1/2) B^T v||^2
      <= (eta/gamma)^2 ||v||^2.

Decompose e_i=P_S e_i+(I-P_S)e_i and use the triangle inequality after applying K_gamma^(1/2). Contractivity on the first component and the preceding bound on the second give the sharper estimate and hence (6.1). QED.

This is an operator-norm perturbation argument, not an assumption that the perturbing quadratic form is independent noise.

## 7. Spectral-window theorem, including full-rank matrices

### Theorem

Let A be symmetric with at least three eigenvalues of magnitude at least one. Let P be the spectral projection onto the sum of all eigenspaces with |lambda|>=1/64. Assume

    max_i P_ii <= 1/32.                                    (7.1)

For all independent real X_i with probability densities bounded by one, Q=X^TAX has a continuous C_0 density with

    ||p_Q||_infinity <= 288 sqrt(3e)/13 <64.                 (7.2)

Arbitrary coordinate-separable measurable real perturbations, finite almost surely, are allowed as well.

### Proof

Write A=A_H+E, where A_H=U Lambda_H U^T is the spectral truncation onto P and U has orthonormal columns. Then ||E||<=eta=1/64, every row u_i of U has squared norm at most 1/32, and Lambda_H is invertible with at least three singular values >=1.

The two-part case of MSS Corollary 1.5 says that a tight frame sum u_i u_i^T=I with ||u_i||^2<=epsilon admits a partition I,J whose two partial frame sums have norm at most (1/sqrt(2)+sqrt(epsilon))^2. With epsilon=1/32 this upper bound is 25/32. Since the sums add to I, both Gram matrices satisfy

    delta I <= M_I=U_I^TU_I, M_J=U_J^TU_J <= (25/32)I,
    delta=7/32.                                            (7.3)

The nonzero singular values of B_0=(A_H)[I,J] are those of M_I^(1/2) Lambda_H M_J^(1/2). Multiplication on the left and right by these invertible square roots reduces each singular value by at most a factor delta. For example apply s_j(C T D)<=||C||||D||s_j(T) to Lambda_H=M_I^(-1/2)(M_I^(1/2)Lambda_H M_J^(1/2))M_J^(-1/2). Thus s_3(B_0)>=delta.

For the full cross block B=A[I,J]=B_0+E[I,J], ||E[I,J]||<=eta. On the top-three right-singular subspace of B_0, ||Bv||>=(delta-eta)||v||; the min-max characterization of singular values gives

    s_3(B)>=sigma=delta-eta=13/64.                           (7.4)

Because both restricted frames have full column rank and Lambda_H is invertible, range(B_0)=range(U_I). Its projection diagonal satisfies

    (P_range(B_0))_ii=u_i^T M_I^(-1)u_i
       <= (1/32)/(7/32)=1/7.                               (7.5)

Set gamma=sigma/sqrt(6)=13/(64sqrt(6)). Applying Section 6 to the full B gives

    max_i(K_gamma)_ii <= (1/sqrt(7)+sqrt(6)/13)^2 <1/2.       (7.6)

For an entirely rational check of the strict comparison, 1/sqrt(7)<2/5 and sqrt(6)/13<1/5, so its square is less than 9/25<1/2. Section 5 with the three singular values in (7.4) now gives

    ||p_Q||_infinity <= 9sqrt(3e)/(2sigma)
                     =288sqrt(3e)/13.

The Fourier envelope is integrable because theta_gamma>=18/7>2; consequently the density is continuous and vanishes at infinity. All additional spectral directions are retained inside B throughout. Within-block terms, including arbitrary separable perturbations, are allowed by the proof of (5.3). QED.

## 8. What this closes, and what it does not

The previous entire-range theorem fails as a certificate for every invertible matrix because its range projection is I. The present theorem permits A to be invertible. For example, take n=128 and three orthonormal flat columns U of a normalized Walsh-Hadamard matrix. Let Lambda_H=diag(1,1,-1), choose any orthonormal basis V of its orthogonal complement, and let T be any invertible symmetric matrix on that complement with ||T||<1/64. Then

    A=U Lambda_H U^T+VTV^T

is invertible, can be indefinite with both signs among its small eigenvalues, and satisfies (7.1), since P=UU^T has diagonal 3/128. T need not be diagonal in original coordinates and may generate dense couplings. This example establishes coverage beyond the entire-range condition, not novelty of the example family itself.

There is still no proof that every target A has a coordinate cut satisfying the ridge criterion, nor a proof that all remaining matrices can be paid by the existing local/aggregate theorems with uniform constants. Indeed, the already-recorded family

    [1] direct_sum J_m/m direct_sum (-J_m/m)

has eigenvalues {1,1,-1}, but all cross blocks have rank at most two. For any such B, theta_gamma<2 at positive gamma, so the q>=1 criterion cannot close that family. It is handled by independent coordinate-bank methods in the archive. This prevents claiming the new cross-block method alone is an exhaustive proof.

The next full-target implication is an exhaustive product-preserving reduction combining the ridge-certified distributed branch with leverage-heavy and low-cross-rank aggregate branches. Replacing this by an unsupported universal rank-three-cut or fixed-local-minor dichotomy would reuse a refuted reduction. The input hypotheses do not authorize conditional density caps after rotation or conditioning on dependent projections.

## 9. Executed checks and review scope

The accompanying checks.py and check_results.json contain: exact algebra for the constants and theta lower bound; three numerical integrations of the power envelope; 36 Gaussian graph examples with arbitrary admissible regularizers and direct frame-identity checks; and six n=128 full-rank indefinite examples with dense nonseparable small spectral tails. The examples check cross singular values, ridge leverage, effective dimension and exact Gaussian characteristic functions. They are finite corroborating checks, NOT universal proofs or independent reviews.

The analytic arguments in Sections 3-7, with the cited classical inputs, are the proof offered for the stated supporting results. No success of a computation or scheduler record certifies the original conjecture. Existing account02/B02 and account03/B04 are suitable independent reviewers of the free-regularizer and spectral-perturbation steps. Their earlier reviews must not be transferred to this extension without actual new review records.
