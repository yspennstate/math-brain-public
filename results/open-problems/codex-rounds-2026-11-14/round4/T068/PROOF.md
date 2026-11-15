# An online clique barrier with late admissions and readmissions

All logarithms are to base two. Write pairs(U) for the unordered pairs of distinct elements of U, and put x=log₂n and L=x−1.

## External theorem

David Gamarnik, Eren C. Kızıldağ and Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1, condition (1), and Theorem 2.2, give the following consequence. Fix η>0 and define

\[
c_\eta=\frac{\min\{\eta^2,1\}}8,\qquad
\xi_\eta=\frac{\min\{\eta^2,1\}}{64},\qquad q=c_\eta L^2.
\]

For sufficiently large n, every irrevocable online clique algorithm A on H∼G(n,1/2) with exceptional query union F satisfying

\[
|F\cap\operatorname{pairs}(A(H))|\le q
\]

on every execution obeys

\[
\Pr\{|A(H)|\ge(1+\eta)L\}\le2^{-\xi_\eta L^2}.       \tag{1}
\]

Here a round selects an uninspected vertex, reveals its pairs with all earlier inspected vertices, selects one exceptional query set based on available information, receives its answers, and irrevocably accepts or rejects the selected vertex. An independent random seed is allowed. There is no running-time bound.

To obtain (1), complement H and reverse each answer. Independent fair edge indicators remain independent fair indicators, the adaptive inspection order and exceptional pair sets agree, and cliques become independent sets. The theorem's scale is log₂(n/2)=L and its bound is (n/2)^(−ξ_η L)=2^(−ξ_η L²). Its density range contains 1/2 for sufficiently large n. The cited OGP theorem is used as an external result.

## Revision model and counts

An algorithm B uses the same inspection and exceptional-query stages. Let v_t be its inspected vertex in round t and V_t={v_1,…,v_t}. After the answers in that round, B may replace its current clique by any clique C_t⊆V_t. Set C_0=∅. Rejection followed by later admission, and deletion followed by readmission, are allowed, with no bound on the number of intermediate changes. At round n the update may use the entire revealed graph. All choices use only the revealed information and B's independent seed.

Define

\[
J=C_n,\quad E=\bigcup_{t=1}^n S_t,\quad
P=\{v_t:v_t\in C_t\},\quad
D=\{t:v_t\in C_t\text{ and }v_t\notin J\},\quad
R=J\setminus P.
\]

Thus P records the single decision made about each vertex at the end of its own inspection round. D records such accepted vertices absent from the final output, using their inspection rounds. R records final vertices absent immediately after their own inspection rounds. A vertex accepted at inspection, deleted, and readmitted before the end belongs to neither D nor R. A vertex rejected at inspection, admitted later, and eventually removed also belongs to neither. These counts concern disagreement with final membership, not the total number of changes.

Put J₀=J∩P. Then

\[
|J_0|=|J|-|R|.                                            \tag{2}
\]

## Theorem

For every fixed η>0, all sufficiently large n depending only on η, every B in the revision model, and every integer 0≤r≤n,

\[
\begin{split}
\Pr\{&|J|-|R|\ge(1+\eta)L,\quad |D|\le r,\quad
                |E\cap\operatorname{pairs}(J)|\le c_\eta L^2\}\\
&\le\min\{1,M(n,r)2^{-\xi_\eta L^2}\},\qquad
M(n,r)=\sum_{j=0}^r\binom nj.                              \tag{3}
\end{split}
\]

The conditions on D, R, and the exceptional queries need hold only on the event in (3).

### Proof

For each fixed T⊆[n] with |T|≤r, construct an irrevocable online algorithm A_T. It keeps a private simulation of B with the same seed, a separate output clique K initially empty, and its own exceptional-query union F initially empty. The private state of B includes its current clique and its full transcript. It is never replaced by K.

While the simulation is running, perform round t as follows.

1. Select the vertex v_t prescribed by the private simulation and receive its ordinary inspection answers. Pass those answers to the simulation.

2. Compute B's requested exceptional set S_t, without querying its answers yet. If |(F∪S_t)∩pairs(K)|>q, stop the simulation before making those queries. Reject this vertex and all subsequent vertices, make no more exceptional queries, and finish ordinary inspections in increasing label order.

3. Otherwise query S_t, set F←F∪S_t, and pass the answers to the simulation. Let B complete its update to C_t, including any admissions and deletions of old vertices.

4. If v_t∉C_t or t∈T, reject v_t in K. Otherwise accept v_t into K precisely when K∪{v_t} is a clique and |F∩pairs(K∪{v_t})|≤q. If either test fails, reject v_t in K and continue the private simulation.

All steps obey the information restriction. The new exceptional set is known before its answers, so step 2 only counts labeled pairs. Every pair between v_t and K was revealed by the ordinary inspection stage, so step 4 has the information needed for its clique test. Updates involving old vertices require no additional graph queries: they are part of B's computation from the permitted transcript.

