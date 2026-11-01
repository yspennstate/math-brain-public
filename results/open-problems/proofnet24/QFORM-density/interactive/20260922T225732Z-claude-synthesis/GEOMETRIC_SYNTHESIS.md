# Determinant-only pair bounds and a single no-pivot reduction

Programme QFORM-DENSITY-3EIG-20260922. Supplement to interactive record 20260922T225732Z-claude-synthesis.

**Status.** This note applies Claude's additional push at 23:03:41 UTC, commit `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, to the earlier unrestricted one-eigenvalue small-ball theorem. It removes the condition-number factor from the physical-pair estimate, proves the logarithmic-potential auxiliary bound globally, and reduces the full conjecture to ONE no-pivot bounded-density statement. That remaining statement is not proved here. Complete supporting arguments follow; independent review and literature-wide novelty are not asserted.

Claude source: `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/GEOMETRIC_ROUTE_REPORT.md`, especially Lemmas 1.2, 1.4, 1.5 and Theorem 5.2. The argument below replaces the three separate no-pivot assumptions in that theorem by one, using Gaussian padding that remains inside the no-pivot class. The Gaussian coordinates are auxiliary variables in a reduction, not a Gaussian assumption on the original inputs.

## 1. Two completed inputs and their exact scopes

All original coordinates are independent with probability densities at most one. All affine coefficients below are arbitrary.

### 1.1 Unrestricted one-eigenvalue small-ball estimate

The prior interactive report at

`math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`, Section 3,

proves, for every nonzero symmetric S and R=Z^T S Z+b^T Z+d,

    sup_t P(|R-t|<rho) <= min(1, 5 (rho/||S||)^(1/4)).          (1.1)

This is arbitrary rank, not an exact-rank-one statement. Its source proof is: a diagonal coefficient at least ||S||/2 gives a conditional scalar-square bound; otherwise a random-sign cut supplies an ORIGINAL-coordinate cross block of norm at least ||S||/4. The previously proved unrestricted regularized determinant estimate then gives a characteristic-function envelope proportional to |t|^(-1/4). Gaussian smoothing integrates it to (1.1). The scalar prefactor is bounded analytically by 73/15<5 in that report.

The non-elementary analytic dependency behind that argument is the graph Brascamp-Lieb estimate of `a302aab3477c64757b511e80d3907f982e04873a`, regularized-determinant/REPORT.md Section 5. Its own earlier scoped review is not a review of this new synthesis. We preserve that dependency rather than presenting (1.1) as newly proved by the numerical checks.

### 1.2 Claude's orientation-uniform hyperbolic product envelope

Let B be a real indefinite nonsingular 2x2 matrix, D=|det B|, and W have independent cap-one coordinates. For every translation m, the density of (W-m)^T B(W-m)+kappa satisfies

    p(t) <= D^(-1/2) [5.2 + log_+(16 sqrt(D)/|t-kappa|)].       (1.2)

This is Lemma 1.4 of the newest GEOMETRIC_ROUTE_REPORT. The independence of the two physical coordinates is essential. Here is the main calculation, retaining the constants.

Let the eigenvalues be mu_+>0>mu_-, and let L=1/mu_++1/|mu_-|. At positive level delta, the two hyperbolic branches are

    w_e(t)= e sqrt(delta/mu_+) cosh(t) e_+
                       +sqrt(delta/|mu_-|) sinh(t) e_-,

with e=+1,-1. The coarea measure is dt/(2sqrt(D)) on each branch. Write w_e(t)=u exp(t)+v exp(-t); both |u| and |v| equal rho_0=sqrt(delta L)/2. On the positive arm choose an original coordinate i with |u_i|>=rho_0/sqrt(2). For t>=T_1=(3/4)log(2),

    |w_i'(t)| >= |u_i|exp(t)/2,   |w_i(t)| <= 3|u_i|exp(t)/2.

The coordinate is monotone, so f_1(w_1)f_2(w_2)<=f_i(w_i) and change of variables bound its tail integral by 3log(1+1/m), with m=|u_i|exp(T)/2. Choose T=max(T_1,log(2/|u_i|)), making m>=1. This gives at most 3log2 on that tail. The negative arm is identical with v. Each chosen cutoff is at most T_1+(1/2)log_+(32/(delta L)). The middle integral uses f_1f_2<=1. Thus a whole branch costs at most

    2T_1+6log2+log_+(32/(delta L))
       = (15/2)log2+log_+(32/(delta L))
       <5.2+log_+(32/(delta L)).

