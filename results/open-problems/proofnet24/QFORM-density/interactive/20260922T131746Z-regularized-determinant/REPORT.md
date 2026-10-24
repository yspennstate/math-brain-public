# Regularized determinant bounds and a diffuse-range quadratic-density theorem

Programme: QFORM-DENSITY-3EIG-20260922. Interactive run: 20260922T131746Z-regularized-determinant.

**Status:** complete supporting analytic arguments supplied; independent end-to-end review pending. The unrestricted three-large-eigenvalue conjecture is NOT proved here. No literature-wide novelty claim is made. Repository transport is not native learned-memory ingestion.

## 1. Target, contribution, and scope

The full target concerns independent real coordinates with probability densities bounded by one and every symmetric A having at least three eigenvalues of absolute value at least one. It asks for one universal upper bound for the density of X^T A X. Neither the density bound for a fixed matrix nor a diagonal special case settles its uniformity.

This report proves a regularized determinant estimate for an arbitrary original-coordinate cross block B=A[I,J]. Unlike a bound containing the product of *all* its nonzero singular values in the denominator, this estimate allows extra tiny singular values to be discarded without a loss. Arbitrary within-block quadratic phases, outside coordinates, and outside couplings are retained.

A fractional-exponent version handles three large cross singular values under a specified leverage bound. Combining it with the Marcus--Spielman--Srivastava partition theorem proves the full density conclusion for matrices whose **entire range**, not merely the selected three-eigenspace, has maximum coordinate leverage at most 1/32. All additional nonzero eigenvalues can then be arbitrarily small and of either sign. The constant is 96e/(7 sqrt(2)) < 27. This is an additional geometric hypothesis, not a consequence of the original spectral hypothesis.

## 2. Classical inputs and source attribution

We use the Fourier convention hat f(s)=integral exp(isx) f(x) dx.

For 1<=p<=2 and p'=p/(p-1), sharp Hausdorff--Young is

    ||hat f||_(p') <= (2pi)^(1/p') C_p ||f||_p,
    C_p = p^(1/(2p)) / (p')^(1/(2p')).

Sharp Young convolution, for 1/p+1/q=1+1/r, is

    ||f*g||_r <= (C_p C_q/C_r) ||f||_p ||g||_q.

Endpoint constants are interpreted by continuity. Source: W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182, DOI 10.2307/1970980; publisher https://annals.math.princeton.edu/1975/102-1/p11 . Beckner's original PNAS note also explicitly identifies both inequalities: https://pubmed.ncbi.nlm.nih.gov/16592223/ .

The geometric rank-one Brascamp--Lieb inequality states that if unit vectors v_j in R^m and positive weights c_j satisfy sum c_j v_j v_j^T=I_m, then

    integral prod F_j(v_j dot x)^(c_j) dx <= prod (integral F_j)^(c_j).

The exact normalized formulation is Theorem 3.3 of G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, https://arxiv.org/pdf/1507.07949 . These are classical inputs, not claims of this report.

The partition input used in Section 7 is Corollary 1.5 of A. W. Marcus, D. A. Spielman and N. Srivastava, *Interlacing families II: Mixed characteristic polynomials and the Kadison--Singer problem*, Annals of Mathematics 182 (2015), 327--350, DOI 10.4007/annals.2015.182.1.8; https://arxiv.org/pdf/1306.3969 . Its precise two-part formulation is stated where applied.

## 3. Two scalar norm estimates

Let f be a probability density with 0<=f<=1. Hence ||f||_p<=1 for every p>=1. Put g=f*tilde f, where tilde f(x)=f(-x), the density of the difference of independent copies.

For 0<c<=1, sharp Young with inputs p=2/(1+c) and output r=1/c gives

    ||g||_(1/c) <= 2^c c^(c/2) (1+c)^(-(1+c)/2).                 (3.1)

Indeed C_p^2/C_r simplifies to exactly the right-hand side. The norm bounds on the input factors supply no extra constants.

Next fix 1<=q<=2 and let h(s)=|hat f(s)|^q. For 0<c<=q/2, sharp Hausdorff--Young with Fourier exponent q/c>=2 gives

    ||h||_(1/c) = ||hat f||_(q/c)^q
       <= (2pi)^c q^(q/2-c) (q-c)^(-(q-c)/2) c^(c/2).          (3.2)

The restriction c<=q/2 is essential. It is not available for arbitrary c when q<2.

Define

    G(c)=2^c (1+c)^(-(1+c)/2),
    H_q(c)=q^(q/2-c) (q-c)^(-(q-c)/2).

