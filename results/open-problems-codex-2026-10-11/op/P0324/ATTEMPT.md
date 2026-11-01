# P0324: Analyticity of the one-dimensional Riesz free energy

Research date: 2026-10-12. Verdict: PARTIAL. No proof or counterexample for the intended finite thermodynamic free energy is obtained.

## 1. Exact target and normalization

Fix s in (0,1), T=R/Z, and beta>0. Boursier defines

    g_s(x) = lim_{m->infinity} [sum_{k=-m}^m |x+k|^{-s} - 2m^{1-s}/(1-s)],
    H_N = N^{-s} sum_{i != j} g_s(x_i-x_j),
    Z_N(beta) = integral_{D_N} exp(-beta H_N) dX,

where D_N orders x_2,...,x_N cyclically relative to x_1. The source's (1.10), PDF page 5, is

    f(beta) = lim_N -N^{-1}[log Z_N(beta)
                     - (beta/2) N^{2-s} integral_{T^2} g_s(x-y) dxdy].

The kernel in (1.1) has zero mean; the displayed background term is zero. Under literal Lebesgue dX, (1.10) has a beta-independent divergent entropy term; see Section 3. The intended research question concerns the FINITE free energy with the usual entropy normalization. We use

    F_N(beta) = -N^{-1} log[(N-1)! Z_N(beta)]

for clarity. Relative to this normalization, replacing the partition by a further beta-independent factor whose per-particle logarithm has a finite limit changes the limiting free energy by a constant and does not affect analyticity. For example, rescaling the circle to length N and dividing the labeled integral by N! gives the partition (N^N/N!) [(N-1)! Z_N]; the extra factor has per-particle logarithm tending to 1. More generally Section 5 applies to ANY beta-independent normalization for which a finite pointwise limit exists. Existence of the appropriately normalized limit is the known input cited as [LS17] in the source; no identification of different infinite-volume Gibbs constructions is needed below.

Target: for every fixed s in (0,1), prove that the finite thermodynamic limit is real analytic at every beta_0>0. We do NOT claim that normalization repairs prove this target.

## 2. Kernel convexity and the exact ground state (proved)

On each compact subinterval of (0,1), differentiation twice of the defining paired series is legitimate: second-derivative tails are bounded by C sum_{k>=m} k^{-s-2}, uniformly there. Thus

    g_s''(r) = s(s+1) sum_{k in Z} |r+k|^{-s-2} > 0,  0<r<1.

The kernel is symmetric, g_s(1-r)=g_s(r), strictly convex on (0,1), and tends to +infinity at both endpoints. It is therefore bounded below.

Its mean is zero. Indeed the integral of the m-th regularized partial sum on [0,1] equals

    [(m+1)^{1-s}-m^{1-s}]/(1-s) -> 0.

Passing to the limiting integral is legitimate: subtract the two endpoint singular terms r^{-s} and (1-r)^{-s}; the remaining paired tails converge uniformly, by the paired Taylor estimate and the scalar convergence of the regularized sum at one fixed interior point. The endpoint singularities are integrable since s<1.

Put y_i=N(x_{i+1}-x_i), cyclically, so y_i>0 and sum_i y_i=N. For k=1,...,N-1 put

    r_{i,k} = (y_i+...+y_{i+k-1})/N.

Every ordered pair corresponds to exactly one (i,k), and sum_i r_{i,k}=k, since each gap occurs k times. Jensen's inequality gives

    H_N >= N^{1-s} sum_{k=1}^{N-1} g_s(k/N).

Equality is attained by the equally spaced configuration. Strict convexity, already for k=1, forces all gaps to equal 1 at equality. Thus the minimizers are exactly the rotated regular N-gons.

For an explicit value, the standard Hurwitz-zeta continuation identity gives

    g_s(r)=zeta(s,r)+zeta(s,1-r),
    sum_{k=1}^{N-1} zeta(s,k/N)=(N^s-1) zeta(s).

Here is the justification for continuation rather than a divergent-series manipulation: for real part z>1, partitioning the convergent zeta series by residue classes proves
sum_{k=1}^N zeta(z,k/N)=N^z zeta(z). Both sides are meromorphic functions of z, so the identity extends to z=s in (0,1), where neither side has a pole. The first identity follows directly from the regularized Hurwitz partial sums; the differences between their endpoint subtraction constants and 2m^{1-s}/(1-s) tend to zero. Consequently

    E_N := min H_N = 2 zeta(s) [N-N^{1-s}].                   (2.1)