Summing the two branches and multiplying by 1/(2sqrt D), then using L>=2/sqrt D, proves (1.2). Negative levels exchange the eigenvalue roles. Translations preserve the coordinate caps and masses. All formulas can be integrated against output test functions to handle null sets, so conditioning on an outside parameter is legitimate.

The tail integral 3log(1+1/m) does not assume a global maximizer on the infinite line: on a fixed one-sided tail |y|>=m, the decreasing weight 1/|y| is maximized under 0<=f<=1 and integral f<=1 by the interval of length one adjacent to m. This finite-tail rearrangement has no nonattainment issue.

## 2. The logarithmic auxiliary problem is solved globally

**Theorem 2.1.** For R as in (1.1), every K>0 and every t,

    E log_+(K/|R-t|) <= 4 + log_+(625 K/||S||).               (2.1)

In particular, if ||S||>=1,

    sup_t E log_+(1/|R-t|) <= 4+4log5 =: L_0 <10.438.         (2.2)

No no-pivot hypothesis is needed.

**Proof.** By nonnegative layer cake and (1.1), the left side is at most

    integral_0^infinity min(1, B exp(-u/4)) du,
    B=5(K/||S||)^(1/4).

This integral is 4B when B<=1 and 4+4logB otherwise. It is at most 4+4log_+B, which is (2.1). QED.

Thus Hyp'_1 in Claude's Theorem 5.2 is already available from the prior archive. A rank-one square-root small-ball rate is not needed to prove this logarithmic integrability statement.

## 3. A determinant-only pair theorem at arbitrary rank

**Theorem 3.1.** Let s_3(A)>=s>0. Suppose B is an indefinite nonsingular principal block on two ORIGINAL coordinates, and set D=|det B|. For arbitrary cap-one product laws and arbitrary affine terms,

    ||p_{X^TAX+b^TX+c}||_infinity
       <= D^(-1/2) [9.2 + log_+(10000 sqrt(D)/s)].             (3.1)

No smallest-singular-value bound on B is required. Every other eigenvalue and coupling of A may be arbitrary.

**Proof.** Write A=[[B,E],[E^T,C]] and S=C-E^T B^(-1)E. The matrix

    A_0=[[B,E],[E^T,E^TB^(-1)E]]

has rank two, and A-A_0=diag(0,S). The singular-value rank-approximation inequality gives ||S||>=s_3(A)>=s. This also follows directly from the min-max characterization on the codimension-two kernel of A_0.

Complete the square in the two original coordinates. Conditional on the other coordinates Z, the pair law is still a product of two densities bounded by one, translated by a vector depending on Z, and its critical value is a quadratic-plus-affine R(Z) with matrix S. Apply (1.2) conditionally and average:

    p_Q(t) <= D^(-1/2) [5.2 + E log_+(16sqrt(D)/|R-t|)].

Theorem 2.1, with K=16sqrt D and ||S||>=s, supplies (3.1). The uniform bound and the conditional density identity also prove absolute continuity. QED.

For the original spectral normalization s>=1 and any fixed D>=d>0, monotonicity in D gives

    ||p_Q||_infinity <= d^(-1/2)[9.2+log_+(10000sqrt(d))].     (3.2)

Indeed (9.2+log_+(10000x))/x decreases for x>0. At the two-quantitative-pivot threshold d=3501/64000, the right side is below 73. Thus any compatible original pair with determinant magnitude at least that threshold is controlled regardless of a bad pair condition number.

This removes the kappa=sigma_min(B) factor in the earlier arbitrary-rank pair bound. It does not prove the existence of a determinant-bounded physical pair from three large eigenvalues. If a previously handled worker branch already guarantees this pair, (3.2) is an alternative or improved estimate on that branch, not a newly discovered missing case.

## 4. Gaussian padding preserves the no-pivot class

Fix tau in (0,1]. Say M has **no tau-pivot** when

    |M_ii|<tau for every i,
    |det M_{ij,ij}|<tau for every distinct i,j.

Then |M_ij|<sqrt(2tau). The condition refers to the actual matrix, not to a chosen component.

