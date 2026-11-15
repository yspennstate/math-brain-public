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