N=1 has H_1=0, consistent with (2.1). For 0<s<1, zeta(s)<0: the alternating eta series is positive by pairing successive decreasing terms, while eta(s)=(1-2^{1-s}) zeta(s) and its prefactor is negative. In particular E_N/N is bounded uniformly in N. This calculation is not a positive-temperature analyticity result.

## 3. Literal entropy-normalization obstruction (proved, not the intended solution)

Fix x_1 and use r_j=(x_j-x_1) mod 1 for j>=2. Then

    0<r_2<...<r_N<1,

the Jacobian is one, translation integrates to length one, and

    vol(D_N)=1/(N-1)!.

The lower bound H_N>=E_N gives

    Z_N(beta) <= exp(-beta E_N)/(N-1)!,
    -N^{-1} log Z_N(beta) >= N^{-1}log((N-1)!) + beta E_N/N.

The right-hand side tends to +infinity, because E_N/N is bounded and Stirling's formula gives N^{-1}log((N-1)!)=log N-1+o(1). Since the mean background integral is zero, the literal (1.10) is +infinity under the explicitly displayed Lebesgue measure. This diagnoses a normalization omission/convention in the displayed source formula. It does not establish a singularity in beta of the finite, entropy-renormalized free energy and is not counted as solving P0324.

There is a simpler finite-volume extensivity check for the normalized partition. The full labeled integral is exactly (N-1)! Z_N, since the (N-1)! orderings relative to x_1 have equal integrals. Under independent uniform labeled points on the unit circle, H_N is integrable since s<1 and its expectation is zero by the zero mean of g_s. Jensen's inequality therefore gives

    (N-1)! Z_N(beta)=E_uniform exp(-beta H_N) >= 1.

Combining this with the ground-state upper bound gives

    beta E_N/N <= F_N(beta) <= 0.

Thus this entropy-normalized sequence is uniformly finite on compact temperature intervals. These bounds do not prove convergence; existence remains a separate known input. Furthermore E_beta H_N lies between E_N and 0: the lower bound is pointwise, while the upper follows because log[(N-1)! Z_N] is convex and has right derivative zero at beta=0 (dominated first differentiation uses integrability of H_N and its lower bound). Hence the derivative E_beta H_N/N is uniformly bounded, directly for this normalization.

## 4. Uniform energy variance from convexity (proved)

For fixed x_1=0, use ordered coordinates u=(r_2,...,r_N) in the open convex simplex

    Omega={0<r_2<...<r_N<1} subset R^d, d=N-1.

The energy V(u)=H_N(0,u) is convex. Indeed each pair contributes a positive multiple of g_s applied to a positive affine difference in (0,1), after using symmetry of g_s. Sum and affine composition preserve convexity. V is smooth in Omega, bounded below, and diverges at collision boundaries. Translation invariance gives Z_N=integral_Omega exp(-beta V(u))du, with no beta-dependent Jacobian or gap weight.