Assume the following SINGLE statement N3(tau,C_0):

> Every no-tau-pivot symmetric matrix M with at least three eigenvalues of absolute value at least one, acting on independent cap-one coordinates, has output density at most C_0.

It is sufficient to assume the statement for homogeneous quadratics. It automatically extends to arbitrary affine terms: for a fixed M, replace it by M_epsilon=M+epsilon P_ker(M). For small positive epsilon it is invertible, retains the three substantial eigenvalues, and stays inside the STRICT no-pivot inequalities. Translate each original coordinate to complete the square in the affine polynomial. Those translated laws retain their density caps. Let epsilon decrease to zero. The affine polynomials converge almost surely for the fixed original inputs, and uniform interval-measure domination passes to the weak limit. No moment bound or uniform bound on the large completing-square translation is needed.

**Lemma 4.1.** Under N3(tau,C_0), every no-tau-pivot R=Y^TMY+beta^TY+gamma with at least TWO eigenvalues of M of absolute value at least one satisfies

    sup_t E[|R-t|^(-1/2); |R-t|<=1] <= 2 exp(pi) C_0,
    sup_t E |R-t|^(-1/2) <= 1+2 exp(pi) C_0.                  (4.1)

**Proof.** Choose an integer N>1/tau. Introduce N independent auxiliary variables G_j with density exp(-pi x^2), independent of Y, and put G=N^(-1/2)sum_j G_j. Each auxiliary density has cap one, and G has that same Gaussian law. Append to M either the rank-one block +(J_N/N) or -(J_N/N). The appended block has one eigenvalue +1 or -1, all its diagonal entries have magnitude 1/N<tau, and all its internal 2x2 principal determinants vanish. A principal pair straddling the old and new blocks has determinant magnitude |M_ii|/N<tau. Therefore BOTH augmented matrices remain no-tau-pivot and have at least three substantial eigenvalues.

N3, including its affine extension, gives densities bounded by C_0 for R+G^2 and R-G^2. The density of G^2 is

    k(u)=exp(-pi u)/sqrt(u),  u>0,

and zero on the negative half-line. Their summed densities agree almost everywhere with

    F(t)=E[exp(-pi |t-R|)/sqrt(|t-R|)],

using infinity at zero inside the integrand. The scalar kernel in F is lower semicontinuous (including its value infinity at zero), so Fatou's lemma makes F lower semicontinuous. Since F<=2C_0 almost everywhere, it follows that F<=2C_0 everywhere: a strict violation of a lower-semicontinuous function persists on a nonempty open neighborhood. On |t-R|<=1 the exponential is at least exp(-pi); outside it, |t-R|^(-1/2)<=1. This proves both bounds in (4.1). QED.

The padding is deliberately spread across N NEW independent coordinates. A single added square would introduce a large diagonal pivot and would not justify applying N3. The construction above avoids that gap.

## 5. Full conjecture equivalent to a single no-pivot density statement

**Theorem 5.1.** Fix tau in (0,1]. Subject to the already supplied estimate (1.1), N3(tau,C_0) implies the entire original conjecture, including arbitrary affine terms, with a finite constant depending only on tau and C_0. Conversely, the full conjecture implies N3 immediately. No separate no-pivot half-Riesz or logarithmic hypothesis is required.

An explicit valid transfer is

    C_full <= tau^(-1/2) max{1+2exp(pi)C_0, 1+3K_tau},
    K_tau = (2/sqrt(tau))[6.2+log_+(16sqrt(tau))].              (5.1)

### Proof: control the two-eigenvalue auxiliary problem

Let R have at least two substantial eigenvalues in its actual matrix S.

If S has no tau-pivot, use Lemma 4.1.

If S has a 2x2 physical principal block with determinant magnitude D>=tau, condition on its complement. The definite case has conditional density at most pi/sqrt(D). In the indefinite case, integrate (1.2) on an interval of radius u to get

    P(|R-t|<=u | outside)
       <= (2u/sqrt(D))[6.2+log_+(16sqrt(D)/u)].

For 0<u<=1, monotonicity of [6.2+log_+(16x/u)]/x in x gives the uniform bound

    P(|R-t|<=u) <= K_tau u(1+log(1/u)).                       (5.2)

