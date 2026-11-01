# D0026: working mathematical record

Date: 2026-10-11. Infection means spin 0, not spin 1.

## Verified target

Martinelli, Shapira and Toninelli, arXiv:2510.20461v1, Conjecture 1,
Section 1.1, PDF page 2: for every q in (0,1), every local function f,
and every probability law nu with at least one infection almost surely,
|nu P_t f - pi(f)| tends to zero. Here pi(eta_x=0)=q, and
c_x(eta)=1{eta_{x-1}=0 or eta_{x+1}=0}. The update rate is one with
heat-bath spin 0 probability q. This is the FA-1f model, not BABP.

## Proposition 1: reduction to deterministic starts (proved)

Fix q. The target for every admissible nu is equivalent to the target
for every deterministic eta different from the all-healthy configuration.
One direction follows by taking nu=delta_eta. Conversely, if the latter
assertion holds, then for every bounded local f, P_t f(eta) tends to pi(f)
at every eta other than the all-healthy configuration. All local functions
are bounded since their domain is finite. Also |P_t f(eta)-pi(f)| is at
most 2||f||_infinity. Integrating with respect to an admissible nu and using
dominated convergence proves the former assertion. Measurability of P_t f
is part of the graphical construction. No uniform rate in eta is needed.

## Earlier-attempt audit

The read-only intake ledger D0026-A001 (2026-09-08) contains useful warnings
about non-attractiveness and singular initial measures, but two assertions
must not be used: it says survival of an isolated infection is unproved,
and asserts an equivalence with L1-to-L2 regularization without a proof.
The first is false if survival means non-extinction: the last infection
cannot legally heal. The second is not an established equivalence.
Local convergence does not imply global absolute continuity at positive
finite times. A proof and a quantitative illustration follow below.

## Remaining target

No proof of pointwise local convergence for all nonempty configurations,
and no counterexample, has been obtained. Further claims will be recorded
with separate proofs and explicitly stated hypotheses.

## Proposition 2: finite-seed survival and persistent singularity (proved)

For every q in (0,1), a process starting from a finite, nonempty infection
set has a finite, nonempty infection set at every finite time, almost surely.
Consequently its law at every finite time is singular with respect to pi.

Proof. At a state with N infections, births can occur only at the at most
2N healthy neighbors of infections, at rate q per site. Total birth rate is
therefore at most 2qN. Healings occur at rate at most (1-q)N, and cannot
increase N. The number of births is dominated by that of a pure birth
chain starting from N(0), with rate 2qk at population k. This domination
can be built successively at jump times: add fictitious births to make the
dominating rate 2q times its population, and never decrement that population.
The pure birth chain is nonexplosive. For completeness, stopping at level m
and applying its generator to population gives E Z(t∧tau_m) ≤ N(0)e^{2qt}
by Gronwall; hence P(tau_m≤t) ≤ N(0)e^{2qt}/m. Let m tend to infinity.
While the birth count is bounded, the real jump rate is bounded as well,
so healings cannot cause an explosion. Each birth adds only a neighbor
of an existing infection. Thus the jump-chain construction gives finite
support at all finite times and agrees with the graphical process.
When N=1, the sole infected site's two neighbors are healthy, so its
healing rate is zero. A transition from N=1 to N=0 is impossible; all
changes of N are by one. Nonexplosion proves nonextinction simultaneously
for all times. Under pi, infinitely many sites in the positive half-line
are infected almost surely: the probability that all sites x≥k are healthy
is lim_{m→∞}(1-q)^{m-k+1}=0; take the countable union over k.
Therefore the measurable event 'finitely many infections' has probability
one under the finite-seed law and zero under pi, proving singularity. QED.

This refutes a proposed GLOBAL density-regularization route, not the
conjecture. Finite-support infection laws can converge weakly to pi even
though they remain singular at every finite time. Local convergence and
global total variation convergence have different meanings here.

## Proposition 3: all absolutely continuous initial laws (proved special case)

For every q in (0,1), if nu≪pi, then nu P_t tends to pi in total variation.
No L2 density assumption is needed. This is a standard semigroup consequence,
not a claimed new literature resolution of the singular-start conjecture.

Proof. Write A=-L for the nonnegative self-adjoint operator generating
the reversible strongly continuous Markov semigroup P_t=e^{-tA} on L2(pi).
(The sign in the prose surrounding (1.4) of the source is inconsistent;
its generator formula and Dirichlet form give the sign used here.) We
first prove that the kernel of A consists only of constants, using
Corollary 2.9 of the source.

