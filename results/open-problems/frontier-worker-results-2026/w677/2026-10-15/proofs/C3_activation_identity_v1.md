# C3_activation_identity v1 — standard first-moment tool, no novelty claim

For the ordinary one-frog simple-random-walk model on the infinite rooted d-ary tree, d>=2, start one active frog at the root and one sleeping frog at each other vertex. Write p_n for the probability a particular depth-n vertex is ever activated. Let N count all visits to the root by all frogs, including the initial frog's presence at time zero. Then, as an equality of extended nonnegative expectations,

    E[N] = d/(d-1) * (1 + sum_(n>=1) p_n).                 (1)

For returns R excluding that initial presence,

    E[R] = 1/(d-1) + d/(d-1) * sum_(n>=1) p_n.            (2)

In particular, finite expected root returns are equivalent to summability of these activation probabilities. Summability proves transience almost surely. Non-summability does not by itself prove recurrence: a finite almost surely random variable can have infinite mean. This is a standard Green-function reduction derived for this task, not a new solution or a novelty claim. Independent review pending.

The hardest unresolved step in this route is a summable upper bound on p_n for d=4 that retains cross-branch activations. No such estimate is supplied here.

## Proof

Attach the entire independent walk S_v to the initially sleeping frog at v, but do not use it until activation. Let A_v be the event v is activated. Replace the sleeping frog at v by no frog, keeping every other path and the initial active frog unchanged. Up to the first visit to v the two systems coincide, since the sleeping frog has not yet taken any step. Thus the event that v is ever visited is the same in these two systems. In the modified system it is measurable using only the other frogs' paths. Consequently A_v is independent of S_v. This is independence of an activation event from its own unused frog path; it is not independence between different activation events.

Let L_v be the total number of root visits on S_v, counting its time-zero position (only relevant for v=root). The actual contribution of a non-root frog is 1_(A_v)L_v, regardless of the random activation time. Every root visit in the full system belongs to exactly one frog, so pathwise N=L_root+sum_(v!=root)1_(A_v)L_v. Tonelli gives

    E[N]=E[L_root]+sum_(v!=root) P(A_v) E[L_v].

A single random walk at depth n>0 has inward transition probability 1/(d+1) and outward probability d/(d+1). The probability it ever reaches depth zero is d^(-n). One direct proof uses the martingale d^(-D_t) stopped when the depth hits either 0 or m, m>n. This stopped chain is finite and absorbed almost surely, so optional stopping of the bounded martingale yields

    P_n(hit 0 before m)=(d^(-n)-d^(-m))/(1-d^(-m)).

As m tends to infinity these events increase to eventual root hitting: any finite path to the root has a finite maximum depth. Their probabilities tend to d^(-n).

Starting at the root, a simple walk first moves to depth one and subsequently returns with probability 1/d. By the strong Markov property, its number of root visits including time zero is geometric with mean G(root,root)=1/(1-1/d)=d/(d-1). Starting at v of depth n, the walk contributes no root visits if it never hits the root; conditional on the first hit, its future visit count has the root-started law. Hence

    E[L_v]=d^(-n)*d/(d-1).

The initial model and path law are invariant under rooted-tree automorphisms, so P(A_v)=p_n at every vertex of depth n. There are d^n such vertices. Substitution cancels these two powers of d and proves (1); subtract one to obtain (2). All summations and limiting expectations are nonnegative, so no integrability assumption was used before the equality.

If sum p_n is finite, (2) gives a finite mean and therefore R<infinity almost surely. Conversely (2) gives the exact finite-mean equivalence; it does not convert almost sure finiteness into finite mean. For example a random integer K with P(K=k)=1/(k(k+1)), k>=1, is finite almost surely but E[K]=sum_(k>=1)1/(k+1)=infinity.

A proposed geometric activation estimate p_n<=C alpha^n with 0<=alpha<1 would imply E[R]<=1/(d-1)+d C alpha/((d-1)(1-alpha)). Such an estimate has not been established for d=4. Finite-depth estimates are lower bounds on infinite activation probabilities and do not supply the missing upper tail.

Source context: HJJ arXiv:1404.6238 defines the ordinary model and distinguishes expectation-based simulation evidence in Section 5. The displayed identity is the worker's standard-tool derivation from Tonelli and the tree hitting probability; no paper-specific new theorem is attributed to HJJ.
