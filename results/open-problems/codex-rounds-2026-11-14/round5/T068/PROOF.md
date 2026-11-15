# Guessing only inspection-time positive decisions

All logarithms are to base two. Let pairs(U) denote the unordered pairs of distinct vertices in U, and put x=log₂n and L=x−1.

## External theorem and model

David Gamarnik, Eren C. Kızıldağ and Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1, condition (1), and Theorem 2.2, imply the following clique statement. For every fixed η>0, set

\[
c=\frac{\min\{\eta^2,1\}}8,\qquad
\xi=\frac{\min\{\eta^2,1\}}{64},\qquad q=cL^2.
\]

For all sufficiently large n, any irrevocable online clique algorithm A satisfying

\[
|F\cap\operatorname{pairs}(A(H))|\le q
\quad\text{on every execution}
\]

has

\[
\Pr\{|A(H)|\ge(1+\eta)L\}\le 2^{-\xi L^2},
\qquad H\sim G(n,1/2).                                  \tag{1}
\]

Here each round selects an uninspected vertex v_t, reveals its adjacencies to the earlier inspected vertices, selects an exceptional pair set S_t using the information then available, receives its answers, and irrevocably accepts or rejects v_t. The union F comprises every requested S_t, even if some answers were already known. Independent randomness is allowed, with no computation-time bound.

Indeed, complement the graph and reverse every query answer. Independent fair edge indicators remain independent fair indicators; queries, inspection order, and output size are preserved, while cliques become independent sets. The source theorem has scale log₂(n/2)=L and bound (n/2)^(−ξL)=2^(−ξL²). Its density range d/n≤p≤1−n^(−1/d) includes p=1/2 once n≥max{2d,2^d}. Its OGP theorem is an external input.

Let B use those same information stages, but after each round allow any clique C_t among V_t={v₁,…,v_t} as its current state. Set C₀=∅. All its choices use only its revealed transcript and independent seed. Arbitrary deletion, late admission, and readmission are allowed. Define

\[
J=C_n,\quad E=\bigcup_{t=1}^n S_t,\quad
P=\{v_t:v_t\in C_t\},\quad J_0=J\cap P,
\]
\[
D=\{t:v_t\in C_t,\ v_t\notin J\},\qquad R=J\setminus P.
\]

Membership in P records the decision at each vertex's own inspection round. Thus |J₀|=|J|−|R|, and |D| counts inspection-time positive decisions absent from J. Temporary changes do not themselves contribute to either count.

## The improved reduction

**Theorem.** Fix η>0. For all sufficiently large n, every integer k≥ceil((1+η)L) with k≥1, every integer 0≤r≤n, and every B as above,

\[
\begin{split}
\Pr\{\,|J_0|\ge k,\ |D|\le r,\ 
 |E\cap\operatorname{pairs}(J)|\le q\,\}
\le \min\left\{1,\binom{k+r}{r}2^{-\xi L^2}\right\}.       \tag{2}
\end{split}
\]

If k>n the event is empty, so it suffices to prove the result for k≤n.

### A fixed family of advice words

Let W(k,r) be the binary words with exactly k ones, at most r zeros, and last symbol one. A one means to attempt accepting the current inspection-time positive vertex; a zero means to skip it. No symbol is consumed at an inspection-time negative decision.

For a word with d zeros, deleting the final one leaves k−1 ones and d zeros, hence binom(k+d−1,d) possibilities. Therefore

\[
|W(k,r)|=\sum_{d=0}^r\binom{k+d-1}{d}
        =\binom{k+r}{r}.                                  \tag{3}
\]

For completeness, the sum identity follows by induction on r: it is 1 at r=0, and the increment binom(k+r−1,r) added to binom(k+r−1,r−1) gives binom(k+r,r). A second count distributes the zeros among the k gaps before the successive ones. These gap sizes form a nonnegative k-tuple with sum at most r. Adding a slack coordinate gives a nonnegative (k+1)-tuple with sum r. In the stars-and-bars bijection, choosing the k separator positions among k+r positions gives binom(k+r,k), which equals (3).

### A guarded irrevocable algorithm for every word

Fix w∈W(k,r) before seeing the graph or seed. Algorithm A_w keeps a private simulation of B with the same seed, a separate irrevocable clique K=∅, an exceptional union F=∅, and a pointer to the next symbol of w. While active, round t is:

