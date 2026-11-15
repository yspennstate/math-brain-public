# A sharper clique barrier from charging previously exposed edges

All logarithms are to base two. Write pairs(U) for the unordered pairs of distinct elements of U.

## Model and result

Let H have distribution G(n,1/2). In round t an algorithm B chooses an uninspected vertex v_t using its independent seed and the information already revealed. It learns all pairs between v_t and the previously inspected set V_{t-1}. Based on that information it selects an exceptional pair set S_t, receives its answers, and then chooses a clique C_t contained in V_t=V_{t-1} union {v_t}. Initially C_0 is empty. Arbitrary changes to membership of previously inspected vertices are allowed; there is no computation-time restriction. Set E=union_t S_t, counting the requested pairs even when already known.

Define

\[
J=C_n,\qquad P=\{v_t:v_t\in C_t\},\qquad
J_0=J\cap P,\qquad R=J\setminus P,\qquad D=P\setminus J.
\]

Thus |J_0|=|J|-|R|. The cardinality |D| agrees with the deletion-round count in round 5, since every vertex has exactly one inspection round. These counts concern final disagreements, rather than the number of temporary revisions.

For integers 1<=k<=n, 0<=s<k, and real q>=0, put ell=k-s and

\[
U_q(n,k,s)=\min\left\{1,\binom n\ell
             2^{q-s\ell-\binom\ell2}\right\}.
\tag{1}
\]

**Theorem.** For every B in this model and integer r>=0,

\[
\Pr\{|J_0|\ge k,\ |D|\le r,\ |E\cap\operatorname{pairs}(J)|\le q\}
\le \min\left\{1,\binom{k+r}{k}\,U_q(n,k,s)\right\}.
\tag{2}
\]

One may minimize the right side over s. If k>n the event is empty.

Consequently, for every fixed eta>0 and 0<=c<eta^2/2, x=log n, and

\[
k=\lceil(1+\eta)x\rceil,\qquad
 a_* =\frac{\eta^2/2-c}{1+\eta},
\]

any fixed 0<=a<a_* and r<=n^a satisfy

\[
\Pr\{|J_0|\ge(1+\eta)x,\ |D|\le r,
             |E\cap\operatorname{pairs}(J)|\le cx^2\}
\le 2^{-\left(\eta^2/2-c-a(1+\eta)-o(1)\right)x^2}.
\tag{3}
\]

The endpoint also gives a vanishing bound: for r<=floor(n^{a_*}),

\[
\Pr\{|J_0|\ge(1+\eta)x,\ |D|\le r,
             |E\cap\operatorname{pairs}(J)|\le cx^2\}
\le 2^{-(1+2\eta)x\log x+O(x)}.
\tag{4}
\]

All constants implicit here may depend on eta and a, but not on B. Only the interesting range r<=n need be used; allowing larger r in (2) is harmless.

All three caps are event-level conditions; B need not satisfy them on its other executions. In particular c=0 permits arbitrary exceptional queries outside the final clique, not just the absence of exceptional queries. Section 5 separately studies the genuinely no-query case to audit the source coefficient.

## 1. Fresh edges under adaptive inspection

Include the independent seed in the initial history. At each round, condition on the preceding history, which specifies the inspected vertices and every edge revealed so far, either ordinarily or exceptionally. Every unrevealed edge remains an independent fair bit.

This assertion follows inductively. Initially it is the product law of H and independence of the seed. Given a history, the selected label v_t is fixed. The newly revealed ordinary pairs are a subset of the remaining independent bits. Conditioning on their values leaves all other unrevealed bits independent and fair. The selected exceptional set is then fixed by the enlarged history; revealing its previously unknown bits again preserves the product law on the remaining bits. Decisions and internal computations reveal no additional graph bits. This proves the assertion for the next history. For randomized policies, one may condition on the seed and then average.

For an irrevocable online clique algorithm A, let K_t be its retained set, M_t=|K_t|, and F_t its exceptional-query union. Just after selecting v_t but before its ordinary row is exposed, define

\[
B_t=F_{t-1}\cap\{\{v_t,u\}:u\in K_{t-1}\},\qquad b_t=|B_t|.
\]

Both are determined by the preceding history and selected label. Since v_t is uninspected, a known pair between v_t and K_{t-1} must have been exceptionally exposed. Exactly M_{t-1}-b_t such pairs remain fresh fair bits. If any known pair is a nonedge, compatibility is impossible. Otherwise it has conditional probability 2^{-(M_{t-1}-b_t)}. The subsequent exceptional queries and decision can only restrict acceptance further. Thus

