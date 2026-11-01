# T353 Exact privacy of DP-SGD with shuffled batches

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 06:47 audit (status PARTLY, shuffle-mixture diagnostic)).

## STATEMENT
Repaired statement (the audit: the row must fix n, clipping and noise scaling, zero-out versus replacement adjacency, the
adaptive query class, transcript versus final model, shuffle secrecy and persistent versus fresh permutations): zero-out
adjacency, a secret fresh shuffle of n = bT records into T batches of size b, Gaussian noise of standard deviation sigma C on
each batch sum, an arbitrary adaptive sequence of unit-bounded linear queries (the ABLQ mechanism), the whole transcript
released. Prove or refute Chua et al.'s Conjecture 3.2 (2403.17673) on the worst-case pair for one epoch; multi-epoch
composition with fresh or persistent permutations is a separate extension.

## FRONTIER
- Chua, Ghazi, Kamath, Kumar, Manurangsi, Sinha arXiv:2403.17673: gap between shuffling and Poisson; lower bounds; the
  conjecture.
- Chua et al. arXiv:2411.04205: multi-epoch lower bounds for shuffled ABLQ.
- Chua, Ghazi, Harrison, Leeman, Kamath, Kumar arXiv:2412.16802: balls-and-bins sampling, privacy like Poisson.
- Annamalai et al. arXiv:2411.10614: auditing shuffled DP-SGD.
- Ertan, van Dijk arXiv:2601.10237: f-DP for one shuffled epoch with M updates: sigma >= 1/sqrt(2 ln M) or separation
  kappa >= (1/sqrt 8)(1 - 1/sqrt(4 pi ln M)).
- Audit diagnostic: the nonadaptive zero-common-record mixture P = mean_t N(e_t, sigma^2 I) vs Q = N(0, sigma^2 I) has
  D_2 = log(1 + (exp(1/sigma^2) - 1)/T); it is the known tight pair for balls-and-bins, not for adaptive shuffling.
- Open: the conjecture.

## ARCHITECTURE
In one epoch the differing record lands in exactly one batch; an adaptive adversary can set the other records' queries to
reveal which batch (through the shuffle, which is secret but correlates positions). The conjectured worst case lets the
other records' contributions identify the slot, giving a mixture over T positions with a shifted rather than zero mean.

## FAILURE POINT
Adaptivity: a dominating-pair argument must hold for every adaptive query sequence, and the shuffle's dependence between
batches defeats the product structure used for Poisson.

## SHAPE
Days for T = 2 (two batches): the worst-case pair can be computed by direct optimization over the one-dimensional query
family; weeks for general T.

## OBSTRUCTION
Adaptive dominating pairs without independence. Moves: reduce to the record's own column (the others are public up to the
permutation), then show the adversary's best adaptive strategy is non-adaptive by a convexity-in-queries argument.

## TARGETS
1. T = 2: the exact worst-case Renyi divergence of order 2 for shuffled ABLQ; compare with the conjecture.
