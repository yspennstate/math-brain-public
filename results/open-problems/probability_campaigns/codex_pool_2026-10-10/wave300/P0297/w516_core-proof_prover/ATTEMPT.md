# P0297: Gaussian response of optimized LFPP lengths

Author w516, 2026-10-10. Author proofs below await w518's independent check. P0297 is unresolved. No novelty or formal-check claim is made.

## Exact target and assumptions

For each fixed gamma in (0,2), compute the deterministic almost-sure value d_gamma=dim_H(C,D_h), where h is the unit-circle-normalized whole-plane GFF and D_h is its gamma-LQG metric. This is the metric dimension, not the Euclidean dimension of a measure support. Positive deterministic rescaling of D_h does not change it. The known anchor is d_sqrt(8/3)=4. No simultaneous almost-sure assertion for uncountably many gamma is needed.

For heat-kernel-regularized h_epsilon, let L_epsilon(xi) be the infimum of integral exp(xi h_epsilon(z)) |dz| over left-right paths inside the unit square, and let a_epsilon be its median. Established input: a_epsilon=epsilon^(1-xi Q(xi)+o(1)); Q is continuous; xi=gamma/d_gamma and Q(xi)=2/gamma+gamma/2 in the subcritical regime. Put T=log(1/epsilon) and g(xi)=xi Q(xi)-1. At xi_*=1/sqrt(6), g(xi_*)=-1/6. These inputs are cited mathematical results, not proved here. Primary formulation: Ding-Dubedat-Gwynne, ICM 2022, equations (2.2)-(2.5) and Problem 5.1, https://ems.press/content/book-chapter-files/33292, CC BY 4.0. Original P0297 source independently recovered: Rhodes-Vargas, Two Decades of Probabilistic Approach to Liouville Conformal Field Theory, arXiv:2509.21053v1, Section 3, https://arxiv.org/html/2509.21053v1. The 2026 ICM primary publication https://epubs.siam.org/doi/10.1137/25M181012X still describes general d_gamma as unknown. Global current openness remains UNKNOWN beyond this scoped evidence.

## Prior-attempt digest checkpoint

Ranking row 554 records P0297 as tier 5, unsolved on 2026-09-07. Exact-ID and title searches in the named H/I attempts and Lean campaign found no target proof. The independently read intake aliases D0049 and D0052 share dedup_key lqg_hausdorff_dimension_d_gamma. Their unreviewed attempts are an obstruction digest (with a wrong d_gamma=2Q/xi string that w522 owns correcting) and exclusion of affine guesses by known bounds. Neither supplies a formula. Direct read-only population-store SQL retrieved the original P0297 problem and constant-shift attempt; both are unverified, and the attempt explicitly cannot calculate xi. PRIOR_ALIAS_ROWS.json and EXISTING_P0297_CARDS.json preserve these exact records. These scoped negative checks do not certify absence of any owner result. Team O's P0297 row has no claimant or kept bundle in the inspected board. The sharp-boundary triad's source pointers indicate a related D0049 normalization attempt; w516 is not repeating its KPZ optimization or correction computations. The independent-route triad is testing normalization/heat-kernel arguments. Our local lane is the finite Gaussian optimization response and its near-tie term.

The requested perceptron proof-gap scar was read from its named memory file. brain.py recall timed out after 60 seconds and its receipt is recall_mistakes.txt. A passed calculation will not be treated as closing the scale-limit gap.

## L1: exact finite Gaussian identity

Let X=(X_1,...,X_m) be centered Gaussian with covariance C (positive semidefinite). Let P be a nonempty finite collection of coefficient vectors a_p=(a_pi), a_pi>=0, each with at least one positive coefficient. For xi>0 define

    l_p = sum_i a_pi exp(xi X_i), f_p=log l_p,
    w_pi = a_pi exp(xi X_i)/l_p,
    pi_p = exp(-beta f_p)/sum_q exp(-beta f_q), beta>0,
    F_beta = -(1/beta) log sum_p exp(-beta f_p),
    bar_w = sum_p pi_p w_p,
    A_beta = sum_p pi_p [sum_i C_ii w_pi - w_p^T C w_p],
    B_beta = sum_p pi_p w_p^T C w_p - bar_w^T C bar_w.

