# Open problem T050: Strict convexity of the limit shape in first-passage percolation

Statement: For first-passage percolation on Z^d, d ≥ 2, with iid continuous edge weights satisfying E min(t_1, …, t_{2d})^d < ∞ (so that the shape theorem holds), the limit shape (the asymptotic shape of the ball of passage time t, scaled by t) is strictly convex.

Caveat: Weights with an atom at their minimum of mass above the directed-percolation threshold give flat edges (Durrett–Liggett 1981), hence the continuity assumption.

Source: H. Kesten, Aspects of first passage percolation, École d'Été de Saint-Flour XIV (Lecture Notes in Math. 1180, 1986); A. Auffinger, M. Damron and J. Hanson, 50 Years of First-Passage Percolation (AMS University Lecture Series 68, 2017)

Where it stands (checked by us, Nov 2026): The limit shape is compact and convex (Cox–Durrett 1981); examples of non-polygonal shapes (Damron–Hochman 2013). Strict convexity is unknown for every continuous distribution, including exponential weights.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T050 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T050 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T050 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T050 (read it, never
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
VERDICT: PARTIAL proved an explicit simultaneous-envelope theorem for fixed road windows

The round-4 finite-cell local-potential theorem holds under its stated
assumptions. Its projection identities, boundary clearance, radius and
error constant were independently re-derived in [LOG.md](LOG.md).
The bounded literature update found no verified solution of the full
continuous-law problem.

New beyond round 4: [PROOF.md](PROOF.md) proves the next named step,
the simultaneous-envelope passage associated with Lemma 10.4. For p
road periods and q edges of an anchor comparison tree, assume mean
period defect at most beta and mean absolute anchor increment error
at most c beta. The comparison budget is

    Lambda = [2p+c(p+q)] beta.

Local envelopes have expectation at most `(2K+1) Lambda` for trips
with at most K switches, and `3 Lambda` for physical competitors
with two signed center adjustments. These bounds hold simultaneously
over attachment occurrences, repeated visits and interior-edge points.
Their constants do not count microscopic occurrences or candidate paths.
The proof includes the measurability and spatial support of the envelopes.

A positive-edge finite-window example shows that linear growth with the
number of labels can be necessary under these hypotheses: each individual
pairwise anchor error has expectation at most 2 beta, while the maximum
switch difference among m labels equals m beta. This concerns what follows
from the estimates alone; it is not a counterexample to the canonical FPP
gauges or an error in the manuscript's fixed-label lemma.

Validation: a second interpolation identity checks the signs and the
period bound; independent counts check all coefficients. The proof tests
pauses, repeated visits, selected centers, empty competitor families,
disconnected subgraphs and common additive offsets. No numerical program
or simulation was needed.

Commands used `env OMP_NUM_THREADS=1 nice -n 15` followed by `rg --files`
on the four T050 folders or `cat` on the listed prior files and current
`PROOF.md LOG.md`. All prior reports, logs and proofs were read; file
enumeration found no prior research scripts and no original PROOF.md.
The exact web queries, source URLs, calculations and outputs are in LOG.md.

Opened primary source: OpenAI, *Strict convexity and differentiability of
the planar exponential first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Section 10.3 and Lemma 10.4, with Sections 15.6–15.7 read for scope.
No arXiv identifier was verified. The opened
[scope note](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md)
still excludes strict convexity from its selected formalization.

Failures and limits: the first PDF open failed; the landing-page link
succeeded. The sandbox denied nice's priority change; reads completed,
and no heavy program ran. No mutation outside this folder, git, subagents
or external communication occurred. Strict convexity and the contraction
remain unproved here. No error was found in the finite-window envelope
step under its explicit assumptions.

Next worker: track p, q, c and K in the actual phase-dependent constructions.
Determine which families are averaged and which are maximized as the phase
mesh is refined. Prove the needed uniform expectation and support bounds
before using the rescaling choice in Sections 15.6–15.7. The present theorem
allows that bookkeeping to be checked without counting lattice occurrences.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 07:41:24 Asia/Tbilisi (03:41:24 UTC;
receipt time not supplied).
