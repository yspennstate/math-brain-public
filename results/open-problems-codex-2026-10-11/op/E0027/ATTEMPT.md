# E0027: mathematics and referee audit

Date: 2026-10-12. Result: PARTIAL. The unrestricted question remains unanswered in this attempt.

## 1. Exact question and conventions

For every n >= 1, let X,Y be independent R^n-valued Levy processes, each satisfying Hunt's hypothesis (H): every semipolar set is polar. Must Z=X+Y satisfy (H)? There is NO assumption of resolvent densities, transition densities, Gaussian nondegeneracy, or a sector bound.

Write E exp(i<z,X_t>)=exp(-t psi_1(z)) and similarly for Y. Independence of the entire processes gives psi_Z=psi_1+psi_2, by multiplying the characteristic functions of every independent increment. Put r_i=Re psi_i >= 0, u_i=Im psi_i,

    A_i=1+r_i, B_i=|1+psi_i|,
    A=1+r_1+r_2, B=|1+psi_1+psi_2|.

For a finite positive measure nu, its 1-energy is, up to an irrelevant positive Fourier normalization,

    E_1^X(nu)= integral [A_1/B_1^2] |hat nu|^2 dz.

We use two verified published results as input, not reprove all potential theory here:

* Survey Theorem 2.3, PDF p. 4 (Rao 1988, Theorem 2): under resolvent densities, an increasing positive f with integral_1^infinity ds/(s f(s))=infinity and B <= A f(A) implies (H).
* Survey Proposition 2.13, PDF p. 8: under resolvent densities (equivalently the stated lower semicontinuity of all 1-excessive functions), (H) is equivalent to

      lim_{lambda -> infinity} integral lambda/(lambda^2+B(z)^2) |hat nu(z)|^2 dz = 0

  for every finite positive nu of finite 1-energy.

All deductions below identify where these inputs are used. None is a proof of the unrestricted assertion.

## 2. Common Rao envelope: proved special case

Proposition. Assume Z has resolvent densities. Let f:[1,infinity)->[1,infinity) be finite-valued and nondecreasing, with integral_N^infinity ds/(s f(s))=infinity for every N>=1. Suppose, for constants C_1,C_2>=0,

    |u_i(z)| <= C_i A_i(z) f(A_i(z)), i=1,2.

Then Z satisfies (H). To interpret this as a subclass of the question, one can also require resolvent densities for X and Y; Rao then gives (H) for both as well.

Proof. A_i<=A. Hence monotonicity and nonnegativity give

    |u_1+u_2| <= C_1 A_1 f(A_1)+C_2 A_2 f(A_2)
                <= (C_1+C_2) A f(A).

For a positive a and real u, sqrt(a^2+u^2)<=a+|u|. Consequently

    B <= A+|u_1+u_2| <= (1+C_1+C_2) A f(A).

Set F=(1+C_1+C_2)f. It remains increasing and positive and its reciprocal integral is the given infinite integral divided by a fixed finite positive constant. Rao's theorem, with the explicitly assumed resolvent densities of Z, proves the claim. This includes two Kanda-Forst bounds by taking f=1. It also includes one common envelope 1+log s. End proof.

A sufficient way to supply the density assumption is that one summand has transition densities at EVERY t>0. Indeed, if N is a Lebesgue-null Borel set, independence gives

    P(X_t+Y_t in N)=integral P(X_t in N-y) P(Y_t in dy)=0.

Every translate N-y is null, so the integrand is zero for every y. Thus Z_t is absolutely continuous for every t>0; integrating exp(-alpha t) P(Z_t in N) over t proves absolute continuity of each resolvent. This argument concerns transition densities, not just resolvent densities.

## 3. An explicit obstruction to merging two arbitrary Rao envelopes

Proposition. There exist two finite positive nondecreasing functions f_1,f_2 on [1,infinity), each satisfying integral_N^infinity ds/(s f_i(s))=infinity for every N>=1, but

    integral_1^infinity ds/[s(f_1(s)+f_2(s))] < infinity,
    integral_1^infinity ds/[s max(f_1(s),f_2(s))] < infinity.

In particular there need not exist a positive admissible common majorant F>=f_1,f_2.