1. Select B's prescribed v_t, receive its ordinary inspection answers, and pass them to the private simulation.
2. Compute B's requested S_t without obtaining its answers. If |(F∪S_t)∩pairs(K)|>q, deactivate before making this request and reject v_t. Otherwise request S_t, update F←F∪S_t, pass its answers to B, and complete B's update to C_t.
3. If v_t∉C_t, reject v_t and consume no symbol. If v_t∈C_t, consume the next symbol. For zero, reject v_t. For one, accept v_t precisely when K∪{v_t} is a clique and |F∩pairs(K∪{v_t})|≤q; otherwise reject it.
4. If the final symbol has been consumed, deactivate immediately, whether or not its acceptance test passed.

After deactivation, finish the remaining ordinary inspections in increasing label order, with no exceptional requests and no acceptances. In step 2, deactivation also means the rest of that round has no exceptional requests or acceptance. The private simulation need not continue after deactivation.

Every choice is legal online. The next word symbol is fixed in advance and its pointer depends only on completed simulated decisions. Each pair between K and v_t is known after ordinary inspection. The pre-query guard counts labeled pairs before obtaining any new answers. Updating B's current clique is private computation using its permitted transcript.

Every A_w satisfies the hypotheses of (1), including wrong words. The clique test ensures that K remains a clique. The pre-query guard preserves |F∩pairs(K)|≤q when F grows; the acceptance-budget guard preserves it when K grows. Afterwards both sets are fixed. Thus (1) applies to every A_w, without any condition on B's eventual output or budget.

### The correct word

Fix a graph and B-seed in the event in (2). Let τ be the inspection round of the kth vertex of J₀ in inspection order, and let Q be those first k vertices of J₀. Read B's inspection-time positive decisions up to and including τ, writing one for a vertex in J and zero for a vertex outside J. Call the resulting word w*. Its ones are exactly the vertices in Q. It has k ones, its last symbol is one, and its number d of zeros is at most |D|≤r. Thus w* belongs to the fixed family W(k,r).

The use of the final output to identify w* is only an event-covering argument. Each A_w was defined independently of that output.

Induct on rounds t≤τ. Until round τ completes, A_(w*) has B's exact simulated transcript and

\[
K_t=Q\cap V_t.                                           \tag{4}
\]

This holds at t=0. Assume it through t−1. The private simulation chooses the same v_t and S_t as B. Since K⊆Q⊆J and F∪S_t⊆E,

\[
|(F\cup S_t)\cap\operatorname{pairs}(K)|
\le |E\cap\operatorname{pairs}(J)|\le q.
\]

The pre-query guard passes, and B receives the same answers and makes the same update. If v_t∉C_t, then v_t∉P and hence v_t∉Q; no symbol or vertex is added. If v_t∈C_t and v_t∉J, the next word symbol is zero and it is skipped. If v_t∈C_t and v_t∈J, then v_t∈J₀ and, because t≤τ, v_t∈Q. The next word symbol is one. The proposed output is a subset of J and hence is a clique with permitted exceptional-pair count. Both acceptance tests pass, establishing (4).

Before τ the word cannot be exhausted, since its final one corresponds to the kth core vertex. At round τ it is exhausted and K=Q has size k. A_(w*) deactivates at that point. Exceptional requests that B makes later are never made by A_(w*), so they cannot invalidate its output budget. Consequently A_(w*)(H) has size k.

The event in (2) is therefore contained in

\[
\bigcup_{w\in W(k,r)}\{|A_w(H)|\ge k\}.
\]

Since k≥(1+η)L, (1), (3), and the union bound prove (2). No conditioning of the graph distribution on the realized word is used. ∎

In fact the proof only needs at most r inspection-time positives outside J before τ. The total |D| condition is a convenient stronger hypothesis. No assumption on the structure of the possible D sets was imposed.

## Polynomial deletion-disagreement budgets

Fix ε>0 and 0≤β<ε, put η=ε−β, and retain the corresponding c and ξ. For x=log₂n, let

\[
k=\lceil(1+\eta)(x-1)\rceil.
\]

If |J|≥(1+ε)x and |R|≤βx, then

\[
|J_0|=|J|-|R|\ge(1+\eta)x\ge k.
\]

For the last inequality, ceil(y)≤y+1 applied to y=(1+η)(x−1) gives k≤(1+η)x−η<(1+η)x. Thus (2) bounds the Karp target event with these R and D caps and exceptional budget q.

