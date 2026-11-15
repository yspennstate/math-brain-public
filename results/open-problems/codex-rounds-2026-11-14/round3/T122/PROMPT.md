# Open problem T122: The maximum cut of sparse random graphs

Statement: For fixed d > 1, determine the limit of MaxCut(G)/n for G = G(n, d/n), or for a uniformly random d-regular graph, and prove that it equals the zero-temperature value predicted by the cavity method for the diluted antiferromagnet.

Caveat: For d ≤ 1, MaxCut/n → d/2 in G(n, d/n), since almost every edge lies in a tree component. As d → ∞ the answer is n(d/4 + P_*√(d/4) + o(√d)) with P_* ≈ 0.7632 the Parisi constant. For fixed d the prediction is the full replica-symmetry-breaking (Mézard–Parisi) cavity functional on a sparse graph, for which no rigorous variational formula is known.

Source: M. Mézard and G. Parisi, The Bethe lattice spin glass revisited, Eur. Phys. J. B 20 (2001); A. Dembo, A. Montanari and S. Sen, Extremal cuts of sparse random graphs, Ann. Probab. 45 (2017)

Where it stands (checked by us, Nov 2026): The limit exists (Bayati–Gamarnik–Tetali 2013). The large-d asymptotics are due to Dembo–Montanari–Sen (arXiv:1503.03923). For diluted spin glasses the Parisi-type formula gives upper bounds (Franz–Leone, J. Stat. Phys. 111 (2003); Panchenko–Talagrand, Probab. Theory Related Fields 130 (2004)); Harangi (arXiv:2506.21296) proves 2-RSB upper bounds that beat 1-RSB, and Aronow and Lopatto (arXiv:2609.19057) show that max-cut and max-bisection have the same limit at every fixed degree of a random regular graph. The exact value for fixed d > 1 is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T122 (read it,
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
VERDICT: PARTIAL located recent cavity-formula proofs covering the Erdős–Rényi branch; regular-graph coverage not verified

The literature stopping condition was met within ten minutes. See
[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for references, theorem scope,
and the deduction for G(n,d/n). No new research proof is claimed.

The principal arXiv finding is Dmitry Panchenko, *The Mézard-Parisi formula*,
[arXiv:2610.39545](https://arxiv.org/abs/2610.39545), submitted October 29,
2026, with companion [arXiv:2610.39542](https://arxiv.org/abs/2610.39542).
The separate OpenAI manuscript linked in SOLVED_ELSEWHERE.md states a general
Poisson theorem whose hypotheses include deterministic antiferromagnetic
two-spin interactions. Its stated equality yields the Erdős–Rényi
zero-temperature variational value. These are recent proof manuscripts;
their full proofs were not audited here.

Checks: verified the antiferromagnetic factorization, positivity for every
integer moment, interaction-density normalization, finite-volume entropy
error log(2)/beta, Poisson-to-simple-graph coupling with expected edit count
at most d^2(n-1)/(2n), and concentration. Rechecked the energy normalization
independently through Cut=(|E|-sum sigma_u sigma_v)/2. No numerical constants
or computation results are asserted.

Commands: read-only `pwd`, `rg --files`, `rg -n`, `sed -n`, and
`date '+%Y-%m-%d %H:%M:%S %Z'`; web-tool searches and opened primary papers
and primary TeX, listed in LOG.md. A startup Python file read and a later
echo probe under `nice -n 15` both reported `setpriority: Operation not
permitted`. No research computation followed, and no script or dataset was
needed. All created files are in this folder. No git, external writes, or
subagents were used.

What stopped: the proposed quantitative subdivision reduction in LOG.md was
abandoned once the literature stopping condition was satisfied. It has not
been proved here. What remains uncertain: independent validation of the new
proof manuscripts and the fixed-degree regular ensemble. Next worker: audit
the cited general theorem and determine whether its lower-bound argument
extends to regular factor graphs; do not infer regular coverage from Poisson
coverage or symmetric-coupling examples.

Task: “push this problem forward by one checkable piece” — T122, received
2026-11-14 approximately 22:00 +04 (Asia/Tbilisi).