Construction and full proof. Work in t=log s, so ds/s=dt. Put M_0=1, M_j=2^j M_{j-1}=2^{j(j+1)/2}, T_0=0 and T_j=T_{j-1}+M_{j-1} for j>=1. These strictly increasing T_j tend to infinity since each increment is at least 1. On block [T_{j-1},T_j), define

    (h_1,h_2)=(M_j,M_{j-1}) if j is odd,
               (M_{j-1},M_j) if j is even.

At the first block both values are >=1. At an odd-to-even transition, h_1 stays at the old M_j and h_2 increases from M_{j-1} to M_{j+1}; at an even-to-odd transition the roles reverse. Hence both h_i are nondecreasing. They are finite at each finite t because the blocks have no finite accumulation. Define f_i(s)=h_i(log s).

On each odd block integral dt/h_2 = M_{j-1}/M_{j-1}=1. On each even block integral dt/h_1=1. There are infinitely many blocks of each parity beyond any finite t, proving both required divergences, including every lower endpoint N.

On every block,

    integral dt/(h_1+h_2)=1/(1+2^j) <= 2^{-j},
    integral dt/max(h_1,h_2)=2^{-j}.

Summing over j>=1 gives the first integral <=1 and the second exactly 1. For any F>=max(f_1,f_2), its reciprocal integrand is at most that for the maximum, so its integral is finite. This proves the nonexistence of an admissible common majorant. End proof.

Here 'increasing' is used in its standard nondecreasing sense. Even if strict increase is desired, replace f_i(s) by f_i(s)+s/(1+s). This adds a bounded strictly increasing function between 0 and 1. Since f_i>=1, the new f_i is at most 2 f_i, so the individual integrals still diverge, while their sum and maximum still have finite reciprocal integrals.

REFEREE LIMIT: these are envelope functions, not characteristic exponents. No Levy processes attaining these envelope profiles have been constructed here. A process with a loose envelope may admit another, smaller envelope. Thus the construction refutes an envelope-combination inference in the earlier intake attempt E0027-A001; it does not show that the class of processes admitting some Rao envelope fails closure, and does not refute (H)-stability.

## 4. A dominated perturbation theorem, with complete scalar proof

Proposition. Assume X and Z=X+Y both have resolvent densities, X satisfies (H), and for some c>=0,

    |psi_2(z)| <= c(1+Re psi_1(z)) for every z.

Then Z satisfies (H). This is already a published special case: Hu-Sun 2018, Theorem 4.1 plus Proposition 4.2(i), arXiv PDF p. 14. The calculation below is an independent check, not a novelty claim. Notice that no separate (H) assumption on Y is needed for this proposition.

Proof. Fix z and abbreviate a=1+r_1>=1, b=r_2>=0, u=u_1, v=u_2. The hypothesis implies b<=ca and |v|<=ca. Let

    D_1=a^2+u^2, D=(a+b)^2+(u+v)^2,
    K=(1+c)^2+2c^2+2, L=2c^2+2.

Both denominators are strictly positive and K,L>=1. Since (u+v)^2<=2u^2+2v^2 and (a+b)^2<=(1+c)^2a^2,

    D <= [(1+c)^2+2c^2] a^2+2u^2 <= K D_1.

Therefore

    a/D_1 <= K(a+b)/D,

because D<=K D_1 and a<=a+b. For any finite measure of finite energy for Z, multiplication by |hat nu|^2 and integration proves finite energy for X. Positivity makes this implication valid even before finiteness is known.

For the second comparison, u=(u+v)-v gives u^2<=2(u+v)^2+2v^2. Also a^2<=(a+b)^2 and v^2<=c^2(a+b)^2, so

    D_1 <= (1+2c^2)(a+b)^2+2(u+v)^2 <= L D.

For every lambda>0 this implies

    lambda/(lambda^2+D) <= L lambda/(lambda^2+D_1),

since lambda^2+D_1 <= L(lambda^2+D). Thus the criterion integral for Z is bounded above by L times the corresponding one for X. The latter tends to zero by (H) for X and the energy inclusion already proved. The integral for Z is nonnegative, so it tends to zero as well. Apply survey Proposition 2.13 to Z, using its assumed resolvent densities, to conclude (H). End proof.

The squared-denominator algebra is formalized in ScalarChecks.lean. This is only scalar algebra; Lean does not formalize the probabilistic criterion or this entire theorem.

## 5. Energy inclusion is not automatic, even for two (H) processes

