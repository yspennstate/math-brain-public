"""Build review-only mathematics drafts. All writes remain in w339."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
entries = []
problem_for = {}

def add(pid, key, kind, title, statement, proof=None, assumptions=()):
    entries.append({
        'key':key, 'namespace':'probability.open-problems', 'logical_name':'w339-'+key,
        'kind':kind, 'title':title, 'statement':statement, 'proof_text':proof,
        'assumptions':list(assumptions), 'domain':'probability theory',
        'source':{'source_id':'owner-campaign-w339-20261010:'+key,
                  'url':'~/brain_workers/w339/CLAIMS.md',
                  'revision':'unreviewed-2026-10-10-v1',
                  'license':'owner-own-work (campaign proof or attributed rederivation; novelty not claimed)',
                  'excerpt':None},
    })
    problem_for[key] = pid

add('P0267','reciprocal-bes4-finite-horizon', 'lemma',
    'Reciprocal BES(4): finite fixed-time second moment and infinite maximal second moment',
    'Let R be a four-dimensional Bessel process started at r>0. For every S>0, E[R_S^(-2)]=(1-exp(-r^2/(2S)))/r^2, while E[sup_{0<=s<=S} R_s^(-2)]=infinity. More precisely, if tau_b is the first hitting time of b in (0,r), then lim_{b down to 0} P(tau_b<=S)/b^2=exp(-r^2/(2S))/r^2.',
    'R has the law of the radius of a four-dimensional Brownian motion started at a point x with |x|=r, and does not hit zero. The positive identity |y|^(-2)=integral_0^infinity exp(-lambda |y|^2) d lambda and Tonelli give E R_S^(-2)=integral_0^infinity (1+2S lambda)^(-2) exp(-lambda r^2/(1+2S lambda)) d lambda. Substitute v=(1+2S lambda)^(-1) to obtain the stated expectation. The harmonic function |x|^(-2) stopped at tau_b is bounded by b^(-2), so optional stopping at tau_b wedge S gives P(tau_b<=S)/b^2=r^(-2)-E[R_S^(-2);tau_b>S]. As b decreases to zero, the indicators increase to one; integrability and the expectation formula give the positive limit. Substituting b=x^(-1/2) shows x P(sup R^(-2)>=x) tends to this positive constant. Tail integration then gives the infinite expectation.',
    ['r>0', 'S>0', 'BES dimension is exactly four'])

add('P0267','critical-scalar-endpoint-counterexample', 'lemma',
    'Critical scalar SPDE candidate counterexample to endpoint energy-space continuity',
    'For the Ito SDE dU=(U-U^3)dt+sqrt(2)U^2 dW with U_0=a>0, its global strong solution has E U_t^2=e^(2t) a^2 [1-exp(-1/(4 a^2 s(t)))], where s(t)=(e^(2t)-1)/2, for t>0. For every T>0, E sup_{t<=T} U_t^2=infinity. Thus solutions with deterministic initial values a_n=1/n cannot converge to the zero solution in L^2(Omega;C([0,T];R)), despite a_n tending to zero in L^2. This is an unreviewed candidate application to the general numbered Agresti-Veraar Problem 5; it makes no claim about extra hypotheses in the surrounding prose or present openness.',
    'Put r=1/(sqrt(2)a), let R be BES(4) driven by a one-dimensional Brownian motion, and set U_t=e^t/(sqrt(2) R_{s(t)}). Ito applied to 1/(sqrt(2)R) gives drift -z^3 and diffusion -sqrt(2)z^2. Since s prime=e^(2t), the time change and multiplier give drift U-U^3 and diffusion -sqrt(2)U^2; reverse the Brownian sign. BES(4) stays positive, yielding a global solution; local Lipschitz coefficients give pathwise uniqueness and permit simultaneous solutions on a common driver for the countable initial family. The preceding reciprocal-BES lemma gives the fixed-time formula and infinite maximal moment, since e^(2t)>=1. To check the source framework, take V=H=V*=R, A=I, B=0, F(v)=2v-v^3, G(v)=sqrt(2)v^2. Linear coercivity holds with theta=1,M=0. Nonlinear coercivity is v(Av-F(v))-|G(v)|^2/2=-v^2 >= |v|^2-2|v|^2-2. All interpolation norms coincide; rho=2,beta=2/3 gives (2 beta-1)(rho+1)=1 and the polynomial local Lipschitz bounds. The zero initial solution is identically zero. Each positive member has an infinite L^2 maximal distance from it. The fixed-time formula still bounds E integral_0^T U_t^2 dt by a^2 integral_0^T e^(2t)dt. Source: Agresti and Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA (2025), Assumption 6.1, Theorem 6.4, Problem 5, published text lines 4474-4511,4581-4626,9839-9847 in the cache. Earlier campaign construction credited: proofs/P0266_P0267_critical_allen_cahn_counterexamples_candidate.md.',
    ['Ito convention', 'one scalar Brownian driver', 'critical noise coefficient sqrt(2)', 'T>0', 'general numbered Problem 5 only'])

add('C0031','polynomial-smallest-singular-value-not-log-ui', 'lemma',
    'Weak singular-value convergence and a polynomial minimum do not imply logarithmic uniform integrability',
    'For n>=3 let m_n=floor(n/log n), and let D_n be diagonal with m_n diagonal entries 1/n and n-m_n entries 1. Its empirical singular-value measure converges weakly to delta_1 and its smallest singular value is exactly 1/n, but for every fixed epsilon in (0,1), lim_n (1/n) sum_{s_i(D_n)<epsilon} |log s_i(D_n)|=1. Therefore a polynomial lower bound on the minimum, even if deterministic, does not alone establish the logarithmic uniform integrability used in Hermitization.',
    'm_n/n tends to zero, so the fraction of singular values differing from 1 vanishes, proving weak convergence. For sufficiently large n, the only values below epsilon are the m_n copies of 1/n. Their normalized logarithmic sum is m_n log(n)/n, which tends to one. This is a deterministic diagnostic, not a counterexample to the heavy-tailed circular law: intermediate-small-singular-value count control must accompany a summable minimum bound.',
    ['n>=3', 'natural logarithm', 'diagnostic matrices are not the iid random matrices in C0031'])

add('C0031','probability-convergence-a-s-subsequence', 'lemma',
    'Convergence in probability gives a deterministic almost-sure subsequence',
    'If random variables Z_n valued in a metric space satisfy d(Z_n,z) tending to zero in probability for a deterministic z, then some deterministic increasing subsequence n_k satisfies Z_{n_k} tending to z almost surely. This does not upgrade the full sequence: independent Bernoulli variables with P(Z_n=1)=1/n converge to zero in probability but equal one infinitely often almost surely.',
    'Choose n_k increasing so that P(d(Z_{n_k},z)>2^(-k))<=2^(-k). The first Borel-Cantelli lemma gives eventual d<=2^(-k). For the Bernoulli example, the probabilities tend to zero while their sum diverges; independence and the second Borel-Cantelli lemma give infinitely many ones. Applied to a metric for weak convergence of probability measures, this gives an a.s. subsequence of the convergence-in-probability circular law, not the requested full sequence.')

add('C0031','heavy-tailed-circular-law-bounded-density-known', 'concept',
    'The cached heavy-tailed circular law already gives almost-sure convergence with bounded density',
    'Let X be an iid complex-entry matrix array. Assume 0<alpha<2, lim_{t to infinity} t^alpha P(|X_11|>=t)=1, and that the conditional law of X_11/|X_11| given |X_11|>=t converges to a probability measure on the unit circle. If the entry law has a bounded density on C, Bordenave and Chafai, Around the circular law, arXiv:1109.3343, Theorem 6.2, printed page 39, already gives almost-sure weak convergence of the empirical eigenvalue measure of n^(-1/alpha) X to mu_alpha. The unrestricted upgrade is the subsequent remark; the bounded-density special case is not open in this cached source. The stated tail normalization is part of the source model, and present openness without the density assumption is unverified.',
    assumptions=['iid complex entries', '0<alpha<2', 'tail normalization lim t^alpha P(|X_11|>=t)=1', 'conditional angular law converges', 'bounded density on C'])

add('C0134','uniform-right-cookies-speed-lower-bound', 'lemma',
    'A uniform rightward bias gives a velocity lower bound without bounded cookie stacks',
    'Let X be a nearest-neighbor walk on Z whose conditional probability of stepping right at every time is at least p_*>1/2 almost surely. Then liminf_n X_n/n >= 2p_*-1 almost surely (for any fixed finite X_0). This applies to cookie environments with every site and every cookie at least p_*, including infinite stacks. It is a special case with infinite total cookie drift, and does not establish the finite-delta threshold in Kosygina-Zerner Problem 5.3.',
    'Write X_n-X_0=D_n+M_n, where D_n=sum_{j<n} E[X_{j+1}-X_j|F_j]. Then D_n>=n(2p_*-1). The martingale M has increments of absolute value at most 2. Azuma gives P(|M_n|>epsilon n)<=2 exp(-epsilon^2 n/8), a summable bound for every epsilon>0. Borel-Cantelli on rational epsilon implies M_n/n tends to zero. The liminf follows. A constant-cookie choice p_*=3/5 has independent steps, velocity 1/5, and delta=infinity; no finite-migration tail theorem is invoked.',
    ['p_*>1/2 uniformly in site, visit, and history'])

add('P0092','reset-automaton-endogeny-critical', 'lemma',
    'Reset tree automata are endogenous at and below the dependency threshold',
    'On the deterministic rooted b-ary tree, b>=2, let iid vertex innovations reset the state with probability r in (0,1], prescribing a state using that vertex innovation, and otherwise apply any fixed measurable function of the b child states and the local innovation. For a nonempty finite state space, if b(1-r)<=1, there is a unique compatible state assignment almost surely, the root is measurable from all innovations, and the distributional recursion has a unique fixed point. For b(1-r)<1, arbitrary depth-n boundary assignments disagree at the root with probability at most [b(1-r)]^n.',
    'Explore dependencies from the root: a reset vertex has zero dependency children; a nonreset vertex has b. This is a Galton-Watson tree with offspring 0 with probability r and b with probability 1-r. Its generating function f(s)=r+(1-r)s^b has extinction probability one when mean b(1-r)<=1, including criticality since the law is nondegenerate there. Explicitly f(s)-s is positive for 0<=s<1 in the subcritical or critical cases, by convexity and f prime(1)<=1, so one is the only extinction fixed point. Extinction means the dependency tree is finite almost surely. Evaluate the resets at its leaves and then the update functions upward; this determines the root from finitely many innovations and is independent of any boundary assignment. Countably many vertices yield simultaneous compatible uniqueness. Any two fixed-point tree constructions can be coupled on the same innovations and arbitrary boundary states at depth n; disagreement requires a dependency vertex at depth n. Its probability is bounded by E Z_n=[b(1-r)]^n below criticality and tends to zero by extinction also at criticality, proving uniqueness of the fixed-point law. Endogeny is relative to the marked tree, not the bare tree.',
    ['iid innovations', 'b>=2', 'reset state independent of child states', 'endogeny relative to all vertex innovations'])

add('P0439','quantile-slo-capacity-necessary', 'lemma',
    'Service-size and capacity lower bounds for a response-time quantile, allowing abandonment',
    'Consider a stationary ergodic arrival stream of intensity lambda>0, job service requirements S>=0 at unit speed, and k identical servers. Jobs cannot receive service from multiple servers simultaneously, and every successful job must consume its full S units. If a stationary policy completes at least a fraction 1-q of arrivals within deadline D>0, then q>=P(S>D) and k>=lambda integral_0^(1-q) F_S^(-1)(u) du. The latter is a necessary capacity bound even if other jobs are abandoned; it is not a sufficient staffing rule.',
    'A successful job has response at least S, proving the first inequality. Let A be its success indicator. Successful arrivals during [0,t-D] complete during [0,t], so their total service is at most kt. The stationary ergodic reward law, followed by t tending to infinity, gives lambda E[S A]<=k. Among selectors with E A>=1-q, the smallest possible E[S A] is attained by selecting the lowest 1-q quantile of sizes, randomizing at any threshold atom. To verify this, choose threshold c=F^(-1)(1-q) and threshold selector A*. Then (S-c)(E[A|S]-E[A*|S])>=0 pointwise, and c(E A-E A*)>=0, so E[S A]>=E[S A*]. The latter expectation is the quantile integral. End cases q=0 or 1 follow by monotone limits. No FCFS or exponential-law assumption is used.',
    ['stationary ergodic workload and policy', 'unit-speed nonparallel service', '0<=q<=1', 'successful jobs consume their full service', 'D finite and positive'])

add('P0439','mmc-response-slo-floor', 'lemma',
    'FCFS M/M/c response tail and its unattainable service-time floor',
    'For lambda>0,mu>0 and an integer c>lambda/mu, consider stationary FCFS M/M/c. Put a=c mu-lambda and let C be Erlang-C. For t>0, P(R>t)=exp(-mu t)+C mu [exp(-mu t)-exp(-a t)]/(a-mu) if a!=mu, and exp(-mu t)(1+C mu t) if a=mu. For every finite stable c this tail is strictly greater than exp(-mu t), and it tends to exp(-mu t) as c tends to infinity. Hence a finite FCFS staffing level meeting P(R>t)<=q exists exactly when q>exp(-mu t), for 0<=q<=1.',
    'The waiting time is zero with probability 1-C and otherwise exponential of rate a, independently of the tagged exponential service time of rate mu. Convolve the two exponentials to get the formula; at a=mu the convolution is Erlang-two, giving the stated limit. C>0 for finite stable c and lambda>0. The correction term is positive, since the two differences have the same sign; at equality of rates it equals C mu t exp(-mu t)>0. With fixed load L=lambda/mu, write A_c=L^c/[c!(1-L/c)] and C=A_c/(sum_{j=0}^{c-1} L^j/j!+A_c). A_c tends to zero by the ratio test, hence C tends to zero. As a tends to infinity, the correction tends to zero, proving the limiting floor and feasibility. This extends the earlier campaign benchmark with the feasibility boundary; it does not optimize over all scheduling policies.',
    ['Poisson arrivals', 'iid exponential service', 'FCFS', 'lambda>0', 't>0', 'c mu>lambda'])

add('C0040','rwre-forward-half-literature', 'concept',
    'C0040: the invariant-measure-to-ballisticity half is already in the source',
    'Drewitz and Ramirez, Selected topics in random walks in random environment, arXiv:1309.2589, Corollary 2.15, states that under ellipticity (E) and ergodicity (ERG), an invariant probability measure absolutely continuous with respect to the environment law yields an annealed almost-sure law of large numbers. If the walk is transient in a given direction, it is ballistic in that direction. Thus the unresolved implication in the cached Open question 2.19 is the converse, ballisticity implying existence of such an invariant probability measure. Present literature status is not certified by this offline check. The campaign already corrected this in C0040-A002; that correction supersedes C0040-A001.',
    assumptions=['source is the cached 2014 survey', 'no present-openness certification'])

add('C0040','one-dimensional-invariant-density', 'lemma',
    'An explicit one-dimensional invariant environment density under a finite series condition',
    'Let P be a shift-invariant law of nearest-neighbor environments on Z with 0<p_i<1 and rho_i=(1-p_i)/p_i. Define S_1=1+sum_{k>=1} product_{j=1}^k rho_j and Z=E_P[(1+rho_0)S_1]. If Z<infinity, then Q with density h=(1+rho_0)S_1/Z is an invariant probability measure for the environment kernel Kf=p_0 f(theta omega)+(1-p_0)f(theta^(-1)omega). It is equivalent to P and E_Q[2p_0-1]=1/Z>0. For iid rho with m=E rho<1, Z=(1+m)/(1-m). This is a known one-dimensional special case rederived here, not a general answer to C0040.',
    'The finite Z ensures the positive series and density are finite a.s.; h is positive, integrable, and normalized. Write S_i=1+rho_i S_{i+1}, where S_i is the same future series starting at i. The unnormalized density H=(1+rho_0)S_1 obeys p_{-1}H(theta^(-1)omega)=S_0 and (1-p_1)H(theta omega)=rho_1 S_2=S_1-1. Their sum is (1+rho_0)S_1=H. Changing variables using shift invariance proves integral Kf h dP=integral f h dP. Furthermore S_1 is integrable since S_1<=H, and stationarity gives E S_0=E S_1. Consequently E[(1-rho_0)S_1]=E[S_1-S_0+1]=1, and integrating the drift gives 1/Z. In the iid case Tonelli and independence yield E S_1=sum_{k>=0}m^k=1/(1-m), with rho_0 independent of S_1, giving the displayed normalization.',
    ['one dimension', 'shift-invariant P', '0<p_i<1', 'Z finite'])

add('C0079','pivotal-count-distance-sharp', 'lemma',
    'Intrinsic distance is at least pivotal count, without an extra one',
    'In any finite open graph with connected distinct vertices u,v, let K be the number of open edges pivotal for u-v connectivity, and let d be the shortest open-path length. Then d>=K, sharply. A single open edge gives d=K=1, so d>=K+1 is false. On a fully open cycle of length 2L with opposite endpoints, K=0 and d=L; hence no uniform additive upper bound on d-K follows from pivotal count. Pointwise, {u connected to v,K>=N} is contained in {u connected to v,d>=N}, so pivotal tail bounds transfer as lower bounds for intrinsic tails, not as upper bounds.',
    'Each connectivity-pivotal edge belongs to every open u-v path: an open path avoiding it would survive its deletion. A shortest path therefore contains all K distinct pivotal edges, proving d>=K. The one-edge and cycle examples prove sharpness and the lack of a uniform reverse bound. Apply the pointwise inequality on each connected percolation configuration for the event inclusion. The +1 in C0079-A001 is invalid for bond-pivotal count; this correction does not supply the asymptotics in Open Problem 15.5.',
    ['pivotal means deletion of that open edge disconnects u and v', 'distance counts edges', 'u!=v'])

add('C0122','gaussian-noise-near-maximum-deficit', 'lemma',
    'Exact mean deficit of a Gaussian noised maximizer, with arbitrary covariance signs',
    'Let X be a finite centered Gaussian vector, let X prime be an independent copy, and set Y=rho X+sqrt(1-rho^2)X prime for 0<=rho<=1. Let I(Y) be a deterministic measurable tie-broken maximizer of Y and m=E max_i X_i. Then D=max_i X_i-X_{I(Y)} is nonnegative and E D=(1-rho)m. Consequently P(D>delta)<=(1-rho)m/delta for every delta>0. No nonnegativity of off-diagonal covariances is required. This proves near-optimal height of a noised maximizer; it supplies no overlap or multiple-peaks guarantee.',
    'An orthogonal rotation of (X,X prime) gives X=rho Y+sqrt(1-rho^2)Z with Z independent of Y and distributed as X, including degenerate covariance matrices. Thus E[X_i|Y]=rho Y_i, and the tie-breaking index is Y-measurable, so E X_{I(Y)}=rho E max_i Y_i=rho m. Subtracting from E max_i X_i proves the expectation identity. Finite Gaussian maxima are integrable and D>=0 by definition, so Markov applies to D. The signed overlap itself is a different variable.',
    ['finite index set', 'centered jointly Gaussian field', 'independent identically distributed copy', 'fixed measurable tie-break'])

add('C0122','signed-overlap-markov-obstruction', 'lemma',
    'Vanishing signed mean overlap does not justify Markov or a second-moment bound',
    'For X=(Z,-Z), Z standard normal, and its Ornstein-Uhlenbeck copy Y=(Z_t,-Z_t), where Z_t=e^(-t)Z+sqrt(1-e^(-2t))Z prime, the covariance overlap R(I(X),I(Y)) equals 1 when the signs agree and -1 otherwise. Its mean is (2/pi)arcsin(e^(-t)), tending to zero as t tends to infinity, while its second moment is exactly one and P(R>1/2) tends to 1/2. Thus a small mean of a signed overlap alone cannot be used with Markov to conclude a small upper tail. This does not refute chaos-to-multiple-peaks at vanishing noise time for a sequence of fields.',
    'The covariance matrix is [[1,-1],[-1,1]], positive semidefinite, so this is a valid Gaussian field. Its maximum index is determined by the sign of Z (ties have probability zero), making the overlap the product of signs. Represent the correlated normal pair by two projections of an isotropic two-dimensional normal vector: its uniform angle gives sign-disagreement probability arccos(e^(-t))/pi. Therefore E R=1-2 arccos(e^(-t))/pi=(2/pi)arcsin(e^(-t)), and R^2=1. The limiting positive-tail probability is 1/2. The noise times here tend to infinity; the conclusion only invalidates the signed-Markov step in C0122-A001, not the original short-noise conjecture.',
    ['signed covariance overlap', 'this diagnostic uses t tending to infinity'])

add('P0011','sir-scaled-lifetimes-fail-inclusion', 'lemma',
    'Scaled exponential infectious lifetimes can reduce the infected set on a fixed contact schedule',
    'In a four-person SIR model with irreversible removal and certain transmission on a listed contact, let A be initially infectious and allow contacts only A-C at time 0.1, A-B at 1, C-B at 9, and B-D at 10. Coupling iid rate-one exponential infectious lifetimes L_A,L_C,L_B to the longer lifetimes 3L_A,3L_C,3L_B gives positive probability that D is infected in the baseline process but never infected in the longer-lifetime process. Therefore this shared-lifetime coupling does not have pathwise inclusion of infected sets. This is a fixed-contact diagnostic, not a counterexample to Brownian SIR survival or survival monotonicity.',
    'Take the open lifetime box .45<L_A<.55, 11.5<L_C<12.5, and 1.8<L_B<2.2. In the baseline A infects C at .1, is removed before 1, and C survives to infect B at 9. B is still infectious at 10 and infects D. Under scaling by three, A survives to infect B at 1; B is removed between 6.4 and 7.6, cannot be reinfected at 9, and cannot infect D at 10. C survives to 9 in both cases. The open box has positive probability, equal to the product of the three differences of exponential tails. This extends the prior deterministic lifetime example to an explicit positive-probability exponential-removal coupling. The Brownian contact realization is not established.',
    ['fixed contact schedule', 'irreversible removal', 'certain transmission at contacts', 'lifetimes measured from infection'])

add('P0037','co-singleton-bk-unicyclic', 'lemma',
    'BK for arbitrary co-singleton laws and weighted unicyclic spanning trees',
    'Let E be finite and T=E minus {J}, with any distribution q for J. For all increasing events A,B in the full edge-coordinate cube, P(A box B)<=P(A)P(B), where box is disjoint occurrence through coordinate certificates. Consequently BK holds for the weighted spanning-tree law on any finite connected unicyclic graph with strictly positive edge weights, for all increasing events.',
    ROOT.joinpath('P0037_proof.md').read_text(encoding='utf-8'),
    ['increasing events on the full coordinate cube', 'co-singleton support', 'for the graph application: finite connected unicyclic graph and positive weights'])

relations = []
def quote(text, limit=210):
    # JSON-quote the actual slice, including any quotation marks in an old card.
    return json.dumps(text[:limit],ensure_ascii=False)
for child,parent,kind in [
    ('critical-scalar-endpoint-counterexample','reciprocal-bes4-finite-horizon','depends_on'),
    ('mmc-response-slo-floor','quantile-slo-capacity-necessary','specializes'),
    ('one-dimensional-invariant-density','rwre-forward-half-literature','semantic_association'),
    ('signed-overlap-markov-obstruction','gaussian-noise-near-maximum-deficit','semantic_association'),
]:
    a=next(e for e in entries if e['key']==child)
    b=next(e for e in entries if e['key']==parent)
    relations.append({'from_key':child,'to_key':parent,'kind':kind,
                      'rationale':f'From {quote(a["statement"],190)} to {quote(b["statement"],190)}: '+
                                  {'depends_on':'the Bessel minimum lemma supplies the divergent maximal moment.',
                                   'specializes':'the exponential nonparallel-service benchmark has the general service-time floor.',
                                   'semantic_association':'the scope of the general problem is essential to this special-case check.'}[kind]})

cards = json.loads(ROOT.joinpath('store_cards.json').read_text(encoding='utf-8'))
observed_latest={c['metadata']['logical_id']:c for c in cards if c['metadata'].get('logical_id')}
ledger = json.loads(ROOT.joinpath('source_rows.json').read_text(encoding='utf-8'))
titles = {}
for row in ledger:
    if row['row'].get('statement'):
        titles[row['row']['problem_id']] = row['row']['title']
for entry in entries:
    pid=problem_for[entry['key']]
    title=titles[pid]
    matched=[c for c in cards if title.casefold() in c['title'].casefold()]
    for category in ('Open problem:', 'Attempt on'):
        target=next((c for c in matched if c['title'].startswith(category)), None)
        if target and target['metadata'].get('logical_id'):
            # C0040 has an A001 and a superseding A002 under the same logical ID.
            # Bind the quoted end to the observed superseding revision, as the validator does.
            target=observed_latest[target['metadata']['logical_id']]
            relations.append({'from_key':entry['key'],
                              'to_existing_logical':target['metadata']['logical_id'],
                              'kind':'cites',
                              'rationale':f'From {quote(entry["statement"])} to existing card {quote(target["body"])}: {pid} scope/prior-attempt evidence; new result remains unreviewed.'})
            if category=='Attempt on' and entry['key'] in ('pivotal-count-distance-sharp','signed-overlap-markov-obstruction'):
                needle='plus one' if entry['key']=='pivotal-count-distance-sharp' else 'by Markov'
                start=target['body'].find(needle)
                if start>=0:
                    excerpt=target['body'][max(0,start-110):start+180]
                    relations.append({'from_key':entry['key'],
                                      'to_existing_logical':target['metadata']['logical_id'],
                                      'kind':'refutes',
                                      'rationale':f'From {quote(entry["statement"])} to prior inference {quote(excerpt,290)}: refutes only this quoted inference, not the general open problem or every part of the earlier attempt.'})

bundle={'spec':'mathbrain-draft-v1','author_agent':'w339','bundle_slug':'w339-open-problems-checked-special-cases-001','entries':entries,'relations':relations}
dest=ROOT/'drafts'
dest.mkdir(exist_ok=True)
dest.joinpath('bundle_001.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
doc=['All claims below are UNREVIEWED, pending w347. No present-openness or novelty certification; no open problem is reported as solved. Source statements and prior attempts are in source_rows.json; observed existing logical IDs and quotations are in store_cards.json.\n']
rows=[]
previous=[json.loads(line) for line in ROOT.joinpath('results.jsonl').read_text(encoding='utf-8').splitlines()]
old_ids={r['entry_key']:r['row_id'] for r in previous if r.get('entry_key')}
next_id=max(int(r['row_id'].rsplit('.',1)[1]) for r in previous)+1
for e in entries:
    pid=problem_for[e['key']]
    doc.append(f'## {pid}: {e["title"]}\n\nLabel: '+('source-scope correction' if e['kind']=='concept' else 'proof; pending independent audit')+'\n\n'+e['statement']+'\n\n'+(e['proof_text'] or 'Primary source read directly; see source_excerpt_report.md. This confirms C0040-A002 rather than reviewing its audit.')+'\n')
    source=next((r for r in reversed(ledger) if r['row'].get('problem_id')==pid and r['row'].get('statement')),None)
    row_id=old_ids.get(e['key'])
    if row_id is None:
        row_id=f'S1.O.w339.{next_id:03d}'
        next_id+=1
    rows.append({'row_id':row_id,'problem_id':pid,'entry_key':e['key'],
                 'label':'source-scope correction' if e['kind']=='concept' else 'proof; unreviewed',
                 'statement':e['statement'],'proof_file':'~/brain_workers/w339/CLAIMS.md',
                 'source':source['file']+':'+str(source['line']),
                 'source_quote':source['row']['statement'],
                 'audit_status':'PENDING w347','full_problem_solved':False,
                 'novelty':'not claimed'})
ROOT.joinpath('CLAIMS.md').write_text('\n'.join(doc),encoding='utf-8')
first=ROOT.joinpath('results.jsonl').read_text(encoding='utf-8').splitlines()[0]
ROOT.joinpath('results.jsonl').write_text(first+'\n'+''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
ROOT.joinpath('entry_problem_map.json').write_text(json.dumps(problem_for,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'entries':len(entries),'relations':len(relations),'problems':len(set(problem_for.values()))}))
