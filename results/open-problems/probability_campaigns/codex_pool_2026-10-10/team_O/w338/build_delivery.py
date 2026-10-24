"""Build only local review artifacts. publish_draft.py copies the authorized draft.

The mathematical statements below are self-contained; all remain pending w346.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
cards = json.loads((ROOT/'assigned_store_cards.json').read_text(encoding='utf-8'))
extra = json.loads((ROOT/'matched_store_cards.json').read_text(encoding='utf-8'))
majority = json.loads((ROOT/'majority_measurements.json').read_text(encoding='utf-8'))
measurements = json.loads((ROOT/'special_case_measurements.json').read_text(encoding='utf-8'))
definitions = []

def result(pid, namespace, name, title, statement, proof, assumptions, scope, quote):
    definitions.append(dict(pid=pid, namespace=namespace, name=name, title=title,
                            statement=statement, proof=proof, assumptions=assumptions,
                            scope=scope, quote=quote))

result('P0266', 'probability.stochastic',
 'allen-cahn-scalar-subcritical-maximal-second-moment-bound',
 'Scalar Allen-Cahn maximal moment: explicit subcritical bound and critical failure',
 '''For dU_t=(U_t-U_t^3)dt+gamma*U_t^2 dW_t, U_0=a>0, and 0<gamma^2<2,
E sup_{0<=t<=T} U_t^2 <= a^2 exp(2T)*(gamma^2+2)/(2-gamma^2) for every T>0.
At gamma^2=2 this expected supremum is infinite, while at every fixed t>0
E U_t^2=a^2 exp(2t)*(1-exp[-1/(2*a^2*(exp(2t)-1))]) is finite.''',
 '''Changing the sign of W permits gamma>0. Put delta=3+2/gamma^2,
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
no renewed review of the old review receipt or novelty certification is claimed.''',
 ['Ito convention; scalar Brownian driver', 'Deterministic a>0 and finite T>0',
  'Scalar equation only; no claim about all additional SPDE hypotheses'],
 'Explicit scalar bound and critical check; no new full SPDE solution or present-openness certification.',
 'E sup_{0<=t<=T} U_t^2 <= a^2 exp(2T)*(gamma^2+2)/(2-gamma^2)')

result('C0021', 'probability.boolean',
 'iterated-three-majority-depth-two-optimal-revealment-and-composition',
 'Depth-two 3-majority optimum and improved block-composition revealment',
 '''For iterated 3-majority f_2 on nine iid fair bits, the minimum expected
number of zero-error single-bit queries is 393/64 and the minimum revealment
is 131/192. For general depth k, an explicit composed algorithm achieves
delta_k <= (131/192)^floor(k/2)*(5/6)^(k mod 2). Thus the achievable exponent
for even depths is -log(131/192)/(2 log 3)=0.17399134015245032.
This is an achievable bound; it does not determine the exact asymptotic exponent.''',
 (ROOT/'C0021_result.md').read_text(encoding='utf-8'),
 ['Uniform independent bits', 'Zero error; query one previously unqueried bit at each step',
  'Randomized algorithms may use tree automorphisms and independent subtree randomness'],
 'Exact finite computation and proved composition; novelty and independent audit pending; asymptotic optimum unresolved.',
 'the minimum revealment\nis 131/192')

result('C0133', 'probability.randomenvironment',
 'fair-cookie-walk-zero-speed-and-polynomial-spatial-excursion-tail',
 'Fair-cookie walk: zero speed, but a polynomial unrestricted excursion tail',
 '''For simple symmetric random walk S on Z starting at zero, if tau is its
first positive return to zero and L>=1 is an integer, then
P(max_{0<=n<=tau}S_n>=L)=1/(2L). Nevertheless S_n/n->0 almost surely.
This fair-cookie example satisfies bounded stacks and uniform ellipticity,
so those assumptions alone do not imply an exponential unrestricted spatial
excursion tail. This does not contradict an exponential estimate with a specified
linear time budget.''',
 '''A positive excursion begins with probability 1/2. From one, the probability
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
forces that limit to be zero, but recurrence does not establish existence of the limit.''',
 ['One-dimensional walk; every cookie is fair', 'Unrestricted spatial height until first return',
  'No conclusion for general excited cookie environments'],
 'A solved special case and a scoped obstruction to the earlier tail route; general C0133 remains unverified.',
 'P(max_{0<=n<=tau}S_n>=L)=1/(2L)')

result('P0090', 'probability.branching',
 'reachable-type-resolvent-certificate-for-pivot-branching-extinction',
 'Extinction certificate for the types reachable from a pivot population',
 '''Let Z be a finite-type Galton-Watson process with finite mean matrix M
(row i lists expected type-j children) and finite deterministic initial population z.
Let R be the forward-reachable types from the support of z. If rho(M_R)<1,
then w=(I-M_R)^(-1)*1 is finite, positive, and M_R*w=w-1.
The expected total population is z_R*w<infinity, hence extinction occurs almost surely.
Unreachable supercritical types do not affect this conclusion; positive regularity
is unnecessary. This is a branching-process certificate, not a full interpretation criterion.''',
 '''R is closed under positive-mean child edges; a child count of mean zero
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
initial support are correctly identified. It makes no critical interpretation claim.''',
 ['Finite type set and finite offspring means', 'Correct initial support and mean matrix',
  'Pivot interpretation requires separate identification of the process'],
 'Generalizes the earlier global subcritical calculation to reachable classes; critical/supercritical interpretation is unresolved.',
 'The expected total population is z_R*w<infinity')

result('P0090', 'probability.branching',
 'critical-deterministic-type-cycle-does-not-become-extinct',
 'Critical multitype deterministic cycles need not become extinct',
 '''A three-type Galton-Watson process in which every particle has exactly one
child of the next type cyclically has spectral radius one and exactly one particle
in every generation when started from one particle. Thus criticality alone,
without a nonsingularity hypothesis, does not imply multitype extinction.''',
 '''The mean matrix is [[0,1,0],[0,0,1],[1,0,0]]. Its cube is the identity,
so its eigenvalues have modulus one and its spectral radius is one. Each particle
deterministically replaces itself by exactly one particle of the next type;
induction gives population one at every generation. This is an abstract branching
example and is not asserted to realize all hypotheses of the tree-automaton problem.''',
 ['Deterministic one-child cycle', 'No automatic realization as a problem-specific pivot tree'],
 'Refutes only unconditional critical-means-extinct reasoning, not a qualified automaton theorem.',
 'criticality alone,\nwithout a nonsingularity hypothesis, does not imply multitype extinction')

result('P0427', 'probability.queueing',
 'two-exponential-jobs-no-arrival-continuation-aware-allocation',
 'Exact no-arrival reduction for two exponentially sized parallel jobs',
 '''Two independent jobs have unit-mean exponential inherent work and increasing,
continuous speed curves r_1,r_2 on [0,S], with r_i(0)=0 and r_i(b)>0 for b>0.
There are no arrivals, service is divisible and preemptible, and all S servers are
allocated. Let V_1=1/r_1(S) and V_2=1/r_2(S). The optimal expected sum of
completion times, even over history-dependent allocations, equals
min_{0<=b<=S} [2+r_1(b)*V_2+r_2(S-b)*V_1]/[r_1(b)+r_2(S-b)].
An optimal policy keeps a minimizing allocation until the first completion,
then assigns all servers to the survivor. This does not characterize a queue with arrivals.''',
 '''Exponential memorylessness makes the two-alive state independent of consumed
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
are evidence, not an exact closed form or a Poisson-arrival policy theorem.''',
 ['Independent Exp(1) inherent work', 'No arrivals', 'Continuous increasing positive speed curves',
  'Divisible preemptible allocations summing to S'],
 'Proves a no-arrival two-job reduction; the numeric minimizer is not claimed exactly or for stationary queues.',
 'An optimal policy keeps a minimizing allocation until the first completion')

result('C0032', 'probability.random-matrices',
 'negative-logarithmic-potential-requires-negative-laplacian-density-sign',
 'Correct density sign for a negative logarithmic potential',
 '''For a finite positive measure mu on C with finite logarithmic moment, define
U(z)=-integral log|z-w| mu(dw) as a locally integrable potential. In distributions,
Delta U=-2*pi*mu. If mu has Lebesgue density g, then g=-(1/(2*pi))*Delta U.
The positive Laplacian sign used with this negative potential in C0032-A001 is incorrect.''',
 '''For a compactly supported smooth test function, integrate log|z| times its
Laplacian over the complement of a disk of radius epsilon and integrate by parts.
The inner boundary term converges to 2*pi times the test function at zero;
the term containing epsilon*log(epsilon) vanishes. Thus Delta log|z|=2*pi*delta_0.
Translation and Fubini (local integrability and the logarithmic-moment condition)
give Delta U=-2*pi*mu. Absolute continuity gives the density formula.
As a check, the negative logarithmic potential of uniform probability on the
unit disk is (1-|z|^2)/2 inside the disk and -log|z| outside; its interior
Laplacian is -2, so the corrected formula gives density 1/pi rather than -1/pi.
This sign correction neither closes the PWIT recursion nor identifies g_alpha.''',
 ['Planar distributional Laplacian', 'Finite positive measure with finite logarithmic moment',
  'Lebesgue density only for the last formula'],
 'Corrects a source-attempt sign; heavy-tailed circular-law density remains unresolved.',
 'Delta U=-2*pi*mu')

result('C0077', 'probability.percolation',
 'rare-event-conditioning-needs-joint-test-asymptotics',
 'Rare-event conditioning requires joint test asymptotics',
 '''Unconditional convergence, even almost sure convergence, and an exact
survival probability of order 1/n do not suffice for a conditioned scaling limit.
For U uniform on (0,1), let A_n={U<=1/n} and Z_n=a_n*1_{A_n}, with a_n=1
for even n and 2 for odd n. Then Z_n->0 almost surely and n*P(A_n)=1 exactly,
but Law(Z_n|A_n) alternates between point masses at one and two.
A valid sufficient replacement on a Polish state space is: n*P(A_n)->c>0
and n*E[f(Z_n)*1_{A_n}]->c*integral f dnu for every bounded continuous f;
then Law(Z_n|A_n) converges weakly to nu.''',
 '''Almost every uniform U is positive; once n>1/U the indicator is zero.
Conditioned on A_n, Z_n equals a_n deterministically, so a bounded continuous
test separating one from two proves nonconvergence. The event probability is
exactly 1/n. For the sufficient replacement, divide the assumed joint-test
asymptotic by n*P(A_n); the resulting conditional expectations converge to nu(f),
which is weak convergence by its bounded-continuous-test characterization.
This demonstrates a missing requirement in the shorthand C0077<=C0076+C0066
when only an unconditioned limit and a one-arm constant are supplied. It does not
disprove the IIC conjecture or the prior attempt's explicitly added commutation
assumption. No percolation joint-test asymptotic is proved here.''',
 ['Rare events have positive probability', 'Polish state space for weak-convergence criterion',
  'No assertion that the toy process is percolation'],
 'A checked obstruction and precise conditional reduction; not an IIC scaling limit.',
 'survival probability of order 1/n do not suffice for a conditioned scaling limit')

result('C0119', 'probability.gaussian',
 'gaussian-polymer-ou-overlap-bound-from-free-energy-variance',
 'Dimension-free Gaussian polymer overlap bound conditional on superconcentration',
 '''For a finite family of n-step paths and iid standard Gaussian time-site
energies X, let F(X)=log sum_paths exp(beta*sum_path X), beta>0. Write
p_j(X) for the Gibbs probability of occupying time-site j, and
X^t=exp(-t)*X+sqrt(1-exp(-2t))*X', with X' independent. Define
Q(t)=E sum_j p_j(X)*p_j(X^t). Then
Var(F)=beta^2*integral_0^infinity exp(-t)*Q(t)dt and
Q(t)<=Var(F)/(beta^2*(1-exp(-t))) for t>0.
Consequently Var(F_n)=o(n) and t_n->0 with Var(F_n)/(n*t_n)->0 imply
Q_n(t_n)/n->0 in every spatial dimension. If additionally Q_n(0)>=c*n,
the perturbed overlap is o(Q_n(0)). The needed variance and initial-overlap
estimates in the target low-temperature regime are not established here.''',
 '''Differentiate the finite partition function to obtain partial_j F=beta*p_j.
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
gradient identity in 1D and 3D; the OU identity is proved by the displayed expansion.''',
 ['Finite family of n-step time-indexed paths', 'Independent standard Gaussian energies; fixed beta>0',
  'Unproved asymptotic variance and unperturbed-overlap hypotheses are explicit'],
 'A conditional Gaussian reduction; no unconditional higher-dimensional chaos solution.',
 'Q(t)<=Var(F)/(beta^2*(1-exp(-t))) for t>0')

result('P0010', 'probability.percolation',
 'biased-square-lattice-finite-outgoing-boundary-balance',
 'Exact closed-boundary weight in the biased square-lattice orientation model',
 '''Independently orient each horizontal Z^2 edge right with probability p
and each vertical edge up with probability p. For any finite vertex set S,
if boundary(S) is its set of edges with exactly one endpoint in S, then
P(no edge leaves S)=[p*(1-p)]^(|boundary(S)|/2).
In particular the origin is a sink with probability p^2*(1-p)^2, so the
probability theta(p) of an infinite directed path from the origin obeys
theta(p)<=1-p^2*(1-p)^2. The boundary condition is necessary but is not
sufficient for S to be exactly the reachable cluster of the origin.''',
 '''On each horizontal lattice line, the indicator of finite S has equally many
0-to-1 and 1-to-0 transitions. Thus the number of left-side and right-side
horizontal boundary edges is equal, say h each. The analogous vertical counts
are v each. Making every boundary edge point into S requires h+v edges to
have their positive-coordinate orientation and h+v to have their negative one.
Independence gives [p*(1-p)]^(h+v), and the boundary size is 2(h+v).
For a singleton h=v=1, yielding the sink probability. A sink cannot begin an
infinite path. Other closed sets can contain vertices not reachable from the
origin, so this weight alone does not prove stochastic domination or survival
for every nonzero bias. Exhaustive boundary orientation checks cover three
shapes of perimeters four, six, and eight at five rational biases.''',
 ['Independent orientations', 'Common right/up probability p in [0,1]',
  'Finite S; full boundary includes holes'],
 'An exact finite-set identity and necessary-event bound; the small-bias survival question is unresolved.',
 'P(no edge leaves S)=[p*(1-p)]^(|boundary(S)|/2)')

result('P0036', 'probability.percolation',
 'cayley-spanning-tree-percolation-growth-lower-bound-and-solved-cases',
 'Growth lower bound and equality cases for Cayley spanning-tree percolation',
 '''Let G be an infinite locally finite Cayley graph with ball growth rate
b=lim_n |B_G(e,n)|^(1/n), and let T be any spanning tree using edges of G.
Then p_c(T)>=1/b. In particular subexponential growth (b=1) implies p_c(T)=1.
If G is the usual 2r-regular Cayley tree of a free group, T=G and
p_c(T)=1/(2r-1)=1/b. The arbitrary exponential-growth geodesic-tree equality
asked in P0036 is not proved by these cases.''',
 '''There is a unique T-path from any vertex v to a vertex at T-distance n.
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
geodesic spanning tree of an exponential-growth Cayley graph.''',
 ['Infinite locally finite Cayley graph and connected spanning tree',
  'Independent Bernoulli bond percolation', 'Free-group equality is only for its usual tree generators'],
 'Proves subexponential and free-group tree cases; the arbitrary exponential geodesic case remains unresolved.',
 'Then p_c(T)>=1/b')

entries = []
relations = []
edge_evidence = []
proof_sections = []
status_rows = []

def selected_card(pid, attempt=False):
    ns = cards[pid.lower()]
    if attempt:
        return next((n for n in ns if n['title'].startswith('Attempt on')), None)
    if pid=='P0266':
        return next((n for n in ns if 'CANDIDATE' in n['title']), ns[0])
    return next(n for n in ns if n['title'].startswith('Open problem:'))

for i,d in enumerate(definitions,1):
    key = f"w338-{d['pid'].lower()}-{i:02}"
    statement = 'AUTHOR-CHECKED; independent w346 audit PENDING. '+d['statement']
    entry = dict(key=key,namespace=d['namespace'],logical_name=d['name'],kind='lemma',
                 title='Author-checked: '+d['title'],statement=statement,proof_text=d['proof'],
                 assumptions=d['assumptions'],domain='probability theory',
                 source=dict(source_id=f"owner-campaign:w338:{d['name']}",
                             url='file:///~/brain_workers/w338/PROOFS.md',
                             revision='author-checked-2026-10-10-audit-pending',
                             license='owner-own-work',excerpt=d['quote'].replace('\n',' ')))
    entries.append(entry)
    target = selected_card(d['pid'])
    target_quote = target['body'].split(' Source:')[0].split('\n')[0]
    # Preserve the complete mathematical source sentence, excluding status boilerplate.
    if '). ' in target_quote:
        target_quote = target_quote.split('). ',1)[1]
    link_kind = 'specializes'
    if d['pid']=='P0266':link_kind='generalizes'
    if d['pid'] in {'C0032','C0119'}:link_kind='semantic_association'
    if d['pid']=='C0077' or (d['pid']=='P0090' and i==5):link_kind='analogous_to'
    relation = dict(from_key=key,to_existing_logical=target['logical_id'],
                    kind=link_kind,
                    rationale=f'FROM "{d["quote"]}"; TO "{target_quote}". {d["scope"]}')
    relations.append(relation)
    edge_evidence.append(dict(from_key=key,to_existing_logical=target['logical_id'],
                              kind=relation['kind'],from_quote=d['quote'],
                              to_quote=target_quote,target_body=target['body']))
    old = selected_card(d['pid'],attempt=True)
    if old:
        old_quote = old['body'].split(' Result: ',1)[-1].split(' Check: ',1)[0]
        if old_quote == old['body']:
            old_quote = old['body'].split('Result: ',1)[-1].split(' Obstruction:',1)[0]
        old_quote = old_quote.split('. ',1)[0]+('.' if '. ' in old_quote else '')
        kind = 'generalizes' if d['pid'] in {'P0090','P0427'} and i!=5 else 'semantic_association'
        if d['pid']=='C0032':
            kind='refutes'
            old_quote='The density is g_alpha(r) = (1/2pi) Delta_z of the log-potential U(z) = -integral log|z-w| dmu_alpha(w)'
        relations.append(dict(from_key=key,to_existing_logical=old['logical_id'],kind=kind,
                               rationale=f'FROM "{d["quote"]}"; TO "{old_quote}". {d["scope"]}'))
        edge_evidence.append(dict(from_key=key,to_existing_logical=old['logical_id'],kind=kind,
                                  from_quote=d['quote'],to_quote=old_quote,target_body=old['body']))
    source_locator = target['body'].split('Source:',1)[-1].split('\n')[0].strip()
    if d['pid']=='P0266':
        source_locator='Agresti and Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA (2025), Problem 4, journal p. 130; arXiv:2501.18561. Prior candidate is unrefereed; this packet checks only the scalar construction.'
    status_rows.append(dict(problem_id=d['pid'],cached_status='candidate_refutation' if d['pid']=='P0266' else 'source_says_open_current_unverified',
                            primary_reference=source_locator,prior_attempt_logical=(old or target)['logical_id'],
                            result_kind='proof with exact computational certificate' if d['pid']=='C0021' else 'proof of special case, lemma, or scoped obstruction',
                            independent_audit='PENDING_W346',scope=d['scope']))
    proof_sections.append(f"## {d['pid']}: {d['title']}\n\nLabel: author-checked proof; w346 audit pending.\n\n{d['statement']}\n\n{d['proof']}\n\nScope: {d['scope']}\n\nCached primary reference: {source_locator}\n")

# Link the majority construction to the exact prior bound it improves.
bound = next(n for n in extra['iterated 3-majority'] if 'exponent-between' in (n.get('logical_id') or ''))
qfrom = 'the minimum revealment\nis 131/192'
qto = 'The greedy recursive algorithm (evaluate two random children, the third only if they disagree) has revealment (5/6)^k'
relations.append(dict(from_key=entries[1]['key'],to_existing_logical=bound['logical_id'],kind='cites',
                       rationale=f'FROM "{qfrom}"; TO "{qto}". The finite-block construction improves the recorded greedy upper bound; the influence lower bound and asymptotic gap remain.'))
edge_evidence.append(dict(from_key=entries[1]['key'],to_existing_logical=bound['logical_id'],kind='cites',
                          from_quote=qfrom,to_quote=qto,target_body=bound['body']))

bundle = dict(spec='mathbrain-draft-v1',author_agent='w338',
              bundle_slug='open-problems-w338-exact-majority-and-scoped-lemmas-001',
              entries=entries,relations=relations)
(ROOT/'bundle_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')
(ROOT/'edge_evidence.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in edge_evidence),encoding='utf-8')
(ROOT/'problem_statuses.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in status_rows),encoding='utf-8')
(ROOT/'PROOFS.md').write_text('# w338 ten-problem proof packet\n\nAll claims are pending independent w346 audit. Cached sources establish historical problem statements, not present openness. No web search was used.\n\n'+'\n'.join(proof_sections),encoding='utf-8')

# Preserve the first two immediate-save rows and append the finished batch idempotently.
existing = [json.loads(line) for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines()]
known = {r.get('entry_key') for r in existing}
for i,(entry,d) in enumerate(zip(entries,definitions),3):
    if entry['key'] in known:continue
    r = dict(row_id=f'S1.O.w338.{i:03}',problem_id=d['pid'],entry_key=entry['key'],
             label='proof with exact computational certificate' if d['pid']=='C0021' else 'proof',
             audit_status='PENDING_W346',claim=d['statement'],proof_file=str(ROOT/'PROOFS.md'),
             source_logical=selected_card(d['pid'])['logical_id'],
             source_quote=selected_card(d['pid'])['body'].split('\n')[0],scope=d['scope'])
    if d['pid']=='C0021':r['measurements']=majority
    elif d['pid'] in measurements:r['measurements']=measurements[d['pid']]
    with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(json.dumps(dict(entries=len(entries),relations=len(relations),problems=len(set(d['pid'] for d in definitions))),indent=2))