Take independent symmetric stable processes on R with psi_1(z)=|z|^(1/2), psi_2(z)=|z|^(3/2). Each satisfies (H): its characteristic function exp(-t|z|^alpha) is integrable for every t>0, so Fourier inversion supplies bounded continuous transition densities; its imaginary part is zero; the Kanda-Forst theorem applies. The sum likewise has these densities and zero imaginary part, and also satisfies (H).

For nu=delta_0, |hat nu|=1. Its energy for X is infinite: for z>=1,

    1/(1+sqrt(z)) >= 1/(2 sqrt(z)),

whose integral to infinity diverges. Its energy for Z is finite: the integrand is at most 1 on [-1,1], and for |z|>=1 it is at most |z|^(-3/2), which is integrable. Consequently finite energy for Z does not imply finite energy for X, although both summands and Z satisfy (H). This is an actual counterexample to a proposed automatic energy-inclusion lemma, not a counterexample to the question. Swapping the roles in this example permits inclusion; it does not disprove all possible transfer arguments.

### 5.1 The same energy measure can fail for BOTH summands

Here is a stronger obstruction to repairing Section 5 by simply choosing the other summand. In R^2 take alpha=1/2, beta=3/2 and independent processes with real exponents

    psi_1(z_1,z_2)=|z_1|^alpha+|z_2|^beta,
    psi_2(z_1,z_2)=|z_1|^beta+|z_2|^alpha.

Construct each from two independent one-dimensional symmetric stable coordinates; construct the two processes independently of each other. The product stable densities at every t>0 are bounded and continuous. Their imaginary exponents vanish, so both satisfy (H) by Kanda-Forst. The sum has a bounded continuous density by convolution (bounded uniform continuity follows, for example, from the integrable characteristic function); its imaginary exponent is again zero, so it also satisfies (H).

Let G have centered Gaussian law of variance 2. Let nu_h be the law of (G,0), nu_v the law of (0,G), and nu=nu_h+nu_v, a finite positive measure of total mass 2. Its Fourier transform is

    hat nu(z_1,z_2)=exp(-z_1^2)+exp(-z_2^2).

On the strip |z_2|<=1, z_1>=1, its square is at least exp(-2), while

    1+psi_1 <= 2+sqrt(z_1) <= 3 sqrt(z_1).

Thus its psi_1 energy is bounded below by a fixed positive constant times integral_1^infinity z_1^(-1/2) dz and is infinite. On the strip |z_1|<=1, z_2>=1, the same reasoning proves infinite psi_2 energy.

On the other hand, 1+psi_1+psi_2 >= 1+|z_1|^beta+|z_2|^beta and

    |hat nu|^2 <= 2 exp(-2 z_1^2)+2 exp(-2 z_2^2).

The first term in the energy integral is at most

    2 [integral_R exp(-2z_1^2) dz_1]
      [integral_R 1/(1+|z_2|^beta) dz_2],

which is finite because beta>1; the second term is finite by the swapped estimate. Hence nu has finite energy for the sum and infinite energy for each summand. All integrals are nonnegative, so Tonelli applies without hidden integrability assumptions. This is an actual counterexample to the lemma that a sum-energy measure must have finite energy for at least one of two (H) summands, with resolvent densities for all three processes. It is still NOT a counterexample to Question 7: the sum satisfies (H).

## 6. Resolvent densities alone do not automatically pass to sums

Let X_t=t and Y_t=-t be deterministic processes on R, treated as independent (their sigma-fields are trivial). At starting point 0 their alpha-resolvents are

    R_alpha^X(dx)=exp(-alpha x) 1_{x>0} dx,
    R_alpha^Y(dx)=exp(alpha x) 1_{x<0} dx.

This follows by substituting x=t or x=-t in integral_0^infinity exp(-alpha t)g(X_t)dt. At every other starting point they are translated densities. But X+Y=0 has resolvent alpha^(-1) delta_0, which is singular. In fact, Y alone suffices as a counterexample to the claim that a sum inherits resolvent densities whenever one summand has them.

Both nonzero deterministic drifts fail (H), as shown by the hyperplane argument in Section 8 in dimension one. Thus this example does NOT settle whether extra (H) assumptions might force density inheritance. It explains why no such inference is used in Sections 2 or 4.

## 7. Proportional exponents: a special case without densities

