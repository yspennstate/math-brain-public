# A finite-time product-mixture estimate for full FIFO states

Fix \(0<\lambda<1\), an integer \(d\geq2\), and \(N\geq d\). Sampling is uniform without replacement, and ties are broken uniformly. All initial queues have finitely many jobs and finite residual and waiting requirements. The initial state is independent of the future arrival and service randomness. The service law \(G\) is any probability law on \([0,\infty)\) with mean one.

Use a full FIFO state \(x\): its queue length \(q(x)\), the residual requirement of the job in service, and the ordered requirements of the waiting jobs. The service age can also be retained throughout. Requirements of arriving jobs are revealed on arrival, independently with law \(G\). Let \(E\) be this standard Borel state space. With no arrivals there is a deterministic measurable service flow. Jobs of requirement zero are removed when they reach service. An ambient disjoint union of closed Euclidean components supplies left limits at departure boundaries. Path laws below use the coordinate sigma field on the resulting right-continuous paths. Equality of paths includes all retained coordinates, not just queue length.

For a probability measure \(\nu\) on \(E\), put

\[
 p_r(\nu)=\nu\{x:q(x)\geq r\},\qquad r\geq0,
\]

and define the cavity arrival rate

\[
 b(r,\nu)=\lambda\sum_{j=0}^{d-1}
       p_r(\nu)^{d-1-j}p_{r+1}(\nu)^j.
 \tag{1}
\]

Powers of exponent zero in this polynomial are one, including at zero. Write

\[
 C=\lambda d(d-1),\quad
 \epsilon_N=\frac{\lambda d^2(d-1)}{2N},\quad
 H_N(T)=\left(\frac4{\sqrt N}+\frac d{2N}\right)(e^{CT}-1).
 \tag{2}
\]

For an initial law \(\mu\), let \(\mu_t\) be the nonlinear queue law with initial law \(\mu\), deterministic service flow, and arrival rate \(b(q(x),\mu_t)\) in state \(x\). Let \(Q_\mu^T\) denote its full-state path law on \([0,T]\). Existence, uniqueness and the estimates needed for this definition are proved below.

**Theorem.** Let \(X^N(0)\) have any exchangeable law on \(E^N\), and let

\[
 L_N(0)=\frac1N\sum_{i=1}^N\delta_{X_i^N(0)}.
\]

For \(1\leq k\leq N\), the total variation distance, with convention \(\|P-R\|_{\rm TV}=\sup_A|P(A)-R(A)|\), satisfies

\[
 \left\|\mathcal L\bigl(X_1^N[0,T],\ldots,X_k^N[0,T]\bigr)
  -\mathbb E\left[(Q_{L_N(0)}^T)^{\otimes k}\right]\right\|_{\rm TV}
 \leq \min\left\{1,\ kH_N(T)+\frac{k(k-1)}{2N}\right\}.
 \tag{3}
\]

The expectation on the left is a mixture of probability measures. It does not replace the random measure \(L_N(0)\) by its expectation. More precisely, for almost every empirical measure \(\mu\) under the law of \(L_N(0)\),

\[
 \left\|\mathcal L\bigl(X_1^N[0,T],\ldots,X_k^N[0,T]\mid L_N(0)=\mu\bigr)
       -(Q_\mu^T)^{\otimes k}\right\|_{\rm TV}
 \leq\min\left\{1,\ kH_N(T)+\frac{k(k-1)}{2N}\right\}.
\]

## 1. A uniform replacement for arrival-rate monotonicity

For a deterministic configuration \(x=(x_1,\ldots,x_N)\), let \(a_i^N(x)\) be the rate of arrivals routed to \(i\), and let \(L_x=N^{-1}\sum_i\delta_{x_i}\). Then

\[
 0\leq a_i^N(x),b(q(x_i),L_x)\leq\lambda d,
 \qquad
 |a_i^N(x)-b(q(x_i),L_x)|\leq\epsilon_N.
 \tag{4}
\]

To prove this, condition on inclusion of \(i\) in the sample. Its probability is \(d/N\), so its rate factor is \(\lambda d\). The competitors are \(d-1\) distinct uniform labels other than \(i\). Replace them by \(d-1\) independent labels uniform on all \(N\) labels. The latter sample is distinct and avoids \(i\), except on an event of probability at most