The logarithms are concave. Their tangents at c=1 and c=0, respectively, yield

    log G(c) <= (1-log 2)(1-c)/2,                              (3.3)
    log H_q(c) <= (1-log q)c/2.                                (3.4)

For clarity, (log G)''=-1/[2(1+c)] and (log H_q)''=-1/[2(q-c)]. Also log G(1)=0 and log H_q(0)=0. These observations prove (3.3)--(3.4), including their endpoint limits.

## 4. Regularized graph integral

Let R be any real m-by-k matrix, with columns r_j. Let independent D_i have densities g_i, each the difference density of two independent copies of a density bounded by one. Let f_j be arbitrary additional probability densities bounded by one. The two lists need not have identical laws.

For a real number a and 1<=q<=2, define

    L_q=pi e sqrt(2/q),  alpha=L_q^2,
    M=alpha I_m+a^2 R R^T,
    c_i=alpha e_i^T M^(-1)e_i,
    d_j=a^2 r_j^T M^(-1)r_j.

Assume d_j<=q/2 for all j. Then

    E prod_j |hat f_j(a r_j dot D)|^q
       <= det(I_m+a^2 R R^T/L_q^2)^(-1/2).                    (4.1)

For q=2 the assumption is automatic for every matrix R and every a.

### Proof

The case a=0 is immediate. For general a set

    v_i=sqrt(alpha) M^(-1/2)e_i,
    w_j=a M^(-1/2)r_j.

Their outer products sum to I_m. Their squared norms are c_i and d_j, so

    0<c_i<=1, 0<=d_j<=1,
    sum_i c_i+sum_j d_j=m.

Ignore zero w_j, whose Fourier factors equal one. Put theta=sum_j d_j=sum_i(1-c_i).

Change variables x=M^(-1/2)z in the defining integral, normalize the vectors v_i and w_j to unit length, and apply geometric Brascamp--Lieb. This gives

    integral prod_i g_i(x_i) prod_j h_j(a r_j dot x) dx
     <= det(M)^(-1/2)
        prod_i [alpha^(c_i/2) c_i^(-c_i/2) ||g_i||_(1/c_i)]
        prod_j [d_j^(-d_j/2) ||h_j||_(1/d_j)],                 (4.2)

where h_j=|hat f_j|^q. For example, the scalar change of variable on a g_i factor contributes alpha^(c_i/2)c_i^(-c_i/2); this factor must not be omitted.

Insert (3.1) and (3.2). The c_i^(c_i/2) and d_j^(d_j/2) factors cancel the corresponding Brascamp--Lieb factors. The result is

    det(M)^(-1/2) alpha^((m-theta)/2) (2pi)^theta
        prod_i G(c_i) prod_j H_q(d_j).

By (3.3)--(3.4), the last product is at most

    exp{[1-(log(2q))/2] theta}.

Factoring alpha^m from det M leaves the dimensionless multiplier

    [2pi exp(1-(log(2q))/2)/sqrt(alpha)]^theta = 1.

The remainder is precisely (4.1). All functions in the Brascamp--Lieb application are integrable by (3.1)--(3.2). No moment, smoothness or connected-support assumption enters. QED.

A useful sufficient condition for d_j<=q/2 at all a is that the coordinate diagonal of the orthogonal projection onto range(R^T) be at most q/2: the regularized matrix a^2 R^T(alpha I+a^2RR^T)^(-1)R is bounded above by that projection.

## 5. Characteristic functions of arbitrary quadratic forms

Let A be any real symmetric matrix and let I,J be disjoint sets of its ORIGINAL coordinates. Put B=A[I,J]. For q in [1,2), assume

    max_i (P_range(B))_(ii) <= q/2,                            (5.1)

where this projection is in R^I. One may interchange I and J to use the other side. For q=2 no assumption (5.1) is necessary.

Then, for all real t,

    |E exp(it X^T A X)|
      <= det(I+2q t^2 B B^T/(pi^2 e^2))^(-1/(4q)).            (5.2)

In particular the unconditional, arbitrary-matrix estimate is

    |E exp(it X^T A X)|
      <= det(I+4t^2 B B^T/(pi^2 e^2))^(-1/8).                (5.3)

### Proof

Condition on all coordinates outside I union J. The remaining coordinates stay independent with their original density bounds. The conditional form is

    q_I(X_I)+q_J(X_J)+2 X_I^T B X_J+c,

where the self terms include all within-block couplings and induced linear terms. The proof works even for arbitrary measurable real self functions q_I and q_J, finite almost surely.