Proposition. If Y is independent of X and psi_Y=c psi_X with c>=0, and X satisfies (H), then X+Y satisfies (H).

Proof. The sum has exponent (1+c)psi_X. Hence its law as a Levy process is the law of W_t=X_{(1+c)t}: stationary independent increments identify all finite-dimensional distributions; the cadlag path law is determined by these distributions on rational times. Under the coupling defining W, for every hitting set D,

    T_D^W=T_D^X/(1+c),

including zero and infinity. The bijective continuous deterministic time reparametrization preserves the nearly Borel admissibility of hitting sets (equivalently, their hitting events under the corresponding path laws). Thus the conditions defining thin and polar sets agree under X and W at every starting point. Semipolar sets, being sets covered by countably many thin sets, agree as well. Therefore (H) is invariant under this positive constant change of time. In particular an independent sum of any finite number of copies of X satisfies (H). End proof.

## 8. All Gaussian Levy summands, including degenerate ones

Let X_t=b t+Q^(1/2)B_t for a symmetric positive semidefinite matrix Q. Put S=range Q=range Q^(1/2). We verify that X satisfies (H) exactly when b belongs to S.

Necessity. If b is not in S, choose a linear functional ell annihilating S but with ell(b)=1. Along every path started from x, ell(X_t)=ell(x)+t. The closed hyperplane D={ell=1} has first hitting time 1-ell(x) when ell(x)<1, and infinity when ell(x)>=1. In particular this time is never zero at any starting point: D is thin. Starting at x=0, D is hit at time 1 with probability 1, so it is not polar. This violates (H).

Sufficiency. If dim S=0, then b=0 and the process is constant. A thin set cannot contain any point x, because from x its positive-time hitting infimum would be zero; hence only the empty set is thin and (H) holds. If dim S=k>0 and b lies in S, the process stays on the coset x+S from any x. On that coset it is a k-dimensional nondegenerate Gaussian Levy process. Its real exponent is at least m|z|^2/2 for some m>0; its imaginary exponent is bounded by |b||z|, which is bounded by a constant times 1+m|z|^2/2 (use |z|<=1+|z|^2). It has bounded continuous Gaussian transition densities on the coset. Kanda-Forst proves (H) for the restricted process. To pass to R^n, let D be thin for the full process, with a nearly Borel thin witness C. Intersect C with each invariant coset; the restricted hitting events are the same, so each intersection is thin for the restricted process. For a semipolar set use the countable thin cover and restrict each witness to the coset. The restricted (H) property makes this cover polar from every starting point in that coset. Every starting point belongs to one such coset; thus the original set is polar for the full process. This proves sufficiency.

Now suppose Gaussian X,Y both satisfy (H), with drifts b_1,b_2 and covariance matrices Q_1,Q_2. Then b_i is in range Q_i. Their independent sum has covariance Q_1+Q_2 and drift b_1+b_2. For positive semidefinite matrices,

    ker(Q_1+Q_2)=ker Q_1 intersection ker Q_2.

Indeed, z^T(Q_1+Q_2)z=0 is a sum of two nonnegative quadratic forms; each must vanish; diagonalization of a positive semidefinite matrix shows that its quadratic form vanishes exactly on its kernel. Conversely belonging to both kernels implies belonging to the kernel of their sum. Taking orthogonal complements yields

    range(Q_1+Q_2)=range Q_1+range Q_2.

Therefore b_1+b_2 belongs to range(Q_1+Q_2), and the already proved characterization implies (H) for the sum. This rules out a Gaussian counterexample, even with singular covariance matrices. This also follows from the source's Theorem 2.15; no novelty is claimed.

## 9. Product reduction and the exact outstanding gap

The source's Lemma 3.1 proves that orthogonal projections of a Levy process satisfying (H) satisfy (H). Thus a positive answer to independent-product stability would imply sum stability: apply it to (X,Y), project R^(2n) onto the diagonal, and identify that diagonal with R^n (the resulting process is a nonzero constant spatial rescaling of X+Y). The product-stability assertion is itself the source's open Question 4'. It is not an available theorem.

For processes with resolvent densities, a concrete sufficient route is: for every finite positive measure nu of finite energy for Z, prove that its Z criterion integral in Section 1 tends to zero. Section 4 achieves this via energy inclusion and control of the second imaginary part. Section 5.1 proves that a single finite-energy measure for the sum can have infinite energy for both summands, even when all three processes satisfy (H) and have resolvent densities. The general question additionally has no density assumption, so even proving the criterion statement in the density setting would leave an additional case.