\[
 \frac{d-1}{N}+\frac{\binom{d-1}{2}}{N}
 =\frac{d(d-1)}{2N}.
 \tag{5}
\]

Conditional on that good event its law is exactly the ordered competitor sample without replacement. Couple the samples identically on the good event. The routing probability lies in \([0,1]\), so their expected winning probabilities differ by at most (5).

Set \(r=q(x_i)\), \(u=p_r(L_x)\), and \(v=p_{r+1}(L_x)\). Against independent competitors, the tag can win only if all competitors have length at least \(r\). If exactly \(j\) have length \(r\), it wins with probability \(1/(j+1)\). Its winning probability is therefore

\[
 \sum_{j=0}^{d-1}\binom{d-1}{j}
       \frac{(u-v)^jv^{d-1-j}}{j+1}
 =\int_0^1(v+z(u-v))^{d-1}\,dz.
 \tag{6}
\]

Multiplication by \(\lambda d\) gives (1), by integrating the power or using \(u^d-v^d=(u-v)\sum_{j=0}^{d-1}u^{d-1-j}v^j\). When \(u=v\), the integral gives the same polynomial directly. Equations (5)--(6) prove (4), including classes of zero or vanishing empirical mass. The bound \(\lambda d\) also follows directly from tag inclusion.

For arbitrary probability measures \(\nu,\eta\), write

\[
 D(\nu,\eta)=\sup_{r\geq0}|p_r(\nu)-p_r(\eta)|.
\]

The integral in (6) and \(|s^{d-1}-t^{d-1}|\leq(d-1)|s-t|\) on \([0,1]\) give

\[
 \sup_r|b(r,\nu)-b(r,\eta)|\leq C D(\nu,\eta)
 \leq C\|\nu-\eta\|_{\rm TV}.
 \tag{7}
\]

Indeed, the two affine interpolants in (6) differ by at most the larger difference of their endpoints. This establishes the constant \(C\) without dividing by a queue-length class mass.

## 2. The nonlinear queue is well defined

Given a deterministic measurable curve \(\nu_t\) of probability measures, construct a queue with initial law \(\mu\) using a Poisson candidate stream of rate \(\lambda d\). Each candidate has an independent uniform mark \(U\in[0,\lambda d]\) and service requirement \(S\sim G\). Accept it in state \(x\) at time \(t\) precisely when \(U\leq b(q(x),\nu_t)\). Apply the deterministic FIFO service flow between candidates. Bounded candidate rate implies finitely many candidates on every bounded time interval; finite initial queues and finite requirements imply this construction is well defined even when \(G\{0\}>0\).

Let \(\Phi_\mu(\nu)_t\) be the resulting one-time law. Couple the constructions for curves \(\nu,\eta\) with the same initial state and candidate marks. Until their first different acceptance their entire states agree. The intensity of a different acceptance is the absolute rate difference, bounded by (7). Consequently

\[
 \sup_{t\leq T}\|\Phi_\mu(\nu)_t-\Phi_\mu(\eta)_t\|_{\rm TV}
 \leq CT\sup_{t\leq T}\|\nu_t-\eta_t\|_{\rm TV}.
 \tag{8}
\]

The space of measurable probability kernels \(t\mapsto\nu_t\), equipped with uniform total variation distance, is complete: a uniform Cauchy sequence converges in total variation at each time, and evaluation on each Borel set remains measurable in the limit. On an interval with \(CT<1\), (8) makes \(\Phi_\mu\) a contraction. Its fixed point exists and is unique. Restart this construction at each interval endpoint to cover every finite horizon.

Here are measurability details for the reference path kernel. Conditional on any fixed finite number of candidates, their ordered times and marks, the trajectory is a finite composition of measurable service flows, queue updates, and acceptance comparisons. Its path coordinates are therefore measurable. Integrating over times and marks and summing over the Poisson candidate count gives a measurable path law whenever the input curve is a probability kernel. Start Picard iteration from the constant curve \(\nu_t=\mu\). At every iteration the curve is jointly measurable in \((\mu,t)\), since evaluation of a probability measure on a Borel set is measurable. The same coupling used in (8) bounds the total variation distance of the entire output path laws by \(CT\) times the uniform total variation distance of the input curves. Thus their path laws also converge in total variation. Evaluation on every Borel path event passes to the limit, giving a measurable kernel \(\mu\mapsto Q_\mu^T\). Iteration across finitely many short intervals preserves this property. This defines the mixture in (3). The argument requires only measurable kernels, not continuity in total variation of the deterministic service flow.

