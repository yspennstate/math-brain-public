# Open problem T284: All-algorithm hardness at the sparse independent-set overlap barrier

Statement: For every fixed epsilon>0 and sufficiently large fixed d, determine whether any randomized algorithm of time polynomial in n can, with probability tending to one, find an independent set of size at least (1+epsilon)(log d/d)n in G(n,d/n). Prove the obstruction for all polynomial-time algorithms under an explicitly stated average-case complexity assumption, or construct an algorithm crossing this barrier. This asks whether the multi-overlap barrier in this standard model captures a real computational limit.

Caveat: No universal implication from an overlap gap to hardness is asserted. Any complexity assumption in a solution must be named; worst-case NP-hardness alone is insufficient.

Source: Gamarnik, The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures (arXiv:2109.14409); Li-Schramm, arXiv:2411.01836.

Where it stands (checked by us, Nov 2026): 2411.01836 supplies an easy optimization problem with an overlap gap, answering the old generic-counterexample branch. Stable/local/low-degree lower bounds do not by themselves rule out every polynomial-time algorithm for the stated independent-set task.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T284 (read it,
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
VERDICT: PARTIAL inverse-polynomial success amplifies to high probability with any fixed density loss

For fixed rational d>0 and 0<b<a<=1, a polynomial-time algorithm that finds an independent set of size ceil(a n) in G(n,d/n) with eventual success at least c n^(-s) can be transformed into a polynomial-time algorithm that finds one of size ceil(b n) with failure O(n^(-L)), for any fixed L>0. The graph distribution and degree d are preserved. PROOF.md gives every reduction step and an explicit finite-n failure bound. The only non-elementary input is the biased-product reverse hypercontractive inequality in Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/pdf/1108.1210 . No novelty claim is made for this application.

At every fixed integer d, the supremum of independent-set densities achievable with eventual inverse-polynomial success equals the supremum achievable with high probability. In particular, any inverse-polynomial-success algorithm crossing the (log d)/d barrier by epsilon would give a high-probability algorithm crossing it by every smaller positive epsilon'. This removes the success-probability quantifier, with fixed slack; it does not remove the need to prove hardness or construct an algorithm.

Verification command:

    env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py

Result: PASS. Exact rational enumeration checked 4096 Bayes identities and 225 conditional repair distributions on four vertices. Additional checks covered 3060 Boolean negative-moment examples, 80 non-Boolean examples, and 12933 ceiling/mean cases. The repair exponent was re-derived with an optimized Chernoff bound, and log(2) was evaluated independently by an exact series. Full data are in verification.json; exact command output is in LOG.md; the adversarial audit is in AUDIT.md. The run took 0.2713 seconds and peaked at 15253504 bytes of resident memory. OMP_NUM_THREADS was 1. The inherited nice value was 20; attempts to request nice 15 were denied by the sandbox, leaving the lower inherited priority in place.

What failed: the initial verifier launch stopped at an unsupported macOS address-space-limit operation, before doing any checks. The verifier now records that limitation and uses fixed tiny inputs; its measured peak memory is about 15 MB. Repetition with fresh solver coins alone does not handle hard input instances. Conditioning the repair law on the first selected successful trial would need an unjustified argument; the proof uses a union bound over predetermined trials instead.

Unresolved: T284 itself is not settled. No all-algorithm obstruction, named average-case complexity reduction, or barrier-crossing algorithm is supplied. No amplification at exactly the original density, no growing-d runtime claim, and no upgrade from an isolated success subsequence are asserted. The bounded literature search found no whole-problem settlement; it is recorded in LOG.md, together with the primary papers actually opened.

Next worker: use PROOF.md to formulate the remaining hardness question at inverse-polynomial success and with a fixed density margin. The substantive missing step is a distribution-preserving reduction from a separate, explicitly named average-case assumption, or a new algorithm. For improving this lemma itself, investigate amplification without fixed density slack and whether the runtime exponent can be reduced; the present proof needs both a refresh probability bounded away from zero as n grows and an exponential repair tail beating the number of trials.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 21:27 +04.