Let Y,Y' be independent copies of X_J. One Cauchy--Schwarz inequality, followed by expansion of the square and the triangle inequality, gives

    |phi(t)|^2
     <= E_(Y,Y') prod_(i in I) |hat f_i(2t [B(Y-Y')]_i)|.

For q>=1, Jensen's inequality therefore gives

    |phi(t)|^(2q)
     <= E_(Y,Y') prod_(i in I) |hat f_i(2t [B(Y-Y')]_i)|^q.     (5.4)

Apply (4.1) with difference dimension |J|, R=B^T, and a=2t. Condition (5.1) is exactly the sufficient all-frequency condition described after (4.2). This proves (5.2), since 4/L_q^2=2q/(pi^2e^2) and det(I+sB^TB)=det(I+sBB^T). The bound is uniform in the initially conditioned values, so averaging proves the unconditional assertion. QED.

This proof never declares spectral coordinates independent. The arbitrary self phases disappear in the first Cauchy--Schwarz and triangle steps, rather than being falsely factored coordinatewise.

## 6. Density consequences insensitive to small additional singular values

Suppose B has at least r singular values >=sigma>0. It can have any number of additional nonzero singular values, however small. Under the assumptions of (5.2), if r>2q, then

    |phi(t)| <= (1+2q sigma^2 t^2/(pi^2e^2))^(-r/(4q)).         (6.1)

Every discarded singular-value factor is at most one. Thus the extra directions do not introduce a reciprocal-small-singular-value cost.

The right side of (6.1) is integrable. Fourier inversion gives a continuous density vanishing at infinity and

    ||p_Q||_infinity
      <= [e sqrt(pi)/(2 sqrt(2q) sigma)]
           Gamma(r/(4q)-1/2)/Gamma(r/(4q))
      <= [e/(sqrt(2q) sigma)] r/(r-2q).                       (6.2)

For the simpler second inequality, bound (6.1) by min(1,(beta|t|)^(-r/(2q))) where beta=sqrt(2q)sigma/(pi e), split the time integral at 1/beta, and integrate exactly. Continuity follows from phi in L^1, not merely from boundedness of a density.

Examples of the scope:

* With no leverage assumption, five cross singular values >=sigma imply ||p_Q||_infinity<=5e/(2sigma). The gamma expression gives approximately 6.32595/sigma instead of 6.79570/sigma.
* With column-space leverage at most 2/3 on one physical side, three cross singular values >=sigma imply ||p_Q||_infinity<=9e sqrt(3/8)/sigma, by q=4/3.
* With leverage at most 1/2, three cross singular values >=sigma imply ||p_Q||_infinity<=3e/(sqrt(2)sigma), by q=1.

These are cross-block singular-value hypotheses, not the original three-eigenvalue hypothesis. In particular one must not call the five-cross-direction conclusion the full three-eigenvalue solution.

## 7. Three large eigenvalues with arbitrary smaller eigenvalues: a diffuse-range theorem

### Theorem

Suppose A=U Lambda U^T, where U has r>=3 orthonormal columns spanning the ENTIRE range of A, Lambda is invertible symmetric, and at least three eigenvalues of Lambda have absolute value >=1. The other eigenvalues may be arbitrarily small, of either sign and in arbitrary number. Assume

    max_i ||u_i||^2 <= 1/32,                                 (7.1)

where u_i^T are the rows of U. Then

    ||p_(X^T A X)||_infinity <= 96e/(7 sqrt(2)) < 27.           (7.2)

The density is continuous and vanishes at infinity. The same conclusion holds after adding ANY coordinate-separable measurable real term sum V_i(X_i), finite almost surely.

### Proof

The two-part case of Marcus--Spielman--Srivastava, Corollary 1.5, states that a tight frame sum u_i u_i^T=I with ||u_i||^2<=epsilon admits a partition I,J such that both partial frame sums have norm at most (1/sqrt(2)+sqrt(epsilon))^2.

Apply it with epsilon=1/32. Since

    (1/sqrt(2)+1/sqrt(32))^2 = 25/32,

both M_I=U_I^TU_I and M_J=U_J^TU_J satisfy

    (7/32) I_r <= M_I,M_J <= (25/32) I_r.                    (7.3)

The lower bounds follow from M_I+M_J=I_r. In particular both restricted frames have full column rank.

For the original-coordinate cut B=A[I,J]=U_I Lambda U_J^T, its nonzero singular values equal those of

    M_I^(1/2) Lambda M_J^(1/2).

