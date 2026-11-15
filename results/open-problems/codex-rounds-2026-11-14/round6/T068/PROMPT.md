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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T068 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PROVED online clique barrier with polynomially many final deletion disagreements

The round-4 result holds: its reduction was independently re-derived and its verification rerun unchanged, reproducing every recorded count. The new result improves its guessing factor from Σ_{j≤r} binom(n,j) to binom(k+r,r), without imposing structure on the possible deletion sets. This extends the allowed final deletion disagreement from O(log n) to a positive power of n. Full argument: [PROOF.md](PROOF.md). The unrestricted Karp problem remains open.

Use the round-4 model: B inspects vertices adaptively and may replace its clique by any clique among inspected vertices after each round. Let J be its final clique, P the vertices present immediately after their own inspection rounds, D the inspection rounds of vertices in P\J, R=J\P, and E the exceptional-query union. Put L=log₂n−1. For fixed η>0, c=min{η²,1}/8, ξ=min{η²,1}/64, integer k≥ceil((1+η)L), and 0≤r≤n, sufficiently large n satisfy

\[
\Pr\{|J|-|R|\ge k,\ |D|\le r,\ |E\cap\tbinom J2|\le cL^2\}
\le\min\left\{1,\binom{k+r}{r}2^{-\xi L^2}\right\}.
\]

The proof guesses a binary word indexed only by inspection-time positive decisions. It retains the first k final-core vertices, skips at most r other positives before them, and stops simulating immediately afterwards. Words have k ones, at most r zeros, and end in one, so their number is binom(k+r,r). Clique and both query-budget guards make every wrong word a valid irrevocable algorithm. The correct word preserves B's transcript only up to its stopping round. This shorter guarantee is sufficient. In fact only disagreements before the kth final-core vertex need be capped.

For the target (1+ε)log₂n, choose any fixed 0≤β<ε and η=ε−β. With |R|≤βlog₂n, |D|≤floor(n^a), and exceptional cap cL² evaluated at η, every fixed

\[
0\le a<\frac{\xi}{1+\eta}
\]

gives success probability at most 2^(−(ξ−a(1+η)−o(1))(log₂n)²). Arbitrarily many temporary revisions remain allowed. There is no running-time hypothesis.

Explicitly, set h=min{ε²/4,1} and a=h/[128(1+ε/2)]. The caps

\[
|R|\le\lfloor\varepsilon\log_2n/2\rfloor,\quad
|D|\le\lfloor n^a\rfloor,\quad
|E\cap\tbinom J2|\le hL^2/8
\]

give 2^(−(h/128−o(1))(log₂n)²). The preceding report obtained that exponent with deletion cap floor(h log₂n/128). For ε=1 the new a is 1/768 and the probability coefficient is 1/512. The new factor also has logarithm O(log n) for r=O(log n), recovering the full source exponent to leading order in that regime.

Validation commands, both exited 0:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T068/verify_revision.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_words.py > verification_output.txt 2>&1
```

The new set-based oracle implementation checked all 23,112 legal clique trajectories on every graph on 1–4 vertices, then adaptive inspection/query policies. Combined totals: 24,000 original runs, 865,050 guarded runs, and 20,832 correct-word/budget events. All guards fired on wrong words. Independent schedule-first counting reproduced the trajectory and run totals. Forty-two exact word-family cases, exact large-integer binomial counts, logarithmic products, and Bernoulli thinning checked the count and exponent separately. Targeted fixtures checked early stopping with four later disagreements and the necessity of the late-admission restriction. Final run: 11.043 seconds, peak RSS 19,480,576 bytes, actual nice 20, one thread. Complete output is in [LOG.md](LOG.md) and [verification_output.txt](verification_output.txt).

The bounded literature check found no general solution. The external input remains David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1 and Theorem 2.2. The arXiv abstract and relevant full-text sections were opened. The related induced-matching and common-induced-subgraph papers opened during the check do not state a solution of this problem; bibliographic details are in LOG.md. Priority for this reduction in the wider literature is not established.

What failed or remains uncertain: the full OGP theorem is used externally, not independently reconstructed. Finite enumeration audits the reduction, not that asymptotic theorem. Removing the guards or requiring full transcript preservation after the stopping round would invalidate the present argument. Unrestricted late admissions remain uncontrolled: selecting a maximum clique only at the final update has E=∅, D=∅, and core size at most one. Large enough powers of n make the bound vacuous; no optimal disagreement exponent is established. No substantive mathematical or computational check failed. One no-op log patch missed its context; the launcher warned about setpriority, while both scripts verified actual inherited nice 20.

Next worker: sharpen the permissible power a, starting with E=∅ and R=∅. The present leading entropy cost is a(1+η)(log₂n)²; improve the external probability exponent or exploit graph information to reduce this cost. Compare with explicit revising algorithms using a polynomial-size inspected candidate set, to determine how far the bound is from the actual threshold. A direct stopping-time argument could also replace the advice-word union bound. None of these further improvements is established here.

Task: “take the NEXT checkable step on this problem, building on that work.” — T068, 15 November 2026, 07:56:03 Asia/Tbilisi (first recorded clock).