Let real h∈ker A. Spectral calculus gives P_s h=h for every s≥0.
Let K_s(eta,dzeta) be its transition kernel. By invariance and Jensen,
P_s(h²)≥(P_s h)²=h² pi-a.e., and both sides have the same integral.
The nonnegative difference therefore vanishes pi-a.e. Conditional variance
zero implies h(zeta)=h(eta) for K_s(eta,·)-almost every zeta, at pi-almost
every eta. Hence for every bounded Borel function phi, P_s(phi∘h)=phi∘h
pi-a.e. This holds for each s; the null set may depend on s and that
causes no difficulty for stationarity.

In particular g_M=max(-M,min(h,M)) is bounded and fixed by every P_s.
Set K=M+1 and Z=pi(g_M+K)>0. The probability measure mu_M with density
(g_M+K)/Z is stationary: for any bounded measurable f, reversibility gives
mu_M(P_s f)=pi(P_s(g_M+K) f)/Z=mu_M(f). Corollary 2.9 says that mu_M
is lambda pi+(1-lambda)delta_1. Since mu_M≪pi and pi({1})=0, lambda=1.
Thus g_M is pi-a.s. constant for every positive integer M. Intersect
these countably many full-measure sets. At each point where h is finite,
g_M tends to h, so h is also pi-a.s. constant. The argument applies to
real and imaginary parts separately if complex L2 is used.

For u∈L2(pi), the spectral theorem now gives
||P_t u-pi(u)||_2² = integral_{(0,infinity)} exp(-2t lambda) d m_u(lambda)
→0 by dominated convergence, where m_u is the finite spectral measure
of u-pi(u). No spectral gap or convergence rate was used.

Let h=dnu/dpi≥0, pi(h)=1, and h_M=min(h,M), a_M=pi(h_M).
Invariance and Jensen imply that P_t is an L1 contraction; its L1
extension agrees with the density evolution, by reversibility and
bounded-density approximation. Thus

||P_t h-1||_1 ≤ ||P_t(h-h_M)||_1
               + ||P_t h_M-a_M||_1 + |a_M-1|
            ≤ 2 pi(h-h_M) + ||P_t h_M-a_M||_2.

For fixed M the last term tends to zero by the preceding L2 result.
Then M→infinity removes the other term by monotone convergence.
Total variation distance is one half of the L1 distance of densities.
This proves the assertion. Since pi({1})=0, nu≪pi automatically satisfies
the conjecture's nonempty-infection hypothesis. QED.

## Proposition 4: Cesàro limits and a universal occupation bound (proved)

For any initial law nu, define bar_mu_T=(1/T) integral_0^T nu P_t dt.
Every weak subsequential limit is lambda pi+(1-lambda)delta_1. Consequently,
for every site x,

limsup_{T→infinity} (1/T) integral_0^T P_nu(eta_x(t)=0) dt ≤ q.

Moreover, bar_mu_T→pi if and only if this time-averaged infection
probability at one fixed site tends to q.

Proof. Omega={0,1}^Z is compact metrizable, so the probability laws are
weakly sequentially compact. FA-1f is Feller. One direct justification is
the graphical construction: for a local observable in a finite set F,
dependence on initial sites at distance at least n requires a nearest-neighbor
chain of at least n clock rings in chronological order during time s.
For each length k there are at most |F|2^k spatial paths, and the expected
number of corresponding ordered clock tuples is s^k/k! (the same
factorial-moment bound applies to repeated sites). Hence the probability
is at most |F| sum_{k≥n} (2s)^k/k!, which tends to zero. Finite-window
approximations of P_s f therefore converge uniformly and are continuous.
Every continuous function is uniformly approximable by local functions
on this compact product space, and the Markov semigroup is a uniform-norm
contraction. This proves the Feller assertion.

For bounded continuous g and fixed s≥0, the semigroup property gives

|bar_mu_T(P_s g)-bar_mu_T(g)| ≤ 2s||g||_infinity/T.

Indeed the difference of integrals is the integral over [T,T+s] minus
the integral over [0,s], divided by T. Feller continuity permits passage
to any weak limit mu, giving mu(P_s g)=mu(g) for every s and g. Thus mu
is stationary. Apply Corollary 2.9. The local indicator I_x=1{eta_x=0}
is continuous and has expectation lambda q in this mixture. Every
subsequential limit of bar_mu_T(I_x) is therefore in [0,q], proving the
limsup bound. If bar_mu_T(I_x)→q, every weak cluster point has lambda=1,
so uniqueness of the cluster point on a compact space proves bar_mu_T→pi.
The converse follows by testing I_x. QED.

Gap: proving that this mean tends to q for every nonempty deterministic
start is still missing. Even that would only give time-average convergence;
one would also need an argument establishing convergence at fixed large times.

## Proposition 5: finite intervals (proved special case)

On a finite interval of n sites with healthy exterior, restricted to
nonempty infection sets, the chain converges from every start to the
Bernoulli infection law conditioned on being nonempty.

