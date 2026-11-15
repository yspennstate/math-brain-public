# Open problem T071: Branching Brownian motion with selection: the Bolthausen–Sznitman genealogy of N-BBM

Statement: For N-BBM (branching Brownian motion in which, at each branching, the leftmost particle is removed to keep N particles), the genealogy on time scale (log N)³ converges to the Bolthausen–Sznitman coalescent. The Brunet–Derrida speed v_N = v_∞ − c/(log N)² + o((log N)^{−2}) is proved; see where it stands.

Source: É. Brunet and B. Derrida, Shift in the velocity of a front due to a cutoff, Phys. Rev. E 56 (1997); É. Brunet, B. Derrida, A. H. Mueller and S. Munier, Noisy traveling waves: effect of selection on genealogies, Europhys. Lett. 76 (2006)

Where it stands (checked by us, Nov 2026): Speed: proved for N-BBM (Maillard, arXiv:1304.0562, published 2016) and recovered in a time-inhomogeneous joint limit, log N ≪ T^{1/3} (Legrand–Maillard, arXiv:2402.04917 v4, Theorem 1.1(i) and Corollary 2.1); also for N-branching random walk (Bérard–Gouéré 2010) and noisy FKPP (Mueller–Mytnik–Quastel 2011). Genealogy: proved for BBM with absorption at a moving barrier (Berestycki–Berestycki–Schweinsberg 2013); for N-BBM itself it is open (the w672 audit read Legrand–Maillard in full; no genealogy theorem there).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T071 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T071 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T071 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T071 (read it, never
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
VERDICT: PARTIAL sharp propagation bound for the terminal-weighted family moment

The earlier family-moment identity and sliding-window criterion hold under
their stated hypotheses. Their independent recheck is in [LOG.md](LOG.md).
The opening literature check found no later solution of the N-BBM genealogy
problem. The conjecture remains unproved here.

## New beyond round 4

[PROOF.md](PROOF.md) controls the unequal terminal weights over a physical
future interval L. Freeze the older, middle and younger forest, and let
Q(L) be the previous report's statistic using descendants at L time units
after the younger time. Then

    E[Q(L) | frozen forest and positions] <= exp(4L) Q(0).

The older-ancestor filter is retained. The numerator is a nonnegative sum
of products of four distinct younger colors. Independent unselected Yule
trees give the bound; a separate generator calculation gives the exact
identity

    generator F = 4F - R,   R>=0,

with R explicitly equal to the loss from the selected deletions. Formula
(5) integrates this loss, identifying the correction a stronger estimate
would need to exploit.

For physical short-window length ell and remaining sampling interval L,
this extends the preceding endpoint estimate to

    3 E Q(L) <= min(1,
      12 exp(4L+2ell)(exp(ell)-1)^2 / ((N-2)(N-3))).

It yields an explicit physical-time disjoint-burst bound, formula (8),
with a quadratic short-window probability before integration.

The propagation factor is optimal uniformly over particle positions and
compatible ancestral marks. Four particles placed far right, grouped into
two middle families with different older ancestors, nearly attain exp(4L).
This holds at fixed L and in relative error for L<=(1-eta)log N.
At deterministic L_N=log(N/16), this example satisfies

    liminf_N 3 E Q(L_N) >= 3/16384,
    3 Q(0)=24/(N)_4 -> 0.

These are conditional statements for the specified separated states.
They do not assert that those states occur with positive limiting
probability in the all-zero late-time observation regime.

## Checks, failed approaches and limits

[AUDIT.md](AUDIT.md) independently checks the growth exponent by the
generator, the sample coefficients by unordered sampling, the weighted
saturation error by size-biased geometric laws, and the spatial error by
an exponential-martingale Brownian bound. It re-derives the lower bound
3/16384 a second way and checks same-color deletion, cross terms,
finite histories and deterministic observation times. No error was found.

Trying to improve the multiplicative propagation factor uniformly over
all spatial states fails: the separated-leader example saturates it.
Dropping terminal weights would also fail, as its amplification shows.
The new upper bound becomes trivial when L and ell are fixed positive
multiples of (log N)^3. No required averaged moment estimate, marked
transform limit, time constant or full genealogy convergence was obtained.
These are elementary auxiliary results, with no claim of literature novelty.

## Literature and commands

The web check was confined to approximately 07:56–07:58 Asia/Tbilisi,
under five minutes. Only opened primary sources are cited:

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4),
  Section 1.4: its spatial comparison changes the genealogy.
- [Alexandre Legrand and Pascal Maillard,
  arXiv:2402.04917](https://arxiv.org/abs/2402.04917): latest revision v4,
  9 April 2026, with displacement results in the abstract.
- [F. E. Bravo Lozano and M. C. Fittipaldi,
  arXiv:2605.28801](https://arxiv.org/abs/2605.28801): a variable-size
  logistic model, hydrodynamics and propagation speed, rather than the
  fixed-N genealogy theorem sought here.

No qualifying solution was found; this bounded search does not certify
that none exists. No SOLVED_ELSEWHERE.md was created.

All predecessor REPORT.md, LOG.md and PROOF.md files were read. Their
folders contain no mathematical scripts. Verification was analytic;
no numerical script or simulation was run. The proof readback command was

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

It returned the saved proof and 2026-11-15 08:05:41 +04. The sandbox
reported `nice: setpriority: Operation not permitted`; no numerical
workload or background job was launched. All writes stayed in this folder.
No git, subagents, external messages or predecessor edits were used.

## Next checkable step

Estimate the four-distinct-color descendant kernel after averaging over
the actual younger spatial configuration in the observation regime
tau_N=(log N)^4, a_N=(log N)^3. A bound uniform over arbitrary positions
cannot remove the exponential propagation cost. One concrete route is
to lower-bound the selection-loss integral in (5) for that random marked
configuration, or control the weighted kernel directly on a set of states
whose complement has a sufficiently small weighted contribution.

The target remains round 4's averaged off-diagonal moment with the older
filter. Even its vanishing would still leave both marked-transform limits
from round 3 and larger sample sizes.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 07:56 Asia/Tbilisi.