Unresolved: there is neither a proof that the original (H)+(H) premises imply (H) for the sum, nor an independent pair satisfying those premises with a semipolar nonpolar set for the sum. The envelope obstruction is not realized as such a pair. We do not assert that arbitrary processes each admitting some Rao envelope fail closure; only the particular common-majorant inference is refuted.

## 10. Hostile-referee checks

* Independence is used to add exponents; equality of individual one-time laws alone is insufficient without independence of the processes.
* Density hypotheses are explicitly retained. Section 6 forbids the naive resolvent inheritance step; Section 2 supplies a valid transition-density argument.
* Distinct Rao envelopes cannot automatically be merged: Section 3 proves the obstruction without relying on numerics.
* Energy inclusion is proved before applying the criterion in Section 4. Section 5 tests the necessity of this check on actual (H) stable processes.
* Denominators are strictly positive since a>=1; c=0 is allowed and causes no division by c. The constants K,L are finite and at least 1.
* The criterion limit passes by a pointwise integral inequality, not by an unjustified dominated convergence argument.
* All numerical checks are of algebra, not simulations of polarity. exact_checks.py tests 4,000 rational tuples and three lambda values each, and 24 exact envelope blocks. Results are in checks.json.
* Lean checks only the universal squared-denominator inequalities; the final checker output and axiom list are in lean_check.log. No stochastic assertion is described as formally verified.
* Thin sets use infimum over t>0. For the drift hyperplane, starting in the hyperplane gives infinite return time, not time zero. The constant-process case has infimum zero when started at a point in the set.
* No failed API search is counted as evidence of no published solution. Citation searches cover both the arXiv and journal identities of the survey.

## 11. Completed verification results

Lean completed successfully on the final ScalarChecks.lean (exit 0, about 243 seconds). Each of square_add_bound, energy_denominator_bound, and norm_transfer_bound lists only the standard axioms propext, Classical.choice, and Quot.sound. The file has no sorry, admitted assertion, native_decide, or unchecked native computation. The initial compile failed because PowerShell's stdin encoding changed Unicode symbols to question marks; replacing these with ASCII Lean notation corrected the source before the successful check.

The 4,000 exact rational denominator/energy/kernel checks all passed. For the envelope example, after 24 blocks the two reciprocal integrals are approximately 12.666667 and 12.333333, while that of their sum is about 0.764500 and that of their maximum is 0.99999994. Infinite divergence and convergence are proved in Section 3, rather than inferred from these values.

For the Section 5.1 energy obstruction, energy_quadrature.py used an 821-by-821 grid, far below 1 GB, for each square cutoff. The unnormalized truncated energies for X and Y agree to rounding. At R=10,100,1000,10000 they are approximately 14.6247,43.9516,145.7336,481.3029 for each summand; for the sum they are approximately 7.5373,9.5691,10.2511,10.4679. These are quadrature values without rigorous error bars. The exact proof, not quadrature, establishes infinite individual energies and finite sum energy. Reproduction data are in energy_quadrature.json.

This attempt is closed as PARTIAL. A concrete next research direction is to determine whether the measure-dependent C_log/C_log-log criteria can be transferred to the sum without energy inclusion into either summand. The original (H)+(H) implication, especially without resolvent densities, is still the precise remaining problem.

## 12. Reopened attempt

2026-10-12: A user-requested renewed attempt is recorded in SECOND_ATTEMPT.md. Its two new routes are transfer of integrable EKFR remainders with a cancellation split, and local absolute continuity of Levy laws. STATE is WORKING during this attempt.

## 13. Renewed attempt completed

2026-10-12: See SECOND_ATTEMPT.md for the two new approaches, full cancellation-split EKFR theorem, same-sign corollary, free scalar obstruction (not Levy exponents), and density-free local-absolute-continuity comparison. The first route avoids energy inclusion but still needs a common decomposition and control of exceptional cancellation frequencies. The second forces finite variation in the added jump component. All new exact checks passed; the corrected three-lemma Lean file has exit 0 and no sorryAx. The original unrestricted question remains unresolved. Final STATE: DONE; VERDICT: PARTIAL.
