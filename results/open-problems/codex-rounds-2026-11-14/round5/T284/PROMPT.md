# Open problem T284: All-algorithm hardness at the sparse independent-set overlap barrier

Statement: For every fixed epsilon>0 and sufficiently large fixed d, determine whether any randomized algorithm of time polynomial in n can, with probability tending to one, find an independent set of size at least (1+epsilon)(log d/d)n in G(n,d/n). Prove the obstruction for all polynomial-time algorithms under an explicitly stated average-case complexity assumption, or construct an algorithm crossing this barrier. This asks whether the multi-overlap barrier in this standard model captures a real computational limit.

Caveat: No universal implication from an overlap gap to hardness is asserted. Any complexity assumption in a solution must be named; worst-case NP-hardness alone is insufficient.

Source: Gamarnik, The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures (arXiv:2109.14409); Li-Schramm, arXiv:2411.01836.

Where it stands (checked by us, Nov 2026): 2411.01836 supplies an easy optimization problem with an overlap gap, answering the old generic-counterexample branch. Stable/local/low-degree lower bounds do not by themselves rule out every polynomial-time algorithm for the stated independent-set task.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T284 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T284 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T284 (read it,
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
VERDICT: PARTIAL inverse-polynomial success amplifies with O(sqrt(n log n)) vertex loss

The earlier amplification theorem holds: its main estimates were independently re-derived and the round-3 verifier rerun unchanged. It passed.

New beyond the earlier report: for fixed rational d>0 and any polynomial-time computable integer target 1<=k_n<=n, a randomized polynomial-time solver with eventual success at least c n^(-s) in G(n,d/n) can be transformed into one returning at least

    k_n-O(sqrt(n log n))

vertices with failure at most n^(-L), for any fixed L>0. The new algorithm has polynomial worst-case time; its exponent may depend on the starting success lower bound and L. Unlike the round-3 transformation, it does not have a fixed runtime exponent independent of all inverse-polynomial success exponents. No positive limiting density for k_n is required.

This answers the earlier report's O(n/log n) constant-success amplification question affirmatively, with a smaller loss. It also strengthens the starting-success and final-failure ranges. It does not preserve exactly k_n vertices.

The construction applies Theorem 1.1, with the representation-length formulation in Theorem 3.2 and Remark 3.3, of Omid Etesami, Saeed Mahloujifar, and Mohammad Mahmoody, *Computational Concentration of Measure: Optimal Bounds, Reductions, and More*, arXiv:1907.05401v1, https://arxiv.org/pdf/1907.05401 . No novelty claim is made for computational concentration. The application groups graph edges into n-1 independent rows by smaller endpoint and puts all solver coins in one additional block. Membership in the solver-success event is polynomial-time decidable. Removing the owners of changed graph rows repairs the resulting independent set at a cost of at most the block distance. PROOF.md includes the deterministic repair, oracle construction, finite-bit implementation and full probability transfer to the original graph law.

Commands, run in this folder:

    env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T284/verify_extension.py
    env OMP_NUM_THREADS=1 nice -n 15 python3 verify_rows.py

Both pass. The new verifier checks 4165 ordered graph pairs, 35256 independent-set repairs, 8330 graph-and-tape distances, 225 exact product masses, 18 exact total-variation bounds, 54 seeded success-event transfers, 153 full sampling-error budgets and 48 fair-bit sampler thresholds. All checks are exact integer or rational calculations. Runtime was 0.0414 seconds and peak resident memory 16203776 bytes. The largest exhaustively enumerated graph has four vertices; a 20-vertex star checks repair of many changed edges by one deletion. Symbolic arithmetic reaches n=2^512 without allocating n-sized objects. OMP_NUM_THREADS=1 and inherited nice=20 were verified; the sandbox denied raising priority to the requested 15. Outputs are recorded in LOG.md, extension_verification.json and row_verification.json.

What failed or needed care: the source's final worst-case parameter display contains a product of logarithms, whereas its main theorem states the sharper single-log distance bound. This work explicitly invokes the stated theorem and does not copy that parameter choice or claim its leading constant. Optimizing its preceding quadratic tail exponent is consistent with the stated scale; this is not a reproof of the entire concentration theorem. The PDF screenshot and publisher formula-image requests failed with cache misses; the primary-source theorem text and publisher abstract were accessible. An attribution error conflating the author lists of two unrelated 2026 papers was corrected in LOG.md. No new verifier assertion failed.

Unresolved and uncertain: the imported concentration theorem is a published input, not independently proved or implemented here. The finite checks verify the application and sampling transfer, not MUCIO's search guarantee. The bounded literature check found no settlement of T284 and is not exhaustive. There is still no named independent average-case hardness reduction, no all-polynomial-time obstruction, and no algorithm crossing the independent-set overlap barrier. The transformation's input graph has the original law, but its auxiliary success graph is deliberately biased; no distribution-preserving hardness reduction is claimed.

Next worker: the requested O(n/log n) amplification improvement is now covered by this vertex-row application. The central remaining step is a reduction from a separate, explicitly named average-case assumption, or an algorithm crossing the barrier; another amplification lemma alone will not settle T284. For a concrete continuation of this line, investigate whether independent-set structure permits loss o(sqrt(n log n)) or exact-target amplification, and distinguish a limitation of arbitrary product-event concentration from a limitation for independent-set search. Inspect the source's Section 3.2 parameter discrepancy before attempting explicit constants or a practical implementation.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 06:30 +04 (Asia/Tbilisi).
