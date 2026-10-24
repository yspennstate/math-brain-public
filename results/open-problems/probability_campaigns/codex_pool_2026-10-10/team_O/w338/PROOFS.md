# w338 ten-problem proof packet

All claims are pending independent w346 audit. Cached sources establish historical problem statements, not present openness. No web search was used.

## P0266: Scalar Allen-Cahn maximal moment: explicit subcritical bound and critical failure

Label: author-checked proof; w346 audit pending.

For dU_t=(U_t-U_t^3)dt+gamma*U_t^2 dW_t, U_0=a>0, and 0<gamma^2<2,
E sup_{0<=t<=T} U_t^2 <= a^2 exp(2T)*(gamma^2+2)/(2-gamma^2) for every T>0.
At gamma^2=2 this expected supremum is infinite, while at every fixed t>0
E U_t^2=a^2 exp(2t)*(1-exp[-1/(2*a^2*(exp(2t)-1))]) is finite.

Changing the sign of W permits gamma>0. Put delta=3+2/gamma^2,
r=1/(gamma*a), s(t)=(exp(2t)-1)/2, and U_t=exp(t)/(gamma*R_{s(t)}),
where dR=dB+(delta-1)/(2R)ds, R_0=r. Ito's formula gives diffusion
-gamma U^2 and drift U-U^3; change the Brownian sign. For delta>=4 the
positive, global Bessel construction is standard (comparison with dimension four
also rules out a zero hit). Set q=delta-2. The generator annihilates R^(-q).
The stopped process before hitting b<r is bounded by b^(-q), so optional
stopping gives P(inf_{s<=S}R_s<=b)<=(b/r)^q. Consequently, with
K=a^2 exp(2T) and alpha=q/2>1,
P(sup U_t^2>x)<=min(1,(K/x)^alpha). Integrating gives K*alpha/(alpha-1),
which is the displayed bound.
For delta=4, optional stopping instead yields the exact identity
P(tau_b<=S)/b^2=r^(-2)-E[R_S^(-2);tau_b>S]. The Gaussian radial
representation gives E R_S^(-2)=(1-exp[-r^2/(2S)])/r^2: insert
y^(-1)=integral_0^infinity exp(-lambda*y) d lambda into a four-dimensional
Gaussian integral and substitute v=1/(1+2S lambda). Dominated convergence
therefore gives P(tau_b<=S)/b^2 -> exp[-r^2/(2S)]/r^2>0.
The random variable sup_{s<=s(T)}(2R_s^2)^(-1), bounded above by sup U_t^2,
has a positive 1/x tail coefficient. Its expectation diverges. The same Gaussian
inverse-moment formula gives the displayed fixed-time second moment.
This independently derives the scalar calculation already in the P0266 candidate;
no renewed review of the old review receipt or novelty certification is claimed.

Scope: Explicit scalar bound and critical check; no new full SPDE solution or present-openness certification.

Cached primary reference: Agresti and Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA (2025), Problem 4, journal p. 130; arXiv:2501.18561. Prior candidate is unrefereed; this packet checks only the scalar construction.

## C0021: Depth-two 3-majority optimum and improved block-composition revealment

Label: author-checked proof; w346 audit pending.

For iterated 3-majority f_2 on nine iid fair bits, the minimum expected
number of zero-error single-bit queries is 393/64 and the minimum revealment
is 131/192. For general depth k, an explicit composed algorithm achieves
delta_k <= (131/192)^floor(k/2)*(5/6)^(k mod 2). Thus the achievable exponent
for even depths is -log(131/192)/(2 log 3)=0.17399134015245032.
This is an achievable bound; it does not determine the exact asymptotic exponent.

# C0021: exact depth-two decision tree and composition

Status: exact computational certificate plus a proved composition lemma; pending w346 KEEP. No novelty or full solution is claimed. Local status source is Garban and Steif, *Noise Sensitivity of Boolean Functions and Percolation* (2012), Exercise VIII.5 note, p. 97. The 7 September intake still labels the exponent unverified and unresolved.

Let f_k be iterated majority of three on 3^k independent fair bits. Algorithms query bits and must always return the exact output. Revealment is the largest probability that an individual bit is queried, under the uniform input and internal randomization.

For k=2, the minimum expected number of queries is 393/64 = 6.140625. Its minimum revealment is 131/192 = 0.6822916667. The usual recursive algorithm has expected cost 25/4 and revealment 25/36. Thus the verified finite-block cost decreases by 1.75%.

