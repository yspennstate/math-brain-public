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
VERDICT: PARTIAL proved and sharpened the finite-cell local-potential lemma in every dimension d >= 2

The round-3 Gamma positive-defect bound holds under its stated assumptions.
Its clipped-excess comparison and constants were independently re-derived;
details are in [LOG.md](LOG.md). The bounded literature check found no
verified solution of the full continuous-law problem. The September 2026
exponential strict-convexity claim remains incompletely audited.

New beyond round 3: [PROOF.md](PROOF.md) proves the finite-cell localization
step that its report left unchecked. If integrable potential increments
between neighboring labeled sites admit radius-H local approximations with
L1 error at most epsilon, independent cells on Z^d, d >= 2, admit local
potentials with increment error at most C(d,H) epsilon. Their radius is
`5H+1`, improving the planar manuscript's `10H+20`. The error constant is
explicit, independent of label count and microscopic cell size. Translation
covariance and means are preserved under the stated hypotheses.

The proof gives every finite-projection identity and every boundary-detour
step. A one-dimensional counterexample shows why a dimension restriction is
needed. Second derivations check the projection identities, clearance,
path length, and error count. No numerical computation or simulation was
needed; there are no research scripts or numerical outputs.

Commands and source access:

```sh
env OMP_NUM_THREADS=1 nice -n 15 cat ~/.claude/brain_startup.md ~/codex_op_1114r3/briefs/T050/PROOF.md
env OMP_NUM_THREADS=1 nice -n 15 cat ~/codex_op_1114r3/briefs/T050/LOG.md
env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md LOG.md
env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
```

Both prior reports and the original log were also read. File enumeration
confirmed the absence of earlier research scripts and of an original
PROOF.md. The exact web queries and useful outputs are in LOG.md. All writes
were patch-tool edits in this folder; neither prior folder was changed.

Opened primary source: OpenAI, *Strict convexity and differentiability of
the planar exponential first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Lemma 10.2, with Sections 10.3 and 15.6–15.7 read for context. No arXiv
identifier for this manuscript was verified. The opened
[scope note](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md)
excludes strict convexity from its selected formalization.

Limits and failures: this is an auxiliary theorem, not strict convexity for
any weight law. The dimension extension concerns the finite-cell lemma;
it supplies no higher-dimensional crossing-road geometry. The large error
constant is not optimized. Labelwise estimates do not justify a supremum
over arbitrarily many labels. No mathematical error was found in Lemma 10.2.
The sandbox rejected nice's priority change (`setpriority: Operation not
permitted`); shell reads nevertheless completed. No heavy program, git,
subagent, external write, or shared-memory mutation was used.

Next worker: audit Lemma 10.4's passage from individual anchor comparisons
to simultaneous envelopes over attachment occurrences. Track the number of
road labels, periods and switches as later phase meshes are refined. Then
check whether the resulting support bounds in Section 15.2 really imply
the s-independent output radius claimed in Section 15.6. Only those uniform
bounds would permit fixing D before s in Section 15.7. This report does not
verify that contraction or the manuscript's final contradiction.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 04:26:09 Asia/Tbilisi (00:26:09 UTC;
receipt time not supplied).