Proof. From any nonempty set A one can infect the entire interval by
adding neighbors successively, using at most n-|A| legal flips. Connectedness
of the interval guarantees an adjacent uninfected site whenever the set is
nonempty and not the entire interval. These births have positive rate q.
For any target nonempty B, reverse its such path to the full set. Each
reverse healing remains legal because the constraint ignores the flipped
site and hence has the same value in both endpoint configurations.
Reverse rates are positive since 1-q>0. Concatenation connects A to B.
The empty state is unreachable by Proposition 2's last-infection argument.
For adjacent states A,A∪{x}, product probabilities have ratio q/(1-q),
which equals the forward birth rate divided by the reverse healing rate.
Conditioning by a common normalizing constant preserves detailed balance.
The restricted chain is thus finite irreducible reversible. Its symmetric
Dirichlet form is a sum over connected edges of positive multiples of
(f(A)-f(B))², so its kernel is the constants and every other eigenvalue of
-L is strictly positive. Finite spectral diagonalization proves convergence.
For n=1 the restricted class is a singleton and the assertion is immediate.
Its equilibrium infection marginal is q/(1-(1-q)^n), tending to q as n grows.
QED.

This does NOT commute the limits n→infinity and t→infinity. Finite-speed
comparison controls a box only before external influence arrives, whereas
worst-start mixing can take a time proportional to the box length. Constants
must be compared, not suppressed. Nor can an artificial infected boundary
be imposed on the true process. For a one-site interval initially infected,
healthy exterior freezes it forever; infected exterior instead yields
P(healthy at t)=(1-q)(1-e^{-t}). At q=0.3,t=1 this is about 0.44248.

## Non-attractiveness: explicit generator test (proved)

Order configurations by their infection indicators. On three sites with
healthy exterior, take A={middle}, B={left,middle}, so A⊆B. The increasing
function f=1{middle infected} has f(A)=f(B)=1. At A its generator value is
0, since the middle is not facilitated and other flips do not change f.
At B its generator value is -(1-q), since it may heal. If the semigroup
preserved increasing functions, P_t f(A)≤P_t f(B) would hold for every t.
Their derivatives at t=0 violate that inequality. This also embeds into Z
by putting healthy spins everywhere else. The obstruction is valid for
every q∈(0,1).

FiniteChecks.lean certifies the finite order/facilitation witness and the
general finite-set fact that deleting x leaves a distinct infected y.
It does not formalize the stochastic semigroup, infinite-volume process,
or Conjecture 1. Compilation succeeded with exit code 0 and no diagnostics;
see CHECKS.md. Only the finite/combinatorial facts are Lean-checked.

finite_experiments.py exhaustively checks all 2^n-1 nonempty states for
2≤n≤9, and detailed balance using exact rational arithmetic for 2≤n≤7
and q∈{1/10,1/3,1/2,9/10}. These computations check the finite model,
not the infinite-volume conclusion.

## Proposition 6: exact dual reduction of the single-infection case (proved)

This lead was recovered from the read-only R7-04 D0027 handoff dated
2026-09-17. We verify its algebra and integrability here rather than
treat the handoff as authoritative. No exponential convergence claim is made.

Write p=1-q and phi(a)=(a-p)/q for the PRIMAL spin a∈{0,1}; thus
phi(1)=1 and phi(0)=-p/q. For finite A⊂Z, put
Phi_A(eta)=product_{x∈A} phi(eta_x), with Phi_empty=1. Define a dual
finite-set process: every currently occupied x rings at rate 1 and
independently refreshes membership of its two neighbors to Bernoulli(q),
while leaving x itself occupied. Its generator is denoted Q.

For all finite A, deterministic eta, and finite t,

E_eta Phi_A(eta(t)) = E_A Phi_{A(t)}(eta).                 (D)

Proof of generator algebra. A primal update at x∉A leaves Phi_A unchanged.
For x∈A, heat-bath averaging phi(eta_x) gives zero, so its generator term is
-c_x Phi_A=(eta_{x-1}eta_{x+1}-1)Phi_A. For a neighbor y,

eta_y Phi_A = p Phi_A + q Phi_{A∪{y}}             if y∉A,
eta_y Phi_A = p Phi_{A\{y}} + q Phi_A            if y∈A.

The first identity uses eta_y=p+q phi(eta_y). The second uses
eta_y phi(eta_y)=eta_y, which holds at both spins. Each expression is
exactly the expected value of Phi when membership of y is replaced by
an independent Bernoulli(q) coin. Applying the two identities successively
to the distinct neighbors x-1 and x+1 yields the Q term at x. Summing
over x∈A proves L_eta Phi_A=Q_A Phi_A pointwise.