The certificate in check_majority.py examines all 19,683 partial assignments. At a partial assignment with m free bits, let A(s) be the sum of the remaining query counts over its 2^m compatible complete inputs. A(s)=0 if the function is forced; otherwise A(s)=2^m+min_i[A(s with bit i=0)+A(s with bit i=1)]. Every zero-error decision tree must choose an unqueried bit at a nonterminal state, so induction on m proves this recurrence gives the optimum. Randomization cannot beat the minimum of its deterministic trees. All computations use integers; the only division is by 2^9 at the root.

The independent checks use the 512-entry truth table to verify the terminal condition in every partial assignment, verify every Bellman residual and chosen action, and execute the complete policy on every input. All three error counts are zero; all outputs are correct and the sum of the 512 query counts is 3144. The policy is in majority_policy.json.

Randomize the policy by a uniform automorphism of the full ternary tree. This finite group preserves f_2 and acts transitively on its nine leaves. Each leaf then has revealment (393/64)/9 = 131/192. Conversely, any algorithm's maximum revealment is at least its expected query count divided by nine. This proves the finite-block optimum, subject to audit of the certificate.

For any k, evaluate each logical bit requested by this depth-two policy using a recursively composed policy on an independent descendant subtree. A logical subtree is selected before any of its own inputs are examined, so its selection event is independent of its bits and fresh internal randomness. At each block, the nine outputs are independent fair bits. A fixed leaf's query probability is consequently the product of the block probabilities. Hence

    delta_k <= (131/192)^floor(k/2) * (5/6)^(k mod 2).

For even k=2m this is n^(-0.17399134015245032), improving the exponent 0.16595623285353023 of the usual recursive construction. It is an achievable bound, not the exact asymptotic exponent. The former influence lower bound delta_k >= (2/3)^k still applies.

Command: python -X utf8 ~/brain_workers/w338/check_majority.py. Recorded runtime: 0.570578 seconds. Full measurements are in majority_measurements.json. The correctness checks concern fair independent inputs, zero error, and single-bit query cost; changing those assumptions changes the problem.


Scope: Exact finite computation and proved composition; novelty and independent audit pending; asymptotic optimum unresolved.

Cached primary reference: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems, Exercise VIII.5 note, p. 97.

## C0133: Fair-cookie walk: zero speed, but a polynomial unrestricted excursion tail

Label: author-checked proof; w346 audit pending.

For simple symmetric random walk S on Z starting at zero, if tau is its
first positive return to zero and L>=1 is an integer, then
P(max_{0<=n<=tau}S_n>=L)=1/(2L). Nevertheless S_n/n->0 almost surely.
This fair-cookie example satisfies bounded stacks and uniform ellipticity,
so those assumptions alone do not imply an exponential unrestricted spatial
excursion tail. This does not contradict an exponential estimate with a specified
linear time budget.

A positive excursion begins with probability 1/2. From one, the probability
of hitting L before zero is 1/L: the affine harmonic function u(i)=i/L solves
u(0)=0,u(L)=1,u(i)=(u(i-1)+u(i+1))/2. Finite-state absorption or optional
stopping proves this probability. A negative first step cannot reach L before
returning to zero. Symmetric one-dimensional walk returns almost surely; this
also follows by letting L tend to infinity in the ruin probability. Thus the
displayed unrestricted excursion probability is exact.
For zero speed, the independent increments are mean-zero and bounded by one;
the exponential-moment bound yields P(|S_n|>=epsilon*n)<=2 exp(-epsilon^2*n/2).
Summation and Borel-Cantelli, followed by rational epsilon decreasing to zero,
give S_n/n->0 almost surely. This solves only the fair-cookie special case.
The prior C0133 attempt is conditional on an unproved uniform excursion estimate;
the example rules out its unrestricted spatial reading, not its timed reading.
If a recurrent path already has a limiting speed, the bounded return subsequence
forces that limit to be zero, but recurrence does not establish existence of the limit.

Scope: A solved special case and a scoped obstruction to the earlier tail route; general C0133 remains unverified.

Cached primary reference: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012, Problem 4.7, p. 19.

## P0090: Extinction certificate for the types reachable from a pivot population

Label: author-checked proof; w346 audit pending.

Let Z be a finite-type Galton-Watson process with finite mean matrix M
(row i lists expected type-j children) and finite deterministic initial population z.
Let R be the forward-reachable types from the support of z. If rho(M_R)<1,
then w=(I-M_R)^(-1)*1 is finite, positive, and M_R*w=w-1.
The expected total population is z_R*w<infinity, hence extinction occurs almost surely.
Unreachable supercritical types do not affect this conclusion; positive regularity
is unnecessary. This is a branching-process certificate, not a full interpretation criterion.

