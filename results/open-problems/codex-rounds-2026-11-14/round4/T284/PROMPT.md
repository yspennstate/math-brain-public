# Open problem T284: All-algorithm hardness at the sparse independent-set overlap barrier

Statement: For every fixed epsilon>0 and sufficiently large fixed d, determine whether any randomized algorithm of time polynomial in n can, with probability tending to one, find an independent set of size at least (1+epsilon)(log d/d)n in G(n,d/n). Prove the obstruction for all polynomial-time algorithms under an explicitly stated average-case complexity assumption, or construct an algorithm crossing this barrier. This asks whether the multi-overlap barrier in this standard model captures a real computational limit.

Caveat: No universal implication from an overlap gap to hardness is asserted. Any complexity assumption in a solution must be named; worst-case NP-hardness alone is insufficient.

Source: Gamarnik, The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures (arXiv:2109.14409); Li-Schramm, arXiv:2411.01836.

Where it stands (checked by us, Nov 2026): 2411.01836 supplies an easy optimization problem with an overlap gap, answering the old generic-counterexample branch. Stable/local/low-degree lower bounds do not by themselves rule out every polynomial-time algorithm for the stated independent-set task.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T284 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T284 (read it,
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
VERDICT: PARTIAL subpolynomial success amplifies to high probability with vanishing density loss

The earlier amplification result holds. Its main bound was re-derived independently and its verifier rerun unchanged from this directory; all checks passed.

New beyond that report: let d>0 be fixed rational and k_n/n->a>0 be a polynomial-time computable target. If an arbitrary randomized polynomial-time solver succeeds in G(n,d/n) with probability v_n=n^(-o(1)), a polynomial-time transformation finds an independent set of size k_n-o(n) with probability tending to one. It makes n^2 ceil(log_2 n) solver calls and does not need to know v_n or its convergence rate. For constant starting success, the loss is O(n log log n/log n), with failure O((log n)^(-K)) for any fixed K>0. PROOF.md gives the exact loss and finite-n probability bound. This removes fixed density slack for a narrower success hypothesis than the earlier theorem; it does not remove all vertex loss.

The construction tries dyadic edge-refresh rates, repairs each solver output by deleting endpoints of original internal edges, and returns the largest valid result. The analytic input is the same as before: Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/pdf/1108.1210 . No novelty claim is made for the underlying amplification method.

Commands, run in this folder:

    env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114/briefs/T284/verify.py
    env OMP_NUM_THREADS=1 nice -n 15 python3 verify_extension.py

Both pass. The new verifier checks 90 exact latent-variable posterior identities, 396 independent count-based posterior identities, 6120 numerical negative-moment inequalities, 111 exact binomial tails compared numerically with the bound, 369 scale/loss cases, 8 complete sampling-error budgets, and 19482 rounding identities. It tests symbolic integers up to n=2^8192 without allocating n-sized objects. Runtime was 1.5033 seconds; peak resident memory was 16482304 bytes. OMP_NUM_THREADS=1 and inherited nice=20 were verified; the sandbox refused raising priority to the requested 15. Full output is in LOG.md; data are in verification.json and extension_verification.json.

What failed or changed: the first new verifier run included small n outside the proof's eventual scale-existence hypothesis. Its test domain was corrected and four such cases are explicitly counted. An audit found that the overlap-scale corollary needed polynomial-time computability of its target constant, rather than mere computability; the corrected corollary uses integer d and rational epsilon, with an explicit approximation argument for log d. No contradiction to either amplification theorem was found.

Unresolved and uncertain: T284 remains open here. There is no named average-case hardness reduction, no all-polynomial-time obstruction, and no algorithm that crosses the barrier. The new theorem does not give exactly k_n vertices, vanishing loss from arbitrary inverse-polynomial starting success, or polynomially small failure with vanishing loss. The imported analytic inequality is checked in the primary paper and used as a theorem; finite numerical checks do not reprove it. The bounded literature check found no settlement and is not exhaustive. AUDIT.md records the attempts to break the result and the limits of the argument.

Next worker: the concrete remaining amplification question is whether constant-success search can be amplified with O(n/log n) loss, rather than the present O(n log log n/log n), or whether a counterexample to such a general transformation can be proved. The present negative-moment estimate alone stops at constant failure when delta log n stays bounded. A more central advance on T284 still needs a distribution-preserving reduction from a separate, explicitly named average-case assumption, or a barrier-crossing algorithm; these amplification lemmas supply neither.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 03:44 +04 (Asia/Tbilisi).
