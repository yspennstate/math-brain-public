# An online clique barrier with bounded deletions

All logarithms in this note are to base two. For a finite vertex set U, write P(U) for its unordered pairs.

## The previously established bound

David Gamarnik, Eren C. Kızıldağ and Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1, condition (1), and Theorem 2.2, imply the following statement by graph complementation.

Fix ε>0 and put

\[
x=\log_2 n,\qquad L=x-1,\qquad
c=\frac{\min\{\varepsilon^2,1\}}8,\qquad
\xi=\frac{\min\{\varepsilon^2,1\}}{64},\qquad q=cL^2.
\]

For sufficiently large n, an irrevocable online clique algorithm A on H∼G(n,1/2), with exceptional query union E_A, satisfies

\[
\Pr\{|A(H)|\ge(1+\varepsilon)x\}\le 2^{-\xi L^2}                 \tag{1}
\]

if |E_A∩P(A(H))|≤q on every execution. At round t the algorithm chooses a previously uninspected vertex, receives its adjacencies to all previously inspected vertices, selects one set of exceptional pair queries, and then either adds the current vertex or rejects it forever. All choices may depend on the revealed information and an independent random seed. There is no bound on computation time.

Indeed, reversing all edge answers simulates A on the complement, which also has distribution G(n,1/2). The independent-set theorem uses log₂(n/2)=L and gives (n/2)^(−ξL)=2^(−ξL²). Its target (1+ε)L is smaller than (1+ε)x, proving (1). Its density hypotheses hold eventually at p=1/2.

## The deletion model

An algorithm B uses the same inspection and exceptional-query stages. At the end of round t it may remove any subset of its current accepted set C_(t−1), and may add the current vertex v_t. Thus

\[
C_0=\varnothing,\qquad
C_t\subseteq C_{t-1}\cup\{v_t\},
\]

and C_t must be a clique. A previously inspected vertex outside C_(t−1) cannot be admitted in round t. In particular, rejected or deleted vertices are never admitted later. The internal state may retain the entire transcript and all earlier accept/reject/delete decisions. Let

\[
J=C_n,\qquad E_B=\bigcup_{t=1}^n S_t,\qquad
D=\{t:v_t\text{ was admitted at round }t\text{ and }v_t\notin J\}.
\]

The deletion count is |D|: every admitted vertex absent from J must have been deleted, and each vertex is admitted at most once. The final update may also delete the just admitted current vertex; it then belongs to D. This convention does not change the argument.

## Proposition: the cost of allowing deletions

For 0≤r≤n an integer, set

\[
M(n,r)=\sum_{j=0}^r\binom nj.
\]

For every B in the deletion model, for all sufficiently large n depending only on ε,

\[
\Pr\left\{|J|\ge(1+\varepsilon)x,\quad
             |E_B\cap P(J)|\le q,\quad |D|\le r\right\}
\le \min\{1,M(n,r)2^{-\xi L^2}\}.                              \tag{2}
\]

The query and deletion conditions in (2) need hold only on the event being bounded. In particular, if they hold on every execution, (2) bounds the algorithm's success probability.

### Proof

Fix any deterministic set T⊆[n], |T|≤r. Construct an irrevocable algorithm A_T with the same random seed as B. It keeps a private simulation of B and a separate irrevocable output K, initially empty. The simulated state of B is never replaced by K.

Until the simulation is stopped, its round t proceeds as follows.

1. Select the vertex v_t chosen by the simulated B. Receive its ordinary adjacencies to all previously inspected vertices and pass these answers to the simulation. This uses exactly the permitted inspection stage.

2. Compute the exceptional query set S_t chosen by the simulated B, before obtaining its answers. Let F be the union of exceptional sets already queried by A_T. If

   \[
   |(F\cup S_t)\cap P(K)|>q,
   \]

   stop the simulation before querying S_t. In this and all remaining rounds, query no exceptional pairs and accept no vertex. Complete the remaining vertex inspections in increasing label order.

3. Otherwise query S_t, replace F by F∪S_t, and pass the answers to the simulation. Complete B's decision stage, including its deletions. If B does not retain v_t at the end of this round, or if t∈T, leave K unchanged.

4. In the remaining case, add v_t to K if both

   \[
   K\cup\{v_t\}\text{ is a clique},\qquad
   |F\cap P(K\cup\{v_t\})|\le q.                              \tag{3}
   \]

   If either test fails, reject v_t in the output K but continue the private simulation of B.