R is closed under positive-mean child edges; a child count of mean zero
is zero almost surely, so no population leaves R. Since rho(M_R)<1, the
nonnegative Neumann series sum_{n>=0} M_R^n converges to (I-M_R)^(-1).
Thus w=sum M_R^n*1 has every coordinate at least one and satisfies M_R*w=w-1.
The branching property gives E Z_n=z_R*M_R^n. Tonelli gives
E sum_n |Z_n|=z_R*w<infinity; a nonnegative total population with finite
expectation is finite almost surely, which implies extinction.
For example, M=diag(1/2,2), z=(1,0), has full spectral radius two but
reachable mean 1/2 and expected total population two. This can be realized
with type-one one-child probability 1/2 and deterministic two type-two children.
The result applies to an automaton's pivot process only after its type law and
initial support are correctly identified. It makes no critical interpretation claim.

Scope: Generalizes the earlier global subcritical calculation to reachable classes; critical/supercritical interpretation is unresolved.

Cached primary reference: Random tree recursions: which fixed points correspond to tangible sets of trees?, Section6, PDF p.39, first paragraph.

## P0090: Critical multitype deterministic cycles need not become extinct

Label: author-checked proof; w346 audit pending.

A three-type Galton-Watson process in which every particle has exactly one
child of the next type cyclically has spectral radius one and exactly one particle
in every generation when started from one particle. Thus criticality alone,
without a nonsingularity hypothesis, does not imply multitype extinction.

The mean matrix is [[0,1,0],[0,0,1],[1,0,0]]. Its cube is the identity,
so its eigenvalues have modulus one and its spectral radius is one. Each particle
deterministically replaces itself by exactly one particle of the next type;
induction gives population one at every generation. This is an abstract branching
example and is not asserted to realize all hypotheses of the tree-automaton problem.

Scope: Refutes only unconditional critical-means-extinct reasoning, not a qualified automaton theorem.

Cached primary reference: Random tree recursions: which fixed points correspond to tangible sets of trees?, Section6, PDF p.39, first paragraph.

## P0427: Exact no-arrival reduction for two exponentially sized parallel jobs

Label: author-checked proof; w346 audit pending.

Two independent jobs have unit-mean exponential inherent work and increasing,
continuous speed curves r_1,r_2 on [0,S], with r_i(0)=0 and r_i(b)>0 for b>0.
There are no arrivals, service is divisible and preemptible, and all S servers are
allocated. Let V_1=1/r_1(S) and V_2=1/r_2(S). The optimal expected sum of
completion times, even over history-dependent allocations, equals
min_{0<=b<=S} [2+r_1(b)*V_2+r_2(S-b)*V_1]/[r_1(b)+r_2(S-b)].
An optimal policy keeps a minimizing allocation until the first completion,
then assigns all servers to the survivor. This does not characterize a queue with arrivals.

Exponential memorylessness makes the two-alive state independent of consumed
work. With a constant split b, the first completion has rate lambda=r_1(b)+r_2(S-b)
and holding cost two. If job one completes, the survivor value is V_2; if job
two completes, it is V_1. This gives the displayed ratio. Its denominator is
bounded away from zero on the compact interval: some job always gets at least S/2.
The continuous ratio attains its minimum v.
For any predictable allocation b_t before the first completion time tau, the
pointwise inequality 2+r_1(b_t)*V_2+r_2(S-b_t)*V_1>=v*lambda_t holds.
Compensating the first-jump counting process gives
E integral_0^tau lambda_t dt=1, and the expected terminal survivor cost is
E integral_0^tau [r_1(b_t)*V_2+r_2(S-b_t)*V_1]dt. Thus every such policy costs
at least v; a constant minimizing split attains it. The finite-state verification
also covers internal randomization. A survivor optimally gets all servers because
its rate is increasing.
For S=4, r_1(b)=min(b,sqrt(b)), r_2(b)=min(b,b^(3/4)), the earlier throughput
split b=1 gives 1.0651926824. Numerical minimization gives b approximately
1.18331975 and value 1.0642800265 (0.08567989% lower). These numerical digits
are evidence, not an exact closed form or a Poisson-arrival policy theorem.

Scope: Proves a no-arrival two-job reduction; the numeric minimizer is not claimed exactly or for stationary queues.

