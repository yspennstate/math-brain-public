# Open problem T068: Karp's problem: finding cliques of size (1 + ε) log₂ n in G(n, 1/2)

Statement: For every ε > 0, no polynomial-time algorithm finds a clique of size (1 + ε) log₂ n in G(n, 1/2) with probability bounded away from zero; equivalently, the greedy algorithm's size log₂ n is the algorithmic threshold, half the clique number 2 log₂ n.

Caveat: Proving it unconditionally would separate P from NP, so the working form asks for proofs against broad algorithm classes.

Source: R. M. Karp, The probabilistic analysis of some combinatorial search algorithms, in Algorithms and Complexity: New Directions and Recent Results (Academic Press, 1976)

Where it stands (checked by us, Nov 2026): The Metropolis process fails (Jerrum 1992); overlap-gap and low-degree barriers rule out large classes of algorithms in related problems: local algorithms for sparse independent sets (Gamarnik–Sudan, arXiv:1304.1831), planted clique (Gamarnik–Zadik, arXiv:1904.07174), low-degree polynomials for sparse independent sets (Wein, arXiv:2010.06563). Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T068 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T068 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T068 (read it,
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
VERDICT: PROVED online clique barrier with bounded final late admissions and arbitrary intermediate revisions

The earlier bounded-deletion result holds: its reduction was independently re-derived and its computation rerun unchanged. The new result follows the earlier report's proposed next step, allowing late admission and readmission. It loses the number of final late vertices from the clique target, with no guessing factor for those vertices. Full proof: [PROOF.md](PROOF.md). This is a deduction from an existing theorem; priority in the wider literature is not established.

The algorithm may replace its clique by any clique among inspected vertices after each inspection round, using the same information model as before. Write J for its final clique, E for its exceptional-query union, P for vertices accepted immediately after their own inspection round, D for inspection rounds of vertices in P\J, and R=J\P. Intermediate deletions and readmissions are unrestricted. Put L=log₂n−1. For every fixed η>0, sufficiently large n, and integer 0≤r≤n,

\[
\Pr\{|J|-|R|\ge(1+\eta)L,\ |D|\le r,
 |E\cap\tbinom J2|\le c_\eta L^2\}
\le\min\left\{1,\left(\sum_{j=0}^r\binom nj\right)2^{-\xi_\eta L^2}\right\},
\quad c_\eta=\frac{\min\{\eta^2,1\}}8,\quad
\xi_\eta=\frac{\min\{\eta^2,1\}}{64}.
\]

For the target (1+ε)log₂n, choose any fixed 0≤β<ε and η=ε−β. Allow |R|≤βlog₂n and |D|≤a log₂n with 0≤a<ξ_η. Under the displayed exceptional-query cap, success has probability at most 2^(−(ξ_η−a−o(1))(log₂n)²). Thus a positive multiple of log n final late admissions is allowed. The query cap must be evaluated at η and may decrease when the allowed late-admission coefficient β increases.

For an explicit choice, let h=min{ε²/4,1}. The caps |R|≤floor(εlog₂n/2), |D|≤floor(hlog₂n/128), and |E∩binom(J,2)|≤hL²/8 give success probability at most 2^(−(h/128−o(1))(log₂n)²). No running-time assumption is needed. Counts D and R measure final disagreement with inspection-time decisions, so the theorem also permits arbitrarily many temporary revisions that do not increase those counts.

The proof guesses D, simulates the complete revising algorithm privately, and builds a separate irrevocable output. On the correct guess that output equals J∩P. Clique and query-budget guards make every wrong guess satisfy the source theorem. A uniformly random guess gives a second derivation of the same multiplicative loss.

Validation commands, all exited 0:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T068/verify_reduction.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_revision.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_counts.py
```

The earlier script reproduced all its recorded counts. The independent revision implementation checked all 23,112 legal clique trajectories across every graph on 1–4 vertices, plus adaptive policies and exceptional queries. In total: 24,808 original runs, 468,796 guarded runs, and 26,405 correct-guess/budget events. Every such event preserved the transcript and produced J∩P. All three guards were exercised. A second enumeration, summing compatible graphs over schedules, reproduced the totals. Exact fractions and independent logarithmic calculations checked the constants and exponents. New scripts ran in 3.709 seconds and 0.001 seconds, respectively, at nice 20 and one thread, with peak RSS below 16 MB. Full output: [LOG.md](LOG.md).

The literature check closed within one minute and found no solution of the unrestricted problem. The source remains David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2). The opened related October induced-matching and November worst-case clique papers do not state a solution to this problem; references and the scope of the bounded search are in LOG.md.

What fails or remains uncertain: removing the |R| loss is invalid for this reduction. Rejecting all vertices until the final update and then choosing a maximum clique has zero exceptional queries and D=∅, but nearly its entire output lies in R. Neither large deletion-disagreement budgets nor unrestricted final late-admission budgets are controlled here. The full OGP source proof remains external. Finite tests audit the reduction, not the asymptotic theorem. The launcher issued a setpriority warning; each computation verified actual inherited nice 20 before proceeding. No substantive verification failed; two illustrative audit fixtures were strengthened during readback.

Next worker: reduce the entropy cost of guessing D when the admissible inspection-time decision vectors have additional structure. For example, a family of at most N possible D sets replaces Σ_{j≤r}binom(n,j) by N in the same guarded reduction. A less immediate next step is a direct stopping-time argument controlling final disagreement, which might improve the deletion coefficient without paying r log₂n. Neither improvement is established here.

Task: “take the NEXT checkable step on this problem, building on that work.” — T068, 15 November 2026, 04:33:47 Asia/Tbilisi (first recorded clock).