Known theorem used (Prekopa's marginal log-concavity theorem): if a nonnegative measurable function W(y,t) is jointly log-concave, its marginal integral_y W(y,t) is log-concave in t whenever the marginal is finite. Zero values outside a convex support are allowed. We apply this classical theorem, rather than claim a new proof of it.

Extend V by +infinity outside Omega. Its perspective

    P(y,beta)=beta V(y/beta), beta>0,

is convex as an extended-real function. Explicitly, take beta_1,beta_2>0 and 0<=t<=1, put b=t beta_1+(1-t)beta_2 and lambda=t beta_1/b. Then 0<=lambda<=1 and

    [t y_1+(1-t)y_2]/b
       = lambda y_1/beta_1 +(1-lambda)y_2/beta_2.

Convexity of V, multiplied by b, proves

    P(t y_1+(1-t)y_2,b)
        <= t P(y_1,beta_1)+(1-t)P(y_2,beta_2).

If an endpoint lies outside the domain, its right-hand side is infinity and the inequality is automatic. The support {(y,beta): beta>0, y/beta in Omega} is convex by the same identity. Thus exp(-P) is jointly log-concave. Its marginal is finite and positive, since change of variables y=beta u gives

    integral exp[-P(y,beta)]dy = beta^d Z_N(beta).

Prekopa implies log[beta^d Z_N(beta)] is concave. Differentiating twice yields

    (log Z_N)''(beta) <= d/beta^2.

The differentiation is justified without any collision regularity assumption: V>=E_N, and on each compact positive-beta interval every polynomial in |V| times exp(-beta V) is bounded by a constant, using the lower bound and exponential decay at positive infinity. Omega has finite volume. Dominated differentiation therefore gives

    (log Z_N)''(beta)=Var_{N,beta}(H_N).

Conclusion:

    0 <= Var_{N,beta}(H_N) <= (N-1)/beta^2.                 (4.1)

N=1 has zero variance separately. This is unconditional for the finite-volume source gas. Additive energy/background constants and beta-independent partition factors do not change (4.1).

A useful consequence, also proved: for the centered energy X=H_N-E_beta H_N and every real t<beta,

    log E_beta exp(tX)
      <= (N-1)[-log(1-t/beta)-t/beta].                     (4.2)

Proof: K(t)=log E exp(tX) is finite for t<beta, K(0)=K'(0)=0, and K''(t)=Var_{beta-t}(H_N). The right-hand side Q has the same value and derivative at zero and Q''=(N-1)/(beta-t)^2. Thus Q-K is convex on (-infinity,beta) and has a minimum zero at t=0. This proves (4.2), including negative t. It is a real-temperature moment bound, not a uniform complex zero-free assertion.

## 5. Any finite normalized thermodynamic limit is locally C^{1,1} (proved)

Let a_N be any beta-independent real constants and set

    G_N(beta)=-N^{-1}log Z_N(beta)+a_N.

Assume G_N(beta)->G(beta) is finite for every beta in an open interval I subset (0,infinity). From (4.1), on [a,b] subset I,

    -1/a^2 <= G_N'' <= 0.                                (5.1)

We now prove, rather than presume, passage to first derivatives. On any slightly smaller compact interval J, concavity bounds G_N'(x) between secant slopes to fixed nearby exterior points. Pointwise convergence at those points and at one interior point, together with (5.1), gives uniform bounds on G_N' throughout J. Also (5.1) makes G_N' uniformly Lipschitz with constant 1/a^2. Arzela-Ascoli gives a uniformly convergent derivative subsequence on J, with continuous Lipschitz limit h. For a fixed c in J, integrate:

    G_N(x)-G_N(c)=integral_c^x G_N'(u)du.

Taking limits gives G(x)-G(c)=integral_c^x h(u)du. Thus G is C^1 and G'=h, locally Lipschitz. Every derivative subsequential limit must equal G', so the full derivative sequence converges uniformly on smaller compact intervals. In particular

    G in C^{1,1}_loc(I),  -1/beta^2 <= G''(beta) <=0 a.e.

The a.e. sharper bound follows by applying (5.1) on arbitrarily small neighborhoods and using differentiation of the Lipschitz derivative. The argument does not imply continuity of G'', nor existence of G'' at every beta. It therefore does not supply the possible C^2 consequence suggested by the source, much less analyticity.

## 6. Smooth convex Gibbs families can have non-C^2 limits (proved obstruction)

This section is NOT a Riesz counterexample. It tests whether Section 4 alone could logically imply analyticity.

On R^n, let Q_n(x)=max(n,|x|^2), a convex energy, and normalize Lebesgue measure by the volume v_n of the ball of radius sqrt(n). Set

    A_n(beta)=v_n^{-1} integral_R^n exp[-beta Q_n(x)]dx.

In radius r=|x|/sqrt(n),

    A_n(beta)=n integral_0^infinity r^{n-1}
                        exp[-beta n max(1,r^2)]dr
             =exp(-beta n)
              +(n/2)(beta n)^{-n/2} Gamma(n/2,beta n).      (6.1)

The pressure p_n=n^{-1}log A_n tends to

    p(beta) = -(1+log(2beta))/2,   0<beta<1/2,
              -beta,             beta>=1/2.               (6.2)

Proof of the limit: put u=log r. Then A_n=n integral_R exp[n phi_beta(u)]du, where phi_beta(u)=u-beta max(1,exp(2u)). On u<=0 the integral is exactly exp(-beta n). On u>=0, phi=u-beta exp(2u), whose maximum is attained at u*=-(1/2)log(2beta) when beta<1/2, and at 0 otherwise. Lower bounds follow by integrating over a fixed small one-sided neighborhood of a maximizer; continuity ensures the exponent is within any prescribed epsilon of its supremum. For the upper bound, on a fixed compact interval use its length times exp[n sup phi]. For u>=U sufficiently large, phi<=-(beta/2)exp(2u); using exp(2(u-U))>=1+2(u-U), its tail integral is at most exp[-n beta exp(2U)/2]/[n beta exp(2U)]. The u<=0 contribution is exact. First take n->infinity, then epsilon->0, choosing U large enough. This proves the Laplace limit and (6.2).

At beta=1/2 both values and first derivatives match: p=-1/2 and p'=-1. The left second derivative is 1/(2beta^2), tending to 2, while the right second derivative is zero. The derivative p' therefore has unequal one-sided derivatives, so p is not twice differentiable at 1/2.

The nonsmooth finite energies can be replaced by REAL ANALYTIC convex energies:

    H_n(x)=n+log(1+exp(|x|^2-n)).

The scalar log(1+exp t) is convex, increasing, and real analytic, and |x|^2-n is convex. Hence H_n is convex and real analytic in x. Directly,

    Q_n <= H_n <= Q_n+log 2.

The normalized pressures differ by at most beta log(2)/n. They therefore have exactly the same non-C^2 limit (6.2). Since H_n>=|x|^2, their partition functions are holomorphic on Re beta>0 by dominated integration on compact subsets, and strictly positive for real beta>0. Applying the perspective proof in dimension n also gives Var(H_n)<=n/beta^2. Thus finite-volume real analyticity, convexity of smooth energies, an extensive variance bound at every temperature, and a finite C^{1,1} limit still do not imply analyticity. Additional structure of the Riesz interaction is essential.

## 7. A precise sufficient all-order condition (proved conditional theorem)

Fix beta_0>0 and suppose G_N from Section 5 converges pointwise to a finite G on a real neighborhood of beta_0. Suppose additionally there are A,B>0 independent of N such that, for every k>=2,

    |kappa_{k,N,beta_0}(H_N)| <= N A B^k k!.              (7.1)

Then G is real analytic on some neighborhood of beta_0.

Proof: finite-volume Z_N is holomorphic for Re z>0 by the domination argument of Section 4 and is positive at beta_0. It therefore has a local holomorphic logarithm. Its derivatives at beta_0 satisfy

    d^k/d beta^k log Z_N(beta_0)=(-1)^k kappa_k(H_N).

This identity follows by writing Z_N(beta_0+w)/Z_N(beta_0)=E_beta_0 exp(-w H_N) and differentiating the logarithmic moment-generating series. Cumulants here mean precisely the derivatives of that log moment-generating function at zero.

The constant Taylor coefficients of G_N converge. The linear coefficients G_N'(beta_0)=E(H_N)/N are uniformly bounded by the argument of Section 5. By (7.1), all higher Taylor coefficients have absolute value <=A B^k. Their formal Taylor series therefore define holomorphic functions T_N on |z-beta_0|<1/B, uniformly bounded on every smaller disk. Fix r<min(beta_0,1/B). Near beta_0, T_N equals the genuine G_N logarithmic germ. The identity

    Z_N(z)=exp[-N(T_N(z)-a_N)]

holds near beta_0 and then throughout |z-beta_0|<r by the holomorphic identity theorem. Thus Z_N is zero-free on that disk, and T_N is its normalized logarithmic branch there. On the real part of the disk, T_N is real by its real coefficients and equals G_N because the real exponential is injective.

Montel's theorem provides locally uniformly convergent subsequences of T_N on the disk. Every subsequential limit equals G on a real interval by pointwise convergence. Any two such holomorphic limits agree throughout by the identity theorem. It follows that G has a holomorphic extension, and its restriction to the real interval is real analytic. This proves the conditional theorem; (7.1) is NOT established for the Riesz gas.

The important quantifier improvement is that (7.1) is required at one temperature beta_0 for ALL orders, not initially on a real interval. Uniformity in volume remains essential. The source's two-gap covariance estimate is not a statement about k-point energy cumulants. Total energy depends on all particle-pair distances, has collision singularities, and after centering still has long-range dependence. No justified decomposition with uniformly controlled higher connected correlations was found here. Real MGF bound (4.2) scales as exp(O(Nt^2)); it cannot be converted by itself into (7.1). Section 6 supplies a concrete logical obstruction to such an inference.

## 8. Checks, scope, and remaining gap

Finite/algebraic formalization: Perspective.lean proves the scalar coordinate identity and the weight range used in Section 4. check_lean.py runs lake env lean on the absolute local path from ~/lean_verify, sequentially with a 3600-second subprocess timeout. Only narrow Mathlib imports are used. The initial file had a PowerShell UTF-8 BOM, removed before the mathematical check; an initial positivity proof needed explicit product-positivity facts, and a shell pipe corrupted newly inserted Unicode symbols, repaired before the final check. No sorry or native_decide is used. This checks algebra, NOT Prekopa's theorem, Jensen's inequality, or the infinite-volume analytic argument.

Numerical checks: numerics.py uses mpmath with 25 decimal digits, checks (2.1) against direct Hurwitz-zeta sums for s=0.2,0.5,0.8 and N=2,3,5,10; computes N=2 energy variance by deterministic quadrature at beta=0.25,1,4, and compares beta^2 Var(H_2) to the upper bound 1; evaluates the exact incomplete-gamma formula (6.1) for n=10,50,200 and beta=0.3,0.5,0.7. numerics.json records results. These finite checks are evidence against algebra/coding mistakes, not proofs or thermodynamic-limit tests for the Riesz gas.

Hostile-referee checkpoints:
- The ordered simplex has dimension N-1 after removing rotation. Using dimension N is safe but loses the precise constant. There is no gap-length density in this particle-rooted coordinate change.
- Global convexity holds on the ORDERED chamber, not on the entire labeled torus. That is sufficient because the partition reduces to that chamber.
- Singular collision energy does not invalidate Prekopa: the extended-real convex potential gives zero density outside its convex domain; dominated derivatives use the energy lower bound.
- The factor beta^{N-1} must be on the correct side: log(beta^d Z) concave gives Var-d/beta^2<=0.
- Entropy normalization is beta-independent, so derivatives and variance conclusions survive it. Literal (1.10) is not treated as a finite analytic function.
- C^{1,1} is weaker than C^2. Section 6 proves this gap can occur for smooth convex Gibbs energies.
- The negative-exponent displacement paper, trapped linear-statistic cumulants, and measure-variable free-energy convexity do not match the source's quantifiers.
- OpenAlex coverage is incomplete due to rate limits, and one Semantic Scholar title/ID was demonstrably mismatched. No literature closure is asserted.

Remaining mathematical gap: prove the extensive factorial energy-cumulant bound (7.1), or another volume-uniform complex-temperature analytic control, around EVERY beta_0>0 for the actual circular positive-exponent Riesz gas. Alternatively construct a genuine positive-temperature singularity for this very model. Neither is obtained here. Further two-point estimates or convergence of periodic laws alone do not fill the gap.

Final check results (2026-10-12): lake env lean exited 0; lean_check.txt has only unused/unreachable-tactic warnings from a redundant ring tactic. Both named theorems in Perspective.lean are kernel checked, without sorry. The maximum numerical ground-state identity discrepancy was 3.06e-15 (input powers were evaluated using ordinary floating-point parameters). All nine sampled N=2 variance ratios were below 1, ranging from 0.0136272 to 0.4183045. The convex-example finite pressures approached the proved limit from above; at n=200 the errors at beta=0.3,0.5,0.7 were approximately 0.0161118,0.0129049,0.00599918. No numerical fit is used as proof.


## 9. Second serious attempt at user request

See SECOND_ATTEMPT.md for two new approaches and a full neutral-cell polymer calculation. New proved result: with fixed s in (0,1), particles confined to disjoint radius-a lattice cells have a thermodynamic pressure holomorphic on the explicit disk |z|<1/(256D), where D=8a^2 s(s+1)(1-2a)^{-s-2} zeta(s+2). The all-order extensive factorial cumulant bound is proved for that restricted model. The proof checks the Kotecky-Preiss criterion, the periodic/interval comparison, and convergence of the logarithmic pressure.

A separate, explicit pressure comparison proves that sufficiently narrow cells miss an extensive part of the actual gas partition, even when the target beta lies in the restricted-model analytic disk. The source CLT also excludes bounded ordered lattice matching for its limiting process. Admitting occupation defects restores a nonsummable monopole tail. No transfer to the unrestricted gas is established. P0324 remains PARTIAL, not solved; the new remaining gap is an expansion or all-order cumulant control that accommodates those defects and unbounded collective displacements.