Cached primary reference: Harchol-Balter: Open problems in queueing theory inspired by datacenter computing, Section3.4; PDF10-11. Status notes: Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.

## C0032: Correct density sign for a negative logarithmic potential

Label: author-checked proof; w346 audit pending.

For a finite positive measure mu on C with finite logarithmic moment, define
U(z)=-integral log|z-w| mu(dw) as a locally integrable potential. In distributions,
Delta U=-2*pi*mu. If mu has Lebesgue density g, then g=-(1/(2*pi))*Delta U.
The positive Laplacian sign used with this negative potential in C0032-A001 is incorrect.

For a compactly supported smooth test function, integrate log|z| times its
Laplacian over the complement of a disk of radius epsilon and integrate by parts.
The inner boundary term converges to 2*pi times the test function at zero;
the term containing epsilon*log(epsilon) vanishes. Thus Delta log|z|=2*pi*delta_0.
Translation and Fubini (local integrability and the logarithmic-moment condition)
give Delta U=-2*pi*mu. Absolute continuity gives the density formula.
As a check, the negative logarithmic potential of uniform probability on the
unit disk is (1-|z|^2)/2 inside the disk and -log|z| outside; its interior
Laplacian is -2, so the corrected formula gives density 1/pi rather than -1/pi.
This sign correction neither closes the PWIT recursion nor identifies g_alpha.

Scope: Corrects a source-attempt sign; heavy-tailed circular-law density remains unresolved.

Cached primary reference: Bordenave and Chafai: Around the circular law, survey with open problems, Section 6.6, p. 39.

## C0077: Rare-event conditioning requires joint test asymptotics

Label: author-checked proof; w346 audit pending.

Unconditional convergence, even almost sure convergence, and an exact
survival probability of order 1/n do not suffice for a conditioned scaling limit.
For U uniform on (0,1), let A_n={U<=1/n} and Z_n=a_n*1_{A_n}, with a_n=1
for even n and 2 for odd n. Then Z_n->0 almost surely and n*P(A_n)=1 exactly,
but Law(Z_n|A_n) alternates between point masses at one and two.
A valid sufficient replacement on a Polish state space is: n*P(A_n)->c>0
and n*E[f(Z_n)*1_{A_n}]->c*integral f dnu for every bounded continuous f;
then Law(Z_n|A_n) converges weakly to nu.

Almost every uniform U is positive; once n>1/U the indicator is zero.
Conditioned on A_n, Z_n equals a_n deterministically, so a bounded continuous
test separating one from two proves nonconvergence. The event probability is
exactly 1/n. For the sufficient replacement, divide the assumed joint-test
asymptotic by n*P(A_n); the resulting conditional expectations converge to nu(f),
which is weak convergence by its bounded-continuous-test characterization.
This demonstrates a missing requirement in the shorthand C0077<=C0076+C0066
when only an unconditioned limit and a one-arm constant are supplied. It does not
disprove the IIC conjecture or the prior attempt's explicitly added commutation
assumption. No percolation joint-test asymptotic is proved here.

Scope: A checked obstruction and precise conditional reduction; not an IIC scaling limit.

Cached primary reference: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems, Open Problem 15.3, p. 221.

## C0119: Dimension-free Gaussian polymer overlap bound conditional on superconcentration

Label: author-checked proof; w346 audit pending.

For a finite family of n-step paths and iid standard Gaussian time-site
energies X, let F(X)=log sum_paths exp(beta*sum_path X), beta>0. Write
p_j(X) for the Gibbs probability of occupying time-site j, and
X^t=exp(-t)*X+sqrt(1-exp(-2t))*X', with X' independent. Define
Q(t)=E sum_j p_j(X)*p_j(X^t). Then
Var(F)=beta^2*integral_0^infinity exp(-t)*Q(t)dt and
Q(t)<=Var(F)/(beta^2*(1-exp(-t))) for t>0.
Consequently Var(F_n)=o(n) and t_n->0 with Var(F_n)/(n*t_n)->0 imply
Q_n(t_n)/n->0 in every spatial dimension. If additionally Q_n(0)>=c*n,
the perturbed overlap is o(Q_n(0)). The needed variance and initial-overlap
estimates in the target low-temperature regime are not established here.

