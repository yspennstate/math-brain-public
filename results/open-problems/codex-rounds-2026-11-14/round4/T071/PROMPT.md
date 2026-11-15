# Open problem T071: Branching Brownian motion with selection: the Bolthausen–Sznitman genealogy of N-BBM

Statement: For N-BBM (branching Brownian motion in which, at each branching, the leftmost particle is removed to keep N particles), the genealogy on time scale (log N)³ converges to the Bolthausen–Sznitman coalescent. The Brunet–Derrida speed v_N = v_∞ − c/(log N)² + o((log N)^{−2}) is proved; see where it stands.

Source: É. Brunet and B. Derrida, Shift in the velocity of a front due to a cutoff, Phys. Rev. E 56 (1997); É. Brunet, B. Derrida, A. H. Mueller and S. Munier, Noisy traveling waves: effect of selection on genealogies, Europhys. Lett. 76 (2006)

Where it stands (checked by us, Nov 2026): Speed: proved for N-BBM (Maillard, arXiv:1304.0562, published 2016) and recovered in a time-inhomogeneous joint limit, log N ≪ T^{1/3} (Legrand–Maillard, arXiv:2402.04917 v4, Theorem 1.1(i) and Corollary 2.1); also for N-branching random walk (Bérard–Gouéré 2010) and noisy FKPP (Mueller–Mytnik–Quastel 2011). Genealogy: proved for BBM with absorption at a moving barrier (Berestycki–Berestycki–Schweinsberg 2013); for N-BBM itself it is open (the w672 audit read Legrand–Maillard in full; no genealogy theorem there).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T071 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T071 (read it,
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
VERDICT: PARTIAL exact four-lineage criterion and disjoint-merger exclusion diagnostic

The N-BBM genealogy conjecture is not proved here. The opening literature
check found no later solution. The earlier three-lineage result holds under
its stated hypotheses, by an independent pair-time reconstruction and rate
calculation recorded in [LOG.md](LOG.md).

## New beyond the earlier report

[PROOF.md](PROOF.md) extends the exact reduction to four exchangeably labelled
lineages, without assuming Markov dynamics for the finite-population
genealogies. Let S be the first merger time, H the subsequent three-block
holding time, G the two-block holding time, and D the indicator that the
two-block partition has shape 2+2. Finite-dimensional convergence to the
normalized four-label Bolthausen–Sznitman coalescent is equivalent to both
transform limits

    E exp(-s S_N-r H_N-q G_N)
      -> [1/3+2/(3(q+1))+(1+3/(q+1))/(r+2)]/(s+3),

    E[D_N exp(-s S_N-r H_N)(1-exp(-q G_N))]
      -> q/[(q+1)(s+3)(r+2)],

for all nonnegative s,r,q. The weighting removes invisible choices of binary
resolution when G_N tends to zero. The time transform alone is insufficient;
an explicit exchangeable binary counterexample is given.

One necessary consequence, for fixed positive T,h,epsilon, is

    P(S_N<=T,H_N<=h,G_N>=epsilon,D_N=1)
      -> (1-exp(-3T))(1-exp(-2h))exp(-epsilon)/6.

Sending h to zero afterward must give zero. This distinguishes disjoint-pair
bursts with a persisting two-block state from allowed quadruple bursts.

A second counterexample is consistent under restriction to arbitrary finite
label sets. It combines pair clocks of rate 1/3, all-block merger events of
rate 1/3, and fair two-color merger events of rate 2/3. Every three-label
restriction is exactly the normalized Bolthausen–Sznitman coalescent, and
the first four-label merger time is Exp(3). Nevertheless it has forbidden
disjoint-pair bursts. At time log 2 its probability of a 2+2 partition is
7/64, compared with the target 1/16: an exact difference of 3/64. Strictly
binary approximations preserve this discrepancy in their limit. These are
abstract genealogies, not N-BBM constructions.

## Verification and limitations

[AUDIT.md](AUDIT.md) independently derives the transforms from a five-state
generator, solves the forward equations, checks the root-time transform,
and checks the counterexample by exhaustive analytic coin counts and a
separate probability-flux calculation. Every displayed central constant is
derived a second way. The conditional labelling and vanishing-holding-time
cases were checked explicitly.

The attempted criterion using an unweighted shape mark was too strong:
the mark need not converge when its holding interval disappears. The
weighted criterion corrects this. The attempt to infer four-label convergence
from three-label laws fails even with restriction consistency and the correct
first four-label rate, as the counterexample demonstrates.

No N-BBM asymptotic probability, physical clock constant, admissible initial
regime, or quantitative shrinking-window rate was obtained. This is an
elementary auxiliary reduction, with no claim of literature novelty. It does
not establish convergence for arbitrary sample sizes.

## Literature and commands

The web check was confined to the first five minutes. Opened sources:

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4),
  concerning speed and front fluctuations.
- [Alexandre Legrand and Pascal Maillard,
  arXiv:2402.04917v4](https://arxiv.org/abs/2402.04917v4), whose current
  abstract and revision history concern the displacement results already
  identified in the task.
- [Jacob Mercer, arXiv:2605.04860](https://arxiv.org/abs/2605.04860), whose
  abstract concerns rank selection, hydrodynamics and velocity.
- [Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg,
  arXiv:1001.2337v3](https://arxiv.org/html/1001.2337v3), the absorption-model
  genealogy theorem and the coalescent-rate definition used here.

No qualifying later theorem was located; this is not an exhaustive negative
bibliographic result. No SOLVED_ELSEWHERE.md was created.

Shell readbacks:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l LOG.md PROOF.md AUDIT.md REPORT.md; cat AUDIT.md REPORT.md'

The sandbox rejects the requested priority change with
`nice: setpriority: Operation not permitted`. No numerical workload was run;
there are no simulation outputs or mathematical scripts. Files were written
only in this folder, and the earlier folder was read only. No git, subagents,
background tasks, or external publication.

## Next checkable step

Obtain an N-BBM-specific bound for the disjoint-pair statistic, after choosing
an explicit observation regime and rescaling. The first target is to prove
that its iterated small-h limit is zero for every fixed T,epsilon>0. This
requires controlling two separate ancestral families becoming macroscopic
within a short interval while remaining distinct for positive rescaled time.
The earlier three-label criterion alone cannot supply that control. The full
four-label result would then still require both displayed transform limits.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 01:09 Asia/Tbilisi.
