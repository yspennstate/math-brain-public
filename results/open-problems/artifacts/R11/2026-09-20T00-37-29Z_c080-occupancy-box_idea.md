# R11 idea note — exchangeable collision compiler and occupancy-box model C080

Methods pursued this run: #3 PROVE SOMETHING STRONGER, #16 COMPUTE EVERY SMALL CASE, #25 COUNT THE SAME THING TWICE.

This note is intentionally committed before any checker code.

## Stronger route

Generalize C079 from a uniform shuffle of one deterministic microblock partition to an arbitrary fresh exchangeable random partition Xi_N of the ambient labels at each proposal. Color each Xi_N-block independently Bernoulli(x), where x=j/N is the harmonic-grid mark. Let

c_N = P(1 and 2 lie in the same Xi_N-block).

For a visible m-set, the probability that some visible pair collides in Xi_N is at most binom(m,2)c_N. Conditional on no collision, the visible colors are exactly iid Bernoulli(x). Because any specified nontrivial binary split requires at least one red and one blue partition block, its markwise probability is at most 2x(1-x). Hence the harmonic clock 1/[2N x(1-x)] cancels the singular factor, giving the generator comparison

|q_N(A|B)-q_N^iid(A|B)| <= binom(m,2)c_N (N-1)/N.

For two labels the formula is exact:

q_N(1|1) = (N-1)/N * (1-c_N).

Therefore c_N -> 0 is necessary and sufficient for every fixed finite restriction to converge to CTCS. This strictly strengthens U059 by removing deterministic block sizes.

A uniform-in-k strengthening should follow because the iid harmonic-grid Riemann-sum error for a specified i|j split, i+j=m, is at most (m-1)/N. Thus for all m<=k,

delta_{N,k} <= binom(k,2)c_N + (k-1)/N.

A partition state on k labels has at most 2^(k-1)-1 available binary split transitions, so common-clock coupling should give path-TV error on [0,T] at most

T(2^(k-1)-1) delta_{N,k}.

This yields growing-k convergence whenever 2^k(k^2 c_N + k/N)->0.

## Concrete new class C080: iid occupancy boxes

At each proposal, independently assign every ambient label to one of M_N boxes uniformly; color each box independently Bernoulli(x); a label inherits its box color. Take

M_N = max(2, floor(sqrt(N))).

The induced ambient partition is exchangeable and has exact pair-collision probability c_N=1/M_N. Hence C080 has the CTCS(infinity) limit. Moreover every restriction of size k_N=floor(alpha log_2 N) with fixed alpha<1/2 converges in path total variation on finite horizons, because M_N ~ sqrt(N).

This is distributionally different from C079: C079 conditions the dependence cells to have deterministic sizes, whereas C080 has multinomially random occupancy sizes at every proposal.

## Count the same object twice

Let R be the number of red boxes, R~Bin(M,x). Conditional on all box colors, labels choose boxes independently, hence their colors are iid Bernoulli(P) with P=R/M. Therefore the exact probability of a specified unordered i|j split is

E[P^i(1-P)^j + P^j(1-P)^i].

This must agree with direct enumeration over box assignments and box colors. It gives a second exact derivation of the generator and a convenient checker.

For N=4, M_4=2, preliminary exact algebra predicts

q(1|3)=3/32 for each specified singleton split,
q(2|2)=3/32 for each specified balanced split,
Lambda_root=21/32,
P(root is 2|2)=3/7.

Source CTCS(4) has q(1|3)=1/3, q(2|2)=1/6 and balanced-root probability 3/11. Thus C080 is not a leaf relabeling or positive global time-rescaling of the source. It is also not C079, whose N=4 balanced-root probability is 1 and whose 1|3 rates vanish.

Pending before promotion: exact checker, current-prior-art search for this occupancy-box mechanism, full hidden-label lumping/path proof, and immutable run report. Independent audits remain absent, so even if the author-side proof succeeds the source-level campaign status stays PARTIAL.
