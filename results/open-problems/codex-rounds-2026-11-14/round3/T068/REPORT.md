VERDICT: PROVED online clique barrier with bounded deletions

The earlier clique specialization of Gamarnik–Kızıldağ–Warnke, Theorem 2.2, holds. The new result extends it to algorithms that may delete accepted vertices, provided each vertex can be admitted only at its own inspection round. The proof is in [PROOF.md](PROOF.md). This is a deduction from an existing theorem and is new beyond the earlier report; priority in the wider literature is not established.

Fix ε>0. Write L=log₂n−1, c=min{ε²,1}/8, and ξ=min{ε²,1}/64. For the deletion model defined in PROOF.md, let J be the final clique, E the union of exceptional query sets, and D the inspection rounds of admitted vertices absent from J. For sufficiently large n and every integer 0≤r≤n,

\[
\Pr\{|J|\ge(1+\varepsilon)\log_2 n,
       |E\cap\tbinom J2|\le cL^2,\ |D|\le r\}
\le \min\left\{1,\left(\sum_{j=0}^r\binom nj\right)2^{-\xi L^2}\right\}.
\]

Consequently, retaining the earlier exceptional-pair restriction and allowing at most floor(min{ε²,1} log₂n/128) deletions still gives success probability at most 2^(−(ξ/2−o(1))(log₂n)²). More generally any fixed deletion coefficient a<ξ gives exponent −(ξ−a−o(1))(log₂n)². No running-time assumption is required.

The reduction guesses which admitted vertices are ultimately deleted and simulates the algorithm while omitting those vertices from a separate irrevocable output. Clique and query-budget guards make every guess satisfy the original theorem. For the correct guess the guards preserve the complete trajectory. Counting the guesses costs Σ_{j≤r} binom(n,j). A second argument using a uniformly random guess recovers the same bound.

Validation command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_reduction.py
```

Exit 0. The check enumerated every graph on 2–5 vertices: 1,098 graphs, 6,588 original policy runs and 308,736 guarded simulations. All 3,815 correct-guess/budget events reproduced the output and transcript, including 3,485 with a nonempty deletion set and final clique of size at least two. All three guards were exercised. Exact binomial/Pascal counts, large-integer exponent calculations, and natural-log conversion also passed. Runtime was 6.181 seconds, peak RSS 15,302,656 bytes, actual nice priority 20, one thread. Full output and independently checked counts are in [LOG.md](LOG.md). These finite checks audit the reduction implementation; the written argument proves the general reduction.

The literature check found no general solution and closed within five minutes. The earlier source remains David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/abs/2504.11450v2). Its Sections 4–5 use a stopping-time identity that deletions invalidate. Virginia Vassilevska Williams and Or Zamir, *The k-Clique hypothesis is dead, for good*, [arXiv:2611.09764](https://arxiv.org/abs/2611.09764), gives a faster worst-case bound n^((ω/3−c)k), whose exponent is proportional to k; its displayed guarantee does not supply a polynomial-time algorithm for the present logarithmic target. Both arXiv pages were opened. Absence of a general solution is not certified by this bounded search.

What fails or remains uncertain: omitting the guards can violate the query restriction under a wrong guess. Arbitrary later admission of earlier vertices is excluded; with that freedom and unbounded computation, full inspection followed by maximum-clique selection defeats any zero-exceptional-query barrier. The multiplicative loss becomes uninformative for larger deletion budgets. The original OGP theorem is used as an external theorem; its entire proof has not been independently reconstructed. The launcher printed a setpriority warning, but the script verified inherited nice 20 before computing. No substantive verification failed.

Next worker: try to remove the later-admission restriction for a bounded number of added-back vertices. One concrete route is to guess those exceptional admissions and omit them from an irrevocable output, thereby losing their count from the clique target; combine that loss with the deletion-round guessing argument. The query guards must still be enforced on every guess. A sharper alternative is a direct modification of Lemma 4.8 allowing bounded symmetric difference on the inspected prefix. Neither extension is proved here.

Task: “take the NEXT checkable step on this problem, building on that work.” — T068, 15 November 2026, 01:09 Asia/Tbilisi (first recorded clock).
