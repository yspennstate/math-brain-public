# Open problem T068: Karp's problem: finding cliques of size (1 + ε) log₂ n in G(n, 1/2)

Statement: For every ε > 0, no polynomial-time algorithm finds a clique of size (1 + ε) log₂ n in G(n, 1/2) with probability bounded away from zero; equivalently, the greedy algorithm's size log₂ n is the algorithmic threshold, half the clique number 2 log₂ n.

Caveat: Proving it unconditionally would separate P from NP, so the working form asks for proofs against broad algorithm classes.

Source: R. M. Karp, The probabilistic analysis of some combinatorial search algorithms, in Algorithms and Complexity: New Directions and Recent Results (Academic Press, 1976)

Where it stands (checked by us, Nov 2026): The Metropolis process fails (Jerrum 1992); overlap-gap and low-degree barriers rule out large classes of algorithms in related problems: local algorithms for sparse independent sets (Gamarnik–Sudan, arXiv:1304.1831), planted clique (Gamarnik–Zadik, arXiv:1904.07174), low-degree polynomials for sparse independent sets (Wein, arXiv:2010.06563). Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T068 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T068 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.


----- earlier REPORT.md -----
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