\[
\mathbb E\left[
 \mathbf1_{\{M_t=M_{t-1}+1\}}2^{-b_t}
 \mid\text{preceding history}\right]
\le 2^{-M_{t-1}}.
\tag{5}
\]

The preceding history includes the selected label, which is measurable from the past and seed. This inequality remains true if A uses all previously exposed future information when choosing that label.

## 2. An elementary finite tail bound

For an irrevocable A let tau_s be its first time with M_t=s, with tau_0=0. Conditional on any history at a finite tau_s, let N=n-tau_s be the number of inspections remaining.

For fixed 1<=u_1<...<u_ell<=N, let E_i be the event that u_1,...,u_i are the times, measured after tau_s, of its next i acceptances. Write Z_i=sum_{j=1}^i b_{tau_s+u_j}. Immediately before u_i on the event consisting of E_{i-1} and no intervening acceptance, the retained set has size s+i-1. Apply (5) after multiplying by the measurable preceding weight 1_{E_{i-1}}2^{-Z_{i-1}} and the indicator of no intervening acceptance. Dropping that last indicator after conditional expectation only increases the bound, because all weights are nonnegative. Induction gives

\[
\mathbb E[\mathbf1_{E_\ell}2^{-Z_\ell}
          \mid\text{history at tau_s}]
\le \prod_{i=1}^{\ell}2^{-(s+i-1)}
=2^{-s\ell-\binom\ell2}.
\tag{6}
\]

Every pair charged in B_t at an accepted vertex has that vertex as its later-inspected endpoint and an earlier accepted vertex as its other endpoint. Two different acceptances cannot charge the same pair. Since the output is irrevocable, all charged pairs belong to F_n intersect pairs(K_n). Consequently Z_ell<=|F_n intersect pairs(K_n)|. On the event that this final count is at most q, 2^{-Z_ell}>=2^{-q}. Equation (6) therefore bounds the conditional probability of E_ell together with this budget event by 2^{q-s ell-binomial(ell,2)}. This step uses a pointwise bound on the event; it does not condition the product law on a favorable future budget.

If A reaches size k, it reaches s and has these ell additional acceptances for some such tuple. There are binom(N,ell)<=binom(n,ell) tuples, with zero tuples if N<ell. The conditional union bound is uniform in the history at tau_s. Averaging over all finite tau_s, and bounding their total probability by one, proves

\[
\Pr\{|A(H)|\ge k,\ |F_n\cap\operatorname{pairs}(A(H))|\le q\}
\le U_q(n,k,s).
\tag{7}
\]

No asymptotic theorem or overlap-gap result is used in this bound.

## 3. Passing from revisions to an irrevocable output

The round-5 advice-word reduction specializes as follows; its argument is included to specify every use of the information restriction.

Let W(k,r) consist of the binary words with k ones, at most r zeros, and final symbol one. A word with d zeros has binom(k+d-1,d) possible placements of those zeros. Summing over d gives

\[
|W(k,r)|=\sum_{d=0}^r\binom{k+d-1}{d}
        =\binom{k+r}{k}.
\tag{8}
\]

The identity also follows by distributing at most r zeros into the k gaps before successive ones and introducing a slack gap: a nonnegative (k+1)-tuple summing to r has binom(k+r,k) choices.

Fix w in W(k,r) before observing the graph or seed. An algorithm A_w privately simulates B with the same seed. It keeps a separate irrevocable output K, initially empty. In each active round it follows B's inspection choice, obtains exactly B's ordinary row, requests B's same exceptional set and passes back its answers, and simulates its update to C_t. If v_t is absent from C_t, it rejects v_t without consuming a symbol. Otherwise it consumes the next symbol. For zero it rejects v_t. For one it accepts v_t if K union {v_t} is a clique, and otherwise rejects it. When the last symbol is consumed, it stops the private simulation, rejects all later vertices, makes no further exceptional queries, and completes ordinary inspections in increasing label order.

The clique test uses only the ordinary answers, because K consists of previously inspected vertices. Every A_w is consequently a legal irrevocable algorithm, including every wrong word. Failed clique tests still consume their symbols. Equation (7) is a joint-event estimate and imposes no hard budget restriction on A_w, so it applies to all words without either budget guard from round 5. Only the clique guard is needed.

Fix a graph and B-seed in the event in (2). Let tau be the inspection round of the kth vertex of J_0, in inspection order, and Q the first k vertices of J_0. Among B's inspection-time positive decisions through tau, write one for a vertex in J and zero for a vertex outside J. The resulting word w* has k ones, ends in one, and has at most |D| zeros, so it belongs to W(k,r).