Then

    d/dxi E F_beta = xi E[A_beta - beta B_beta].                 (L1)

In particular B_beta>=0, and

    B_beta = sum_{p<q} pi_p pi_q (w_p-w_q)^T C (w_p-w_q).

Also 0<=A_beta<=V, where V=max_i C_ii. The covariance includes all correlations; no independence of edge costs is assumed.

Proof. Finite differentiation gives partial_xi F_beta=sum_i bar_w_i X_i. Its absolute value is at most max_i |X_i|, permitting differentiation under expectation. Coordinate differentiation gives

    partial_{X_j} w_pi = xi w_pi(delta_ij-w_pj),
    partial_{X_j} pi_p = -beta xi pi_p(w_pj-bar_w_j),
    partial_{X_j} bar_w_i
      = xi [delta_ij bar_w_i - sum_p pi_p w_pi w_pj
             - beta(sum_p pi_p w_pi w_pj-bar_w_i bar_w_j)].

Gaussian integration by parts E[X_i u(X)]=sum_j C_ij E[partial_j u(X)] now yields L1. This identity also holds for singular C by writing X=C^(1/2)Z. Derivatives are bounded for fixed beta,xi, so this application is integrable. B_beta is a covariance variance, hence nonnegative; expanding the square proves its pair form. For any probability vector w,

    sum_i C_ii w_i - w^T C w
      = (1/2)sum_ij w_i w_j(C_ii+C_jj-2C_ij)>=0,

and it is at most V since w^T C w>=0. Averaging proves the bound for A_beta. This completes L1.

## L2: the path-switching term survives zero temperature

For this lemma assume C is positive definite and remove duplicate coefficient vectors a_p. Then for every fixed xi>0 the minimizing p_*(X,xi) of f_p is unique almost surely. Define F=min_p f_p, f(xi)=E F, and

    A_*(xi,X)=sum_i C_ii w_{p_*i}-w_{p_*}^T C w_{p_*},
    S(xi)=lim_{beta->infinity} beta E B_beta.

The limit exists, is finite and nonnegative, f is continuously differentiable on (0,infinity), and

    f'(xi)=xi(E A_*(xi)-S(xi)),  hence f'(xi)<=xi V.             (L2)

Proof. Distinct coefficient vectors give distinct real analytic functions f_p-f_q on R^m: the underlying difference is sum_i(a_pi-a_qi) exp(xi X_i), which is not identically zero. Its zero set has Lebesgue measure zero; a nondegenerate Gaussian has a density. Finite union proves uniqueness. At a unique minimizer the envelope derivative of F in xi is sum_i w_{p_*i} X_i. F is Lipschitz in xi on each sample with constant max_i |X_i|, so dominated difference quotients prove the formula for f'. The same domination, with uniqueness at any fixed limiting xi, proves continuity of f'.

As beta tends to infinity, pi concentrates on p_* almost surely. Thus partial_xi F_beta tends to partial_xi F with an integrable bound max_i|X_i|, while A_beta tends to A_* and is bounded by V. Rearranging L1 gives

    beta E B_beta=E A_beta-(d/dxi E F_beta)/xi.

Both right-hand terms converge, proving existence, finiteness and the formula for S. Nonnegativity follows before taking the limit. No interchange between beta and a vanishing regularization scale was used.

The error to avoid is applying integration by parts to the discontinuous zero-temperature weights using only their derivative inside the selected path. The envelope formula for the FIRST derivative is valid. It is the subsequent field differentiation of the optimizer weights that has an additional switching contribution.

## L3: an exact counterexample and a useful control

Take two parallel edges of base length one, with independent standard normal X_1,X_2. Then F=xi min(X_1,X_2). Since min(X_1,X_2)=(X_1+X_2-|X_1-X_2|)/2 and X_1-X_2 is N(0,2),

    f'(xi)=-1/sqrt(pi), A_*=0, S(xi)=1/(xi sqrt(pi)).          (L3)

Dropping S predicts derivative zero and loses the entire derivative. Pointwise B_beta tends to zero, yet beta E B_beta has a positive limit. Dominated convergence for beta B_beta is therefore unjustified.

