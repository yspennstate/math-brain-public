# Audit of the workload obstruction

## Earlier certificate

Let q=min_i w_i b_i. If sum_i w_i Lambda_i<q, then

\[
 \sum_i\Lambda_i/b_i
 \le q^{-1}\sum_iw_i\Lambda_i<1.
\]

For every link l, b_i<=C_l on routes using l, so its utilization is at
most sum_i Lambda_i/b_i. Every link is then slack, contrary to Pareto
efficiency at a nonempty state. A single route attaining q realizes
weighted service q. This rederives the earlier exact minimum without
choosing a saturated link, as the earlier proof did.

For normalized workload Y=sum_i W_i/b_i, cumulative service has rate at
least one until empty. Couple Y with a unit-rate workload queue receiving
the same compound Poisson jumps B_i/b_i and starting at Y(x). Between
common jumps, the network's scalar workload decreases at least as fast
whenever it is positive. Order is therefore preserved. The network is
empty no later than the comparison queue's first empty time.

In the comparison busy period, call the initial work generation zero.
Arrivals while serving it bring expected work beta Y(x). Arrivals during
that work bring expected work beta^2 Y(x), and so on. This can be made
literal by serving work in first-come-first-served order and assigning
each arrival to the generation in service at its arrival time. Conditional
on the known work in a generation, independent Poisson increments give
expected child work beta times that work. Tonelli's theorem gives mean
total busy time Y(x)/(1-beta) when beta<1. Thus the earlier emptying and
regeneration conclusions hold independently of its martingale proof.

This comparison proves no stability assertion when beta>=1. The chosen
example has beta=6/5, but link loads 7/10. Both quantities are also checked
by exact arithmetic in check_obstruction.py.

## Two independent ways to see the obstruction

The proof derives D_1 and D_2 separately. Equivalently, their average is
the gradient applied to the average limiting velocity:

\[
 \frac12\{(1/5,1/2,1/2)-e_1\}
 +\frac12\{(1/5,1/2,1/2)-e_2\}
 =(1/5,0,0).
\]

Consequently (D_1+D_2)/2=partial_0 F(e_0)/5=dF(e_0)/5. The cancellation
uses the local offered loads 1/2 and 1/2 exactly; the factor 1/5 is the
through-route load. The limiting service vectors e_1,e_2 have the same
convex average as the local arrival loads, leaving a positive radial
velocity. No sign condition on the local partial derivatives is needed.

For a separate check covering every real degree d>0, take
F(W)=(W_0+W_1+W_2)^d. At the constructed states put S=N+N^-1.
The two present routes share one tight link, so total aggregate service
is exactly one, independently of alpha and the weights. Every arrival
adds one to S and total arrival rate is 6/5. Thus, exactly,

\[
 \mathcal GV=\frac65\{(S+1)^d-S^d\}-dS^{d-1}.
\]

The mean value theorem and S/N->1 give
N^(1-d) GV -> d/5. This independently verifies the scale and the
constant for noninteger degrees, including 0<d<1.

The exact script uses another route: it expands Poisson jump differences
by the binomial theorem as Laurent polynomials in N, clears the service
denominator, and extracts the leading coefficient. It also directly
evaluates the generator at four values of N and checks equality with the
expanded expression. These finite calculations check the algebra of five
examples, not the theorem for all differentiable F.

## Attempts to invalidate the construction

**Bounded residual sizes.** Every residual in the construction is in (0,1].
Large W_0 is obtained from many unit files, not from an inadmissibly long
single residual. Large local counts with tiny local workload are possible
because residual sizes have no positive lower bound, even for unit files.

**Equal residuals have probability zero.** The theorem first uses convenient
deterministic states. Section 4 of PROOF.md then gives a separate positive
probability event from empty. During the first arrival window, service to
any file is at most eta. During the long middle interval, no local file
can depart: up to a putative first departure its rate is 1/K and its
residual remains at least r-eta>0. During the final arrival window its
service is at most eta/K. Hence the whole event ends in the stated narrow
workload region with exactly the required counts. No assertion that a
particular deterministic state is hit with positive probability is used.

**Smallest accessible case.** At N=2, r=1/16, eta=1/256 and K=8, the
smallest local residual is at least 119/2048>0, and total local workload
is at least 119/256>0. In general

\[
 r-\eta-\eta/K=N^{-4}(1-N^{-4}-N^{-7})>0\quad(N\ge2).
\]

This independently verifies the sign of the accessibility bound; the script
checks the same identities with rational arithmetic.

**Very unequal fairness weights.** The effective ratio r_j is fixed and
strictly positive. Lambda_0=1/(1+r_j N^2)->0 for each such ratio. The proof
does not claim convergence uniformly over weights or alpha. The KKT
calculation applies to logarithmic utility at alpha=1 as well as other
positive alpha.

**A negative local derivative.** Local derivatives may have either sign.
Only their difference enters the selected drift. The asymmetric cubic and
the quadratic with a negative local derivative in the script give one
negative branch and one positive branch; selecting the wrong branch would
invalidate the conclusion. The proof selects a branch once from the
limiting gradient and keeps it fixed as N increases.

**Boundary derivatives.** The assumed C^1 extension at e_0 is essential
to the proof: the same gradient must control both sequences and arrivals
onto the absent route. Differentiability only in the strictly positive
orthant would not suffice. This argument makes no claim for a function
whose gradient is singular or discontinuous near e_0.

**Finite jumps versus infinitesimal input.** The stochastic generator has
actual jumps of size one, not a fluid replacement of those jumps. Equation
(7) in PROOF.md uses homogeneity and the fundamental theorem of calculus
to justify the replacement after scaling. Arrival terms are not discarded
on the absent local route.

**Order of limits.** For each fixed N all residuals are positive. The local
generator is taken by letting elapsed time tend to zero at that fixed
state. Only afterward does N tend to infinity. There is no uniform lower
bound on the first departure time, and the proof does not need one.

**Potential instability inference.** The local workload N^-1 is served at
rate tending to one, so, for sufficiently large N, it clears after time
N^-1(1+1/(r_j N^2)) if there is no arrival. A through file cannot depart
before time N, which justifies keeping the rates constant until local
clearing. The hostile service configuration therefore lasts a time
tending to zero. Positive instantaneous drift does not imply positive
drift over a fixed interval or instability. In the full residual state,
the local count is N^3, which also disappears during this short interval;
this shows why workload scaling alone loses relevant information.

## Scope

The result excludes a uniformly negative pointwise generator drift for
V=F(W) with the exact boundary smoothness, homogeneity, and axis positivity
stated in PROOF.md. It gives no counterexample to stochastic stability.
Nonsmooth workload functions, nonhomogeneous workload functions, functions
of counts and residual profiles, and drift over a sampled interval remain
outside the theorem. No claim of priority in the literature is made.