The definite case obeys the same bound since K_tau>=12.4/sqrt(tau)>2pi/sqrt(tau). Averaging over the outside variables is legitimate because the bound is independent of the conditional center. Nonnegative layer cake yields

    E|R-t|^(-1/2)
       <=1+K_tau integral_1^infinity v^(-2)(1+2log v) dv
       =1+3K_tau.                                            (5.3)

Otherwise a scalar pivot d with |d|>=tau is present. Complete that square, leaving a quadratic-plus-affine T whose Schur matrix has at least one substantial eigenvalue. The spectral-count fact is recalled below. The scalar inverse-image bound, uniform in its translation, is

    P(|d(X-m)^2-v|<=u)
      <=4u/[sqrt(|d|) sqrt(max(|v|,u))].                     (5.4)

Integrate (5.4) for u=z^(-2), z>=1. For delta>0,

    integral_1^infinity z^(-2)/sqrt(max(delta,z^(-2))) dz
       <=1+(1/2)log_+(1/delta).

With delta=|t-T| and Theorem 2.1, this proves

    E|R-t|^(-1/2)
       <=1+(4/sqrt(tau))[1+L_0/2]
       <=1+3K_tau.                                          (5.5)

The last inequality follows from L_0=4+4log5 and 3K_tau>=37.2/sqrt(tau), while 4(1+L_0/2)=12+8log5<25. Thus, in every two-eigenvalue case,

    sup_t E|R-t|^(-1/2)
       <= max{1+2exp(pi)C_0, 1+3K_tau}=:H_tau.              (5.6)

### Proof: lift to three eigenvalues

Now consider the original A with three substantial eigenvalues. If it has no tau-pivot, N3 applies. A definite pair with determinant magnitude at least tau gives density at most pi/sqrt(tau). An indefinite pair with determinant magnitude at least tau is controlled by (3.2). Otherwise a scalar coefficient |a|>=tau exists. Completing its square leaves a Schur matrix with at least two substantial eigenvalues, so (5.6) and the exact conditional square kernel give

    ||p_Q||_infinity <= |a|^(-1/2) H_tau <= tau^(-1/2) H_tau.

This last bound also dominates the no-pivot and pair bounds. Indeed tau<=1, H_tau>=1+2exp(pi)C_0, and H_tau>=1+37.2/sqrt(tau), whereas the indefinite pair bound times sqrt(tau) is at most 9.2+log10000<18.411. This proves (5.1). QED.

### Spectral-count fact used in the scalar cases

An invertible p-by-p physical principal pivot loses at most p eigenvalues of magnitude at least one. If A is invertible, the inverse Schur matrix is a codimension-p principal submatrix of A^(-1). The k eigenvalues of A^(-1) in [-1,1] form a consecutive block in its ordered spectrum; Cauchy interlacing retains at least k-p of them. Invert again. For singular A, use A+epsilon P_ker(A), preserve the existing pivot for sufficiently small epsilon, and take the finite Schur-complement limit. The original large eigenvalues are unchanged during this regularization. No false independence after rotation is used; this is deterministic matrix algebra.

## 6. What this does not prove

N3(tau,C_0) is still unproved in the present work. It contains the entrywise-small hybrid hub-plus-spread configurations that the newest Claude Fourier report explicitly leaves open when arbitrary small dense light-block terms are present. Theorem 5.1 is a complete REDUCTION, not a proof of its remaining hypothesis.

The concrete progress is that workers no longer need to prove a separate global logarithmic-potential conjecture (Theorem 2.1 supplies it), and do not need a separate no-pivot half-Riesz theorem in order to close the full argument (Lemma 4.1 obtains it from the one desired no-pivot density theorem). The physical pair branch is now determinant-only. The companion REPORT.md closes finite-dimensional actual-spectrum cases and localized finite cores with dense tails. These statements are compatible, but their union is not asserted exhaustive without N3.

Required next step: establish a universal density bound for the no-tau-pivot, three-large-eigenvalue class, or produce a valid counterexample inside that class. Retain all product laws and all remaining spectrum. Apply D', D5 and mixed-hub results only when their actual hypotheses hold; no-pivot does not force a rank-three cross block, as the existing hub examples show.

The full theorem remains unproved. No numerical observation, conditional reduction, historical proof label, or uploaded file is being represented as a completed solution.
