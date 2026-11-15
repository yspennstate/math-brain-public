# Open problem T050: Strict convexity of the limit shape in first-passage percolation

Statement: For first-passage percolation on Z^d, d ≥ 2, with iid continuous edge weights satisfying E min(t_1, …, t_{2d})^d < ∞ (so that the shape theorem holds), the limit shape (the asymptotic shape of the ball of passage time t, scaled by t) is strictly convex.

Caveat: Weights with an atom at their minimum of mass above the directed-percolation threshold give flat edges (Durrett–Liggett 1981), hence the continuity assumption.

Source: H. Kesten, Aspects of first passage percolation, École d'Été de Saint-Flour XIV (Lecture Notes in Math. 1180, 1986); A. Auffinger, M. Damron and J. Hanson, 50 Years of First-Passage Percolation (AMS University Lecture Series 68, 2017)

Where it stands (checked by us, Nov 2026): The limit shape is compact and convex (Cox–Durrett 1981); examples of non-polygonal shapes (Damron–Hochman 2013). Strict convexity is unknown for every continuous distribution, including exponential weights.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T050 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T050 (read it,
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
VERDICT: PARTIAL extended the uniform positive local-road defect bound to all positive Gamma laws and sharpened its exponential constant

The earlier result holds as a literature-discovery claim. The brief new search
found no verified solution of the full continuous-law problem. The September
2026 manuscript's strict-convexity proof remains only partly audited here.

New beyond the earlier report: [PROOF.md](PROOF.md) independently proves the
positive-defect ingredient for the admissible road class, allowing every
Gamma(shape kappa, rate lambda) law with positive parameters. It uses the
stationary dominated calibration supplied by the standard Damron–Hanson
construction under a hypothetical flat face. This external theorem is stated
explicitly and its primary source was opened.

The central improvement is a bounded comparison. If the untouched route has
defect D2, the competing route has defect D1, the perturbation saves v except
on an event of probability q, and its law changes by total variation delta,
then

    E D1 + E D2 >= v(1-q-delta).

This avoids the source's Markov-event loss. With its geometry and the same
two 1/8 error tolerances, the certified exponential lower bound increases
from `a epsilon/(8 CR)` to `3 a epsilon/(8 CR)`. The proof gives explicit
Gamma constants and a checkable condition on the scale. This is an auxiliary
lemma, not strict convexity for Gamma or exponential weights.

Checks: exact Gamma entropy and an independent likelihood second moment give
the required law-change bound; two path counts verify the lower-tail
estimate; integrating tail events verifies the bounded comparison. Random
cuts, repeated traversals, pauses, support separation, and rate scaling are
checked explicitly. No numerical computation or simulation was needed.

Commands used for the earlier files and readback:

```sh
rg --files ~/codex_op_1114/briefs/T050 ~/codex_op_1114r3/briefs/T050
env OMP_NUM_THREADS=1 nice -n 15 cat ~/codex_op_1114/briefs/T050/REPORT.md ~/codex_op_1114/briefs/T050/LOG.md ~/codex_op_1114/briefs/T050/SOLVED_ELSEWHERE.md
env OMP_NUM_THREADS=1 nice -n 15 cat LOG.md PROOF.md
env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
```

The earlier folder contains no PROOF.md or research scripts. All literature
searches and successful paper reads used the web tool. Exact queries and
the mathematical checks are in [LOG.md](LOG.md).

Failures and limits: the direct PDF open initially failed, raw-PDF access was
unsupported, and shell curl failed DNS; the landing page's PDF link worked.
The sandbox rejected the requested nice priority change. No heavy program,
git, external write, subagent, or mutation outside this folder was used.
No error was found in Proposition 9.5's lower-bound argument. Proposition
15.2's statement was read, but its proof and its antecedent estimates have
not been verified. No uncertainty about that proof is resolved by improving
the lower-bound constant.

Next worker: audit the contraction side, beginning with Lemma 10.2's local
potential construction and then the dependence of the output locality and
tracking constants in Sections 15.6–15.7 on s and the auxiliary cutoffs.
The rescaling integer D must be fixed before s is chosen. Establishing a
positive lower bound alone supplies no contradiction.

Primary sources opened:

- OpenAI, *Strict convexity and differentiability of the planar exponential
  first-passage limit shape*, September 24, 2026,
  [manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
  Definition 9.1, Lemma 9.2, Proposition 9.5, Proposition 15.2.
  No arXiv identifier was located for this manuscript.
- Michael Damron and Jack Hanson, *Busemann functions and infinite geodesics
  in two-dimensional first-passage percolation*,
  [arXiv:1209.3036](https://arxiv.org/abs/1209.3036), Section 3.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 01:00:35 Asia/Tbilisi (2026-11-14 21:00:35 UTC;
receipt time not supplied).
