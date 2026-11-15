# The outer reduction in the diluted lower bound

The assertion checked here is a reduction: the bounded, permutation-invariant cavity inputs described in Section 5 imply the integrable admissible-model lower bound. Those inputs are assumed in this note, not proved. This does not establish the Mézard–Parisi formula.

Write p >= 2 for the arity and alpha > 0 for the clause density. Let theta be a random real function on {-1,1}^p and h an independent field, with

\[
\mathbb E\|\theta\|_\infty+\mathbb E|h|<\infty.
\]

Let F_N be the counting-measure expected pressure with Pois(alpha N) independent clauses and independent uniform endpoints, and let B_M(r,zeta,m) be the hierarchical trial functional defined in the manuscript. The exponent vector satisfies 0 < m_1 < ... < m_r < 1; r=0 is permitted.

## 1. Centering gives the required permutation symmetry

Suppose the admissibility factorization holds almost surely, simultaneously for all spin tuples:

\[
e^{\theta(s)}=a\left(1+b\prod_{l=1}^p f_l(s_l)\right),
\qquad a>0,\qquad \left|b\prod_l f_l(s_l)\right|<1.
\]

Put c=theta(+1,...,+1) and theta_hat(s)=theta(s)-c. Each logarithm below is of a positive number. Taking logarithms at s and at the all-plus tuple and subtracting gives

\[
\widehat\theta(s)=
\log\left(1+b\prod_l f_l(s_l)\right)
-\log\left(1+b\prod_l f_l(+1)\right).
\tag{1}
\]

The multiplier a cancels pointwise. There is no expectation of log a in this argument.

For a permutation e of the p coordinates, replace f_l by f_{e^{-1}(l)} in (1). Reindexing each product shows that the resulting function is theta_hat(s composed with e). The joint law of (b,f_1,...,f_p) is unchanged: the f_l are independent and identically distributed as random two-point functions, and b is independent of their whole vector. Therefore theta_hat is permutation invariant in law. Dependence of a on b or on any of the labeled f_l is irrelevant after (1).

Also |c| <= ||theta||_infinity and ||theta_hat||_infinity <= 2||theta||_infinity. Hence c and theta_hat have the required first moments. The evenness and moment-positivity assumptions used by the upper bound are not needed in this centering step.

## 2. Pressure and trial functional have exactly the same shift

For each realization with k clauses, replacing theta_j by theta_j-c_j subtracts sum_j c_j from every log Boltzmann weight. Factoring exp(-sum_j c_j) out of the partition sum yields

\[
\log Z_N(\widehat M)=\log Z_N(M)-\sum_{j=1}^k c_j.
\]

Condition on k, average the independent clauses, and use E k=alpha N. For every N>=1,

\[
F_N(\widehat M)=F_N(M)-\alpha\mathbb E c.
\tag{2}
\]

For a probability measure mu and a positive exponent m, define P_m(g)=m^{-1} log integral exp(mg) dmu. If t is constant with respect to this integral, factoring exp(mt) gives P_m(g+t)=P_m(g)+t. Applying this identity successively at every hierarchy level, then taking the root expectation, proves translation covariance of the entire hierarchy. For r=0 it follows directly from ordinary expectation. Physical disorder is held fixed during these operations, so a random physical c is such a constant at each hierarchy level.

At an edge insertion, theta -> theta-c subtracts c from log V_e. At a site insertion with k physical clauses, it subtracts sum_j c_j from every message sum and thus from log V_s. Consequently the site term of the functional shifts by -alpha p E c, while the subtracted edge term shifts by +alpha(p-1) E c. Therefore

\[
B_{\widehat M}(r,\zeta,m)
=B_M(r,\zeta,m)-\alpha\mathbb E c.
\tag{3}
\]

All expectations are finite. Indeed, |log V_e| <= ||theta||_infinity and |log V_s| <= |h|+sum_j ||theta_j||_infinity; power means preserve these bounds. The finite-volume inequality |log Z_N-N log 2| <= sum_j ||theta_j||_infinity+sum_i |h_i| also gives uniform boundedness of F_N. Thus liminf in (2) is a finite real number and has the same shift. Equations (2) and (3) cancel that shift in a lower-bound inequality.