If a>0 is fixed and r≤n^a, then

\[
\log_2\binom{k+r}{r}
=\log_2\binom{k+r}{k}
\le k\log_2\frac{e(k+r)}{k}
\le a(1+\eta)x^2+o(x^2).                                \tag{5}
\]

Here binom(k+r,k)≤(k+r)^k/k!, and
ln(k!)=Σ_{j=1}^k ln j≥∫₁^k ln t\,dt=k ln k−k+1≥k ln k−k,
so k!≥(k/e)^k. Since k=(1+η)x+O(1) and k/n^a→0, log₂(k+r)≤ax+o(1), which yields (5). If a=0, the integer r is at most one and the cost is at most log₂(k+1)=o(x²). In either case, for fixed

\[
0\le a<\frac{\xi}{1+\eta},
\]

the probability of

\[
|J|\ge(1+\varepsilon)x,\quad |R|\le\beta x,\quad
|D|\le\lfloor n^a\rfloor,\quad
|E\cap\operatorname{pairs}(J)|\le c(x-1)^2
\]

is at most

\[
2^{-\left(\xi-a(1+\eta)-o(1)\right)x^2}.                 \tag{6}
\]

The allowed a is always less than one: ξ≤1/64 and 1+η>1. Thus floor(n^a)≤n as required.

For an explicit choice set β=ε/2, h=min{ε²/4,1}, and

\[
a=\frac{h}{128(1+\varepsilon/2)}.
\]

The caps

\[
|R|\le\lfloor\varepsilon x/2\rfloor,\quad
|D|\le\lfloor n^a\rfloor,\quad
|E\cap\operatorname{pairs}(J)|\le h(x-1)^2/8
\]

give success probability at most 2^(−(h/128−o(1))x²). The previous round had the same exponent with |D|≤floor(hx/128). The new bound permits a positive power of n, while retaining its late-admission and exceptional-query restrictions.

Also, for r=O(x), the new factor has logarithm O(x), rather than the earlier O(x²) estimate: k+r=O(x), and binom(k+r,r)≤2^(k+r). For r polynomial in x the logarithm is O(x log x)=o(x²).

## Independent randomized derivation of the exponent

As a separate argument, use the same private simulation and guards, but independently keep each inspection-time positive with probability p∈(0,1), and deactivate as soon as K reaches k. Fix a graph and B-seed in the event in (2). Up to τ there are k core positives and d≤r other positives. The coin event that keeps the former and skips the latter has probability p^k(1−p)^d≥p^k(1−p)^r. On this event the same induction as (4) proves that all guards pass up to τ and K reaches k. This argument fixes the unguarded B trajectory first; it does not assume that a wrong coin history preserves B's transcript.

Applying (1) to this single randomized algorithm gives

\[
\Pr\{\text{event in (2)}\}
\le p^{-k}(1-p)^{-r}2^{-\xi L^2}.                         \tag{7}
\]

For r>0, the natural logarithm of this factor is −k ln p−r ln(1−p). Its derivative is −k/p+r/(1−p), which vanishes at p=k/(k+r); its second derivative k/p²+r/(1−p)² is positive. This choice therefore minimizes the factor and gives logarithmic cost

\[
k\log_2(1+r/k)+r\log_2(1+k/r).                           \tag{8}
\]

The second term is at most k/ln 2 because ln(1+u)≤u. The first is at most k log₂(k+r), so for r≤n^a, (8) is at most a(1+η)x²+o(x²), independently recovering the coefficient in (6). For r=0 use p=1, with no loss. This route gives a slightly larger finite factor than (3); it is an independent check of the asymptotic budget and exponent.

## Scope

All bounds are joint-event bounds. B need not satisfy the disagreement or query caps on other executions. Wrong words and wrong coin histories are controlled by the guards. Early stopping is essential to the count in (3): there is no requirement to predict positive decisions after the kth final-core vertex. The reduction does not preserve B's complete transcript after that stopping round.

No late-admission loss has been removed. If B rejects every vertex until its final update and then chooses a maximum clique, E=∅ and D=∅, but |J₀|≤1. Such an algorithm does not meet the large-core event or the stated R cap. The unrestricted polynomial-time problem remains open. No priority claim is made beyond the improvement over the three preceding reports.
