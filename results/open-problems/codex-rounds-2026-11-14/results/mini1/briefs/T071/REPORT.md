VERDICT: PARTIAL exact three-lineage reduction and J1 obstruction

The fixed-size N-BBM genealogy conjecture remains unproved here. The bounded
opening literature search found no solution or later N-BBM genealogy theorem.

## What was proved

[PROOF.md](PROOF.md) proves an exact criterion for the three-label part of the
conjecture. Let S_N be the first sampled merger time, and H_N the interval
between the two sampled mergers, on a proposed rescaled clock. For uniformly
labelled samples with increasing available history, finite-dimensional
convergence to the normalized three-label Bolthausen–Sznitman coalescent is
equivalent to

    E exp(-s S_N-r H_N) -> (r+4)/[2(s+2)(r+1)],  s,r>=0.

The limiting first time is Exp(2), independently of a holding time with law
(1/4) delta_0+(3/4) Exp(1). In particular the conjecture requires

    lim_(h down to 0) lim_N P(S_N<=T,H_N<=h)
      = (1-exp(-2T))/4.

The proof also gives an explicit finite-grid lower bound for short intervals
between mergers. No Markov assumption on the finite-N ancestral process is
needed.

Binary finite-N genealogies cannot converge to this limit in the usual J1
topology on the finite partition space. A bounded continuous path test has
expectation difference (1-exp(-2T))/4 at every N, equal to 3/16 at T=log 2.
This concerns a stronger interpretation of convergence; it does not disprove
the intended finite-dimensional conjecture.

## Checks

[AUDIT.md](AUDIT.md) independently derives the constants using forward
equations and discounted backward equations. The joint transform also agrees
with the separately derived absorption-time density. An explicit exchangeable
binary-process counterexample shows why the two separate time marginals are
insufficient: their dependence must be checked. The audit covers finite
histories, sample labels, Brownian collisions, suppressed branches, and
vanishing intermediate holding times.

This is an elementary auxiliary reduction, not a claim of a new theorem in
the literature. No N-BBM asymptotic estimate was obtained.

## Literature checked

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4):
  Section 1.4 explicitly explains why its spatial comparison does not transfer
  genealogy.
- [Alexandre Legrand and Pascal Maillard, arXiv:2402.04917v4](https://arxiv.org/abs/2402.04917v4):
  the current abstract describes displacement results, consistent with the
  supplied audit.
- [Julien Berestycki and Oliver Tough, arXiv:2407.05792](https://arxiv.org/abs/2407.05792):
  a stationary empirical-measure selection principle.
- [Jacob Mercer, arXiv:2605.04860](https://arxiv.org/html/2605.04860v1):
  rank-based selection, hydrodynamics and velocity results.
- [Emmanuel Schertzer and Alejandro H. Wences, arXiv:2301.07762v2](https://arxiv.org/html/2301.07762v2):
  a genealogy theorem for a different model with discrete generations and
  noisy selection.
- [Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg,
  arXiv:1001.2337v3](https://arxiv.org/html/1001.2337v3):
  Theorem 3 for the absorption model explicitly uses finite-dimensional
  convergence. Section 1.3 supplies the coalescent definition used here.

Only opened sources are listed. The negative search result is not an
exhaustive certification of the literature.

## Commands and limits

The proof and audit are analytic; no simulation or computational data are
claimed. Web queries and file operations are recorded in [LOG.md](LOG.md).
The proof was read back using

    env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md

The sandbox returned `nice: setpriority: Operation not permitted`; no numerical
workload was launched. All created files stayed in this task folder.

The missing step is the displayed joint-transform limit for actual N-BBM.
The physical time constant, an admissible observation regime, a quantitative
shrinking-window rate, and samples larger than three remain unresolved.

The next worker should target the joint law of the first sampled merger time
and the interval to the second, retaining their dependence. Formula (7) in
PROOF.md gives a finite-grid necessary check before attempting the full
transform. A three-label result alone will not establish the full conjecture.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 20:50 Asia/Tbilisi.
