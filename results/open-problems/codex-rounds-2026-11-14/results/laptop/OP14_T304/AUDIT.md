# Independent checks and limitations

## A second derivation of the exponential moment

Write z=X-x_* and r=||z||. Strong convexity gives <z,grad f(x_*+z)>=m r^2. For each integer k>=1, integrate the divergence of

    z r^(2k-2) exp(-f(x_*+z)).

The divergence of z r^(2k-2) is (d+2k-2)r^(2k-2). Boundary terms vanish: f is bounded below by a positive quadratic plus a constant, grad f has at most linear growth by L-smoothness, and the remaining factors are polynomial. Equivalently, multiply by smooth cutoffs supported in balls of radius 2n and equal to 1 in balls of radius n, integrate on R^d, and let n tend to infinity. All cutoff errors are bounded by polynomial times Gaussian tails, hence vanish.

It follows that

    E[r^(2k-2)<z,grad f(X)>] = (d+2k-2) E r^(2k-2),
    E r^(2k) <= (d+2k-2) E r^(2k-2)/m.

Induction, starting with E r^0=1, gives

    E r^(2k) <= m^(-k) product_(j=0)^(k-1) (d+2j).

For 0<=t<m/2, expand the exponential and use monotone convergence:

    E exp(t r^2)
      <= sum_(k>=0) (t/m)^k/k! product_(j=0)^(k-1)(d+2j)
      = (1-2t/m)^(-d/2).

For completeness, the last series has coefficients (d/2)_k (2t/m)^k/k!, where (a)_k is the rising factorial. Its sum h(u) satisfies (1-u)h'(u)=(d/2)h(u), h(0)=1, by the coefficient recurrence. Solving gives h(u)=(1-u)^(-d/2) on 0<=u<1. This re-derives the dilation bound in PROOF.md without using the dilation argument.

## A separate constant audit

Keep delta=epsilon^2 d/(512A). Instead of the proof's chain `9,38,120,480`, use the following inequalities. Since log(A/d)<=A, log 512<7, t=log(1/epsilon)<=A, and A>=1,

    log(1/delta)<=10A,
    mR^2<=42A,
    sqrt(m)D+sqrt(m)R+1 <= (2+sqrt(42))sqrt(A) <9sqrt(A).

Here sqrt(42)<7 follows by squaring the positive sides. Substitution in (1) of PROOF.md gives

    W2^2 <=324 delta A/m = (81/128)epsilon^2 d/m
                           <(15/16)epsilon^2 d/m.

This independent constant chain verifies the advertised tolerance without the three-term Cauchy--Schwarz estimate or the constants 9 and 38 from the original allocation proof. Exact arithmetic in the script also confirms 480/512=15/16 and 3(1+38+1)=120.

## A reverse-transfer obstruction with a common warm start

For d>=3, let P and Q be centered Gaussian laws with precision matrices

    A_P=diag(1,2,1,...,1),
    A_Q=diag(2,2,1,...,1).

Both potentials are C-infinity with actual strong convexity 1 and actual smoothness 2, so both have condition number exactly 2 and known mode zero. They differ only in the first coordinate. Their density ratio is

    q(x)/p(x)=sqrt(2) exp(-x_1^2/2)<=sqrt(2).

Thus the single law Q is a sqrt(2)-warm start for P and a 1-warm start for Q, where warmness means an almost-everywhere upper bound on the density ratio.

The differing one-dimensional densities cross at |x_1|=sqrt(log 2). Let Phi denote the standard Gaussian CDF. Integrating the positive density difference on that interval gives

    TV(P,Q)=2[Phi(sqrt(2 log 2))-Phi(sqrt(log 2))]
           =0.166064074983513...,

independently of d. The remaining common coordinates integrate to 1, justifying the reduction to one coordinate.

For any coupling, Cauchy--Schwarz gives E[X_1Y_1]<=sqrt(E X_1^2 E Y_1^2)=1/sqrt(2), hence

    E||X-Y||^2 >= 1+1/2-2/sqrt(2)=(1-1/sqrt(2))^2.

Take X_1=Z and Y_1=Z/sqrt(2) for a common standard Gaussian Z, and couple every other coordinate identically. This attains the bound, so

    W2(P,Q)=1-1/sqrt(2),
    W2(P,Q)/sqrt(d)= (1-1/sqrt(2))/sqrt(d).

Consequently there is no dimension-uniform implication from constant TV separation to constant normalized W2 separation, even within this well-conditioned class with a common constant warm start. This does not disprove any sampling-query lower bound; it identifies the missing metric step in a proposed transfer of one.

The exact CDF expression was checked by a separate numerical integration of q-p on its positive interval. The coupling formula was derived from both a matching construction and a lower bound for every coupling.

## Other failure modes checked

- **Arbitrary contamination:** a TV-accurate law can have infinite second moment. The proof only invokes W2 after projection, and uses the target's moments for the unprojected leg.
- **The wrong center:** c is not assumed to be a mode or mean. Its distance certificate uses strong monotonicity, and S=D+R is essential. The numerical asymmetric example has mode zero and nonzero mean.
- **Projection bias:** projecting the approximate law alone is insufficient. Equation (8) explicitly charges for projecting the target.
- **Dimension one:** the reduction and its Gaussian moment bound apply to d=1. The cited subpolynomial theorem is stated for d>=2; its corollary is not asserted in dimension one here.
- **Poor initialization:** mD^2=kappa*G0 is included in the tolerance. The constant-allocation grid includes mD^2 as large as 10^100.
- **Very small accuracy:** the grid includes epsilon=10^-100. The proof is in exact arithmetic and is not limited to floating-point ranges; no implementation claim for such tiny tolerances is made.
- **Query accounting:** the dependence on kappa*G0 in the clipping tolerance is absorbed by a fourth power of B. The exponent in the cited TV theorem is chosen as eta/4, not eta. One initial gradient query is included.
- **Regularity:** the main reduction uses C^1 strong convexity and smoothness. The imported sampling theorem and its corollary require C^2. A smoothing argument preserving exact oracle cost has not been supplied.
- **Oracle and computation model:** the corollary uses exact gradients and unrestricted computation between queries. It proves no value-only bound or practical runtime estimate.
- **Accuracy regime:** the cited subpolynomial TV theorem and the corollary are not bounds polynomial in log(1/epsilon). No conclusion on optimal MALA complexity in that stricter regime follows.

## Reproduction

Run `python -B resource_guard.py verify_reduction.py` from this folder. All diagnostics are deterministic, and the complete data are in verification.json. The 1D integrations use composite Simpson quadrature with 12,000 subintervals on stated finite intervals; they are diagnostics. The proofs above supply the uniform statements.