Induct over rounds t<=tau. The private transcript of A_{w*} equals B's transcript and its output equals Q intersect V_t. Initially both statements hold. Assuming them before a round, the simulation selects the same vertex, receives the same ordinary and exceptional answers, and makes B's same update. An inspection-time negative vertex is not in P and hence not in Q. A positive vertex outside J consumes zero. A positive vertex in J inspected through tau belongs to Q and consumes one. In the last case K union {v_t} is a subset of the clique J, so its clique test succeeds. These cases prove the induction. The word is exhausted exactly at tau, leaving output Q and exceptional union F contained in E. Hence |F intersect pairs(Q)|<=|E intersect pairs(J)|<=q.

Thus the event in (2) is contained in the union over the fixed family W(k,r) of {|A_w(H)|>=k, |F_w intersect pairs(A_w(H))|<=q}. Equations (7) and (8), followed by the union bound and a cap at one, prove (2). The input distribution is never conditioned on the realized correct word.

As in round 5, the proof only needs at most r positive vertices outside J before tau; later disagreements do not matter. The total |D| cap is a convenient stronger condition.

## 4. The polynomial deletion exponent and its endpoint

Fix eta>0, 0<=c<eta^2/2, write gamma=1+eta, and take k=ceil(gamma x), s=floor(x), ell=k-s, q=cx^2. For sufficiently large n, 0<=s<k<=n. Then

\[
k=\gamma x+O(1),\quad \ell=\eta x+O(1),\quad x-s=O(1).
\]

For every positive integer m, integration of the increasing function log t gives

\[
\log(m!)\ge\int_1^m\log t\,dt
\ge m\log m-(\log e)m.
\tag{9}
\]

Using binom(n,ell)<=n^ell/ell!, (9), and (1),

\[
\begin{aligned}
\log U_q(n,k,s)
&\le q+\ell(x-s)-\frac{\ell(\ell-1)}2-\log(\ell!)\\
&\le -\left(\frac{\eta^2}2-c\right)x^2-\eta x\log x+O(x).
\end{aligned}
\tag{10}
\]

The inequality is valid even if the uncapped expression in (1) exceeds one; for these asymptotic choices it is eventually less than one. The quadratic term follows from ell=eta x+O(1), and ell log ell=eta x log x+O(x).

If a>0 is fixed and r<=n^a, the other factorial in (2) gives

\[
\begin{aligned}
\log\binom{k+r}{k}
&\le k\log(k+n^a)-\log(k!)\\
&\le a\gamma x^2-\gamma x\log x+O(x).
\end{aligned}
\tag{11}
\]

Indeed log(k+n^a)=a x+log(1+k/n^a)=a x+o(1), while k log k=gamma x log x+O(x). These estimates are uniform over r<=n^a. When a=0, r<=1 and the word factor is at most k+1, whose logarithm is O(log x); (3) still follows.

For a>0, adding (10) and (11) yields the more precise upper exponent

\[
\left(a\gamma-\frac{\eta^2}2+c\right)x^2
  -(1+2\eta)x\log x+O(x).
\tag{12}
\]

This proves (3). At a=a_*, the quadratic coefficient vanishes and (12) proves (4). In particular the endpoint cannot be dismissed merely because a coarse leading-order estimate vanishes there.

For the original target, fix epsilon>0 and 0<=beta<epsilon and put eta=epsilon-beta. The event

\[
|J|\ge(1+\varepsilon)x,\qquad |R|\le\beta x
\]

implies |J_0|>= (1+eta)x, so (3) and (4) apply with the same disagreement cap. With no final late admissions, beta=0 and eta=epsilon.

For example, epsilon=1/2 and beta=0 permit the same exceptional allowance as round 5, q=(x-1)^2/32, together with |D|<=floor(n^{1/16}), with bound

\[
2^{-2x\log x+O(x)}.
\tag{13}
\]

Indeed the smaller preceding cap is at most x^2/32, and (eta^2/2-1/32)/(1+eta)=1/16. Alternatively choose a=1/32 to retain quadratic exponent 3/64. Round 5 allowed only a<1/384 at this eta. Thus the critical power increases by a factor 24 while keeping its exceptional allowance, and the endpoint is included.

