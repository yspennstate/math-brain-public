# Open problem T068: Karp's problem: finding cliques of size (1 + ε) log₂ n in G(n, 1/2)

Statement: For every ε > 0, no polynomial-time algorithm finds a clique of size (1 + ε) log₂ n in G(n, 1/2) with probability bounded away from zero; equivalently, the greedy algorithm's size log₂ n is the algorithmic threshold, half the clique number 2 log₂ n.

Caveat: Proving it unconditionally would separate P from NP, so the working form asks for proofs against broad algorithm classes.

Source: R. M. Karp, The probabilistic analysis of some combinatorial search algorithms, in Algorithms and Complexity: New Directions and Recent Results (Academic Press, 1976)

Where it stands (checked by us, Nov 2026): The Metropolis process fails (Jerrum 1992); overlap-gap and low-degree barriers rule out large classes of algorithms in related problems: local algorithms for sparse independent sets (Gamarnik–Sudan, arXiv:1304.1831), planted clique (Gamarnik–Zadik, arXiv:1904.07174), low-degree polynomials for sparse independent sets (Wein, arXiv:2010.06563). Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T068 (read it,
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
VERDICT: PARTIAL existing broad online-algorithm barrier located and specialized to cliques

The literature check found a direct advance missing from the brief: David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/abs/2504.11450v2), Theorem 2.2. This is a 2025 paper revised in January 2026, not a post-November-2026 development. The unrestricted problem remains open.

Following the substantial-advance stop instruction, the session ends with this literature correction. [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) gives the theorem, exact algorithm restriction, and a checked complement reduction to the stated clique target. Its filename follows the instruction; it does not mean that the full conjecture is solved. No new theorem is claimed.

For every fixed ε>0, the resulting success bound is 2^(−ξ(log₂ n−1)²), with ξ=min{ε²,1}/64, for the specified restricted online class. The precise look-ahead restriction is essential.

Search queries, opened sources, shell commands, outputs, and failed accesses are in [LOG.md](LOG.md). The decisive web operations were opening `https://arxiv.org/abs/2504.11450`, `https://arxiv.org/html/2504.11450v2`, and `https://arxiv.org/pdf/2504.11450v2`, then locating Definition 2.1, condition (1), and Theorem 2.2. There was no mathematical computation and there are no simulation data or computation commands to reproduce.

Audit: checked the theorem against its PDF presentation; derived the complement simulation; checked the allowed density range at p=1/2; retained the −1 shift in log₂(n/2); converted the probability bound using both base-two and natural logarithms; exhibited a full-information algorithm outside the restricted class. The paper's full proof was not independently verified.

Failed or unavailable: publisher access for an edge-query lead returned 403; a scheduler-priority read was sandbox-denied. The preliminary memory command printed a priority warning and attempted an unsuccessful background refresh. No further computation was run. These failures do not affect the literature theorem or the algebraic specialization.

Next worker: update the status to include this direct dense-graph online barrier. Read its Sections 4–5 before attempting an extension to algorithms that may revise earlier membership decisions or exceed its bound on queried output pairs. The search was bounded rather than exhaustive; absence of a general solution is not independently certified.

Task: “Push this problem forward by one checkable piece” — T068, 14 November 2026, approximately 20:49 Asia/Tbilisi.
