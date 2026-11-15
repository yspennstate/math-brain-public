# Open problem T073: Phase transition of the noisy majority vote process on Z^2

Statement: In the majority vote process on Z^2 (each site, at rate one, adopts the majority opinion of its four neighbours with probability 1 − ε and the minority with probability ε, ties broken at random), for ε small enough there are at least two distinct stationary measures.

Caveat: The exact update rule used in the literature (neighbourhood, tie-breaking) is to verify.

Source: T. M. Liggett, Interacting Particle Systems (Springer, 1985); L. F. Gray, The positive rates problem for attractive nearest neighbor spin systems on Z, Z. Wahrsch. Verw. Gebiete 61 (1982)

Where it stands (checked by us, Nov 2026): In one dimension attractive nearest-neighbour systems with positive rates are ergodic (Gray 1982). Toom's anisotropic north-east-centre rule is non-ergodic at low noise (Toom 1980). The general positive-rates conjecture fails (Gács, arXiv:math/0003117, J. Stat. Phys. 103 (2001)). On infinite regular trees the noisy majority vote process has several stationary measures at low noise: Bramson and Gray (2021) for degree at least 5, Ding and Huang (arXiv:2501.16202) for degree at least 3; De Gaspari (arXiv:2508.06935) extends this to graphs with suitable expansion. These arguments use expansion and do not reach Z^2. Open for the symmetric majority rule on Z^2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T073 (read it,
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
VERDICT: PARTIAL explicit high-noise uniqueness criterion for the stated process

For the continuous-time four-neighbor process with fair random ties, proved
uniqueness of the stationary measure whenever

\[
(2-4\varepsilon)(1-\varepsilon^3/2)<1,
\qquad 0\le\varepsilon\le1/2.
\]

Equivalently, uniqueness holds for epsilon > epsilon_*, where epsilon_* is
the unique root in [0,1/2] of
`2*epsilon^4 - epsilon^3 - 4*epsilon + 1 = 0`.
Exact rational bounds put this root between
0.248076921333012290 and 0.248076921333012735. In particular, the whole
interval [0.2481, 0.5] is covered. This slightly extends the elementary
single-neighbor influence criterion epsilon > 1/4. It does not settle the
requested low-noise coexistence statement.

The proof is in [PROOF.md](PROOF.md). In a stationary ordered coupling, a
disagreeing neighbor loses its influence if the other three neighbors have
been forced to a common spin. Decomposing according to the disagreeing
site's last update gives a lower bound `(epsilon^3/2)*d` for this event
weighted by disagreement, where d is the stationary disagreement density.
The resulting contraction forces d=0. Extremal stationary measures then
coincide, and all stationary measures coincide with them.

Reproduce the finite audit with:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

The command exits 0 and writes [audit_output.json](audit_output.json). It
checks all 81 ordered neighbor pairs and all 24 telescoping orders for each,
reconstructs the update rule independently using random three-neighbor
majorities, checks the clock integral three ways, and verifies the endpoint
and root bracket by exact rational arithmetic. At epsilon=0.2481 the
contraction factor is exactly
`4999531215835321/5000000000000000 = 0.9999062431670642`.
The successful run took below one second, used approximately 15.6 MB peak
resident memory, and ran at inherited nice 20 with one thread. On this
worker `nice -n 15` prints `setpriority: Operation not permitted` because
priority is already 20; the script verifies priority >= 15 before running.

The literature search, bounded to under ten minutes, located no solution
or substantial new rigorous advance for the exact process in the task.
This does not establish that none exists. The rule caveat matters:

- Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
  process on trees*, [arXiv:2501.16202](https://arxiv.org/html/2501.16202v1),
  Section 1.1, use synchronous updates, retained ties, and fair-resampling
  noise. These are different dynamics from the task.
- Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
  Process on Nonamenable Graphs*,
  [arXiv:2508.06935](https://arxiv.org/pdf/2508.06935), page 2 and Definition
  2.3, likewise uses a synchronous retained-tie rule and requires expansion;
  it describes the Euclidean-lattice equilibrium question as open.
- Damiano De Gaspari's 2026 thesis, *Out-of-equilibrium systems: stationary
  measures and superdiffusivity*, has an opened
  [catalog entry and abstract](https://repositum.tuwien.at/handle/20.500.12708/231354)
  placing its majority-vote results on nonamenable graphs.

Failures and limits: an initial audit run had an incorrect root-bracket
bookkeeping assertion; correcting the bracket produced the saved successful
run. A macOS address-space limit diagnostic failed; the actual audit remained
far below the memory budget. A potentially relevant Minnesota thesis PDF was
blocked with HTTP 403, so its contents were not used. The proof explicitly
checks the dependence issue in the last-ring calculation, constructs a
stationary joint coupling rather than assuming joint convergence, and covers
nontranslation-invariant stationary measures by extremal squeezing.

No result is obtained at epsilon=epsilon_*, at positive low noise, or for
the retained-tie rule. No monotonicity of the coexistence set in epsilon is
proved. The bound's novelty and its relation to the strongest published
high-noise criteria have not been established.

The next worker should first check whether this elementary last-update
bound is already subsumed by a published uniqueness criterion for this exact
rule. For a further mathematical improvement, sharpen the local bound (4)
by also using its unused slack when three or four neighbors disagree, and
seek a justified lower bound on those events from shared update histories.
Such a bound would still concern uniqueness; low-noise coexistence needs
an additional argument controlling large error clusters on Z^2.

Task: “push this problem forward by one checkable piece” — 2026-11-14,
approximately 20:51 +04 (Asia/Tbilisi).
