# Substantial advance elsewhere: an online barrier

The unrestricted problem remains open. This file records a substantial advance omitted from the supplied status; it does not claim a result published after November 2026.

David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/abs/2504.11450v2). First submitted 15 April 2025; v2 submitted 30 January 2026. The PDF title page is dated 25 January 2026.

## The result being used

[Definition 2.1, condition (1), and Theorem 2.2](https://arxiv.org/html/2504.11450v2) allow randomized, adaptive vertex inspection. Each round reveals the current vertex's pairs with previously inspected vertices, permits additional pair queries, and irrevocably accepts or rejects the current vertex. Let E be the union of additional query sets and I the final independent set. Put b=1/(1-p). If

\[
|E\cap\tbinom I2|\le c\log_b^2(np),
\]

then, for every fixed η>0 and sufficiently large n,

\[
\Pr\{|I|\ge(1+\eta)\log_b(np)\}
\le (np)^{-\xi\log_b(np)},
\quad
c=\frac{\min\{\eta^2,1\}}8,
\quad
\xi=\frac{\min\{\eta^2,1\}}{64}.
\]

The permitted range is d/n≤p≤1−n^(−1/d), for a sufficiently large constant d depending on η. The restriction counts queried **pairs inside the output**, not all additional queries. There is no polynomial-time requirement in this lower bound. See printed page 9 of the [PDF](https://arxiv.org/pdf/2504.11450v2).

## Consequence for the exact clique question

This specialization is a deduction from the cited theorem, not a new lower-bound proof.

Fix ε>0 and use η=ε above. Let H have distribution G(n,1/2), and let G be its complement. For each unordered pair e, its indicator in G is one minus its indicator in H. These indicators remain independent fair bits, so G also has distribution G(n,1/2).

Consider a clique algorithm B with the round structure described above. Simulate it on H using queries to G, reversing every answer. The simulated algorithm A accepts exactly the same vertices as B, using the same internal random seed. Every partial clique of H is an independent set of G. Adaptive choices and query sets agree under the simulation because all answers seen by B agree with the reversed answers seen by A. Thus the simulation preserves the output size and the set E of additional queried pairs, including its intersection with output pairs.

Write L=log₂(n/2)=log₂ n−1. Since b=2 and np=n/2, the theorem gives, for all sufficiently large n,

\[
\boxed{
\Pr\{|B(H)|\ge(1+\varepsilon)\log_2 n\}
\le 2^{-\xi(\log_2 n-1)^2}
}
\]

for every such algorithm satisfying |E∩binom(B(H),2)|≤cL² on every execution. Indeed, (1+ε)log₂ n≥(1+ε)L, so the event displayed is contained in the theorem's event. The bound tends to zero. Algorithms with no additional queries satisfy the restriction with zero budget.

The density hypothesis holds eventually: d/n≤1/2 follows from n≥2d; and 1/2≤1−n^(−1/d) follows from n≥2^d. These conditions can be combined with the theorem's n≥n₀.

## Checks and limits

The exponent has two equivalent forms:

\[
(n/2)^{-\xi\log_2(n/2)}
=2^{-\xi L^2}
=\exp\!\left(-\frac{\xi}{\ln2}[\ln(n/2)]^2\right).
\]

The first equality uses n/2=2^L; the second follows by taking natural logarithms. This checks both the sign and the base conversion.

A full-information algorithm need not satisfy the budget. For example, if it selects all pairs as additional queries before constructing its output, then |E∩binom(B(H),2)|=binom(k,2) for an output of size k. At k≈(1+ε)L this is asymptotic to (1+ε)²L²/2, exceeding cL² because c≤1/8. This supplies a concrete case excluded by the theorem and prevents interpreting the result as an unrestricted algorithmic lower bound.

The statement and constants were checked in both HTML and PDF. The paper's full proof was not independently re-proved here. No numerical experiment establishes this asymptotic theorem.