Let delta=7/32. Left and right multiplication by these square roots reduces each singular value by at most a factor delta: for every j,

    s_j(B) >= delta s_j(Lambda).                             (7.4)

One justification is to write Lambda=M_I^(-1/2)(M_I^(1/2)Lambda M_J^(1/2))M_J^(-1/2) and use the standard singular-value bound s_j(CTD)<=||C||||D||s_j(T). Consequently B has at least three singular values >=7/32, independently of all the other eigenvalue sizes.

Since Lambda is invertible and U_J has full column rank, range(B)=range(U_I). Its projection is U_I M_I^(-1)U_I^T, whose coordinate diagonal satisfies

    (P_range(B))_(ii)=u_i^T M_I^(-1)u_i
       <= ||u_i||^2/delta <= 1/7 < 1/2.                     (7.5)

Apply (6.2) with q=1, r=3 counted large singular values, and sigma=7/32. It gives (7.2). The proof treats the full Lambda; it neither discards small quadratic summands as independent noise nor pays their determinant product.

Adding sum V_i changes only the two arbitrary within-block self phases in Section 5, leaving B unchanged. Hence the same estimate proves the separable-perturbation assertion. QED.

This combines the partition theorem with the newly supplied regularized graph argument. The partition theorem is a cited prior result, not a new resolution of Kadison--Singer.

## 8. Exact advance relative to the current archive

The existing separable-phase proof is at math-open-problems commit 773b7fb6f0e6a8142066f0bac08d228dfc164fdb, path proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md. Its constant contains |det Lambda|^(-1/r); the present Section 7 does not pay the extra tiny eigenvalues, at the price of the stronger explicit leverage threshold 1/32.

The account02/B08 update at commit 84657e690f8411d99602ddc772b622686c3874ed, path proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T124007Z-r11/REPORT.md, supplies whitening and an independent passing review of that earlier separable-phase theorem. It does not establish the current regularized determinant result, which needs its own review.

The account02/B02 cross-block theorem at commit 400f82c8b98fc5623f567581b6ccb0b4298974e8 supplies a complementary exact-rank Fourier estimate. Its product of all nonzero cross singular values can deteriorate under tiny extra directions. The current regularization eliminates that issue in the quantified branches of Sections 6--7, but has a weaker general decay exponent without the leverage hypothesis.

The account03/B10 heavy-row handoff, report commit c1af196adade03e07456c8f6e783f952b0fa0e8d, identifies an isotropic heavy coordinate with dependent residual leakage. That dependence is not removed by this report.

## 9. Remaining full-target implication

The original target does not imply (7.1). In fact an invertible A has full-range projection I_n and every range leverage equals one. A diagonal A has B=0 for every disjoint cut even though its target density bound is already known. Thus Section 7 is a genuine additional branch, not an equivalent reformulation of the full conjecture.

The next required bridge is a dimension-free heavy/light or original-coordinate reduction: starting only from s_3(A)>=1, retain a bounded amount of usable quadratic curvature while either producing a cross block satisfying Section 6, producing a known well-conditioned physical block, or directly controlling the remaining heavy-coordinate/nonseparable interaction. This report proves no exhaustive dichotomy of that form.

At q=2 and only three useful cross singular values, (5.3) has tail order |t|^(-3/4), which is not integrable. Promoting it to a density bound would be an error. No counterexample to the full conjecture is supplied. Universal C=pi remains excluded by the archive's earlier lower-bound correction; no such constant is asserted here.

## 10. Checks and verification status

The accompanying check_algebra.py and check_results.json check exact scalar constant identities, tangent derivatives, the geometric frame identities on 25 finite matrices, 22 one-dimensional uniform examples, 128 full Gaussian quadratic examples, the gamma/min-envelope constants, and finite small-extra-singular-value cases. Additional partition/cross-spectral checks are recorded separately. These computations are sanity checks only; the proofs above carry the universal quantifiers.

Independent reviews requested from existing mathematical workers should focus on (i) Young/Hausdorff--Young exponent bookkeeping and the regularized determinant cancellation, (ii) the decoupling exponent 1/(4q) and leverage orientation, and (iii) the MSS partition and full-spectrum singular-value comparison. A review must not label the unrestricted conjecture solved.

Privacy/provenance: only authorized mathematics, public theorem references and source-pinned private mathematical dependencies are included. No scheduler identifiers, credentials, signed URLs, unrelated personal data, public release, paid calls or native-memory-ingestion claim is involved. Local checks cover only the explicit generated files and are not a whole-repository privacy audit.