As a separate sign check, take the constant clause theta=t and zero field. Directly, F_N=log 2+alpha t. Centering makes every clause zero and gives log 2. The trial functional has shift alpha p t-alpha(p-1)t=alpha t. This checks the same coefficient without using (2) or (3).

## 3. Uniform first-moment stability

Couple two models M and M' with the same density, endpoint draws and clause count, and coupled clause functions and fields. Set

\[
D=\mathbb E\|\theta'-\theta\|_\infty,
\qquad d=\mathbb E|h'-h|.
\]

For each spin configuration the absolute change of its log weight is at most sum_j ||theta'_j-theta_j||_infinity + sum_i |h'_i-h_i|. If two arrays of log weights differ by at most A coordinatewise, their partition sums differ by multiplicative factors between exp(-A) and exp(A); their log partition functions consequently differ by at most A. Averaging, then dividing by N, proves

\[
|F_N(M')-F_N(M)|\le\alpha D+d\quad(N\ge1).
\tag{4}
\]

For the functional, fix all physical disorder first. A log edge insertion changes by at most ||theta'-theta||_infinity: its positive spin weights sum to one and its Boltzmann factors satisfy the same multiplicative comparison. The same comparison gives a message change of at most that norm for each fixed last spin. Hence the site log insertion changes by at most |h'-h|+sum_j ||theta'_j-theta_j||_infinity.

To pass this estimate through a hierarchy, if |g'-g|<=A then exp(-mA) exp(mg)<=exp(mg')<=exp(mA) exp(mg) for every m>0. Integration and logarithms give |P_m(g')-P_m(g)|<=A. Induction on the depth preserves the same A, with no factor depending on m or on the depth. Root expectation preserves it as well. The site clause count has mean alpha p; the edge correction coefficient is alpha(p-1)>=0. The triangle inequality therefore gives, for every trial law and every valid depth and exponents,

\[
|B_{M'}(r,\zeta,m)-B_M(r,\zeta,m)|
\le\alpha(2p-1)D+d.
\tag{5}
\]

An independent coefficient check counts affected insertions: alpha p site clauses plus alpha(p-1) edge corrections give alpha(2p-1) norms. Adding the physical pressure comparison in (4) gives alpha[(2p-1)+1]D+2d=2 alpha p D+2d. There is no bound on the messages or on the hierarchy depth in (4)-(5).

## 4. Clipping removes the bounded-law restriction

Let T_K(x)=max(-K,min(K,x)) for K>=0 and apply it to every entry of theta and to h, producing M_K. Coordinatewise clipping commutes with coordinate permutations, so a permutation-invariant interaction law stays permutation invariant. No preservation of the admissibility factorization is needed: the bounded input below requires symmetry, not that factorization.

For every real x, |T_K(x)-x|=(|x|-K)_+. Taking the maximum over the finite spin space gives the sharper identities

\[
D_K=\mathbb E(\|\theta\|_\infty-K)_+\longrightarrow0,
\qquad d_K=\mathbb E(|h|-K)_+\longrightarrow0.
\tag{6}
\]

The convergence follows by domination by ||theta||_infinity and |h|. Alternatively, each sample is eventually unchanged by clipping, and the difference is bounded by twice its original norm, which is the domination used in NormalizedCutoff.lean. These are independent checks of the first-moment limiting argument; no exponential moment or rate of tail decay is required.

Assume that for every bounded symmetric model and every delta>0 there is a finite-depth trial with B_{M_K} <= liminf_N F_N(M_K)+delta. By (4)-(5) the very same trial satisfies

\[
\begin{aligned}
B_M
&\le B_{M_K}+\alpha(2p-1)D_K+d_K\\
&\le\liminf_N F_N(M_K)+\delta+\alpha(2p-1)D_K+d_K\\
&\le\liminf_N F_N(M)+\delta+2\alpha pD_K+2d_K.
\end{aligned}
\tag{7}
\]

For a prescribed epsilon>0 choose delta=epsilon/2 and then K so that 2 alpha p D_K+2d_K<epsilon/2. The trial's depth may depend on K; (5) is uniform over that depth, so (7) remains valid. This proves symmetric_trial_lower from the bounded input. Applying this result to theta_hat, then using (2)-(3), proves admissible_trial_lower conditional on that input. Finally, the variational infimum is below each exhibited trial value; letting epsilon decrease to zero gives variationalValue <= liminf F_N. The uniform functional envelope ensures the infimum is a finite real number.

## 5. Exact boundary of the bounded input checked here

BoundedCavityLower.lean uses the following three imported mathematical inputs for the actual bounded physical model:

1. For any delta>0, full_regular_covariance_selection gives, for each depth L, a strictly increasing size sequence N_{L,n} and perturbation parameters u_{L,n}, with increment I_{L,n} <= liminf F_N+delta, simultaneously with FullShapeControl at that depth.
2. For those same sequences and parameters, cavityProxy_comparison_tendsto gives lim_{L->infinity} limsup_{n->infinity} g_{L,n}=0, where g is the absolute difference between the proxy P_{L,n} and the actual trial functional B_{L,n}. UpperTrial.lean supplies a finite uniform bound on g.
3. increment_cavityProxy_bound gives |I_{L,n}-P_{L,n}|<=e_{L,n}, where e_{L,n}=cavityIncrementError(...,N_{L,n}+1) tends to zero for each fixed L. The displayed error-limit lemma invokes additional rate-limit results; their proofs are not audited here.

Their combination can be checked without interchanging limits. Fix epsilon>0 and use input 1 with delta=epsilon/4. Input 2 permits choosing a single L for which limsup_n g_{L,n}<epsilon/4. Since g_{L,n} is bounded, eventually g_{L,n}<epsilon/4: choose any number strictly between its limsup and epsilon/4 and use the defining tail-supremum characterization. At this fixed L, strict increase of N_{L,n} implies N_{L,n}->infinity, so input 3 makes e_{L,n}<epsilon/4 eventually. Choose n in the intersection of these two tails. The signs needed are

\[
B_{L,n}\le P_{L,n}+g_{L,n}
\le I_{L,n}+e_{L,n}+g_{L,n}
<\liminf_N F_N+3\epsilon/4.
\tag{8}
\]

Thus one finite-depth trial is below liminf F_N+epsilon. Its exponents are m_i=(i+1)/(L+1), 0<=i<L. They are strictly increasing in (0,1), including the vacuous L=0 case. The terminal exponent 1 is excluded from the trial vector by Fin.castSucc. No finite-RSB assumption, attainment of an infimum, or uniform-in-depth size subsequence is used in (8).

Equation (8) is also checked directly from the absolute-value inequalities: |P-B|<a implies B<P+a, and |I-P|<=b implies P<=I+b, so the three positive error budgets add. Reversing either subtraction inside an absolute value leaves the result unchanged.

## 6. Limits of the audit and cases that could break the reduction

The reduction requires first moments, positive hierarchy exponents and p>=1. All hold in T137. For p=0 the identity p-(p-1)=1 fails with natural-number subtraction; this is why functional_center explicitly assumes p>=1. N=0 need not be compared, since every limit uses the tail N>=1. The case K=0 is legal and merely gives zero clipped clauses/fields. Gaussian couplings are allowed by (6), without a bounded-coupling approximation rate. The sign of c is unrestricted and does not affect the cancellation. A general asymmetric interaction law need not become symmetric after centering; the factorization and joint independence in Section 1 are essential. Odd-K SAT still fails the explicit evenness assumption of the final theorem, although the conditional lower-bound reduction itself does not use evenness.

No gap was found in (1)-(8) under the three stated bounded inputs. The proof of those inputs, the independent-message comparison, the analytic perturbation selection, and the Lean elaboration environment remain outside this audit. In particular, a statement called FullShapeControl is an intermediate conclusion in the displayed selector, not evidence by itself that its full import chain is correct.

The next mathematical input to audit is randomInsertion_comparison_tendsto in RandomInsertion.lean. The label-reindexing wrapper randomInsertionOn_comparison_tendsto is in AveragedEnergyRoot.lean; its almost-sure and Poisson-mixture wrappers in UpperInsertion.lean feed cavityProxy_comparison_tendsto in CavityProxy.lean. PoissonInsertionLimit.lean contains another Poisson wrapper, not the defining independent-message lemma. The independent-message comparison behind these wrappers is where the present conditional argument stops.