Justification at finite times. On any finite cycle with at least three
sites the identity is a finite matrix identity. If D has rows A and
columns eta, it reads D L^T=Q D, so finite matrix exponentiation gives
the semigroup identity. Embed A in larger and larger cycles and use
graphical coupling until boundary influence arrives. Primal local
convergence to the infinite-volume process follows from the factorial
finite-speed bound in Proposition 4.

For the dual, use the historical hull, the smallest interval containing
all sites that have ever belonged to the dual up to the current time.
For an initial nonempty A, an extension of this hull can occur only at
a ring of its left or right endpoint, when that endpoint is occupied.
Total intensity of endpoint rings is at most 2, and each such ring
extends the hull by at most two sites (two only when the hull is a
singleton). Hence its length H_t is stochastically bounded by
H_0+2 Pois(2t), via a rate-2 clock with fictitious rings as necessary.
Once the hull length is bounded, total dual ring rate is bounded by it.
This constructs the nonexplosive finite-set dual and gives, for every
r≥1, E r^{H_t}≤r^{H_0} exp(2t(r²-1)).

The same historical-hull bound holds for the finite-cycle process,
lifting its visited component to an interval before wrapping; after
the entire cycle is visited its number of occupied sites is bounded
by the accumulated visited-hull length as well. More explicitly one
can retain a connected historical visited set, which grows only at its
at most two boundary vertices; each ring adds at most two previously
unvisited vertices. It contains the initial interval A's hull and all
current occupied sites, giving the same bound uniformly in cycle size.
Let K=max(1,p/q). Then |Phi_B(eta)|≤K^{|B|}≤K^{H_t}; the preceding
bound with r=K² ensures uniform square-integrability for all these
finite-cycle and infinite-line variables. Probability of the historical
hull reaching a cycle seam tends to zero as cycle size grows, since
H_t has a Poisson upper bound. Coupling, Cauchy-Schwarz and uniform
square-integrability therefore permit the limit of the dual expectations.
The primal observables Phi_A are bounded independently of cycle size.
This proves (D). A=empty is the trivial constant identity. QED.

For the primal configuration eta^(x) with a single infection at x,
Phi_B(eta^(x))=1-1{x∈B}/q. Consequently

E_{eta^(x)} Phi_A(eta(t)) = 1-P_A(x∈A(t))/q.              (S)

The family {Phi_A: A⊂F} is a basis for all functions of the spins in any
finite F: {1,phi} is a basis on one binary site (the two phi values are
distinct), and its tensor products form the product basis. Under pi,
pi(Phi_A)=0 for nonempty A by independence and mean zero. Thus local
convergence from the single-infection state eta^(x) is equivalent to

P_A(x∈A(t)) → q for every finite nonempty A.              (G)

This is a genuine reduction, not a proof of (G). It handles only the
single-infection primal subclass, and does not imply the full conjecture
because FA-1f is not attractive. For arbitrary primal configurations the
right side of (D) involves products over the random set, and the one-site
dual marginal alone does not control them.

dual_checks.py verifies the generator identity on cycles of sizes 3,4,5
for every pair (A,eta) and q∈{1/4,1/3,1/2,3/4}, in exact rational
arithmetic. The cyclic sizes avoid coincident left/right neighbors.

## Final disposition

STATE: DONE; VERDICT: PARTIAL (2026-10-11). This closes the present
attempt, not the open conjecture. No full proof, counterexample, or exact
solution in later literature was obtained. Propositions 1–6 and the
non-attractiveness test have complete arguments above; external inputs
are the source's reversibility/construction and stationary classification,
plus the standard spectral theorem. The finite computations passed and
the finite Lean certificates compiled successfully.

The sharp remaining singular-start test is (G): for every q∈(0,1), every
finite nonempty dual A and fixed x, prove P_A(x∈A(t))→q. Even solving (G)
would settle only the primal single-infection subclass. For the full
problem one still needs local convergence from every deterministic
nonempty configuration, or an equivalent argument for arbitrary initial
laws. The Cesaro route additionally requires removal of the all-healthy
mixture coefficient and control at individual times.

## Additional serious attempt requested by the user

The previous final disposition above describes the first attempt. The
follow-up, dated 2026-10-11, is written in full in FRESH_ATTEMPT.md and
audited in FRESH_REFEREE.md. It records two approaches not previously
pursued, then develops the sigma-finite reversible heat-kernel route.

New proved partial results: using the independently verified general
one-dimensional component relaxation bound (book Theorem 4.8), both
FA-1f and its neighbor-refresh dual have exponential heat-kernel decay
on the weighted finite-infection state space; their infection counts grow
at least linearly almost surely from every finite nonempty seed, with
continuous-time control. Exact finite-cycle isospectrality and an infinite
stationary Walsh norm identity provide independent checks and reductions.

The fixed-site occupation limit remains unproved. Its test function has
infinite weighted Hilbert norm, and infection-count growth does not prevent
local escape. No full proof or counterexample has been obtained.
