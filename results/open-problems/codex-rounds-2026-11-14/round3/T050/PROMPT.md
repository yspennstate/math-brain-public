# Open problem T050: Strict convexity of the limit shape in first-passage percolation

Statement: For first-passage percolation on Z^d, d ≥ 2, with iid continuous edge weights satisfying E min(t_1, …, t_{2d})^d < ∞ (so that the shape theorem holds), the limit shape (the asymptotic shape of the ball of passage time t, scaled by t) is strictly convex.

Caveat: Weights with an atom at their minimum of mass above the directed-percolation threshold give flat edges (Durrett–Liggett 1981), hence the continuity assumption.

Source: H. Kesten, Aspects of first passage percolation, École d'Été de Saint-Flour XIV (Lecture Notes in Math. 1180, 1986); A. Auffinger, M. Damron and J. Hanson, 50 Years of First-Passage Percolation (AMS University Lecture Series 68, 2017)

Where it stands (checked by us, Nov 2026): The limit shape is compact and convex (Cox–Durrett 1981); examples of non-polygonal shapes (Damron–Hochman 2013). Strict convexity is unknown for every continuous distribution, including exponential weights.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T050 (read it,
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
VERDICT: PARTIAL located a September 2026 preprint claiming planar exponential strict convexity; correctness not independently established

The literature check found OpenAI's *Strict convexity and differentiability of
the planar exponential first-passage limit shape* (September 24, 2026).
[The opened manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf)
states the relevant special case in Theorem 1.1. Reference, scope, and arXiv-ID
search outcome are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

Following the requested literature-discovery stop branch, no new proof or
numerical computation was attempted. The general problem is not proved here.

The audit separated strict convexity from differentiability, exponential from
general Gamma laws, and dimension two from higher dimensions. The
[author's scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md)
confirms that strict convexity is outside the selected Lean statements.
The full proof and the formalization's mathematical fidelity remain unchecked.

Commands, exact search queries, useful outputs, and failed fetches appear in
[LOG.md](LOG.md). No simulation command or numerical data exists. A requested
`nice -n 15` read printed `setpriority: Operation not permitted`; no heavy
programs were run. No git or external write was used.

Next worker: obtain and audit the preprint's strict-convexity argument in Part II,
especially Propositions 9.5 and 15.2 and the admissible path class they share.
Check for independent reviews or corrections before updating T050 to a proved
special case. Do not infer general Gamma strict convexity from differentiability.

Task: “push this problem forward by one checkable piece” — first recorded
2026-11-14 20:46:04 Asia/Tbilisi (16:46:04 UTC; receipt time not supplied).