For every T and every input and seed, K is an irrevocable clique. Its exceptional-pair budget is maintained inductively. Ordinary inspection does not change F. Step 2 checks the budget before F grows. Step 4 checks it before K grows. After stopping, both remain fixed. Therefore |F∩pairs(K)|≤q at the end on every execution. In particular (1) applies to each A_T, including every wrong guess.

Fix a graph and seed in the event on the left of (3). Select the member of this fixed family with T=D. This selection is only used to prove an event inclusion, not supplied as future information to any algorithm.

Induct on t to prove that the simulation never stops, has exactly B's transcript, and satisfies

\[
K_t=J_0\cap V_t.                                         \tag{4}
\]

The assertion holds at t=0. Suppose it holds at t−1. Equal seeds and transcripts give the same inspection vertex and query request as B. Before querying, K⊆J₀⊆J and F∪S_t⊆E, so

\[
|(F\cup S_t)\cap\operatorname{pairs}(K)|
\le |E\cap\operatorname{pairs}(J)|\le q.
\]

Step 2 does not stop. All answers and the simulated update C_t therefore agree with B.

If v_t∈J₀, then v_t∈P, so v_t∈C_t by the definition of P at its inspection round. Also t∉D. Since K∪{v_t}⊆J, both tests in step 4 pass. Hence v_t is added.

If v_t∉J₀ and v_t∉C_t, it is rejected in step 4. In the remaining case v_t∉J₀ and v_t∈C_t. This places v_t in P; because it is outside J∩P, it lies outside J. Thus t∈D and is again rejected. These cases exhaust all possibilities and prove (4).

Late changes to old vertices affect only B's private state. They do not affect (4), even when an old vertex in J₀ temporarily disappears from C_t. The output K is a subset of the fixed final clique J, which is exactly what its guards require.

At t=n, (4) gives A_D(H)=J₀. By (2), the event in (3) is contained in

\[
\bigcup_{T\subseteq[n],\ |T|\le r}
\{|A_T(H)|\ge(1+\eta)L\}.
\]

There are M(n,r) fixed sets T. Applying (1) to each and taking the union bound proves (3), after capping the result at 1. ∎

## Consequence at the Karp target

Fix ε>0 and 0≤β<ε, and set η=ε−β. Let r,s be nonnegative integers with r≤n and s≤βx. On the event

\[
|J|\ge(1+\varepsilon)x,\qquad |R|\le s,
\]

equation (2) gives

\[
|J_0|\ge(1+\varepsilon)x-s
\ge(1+\varepsilon-\beta)x=(1+\eta)x\ge(1+\eta)L.
\]

Thus (3) bounds the probability of this event together with |D|≤r and |E∩pairs(J)|≤c_η L². No factor for guessing R is needed.

Since binom(n,j)≤n^j≤n^r for 0≤j≤r and n≥1,

\[
M(n,r)\le(r+1)n^r.
\]

For any fixed 0≤a<ξ_η and r≤ax, the logarithm of the uncapped bound is at most

\[
\begin{split}
-\xi_\eta(x-1)^2+rx+\log_2(r+1)
&\le-(\xi_\eta-a)x^2+2\xi_\eta x-\xi_\eta
       +\log_2(ax+1)\\
&=-(\xi_\eta-a-o(1))x^2.                                  \tag{5}
\end{split}
\]

In particular, with β=ε/2 and h=min{ε²/4,1}, the three caps

\[
|R|\le\lfloor\varepsilon x/2\rfloor,\qquad
|D|\le\lfloor h x/128\rfloor,\qquad
|E\cap\operatorname{pairs}(J)|\le hL^2/8
\]

give

\[
\Pr\{|J|\ge(1+\varepsilon)x\text{ and these caps hold}\}
\le2^{-(h/128-o(1))x^2}.                                  \tag{6}
\]

For β=0 and no late admissions, P contains every finally retained vertex; D is the earlier deletion count when readmission is disallowed. This recovers the prior result. More generally the theorem allows arbitrary numbers of temporary deletions and late admissions, provided its final disagreement counts meet the caps.

## Checks on the loss and its scope

As a second derivation, choose T uniformly from the M(n,r) allowed sets, independently of H and B's seed, and run A_T. On any graph and seed in (3), the chance of selecting its D is 1/M(n,r), and then A_T outputs J₀. Applying (1) to this one randomized algorithm again gives (3). There is no conditioning of the graph distribution on the realized set D.

The natural-log exponent is also

\[
\ln M(n,r)-\xi_\eta\frac{[\ln(n/2)]^2}{\ln2},
\]

which equals ln(2) times the base-two exponent in (5) before its estimates.

The size loss cannot simply be omitted from this reduction: after rejecting every inspected vertex until the final update, B may select a maximum clique from the fully revealed graph, with E=∅ and D=∅. Its on-inspection core contains at most v_n, and nearly all of its output lies in R. Equation (3) controls that core, not its unrestricted final size. This example explains why a restriction on R is essential for the corollary, without asserting optimality of the constants.

The unrestricted polynomial-time clique problem remains outside the theorem. No claim of priority for this reduction in the wider literature is made.