For deterministic \(x\in E^N\), construct \(N\) independent reference queues \(Y_i\), initially \(x_i\), in the common deterministic environment \(\mu_t^{L_x}\). Their laws need not coincide. Their average law is nevertheless

\[
 \frac1N\sum_i\mathcal L(Y_i(t))=\mu_t^{L_x},
 \tag{9}
\]

because selecting their initial label uniformly gives initial law \(L_x\) and uses exactly the nonlinear queue's deterministic environment and transition mechanism.

## 3. An empirical-tail bound without identical distributions

If \(Z_1,\ldots,Z_N\) are independent integer-valued nonnegative variables, then

\[
 \mathbb E\sup_{r\geq0}\left|\frac1N\sum_i
       (1_{\{Z_i\geq r\}}-\mathbb P(Z_i\geq r))\right|
 \leq\frac4{\sqrt N}.
 \tag{10}
\]

Here is a derivation that does not assume equal laws. Take independent copies \(Z_i'\). Jensen's inequality first bounds the unnormalized left side by

\[
 \mathbb E\sup_r\left|\sum_i(1_{\{Z_i\geq r\}}-1_{\{Z_i'\geq r\}})\right|.
\]

The independent pairs \((Z_i,Z_i')\) can each be swapped without changing their joint law. Introducing independent signs \(\varepsilon_i\), equal to (1) and \(-1\) with probability \(1/2\), and using the triangle inequality therefore bounds this expression by

\[
 2\mathbb E\sup_r\left|\sum_i\varepsilon_i1_{\{Z_i\geq r\}}\right|.
\]

Conditional on all the \(Z_i\), order the labels by decreasing \(Z_i\), breaking ties in any fixed way. Every tail set is a prefix in this order. Thus the supremum is at most \(\max_{0\leq m\leq N}|\sum_{j=1}^m\varepsilon_{\sigma(j)}|\). The ordered signs are still independent fair signs. The elementary \(L^2\) maximal inequality for this martingale gives expectation at most \(2\sqrt N\). For completeness, if \(S_m\) is this walk and \(M=\max_m|S_m|\), the stopping-time inequality \(a\mathbb P(M\geq a)\leq\mathbb E[|S_N|1_{\{M\geq a\}}]\), integrated over \(a\geq0\), gives \(\mathbb E M^2\leq2\mathbb E(M|S_N|)\leq2\sqrt{\mathbb EM^2\mathbb ES_N^2}\), hence \(\mathbb EM^2\leq4N\). Division by \(N\) proves (10).

## 4. Coupling the complete finite system

Condition first on a deterministic initial configuration \(x\). For each label \(i\), use independent Poisson candidate streams of rate \(\lambda d\), with the marks used in Section 2. Construct \(X^N\) by accepting a candidate at \(i\) when \(U\leq a_i^N(X^N(t-))\). This has the law of the original routed system: each actual arrival changes only its chosen coordinate; its rate at \(i\) is \(a_i^N\); the rates sum to \(\lambda N\); and the independent requirement mark has law \(G\). More explicitly, while no accepted arrival has occurred, the queues follow their deterministic service flow and the sum of their acceptance rates remains \(\lambda N\). The next accepted-arrival waiting time is therefore exponential of rate \(\lambda N\). At its occurrence, the chosen label has conditional probability \(a_i^N/(\lambda N)\), precisely the original routing distribution. Recursing after each accepted arrival proves equality of the full process laws. Thus independent candidate streams are a representation of the original arrival transition kernel, rather than an independence assumption on routed queues.

Use the same candidate stream at \(i\) to construct \(Y_i\) with acceptance rate \(b(q(Y_i(t-)),\mu_t^{L_x})\). These reference queues are independent conditional on \(x\), as required in Section 3.

Let \(\tau_i\) be their first different candidate acceptance, and set

\[
 B(t)=\frac1N\sum_i1_{\{\tau_i\leq t\}},\qquad h(t)=\mathbb E_x B(t).
\]

Before \(\tau_i\), the two full states at \(i\) agree, since the initial states, accepted service marks, and service flows agree. At all times,

\[
 D(L_{X^N(t)},L_{Y(t)})\leq B(t).
 \tag{11}
\]

Indeed, the indicators of every queue-length tail coincide on each label that has not yet disagreed. Applying (10) and (9) at each fixed time gives

\[
 \mathbb E_xD(L_{Y(t)},\mu_t^{L_x})\leq4/\sqrt N.
 \tag{12}
\]

Until \(\tau_i\), (4), (7), (11), and (12) bound the expected intensity of a different acceptance by

\[
 \epsilon_N+C\bigl(h(t)+4/\sqrt N\bigr).
\]

Integrating its predictable intensity, and then averaging over \(i\), yields

\[
 h(t)\leq\int_0^t\left[\epsilon_N+C\left(h(s)+\frac4{\sqrt N}\right)\right]ds.
 \tag{13}
\]

Departure times cause no difficulty: a candidate almost surely does not coincide with a previously scheduled completion of a positive residual requirement. Instantaneous zero-requirement departures triggered by a candidate are part of that candidate's state update. Equal service flows cannot cause a first disagreement. All time-integrated comparisons can be taken with left limits. Each queue-length tail of the deterministic law \(\mu_t^{L_x}\) has at most countably many jump times, which do not affect these integrals.

Solving the scalar integral inequality gives

\[
 h(t)\leq\left(\frac4{\sqrt N}+\frac{\epsilon_N}{C}\right)(e^{Ct}-1)=H_N(t).
 \tag{14}
\]

The pre-averaging intensity bound was the same for every \(i\). Substitution of (14) into that bound also gives

\[
 \mathbb P_x(\tau_i\leq T)\leq H_N(T)\quad\text{for every }i.
 \tag{15}
\]

Alternatively, for a uniformly selected label, (14) already suffices. A union bound gives probability at most \(kH_N(T)\) that any of \(k\) distinct uniformly sampled reference paths differs from its finite-system counterpart.

## 5. From deterministic starts to the random empirical mixture

Still condition on \(x\). Sample \(k\) independent uniform labels \(J_1,\ldots,J_k\). For each sampled label use a fresh independent reference path started from \(x_{J_j}\), in the deterministic environment \(\mu_t^{L_x}\). These paths are independent with common law \(Q_{L_x}^T\), including when labels repeat. On the event that all labels are distinct, couple these paths to the corresponding \(Y_{J_j}\). Conditional on distinctness the ordered labels are uniform without replacement, and their corresponding reference paths have precisely the required product of their individual transition laws. Thus sampling without replacement changes the path law by at most

\[
 \mathbb P(\text{some labels repeat})\leq\frac{k(k-1)}{2N}.
 \tag{16}
\]

Equations (14)--(16) compare the paths of uniformly sampled distinct servers to \((Q_{L_x}^T)^{\otimes k}\) with the bound in (3), uniformly over \(x\).

Now randomize \(x=X^N(0)\). Conditional on \(L_N(0)\), its law is invariant under label permutations: an exchangeable law restricted to each empirical multiset assigns equal probabilities to its distinct permutations. The evolution is also invariant under permutations. Fixed tagged labels consequently have, conditional on \(L_N(0)\), the same path law as distinct uniform sampled labels. Integrate the uniform bound just proved over the conditional law of \(x\), and then over \(L_N(0)\). This proves both the conditional and unconditional statements of (3). No independence assumption on the original initial coordinates entered the proof.

## 6. Consequence and limitation for stationary laws

If the finite-system initial law is stationary and exchangeable, its fixed-\(k\) one-time law is, for each fixed \(t\), within the bound (3) of

\[
 \mathbb E\left[(\mu_t^{L_N(0)})^{\otimes k}\right].
 \tag{17}
\]

This follows by projecting paths to time \(t\), which cannot increase total variation distance. Stationarity identifies the left law with the fixed-\(k\) stationary marginal. The right side is still a mixture. In particular, for \(k=2\) and a measurable \(f:E\to[0,1]\), the covariance under the comparison law is exactly

\[
 \operatorname{Var}\bigl(\mu_t^{L_N(0)}f\bigr).
 \tag{18}
\]

To check (18), condition on \(L_N(0)\); the product expectation is \((\mu_t^{L_N(0)}f)^2\) and each marginal expectation is \(\mu_t^{L_N(0)}f\). Hence the variance follows by subtraction. If the distance in (3) is \(\delta\), the actual tagged covariance differs from (18) by at most \(3\delta\), since the joint test and the two marginal tests take values in \([0,1]\). Thus this repair retains, quantitatively, the conditional-mean randomness identified in the original report.

No convergence of the stationary empirical measure, uniqueness of an invariant probability law of the nonlinear evolution, or attraction to a deterministic equilibrium is proved. Equation (3) holds for every fixed horizon; its constants grow exponentially with the horizon. It also gives convergence on \(T_N=a\log N\) for \(0<a<1/(2C)\), but supplies no forgetting estimate on those horizons. A proof of the stationary product limit still has to eliminate the variance in (18) and establish an appropriate unique marginal limit.

The preceding round's monotonicity counterexample is consistent with (4): empirical-measure continuity replaces monotonicity, without making a random empirical environment deterministic. The argument here is a quantitative transient estimate and does not claim a new general stationary theorem.

## 7. Independent constant checks and boundary cases

The exact probability of the good competitor event in Section 1 is

\[
 \prod_{j=1}^{d-1}\left(1-\frac jN\right).
\]

The elementary product inequality \(1-\prod_j(1-z_j)\leq\sum_jz_j\) on \([0,1]\) gives \(d(d-1)/(2N)\), recovering (5) independently of the pairwise collision union bound. Multiplication by the rate \(\lambda d\) recovers \(\epsilon_N\).

There is also a polynomial check on \(C\). Each of the \(d\) monomials in (1) has total degree \(d-1\) in \(u,v\). Its absolute change on the unit square is at most \((d-1)\max(|u-u'|,|v-v'|)\), by telescoping its factors. Summing the \(d\) bounds and multiplying by \(\lambda\) gives \(C=\lambda d(d-1)\), in agreement with the integral proof.

For a second check on the constant in (10), the reflection argument for a fair-sign walk gives, for integer \(m\geq1\),

\[
 \mathbb P(\max_{j\leq N}S_j\geq m)
 =\mathbb P(S_N\geq m)+\mathbb P(S_N\geq m+1).
\]

Indeed, reflect the increments after the first hit of \(m\): paths which hit \(m\) but finish below \(m\) correspond bijectively to paths finishing above \(m\). Summing over \(m\) shows
\(\mathbb E\max_jS_j\leq2\mathbb E(S_N)^+=\mathbb E|S_N|\leq\sqrt N\).
Apply the same estimate to \(-S\) and use
\(\max_j|S_j|\leq\max_jS_j+\max_j(-S_j)\).
This yields \(\mathbb E\max_j|S_j|\leq2\sqrt N\), independently of the stopping-time \(L^2\) argument. With the symmetrization factor two this again gives \(4/\sqrt N\).

The solution of (13) can be checked by differentiation: \(H_N(0)=0\) and
\[
 H_N'(t)=CH_N(t)+4C/\sqrt N+\epsilon_N,
\]
because \(\epsilon_N/C=d/(2N)\). An integrating factor then proves (14). Finally, the exact collision probability for \(k\) independent labels is \(1-(N)_k/N^k\), where \((N)_k=N(N-1)\cdots(N-k+1)\). The same product inequality gives (16).

At \(T=0\), the coupling error \(H_N(0)\) is zero and only initial-label collisions remain. At \(N=d\), all estimates remain valid; their numerical bounds may exceed one, which is why (3) is capped at one. When all queue lengths are equal, both exact and cavity arrival rates equal \(\lambda\). When a queue-length class has a single member or negligible density, (4)--(7) still apply. Deterministic service, atoms at zero, unbounded service support, and infinite second moment do not enter any estimate beyond the stated finite-state admissibility. The condition that future service marks are independent of the initial state and the routing decision is used in the candidate construction.