Differentiate the finite partition function to obtain partial_j F=beta*p_j.
These derivatives are bounded and square integrable. Expand the centered F in
orthonormal Gaussian Hermite chaoses: if a_k is its squared L2 mass in degree k,
then Var(F)=sum_{k>=1}a_k and
E <grad F(X),grad F(X^t)>=sum_{k>=1} k*a_k*exp(-(k-1)*t).
The latter is beta^2 Q(t), is nonnegative, and decreases with t. Integrating
against exp(-t) gives sum a_k by Tonelli, proving the identity. Integrating
only from zero to t and using monotonicity yields
Var(F)>=beta^2*(1-exp(-t))*Q(t). Division gives the bound. Since
(1-exp(-t_n))/t_n->1, the asymptotic conclusions follow by the stated hypotheses.
This supplies the precise Gaussian OU part of the reduction, not a
dimension-independent BKS variance theorem or an inference of strong disorder
from endpoint overlap. The finite-difference experiment checks only the Gibbs
gradient identity in 1D and 3D; the OU identity is proved by the displayed expansion.

Scope: A conditional Gaussian reduction; no unconditional higher-dimensional chaos solution.

Cached primary reference: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions, Section 12, problem (2), p. 59.

## P0010: Exact closed-boundary weight in the biased square-lattice orientation model

Label: author-checked proof; w346 audit pending.

Independently orient each horizontal Z^2 edge right with probability p
and each vertical edge up with probability p. For any finite vertex set S,
if boundary(S) is its set of edges with exactly one endpoint in S, then
P(no edge leaves S)=[p*(1-p)]^(|boundary(S)|/2).
In particular the origin is a sink with probability p^2*(1-p)^2, so the
probability theta(p) of an infinite directed path from the origin obeys
theta(p)<=1-p^2*(1-p)^2. The boundary condition is necessary but is not
sufficient for S to be exactly the reachable cluster of the origin.

On each horizontal lattice line, the indicator of finite S has equally many
0-to-1 and 1-to-0 transitions. Thus the number of left-side and right-side
horizontal boundary edges is equal, say h each. The analogous vertical counts
are v each. Making every boundary edge point into S requires h+v edges to
have their positive-coordinate orientation and h+v to have their negative one.
Independence gives [p*(1-p)]^(h+v), and the boundary size is 2(h+v).
For a singleton h=v=1, yielding the sink probability. A sink cannot begin an
infinite path. Other closed sets can contain vertices not reachable from the
origin, so this weight alone does not prove stochastic domination or survival
for every nonzero bias. Exhaustive boundary orientation checks cover three
shapes of perimeters four, six, and eight at five rational biases.

Scope: An exact finite-set identity and necessary-event bound; the small-bias survival question is unresolved.

Cached primary reference: Selected problems in probability theory, Question 5.1, PDF page 9.

## P0036: Growth lower bound and equality cases for Cayley spanning-tree percolation

Label: author-checked proof; w346 audit pending.

Let G be an infinite locally finite Cayley graph with ball growth rate
b=lim_n |B_G(e,n)|^(1/n), and let T be any spanning tree using edges of G.
Then p_c(T)>=1/b. In particular subexponential growth (b=1) implies p_c(T)=1.
If G is the usual 2r-regular Cayley tree of a free group, T=G and
p_c(T)=1/(2r-1)=1/b. The arbitrary exponential-growth geodesic-tree equality
asked in P0036 is not proved by these cases.

There is a unique T-path from any vertex v to a vertex at T-distance n.
The number of such vertices is at most |B_G(v,n)|=|B_G(e,n)|. A union bound
gives P(v has an open T-path of length n)<=|B_G(e,n)|*p^n. For p<1/b this
tends to zero by the definition of the growth rate. An infinite component
in a locally finite tree gives paths of every length, so every vertex has
zero probability of an infinite cluster. The countable union over vertices
also rules out an infinite cluster anywhere. Hence p_c(T)>=1/b; when b=1,
p_c(T)<=1 proves equality. Geodesicity was not required for this bound.
In a free-group Cayley graph that is already a tree, a connected spanning tree
must contain every edge, hence T=G. Off the root its bond clusters are
Galton-Watson with Binomial(2r-1,p) children, giving threshold 1/(2r-1);
r=1 is the infinite line and also has threshold one.
The old comb obstruction is consistent: attach a finite binary tree of height i
by one edge at spine vertex i. The sphere size is exactly 2^ceil(n/2), but the
only infinite ray is the spine, so p_c=1. This comb is not asserted to be a
geodesic spanning tree of an exponential-growth Cayley graph.

Scope: Proves subexponential and free-group tree cases; the arbitrary exponential geodesic case remains unresolved.

Cached primary reference: Probability on Trees and Networks, paperback electronic version 19 August 2026, Question 3.12, printed p.91.