More generally for two single-edge paths with offsets c_1=log a_1, c_2=log a_2 and Gaussian difference variance sigma^2>0, S(xi)=sigma phi((c_1-c_2)/(xi sigma))/xi, where phi is the standard normal density. To check: E F=(c_1+c_2)/2-(1/2)E|c_1-c_2+xi Z| with Z~N(0,sigma^2); differentiation or the normal density gives f'=-sigma phi((c_1-c_2)/(xi sigma)); A_*=0. This is a proved finite model, not an LQG dimension calculation.

Adding an independent common Gaussian offset changes C to C+c 11^T, c>=0. Both A_beta and B_beta remain unchanged because every w_p sums to one. Correspondingly the expected log minimum length is unchanged. This is a control for covariance and normalization errors.

## L4: mean-median bridge and finite approximations

For a finite model with covariance C, the almost-everywhere field gradient of F is xi w_{p_*}. Its Gaussian gradient norm satisfies xi^2 w^T C w<=xi^2 V. The Gaussian Poincare inequality therefore gives Var(F)<=xi^2 V. For any median M of F, at least half the probability lies on the relevant side of M, so Var(F)>=(1/2)|E F-M|^2. Consequently

    |E F-M|<=xi sqrt(2V).                                    (L4a)

This statement also follows by smoothing with F_beta and passing to the limit in L2. It makes no independent-edge assumption.

For heat-smoothed GFF on the unit square K, V_epsilon=sup_{z in K} Var h_epsilon(z)=T+O(1), obtained by integrating its logarithmic covariance against two heat kernels. The bounded covariance terms stay bounded on K; rescaling the singular log term produces log(1/epsilon). The regularized field is smooth, and its supremum on K has finite second moment.

Here is a constructive theoretical finite approximation, rather than an unsupported identification with a fixed-direction lattice metric. Enumerate polygonal left-right paths with rational vertices in K, including a unit horizontal segment, and approximate their weighted integrals with finite Riemann sums. At fixed epsilon, the infimum over these paths equals the continuum infimum: polygonal approximation of a piecewise C1 path preserves weighted length for a positive continuous weight; rational vertices can then be used. The finite-path minima decrease to this infimum. On each compact xi interval I=[a,b] subset (0,infinity), their log lengths are uniformly Lipschitz in xi with constant ||h_epsilon||_infinity, and their absolute values are at most b||h_epsilon||_infinity. Thus the convergence is uniform on I, first samplewise and then in L2 by domination. The Riemann-sum log error is at most b times the field modulus of continuity at the largest subsegment length, so it tends uniformly to zero in L2 too.

Merge repeated sampling sites into common Gaussian coordinates and remove identical coefficient vectors. If the resulting covariance is singular, add independent coordinate noises with arbitrarily small variance: |F(X+noise)-F(X)|<=b max_i|noise_i|. For the finite number of sites the noise can be chosen to have arbitrarily small L2 maximum, and makes C positive definite. This is a mathematical approximation, not an assertion that independent noise models LQG.

Given epsilon_n->0, choose finite-path and quadrature accuracies and these auxiliary noises so that

    || sup_{xi in I}|F_n(xi)-log L_{epsilon_n}(xi)| ||_2<=1/n,
    V_n=max_i C_{n,ii}=T_n+O(1).

The same approximation passes the Poincare variance bound to the continuum log crossing. Since log is increasing, log a_epsilon is a median of log L_epsilon. L4a and the established median exponent therefore imply for every fixed xi in I

    E F_n(xi)/T_n -> g(xi)=xi Q(xi)-1.                        (L4b)

No mesh direction restriction or exchange of xi differentiation with n->infinity is assumed. The approximation is existential; no large graph was computed here.

## L5: an exact measure reduction, with its unsolved input visible

For the above finite approximants let A_{n,*}, S_n be L2 quantities and put

    g_n(xi)=E F_n(xi)/T_n,
    Psi_n(xi)=(V_n/T_n)xi^2/2-g_n(xi),
    d mu_n(xi) = [xi/T_n][V_n-E A_{n,*}(xi)+S_n(xi)] dxi.

