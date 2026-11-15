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
VERDICT: PARTIAL descendant-family criterion and a uniform short-window N-BBM bound

The earlier four-lineage result holds under its stated hypotheses. Its
reconstruction, marked density and counterexample were independently
checked in [LOG.md](LOG.md). No later solution of the N-BBM genealogy
problem was located in the opening five-minute literature check.

## New beyond the preceding report

[PROOF.md](PROOF.md) converts the disjoint-pair burst diagnostic into an
exact moment of the actual population forest, before sampling. For each
ancestor i at the older endpoint of a short interval, let

    c_i = (d_i)_2 - sum_(v descended from i) (w_v)_2,

where w_v is the number of terminal descendants of a younger ancestor v
and d_i is their sum. Group these collision increments by their ancestor z
at an additional older time, writing zeta_z for the grouped sum. Then

    Q_N(s,delta,e) = sum_(z!=z') zeta_z*zeta_z'/(N)_4

has three times its expectation equal to the probability of four separate
younger lineages becoming two pairs within delta and remaining two separate
families for another e. The older-ancestor filter preserves the persistence
condition required in the preceding report.

Let B_N(T,h,epsilon) be that report's event
{S_N<=T,H_N<=h,G_N>=epsilon,D_N=1}, and set

    A_N = 3 E Q_N(0,2h,epsilon/2)
           + (3/h) integral_0^T E Q_N(s,2h,epsilon/2) ds.

For h<epsilon/4 and sufficient recorded history, the new two-sided bound is

    P(B_N(T,h,epsilon)) <= A_N
       <= 3 P(B_N(T+2h,2h,epsilon/2)).

Thus vanishing of the averaged population moment is equivalent to the
iterated disjoint-burst exclusion. A uniform quadratic bound in delta is
sufficient. The normalized target prescribes a quadratic leading term;
the preceding counterexample instead gives a linear term and fails this
test. The endpoint term handles mergers near backward time zero.

There is also a directly proved N-BBM estimate. For every deterministic
observation time tau>=ell and every starting configuration,

    P(2+2 ancestral partition at physical lag ell)
       <= min(1,12 exp(2ell)(exp(ell)-1)^2/((N-2)(N-3))).

It follows by domination with independent unselected Yule families. For
ell<=(1/2-eta)log N, 0<eta<1/2, the bound is at most
(12+o(1))N^(-4eta). It also bounds the sampling-endpoint population moment.

The explicit observation regime used for the reduction is N particles
initially at zero, sampled at (log N)^4, with backward clock (log N)^3.
No assertion of convergence or rate normalization is made for that regime.
These are elementary auxiliary results, with no claim of literature novelty.

## Verification, failures and limits

[AUDIT.md](AUDIT.md) checks the family identity by unordered sampling and a
hand-counted eight-particle example. It re-derives the sliding-window
constants, the target calibration by both route integration and forward
equations, the Yule moment by its geometric distribution, and the constant
twelve by an independent sample count. No failure was found.

The Yule bound becomes trivial at fixed positive rescaled windows of length
h(log N)^3. For windows away from the sampling endpoint, the terminal
descendant weights are unequal and correlated with selection. Replacing
them by one gives the wrong statistic. No log-cubed-time estimate for these
weighted moments was obtained. In particular the new equivalent criterion
is not proved to vanish for N-BBM, and the genealogy conjecture remains
unproved here.

The next worker should bound the averaged off-diagonal family moment in
Proposition 2, retaining the terminal weights and older-ancestor filter.
A sufficient stronger target is (8) in PROOF.md. Establishing this exclusion
would still leave both transforms in the preceding four-lineage criterion.

## Literature and commands

Only sources opened during the bounded opening check are listed:

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4):
  Section 1.4 explains why the spatial coupling does not transfer genealogy.
- [Alexandre Legrand and Pascal Maillard, arXiv:2402.04917](https://arxiv.org/abs/2402.04917):
  latest version v4, 9 April 2026, concerning displacement.
- [Jacob Mercer, arXiv:2605.04860](https://arxiv.org/abs/2605.04860):
  rank selection, reaction-diffusion equations and velocity.
- [Julien Berestycki and Oliver Tough, arXiv:2407.05792](https://arxiv.org/abs/2407.05792):
  stationary empirical-measure selection principle.
- [Jacob Mercer, arXiv:2412.04527](https://arxiv.org/abs/2412.04527):
  critical drift and speed, not a genealogy theorem.

The search found no qualifying solution; it does not certify that none
exists. No SOLVED_ELSEWHERE.md was created.

Commands included rg --files on the two predecessor folders and direct
reads of their REPORT.md, LOG.md, PROOF.md and AUDIT.md. Neither contains
mathematical scripts. The proof was read back with

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

The output matched the saved proof; the time was 2026-11-15 04:44:05 +04.
The sandbox reported `nice: setpriority: Operation not permitted`. Only
small text reads were executed; no numerical workload, simulation or
background task was launched. This session's verification is analytic.
All writes stayed in this folder. No git, subagents, external messages or
edits to the predecessor folders.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:34 Asia/Tbilisi.
