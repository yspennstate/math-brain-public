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
VERDICT: PARTIAL specialized the regular invariant-kernel variational principle and proved an explicit temperature error; hierarchical equality remains open

The earlier Erdős–Rényi deduction survives independent rechecking,
conditional on its stated external theorems. The bounded recent-literature
search found no advance beyond the earlier reports that settles the
regular hierarchical formula. No complete external solution is asserted.

New beyond round 3: [PROOF.md](PROOF.md) specializes Theorem 2.7 of
Amin Coja-Oghlan and Will Perkins, *Spin systems on Bethe lattices*,
[arXiv:1808.03440v1](https://arxiv.org/html/1808.03440), to binary
antiferromagnetism. It gives the exact regular-ensemble value as a
zero-temperature limit of an optimization over invariant kernel laws.
That is an existing broader variational principle, not the claimed
Mézard–Parisi hierarchy restriction. The deduction explicitly checks POS,
strictly subunit edge weights, spin-prior normalization and concentration.

For integer d>=3, let Phi_d(beta) denote the minimum defined in PROOF.md.
For every beta,L>0 the result includes

\[
 0\leq c_d-\left[\frac d2+
       \frac{\Phi_d(\beta+L)-\Phi_d(\beta)}L\right]
 \leq \frac{\log2}{L}\log(1+L/\beta)\leq\frac{\log2}\beta.
\]

The entropy proof needs no differentiability of the limiting pressure
and no exchange of temperature limits with infima. The invariant spaces
depend on temperature. This explicit error is an elementary refinement
of the temperature passage, not a numerical evaluation of c_d.

The opened paper's HTML Potts specialization displays an edge-term sign
inconsistent with its general equation (2.12). The proof uses (2.12);
edge-weight scaling and direct finite-graph differentiation check its
minus sign. This does not invalidate the external general theorem.

Commands: read-only pwd, rg --files, ls, cat, sed -n, date; primary papers
opened with the web search tool; local files written with apply_patch.
[LOG.md](LOG.md) records the searches and checks. No research computation,
script, git operation, subagent or write outside this folder was used.

What remains unproved: equality of the invariant-kernel minimum with
the finite-hierarchy regular cavity infimum. General invariant laws and
arbitrary cascade trials cannot simply be identified; arbitrary cascade
trials have not been shown invariant. The cited external general theorem
has not been independently audited in full. Degree 2 is outside its
d>=3 hypothesis; no extension to that case is claimed here.

What failed: the regular theorem did not supply the hoped-for
hierarchical identification. Its extra structural requirement remains
the obstruction; no numerical optimization was attempted.

Next worker: start with equation (11) of PROOF.md. Establish the regular
hierarchical interpolation upper bound with exactly that normalization,
then seek the matching lower bound by controlling the invariant kernel
minimizer's structure. Even an o(beta) comparison of the two optimized
pressures suffices for the zero-temperature target; (9) already controls
the temperature passage. Merely replacing a Poisson count by d in the
old proof supplies no such lower bound.

Task: “take the NEXT checkable step on this problem, building on that work”
— T122, received 2026-11-15 approximately 04:55 +04 (Asia/Tbilisi).