Every test is measurable from permitted information. In particular, K consists of previously inspected vertices, so all adjacencies needed for its clique test were revealed at stage 1. The query-budget test in stage 2 uses only the labels of pairs in S_t, not their unrevealed answers. Simulation of B requires no additional graph access.

The output of A_T is irrevocable and is always a clique. Its exceptional-pair budget holds on every execution, even when T is a wrong guess. To verify this, induct on the round. Stage 1 adds no exceptional pairs and changes no output vertex. Stage 2 prevents the exceptional union from exceeding q on the current K. Stage 4 checks the budget before increasing K. Once stopped, F and K never change. Thus

\[
|E_{A_T}\cap P(A_T(H))|\le q.
\]

Consequently (1) applies to each A_T.

Now fix a graph and seed on the event in (2), and take T=D for this execution. This choice is used only to identify a member of the fixed family of algorithms {A_T}; no A_T obtains future information.

We prove by induction that the simulation never stops, its transcript equals B's transcript, and after each round

\[
K=J\cap\{v_1,\ldots,v_t\}.                                  \tag{4}
\]

The claim holds initially. Suppose it holds through round t−1. The simulated B has the same seed and transcript as B and therefore chooses the same v_t and S_t. Before the query, K⊆J and F∪S_t⊆E_B. Hence

\[
|(F\cup S_t)\cap P(K)|\le |E_B\cap P(J)|\le q,
\]

so stage 2 cannot stop the simulation. All query answers and B's decision in the round agree.

If v_t∈J, then B admits it now and retains it at the end of the round, because later admission is prohibited. Also t∉D. Both tests (3) pass: K∪{v_t}⊆J is a clique and F⊆E_B. Thus A_D adds v_t.

If v_t∉J, then either B does not retain v_t at the end of its inspection round, in which case A_D rejects it at stage 3, or it retains v_t at that round and deletes it later, in which case t∈D and A_D again rejects it. This proves (4). Deletions of other vertices affect only the simulation, since (4) contains only vertices of J.

At t=n, (4) gives A_D(H)=J. It follows pointwise that the event in (2) is contained in

\[
\bigcup_{T\subseteq[n],\ |T|\le r}
\{|A_T(H)|\ge(1+\varepsilon)x\}.
\]

The family contains exactly M(n,r) sets T. Apply the union bound and (1); cap the result at 1. This proves (2). ∎

## Consequences

For all 0≤r≤n,

\[
M(n,r)\le(r+1)n^r,
\]

because binom(n,j)≤n^j≤n^r for each 0≤j≤r. Thus the base-two logarithm of the right-hand side of (2), before capping at 1, is at most

\[
-\xi(x-1)^2+rx+\log_2(r+1).                                  \tag{5}
\]

If r=o(x), then rx=o(x²), log₂(r+1)=o(x²), and (5) is

\[
-(\xi-o(1))x^2.
\]

More generally, if r≤a x for a fixed 0≤a<ξ, then (5) is at most

\[
-(\xi-a)x^2+2\xi x-\xi+\log_2(a x+1)
=-(\xi-a-o(1))x^2.                                          \tag{6}
\]

In particular, algorithms with at most

\[
\left\lfloor\frac{\min\{\varepsilon^2,1\}}{128}\log_2 n\right\rfloor
\]

deleted vertices and at most q exceptional pairs inside the final output have success probability at most

\[
2^{-(\xi/2-o(1))(\log_2 n)^2}.
\]

This extends the cited irrevocable model to a positive constant times log n deletions. It imposes no bound on computation time. It does not permit the later admission of an earlier rejected or deleted vertex. If that restriction is removed and no other restriction is imposed, an algorithm can reject every vertex during inspection and choose a maximum clique after the full graph is revealed, using no exceptional queries. Such an algorithm is outside the proposition.

## A second derivation of the multiplicative loss

Independently of the graph and B's seed, choose T uniformly from the M(n,r) subsets of [n] of size at most r, and run A_T. This is one randomized irrevocable, q-restricted algorithm. Conditional on any graph and seed in the event of (2), its probability of choosing T=D is exactly 1/M(n,r). The induction above then gives success. Hence

\[
\Pr(A_T\text{ succeeds})\ge\Pr(\text{event in (2)})/M(n,r).
\]

Applying (1) recovers (2). This derivation does not assume that T=D is independent of B's trajectory. The same logarithmic exponent follows in natural units from

\[
\ln M(n,r)-\xi\ln(2)(x-1)^2
\le\ln(r+1)+r\ln n-\xi\frac{[\ln(n/2)]^2}{\ln2}.
\]

