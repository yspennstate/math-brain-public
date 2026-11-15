# Open problem T122: The maximum cut of sparse random graphs

Statement: For fixed d > 1, determine the limit of MaxCut(G)/n for G = G(n, d/n), or for a uniformly random d-regular graph, and prove that it equals the zero-temperature value predicted by the cavity method for the diluted antiferromagnet.

Caveat: For d ≤ 1, MaxCut/n → d/2 in G(n, d/n), since almost every edge lies in a tree component. As d → ∞ the answer is n(d/4 + P_*√(d/4) + o(√d)) with P_* ≈ 0.7632 the Parisi constant. For fixed d the prediction is the full replica-symmetry-breaking (Mézard–Parisi) cavity functional on a sparse graph, for which no rigorous variational formula is known.

Source: M. Mézard and G. Parisi, The Bethe lattice spin glass revisited, Eur. Phys. J. B 20 (2001); A. Dembo, A. Montanari and S. Sen, Extremal cuts of sparse random graphs, Ann. Probab. 45 (2017)

Where it stands (checked by us, Nov 2026): The limit exists (Bayati–Gamarnik–Tetali 2013). The large-d asymptotics are due to Dembo–Montanari–Sen (arXiv:1503.03923). For diluted spin glasses the Parisi-type formula gives upper bounds (Franz–Leone, J. Stat. Phys. 111 (2003); Panchenko–Talagrand, Probab. Theory Related Fields 130 (2004)); Harangi (arXiv:2506.21296) proves 2-RSB upper bounds that beat 1-RSB, and Aronow and Lopatto (arXiv:2609.19057) show that max-cut and max-bisection have the same limit at every fixed degree of a random regular graph. The exact value for fixed d > 1 is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T122 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T122 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T122 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T122 (read it, never
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
VERDICT: PROVED finite-cascade kernel invariance, yielding the regular hierarchical upper bound

The round 4 result survives independent checking, conditional on its
stated external theorem. The bounded literature search found no new
regular-ensemble solution. The fixed-degree cavity equality remains
unproved here.

New beyond round 4: [PROOF.md](PROOF.md) proves that every no-root finite
Ruelle-cascade trial in its equation (11) defines an invariant weak-kernel
law. The proof handles every bounded positive function of finitely many
sampled columns, including all finite cavity tilts. Successive marked
Poisson point processes preserve the cascade's weighted tree law; a
measure-preserving permutation of product column coordinates removes
the resulting branch relabeling. Biased sampled marks are explicitly
allowed.

This supplies the missing trial-space inclusion. For the hierarchical
infimum J_d(beta) defined in PROOF.md and cut pressure p_d(beta),

\[
 p_d(\beta)\le J_d(\beta),\qquad
 c_d\le J_d(\beta)/\beta.
\]

The general upper bound already appears in Viktor Harangi,
[*RSB bounds on the maximum cut*, arXiv:2506.21296v1,
Theorem 3.2](https://arxiv.org/html/2506.21296v1).
The contribution of this folder is the explicit invariant-law inclusion
and derivation in the earlier report's normalization, using Theorem 2.7
of Amin Coja-Oghlan and Will Perkins,
[*Spin systems on Bethe lattices*, arXiv:1808.03440v1](https://arxiv.org/html/1808.03440v1).
It is not a new numerical bound or a proof of the full cavity formula.

Checks: proved the Poisson intensity scaling directly; verified depths
one and two independently; matched cascade exponents to Harangi's
convention; tested asymmetric endpoint messages where the marks really
are biased; checked row and column map orientations, infinite cascade
summability, measurability, all constant shifts and the entropy error.
Details and the exact asymmetric test values are in [LOG.md](LOG.md).

Commands: read-only pwd, rg --files, cat and sed -n; primary papers
opened with the web search tool; local files written with apply_patch.
Read commands were launched with `nice -n 15 env OMP_NUM_THREADS=1`.
The sandbox rejected the priority change, so no research computation
or script was run. No git, subagents or writes outside this folder.

What failed or remains uncertain: no reverse comparison was obtained.
The external invariant-law theorem's full proof remains unaudited.
No degree-two extension or interchange of hierarchy infima with the
temperature limit is claimed. An initially truncated read was repeated
in smaller pieces. No mathematical counterexample was found in the
analytic checks. A final prose cleanup patch needed a context correction;
no mathematical change resulted.

Next worker: write Delta_d(beta)=J_d(beta)-p_d(beta)>=0. Equation (19)
of PROOF.md shows that the zero-temperature equality is equivalent to
Delta_d(beta)=o(beta). Seek cascade trials whose functional values are
within o(beta) of the invariant-law minimum. The upper-bound inclusion
is now proved; it does not establish that approximation or require
arbitrary invariant minimizers to be hierarchical.

Task: “take the NEXT checkable step on this problem, building on that work”
— T122, received 2026-11-15 approximately 08:23 +04 (Asia/Tbilisi).