By L2, mu_n=dPsi_n is a nonnegative measure. L4b implies Psi_n converges pointwise to the continuous nondecreasing function

    Psi(xi)=xi^2/2-g(xi).

Hence mu_n converges weakly on every compact interior interval to the Lebesgue-Stieltjes measure mu=dPsi. One proof uses integration by parts against compactly supported smooth functions: monotonicity bounds Psi_n by its endpoint values, so dominated convergence applies to the function integrals. Interval masses converge as well since Psi is continuous. This identifies a measure without assuming g is differentiable or mu has a density.

For xi>xi_* in the subcritical interval, the exact reduction is

    g(xi)=-1/6+(xi^2-1/6)/2-mu((xi_*,xi]).                    (L5)

For xi<xi_*, use +mu((xi,xi_*]) instead. An explicit computation of these masses determines Q(xi)=(g(xi)+1)/xi and then d_gamma=gamma/xi for the unique subcritical xi satisfying Q(xi)=2/gamma+gamma/2. This last inversion uses the established strictly increasing relation gamma->xi.

The SINGLE hardest remaining input is H: explicitly evaluate the limiting measure mu from the near-tie/geodesic-occupation expression for mu_n. L1-L5 do not evaluate it. They expose both the within-path covariance contribution V_n-E A_{n,*} and the switching contribution S_n. Either may survive at order T_n. Calling H an identity for a known constant would simply assume the target exponent.

## Attempt on H: what follows, and where it stops

Positivity alone yields, for xi>xi_*,

    g(xi)<=xi^2/2-1/4,  Q(xi)<=3/(4xi)+xi/2,

with the inequality reversed for xi<xi_*. These are comparison bounds, not exact exponents. At a continuous critical endpoint with Q(xi_crit)=2, xi_crit>xi_* and xi_crit<1, the upper comparison yields xi_crit<=2-sqrt(5/2)=0.4188611699... . This numerical bound is a comparison consequence; its novelty is not asserted.

To go further, the pair formula in L1 requires the density of alternatives whose log lengths differ by order 1/beta, weighted by their squared covariance distance. The exact two-edge computation shows this density controls a finite nonzero contribution even though ties have probability zero. Replacing it by an almost-sure uniqueness argument fails. Replacing correlated path lengths by independent lengths is not authorized by the GFF covariance. Treating a finite graph's response as the limiting LQG response without L4-L5 also fails.

We have no estimate that determines mu's masses, no argument for an explicit density, and no exact generic d_gamma. L6 below supplies a conditional two-route density formula. The next concrete proof step is a multi-route screening and weighted-density remainder estimate uniform in the regularization scale; that uniform control is still unproved.

## L6: the two-route weighted near-tie density

Fix xi>0 and two coefficient vectors in L1. Set Delta=f_1-f_2 and D=(w_1-w_2)^T C(w_1-w_2). Define the weighted gap law nu(E)=E[D 1_{Delta in E}]. Assume that on some neighborhood (-delta,delta), nu has a density r(t) continuous at zero. No independence between D and Delta is assumed. Then

    S(xi)=r(0).                                               (L6)

Proof. With k(u)=e^u/(1+e^u)^2, pi_1 pi_2=k(beta Delta), so beta E B_beta=beta integral k(beta t) nu(dt). The contribution from |t|>=delta is at most beta exp(-beta delta) E D, which tends to zero; E D<=4V. On |t|<delta, change variables u=beta t. Continuity makes r bounded on a smaller neighborhood. Dominated convergence against the integrable k(u), whose integral is one, yields r(0); the intervening compact region away from zero is handled by the same exponential tail estimate. This proves L6. The assumption is a weighted density condition, not merely a density for unweighted path lengths.

For the two single-edge paths of L3, D=sigma^2 is constant and Delta=c_1-c_2+xi Z, so r(0)=sigma phi((c_1-c_2)/(xi sigma))/xi, agreeing with the direct Gaussian calculation.

This provides a precise possible input for H. It does not establish a uniform weighted density for the increasing multi-route LFPP family, screen additional almost-minimal paths, or compute mu. The next concrete proof step is to control the multi-route screening remainder and the weighted gap densities uniformly in n, rather than infer their order from uniqueness of the minimum.