More generally the preceding allowance q=min{eta^2,1}(x-1)^2/8 is covered by c=min{eta^2,1}/8. Its new critical power is (eta^2/2-c)/(1+eta). For 0<eta<=1 this is 3eta^2/[8(1+eta)], compared with the preceding min{eta^2,1}/[64(1+eta)], a factor 24. When c=0 the critical power is eta^2/[2(1+eta)]; eta=1/2 gives 1/12 and the same endpoint bound (13). This zero-budget case allows exceptional queries outside J as well.

## 5. Sharpness of the irrevocable quadratic coefficient

This section checks the coefficient eta^2/2 independently. It does not establish that a_* is an optimal disagreement exponent.

Here assume genuinely no exceptional queries. Then b_t=0 in (5), and greedy at size j has compatibility probability p_j=2^{-j}, constant conditional on every earlier history at size j. Therefore its size process has the pure-birth transition j to j+1 with probability p_j. Equivalently its time T_k to size k has the law

\[
T_k=\sum_{j=0}^{k-1}G_j,
\tag{14}
\]

where the G_j are independent geometric variables on {1,2,...} with success probabilities p_j. This representation concerns the pure-birth chain; it can be extended beyond n abstractly and then restricted to its first n steps.

Set m=floor(n/k), eventually at least one. The event G_j<=m for every j implies T_k<=km<=n. For p in [0,1] and integer m>=1,

\[
1-(1-p)^m\ge \frac{mp}{1+mp}
             \ge\tfrac12\min\{mp,1\}.
\tag{15}
\]

For 0<=p<1 the first inequality follows from (1-p)^{-m}>=(1+p)^m>=1+mp; p=1 follows directly. Independence in (14) gives

\[
\log\Pr\{T_k\le n\}
\ge -k-\sum_{j=0}^{k-1}(j-\log m)_+.
\tag{16}
\]

Here m=(n/k)(1+O(k/n)), so log m=x-log x-log gamma+o(1). Put y=log m, b=floor(y), and d=k-1-b, which is positive for sufficiently large n. The sum in (16) is exactly

\[
d(b+1-y)+\frac{d(d-1)}2
=\frac{(k-y)^2}{2}+O(k-y+1).
\]

Since k-y=eta x+log x+O(1) and (log x)^2=O(x), the right side of (16) is

\[
-\frac{\eta^2}2x^2-\eta x\log x+O(x).
\tag{17}
\]

Together with (10) at c=0, this proves the sharper identity

\[
\log\Pr\{\text{greedy size}\ge k\}
=-\frac{\eta^2}{2}x^2-\eta x\log x+O(x),
\]

and in particular

\[
\lim_{n\to\infty}
\frac{\log\Pr\{\text{greedy size}\ge\lceil(1+\eta)\log n\rceil\}}
     {(\log n)^2}
=-\eta^2/2.
\tag{18}
\]

For completeness, greedy also maximizes this finite tail among irrevocable algorithms with genuinely no exceptional queries. Let f_h(j)=Pr(G_j+...+G_{k-1}<=h) for j<k and f_h(k)=1. Removing the first positive summand shows f_h(j+1)>=f_h(j), and the first transition gives

\[
f_h(j)=(1-p_j)f_{h-1}(j)+p_j f_{h-1}(j+1).
\tag{19}
\]

Induct on h. Given such an algorithm's full history at size j, its acceptance probability alpha is at most p_j by (5) with b_t=0. The induction hypothesis bounds continuation after rejection by f_{h-1}(j) and after acceptance by f_{h-1}(j+1). Their convex combination is at most (19), by monotonicity. The h=0 case is immediate. Thus f_n(0) is an exact universal upper bound and is attained by greedy. For B with genuinely no exceptional queries it can replace U_0 in (2), although (1) is simpler for the asymptotics.

## Scope

The finite joint-event bound and its asymptotic consequences are proved here without using an external hardness theorem. The information model follows David Gamarnik, Eren C. Kızıldağ and Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1. The binary-word factor is the round-5 reduction, reproduced above. No priority claim in the wider literature is made for the weighted dense-graph tail or its combination with that reduction.

An algorithm that rejects everything until its last update and then chooses a maximum clique still has no exceptional queries and D empty. Its core has size at most one, so almost all of its output is charged to R. The restriction on final late admissions remains essential for this conclusion. Exceptional queries destroy the unweighted fresh-row probability estimate, but are covered by the predictable charges in (5). The exact greedy optimality in Section 5 is asserted only with no exceptional queries. Neither the endpoint nor that optimal irrevocable coefficient proves an optimal deletion-disagreement exponent or addresses unrestricted polynomial-time clique search. That problem remains open.
